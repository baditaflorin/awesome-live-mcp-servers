#!/usr/bin/env python3
"""
mcp_card_importer.py (vendored; canonical: go-url-categorizer-api/scripts/import_mcp_server_cards.py) — validate MCP server cards / endpoints and upsert them into
DomainScope Postgres (domain_mcp_servers + parent domain_ai_catalog).

DomainScope's database is the source of truth; directories/exports (e.g. the
awesome-live-mcp-servers repo) must be derived FROM it, never the other way around.

Validation ("what counts as an MCP server"):
  1. GET the card; follow up to 3 redirects, incl. {"redirect": "...", "status": "308"} JSON stubs.
  2. HTTP 2xx, not text/html, parses as a JSON object.
  3. Has a server identity (serverInfo.name | name | title) AND at least one of:
     an endpoint (endpoint | transport.endpoint | remotes[].url | url), a tools list,
     or a capabilities object.
  4. Live handshake (best effort): if the endpoint is http(s) and transport is not "webmcp",
     POST JSON-RPC `initialize`. reachable = True (valid JSON-RPC result, JSON or SSE),
     False (connect error / 404 / 5xx / non-JSON-RPC 2xx), None (401/403/405/406: protected
     or unverifiable). Only cards passing 1-3 are imported; reachable records the handshake.

Usage:
  import_mcp_server_cards.py --input domains.txt|list.json --records out.json [--sql out.sql]
Input: a text file of domains (one per line; tries the standard well-known paths) or the
awesome-live-mcp-servers JSON ({"servers":[{"domain","card_url"}]}).
Nothing here talks to Postgres: it writes a SQL file you review and apply.
"""
import argparse
import concurrent.futures as cf
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

UA = "DomainScope-MCP-Verifier/1.0 (+https://domainscope.scrapetheworld.org)"
WELL_KNOWN = ["/.well-known/mcp/server-card.json", "/.well-known/mcp"]
TOOL_VERSION = "0.1.0"


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


_opener = urllib.request.build_opener(_NoRedirect)


def _get(url, timeout=8, accept="application/json"):
    """GET with manual redirect following (max 3). Returns (status, content_type, body, final_url)."""
    for _ in range(4):
        req = urllib.request.Request(url, headers={"Accept": accept, "User-Agent": UA})
        try:
            with _opener.open(req, timeout=timeout) as r:
                return r.status, r.headers.get("Content-Type", "").lower(), r.read(400_000), url
        except urllib.error.HTTPError as e:
            if e.code in (301, 302, 303, 307, 308) and e.headers.get("Location"):
                url = urllib.parse.urljoin(url, e.headers["Location"])
                continue
            return e.code, "", b"", url
        except Exception:  # DNS/TLS/timeout/reset: treat as unreachable, never abort the batch
            return 0, "", b"", url
    return 310, "", b"", url


def _first(d, *keys):
    for k in keys:
        v = d.get(k)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return ""


def parse_card(doc):
    """Return a normalized dict or None if the document is not a plausible server card."""
    if not isinstance(doc, dict):
        return None
    si = doc.get("serverInfo") if isinstance(doc.get("serverInfo"), dict) else {}
    name = _first(si, "name", "title") or _first(doc, "name", "title")
    if not name:
        return None
    transport = doc.get("transport") if isinstance(doc.get("transport"), dict) else {}
    endpoint = _first(doc, "endpoint", "url") or _first(transport, "endpoint", "url")
    if not endpoint and isinstance(doc.get("remotes"), list):
        for r in doc["remotes"]:
            if isinstance(r, dict) and _first(r, "url"):
                endpoint = _first(r, "url")
                break
    tools = doc.get("tools")
    if tools is None and isinstance(doc.get("capabilities"), dict):
        t = doc["capabilities"].get("tools")
        tools = t.get("definitions") if isinstance(t, dict) else None
    has_caps = isinstance(doc.get("capabilities"), dict)
    if not (endpoint or tools or has_caps):
        return None
    pv = doc.get("protocolVersion") or si.get("protocolVersion") or doc.get("protocol_version")
    return {
        "server_name": name[:200],
        "server_version": (_first(si, "version") or _first(doc, "version"))[:100],
        "server_title": (_first(si, "title") or _first(doc, "title"))[:200],
        "server_description": (_first(si, "description") or _first(doc, "description"))[:1000],
        "website_url": (_first(si, "websiteUrl", "website_url") or _first(doc, "websiteUrl", "website_url"))[:500],
        "endpoint": endpoint,
        "transport": (_first(transport, "type") or _first(doc, "transport"))[:40],
        "protocol_versions": [str(pv)] if pv else [],
        "tools_count": len(tools) if isinstance(tools, list) else 0,
    }


