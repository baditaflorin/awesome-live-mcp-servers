# Awesome MCP Servers 🌐⚡

> **The definitive, live-benchmarked directory of public Model Context Protocol (MCP) servers and streamable AI manifests on the internet.**

[![Total Servers](https://img.shields.io/badge/MCP_Servers-138-purple?style=for-the-badge&logo=anthropic)](data/mcp-servers.json)
[![Live Reachable](https://img.shields.io/badge/Live_Reachable-136%20Online-emerald?style=for-the-badge)](data/mcp-servers.json)
[![Domains Scanned](https://img.shields.io/badge/Scanned_Corpus-290k+_Domains-blue?style=for-the-badge)](https://domainscope.scrapetheworld.org/mcp-directory)
[![CI: Woodpecker](https://img.shields.io/badge/CI-Woodpecker_Self--Hosted-2088FF?style=for-the-badge&logo=linux)](https://ci.0exec.com)

Unlike static lists of local `stdio` scripts, this repository is **continuously crawled, benchmarked, and updated** by [DomainScope](https://domainscope.scrapetheworld.org) running on self-hosted bare-metal fleet infrastructure (Woodpecker CI & server cron daemons) across 13M+ domains to index real, streamable-HTTP and machine-readable `/.well-known/ai-catalog.json` endpoints.

---

## 📥 Machine-Readable Feeds (For AI Agents)

Autonomous agents (in Cursor, Windsurf, Claude Desktop, Antigravity) can ingest the live directory directly:
- **JSON**: [`data/mcp-servers.json`](data/mcp-servers.json)
- **CSV**: [`data/mcp-servers.csv`](data/mcp-servers.csv)
- **Live Query Tool**: Use DomainScope's native MCP tool `domainscope_search_mcp_servers()` at `https://domainscope.scrapetheworld.org/mcp`

---

## 🔌 1-Click Connect Guide

### Cursor (`.cursor/mcp.json`)
```json
{
  "mcpServers": {
    "domainscope": {
      "url": "https://domainscope.scrapetheworld.org/mcp"
    }
  }
}
```

### Claude Desktop (`claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "domainscope": {
      "url": "https://domainscope.scrapetheworld.org/mcp"
    }
  }
}
```

---

## 📑 Directory of Public MCP Servers

### 🌐 Search & Web Data Extraction (1)

| Domain / Server | Status | Latency | Tools | Manifest | Dossier |
|---|:---:|:---:|:---:|:---:|:---:|
| **[brandfetch.com](https://brandfetch.com)**<br>*brandfetch.com* | 🟢 **Live** | 109 ms | ✓ | [Manifest ↗](https://brandfetch.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/brandfetch.com) |

### 💼 Enterprise & SaaS Platforms (47)

| Domain / Server | Status | Latency | Tools | Manifest | Dossier |
|---|:---:|:---:|:---:|:---:|:---:|
| **[198782.xyz](https://198782.xyz)**<br>*198782.xyz* | 🟢 **Live** | 102 ms | ✓ | [Manifest ↗](https://198782.xyz/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/198782.xyz) |
| **[adzartz.com](https://adzartz.com)**<br>*adzartz.com* | 🟢 **Live** | 986 ms | ✓ | [Manifest ↗](https://adzartz.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/adzartz.com) |
| **[bartin.info](https://bartin.info)**<br>*bartin.info* | 🟢 **Live** | 186 ms | ✓ | [Manifest ↗](https://bartin.info/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/bartin.info) |
| **[beautifulpeoplepersonals.com](https://beautifulpeoplepersonals.com)**<br>*beautifulpeoplepersonals.com* | 🟢 **Live** | 490 ms | ✓ | [Manifest ↗](https://beautifulpeoplepersonals.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/beautifulpeoplepersonals.com) |
| **[best-of-saas.com](https://best-of-saas.com)**<br>*best-of-saas.com* | 🟢 **Live** | 1587 ms | ✓ | [Manifest ↗](https://best-of-saas.com/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/best-of-saas.com) |
| **[bg245.com](https://bg245.com)**<br>*bg245.com* | 🟢 **Live** | 5071 ms | ✓ | [Manifest ↗](https://bg245.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/bg245.com) |
| **[canto-jazz.com](https://canto-jazz.com)**<br>*canto-jazz.com* | 🟢 **Live** | 205 ms | ✓ | [Manifest ↗](https://canto-jazz.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/canto-jazz.com) |
| **[careers-page.net](https://careers-page.net)**<br>*careers-page.net* | 🟢 **Live** | 175 ms | ✓ | [Manifest ↗](https://careers-page.net/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/careers-page.net) |
| **[ceo-sure.com](https://ceo-sure.com)**<br>*ceo-sure.com* | 🟢 **Live** | 218 ms | ✓ | [Manifest ↗](https://ceo-sure.com/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ceo-sure.com) |
| **[chatguatemalteco.net](https://chatguatemalteco.net)**<br>*chatguatemalteco.net* | 🟢 **Live** | 726 ms | ✓ | [Manifest ↗](https://chatguatemalteco.net/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/chatguatemalteco.net) |
| **[checkatrade.com](https://checkatrade.com)**<br>*checkatrade.com* | 🟢 **Live** | 228 ms | ✓ | [Manifest ↗](https://checkatrade.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/checkatrade.com) |
| **[chen1.net](https://chen1.net)**<br>*chen1.net* | 🟢 **Live** | 942 ms | ✓ | [Manifest ↗](https://chen1.net/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/chen1.net) |
| **[cliffwinters.org](https://cliffwinters.org)**<br>*cliffwinters.org* | 🟢 **Live** | 1239 ms | ✓ | [Manifest ↗](https://cliffwinters.org/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/cliffwinters.org) |
| **[colbergtech.net](https://colbergtech.net)**<br>*colbergtech.net* | 🟢 **Live** | 604 ms | ✓ | [Manifest ↗](https://colbergtech.net/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/colbergtech.net) |
| **[connectideas2business.org](https://connectideas2business.org)**<br>*connectideas2business.org* | 🟢 **Live** | 799 ms | ✓ | [Manifest ↗](https://connectideas2business.org/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/connectideas2business.org) |
| **[davidbuenov.com](https://davidbuenov.com)**<br>*davidbuenov.com* | 🟢 **Live** | 127 ms | 10 | [Manifest ↗](https://davidbuenov.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/davidbuenov.com) |
| **[db6353.com](https://db6353.com)**<br>*db6353.com* | 🟢 **Live** | 5083 ms | ✓ | [Manifest ↗](https://db6353.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/db6353.com) |
| **[db6737.com](https://db6737.com)**<br>*db6737.com* | 🟢 **Live** | 1290 ms | ✓ | [Manifest ↗](https://db6737.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/db6737.com) |
| **[db6999.com](https://db6999.com)**<br>*db6999.com* | 🟢 **Live** | 1265 ms | ✓ | [Manifest ↗](https://db6999.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/db6999.com) |
| **[db7049.com](https://db7049.com)**<br>*db7049.com* | 🟢 **Live** | 5394 ms | ✓ | [Manifest ↗](https://db7049.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/db7049.com) |
| **[densu100tre.com](https://densu100tre.com)**<br>*densu100tre.com* | 🟢 **Live** | 298 ms | ✓ | [Manifest ↗](https://densu100tre.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/densu100tre.com) |
| **[dirnat.no](https://dirnat.no)**<br>*dirnat.no* | 🟢 **Live** | 1050 ms | ✓ | [Manifest ↗](https://dirnat.no/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/dirnat.no) |
| **[document360.com](https://document360.com)**<br>*document360.com* | 🟢 **Live** | 279 ms | ✓ | [Manifest ↗](https://document360.com/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/document360.com) |
| **[dokuzeylul.com](https://dokuzeylul.com)**<br>*dokuzeylul.com* | 🟢 **Live** | 98 ms | ✓ | [Manifest ↗](https://dokuzeylul.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/dokuzeylul.com) |
| **[dominicdraws.art](https://dominicdraws.art)**<br>*dominicdraws.art* | 🟢 **Live** | 881 ms | ✓ | [Manifest ↗](https://dominicdraws.art/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/dominicdraws.art) |
| **[egetelgraf.com](https://egetelgraf.com)**<br>*egetelgraf.com* | 🟢 **Live** | 298 ms | ✓ | [Manifest ↗](https://egetelgraf.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/egetelgraf.com) |
| **[elang800.com](https://elang800.com)**<br>*elang800.com* | 🟢 **Live** | 287 ms | ✓ | [Manifest ↗](https://elang800.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/elang800.com) |
| **[everestexp26.com](https://everestexp26.com)**<br>*everestexp26.com* | 🟢 **Live** | 1139 ms | ✓ | [Manifest ↗](https://everestexp26.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/everestexp26.com) |
| **[frase.io](https://frase.io)**<br>*frase.io* | 🟢 **Live** | 366 ms | ✓ | [Manifest ↗](https://frase.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/frase.io) |
| **[gendut188tall.org](https://gendut188tall.org)**<br>*gendut188tall.org* | 🟢 **Live** | 483 ms | ✓ | [Manifest ↗](https://gendut188tall.org/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/gendut188tall.org) |
| **[gengpgjp.org](https://gengpgjp.org)**<br>*gengpgjp.org* | 🟢 **Live** | 482 ms | ✓ | [Manifest ↗](https://gengpgjp.org/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/gengpgjp.org) |
| **[guruwalk.com](https://guruwalk.com)**<br>*guruwalk.com* | 🟢 **Live** | 250 ms | ✓ | [Manifest ↗](https://guruwalk.com/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/guruwalk.com) |
| **[inco.vc](https://inco.vc)**<br>*inco.vc* | 🟢 **Live** | 192 ms | 3 | [Manifest ↗](https://inco.vc/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/inco.vc) |
| **[invisible.college](https://invisible.college)**<br>*invisible.college* | 🟢 **Live** | 641 ms | ✓ | [Manifest ↗](https://invisible.college/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/invisible.college) |
| **[japanophone.com](https://japanophone.com)**<br>*japanophone.com* | 🟢 **Live** | 462 ms | ✓ | [Manifest ↗](https://japanophone.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/japanophone.com) |
| **[jepe500.org](https://jepe500.org)**<br>*jepe500.org* | 🟢 **Live** | 288 ms | ✓ | [Manifest ↗](https://jepe500.org/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/jepe500.org) |
| **[lesensduneviefondationdefrance.org](https://lesensduneviefondationdefrance.org)**<br>*lesensduneviefondationdefrance.org* | 🟢 **Live** | 834 ms | ✓ | [Manifest ↗](https://lesensduneviefondationdefrance.org/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/lesensduneviefondationdefrance.org) |
| **[mentimeter.com](https://mentimeter.com)**<br>*mentimeter.com* | 🟢 **Live** | 267 ms | 3 | [Manifest ↗](https://mentimeter.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/mentimeter.com) |
| **[opus.pro](https://opus.pro)**<br>*opus.pro* | 🟢 **Live** | 211 ms | ✓ | [Manifest ↗](https://opus.pro/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/opus.pro) |
| **[pangram.com](https://pangram.com)**<br>*pangram.com* | 🟢 **Live** | 578 ms | 2 | [Manifest ↗](https://pangram.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/pangram.com) |
| **[pocket.science](https://pocket.science)**<br>*pocket.science* | 🟢 **Live** | 239 ms | ✓ | [Manifest ↗](https://pocket.science/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/pocket.science) |
| **[questportal.com](https://questportal.com)**<br>*questportal.com* | 🟢 **Live** | 367 ms | 8 | [Manifest ↗](https://questportal.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/questportal.com) |
| **[rar.design](https://rar.design)**<br>*rar.design* | 🟢 **Live** | 205 ms | ✓ | [Manifest ↗](https://rar.design/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/rar.design) |
| **[tomathoki.net](https://tomathoki.net)**<br>*tomathoki.net* | 🟢 **Live** | 472 ms | ✓ | [Manifest ↗](https://tomathoki.net/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/tomathoki.net) |
| **[vitaboy.net](https://vitaboy.net)**<br>*vitaboy.net* | 🟢 **Live** | 579 ms | ✓ | [Manifest ↗](https://vitaboy.net/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/vitaboy.net) |
| **[acufocus.com](https://acufocus.com)**<br>*acufocus.com* | 🔴 *Down* | - | ✓ | [Manifest ↗](https://acufocus.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/acufocus.com) |
| **[campjellystone.com](https://campjellystone.com)**<br>*campjellystone.com* | 🔴 *Down* | - | ✓ | [Manifest ↗](https://campjellystone.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/campjellystone.com) |

### 📊 Analytics & Business Intelligence (2)

| Domain / Server | Status | Latency | Tools | Manifest | Dossier |
|---|:---:|:---:|:---:|:---:|:---:|
| **[egg-road.com](https://egg-road.com)**<br>*egg-road.com* | 🟢 **Live** | 129 ms | ✓ | [Manifest ↗](https://egg-road.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/egg-road.com) |
| **[enginuityanalytics.com](https://enginuityanalytics.com)**<br>*enginuityanalytics.com* | 🟢 **Live** | 419 ms | ✓ | [Manifest ↗](https://enginuityanalytics.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/enginuityanalytics.com) |

### 🛒 E-Commerce & Retail (4)

| Domain / Server | Status | Latency | Tools | Manifest | Dossier |
|---|:---:|:---:|:---:|:---:|:---:|
| **[car919.com](https://car919.com)**<br>*car919.com* | 🟢 **Live** | 2176 ms | ✓ | [Manifest ↗](https://car919.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/car919.com) |
| **[ecomplannerhk.com](https://ecomplannerhk.com)**<br>*ecomplannerhk.com* | 🟢 **Live** | 313 ms | ✓ | [Manifest ↗](https://ecomplannerhk.com/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ecomplannerhk.com) |
| **[kumpulan0j0l.motorcycles](https://kumpulan0j0l.motorcycles)**<br>*kumpulan0j0l.motorcycles* | 🟢 **Live** | 300 ms | ✓ | [Manifest ↗](https://kumpulan0j0l.motorcycles/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/kumpulan0j0l.motorcycles) |
| **[sellerassistant.app](https://sellerassistant.app)**<br>*sellerassistant.app* | 🟢 **Live** | 372 ms | ✓ | [Manifest ↗](https://sellerassistant.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/sellerassistant.app) |

### 🛠️ Developer Tools & DevOps (31)

| Domain / Server | Status | Latency | Tools | Manifest | Dossier |
|---|:---:|:---:|:---:|:---:|:---:|
| **[21st.dev](https://21st.dev)**<br>*21st.dev* | 🟢 **Live** | 191 ms | ✓ | [Manifest ↗](https://21st.dev/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/21st.dev) |
| **[apify.com](https://apify.com)**<br>*apify.com* | 🟢 **Live** | 184 ms | 9 | [Manifest ↗](https://apify.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/apify.com) |
| **[apilayer.net](https://apilayer.net)**<br>*apilayer.net* | 🟢 **Live** | 420 ms | ✓ | [Manifest ↗](https://apilayer.net/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/apilayer.net) |
| **[appwrite.io](https://appwrite.io)**<br>*appwrite.io* | 🟢 **Live** | 137 ms | ✓ | [Manifest ↗](https://appwrite.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/appwrite.io) |
| **[aptos.dev](https://aptos.dev)**<br>*aptos.dev* | 🟢 **Live** | 212 ms | ✓ | [Manifest ↗](https://aptos.dev/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aptos.dev) |
| **[balderton.com](https://balderton.com)**<br>*balderton.com* | 🟢 **Live** | 113 ms | ✓ | [Manifest ↗](https://balderton.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/balderton.com) |
| **[bridger.to](https://bridger.to)**<br>*bridger.to* | 🟢 **Live** | 223 ms | ✓ | [Manifest ↗](https://bridger.to/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/bridger.to) |
| **[buildkite.com](https://buildkite.com)**<br>*buildkite.com* | 🟢 **Live** | 232 ms | ✓ | [Manifest ↗](https://buildkite.com/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/buildkite.com) |
| **[cal.com](https://cal.com)**<br>*cal.com* | 🟢 **Live** | 194 ms | ✓ | [Manifest ↗](https://cal.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/cal.com) |
| **[cdn-trackers.com](https://cdn-trackers.com)**<br>*cdn-trackers.com* | 🟢 **Live** | 986 ms | ✓ | [Manifest ↗](https://cdn-trackers.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/cdn-trackers.com) |
| **[chery-server.com](https://chery-server.com)**<br>*chery-server.com* | 🟢 **Live** | 763 ms | ✓ | [Manifest ↗](https://chery-server.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/chery-server.com) |
| **[clickhouse.tech](https://clickhouse.tech)**<br>*clickhouse.tech* | 🟢 **Live** | 415 ms | ✓ | [Manifest ↗](https://clickhouse.tech/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/clickhouse.tech) |
| **[collabson.cloud](https://collabson.cloud)**<br>*collabson.cloud* | 🟢 **Live** | 264 ms | ✓ | [Manifest ↗](https://collabson.cloud/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/collabson.cloud) |
| **[courtneyr.dev](https://courtneyr.dev)**<br>*courtneyr.dev* | 🟢 **Live** | 193 ms | ✓ | [Manifest ↗](https://courtneyr.dev/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/courtneyr.dev) |
| **[custats.info](https://custats.info)**<br>*custats.info* | 🟢 **Live** | 401 ms | 4 | [Manifest ↗](https://custats.info/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/custats.info) |
| **[fly.io](https://fly.io)**<br>*fly.io* | 🟢 **Live** | 163 ms | ✓ | [Manifest ↗](https://fly.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/fly.io) |
| **[github.com](https://github.com)**<br>*github.com* | 🟢 **Live** | 290 ms | ✓ | [Manifest ↗](https://github.com/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/github.com) |
| **[img.ly](https://img.ly)**<br>*img.ly* | 🟢 **Live** | 284 ms | ✓ | [Manifest ↗](https://img.ly/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/img.ly) |
| **[infraspeak.com](https://infraspeak.com)**<br>*infraspeak.com* | 🟢 **Live** | 182 ms | ✓ | [Manifest ↗](https://infraspeak.com/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/infraspeak.com) |
| **[mindstamp.com](https://mindstamp.com)**<br>*mindstamp.com* | 🟢 **Live** | 348 ms | ✓ | [Manifest ↗](https://mindstamp.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/mindstamp.com) |
| **[mobiloud.com](https://mobiloud.com)**<br>*mobiloud.com* | 🟢 **Live** | 227 ms | ✓ | [Manifest ↗](https://mobiloud.com/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/mobiloud.com) |
| **[neon.tech](https://neon.tech)**<br>*neon.tech* | 🟢 **Live** | 374 ms | ✓ | [Manifest ↗](https://neon.tech/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/neon.tech) |
| **[nextjs.org](https://nextjs.org)**<br>*nextjs.org* | 🟢 **Live** | 137 ms | ✓ | [Manifest ↗](https://nextjs.org/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/nextjs.org) |
| **[noos.cloud](https://noos.cloud)**<br>*noos.cloud* | 🟢 **Live** | 204 ms | ✓ | [Manifest ↗](https://noos.cloud/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/noos.cloud) |
| **[quicknode.com](https://quicknode.com)**<br>*quicknode.com* | 🟢 **Live** | 232 ms | 19 | [Manifest ↗](https://quicknode.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/quicknode.com) |
| **[screenwriter.dev](https://screenwriter.dev)**<br>*screenwriter.dev* | 🟢 **Live** | 395 ms | 26 | [Manifest ↗](https://screenwriter.dev/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/screenwriter.dev) |
| **[supabase.com](https://supabase.com)**<br>*supabase.com* | 🟢 **Live** | 195 ms | ✓ | [Manifest ↗](https://supabase.com/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/supabase.com) |
| **[txbonline.tech](https://txbonline.tech)**<br>*txbonline.tech* | 🟢 **Live** | 1338 ms | ✓ | [Manifest ↗](https://txbonline.tech/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/txbonline.tech) |
| **[vercel.com](https://vercel.com)**<br>*vercel.com* | 🟢 **Live** | 183 ms | ✓ | [Manifest ↗](https://vercel.com/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/vercel.com) |
| **[weaviate.io](https://weaviate.io)**<br>*weaviate.io* | 🟢 **Live** | 314 ms | ✓ | [Manifest ↗](https://weaviate.io/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/weaviate.io) |
| **[zinklabs.dev](https://zinklabs.dev)**<br>*zinklabs.dev* | 🟢 **Live** | 342 ms | ✓ | [Manifest ↗](https://zinklabs.dev/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/zinklabs.dev) |

### 🤖 AI Labs & Foundation Models (53)

| Domain / Server | Status | Latency | Tools | Manifest | Dossier |
|---|:---:|:---:|:---:|:---:|:---:|
| **[3igate.ai](https://3igate.ai)**<br>*3igate.ai* | 🟢 **Live** | 165 ms | ✓ | [Manifest ↗](https://3igate.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/3igate.ai) |
| **[actava.ai](https://actava.ai)**<br>*actava.ai* | 🟢 **Live** | 355 ms | ✓ | [Manifest ↗](https://actava.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/actava.ai) |
| **[agenticplug.ai](https://agenticplug.ai)**<br>*agenticplug.ai* | 🟢 **Live** | 174 ms | 5 | [Manifest ↗](https://agenticplug.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/agenticplug.ai) |
| **[aiboxbot.com](https://aiboxbot.com)**<br>*aiboxbot.com* | 🟢 **Live** | 1472 ms | ✓ | [Manifest ↗](https://aiboxbot.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aiboxbot.com) |
| **[alphasignal.ai](https://alphasignal.ai)**<br>*alphasignal.ai* | 🟢 **Live** | 210 ms | ✓ | [Manifest ↗](https://alphasignal.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/alphasignal.ai) |
| **[amplitude.com](https://amplitude.com)**<br>*amplitude.com* | 🟢 **Live** | 842 ms | ✓ | [Manifest ↗](https://amplitude.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/amplitude.com) |
| **[artificialstudio.ai](https://artificialstudio.ai)**<br>*artificialstudio.ai* | 🟢 **Live** | 418 ms | ✓ | [Manifest ↗](https://artificialstudio.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/artificialstudio.ai) |
| **[askcory.ai](https://askcory.ai)**<br>*askcory.ai* | 🟢 **Live** | 393 ms | ✓ | [Manifest ↗](https://askcory.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/askcory.ai) |
| **[backlight.ai](https://backlight.ai)**<br>*backlight.ai* | 🟢 **Live** | 176 ms | ✓ | [Manifest ↗](https://backlight.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/backlight.ai) |
| **[bandar388.net](https://bandar388.net)**<br>*bandar388.net* | 🟢 **Live** | 299 ms | ✓ | [Manifest ↗](https://bandar388.net/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/bandar388.net) |
| **[belochki24.info](https://belochki24.info)**<br>*belochki24.info* | 🟢 **Live** | 589 ms | ✓ | [Manifest ↗](https://belochki24.info/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/belochki24.info) |
| **[bolta.ai](https://bolta.ai)**<br>*bolta.ai* | 🟢 **Live** | 215 ms | ✓ | [Manifest ↗](https://bolta.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/bolta.ai) |
| **[bonnard.ai](https://bonnard.ai)**<br>*bonnard.ai* | 🟢 **Live** | 296 ms | ✓ | [Manifest ↗](https://bonnard.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/bonnard.ai) |
| **[braininfra.ai](https://braininfra.ai)**<br>*braininfra.ai* | 🟢 **Live** | 899 ms | ✓ | [Manifest ↗](https://braininfra.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/braininfra.ai) |
| **[camgirlstats.com](https://camgirlstats.com)**<br>*camgirlstats.com* | 🟢 **Live** | 338 ms | ✓ | [Manifest ↗](https://camgirlstats.com/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/camgirlstats.com) |
| **[carshippers.ai](https://carshippers.ai)**<br>*carshippers.ai* | 🟢 **Live** | 725 ms | 2 | [Manifest ↗](https://carshippers.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/carshippers.ai) |
| **[certiv.ai](https://certiv.ai)**<br>*certiv.ai* | 🟢 **Live** | 641 ms | ✓ | [Manifest ↗](https://certiv.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/certiv.ai) |
| **[chatprd.ai](https://chatprd.ai)**<br>*ChatPRD* | 🟢 **Live** | 391 ms | ✓ | [Manifest ↗](https://chatprd.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/chatprd.ai) |
| **[chickenwordchain.com](https://chickenwordchain.com)**<br>*chickenwordchain.com* | 🟢 **Live** | 142 ms | ✓ | [Manifest ↗](https://chickenwordchain.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/chickenwordchain.com) |
| **[chronoflow.ai](https://chronoflow.ai)**<br>*chronoflow.ai* | 🟢 **Live** | 178 ms | ✓ | [Manifest ↗](https://chronoflow.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/chronoflow.ai) |
| **[civicstar.ai](https://civicstar.ai)**<br>*Boardwalk AI Catalog* | 🟢 **Live** | 414 ms | ✓ | [Manifest ↗](https://civicstar.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/civicstar.ai) |
| **[cloptima.ai](https://cloptima.ai)**<br>*cloptima.ai* | 🟢 **Live** | 407 ms | ✓ | [Manifest ↗](https://cloptima.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/cloptima.ai) |
| **[cms.ai](https://cms.ai)**<br>*cms.ai* | 🟢 **Live** | 198 ms | ✓ | [Manifest ↗](https://cms.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/cms.ai) |
| **[companyresearch.ai](https://companyresearch.ai)**<br>*companyresearch.ai* | 🟢 **Live** | 407 ms | 70 | [Manifest ↗](https://companyresearch.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/companyresearch.ai) |
| **[constitucion.ai](https://constitucion.ai)**<br>*constitucion.ai* | 🟢 **Live** | 401 ms | ✓ | [Manifest ↗](https://constitucion.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/constitucion.ai) |
| **[content-center.ai](https://content-center.ai)**<br>*content-center.ai* | 🟢 **Live** | 454 ms | 1 | [Manifest ↗](https://content-center.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/content-center.ai) |
| **[coot.ai](https://coot.ai)**<br>*coot.ai* | 🟢 **Live** | 193 ms | ✓ | [Manifest ↗](https://coot.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/coot.ai) |
| **[createprints.ai](https://createprints.ai)**<br>*createprints.ai* | 🟢 **Live** | 313 ms | ✓ | [Manifest ↗](https://createprints.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/createprints.ai) |
| **[dasha.ai](https://dasha.ai)**<br>*dasha.ai* | 🟢 **Live** | 496 ms | ✓ | [Manifest ↗](https://dasha.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/dasha.ai) |
| **[efunnygame.com](https://efunnygame.com)**<br>*efunnygame.com* | 🟢 **Live** | 297 ms | ✓ | [Manifest ↗](https://efunnygame.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/efunnygame.com) |
| **[explorium.ai](https://explorium.ai)**<br>*explorium.ai* | 🟢 **Live** | 671 ms | 14 | [Manifest ↗](https://explorium.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/explorium.ai) |
| **[guild.ai](https://guild.ai)**<br>*guild.ai* | 🟢 **Live** | 369 ms | 4 | [Manifest ↗](https://guild.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/guild.ai) |
| **[huggingface.co](https://huggingface.co)**<br>*huggingface.co* | 🟢 **Live** | 265 ms | ✓ | [Manifest ↗](https://huggingface.co/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/huggingface.co) |
| **[jobpal.ai](https://jobpal.ai)**<br>*jobpal.ai* | 🟢 **Live** | 1061 ms | ✓ | [Manifest ↗](https://jobpal.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/jobpal.ai) |
| **[layer.ai](https://layer.ai)**<br>*Layer* | 🟢 **Live** | 172 ms | ✓ | [Manifest ↗](https://layer.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/layer.ai) |
| **[letz.ai](https://letz.ai)**<br>*letz.ai* | 🟢 **Live** | 172 ms | ✓ | [Manifest ↗](https://letz.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/letz.ai) |
| **[loops.so](https://loops.so)**<br>*loops.so* | 🟢 **Live** | 316 ms | ✓ | [Manifest ↗](https://loops.so/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/loops.so) |
| **[magichour.ai](https://magichour.ai)**<br>*magichour.ai* | 🟢 **Live** | 138 ms | ✓ | [Manifest ↗](https://magichour.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/magichour.ai) |
| **[marketscale.com](https://marketscale.com)**<br>*MarketScale* | 🟢 **Live** | 223 ms | ✓ | [Manifest ↗](https://marketscale.com/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/marketscale.com) |
| **[meetsquad.ai](https://meetsquad.ai)**<br>*meetsquad.ai* | 🟢 **Live** | 176 ms | ✓ | [Manifest ↗](https://meetsquad.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/meetsquad.ai) |
| **[momentic.ai](https://momentic.ai)**<br>*momentic.ai* | 🟢 **Live** | 169 ms | 26 | [Manifest ↗](https://momentic.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/momentic.ai) |
| **[ora.ai](https://ora.ai)**<br>*ora.ai* | 🟢 **Live** | 469 ms | 13 | [Manifest ↗](https://ora.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ora.ai) |
| **[outlit.ai](https://outlit.ai)**<br>*outlit.ai* | 🟢 **Live** | 756 ms | 46 | [Manifest ↗](https://outlit.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/outlit.ai) |
| **[paz.ai](https://paz.ai)**<br>*paz.ai* | 🟢 **Live** | 525 ms | 6 | [Manifest ↗](https://paz.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/paz.ai) |
| **[performa.ai](https://performa.ai)**<br>*performa.ai* | 🟢 **Live** | 184 ms | ✓ | [Manifest ↗](https://performa.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/performa.ai) |
| **[qdtech.ai](https://qdtech.ai)**<br>*qdtech.ai* | 🟢 **Live** | 943 ms | ✓ | [Manifest ↗](https://qdtech.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/qdtech.ai) |
| **[railway.app](https://railway.app)**<br>*railway.app* | 🟢 **Live** | 212 ms | ✓ | [Manifest ↗](https://railway.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/railway.app) |
| **[reducto.ai](https://reducto.ai)**<br>*reducto.ai* | 🟢 **Live** | 189 ms | 9 | [Manifest ↗](https://reducto.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/reducto.ai) |
| **[roboflow.ai](https://roboflow.ai)**<br>*roboflow.ai* | 🟢 **Live** | 241 ms | ✓ | [Manifest ↗](https://roboflow.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/roboflow.ai) |
| **[rocketgrowth.ai](https://rocketgrowth.ai)**<br>*RocketGrowth* | 🟢 **Live** | 112 ms | ✓ | [Manifest ↗](https://rocketgrowth.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/rocketgrowth.ai) |
| **[sitegpt.ai](https://sitegpt.ai)**<br>*sitegpt.ai* | 🟢 **Live** | 225 ms | 17 | [Manifest ↗](https://sitegpt.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/sitegpt.ai) |
| **[sweetspot.stream](https://sweetspot.stream)**<br>*sweetspot.stream* | 🟢 **Live** | 206 ms | ✓ | [Manifest ↗](https://sweetspot.stream/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/sweetspot.stream) |
| **[vast.ai](https://vast.ai)**<br>*vast.ai* | 🟢 **Live** | 237 ms | ✓ | [Manifest ↗](https://vast.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/vast.ai) |

---

## 🔄 Automated Liveness & Fleet Updating

This repository is maintained and synchronized on our self-hosted bare-metal infrastructure (Woodpecker CI + systemd automation on `0docker.com` / `0mcp.com`):
1. **Continuous Crawler**: Ingests newly discovered MCP domains from [DomainScope's](https://domainscope.scrapetheworld.org) 13M+ domain corpus.
2. **Real-World HTTP Probes**: Verifies endpoint availability, protocol compliance, latency, and tool declarations.
3. **Local CI/CD Pipeline**: Validated on every commit via [Woodpecker CI](https://ci.0exec.com) ([`.woodpecker.yml`](.woodpecker.yml)).
4. **Autonomous Sync Daemon**: Scheduled via [`systemd/mcp-directory-sync.timer`](systemd/mcp-directory-sync.timer) executing [`scripts/fleet-sync-cron.sh`](scripts/fleet-sync-cron.sh).

## 🤝 Contributing & Submitting a Server

Host your MCP server card at `https://yourdomain.com/.well-known/mcp/server-card.json` or `/.well-known/ai-catalog.json`. DomainScope's crawler will discover it automatically, or submit an issue / PR!

**Maintained by [DomainScope](https://domainscope.scrapetheworld.org) & Badita Florin** · *Licensed under MIT*.
