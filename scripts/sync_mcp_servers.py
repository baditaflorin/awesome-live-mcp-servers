#!/usr/bin/env python3
"""
sync_mcp_servers.py

Autonomous synchronizer for the Awesome MCP Servers repository.
Queries DomainScope's 13M+ domain corpus intelligence engine and
real-world AI catalog discovery probes to compile, verify, and
benchmark all live public Model Context Protocol (MCP) servers on the web.

Generates:
  - README.md (clean, formatted, categorized tables with liveness badges)
  - data/mcp-servers.json (machine-readable for AI agents and LLMs)
  - data/mcp-servers.csv (data analysis spreadsheet)
"""

import urllib.request
import urllib.error
import json
import csv
import time
import os
import sys
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed

DOMAINSCOPE_API = "https://domainscope.scrapetheworld.org/api/v1"
DOMAINSCOPE_WEB = "https://domainscope.scrapetheworld.org"
USER_AGENT = "Awesome-MCP-Servers-Bot/1.0 (+https://github.com/baditaflorin/awesome-mcp-servers)"

def fetch_json(url, timeout=6):
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
            return resp.status == 200, elapsed_ms
    except Exception:
        return False, None

def get_domain_details(domain):
    data = fetch_json(f"{DOMAINSCOPE_API}/public/domain/{domain}")
    if data and "data" in data and data["data"]:
        d = data["data"]
        return {
            "category": d.get("category") or "General Tech",
            "industry": d.get("industry") or "Technology",
            "description": d.get("description") or "",
        }
    return {"category": "General Tech", "industry": "Technology", "description": ""}

def fetch_manifest_details(domain):
    # Try server-card first
    card_url = f"https://{domain}/.well-known/mcp/server-card.json"
    card = fetch_json(card_url, timeout=3)
    if card and isinstance(card, dict):
        title = card.get("server_title") or card.get("server_name") or domain
        desc = card.get("server_description") or ""
        tools = card.get("tools") or []
        version = card.get("server_version") or "1.0"
        return {
            "title": title,
            "description": desc,
            "tools_count": len(tools) if isinstance(tools, list) else 0,
            "version": version,
            "card_url": card_url,
            "type": "server_card",
        }
    
    # Try ai-catalog.json
    catalog_url = f"https://{domain}/.well-known/ai-catalog.json"
    cat = fetch_json(catalog_url, timeout=3)
    if cat and isinstance(cat, dict):
        servers = cat.get("mcp_servers") or []
        first = servers[0] if servers and isinstance(servers, list) else {}
        title = first.get("title") or first.get("name") or cat.get("name") or domain
        desc = first.get("description") or cat.get("description") or ""
        tools = first.get("tools") or []
        return {
            "title": title,
            "description": desc,
            "tools_count": len(tools) if isinstance(tools, list) else 0,
            "version": first.get("version") or "1.0",
            "card_url": catalog_url,
            "type": "ai_catalog",
        }

    return {
        "title": domain,
        "description": "",
        "tools_count": 0,
        "version": "1.0",
        "card_url": f"https://{domain}/.well-known/mcp/server-card.json",
        "type": "probe",
    }

def categorize_server(domain, cat_name, industry, title, desc):
    text = f"{domain} {cat_name} {industry} {title} {desc}".lower()
    if any(k in text for k in ["ai", "model", "llm", "agent", "intelligence", "neural", "anthropic", "openai", "deepseek", "hugging"]):
        return "🤖 AI Labs & Foundation Models"
    if any(k in text for k in ["dev", "code", "git", "api", "infra", "cloud", "docker", "database", "sql", "supabase", "apify"]):
        return "🛠️ Developer Tools & DevOps"
    if any(k in text for k in ["analytics", "bi", "metrics", "amplitude", "mixpanel", "growth", "stats", "telemetry"]):
        return "📊 Analytics & Business Intelligence"
    if any(k in text for k in ["scrap", "crawl", "extract", "search", "proxy", "spider", "fetch"]):
        return "🌐 Search & Web Data Extraction"
    if any(k in text for k in ["ecommerce", "shop", "retail", "store", "commerce", "payment", "stripe"]):
        return "🛒 E-Commerce & Retail"
    if any(k in text for k in ["security", "auth", "identity", "cyber", "dns", "cert", "tls"]):
        return "🔒 Security & Identity"
    return "💼 Enterprise & SaaS Platforms"

def main():
    print("🚀 Querying DomainScope AI Ecosystem API...")
    res = fetch_json(f"{DOMAINSCOPE_API}/stats/ai-ecosystem")
    if not res or "data" not in res:
        print("❌ Failed to fetch from DomainScope API")
        sys.exit(1)

    data = res["data"]
    total_scanned = data.get("total_scanned_domains", 0)
    total_catalogs = data.get("total_active_catalogs", 0)
    raw_servers = data.get("top_mcp_domains", [])
    print(f"📊 Discovered {len(raw_servers)} potential MCP host domains across {total_scanned:,} scanned domains.")

    # Process all domains concurrently
    processed_servers = []
    print("⚡ Inspecting live manifests and reachability benchmarks...")

    with ThreadPoolExecutor(max_workers=16) as executor:
        futures = {}
        for item in raw_servers:
            domain = item["domain"]
            futures[executor.submit(process_single_domain, domain, item)] = domain

        for f in as_completed(futures):
            srv = f.result()
            if srv:
                processed_servers.append(srv)

    # Sort servers by reachability, then domain
    processed_servers.sort(key=lambda s: (not s["reachable"], s["domain"]))

    active_count = sum(1 for s in processed_servers if s["reachable"])
    total_count = len(processed_servers)
    print(f"✅ Finished inspecting: {active_count}/{total_count} servers are LIVE & REACHABLE.")

    # Write Data Artifacts
    write_json(processed_servers, total_scanned, total_catalogs)
    write_csv(processed_servers)
    write_readme(processed_servers, total_scanned, total_catalogs, active_count)
    print("🎉 Sync completed successfully! Updated README.md and data files.")