def handshake(endpoint, transport):
    """POST initialize. Returns (reachable: True/False/None, protocolVersion|None)."""
    if not endpoint.startswith(("http://", "https://")) or transport.lower() == "webmcp":
        return None, None
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
        "protocolVersion": "2025-03-26", "capabilities": {},
        "clientInfo": {"name": "domainscope-verifier", "version": TOOL_VERSION}}}).encode()
    req = urllib.request.Request(endpoint, data=body, method="POST", headers={
        "Content-Type": "application/json", "Accept": "application/json, text/event-stream", "User-Agent": UA})
    try:
        with urllib.request.build_opener().open(req, timeout=8) as r:
            raw = r.read(200_000).decode("utf-8", "replace")
            ct = r.headers.get("Content-Type", "").lower()
    except urllib.error.HTTPError as e:
        return (None if e.code in (401, 403, 405, 406) else False), None
    except Exception:
        return False, None
    if "text/event-stream" in ct:
        m = re.search(r"data:\s*(\{.*\})", raw)
        raw = m.group(1) if m else ""
    try:
        j = json.loads(raw)
    except Exception:
        return False, None
    res = j.get("result") if isinstance(j, dict) else None
    if isinstance(res, dict) and (res.get("protocolVersion") or res.get("serverInfo") or res.get("capabilities")):
        return True, res.get("protocolVersion")
    return False, None


def verify(domain, card_url=None):
    urls = [card_url] if card_url else ["https://%s%s" % (domain, p) for p in WELL_KNOWN]
    for u in urls:
        st, ct, body, final = _get(u)
        if not (200 <= st < 300) or "text/html" in ct:
            continue
        try:
            doc = json.loads(body)
        except Exception:
            continue
        if isinstance(doc, dict) and set(doc) <= {"redirect", "status"} and doc.get("redirect"):
            st, ct, body, final = _get(urllib.parse.urljoin(final, doc["redirect"]))
            if not (200 <= st < 300) or "text/html" in ct:
                continue
            try:
                doc = json.loads(body)
            except Exception:
                continue
        card = parse_card(doc)
        if not card:
            continue
        reach, pv = handshake(card["endpoint"], card["transport"])
        if pv and not card["protocol_versions"]:
            card["protocol_versions"] = [str(pv)]
        card.update(domain=domain.lower(), server_card_url=final[:1000], identifier=final[:1000],
                    mcp_endpoint_reachable=reach)
        return card
    return None


def load_inputs(path):
    txt = open(path).read()
    if txt.lstrip().startswith("{") or txt.lstrip().startswith("["):
        d = json.loads(txt)
        items = d["servers"] if isinstance(d, dict) else d
        return [(x["domain"], x.get("card_url")) for x in items if x.get("domain")]
    return [(l.strip(), None) for l in txt.splitlines() if l.strip() and not l.startswith("#")]


def q(s):
    return "'" + str(s).replace("\x00", "").replace("'", "''") + "'"


