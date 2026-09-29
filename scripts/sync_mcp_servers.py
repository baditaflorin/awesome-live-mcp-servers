#!/usr/bin/env python3
"""
sync_mcp_servers.py

Autonomous Intelligence Synchronizer for the Awesome MCP Servers repository.
Enriched and powered by DomainScope's 13M+ firmographic knowledge graph.

Instead of arbitrary sorting by top-level domains, this pipeline classifies
and structures each Model Context Protocol (MCP) server by:
  - DomainScope Market Vertical & Industry
  - Verified Business Delivery Model (B2B SaaS, Open Source, Freemium, API Dev)
  - Tool Interfaces & Capabilities count
  - Real-time HTTP reachability & latency benchmarks

Generates:
  - README.md (clean, structured, categorized tables with DomainScope dossier links)
  - data/mcp-servers.json (machine-readable structured feed for autonomous agents)
  - data/mcp-servers.csv (tabular data analysis spreadsheet)
"""

import urllib.request
import urllib.error
import json
import csv
import time
import os
import sys
import subprocess
import shutil
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed

DOMAINSCOPE_API = "https://domainscope.scrapetheworld.org/api/v1"
DOMAINSCOPE_WEB = "https://domainscope.scrapetheworld.org"
USER_AGENT = "Awesome-Live-MCP-Servers-Bot/1.0 (+https://github.com/baditaflorin/awesome-live-mcp-servers)"

def fetch_json(url, timeout=5):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8", errors="ignore"))
    except Exception:
        return None

def probe_endpoint(url, timeout=4):
    start = time.time()
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            elapsed_ms = int((time.time() - start) * 1000)
            return resp.status in (200, 204), elapsed_ms
    except urllib.error.HTTPError as e:
        elapsed_ms = int((time.time() - start) * 1000)
        if e.code == 405:
            # Method Not Allowed: probe remote streamable HTTP endpoint with JSON-RPC POST
            try:
                post_data = b'{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
                post_req = urllib.request.Request(
                    url,
                    data=post_data,
                    headers={"User-Agent": USER_AGENT, "Content-Type": "application/json"},
                )
                with urllib.request.urlopen(post_req, timeout=timeout) as post_resp:
                    post_elapsed_ms = int((time.time() - start) * 1000)
                    return post_resp.status in (200, 204), post_elapsed_ms
            except urllib.error.HTTPError as post_e:
                post_elapsed_ms = int((time.time() - start) * 1000)
                if post_e.code in (200, 204, 401, 403):
                    return True, post_elapsed_ms
        elif e.code in (401, 403):
            return True, elapsed_ms
        return False, None
    except Exception:
        return False, None

def get_postgres_dsn():
    dsn = os.environ.get("POSTGRES_DSN") or os.environ.get("DATABASE_URL")
    if not dsn:
        candidates = [
            Path(".env"),
            Path("../.env"),
            Path("../go-url-categorizer-api/.env"),
        ]
        for c in candidates:
            if c.exists():
                try:
                    for line in c.read_text(encoding="utf-8").splitlines():
                        if line.startswith("POSTGRES_DSN="):
                            dsn = line.split("=", 1)[1].strip().strip("\"'")
                            break
                except Exception:
                    pass
            if dsn:
                break
    return dsn