def process_single_domain(domain, raw_item):
    try:
        manifest = fetch_manifest_details(domain)
        d_info = get_domain_details(domain)

        # Check reachability directly
        card_reachable, latency = probe_endpoint(manifest["card_url"], timeout=4)
        if not card_reachable:
            # Try domain root
            card_reachable, latency = probe_endpoint(f"https://{domain}", timeout=3)

        category = categorize_server(
            domain,
            d_info["category"],
            d_info["industry"],
            manifest["title"],
            manifest["description"]
        )

        desc = manifest["description"]
        if not desc:
            desc = d_info["description"]
        if not desc:
            desc = f"{d_info['category']} intelligence & services."

        return {
            "domain": domain,
            "title": manifest["title"],
            "description": desc,
            "category": category,
            "industry": d_info["industry"],
            "reachable": card_reachable,
            "latency_ms": latency if latency is not None else 0,
            "tools_count": manifest["tools_count"],
            "version": manifest["version"],
            "card_url": manifest["card_url"],
            "server_count": raw_item.get("server_count", 1),
            "artifact_count": raw_item.get("artifact_count", 0),
            "dossier_url": f"{DOMAINSCOPE_WEB}/domains/{domain}"
        }
    except Exception as e:
        print(f"Warning: error processing {domain}: {e}")
        return None

def write_json(servers, total_scanned, total_catalogs):
    out = {
        "metadata": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "generator": "DomainScope Live Scanner",
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
    keys = ["domain", "title", "category", "industry", "reachable", "latency_ms", "tools_count", "card_url", "dossier_url", "description"]
    with open("data/mcp-servers.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for s in servers:
            writer.writerow({k: s.get(k, "") for k in keys})

def write_readme(servers, total_scanned, total_catalogs, active_count):
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # Group by category
    categories = {}
    for s in servers:
        cat = s["category"]
        categories.setdefault(cat, []).append(s)

    lines = [
        "# Awesome MCP Servers 🌐⚡",
        "",
        "> **The definitive, live-benchmarked directory of public Model Context Protocol (MCP) servers and streamable AI manifests on the internet.**",
        "",
        f"[![Total Servers](https://img.shields.io/badge/MCP_Servers-{len(servers)}-purple?style=for-the-badge&logo=anthropic)](data/mcp-servers.json)",
        f"[![Live Reachable](https://img.shields.io/badge/Live_Reachable-{active_count}%20Online-emerald?style=for-the-badge)](data/mcp-servers.json)",
        f"[![Domains Scanned](https://img.shields.io/badge/Scanned_Corpus-290k+_Domains-blue?style=for-the-badge)](https://domainscope.scrapetheworld.org/mcp-directory)",
        f"[![Last Auto Sync](https://img.shields.io/badge/Last_Sync-{now_str.replace(' ', '_')}-grey?style=for-the-badge)](https://github.com/baditaflorin/awesome-mcp-servers/actions)",
        "",
        "Unlike static lists of local `stdio` scripts, this repository is **automatically crawled, benchmarked, and updated every Monday** by [DomainScope](https://domainscope.scrapetheworld.org) across 13M+ domains to index real, streamable-HTTP and machine-readable `/.well-known/ai-catalog.json` endpoints.",
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
        "## 📑 Directory of Public MCP Servers",
        ""
    ]

    for cat_name in sorted(categories.keys()):
        cat_servers = categories[cat_name]
        lines.append(f"### {cat_name} ({len(cat_servers)})")
        lines.append("")
        lines.append("| Domain / Server | Status | Latency | Tools | Manifest | Dossier |")
        lines.append("|---|:---:|:---:|:---:|:---:|:---:|")
        for s in cat_servers:
            status_badge = "🟢 **Live**" if s["reachable"] else "🔴 *Down*"
            lat_str = f"{s['latency_ms']} ms" if s["latency_ms"] > 0 else "-"
            tools_str = str(s["tools_count"]) if s["tools_count"] > 0 else "✓"
            lines.append(f"| **[{s['domain']}](https://{s['domain']})**<br>*{s['title']}* | {status_badge} | {lat_str} | {tools_str} | [Manifest ↗]({s['card_url']}) | [Dossier ↗]({s['dossier_url']}) |")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## 🔄 Automated Liveness & Weekly Updating",
        "",
        "This repository runs a scheduled GitHub Action [`.github/workflows/update-mcp-directory.yml`](.github/workflows/update-mcp-directory.yml) every Monday at 00:00 UTC:",
        "1. Fetches newly discovered MCP domains from [DomainScope's](https://domainscope.scrapetheworld.org) global crawler.",
        "2. Executes real-world HTTP health probes to detect newly published servers and flag offline endpoints.",
        "3. Updates `README.md`, `data/mcp-servers.json`, and `data/mcp-servers.csv` automatically.",
        "",
        "## 🤝 Contributing & Submitting a Server",
        "",
        "Host your MCP server card at `https://yourdomain.com/.well-known/mcp/server-card.json` or `/.well-known/ai-catalog.json`. DomainScope's crawler will discover it automatically, or submit an issue / PR!",
        "",
        "**Maintained by [DomainScope](https://domainscope.scrapetheworld.org) & Badita Florin** · *Licensed under MIT*."
    ])

    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

if __name__ == "__main__":
    main()