def to_sql(recs):
    def arr(a):
        return "ARRAY[%s]::text[]" % ",".join(q(x) for x in a) if a else "ARRAY[]::text[]"
    vals = []
    for r in recs:
        vals.append("(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % (
            q(r["domain"]), q(r["identifier"]), q(r["server_name"]),
            q(r["server_version"]) if r["server_version"] else "NULL",
            q(r["server_title"]) if r["server_title"] else "NULL",
            q(r["server_description"]) if r["server_description"] else "NULL",
            q(r["server_card_url"]), q(r["website_url"]) if r["website_url"] else "NULL",
            arr(r["protocol_versions"]),
            {True: "true", False: "false", None: "NULL"}[r["mcp_endpoint_reachable"]]))
    return f"""BEGIN;
CREATE TEMP TABLE _mcp_import (domain text, identifier text, server_name text, server_version text,
  server_title text, server_description text, server_card_url text, website_url text,
  protocol_versions text[], mcp_endpoint_reachable boolean) ON COMMIT DROP;
INSERT INTO _mcp_import VALUES
{",\n".join(vals)};
INSERT INTO domain_mcp_servers (domain_id, identifier, server_name, server_version, server_title,
  server_description, server_card_url, website_url, protocol_versions, mcp_endpoint_reachable)
SELECT d.id, i.identifier, i.server_name, i.server_version, i.server_title, i.server_description,
       i.server_card_url, i.website_url, i.protocol_versions, i.mcp_endpoint_reachable
  FROM _mcp_import i JOIN domains d ON d.name = i.domain
ON CONFLICT (domain_id, identifier) DO UPDATE SET
  server_name = EXCLUDED.server_name, server_version = EXCLUDED.server_version,
  server_title = EXCLUDED.server_title, server_description = EXCLUDED.server_description,
  server_card_url = EXCLUDED.server_card_url, website_url = EXCLUDED.website_url,
  protocol_versions = EXCLUDED.protocol_versions,
  mcp_endpoint_reachable = EXCLUDED.mcp_endpoint_reachable, last_seen = CURRENT_TIMESTAMP;
-- Parent rows: create for domains without one (has_ai_catalog=false: this is a server card, not a
-- catalog); for existing rows refresh only the MCP columns, never has_ai_catalog/artifact counts.
INSERT INTO domain_ai_catalog (domain_id, has_ai_catalog, discovery_source, ai_artifact_count,
  mcp_server_count, a2a_agent_count, nested_catalog_count, mcp_endpoint_reachable, mcp_server_names,
  tool_name, tool_version, last_checked_at, status, updated_at)
SELECT s.domain_id, false, 'mcp_server_card', 0, COUNT(*), 0, 0, bool_or(s.mcp_endpoint_reachable),
       array_agg(s.server_name ORDER BY s.id), 'mcp-card-import', '{TOOL_VERSION}',
       CURRENT_TIMESTAMP, 1, CURRENT_TIMESTAMP
  FROM domain_mcp_servers s
 WHERE s.domain_id IN (SELECT d.id FROM _mcp_import i JOIN domains d ON d.name = i.domain)
 GROUP BY s.domain_id
ON CONFLICT (domain_id) DO UPDATE SET
  mcp_server_count = EXCLUDED.mcp_server_count, mcp_server_names = EXCLUDED.mcp_server_names,
  mcp_endpoint_reachable = EXCLUDED.mcp_endpoint_reachable, updated_at = CURRENT_TIMESTAMP;
COMMIT;
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", required=True)
    ap.add_argument("--records", required=True)
    ap.add_argument("--sql")
    ap.add_argument("--workers", type=int, default=60)
    a = ap.parse_args()
    items = load_inputs(a.input)
    def safe(t):
        try:
            return verify(*t)
        except Exception:
            return None
    with cf.ThreadPoolExecutor(a.workers) as ex:
        res = list(ex.map(safe, items))
    recs = [r for r in res if r]
    json.dump(recs, open(a.records, "w"))
    reach = {True: 0, False: 0, None: 0}
    for r in recs:
        reach[r["mcp_endpoint_reachable"]] += 1
    print("checked=%d validated=%d handshake_ok=%d handshake_failed=%d unverifiable=%d" % (
        len(items), len(recs), reach[True], reach[False], reach[None]))
    if a.sql:
        open(a.sql, "w").write(to_sql(recs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