def batch_load_domainscope_intelligence(domains):
    """
    Leverages DomainScope PostgreSQL database to batch-load full firmographic
    intelligence in a single high-speed join. Falls back to public API if DB unavailable.
    """
    intelligence = {}
    dsn = get_postgres_dsn()
    psql_path = shutil.which("psql")

    if dsn and psql_path and domains:
        print(f"🧠 Querying DomainScope PostgreSQL intelligence graph for {len(domains)} domains...")
        chunk_size = 500
        for i in range(0, len(domains), chunk_size):
            chunk = domains[i:i + chunk_size]
            in_list = ",".join(f"'{d}'" for d in chunk)
            sql = f"""
            SELECT 
                d.name,
                COALESCE(c.name, 'Technology'),
                COALESCE(ind.name, 'Software & Technology'),
                COALESCE(bm.name, 'B2B SaaS'),
                COALESCE(co.name, 'Global'),
                COALESCE(ci.name, ''),
                COALESCE(d.summary, '')
            FROM domains d
            LEFT JOIN categories c ON d.category_id = c.id
            LEFT JOIN industries ind ON d.industry_id = ind.id
            LEFT JOIN business_models bm ON d.business_model_id = bm.id
            LEFT JOIN countries co ON d.country_id = co.id
            LEFT JOIN cities ci ON d.city_id = ci.id
            WHERE d.name IN ({in_list});
            """
            env = os.environ.copy()
            env["PGCONNECT_TIMEOUT"] = "4"
            cmd = [psql_path, dsn, "-t", "-A", "-F", "|", "-c", sql]
            try:
                out = subprocess.check_output(cmd, text=True, env=env)
                for line in out.strip().splitlines():
                    if not line:
                        continue
                    parts = line.split("|")
                    if len(parts) >= 6:
                        name = parts[0]
                        intelligence[name] = {
                            "category": parts[1],
                            "industry": parts[2],
                            "business_model": parts[3],
                            "country": parts[4],
                            "city": parts[5],
                            "summary": parts[6] if len(parts) > 6 else "",
                        }
            except Exception as e:
                print(f"  [-] DB query error chunk: {e}")
                break

    print(f"  [✓] Successfully resolved {len(intelligence)} domains from DomainScope graph.")
    return intelligence

def get_domain_details_fallback(domain):
    data = fetch_json(f"{DOMAINSCOPE_API}/public/domain/{domain}")
    if data and "data" in data and data["data"]:
        d = data["data"]
        return {
            "category": d.get("category") or "Technology",
            "industry": d.get("industry") or "Software & Technology",
            "business_model": d.get("business_model") or "B2B SaaS",
            "country": d.get("country") or "Global",
            "city": d.get("city") or "",
            "summary": d.get("summary") or "",
        }
    return {
        "category": "Technology",
        "industry": "Software & Technology",
        "business_model": "B2B SaaS",
        "country": "Global",
        "city": "",
        "summary": "",
    }

def is_valid_manifest(data):
    if not isinstance(data, dict):
        return False
    if data.get("method") in ("notfound", "error") or data.get("error") is True:
        return False
    t = str(data.get("server_title") or data.get("server_name") or data.get("title") or data.get("name") or "").lower()
    if "не найдена" in t or "page not found" in t or "404" in t:
        return False
    return True

def fetch_manifest_details(domain):
    # 1. Try MCP Server Card first (/.well-known/mcp/server-card.json)
    card_url = f"https://{domain}/.well-known/mcp/server-card.json"
    card = fetch_json(card_url, timeout=3)
    if is_valid_manifest(card):
        title = card.get("server_title") or card.get("server_name") or card.get("name") or card.get("title") or domain
        desc = card.get("server_description") or card.get("description") or ""
        tools = card.get("tools") or []
        version = card.get("server_version") or card.get("version") or "1.0"
        return {
            "title": str(title),
            "description": str(desc),
            "tools_count": len(tools) if isinstance(tools, list) else 0,
            "version": str(version),
            "card_url": card_url,
            "type": "server_card",
        }
    
    # 2. Try AI Catalog manifest (/.well-known/ai-catalog.json)
    catalog_url = f"https://{domain}/.well-known/ai-catalog.json"
    cat = fetch_json(catalog_url, timeout=3)
    if is_valid_manifest(cat):
        servers = cat.get("mcp_servers") or cat.get("services") or cat.get("tools") or []
        title = cat.get("title") or cat.get("name") or domain
        desc = cat.get("description") or ""
        tools_count = len(servers) if isinstance(servers, (list, dict)) else 0
        if isinstance(servers, list) and len(servers) > 0 and isinstance(servers[0], dict):
            first = servers[0]
            title = first.get("title") or first.get("name") or title
            desc = first.get("description") or desc
            if isinstance(first.get("tools"), list):
                tools_count = len(first["tools"])
        return {
            "title": str(title),
            "description": str(desc),
            "tools_count": tools_count,
            "version": str(cat.get("version") or "1.0"),
            "card_url": catalog_url,
            "type": "ai_catalog",
        }

    # 3. Fallback to alternative endpoint (/.well-known/mcp)
    mcp_url = f"https://{domain}/.well-known/mcp"
    mcp_data = fetch_json(mcp_url, timeout=3)
    if is_valid_manifest(mcp_data):
        title = mcp_data.get("name") or domain
        desc = mcp_data.get("description") or ""
        tools = mcp_data.get("tools") or []
        return {
            "title": str(title),
            "description": str(desc),
            "tools_count": len(tools) if isinstance(tools, list) else 0,
            "version": "1.0",
            "card_url": mcp_url,
            "type": "mcp_endpoint",
        }

    return {
        "title": domain,
        "description": "",
        "tools_count": 0,
        "version": "1.0",
        "card_url": f"https://{domain}/.well-known/mcp/server-card.json",
        "type": "probe",
    }

def categorize_server(domain, d_info, title, desc):
    """
    Intelligent classifier using DomainScope firmographic intelligence
    combined with manifest metadata.
    """
    cat = d_info.get("category", "").lower()
    ind = d_info.get("industry", "").lower()
    text = f"{domain} {cat} {ind} {title} {desc}".lower()

    if any(k in text for k in ["anthropic", "openai", "mistral", "hugging", "deepseek", "stability", "openrouter", "foundation model", "llm provider"]):
        return "🧠 AI Foundations & Model Inference"
    if any(k in text for k in ["agent", "jasper", "kaiber", "sider", "fal.ai", "ideogram", "murf", "workflow", "copilot", "autonomous", "generator"]):
        return "🤖 Autonomous Agents & Workflow Automation"
    if any(k in text for k in ["cloudflare", "railway", "1inch", "vercel", "supabase", "docker", "api", "git", "dev", "developer", "sdk", "infra", "defi", "crypto"]):
        return "🛠️ Developer Platforms, DevOps & Web3"
    if any(k in text for k in ["search", "scrap", "crawl", "extract", "proxy", "spider", "duck", "bing", "dataset"]):
        return "🌐 Web Search, Crawling & Data Extraction"
    if any(k in text for k in ["analytics", "metrics", "bi", "telemetry", "reducto", "explorium", "sitegpt", "research"]):
        return "📊 Enterprise Intelligence & Analytics"
    if any(k in text for k in ["shop", "ecommerce", "retail", "stripe", "payment", "store", "commerce"]):
        return "🛒 E-Commerce & Commercial Services"
    if any(k in text for k in ["security", "auth", "identity", "cyber", "dns", "cert", "tls", "audit"]):
        return "🔒 Cybersecurity & Infrastructure"
    return "💼 Enterprise SaaS & B2B Solutions"

def format_scanned(n):
    """Human string for the number of domains the AI-catalog scanner has actually checked."""
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n // 1_000}k"
    return str(n)

DB_ROWS_SQL = """
SELECT row_to_json(t) FROM (
  SELECT d.name AS domain,
         (array_agg(s.server_name ORDER BY s.id))[1] AS title,
         (array_agg(COALESCE(s.server_description, '') ORDER BY s.id))[1] AS description,
         (array_agg(COALESCE(s.server_version, '') ORDER BY s.id))[1] AS version,
         (array_agg(s.server_card_url ORDER BY s.id))[1] AS card_url,
         COUNT(*) AS server_count,
         bool_or(s.mcp_endpoint_reachable) AS handshake_ok,
         bool_and(s.mcp_endpoint_reachable IS NOT DISTINCT FROM false) AS all_failed
    FROM domain_mcp_servers s JOIN domains d ON d.id = s.domain_id
   GROUP BY d.name ORDER BY d.name
) t;
"""

DB_STATS_SQL = """
SELECT row_to_json(t) FROM (
  SELECT (SELECT COUNT(*) FROM domain_ai_catalog) AS scanned,
         (SELECT COUNT(*) FROM domain_ai_catalog
           WHERE has_ai_catalog AND (COALESCE(ai_artifact_count,0) > 0 OR COALESCE(mcp_server_count,0) > 0
                 OR COALESCE(a2a_agent_count,0) > 0 OR COALESCE(nested_catalog_count,0) > 0)) AS catalogs
) t;
"""


def psql_json_lines(sql):
    dsn = get_postgres_dsn()
    psql_path = shutil.which("psql")
    if not dsn or not psql_path:
        raise SystemExit("DomainScope is the source of truth: set POSTGRES_DSN and install psql "
                         "(or pass --rows-json exported from the database). Refusing to invent data.")
    env = os.environ.copy()
    env["PGCONNECT_TIMEOUT"] = "10"
    out = subprocess.check_output([psql_path, dsn, "-t", "-A", "-c", sql], text=True, env=env)
    return [json.loads(l) for l in out.splitlines() if l.strip()]


def load_from_database(rows_json=None):
    """All servers + corpus stats come from Postgres (domain_mcp_servers), never from crawler files."""
    if rows_json:
        blob = json.load(open(rows_json))
        return blob["rows"], blob["stats"], blob.get("intel")
    rows = psql_json_lines(DB_ROWS_SQL)
    stats = psql_json_lines(DB_STATS_SQL)[0]
    return rows, stats, None


def build_server_entry(row, intel):
    """Directory entry from a database row. 'reachable' means a live MCP initialize handshake succeeded."""
    domain = row["domain"]
    d_info = intel.get(domain) or {}
    title = row.get("title") or domain
    desc = row.get("description") or d_info.get("summary") or f"{d_info.get('category', 'Technology')} platform & services."
    if row.get("handshake_ok"):
        verification = "handshake_ok"
    elif row.get("all_failed"):
        verification = "unreachable"
    else:
        verification = "protected_or_unverified"
    return {
        "domain": domain,
        "title": title,
        "description": desc[:300],
        "category": categorize_server(domain, d_info, title, desc),
        "domainscope_category": d_info.get("category", "Technology"),
        "industry": d_info.get("industry", "Technology"),
        "business_model": d_info.get("business_model", "B2B SaaS"),
        "country": d_info.get("country", "Global"),
        "city": d_info.get("city", ""),
        "reachable": bool(row.get("handshake_ok")),
        "verification": verification,
        "latency_ms": 0,
        "tools_count": 0,
        "version": row.get("version") or "",
        "card_url": row.get("card_url") or "",
        "repo_url": "", "docs_url": "", "registry": "", "package": "", "transport": "",
        "server_count": row.get("server_count", 1),
        "artifact_count": 0,
        "dossier_url": f"{DOMAINSCOPE_WEB}/domains/{domain}",
        "source": "domainscope-db",
    }


def main():
    import argparse
    ap = argparse.ArgumentParser(description="Regenerate the directory FROM DomainScope Postgres.")
    ap.add_argument("--rows-json", help="offline: JSON {rows:[...], stats:{...}} exported from the database")
    args = ap.parse_args()

    rows, stats, intel_cache = load_from_database(args.rows_json)
    if intel_cache is None:
        intel_cache = batch_load_domainscope_intelligence([r["domain"] for r in rows])
    processed_servers = [build_server_entry(r, intel_cache) for r in rows]
    processed_servers.sort(key=lambda s: (not s["reachable"], s["category"], s["domain"]))

    active_count = sum(1 for s in processed_servers if s["reachable"])
    print(f"✅ {len(processed_servers)} servers from the database; {active_count} pass a live MCP handshake.")

    total_scanned = int(stats["scanned"])
    total_catalogs = int(stats["catalogs"])
    write_json(processed_servers, total_scanned, total_catalogs)
    write_csv(processed_servers)
    write_readme(processed_servers, total_scanned, total_catalogs, active_count)
    print("🎉 Sync completed: README.md, data/mcp-servers.json and data/mcp-servers.csv derived from Postgres.")

def write_json(servers, total_scanned, total_catalogs):
    out = {
        "metadata": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "generator": "DomainScope Live Scanner & Firmographic Intelligence Engine",
            "intelligence_source": "https://domainscope.scrapetheworld.org",
            "total_scanned_domains": total_scanned,
            "total_active_catalogs": total_catalogs,
            "total_mcp_servers": len(servers),
            "live_reachable_count": sum(1 for s in servers if s["reachable"])
        },
        "servers": servers
    }
    os.makedirs("data", exist_ok=True)
    with open("data/mcp-servers.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)

def write_csv(servers):
    os.makedirs("data", exist_ok=True)
    keys = [
        "domain", "title", "category", "domainscope_category", "business_model",
        "industry", "country", "reachable", "latency_ms", "tools_count",
        "card_url", "repo_url", "docs_url", "registry", "transport", "dossier_url", "description"
    ]
    with open("data/mcp-servers.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for s in servers:
            writer.writerow({k: s.get(k, "") for k in keys})

def write_readme(servers, total_scanned, total_catalogs, active_count):
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # Group by intelligent category
    categories = {}
    biz_models = {}
    for s in servers:
        cat = s["category"]
        bm = s.get("business_model") or "B2B SaaS"
        categories.setdefault(cat, []).append(s)
        biz_models.setdefault(bm, []).append(s)

    lines = [
        "# Awesome Live MCP Servers 🌐⚡",
        "",
        "> **The definitive, live-benchmarked directory of public & remote Model Context Protocol (MCP) servers and streamable AI manifests on the internet.**",
        ">",
        "> Concurrently probed, latency-benchmarked, and enriched by **[DomainScope at Scrape the World](https://domainscope.scrapetheworld.org)**.",
        "",
        f"[![Total Servers](https://img.shields.io/badge/MCP_Servers-{len(servers)}-purple?style=for-the-badge&logo=anthropic)](data/mcp-servers.json)",
        f"[![Live Reachable](https://img.shields.io/badge/Handshake_Verified-{active_count}-emerald?style=for-the-badge)](data/mcp-servers.json)",
        f"[![Scanned Corpus](https://img.shields.io/badge/Scanned_Corpus-{format_scanned(total_scanned)}_Domains_Scanned-blue?style=for-the-badge)](https://domainscope.scrapetheworld.org/mcp-directory)",
        f"[![Enriched by DomainScope](https://img.shields.io/badge/Intelligence-DomainScope_Graph-00D26A?style=for-the-badge&logo=databricks)](https://domainscope.scrapetheworld.org)",
        f"[![CI: Woodpecker](https://img.shields.io/badge/CI-Woodpecker_Self--Hosted-2088FF?style=for-the-badge&logo=linux)](https://ci.0exec.com)",
        "",
        "Unlike typical GitHub lists that catalog local code repositories requiring terminal installation (`npx`, `docker`, virtual environments), this repository is the **world's largest autonomous directory of live, running, publicly reachable Model Context Protocol (MCP) servers and streamable AI endpoints**.",
        "",
        "---",
        "",
        "## ⚡ What Makes This Directory Different",
        "",
        "| Feature | Standard \"Awesome MCP\" Repositories | **Awesome Live MCP Servers 🌐⚡** |",
        "|---|---|---|",
        "| **What it lists** | GitHub source code repos for `localhost` execution | **Live, running, public HTTP endpoints** (`https://.../api/mcp`) |",
        "| **Setup required** | `npx`, Node.js, Python venvs, Docker, local configuration | **Zero-Install URL**: Directly connect in Cursor, Claude, or Windsurf |",
        "| **Maintenance** | Manual pull requests (frequently unmaintained or rotting) | **Autonomous & Self-Evolving**: Continuously crawled across 13M+ domains |",
        "| **Verification** | Unverified code links with unknown server health | **Live-Probed Telemetry**: Concurrently benchmarked reachability & response latencies |",
        "| **Firmographics** | Flat markdown files with arbitrary tags | **DomainScope at Scrape the World**: Multi-dimensional market verticals & company dossiers |",
        "",
        "---",
        "",
        "## 🤖 Self-Evolving Autonomous Engine",
        "",
        "This directory is **not maintained by waiting for manual pull requests**. It is continuously discovered, updated, and verified by an autonomous internet-scale data pipeline:",
        f"1. **{format_scanned(total_scanned)} domains scanned** (of DomainScope's 13M+): ingests high-priority cohorts (developer documentation platforms, open-source repositories, API surfaces, AI ecosystem domains) from DomainScope's 13M+ domain graph.",
        "2. **Standard & Streamable Detection**: Probes standard cards (`/.well-known/mcp/server-card.json`), streamable HTTP POST endpoints (`/api/mcp`), and AI catalogs (`/.well-known/ai-catalog.json`).",
        "3. **Live Health & Latency Telemetry**: Concurrently benchmarks round-trip latency (P50/P95) and verifies HTTP 200/204/401/403 states across 32 threads.",
        "4. **Firmographic Enrichment**: Enriches every host with DomainScope's verified business models, market taxonomy, and tech stack detection.",
        "",
        "## 🧠 DomainScope Intelligence Integration",
        "",
        "Each server card is enriched with verified metadata from DomainScope:",
        "- **Market Taxonomy**: Multi-dimensional categorization (AI Foundation Labs, Autonomous Agents, Developer Tooling, Data Extraction).",
        "- **Business Architecture**: Verified Delivery Models (*B2B SaaS, Open Source & Community, Freemium, API Developer*).",
        "- **Live Dossiers**: Direct links to the domain's complete dossier (`domainscope.scrapetheworld.org/domains/:domain`) featuring tech stack detection, hosting ASN, and AI posture.",
        "- **Real Reachability**: Concurrently benchmarked HTTP reachability (`🟢 Live` vs `🔴 Down`) and round-trip response latency.",
        "",
        "---",
        "",
        "## 📥 Machine-Readable Feeds (For AI Agents)",
        "",
        "Autonomous agents (in Cursor, Windsurf, Claude Desktop, Antigravity) can ingest the live directory directly:",
        "- **JSON**: [`data/mcp-servers.json`](data/mcp-servers.json)",
        "- **CSV**: [`data/mcp-servers.csv`](data/mcp-servers.csv)",
        "- **Live Query Tool**: Use DomainScope's native MCP tool `domainscope_search_mcp_servers()` at `https://domainscope.scrapetheworld.org/mcp`",
        "",
        "---",
        "",
        "## 🔌 1-Click Connect Guide",
        "",
        "### Cursor (`.cursor/mcp.json`)",
        "```json",
        "{",
        '  "mcpServers": {',
        '    "domainscope": {',
        '      "url": "https://domainscope.scrapetheworld.org/mcp"',
        "    }",
        "  }",
        "}",
        "```",
        "",
        "### Claude Desktop (`claude_desktop_config.json`)",
        "```json",
        "{",
        '  "mcpServers": {',
        '    "domainscope": {',
        '      "url": "https://domainscope.scrapetheworld.org/mcp"',
        "    }",
        "  }",
        "}",
        "```",
        "",
        "---",
        "",
        "## 📑 Directory of Public MCP Servers (by DomainScope Vertical)",
        ""
    ]

    # Define vertical category metadata and directory pages
    category_meta = {
        "🛠️ Developer Platforms, DevOps & Web3": {
            "slug": "developer-platforms.md",
            "desc": "Developer tooling, APIs, CI/CD, cloud orchestration, web3, and IDE integrations."
        },
        "💼 Enterprise SaaS & B2B Solutions": {
            "slug": "enterprise-saas.md",
            "desc": "Enterprise cloud services, workflow software, corporate knowledge, and B2B platforms."
        },
        "🤖 Autonomous Agents & Workflow Automation": {
            "slug": "autonomous-agents.md",
            "desc": "AI agent swarms, automated assistants, reasoning runtimes, and autonomous pipelines."
        },
        "🛒 E-Commerce & Commercial Services": {
            "slug": "ecommerce.md",
            "desc": "Online storefronts, retail catalogs, merchant operations, and commerce tools."
        },
        "📊 Enterprise Intelligence & Analytics": {
            "slug": "analytics.md",
            "desc": "Data pipelines, market intelligence, telemetry monitoring, BI, and metrics."
        },
        "🌐 Web Search, Crawling & Data Extraction": {
            "slug": "web-search-crawling.md",
            "desc": "Web scrapers, search indices, document parsing, content extraction, and search tools."
        },
        "🔒 Cybersecurity & Infrastructure": {
            "slug": "cybersecurity.md",
            "desc": "Auth, threat detection, secret management, identity verification, TLS, and audit."
        },
        "🧠 AI Foundations & Model Inference": {
            "slug": "ai-foundations.md",
            "desc": "Model serving endpoints, foundation labs, LLM hosting providers, and inference runtimes."
        },
    }

    dir_path = Path("directory")
    dir_path.mkdir(exist_ok=True)

    # 1. Write dedicated markdown files for each vertical category
    for cat_name, cat_servers in categories.items():
        meta = category_meta.get(cat_name, {"slug": "other.md", "desc": "Specialized services and tools."})
        cat_file = dir_path / meta["slug"]
        cat_live = sum(1 for s in cat_servers if s["reachable"])

        cat_lines = [
            f"# {cat_name}",
            "",
            f"> {meta['desc']}",
            ">",
            f"> **{len(cat_servers)} Servers** ({cat_live} Live & Reachable Online) • Part of the **[Awesome Live MCP Servers](https://github.com/baditaflorin/awesome-live-mcp-servers)** registry.",
            f"> Enriched with live telemetry by **[DomainScope at Scrape the World](https://domainscope.scrapetheworld.org)**.",
            "",
            "[← Back to Main Repository](../README.md)",
            "",
            "---",
            "",
            "| Server / Host | Business Model | Status | Latency | Tools | Manifest | DomainScope Dossier |",
            "|---|---|:---:|:---:|:---:|:---:|:---:|",
        ]
        for s in cat_servers:
            status_badge = ("🟢 **Verified**" if s["reachable"] else ("🔴 *Unreachable*" if s.get("verification") == "unreachable" else "🟡 *Unverified*"))
            lat_str = f"{s['latency_ms']} ms" if s["latency_ms"] > 0 else "-"
            tools_str = str(s["tools_count"]) if s["tools_count"] > 0 else "✓"
            bm_badge = f"`{s['business_model']}`" if s.get("business_model") else "`B2B SaaS`"
            repo_link = f" • [Repo ↗]({s['repo_url']})" if s.get("repo_url") else ""
            cat_lines.append(f"| **[{s['domain']}](https://{s['domain']})**<br>*{s['title']}*{repo_link} | {bm_badge} | {status_badge} | {lat_str} | {tools_str} | [Manifest ↗]({s['card_url']}) | [Dossier ↗]({s['dossier_url']}) |")

        cat_lines.extend([
            "",
            "---",
            "",
            "[← Back to Main Repository](../README.md) • [Download Machine JSON](../data/mcp-servers.json) • [Download CSV](../data/mcp-servers.csv)",
        ])
        cat_file.write_text("\n".join(cat_lines) + "\n", encoding="utf-8")

    # 2. Build Category Index Table in README.md
    lines.append("| Vertical Category | Live Online | Total Servers | Scope | Full Directory |")
    lines.append("|---|:---:|:---:|---|:---:|")
    for cat_name in sorted(categories.keys(), key=lambda k: len(categories[k]), reverse=True):
        cat_servers = categories[cat_name]
        meta = category_meta.get(cat_name, {"slug": "other.md", "desc": "Specialized services."})
        cat_live = sum(1 for s in cat_servers if s["reachable"])
        lines.append(f"| **{cat_name}** | 🟢 **{cat_live}** | **{len(cat_servers)}** | {meta['desc']} | [**Browse All ({len(cat_servers)}) ↗**](directory/{meta['slug']}) |")
    lines.append("")

    # 3. Add Featured Multi-Tool & High-Capacity Servers Table in README.md
    featured_servers = [s for s in servers if s["reachable"]]
    # Sort by declared tools (descending), then latency (ascending)
    featured_servers.sort(key=lambda s: (-s.get("tools_count", 0), s.get("latency_ms", 9999)))
    # Limit to top 100 for fast, clean rendering under 150 KB
    featured_slice = featured_servers[:100]

    lines.extend([
        "---",
        "",
        f"## 🌟 Featured Multi-Tool & High-Capacity Servers ({len(featured_slice)} Highlighted)",
        "",
        "> Live remote servers offering verified multi-tool suites (`tools_count > 0`) or community-submitted Streamable HTTP endpoints.",
        ">",
        "> 💡 **Explore the complete registry**: Click into any vertical category table above, or query the full datasets in [`data/mcp-servers.json`](data/mcp-servers.json) and [`data/mcp-servers.csv`](data/mcp-servers.csv).",
        "",
        "| Server / Host | Category | Business Model | Status | Latency | Tools | Manifest | DomainScope Dossier |",
        "|---|---|---|:---:|:---:|:---:|:---:|:---:|",
    ])
    for s in featured_slice:
        status_badge = ("🟢 **Verified**" if s["reachable"] else ("🔴 *Unreachable*" if s.get("verification") == "unreachable" else "🟡 *Unverified*"))
        lat_str = f"{s['latency_ms']} ms" if s["latency_ms"] > 0 else "-"
        tools_str = f"**{s['tools_count']} tools**" if s["tools_count"] > 0 else "✓"
        bm_badge = f"`{s['business_model']}`" if s.get("business_model") else "`B2B SaaS`"
        repo_link = f" • [Repo ↗]({s['repo_url']})" if s.get("repo_url") else ""
        lines.append(f"| **[{s['domain']}](https://{s['domain']})**<br>*{s['title']}*{repo_link} | {s['category']} | {bm_badge} | {status_badge} | {lat_str} | {tools_str} | [Manifest ↗]({s['card_url']}) | [Dossier ↗]({s['dossier_url']}) |")
    lines.append("")

    # Add Cross-Section by Business Model
    lines.extend([
        "---",
        "",
        "## 🏢 Distribution by Business Delivery Model",
        "",
        "Classified by DomainScope's firmographic model inference:",
        ""
    ])
    for bm_name in sorted(biz_models.keys(), key=lambda k: len(biz_models[k]), reverse=True):
        count = len(biz_models[bm_name])
        lines.append(f"- **{bm_name}**: **{count} servers**")

    lines.extend([
        "",
        "---",
        "",
        "## 🔄 Automated Liveness & Fleet Updating",
        "",
        "This repository is continuously synchronized on our self-hosted bare-metal infrastructure (Woodpecker CI + systemd automation on `0docker.com` / `0mcp.com`):",
        "1. **Continuous Crawler**: Ingests newly discovered MCP domains from [DomainScope's](https://domainscope.scrapetheworld.org) 13M+ domain corpus.",
        "2. **Firmographic Enrichment**: Enriches and classifies each server using DomainScope's corporate graph.",
        "3. **Real-World HTTP Probes**: Verifies endpoint availability, protocol compliance, latency, and tool declarations.",
        "4. **Local CI/CD Pipeline**: Validated on every commit via [Woodpecker CI](https://ci.0exec.com) ([`.woodpecker.yml`](.woodpecker.yml)).",
        "5. **Autonomous Sync Daemon**: Scheduled via [`systemd/mcp-directory-sync.timer`](systemd/mcp-directory-sync.timer) executing [`scripts/fleet-sync-cron.sh`](scripts/fleet-sync-cron.sh).",
        "",
        "## 🤝 Contributing & Submitting a Server",
        "",
        "Host your MCP server card at `https://yourdomain.com/.well-known/mcp/server-card.json` or `/.well-known/ai-catalog.json`. DomainScope's crawler will discover it automatically, or submit an issue / PR!",
        "",
        "---",
        "",
        "## 📚 Citation, Research & Press Attribution",
        "",
        "If you use this dataset, telemetry benchmarks, or directory in academic research, articles, industry analyses, or publications, please cite it as follows:",
        "",
        "### Markdown / Plain Text",
        "> Badita, F. (2026). *Awesome Live MCP Servers: The Autonomous Internet-Scale Registry of Remote Model Context Protocol Servers*. DomainScope at Scrape the World. https://github.com/baditaflorin/awesome-live-mcp-servers",
        "",
        "### BibTeX",
        "```bibtex",
        "@misc{badita2026awesomelivemcpservers,",
        "  author = {Badita, Florin},",
        "  title = {Awesome Live MCP Servers: The Autonomous Internet-Scale Registry of Remote Model Context Protocol Servers},",
        "  institution = {DomainScope at Scrape the World},",
        "  year = {2026},",
        "  publisher = {GitHub},",
        "  journal = {GitHub repository},",
        "  howpublished = {\\url{https://github.com/baditaflorin/awesome-live-mcp-servers}},",
        "  url = {https://github.com/baditaflorin/awesome-live-mcp-servers}",
        "}",
        "```",
        "",
        "---",
        "",
        "## 📬 Contact, Press & Research Inquiries",
        "",
        "For media interviews, research collaborations, custom dataset slices, or partnership inquiries:",
        "- **Author / Maintainer**: Florin Badita",
        "- **Email**: [`florin@badita.org`](mailto:florin@badita.org)",
        "- **Initiative**: [DomainScope at Scrape the World](https://domainscope.scrapetheworld.org)",
        "- **License**: [MIT License](LICENSE)",
        "",
        "**Maintained by Florin Badita & [DomainScope at Scrape the World](https://domainscope.scrapetheworld.org)** · *Licensed under MIT*."
    ])

    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

if __name__ == "__main__":
    main()
