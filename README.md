# Awesome MCP Servers 🌐⚡

> **The definitive, live-benchmarked directory of public Model Context Protocol (MCP) servers and streamable AI manifests on the internet.**
>
> Powered & enriched by **[DomainScope Deep Domain Intelligence](https://domainscope.scrapetheworld.org)**.

[![Total Servers](https://img.shields.io/badge/MCP_Servers-484-purple?style=for-the-badge&logo=anthropic)](data/mcp-servers.json)
[![Live Reachable](https://img.shields.io/badge/Live_Reachable-471%20Online-emerald?style=for-the-badge)](data/mcp-servers.json)
[![Scanned Corpus](https://img.shields.io/badge/Scanned_Corpus-450k+_Domains-blue?style=for-the-badge)](https://domainscope.scrapetheworld.org/mcp-directory)
[![Enriched by DomainScope](https://img.shields.io/badge/Intelligence-DomainScope_Graph-00D26A?style=for-the-badge&logo=databricks)](https://domainscope.scrapetheworld.org)
[![CI: Woodpecker](https://img.shields.io/badge/CI-Woodpecker_Self--Hosted-2088FF?style=for-the-badge&logo=linux)](https://ci.0exec.com)

Unlike uncurated lists that classify servers merely by top-level domains (`.ai`, `.dev`, `.com`), this repository utilizes **[DomainScope's](https://domainscope.scrapetheworld.org) 13M+ firmographic graph** to classify servers by verified market vertical, business architecture, tool interface capacity, and real-world network latency.

---

## 🧠 DomainScope Intelligence Integration

Each server card is enriched with verified metadata from DomainScope:
- **Market Taxonomy**: Multi-dimensional categorization (AI Foundation Labs, Autonomous Agents, Developer Tooling, Data Extraction).
- **Business Architecture**: Verified Delivery Models (*B2B SaaS, Open Source & Community, Freemium, API Developer*).
- **Live Dossiers**: Direct links to the domain's complete dossier (`domainscope.scrapetheworld.org/domains/:domain`) featuring tech stack detection, hosting ASN, and AI posture.
- **Real Reachability**: Concurrently benchmarked HTTP reachability (`🟢 Live` vs `🔴 Down`) and round-trip response latency.

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

## 📑 Directory of Public MCP Servers (by DomainScope Vertical)

### 🌐 Web Search, Crawling & Data Extraction (23)

| Server / Host | Business Model | Status | Latency | Tools | Manifest | DomainScope Dossier |
|---|---|:---:|:---:|:---:|:---:|:---:|
| **[a2milk.vn](https://a2milk.vn)**<br>*a2milk.vn* | `Retail Sales` | 🟢 **Live** | 303 ms | ✓ | [Manifest ↗](https://a2milk.vn/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/a2milk.vn) |
| **[a2nutrition.com.au](https://a2nutrition.com.au)**<br>*a2nutrition.com.au* | `B2C Sales` | 🟢 **Live** | 297 ms | ✓ | [Manifest ↗](https://a2nutrition.com.au/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/a2nutrition.com.au) |
| **[aartha.net](https://aartha.net)**<br>*aartha.net* | `SaaS subscription` | 🟢 **Live** | 887 ms | ✓ | [Manifest ↗](https://aartha.net/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aartha.net) |
| **[aegean.ai](https://aegean.ai)**<br>*aegean.ai Docs MCP* | `AI Services & Solutions` | 🟢 **Live** | 239 ms | 2 | [Manifest ↗](https://aegean.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aegean.ai) |
| **[alphasignal.ai](https://alphasignal.ai)**<br>*ai.alphasignal/news* | `Email subscription` | 🟢 **Live** | 361 ms | ✓ | [Manifest ↗](https://alphasignal.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/alphasignal.ai) |
| **[bonono.ai](https://bonono.ai)**<br>*BibiGPT* | `Subscription` | 🟢 **Live** | 220 ms | 6 | [Manifest ↗](https://bonono.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/bonono.ai) |
| **[chatimg.ai](https://chatimg.ai)**<br>*BibiGPT* | `Freemium with Subscription` | 🟢 **Live** | 272 ms | 6 | [Manifest ↗](https://chatimg.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/chatimg.ai) |
| **[companyresearch.ai](https://companyresearch.ai)**<br>*com.youspot/youspot* | `SaaS subscription` | 🟢 **Live** | 593 ms | 111 | [Manifest ↗](https://companyresearch.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/companyresearch.ai) |
| **[constitucion.ai](https://constitucion.ai)**<br>*com.kemenystudio/buyer-commerce* | `Non-profit` | 🟢 **Live** | 384 ms | ✓ | [Manifest ↗](https://constitucion.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/constitucion.ai) |
| **[donethat.ai](https://donethat.ai)**<br>*donethat* | `SaaS subscription` | 🟢 **Live** | 114 ms | 9 | [Manifest ↗](https://donethat.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/donethat.ai) |
| **[explorium.ai](https://explorium.ai)**<br>*explorium* | `SaaS subscription` | 🟢 **Live** | 624 ms | 14 | [Manifest ↗](https://explorium.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/explorium.ai) |
| **[flowtivity.ai](https://flowtivity.ai)**<br>*flowtivity* | `SaaS subscription` | 🟢 **Live** | 117 ms | 6 | [Manifest ↗](https://flowtivity.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/flowtivity.ai) |
| **[geoguru.ai](https://geoguru.ai)**<br>*LovedByAI* | `SaaS subscription` | 🟢 **Live** | 357 ms | 1 | [Manifest ↗](https://geoguru.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/geoguru.ai) |
| **[getcatalog.ai](https://getcatalog.ai)**<br>*ai.getcatalog/site* | `SaaS subscription` | 🟢 **Live** | 445 ms | ✓ | [Manifest ↗](https://getcatalog.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/getcatalog.ai) |
| **[infino.ai](https://infino.ai)**<br>*Infino Docs MCP* | `SaaS subscription` | 🟢 **Live** | 647 ms | 2 | [Manifest ↗](https://infino.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/infino.ai) |
| **[instant.ai](https://instant.ai)**<br>*ai.instant/domain-search* | `E-commerce` | 🟢 **Live** | 136 ms | ✓ | [Manifest ↗](https://instant.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/instant.ai) |
| **[listingbooster.ai](https://listingbooster.ai)**<br>*listingbooster-public-discovery* | `SaaS subscription` | 🟢 **Live** | 447 ms | 4 | [Manifest ↗](https://listingbooster.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/listingbooster.ai) |
| **[name.ai](https://name.ai)**<br>*name-ai* | `Marketplace, Brokerage` | 🟢 **Live** | 130 ms | 4 | [Manifest ↗](https://name.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/name.ai) |
| **[plantis.ai](https://plantis.ai)**<br>*The AI Conductor Framework Docs MCP* | `SaaS subscription` | 🟢 **Live** | 224 ms | 2 | [Manifest ↗](https://plantis.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/plantis.ai) |
| **[tooldirectory.ai](https://tooldirectory.ai)**<br>*ai.tooldirectory/catalog* | `Advertising, Affiliate Marketing` | 🟢 **Live** | 138 ms | 6 | [Manifest ↗](https://tooldirectory.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/tooldirectory.ai) |
| **[trustfoundry.ai](https://trustfoundry.ai)**<br>*trustfoundry.ai* | `SaaS_subscription` | 🟢 **Live** | 299 ms | ✓ | [Manifest ↗](https://trustfoundry.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/trustfoundry.ai) |
| **[tryconvert.ai](https://tryconvert.ai)**<br>*tryconvert.ai* | `SaaS subscription` | 🟢 **Live** | 642 ms | 18 | [Manifest ↗](https://tryconvert.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/tryconvert.ai) |
| **[urg.ai](https://urg.ai)**<br>*urg.ai* | `SaaS subscription` | 🟢 **Live** | 317 ms | ✓ | [Manifest ↗](https://urg.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/urg.ai) |

### 💼 Enterprise SaaS & B2B Solutions (240)

| Server / Host | Business Model | Status | Latency | Tools | Manifest | DomainScope Dossier |
|---|---|:---:|:---:|:---:|:---:|:---:|
| **[0x27.eu](https://0x27.eu)**<br>*0x27.eu* | `Unknown` | 🟢 **Live** | 327 ms | ✓ | [Manifest ↗](https://0x27.eu/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/0x27.eu) |
| **[1001bus-ufa.ru](https://1001bus-ufa.ru)**<br>*Страница не найдена* | `Ticket Sales` | 🟢 **Live** | 392 ms | ✓ | [Manifest ↗](https://1001bus-ufa.ru/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/1001bus-ufa.ru) |
| **[100ke.ai](https://100ke.ai)**<br>*100ke.ai* | `Free, Non-Profit` | 🟢 **Live** | 295 ms | ✓ | [Manifest ↗](https://100ke.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/100ke.ai) |
| **[101.cam](https://101.cam)**<br>*101.cam* | `Subscription-based` | 🟢 **Live** | 606 ms | ✓ | [Manifest ↗](https://101.cam/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/101.cam) |
| **[1440.org](https://1440.org)**<br>*1440.org* | `Donations, grants, and tuition fees` | 🟢 **Live** | 785 ms | ✓ | [Manifest ↗](https://1440.org/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/1440.org) |
| **[15651.app](https://15651.app)**<br>*15651.app* | `Unknown` | 🟢 **Live** | 5196 ms | ✓ | [Manifest ↗](https://15651.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/15651.app) |
| **[15881588.xyz](https://15881588.xyz)**<br>*15881588.xyz* | `Unknown` | 🟢 **Live** | 99 ms | ✓ | [Manifest ↗](https://15881588.xyz/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/15881588.xyz) |
| **[15bw.app](https://15bw.app)**<br>*15bw.app* | `Unknown` | 🟢 **Live** | 5152 ms | ✓ | [Manifest ↗](https://15bw.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/15bw.app) |
| **[168premiumcar.com](https://168premiumcar.com)**<br>*168premiumcar.com* | `Rental Services` | 🟢 **Live** | 728 ms | ✓ | [Manifest ↗](https://168premiumcar.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/168premiumcar.com) |
| **[18237.app](https://18237.app)**<br>*18237.app* | `Unknown` | 🟢 **Live** | 5092 ms | ✓ | [Manifest ↗](https://18237.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/18237.app) |
| **[188betm.net](https://188betm.net)**<br>*188betm.net* | `Gaming Revenue` | 🟢 **Live** | 1031 ms | ✓ | [Manifest ↗](https://188betm.net/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/188betm.net) |
| **[194935.xyz](https://194935.xyz)**<br>*194935.xyz* | `Unknown` | 🟢 **Live** | 230 ms | ✓ | [Manifest ↗](https://194935.xyz/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/194935.xyz) |
| **[198782.xyz](https://198782.xyz)**<br>*198782.xyz* | `Unknown` | 🟢 **Live** | 98 ms | ✓ | [Manifest ↗](https://198782.xyz/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/198782.xyz) |
| **[1a.net](https://1a.net)**<br>*1a.net* | `Advertising` | 🟢 **Live** | 284 ms | ✓ | [Manifest ↗](https://1a.net/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/1a.net) |
| **[1liga.by](https://1liga.by)**<br>*1liga.by* | `Non-profit` | 🟢 **Live** | 474 ms | ✓ | [Manifest ↗](https://1liga.by/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/1liga.by) |
| **[1love.cam](https://1love.cam)**<br>*1love.cam* | `Subscription-based and Pay-per-view` | 🟢 **Live** | 709 ms | ✓ | [Manifest ↗](https://1love.cam/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/1love.cam) |
| **[1on1cam.show](https://1on1cam.show)**<br>*1on1cam.show* | `Pay-per-service` | 🟢 **Live** | 760 ms | ✓ | [Manifest ↗](https://1on1cam.show/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/1on1cam.show) |
| **[2020institute.com](https://2020institute.com)**<br>*2020institute.com* | `Medical Services` | 🟢 **Live** | 349 ms | ✓ | [Manifest ↗](https://2020institute.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/2020institute.com) |
| **[22192petcare.cam](https://22192petcare.cam)**<br>*22192petcare.cam* | `Advertising` | 🟢 **Live** | 313 ms | ✓ | [Manifest ↗](https://22192petcare.cam/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/22192petcare.cam) |
| **[23589.app](https://23589.app)**<br>*23589.app* | `Unknown` | 🟢 **Live** | 1199 ms | ✓ | [Manifest ↗](https://23589.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/23589.app) |
| **[24-7intouch.com](https://24-7intouch.com)**<br>*24-7intouch.com* | `B2B service` | 🟢 **Live** | 386 ms | ✓ | [Manifest ↗](https://24-7intouch.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/24-7intouch.com) |
| **[26bw.app](https://26bw.app)**<br>*26bw.app* | `Unknown` | 🟢 **Live** | 5138 ms | ✓ | [Manifest ↗](https://26bw.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/26bw.app) |
| **[2casinoextra.com](https://2casinoextra.com)**<br>*2casinoextra.com* | `Gaming Revenue` | 🟢 **Live** | 263 ms | ✓ | [Manifest ↗](https://2casinoextra.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/2casinoextra.com) |
| **[2folie.cam](https://2folie.cam)**<br>*2folie.cam* | `Subscription-based and Pay-per-minute` | 🟢 **Live** | 683 ms | ✓ | [Manifest ↗](https://2folie.cam/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/2folie.cam) |
| **[2liga.by](https://2liga.by)**<br>*2liga.by* | `Non-profit` | 🟢 **Live** | 439 ms | ✓ | [Manifest ↗](https://2liga.by/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/2liga.by) |
| **[35bw.app](https://35bw.app)**<br>*35bw.app* | `Unknown` | 🟢 **Live** | 5155 ms | ✓ | [Manifest ↗](https://35bw.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/35bw.app) |
| **[3byggetilbud.dk](https://3byggetilbud.dk)**<br>*3byggetilbud.dk* | `Lead Generation` | 🟢 **Live** | 151 ms | ✓ | [Manifest ↗](https://3byggetilbud.dk/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/3byggetilbud.dk) |
| **[3dermatch.com](https://3dermatch.com)**<br>*3dermatch.com* | `Subscription-based Dating Service` | 🟢 **Live** | 640 ms | ✓ | [Manifest ↗](https://3dermatch.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/3dermatch.com) |
| **[3dpack.ing](https://3dpack.ing)**<br>*ing.3dpack/container-loading* | `SaaS subscription` | 🟢 **Live** | 236 ms | ✓ | [Manifest ↗](https://3dpack.ing/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/3dpack.ing) |
| **[3dvizual.cam](https://3dvizual.cam)**<br>*3dvizual.cam* | `Freemium` | 🟢 **Live** | 279 ms | ✓ | [Manifest ↗](https://3dvizual.cam/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/3dvizual.cam) |
| **[4over4.com](https://4over4.com)**<br>*4over4.com* | `B2B Sales` | 🟢 **Live** | 300 ms | ✓ | [Manifest ↗](https://4over4.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/4over4.com) |
| **[4plaisir.cam](https://4plaisir.cam)**<br>*4plaisir.cam* | `Subscription-based with pay-per-minute shows` | 🟢 **Live** | 687 ms | ✓ | [Manifest ↗](https://4plaisir.cam/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/4plaisir.cam) |
| **[4roomsclub.com](https://4roomsclub.com)**<br>*Four Rooms - Страница не найдена* | `Paid Services` | 🟢 **Live** | 431 ms | ✓ | [Manifest ↗](https://4roomsclub.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/4roomsclub.com) |
| **[52bw.app](https://52bw.app)**<br>*52bw.app* | `Unknown` | 🟢 **Live** | 5121 ms | ✓ | [Manifest ↗](https://52bw.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/52bw.app) |
| **[59haber.com](https://59haber.com)**<br>*59haber.com* | `Advertising` | 🟢 **Live** | 188 ms | ✓ | [Manifest ↗](https://59haber.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/59haber.com) |
| **[60plusdating.com](https://60plusdating.com)**<br>*60plusdating.com* | `Subscription` | 🟢 **Live** | 664 ms | ✓ | [Manifest ↗](https://60plusdating.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/60plusdating.com) |
| **[61saat.com](https://61saat.com)**<br>*61saat.com* | `Advertising` | 🟢 **Live** | 201 ms | ✓ | [Manifest ↗](https://61saat.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/61saat.com) |
| **[6ftdan.com](https://6ftdan.com)**<br>*6ftdan.com* | `Personal Blog` | 🟢 **Live** | 491 ms | ✓ | [Manifest ↗](https://6ftdan.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/6ftdan.com) |
| **[72bw.app](https://72bw.app)**<br>*72bw.app* | `Unknown` | 🟢 **Live** | 6022 ms | ✓ | [Manifest ↗](https://72bw.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/72bw.app) |
| **[73win.org](https://73win.org)**<br>*73win.org* | `Betting Commission` | 🟢 **Live** | 2157 ms | ✓ | [Manifest ↗](https://73win.org/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/73win.org) |
| **[7deniz.net](https://7deniz.net)**<br>*7deniz.net* | `Advertising` | 🟢 **Live** | 184 ms | ✓ | [Manifest ↗](https://7deniz.net/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/7deniz.net) |
| **[82bw.app](https://82bw.app)**<br>*82bw.app* | `Unknown` | 🟢 **Live** | 5124 ms | ✓ | [Manifest ↗](https://82bw.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/82bw.app) |
| **[83bw.app](https://83bw.app)**<br>*83bw.app* | `Unknown` | 🟢 **Live** | 5222 ms | ✓ | [Manifest ↗](https://83bw.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/83bw.app) |
| **[85bw.app](https://85bw.app)**<br>*85bw.app* | `Unknown` | 🟢 **Live** | 5174 ms | ✓ | [Manifest ↗](https://85bw.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/85bw.app) |
| **[888auto.club](https://888auto.club)**<br>*Страница не найдена* | `Rental Services` | 🟢 **Live** | 415 ms | ✓ | [Manifest ↗](https://888auto.club/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/888auto.club) |
| **[89bw.app](https://89bw.app)**<br>*89bw.app* | `Unknown` | 🟢 **Live** | 1256 ms | ✓ | [Manifest ↗](https://89bw.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/89bw.app) |
| **[93682.app](https://93682.app)**<br>*93682.app* | `Unknown` | 🟢 **Live** | 1142 ms | ✓ | [Manifest ↗](https://93682.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/93682.app) |
| **[96bw.app](https://96bw.app)**<br>*96bw.app* | `Unknown` | 🟢 **Live** | 5124 ms | ✓ | [Manifest ↗](https://96bw.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/96bw.app) |
| **[975country.com](https://975country.com)**<br>*975country.com* | `Advertising` | 🟢 **Live** | 249 ms | ✓ | [Manifest ↗](https://975country.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/975country.com) |
| **[9784023.ru](https://9784023.ru)**<br>*Страница не найдена* | `Tuition Fees` | 🟢 **Live** | 369 ms | ✓ | [Manifest ↗](https://9784023.ru/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/9784023.ru) |
| **[97bw.app](https://97bw.app)**<br>*97bw.app* | `Unknown` | 🟢 **Live** | 5202 ms | ✓ | [Manifest ↗](https://97bw.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/97bw.app) |
| **[9badges25mm.cam](https://9badges25mm.cam)**<br>*9badges25mm.cam* | `Advertising` | 🟢 **Live** | 357 ms | ✓ | [Manifest ↗](https://9badges25mm.cam/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/9badges25mm.cam) |
| **[9punto5.cl](https://9punto5.cl)**<br>*cl.9punto5/application-preparation* | `Event-based` | 🟢 **Live** | 103 ms | ✓ | [Manifest ↗](https://9punto5.cl/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/9punto5.cl) |
| **[9to5sas.com](https://9to5sas.com)**<br>*9to5sas.com* | `Non-profit` | 🟢 **Live** | 125 ms | ✓ | [Manifest ↗](https://9to5sas.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/9to5sas.com) |
| **[a1.gallery](https://a1.gallery)**<br>*a1.gallery* | `Advertising` | 🟢 **Live** | 267 ms | 17 | [Manifest ↗](https://a1.gallery/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/a1.gallery) |
| **[a1machinery.com](https://a1machinery.com)**<br>*a1machinery.com* | `Rental and Sales` | 🟢 **Live** | 957 ms | ✓ | [Manifest ↗](https://a1machinery.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/a1machinery.com) |
| **[aaaa.com.hk](https://aaaa.com.hk)**<br>*aaaa.com.hk* | `Membership fees` | 🟢 **Live** | 655 ms | ✓ | [Manifest ↗](https://aaaa.com.hk/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aaaa.com.hk) |
| **[aaapeks.info](https://aaapeks.info)**<br>*aaapeks.info* | `Event Organization` | 🟢 **Live** | 842 ms | ✓ | [Manifest ↗](https://aaapeks.info/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aaapeks.info) |
| **[aaat.com](https://aaat.com)**<br>*aaat.com* | `Freight Brokerage` | 🟢 **Live** | 152 ms | ✓ | [Manifest ↗](https://aaat.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aaat.com) |
| **[aabraga.pt](https://aabraga.pt)**<br>*pt.aabraga/site-content* | `Non-profit Organization` | 🟢 **Live** | 306 ms | ✓ | [Manifest ↗](https://aabraga.pt/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aabraga.pt) |
| **[aambfs.edu.eg](https://aambfs.edu.eg)**<br>*aambfs.edu.eg* | `Tuition fees and partnerships` | 🟢 **Live** | 113 ms | ✓ | [Manifest ↗](https://aambfs.edu.eg/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aambfs.edu.eg) |
| **[aambfs.org](https://aambfs.org)**<br>*aambfs.org* | `Tuition Fees` | 🟢 **Live** | 95 ms | ✓ | [Manifest ↗](https://aambfs.org/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aambfs.org) |
| **[aamcooverlandpark.com](https://aamcooverlandpark.com)**<br>*aamcooverlandpark.com* | `Service-based` | 🟢 **Live** | 821 ms | ✓ | [Manifest ↗](https://aamcooverlandpark.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aamcooverlandpark.com) |
| **[aaplagaon.com](https://aaplagaon.com)**<br>*aaplagaon.com* | `Accommodation and Activity Bookings` | 🟢 **Live** | 747 ms | ✓ | [Manifest ↗](https://aaplagaon.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aaplagaon.com) |
| **[aave.com](https://aave.com)**<br>*com.aave/mcp* | `Open-source software development, decentralized finance platform` | 🟢 **Live** | 154 ms | 53 | [Manifest ↗](https://aave.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aave.com) |
| **[aave.org](https://aave.org)**<br>*com.aave/mcp* | `Open-source protocol with decentralized governance` | 🟢 **Live** | 172 ms | 53 | [Manifest ↗](https://aave.org/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aave.org) |
| **[abaargroup.com](https://abaargroup.com)**<br>*abaargroup.com* | `Project-based Services` | 🟢 **Live** | 351 ms | ✓ | [Manifest ↗](https://abaargroup.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/abaargroup.com) |
| **[abadimex.com](https://abadimex.com)**<br>*abadimex.com* | `B2B Sales` | 🟢 **Live** | 104 ms | ✓ | [Manifest ↗](https://abadimex.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/abadimex.com) |
| **[abainsurance.com](https://abainsurance.com)**<br>*ABA Insurance Program* | `Affinity marketing` | 🟢 **Live** | 1007 ms | ✓ | [Manifest ↗](https://abainsurance.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/abainsurance.com) |
| **[abaliogluyem.com.tr](https://abaliogluyem.com.tr)**<br>*abaliogluyem.com.tr* | `B2B Sales` | 🟢 **Live** | 222 ms | ✓ | [Manifest ↗](https://abaliogluyem.com.tr/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/abaliogluyem.com.tr) |
| **[abeille-transport.ch](https://abeille-transport.ch)**<br>*abeille-transport.ch* | `Service-based` | 🟢 **Live** | 350 ms | ✓ | [Manifest ↗](https://abeille-transport.ch/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/abeille-transport.ch) |
| **[actava.ai](https://actava.ai)**<br>*actava.ai* | `SaaS subscription` | 🟢 **Live** | 352 ms | ✓ | [Manifest ↗](https://actava.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/actava.ai) |
| **[adsgram.ai](https://adsgram.ai)**<br>*ai.adsgram/site* | `Advertising (CPM)` | 🟢 **Live** | 156 ms | ✓ | [Manifest ↗](https://adsgram.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/adsgram.ai) |
| **[agilitywriter.ai](https://agilitywriter.ai)**<br>*Agility Writer* | `SaaS_subscription` | 🟢 **Live** | 119 ms | ✓ | [Manifest ↗](https://agilitywriter.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/agilitywriter.ai) |
| **[aidelly.ai](https://aidelly.ai)**<br>*Aidelly MCP Server* | `SaaS subscription` | 🟢 **Live** | 414 ms | ✓ | [Manifest ↗](https://aidelly.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aidelly.ai) |
| **[aipufy.ai](https://aipufy.ai)**<br>*aipufy.ai* | `Consulting Services` | 🟢 **Live** | 351 ms | 1 | [Manifest ↗](https://aipufy.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aipufy.ai) |
| **[airvago.ai](https://airvago.ai)**<br>*airvago.ai* | `Freemium (with in-app purchases)` | 🟢 **Live** | 4329 ms | 4 | [Manifest ↗](https://airvago.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/airvago.ai) |
| **[amdahl.ai](https://amdahl.ai)**<br>*amdahl.ai* | `SaaS subscription` | 🟢 **Live** | 96 ms | ✓ | [Manifest ↗](https://amdahl.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/amdahl.ai) |
| **[anonity.ai](https://anonity.ai)**<br>*anonity.ai* | `Unknown` | 🟢 **Live** | 257 ms | ✓ | [Manifest ↗](https://anonity.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/anonity.ai) |
| **[applyboost.ai](https://applyboost.ai)**<br>*applyboost.ai* | `SaaS subscription` | 🟢 **Live** | 414 ms | ✓ | [Manifest ↗](https://applyboost.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/applyboost.ai) |
| **[artificialstudio.ai](https://artificialstudio.ai)**<br>*artificialstudio.ai* | `SaaS subscription` | 🟢 **Live** | 492 ms | ✓ | [Manifest ↗](https://artificialstudio.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/artificialstudio.ai) |
| **[askcory.ai](https://askcory.ai)**<br>*ai.askcory/askcory* | `SaaS subscription` | 🟢 **Live** | 387 ms | ✓ | [Manifest ↗](https://askcory.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/askcory.ai) |
| **[askiot.ai](https://askiot.ai)**<br>*askiot.ai* | `SaaS subscription` | 🟢 **Live** | 1697 ms | ✓ | [Manifest ↗](https://askiot.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/askiot.ai) |
| **[askpoppy.ai](https://askpoppy.ai)**<br>*askpoppy.ai* | `Freemium with premium subscriptions` | 🟢 **Live** | 231 ms | ✓ | [Manifest ↗](https://askpoppy.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/askpoppy.ai) |
| **[atendro.ai](https://atendro.ai)**<br>*ai.atendro/atendro-mcp* | `SaaS_subscription` | 🟢 **Live** | 157 ms | ✓ | [Manifest ↗](https://atendro.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/atendro.ai) |
| **[atlaswork.ai](https://atlaswork.ai)**<br>*Atlas* | `SaaS subscription` | 🟢 **Live** | 168 ms | ✓ | [Manifest ↗](https://atlaswork.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/atlaswork.ai) |
| **[auftrag.ai](https://auftrag.ai)**<br>*auftrag.ai* | `Subscription-based SaaS` | 🟢 **Live** | 282 ms | ✓ | [Manifest ↗](https://auftrag.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/auftrag.ai) |
| **[augmtd.ai](https://augmtd.ai)**<br>*augmtd.ai* | `SaaS subscription` | 🟢 **Live** | 169 ms | 3 | [Manifest ↗](https://augmtd.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/augmtd.ai) |
| **[aurolabs.ai](https://aurolabs.ai)**<br>*aurolabs.ai* | `SaaS subscription` | 🟢 **Live** | 155 ms | ✓ | [Manifest ↗](https://aurolabs.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aurolabs.ai) |
| **[avpro.ai](https://avpro.ai)**<br>*avpro.ai* | `SaaS subscription` | 🟢 **Live** | 1456 ms | ✓ | [Manifest ↗](https://avpro.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/avpro.ai) |
| **[awamer.ai](https://awamer.ai)**<br>*awamer* | `SaaS subscription` | 🟢 **Live** | 690 ms | 7 | [Manifest ↗](https://awamer.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/awamer.ai) |
| **[backlight.ai](https://backlight.ai)**<br>*backlight.ai* | `SaaS subscription` | 🟢 **Live** | 202 ms | ✓ | [Manifest ↗](https://backlight.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/backlight.ai) |
| **[badcontent.ai](https://badcontent.ai)**<br>*DOOMSCROLLR MCP Remote* | `SaaS subscription` | 🟢 **Live** | 251 ms | ✓ | [Manifest ↗](https://badcontent.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/badcontent.ai) |
| **[berean.ai](https://berean.ai)**<br>*berean.ai* | `Freemium (with potential premium features)` | 🟢 **Live** | 258 ms | 5 | [Manifest ↗](https://berean.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/berean.ai) |
| **[bonnard.ai](https://bonnard.ai)**<br>*bonnard.ai* | `SaaS subscription` | 🟢 **Live** | 161 ms | ✓ | [Manifest ↗](https://bonnard.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/bonnard.ai) |
| **[brightfold.ai](https://brightfold.ai)**<br>*brightfold.ai* | `SaaS subscription` | 🟢 **Live** | 215 ms | ✓ | [Manifest ↗](https://brightfold.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/brightfold.ai) |
| **[brito.ai](https://brito.ai)**<br>*ai.brito/website* | `SaaS subscription` | 🟢 **Live** | 122 ms | ✓ | [Manifest ↗](https://brito.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/brito.ai) |
| **[buzzwatch.ai](https://buzzwatch.ai)**<br>*buzzwatch.ai* | `SaaS subscription` | 🟢 **Live** | 136 ms | ✓ | [Manifest ↗](https://buzzwatch.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/buzzwatch.ai) |
| **[byark.ai](https://byark.ai)**<br>*byark.ai* | `SaaS subscription` | 🟢 **Live** | 602 ms | ✓ | [Manifest ↗](https://byark.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/byark.ai) |
| **[callcast.ai](https://callcast.ai)**<br>*callcast.ai* | `SaaS subscription` | 🟢 **Live** | 709 ms | ✓ | [Manifest ↗](https://callcast.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/callcast.ai) |
| **[channlworks.ai](https://channlworks.ai)**<br>*channlworks.ai* | `SaaS subscription` | 🟢 **Live** | 173 ms | ✓ | [Manifest ↗](https://channlworks.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/channlworks.ai) |
| **[chronoflow.ai](https://chronoflow.ai)**<br>*chronoflow.ai* | `SaaS subscription` | 🟢 **Live** | 188 ms | ✓ | [Manifest ↗](https://chronoflow.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/chronoflow.ai) |
| **[clairemed.ai](https://clairemed.ai)**<br>*Claire Knowledge MCP* | `SaaS subscription` | 🟢 **Live** | 117 ms | 4 | [Manifest ↗](https://clairemed.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/clairemed.ai) |
| **[colorfun.ai](https://colorfun.ai)**<br>*colorfun.ai* | `Advertising` | 🟢 **Live** | 720 ms | ✓ | [Manifest ↗](https://colorfun.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/colorfun.ai) |
| **[concurred.ai](https://concurred.ai)**<br>*concurred.ai* | `SaaS subscription` | 🟢 **Live** | 208 ms | ✓ | [Manifest ↗](https://concurred.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/concurred.ai) |
| **[contextual.ai](https://contextual.ai)**<br>*contextual.ai* | `SaaS subscription` | 🟢 **Live** | 209 ms | ✓ | [Manifest ↗](https://contextual.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/contextual.ai) |
| **[coot.ai](https://coot.ai)**<br>*coot.ai* | `SaaS subscription` | 🟢 **Live** | 202 ms | ✓ | [Manifest ↗](https://coot.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/coot.ai) |
| **[curata.ai](https://curata.ai)**<br>*curata.ai* | `Freemium (App Store)` | 🟢 **Live** | 223 ms | ✓ | [Manifest ↗](https://curata.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/curata.ai) |
| **[datalegion.ai](https://datalegion.ai)**<br>*datalegion.ai* | `B2B Services` | 🟢 **Live** | 362 ms | 9 | [Manifest ↗](https://datalegion.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/datalegion.ai) |
| **[dearben.ai](https://dearben.ai)**<br>*dearben.ai* | `SaaS subscription` | 🟢 **Live** | 446 ms | ✓ | [Manifest ↗](https://dearben.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/dearben.ai) |
| **[deepparser.ai](https://deepparser.ai)**<br>*deepparser.ai* | `SaaS subscription` | 🟢 **Live** | 445 ms | ✓ | [Manifest ↗](https://deepparser.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/deepparser.ai) |
| **[directcare.ai](https://directcare.ai)**<br>*directcare.ai* | `Subscription-based` | 🟢 **Live** | 341 ms | 3 | [Manifest ↗](https://directcare.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/directcare.ai) |
| **[doccentral.ai](https://doccentral.ai)**<br>*doccentral.ai* | `SaaS subscription` | 🟢 **Live** | 1227 ms | 5 | [Manifest ↗](https://doccentral.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/doccentral.ai) |
| **[docsbot.ai](https://docsbot.ai)**<br>*docsbot.ai* | `SaaS subscription` | 🟢 **Live** | 168 ms | 3 | [Manifest ↗](https://docsbot.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/docsbot.ai) |
| **[domainsales.ai](https://domainsales.ai)**<br>*com.youspot/youspot* | `E-commerce` | 🟢 **Live** | 432 ms | 111 | [Manifest ↗](https://domainsales.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/domainsales.ai) |
| **[dynamia.ai](https://dynamia.ai)**<br>*dynamia.ai* | `SaaS subscription` | 🟢 **Live** | 174 ms | 2 | [Manifest ↗](https://dynamia.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/dynamia.ai) |
| **[dynoraptors.ai](https://dynoraptors.ai)**<br>*dynoraptors.ai* | `SaaS subscription` | 🟢 **Live** | 883 ms | ✓ | [Manifest ↗](https://dynoraptors.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/dynoraptors.ai) |
| **[ecoforce.ai](https://ecoforce.ai)**<br>*ecoforce.ai* | `SaaS subscription` | 🟢 **Live** | 965 ms | ✓ | [Manifest ↗](https://ecoforce.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ecoforce.ai) |
| **[effo.ai](https://effo.ai)**<br>*effo.ai* | `SaaS subscription` | 🟢 **Live** | 243 ms | ✓ | [Manifest ↗](https://effo.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/effo.ai) |
| **[epicweb.ai](https://epicweb.ai)**<br>*epicweb.ai* | `SaaS subscription` | 🟢 **Live** | 538 ms | ✓ | [Manifest ↗](https://epicweb.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/epicweb.ai) |
| **[extruct.ai](https://extruct.ai)**<br>*extruct.ai* | `SaaS subscription` | 🟢 **Live** | 396 ms | ✓ | [Manifest ↗](https://extruct.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/extruct.ai) |
| **[flamel.ai](https://flamel.ai)**<br>*flamel.ai* | `SaaS subscription` | 🟢 **Live** | 367 ms | 9 | [Manifest ↗](https://flamel.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/flamel.ai) |
| **[fonestorm.ai](https://fonestorm.ai)**<br>*fonestorm.ai* | `SaaS subscription` | 🟢 **Live** | 293 ms | 1 | [Manifest ↗](https://fonestorm.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/fonestorm.ai) |
| **[fonzi.ai](https://fonzi.ai)**<br>*fonzi.ai* | `SaaS subscription` | 🟢 **Live** | 178 ms | ✓ | [Manifest ↗](https://fonzi.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/fonzi.ai) |
| **[forex-gpt.ai](https://forex-gpt.ai)**<br>*forex-gpt.ai* | `SaaS subscription with free and paid plans` | 🟢 **Live** | 247 ms | ✓ | [Manifest ↗](https://forex-gpt.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/forex-gpt.ai) |
| **[fortunegames.ai](https://fortunegames.ai)**<br>*fortunegames.ai* | `Advertising` | 🟢 **Live** | 93 ms | ✓ | [Manifest ↗](https://fortunegames.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/fortunegames.ai) |
| **[fynex.ai](https://fynex.ai)**<br>*fynex.ai* | `SaaS subscription` | 🟢 **Live** | 286 ms | ✓ | [Manifest ↗](https://fynex.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/fynex.ai) |
| **[gaiotech.ai](https://gaiotech.ai)**<br>*gaiotech.ai* | `SaaS subscription` | 🟢 **Live** | 346 ms | ✓ | [Manifest ↗](https://gaiotech.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/gaiotech.ai) |
| **[getminds.ai](https://getminds.ai)**<br>*getminds.ai* | `Services` | 🟢 **Live** | 302 ms | 23 | [Manifest ↗](https://getminds.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/getminds.ai) |
| **[getperspective.ai](https://getperspective.ai)**<br>*getperspective.ai* | `SaaS subscription` | 🟢 **Live** | 190 ms | ✓ | [Manifest ↗](https://getperspective.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/getperspective.ai) |
| **[getscribe.ai](https://getscribe.ai)**<br>*getscribe.ai* | `SaaS_subscription` | 🟢 **Live** | 335 ms | ✓ | [Manifest ↗](https://getscribe.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/getscribe.ai) |
| **[glasp.ai](https://glasp.ai)**<br>*glasp.ai* | `Freemium with Premium Subscription` | 🟢 **Live** | 176 ms | 9 | [Manifest ↗](https://glasp.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/glasp.ai) |
| **[glowtogether.ai](https://glowtogether.ai)**<br>*glowtogether.ai* | `SaaS subscription` | 🟢 **Live** | 211 ms | ✓ | [Manifest ↗](https://glowtogether.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/glowtogether.ai) |
| **[godric.ai](https://godric.ai)**<br>*godric.ai* | `SaaS subscription` | 🟢 **Live** | 493 ms | ✓ | [Manifest ↗](https://godric.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/godric.ai) |
| **[gritworks.ai](https://gritworks.ai)**<br>*gritworks.ai* | `SaaS subscription` | 🟢 **Live** | 658 ms | ✓ | [Manifest ↗](https://gritworks.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/gritworks.ai) |
| **[hurdle.ai](https://hurdle.ai)**<br>*hurdle.ai* | `SaaS subscription` | 🟢 **Live** | 399 ms | ✓ | [Manifest ↗](https://hurdle.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/hurdle.ai) |
| **[hypercube.ai](https://hypercube.ai)**<br>*pinecone-marketing* | `SaaS_subscription` | 🟢 **Live** | 444 ms | ✓ | [Manifest ↗](https://hypercube.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/hypercube.ai) |
| **[ibl.ai](https://ibl.ai)**<br>*ibl.ai* | `SaaS subscription` | 🟢 **Live** | 218 ms | 1 | [Manifest ↗](https://ibl.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ibl.ai) |
| **[ihatepeople.ai](https://ihatepeople.ai)**<br>*ihatepeople.ai* | `Advertising` | 🟢 **Live** | 283 ms | ✓ | [Manifest ↗](https://ihatepeople.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ihatepeople.ai) |
| **[incentro.ai](https://incentro.ai)**<br>*incentro.ai* | `Consulting Services` | 🟢 **Live** | 448 ms | ✓ | [Manifest ↗](https://incentro.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/incentro.ai) |
| **[inspiresa.ai](https://inspiresa.ai)**<br>*inspiresa.ai* | `SaaS subscription` | 🟢 **Live** | 280 ms | ✓ | [Manifest ↗](https://inspiresa.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/inspiresa.ai) |
| **[intelfactor.ai](https://intelfactor.ai)**<br>*intelfactor.ai* | `SaaS subscription` | 🟢 **Live** | 342 ms | ✓ | [Manifest ↗](https://intelfactor.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/intelfactor.ai) |
| **[intelligentlabs.ai](https://intelligentlabs.ai)**<br>*hermes-chart-mcp* | `SaaS subscription` | 🟢 **Live** | 229 ms | ✓ | [Manifest ↗](https://intelligentlabs.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/intelligentlabs.ai) |
| **[ithelps.ai](https://ithelps.ai)**<br>*ithelps.ai* | `SaaS subscription` | 🟢 **Live** | 379 ms | ✓ | [Manifest ↗](https://ithelps.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ithelps.ai) |
| **[jamout.ai](https://jamout.ai)**<br>*jamout.ai* | `Subscription-based (Club Jam) and Consulting Services` | 🟢 **Live** | 174 ms | ✓ | [Manifest ↗](https://jamout.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/jamout.ai) |
| **[jasnow.ai](https://jasnow.ai)**<br>*jasnow.ai* | `SaaS subscription` | 🟢 **Live** | 316 ms | ✓ | [Manifest ↗](https://jasnow.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/jasnow.ai) |
| **[jellypod.ai](https://jellypod.ai)**<br>*com.jellypod/jellypod* | `SaaS subscription` | 🟢 **Live** | 366 ms | ✓ | [Manifest ↗](https://jellypod.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/jellypod.ai) |
| **[jobpal.ai](https://jobpal.ai)**<br>*jobpal.ai* | `SaaS subscription` | 🟢 **Live** | 536 ms | ✓ | [Manifest ↗](https://jobpal.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/jobpal.ai) |
| **[jupitex.ai](https://jupitex.ai)**<br>*jupitex.ai* | `Subscription-based` | 🟢 **Live** | 642 ms | 4 | [Manifest ↗](https://jupitex.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/jupitex.ai) |
| **[kribu.ai](https://kribu.ai)**<br>*kribu.ai* | `Consulting Services` | 🟢 **Live** | 120 ms | ✓ | [Manifest ↗](https://kribu.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/kribu.ai) |
| **[kw.ai](https://kw.ai)**<br>*kw.ai* | `SaaS subscription` | 🟢 **Live** | 1011 ms | ✓ | [Manifest ↗](https://kw.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/kw.ai) |
| **[lastmileinc.ai](https://lastmileinc.ai)**<br>*lastmileinc.ai* | `SaaS subscription` | 🟢 **Live** | 297 ms | 4 | [Manifest ↗](https://lastmileinc.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/lastmileinc.ai) |
| **[launchdub.ai](https://launchdub.ai)**<br>*launchdub.ai* | `Professional Services` | 🟢 **Live** | 319 ms | 2 | [Manifest ↗](https://launchdub.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/launchdub.ai) |
| **[leethi.ai](https://leethi.ai)**<br>*leethi.ai* | `Subscription-based` | 🟢 **Live** | 837 ms | ✓ | [Manifest ↗](https://leethi.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/leethi.ai) |
| **[legalbenchmarks.ai](https://legalbenchmarks.ai)**<br>*legalbenchmarks.ai* | `Non-profit, funded by grants or sponsorships` | 🟢 **Live** | 408 ms | ✓ | [Manifest ↗](https://legalbenchmarks.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/legalbenchmarks.ai) |
| **[lensgo.ai](https://lensgo.ai)**<br>*lensgo.ai* | `SaaS subscription` | 🟢 **Live** | 324 ms | 4 | [Manifest ↗](https://lensgo.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/lensgo.ai) |
| **[lessmanual.ai](https://lessmanual.ai)**<br>*lessmanual.ai* | `SaaS subscription` | 🟢 **Live** | 395 ms | ✓ | [Manifest ↗](https://lessmanual.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/lessmanual.ai) |
| **[leucine.ai](https://leucine.ai)**<br>*leucine.ai* | `SaaS subscription` | 🟢 **Live** | 102 ms | ✓ | [Manifest ↗](https://leucine.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/leucine.ai) |
| **[lexxy.ai](https://lexxy.ai)**<br>*lexxy.ai* | `SaaS subscription` | 🟢 **Live** | 835 ms | ✓ | [Manifest ↗](https://lexxy.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/lexxy.ai) |
| **[librebot.ai](https://librebot.ai)**<br>*librebot.ai* | `SaaS subscription` | 🟢 **Live** | 99 ms | ✓ | [Manifest ↗](https://librebot.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/librebot.ai) |
| **[lifescenario.ai](https://lifescenario.ai)**<br>*lifescenario.ai* | `Subscription` | 🟢 **Live** | 205 ms | ✓ | [Manifest ↗](https://lifescenario.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/lifescenario.ai) |
| **[liftli.ai](https://liftli.ai)**<br>*liftli* | `SaaS subscription` | 🟢 **Live** | 141 ms | ✓ | [Manifest ↗](https://liftli.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/liftli.ai) |
| **[listenlabs.ai](https://listenlabs.ai)**<br>*listenlabs.ai* | `SaaS subscription` | 🟢 **Live** | 252 ms | ✓ | [Manifest ↗](https://listenlabs.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/listenlabs.ai) |
| **[listnr.ai](https://listnr.ai)**<br>*listnr.ai* | `SaaS subscription` | 🟢 **Live** | 165 ms | ✓ | [Manifest ↗](https://listnr.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/listnr.ai) |
| **[liveframe.ai](https://liveframe.ai)**<br>*liveframe.ai* | `SaaS subscription` | 🟢 **Live** | 174 ms | 1 | [Manifest ↗](https://liveframe.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/liveframe.ai) |
| **[llmpulse.ai](https://llmpulse.ai)**<br>*llmpulse.ai* | `SaaS subscription` | 🟢 **Live** | 122 ms | ✓ | [Manifest ↗](https://llmpulse.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/llmpulse.ai) |
| **[lumify.ai](https://lumify.ai)**<br>*lumify.ai* | `SaaS subscription` | 🟢 **Live** | 521 ms | ✓ | [Manifest ↗](https://lumify.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/lumify.ai) |
| **[magichour.ai](https://magichour.ai)**<br>*magichour.ai* | `Freemium (with premium features)` | 🟢 **Live** | 132 ms | ✓ | [Manifest ↗](https://magichour.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/magichour.ai) |
| **[mainstreetwealth.ai](https://mainstreetwealth.ai)**<br>*mainstreetwealth.ai* | `Commission-based` | 🟢 **Live** | 308 ms | 5 | [Manifest ↗](https://mainstreetwealth.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/mainstreetwealth.ai) |
| **[makeform.ai](https://makeform.ai)**<br>*makeform.ai* | `SaaS subscription` | 🟢 **Live** | 475 ms | ✓ | [Manifest ↗](https://makeform.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/makeform.ai) |
| **[marketbetter.ai](https://marketbetter.ai)**<br>*marketbetter.ai* | `SaaS subscription` | 🟢 **Live** | 291 ms | ✓ | [Manifest ↗](https://marketbetter.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/marketbetter.ai) |
| **[marketdata.ai](https://marketdata.ai)**<br>*ai.firmfact/mcp* | `SaaS subscription` | 🟢 **Live** | 236 ms | ✓ | [Manifest ↗](https://marketdata.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/marketdata.ai) |
| **[marketsu.ai](https://marketsu.ai)**<br>*marketsu.ai* | `Consulting Services` | 🟢 **Live** | 136 ms | ✓ | [Manifest ↗](https://marketsu.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/marketsu.ai) |
| **[marvenn.ai](https://marvenn.ai)**<br>*Marvenn MCP Server* | `SaaS subscription` | 🟢 **Live** | 464 ms | 9 | [Manifest ↗](https://marvenn.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/marvenn.ai) |
| **[mentu.ai](https://mentu.ai)**<br>*mentu.ai* | `Service-based subscription` | 🟢 **Live** | 333 ms | 3 | [Manifest ↗](https://mentu.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/mentu.ai) |
| **[meritex.ai](https://meritex.ai)**<br>*meritex.ai* | `SaaS subscription` | 🟢 **Live** | 216 ms | 18 | [Manifest ↗](https://meritex.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/meritex.ai) |
| **[migma.ai](https://migma.ai)**<br>*ai.migma/mcp* | `SaaS subscription` | 🟢 **Live** | 362 ms | ✓ | [Manifest ↗](https://migma.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/migma.ai) |
| **[myarchivist.ai](https://myarchivist.ai)**<br>*myarchivist.ai* | `SaaS subscription` | 🟢 **Live** | 365 ms | ✓ | [Manifest ↗](https://myarchivist.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/myarchivist.ai) |
| **[myess.ai](https://myess.ai)**<br>*myess.ai* | `SaaS subscription` | 🟢 **Live** | 755 ms | ✓ | [Manifest ↗](https://myess.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/myess.ai) |
| **[mypaperwork.ai](https://mypaperwork.ai)**<br>*mypaperwork.ai* | `SaaS subscription` | 🟢 **Live** | 890 ms | 2 | [Manifest ↗](https://mypaperwork.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/mypaperwork.ai) |
| **[negu.ai](https://negu.ai)**<br>*negu.ai* | `SaaS subscription` | 🟢 **Live** | 622 ms | ✓ | [Manifest ↗](https://negu.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/negu.ai) |
| **[neteon.ai](https://neteon.ai)**<br>*neteon.ai* | `Hardware Sales` | 🟢 **Live** | 370 ms | ✓ | [Manifest ↗](https://neteon.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/neteon.ai) |
| **[nextecontech.ai](https://nextecontech.ai)**<br>*nextecontech.ai* | `Unknown` | 🟢 **Live** | 157 ms | ✓ | [Manifest ↗](https://nextecontech.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/nextecontech.ai) |
| **[norg.ai](https://norg.ai)**<br>*norg.ai* | `SaaS subscription` | 🟢 **Live** | 262 ms | ✓ | [Manifest ↗](https://norg.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/norg.ai) |
| **[ooomg.ai](https://ooomg.ai)**<br>*ooomg.ai* | `SaaS subscription` | 🟢 **Live** | 136 ms | ✓ | [Manifest ↗](https://ooomg.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ooomg.ai) |
| **[optmzr.ai](https://optmzr.ai)**<br>*optmzr.ai* | `Consulting Services` | 🟢 **Live** | 98 ms | ✓ | [Manifest ↗](https://optmzr.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/optmzr.ai) |
| **[originalvoices.ai](https://originalvoices.ai)**<br>*originalvoices.ai* | `SaaS subscription` | 🟢 **Live** | 276 ms | ✓ | [Manifest ↗](https://originalvoices.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/originalvoices.ai) |
| **[orizn.ai](https://orizn.ai)**<br>*orizn.ai* | `Consulting Services` | 🟢 **Live** | 184 ms | 5 | [Manifest ↗](https://orizn.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/orizn.ai) |
| **[otomasyon.ai](https://otomasyon.ai)**<br>*otomasyon.ai* | `SaaS subscription` | 🟢 **Live** | 473 ms | ✓ | [Manifest ↗](https://otomasyon.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/otomasyon.ai) |
| **[pageindex.ai](https://pageindex.ai)**<br>*ai.pageindex/pageindex* | `SaaS subscription` | 🟢 **Live** | 222 ms | ✓ | [Manifest ↗](https://pageindex.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/pageindex.ai) |
| **[plantcam.ai](https://plantcam.ai)**<br>*plantcam.ai* | `SaaS subscription` | 🟢 **Live** | 1509 ms | ✓ | [Manifest ↗](https://plantcam.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/plantcam.ai) |
| **[pmtoolkit.ai](https://pmtoolkit.ai)**<br>*pmtoolkit.ai* | `Freemium Subscription` | 🟢 **Live** | 269 ms | ✓ | [Manifest ↗](https://pmtoolkit.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/pmtoolkit.ai) |
| **[pocketgirlfriend.ai](https://pocketgirlfriend.ai)**<br>*pocketgirlfriend.ai* | `Premium Subscription` | 🟢 **Live** | 683 ms | ✓ | [Manifest ↗](https://pocketgirlfriend.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/pocketgirlfriend.ai) |
| **[pocketromance.ai](https://pocketromance.ai)**<br>*pocketromance.ai* | `Subscription or Freemium` | 🟢 **Live** | 722 ms | ✓ | [Manifest ↗](https://pocketromance.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/pocketromance.ai) |
| **[postcodeproperty.ai](https://postcodeproperty.ai)**<br>*PostcodeProperty.ai* | `SaaS subscription` | 🟢 **Live** | 602 ms | ✓ | [Manifest ↗](https://postcodeproperty.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/postcodeproperty.ai) |
| **[posteverywhere.ai](https://posteverywhere.ai)**<br>*posteverywhere.ai* | `SaaS subscription` | 🟢 **Live** | 193 ms | 5 | [Manifest ↗](https://posteverywhere.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/posteverywhere.ai) |
| **[postnitro.ai](https://postnitro.ai)**<br>*ai.postnitro/mcp* | `SaaS subscription` | 🟢 **Live** | 170 ms | ✓ | [Manifest ↗](https://postnitro.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/postnitro.ai) |
| **[precise.ai](https://precise.ai)**<br>*precise.ai* | `SaaS subscription` | 🟢 **Live** | 207 ms | ✓ | [Manifest ↗](https://precise.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/precise.ai) |
| **[prome.ai](https://prome.ai)**<br>*prome.ai* | `Selling Software` | 🟢 **Live** | 178 ms | 1 | [Manifest ↗](https://prome.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/prome.ai) |
| **[proptonomy.ai](https://proptonomy.ai)**<br>*proptonomy* | `Subscription-based service` | 🟢 **Live** | 469 ms | ✓ | [Manifest ↗](https://proptonomy.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/proptonomy.ai) |
| **[qdtech.ai](https://qdtech.ai)**<br>*qdtech.ai* | `SaaS subscription` | 🟢 **Live** | 938 ms | ✓ | [Manifest ↗](https://qdtech.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/qdtech.ai) |
| **[questom.ai](https://questom.ai)**<br>*questom.ai* | `SaaS_subscription` | 🟢 **Live** | 376 ms | ✓ | [Manifest ↗](https://questom.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/questom.ai) |
| **[raconte.ai](https://raconte.ai)**<br>*ai.raconte/raconte* | `SaaS subscription` | 🟢 **Live** | 354 ms | 8 | [Manifest ↗](https://raconte.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/raconte.ai) |
| **[render.ai](https://render.ai)**<br>*render.ai* | `SaaS subscription` | 🟢 **Live** | 150 ms | ✓ | [Manifest ↗](https://render.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/render.ai) |
| **[revo.ai](https://revo.ai)**<br>*revo.ai* | `SaaS subscription` | 🟢 **Live** | 379 ms | ✓ | [Manifest ↗](https://revo.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/revo.ai) |
| **[robauto.ai](https://robauto.ai)**<br>*robauto.ai* | `Services` | 🟢 **Live** | 301 ms | 28 | [Manifest ↗](https://robauto.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/robauto.ai) |
| **[rootdata.ai](https://rootdata.ai)**<br>*Root Data Public MCP Server* | `SaaS subscription` | 🟢 **Live** | 618 ms | 8 | [Manifest ↗](https://rootdata.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/rootdata.ai) |
| **[rootsignals.ai](https://rootsignals.ai)**<br>*rootsignals.ai* | `SaaS subscription` | 🟢 **Live** | 313 ms | ✓ | [Manifest ↗](https://rootsignals.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/rootsignals.ai) |
| **[ruleo.ai](https://ruleo.ai)**<br>*ruleo.ai* | `SaaS subscription` | 🟢 **Live** | 898 ms | ✓ | [Manifest ↗](https://ruleo.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ruleo.ai) |
| **[secureprivacy.ai](https://secureprivacy.ai)**<br>*secureprivacy.ai* | `SaaS subscription` | 🟢 **Live** | 117 ms | ✓ | [Manifest ↗](https://secureprivacy.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/secureprivacy.ai) |
| **[shaprice.ai](https://shaprice.ai)**<br>*shaprice.ai* | `Paid subscriptions and courses` | 🟢 **Live** | 199 ms | ✓ | [Manifest ↗](https://shaprice.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/shaprice.ai) |
| **[shareofmodel.ai](https://shareofmodel.ai)**<br>*shareofmodel.ai* | `SaaS subscription` | 🟢 **Live** | 104 ms | ✓ | [Manifest ↗](https://shareofmodel.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/shareofmodel.ai) |
| **[sharpe.ai](https://sharpe.ai)**<br>*sharpe.ai* | `SaaS subscription` | 🟢 **Live** | 285 ms | ✓ | [Manifest ↗](https://sharpe.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/sharpe.ai) |
| **[shunyalabs.ai](https://shunyalabs.ai)**<br>*shunyalabs.ai* | `SaaS subscription` | 🟢 **Live** | 283 ms | ✓ | [Manifest ↗](https://shunyalabs.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/shunyalabs.ai) |
| **[smartmaya.ai](https://smartmaya.ai)**<br>*Smart Maya AI* | `SaaS subscription` | 🟢 **Live** | 302 ms | ✓ | [Manifest ↗](https://smartmaya.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/smartmaya.ai) |
| **[sociologic.ai](https://sociologic.ai)**<br>*sociologic.ai* | `SaaS subscription` | 🟢 **Live** | 400 ms | ✓ | [Manifest ↗](https://sociologic.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/sociologic.ai) |
| **[spaitial.ai](https://spaitial.ai)**<br>*spaitial.ai* | `SaaS subscription` | 🟢 **Live** | 182 ms | 15 | [Manifest ↗](https://spaitial.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/spaitial.ai) |
| **[startuphub.ai](https://startuphub.ai)**<br>*startuphub.ai* | `Advertising & Sponsored Content` | 🟢 **Live** | 210 ms | 25 | [Manifest ↗](https://startuphub.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/startuphub.ai) |
| **[steadman.ai](https://steadman.ai)**<br>*Steadman* | `Consulting Services` | 🟢 **Live** | 217 ms | 3 | [Manifest ↗](https://steadman.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/steadman.ai) |
| **[stickyhive.ai](https://stickyhive.ai)**<br>*stickyhive* | `SaaS subscription` | 🟢 **Live** | 225 ms | 72 | [Manifest ↗](https://stickyhive.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/stickyhive.ai) |
| **[subramanya.ai](https://subramanya.ai)**<br>*subramanya.ai* | `Personal Blog` | 🟢 **Live** | 179 ms | ✓ | [Manifest ↗](https://subramanya.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/subramanya.ai) |
| **[supermemory.ai](https://supermemory.ai)**<br>*supermemory.ai* | `SaaS subscription` | 🟢 **Live** | 101 ms | 4 | [Manifest ↗](https://supermemory.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/supermemory.ai) |
| **[tailyx.ai](https://tailyx.ai)**<br>*tailyx.ai* | `SaaS subscription` | 🟢 **Live** | 496 ms | ✓ | [Manifest ↗](https://tailyx.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/tailyx.ai) |
| **[tapnow.ai](https://tapnow.ai)**<br>*tapnow.ai* | `SaaS subscription` | 🟢 **Live** | 1328 ms | ✓ | [Manifest ↗](https://tapnow.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/tapnow.ai) |
| **[teamcadence.ai](https://teamcadence.ai)**<br>*ai.teamcadence.marketing/site* | `SaaS subscription` | 🟢 **Live** | 123 ms | 3 | [Manifest ↗](https://teamcadence.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/teamcadence.ai) |
| **[thecatchup.ai](https://thecatchup.ai)**<br>*thecatchup.ai* | `SaaS subscription` | 🟢 **Live** | 510 ms | ✓ | [Manifest ↗](https://thecatchup.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/thecatchup.ai) |
| **[theorytest.ai](https://theorytest.ai)**<br>*theorytest.ai* | `SaaS subscription` | 🟢 **Live** | 201 ms | ✓ | [Manifest ↗](https://theorytest.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/theorytest.ai) |
| **[tineo.ai](https://tineo.ai)**<br>*tineo.ai* | `SaaS subscription` | 🟢 **Live** | 125 ms | ✓ | [Manifest ↗](https://tineo.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/tineo.ai) |
| **[traderman.ai](https://traderman.ai)**<br>*traderman.ai* | `Subscription-based with profit sharing` | 🟢 **Live** | 151 ms | ✓ | [Manifest ↗](https://traderman.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/traderman.ai) |
| **[vectify.ai](https://vectify.ai)**<br>*ai.pageindex/pageindex* | `SaaS subscription` | 🟢 **Live** | 441 ms | ✓ | [Manifest ↗](https://vectify.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/vectify.ai) |
| **[webotit.ai](https://webotit.ai)**<br>*webotit.ai* | `SaaS subscription` | 🟢 **Live** | 410 ms | 3 | [Manifest ↗](https://webotit.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/webotit.ai) |
| **[welcome.ai](https://welcome.ai)**<br>*welcome.ai* | `Advertising, Subscription` | 🟢 **Live** | 541 ms | ✓ | [Manifest ↗](https://welcome.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/welcome.ai) |
| **[writehuman.ai](https://writehuman.ai)**<br>*writehuman-mcp* | `SaaS subscription` | 🟢 **Live** | 236 ms | 3 | [Manifest ↗](https://writehuman.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/writehuman.ai) |
| **[88203.app](https://88203.app)**<br>*88203.app* | `Unknown` | 🔴 *Down* | - | ✓ | [Manifest ↗](https://88203.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/88203.app) |
| **[91wlcx.com](https://91wlcx.com)**<br>*91wlcx.com* | `Advertising` | 🔴 *Down* | - | ✓ | [Manifest ↗](https://91wlcx.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/91wlcx.com) |
| **[92bw.app](https://92bw.app)**<br>*92bw.app* | `Unknown` | 🔴 *Down* | - | ✓ | [Manifest ↗](https://92bw.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/92bw.app) |
| **[9p.mom](https://9p.mom)**<br>*9p.mom* | `Subscription` | 🔴 *Down* | - | ✓ | [Manifest ↗](https://9p.mom/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/9p.mom) |
| **[aainterlock.net](https://aainterlock.net)**<br>*aainterlock.net* | `Government Services` | 🔴 *Down* | - | ✓ | [Manifest ↗](https://aainterlock.net/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aainterlock.net) |
| **[chat-gpt-5.ai](https://chat-gpt-5.ai)**<br>*chat-gpt-5.ai* | `B2B SaaS` | 🔴 *Down* | - | ✓ | [Manifest ↗](https://chat-gpt-5.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/chat-gpt-5.ai) |
| **[gohan.ai](https://gohan.ai)**<br>*gohan.ai* | `Job Board` | 🔴 *Down* | - | ✓ | [Manifest ↗](https://gohan.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/gohan.ai) |

### 📊 Enterprise Intelligence & Analytics (14)

| Server / Host | Business Model | Status | Latency | Tools | Manifest | DomainScope Dossier |
|---|---|:---:|:---:|:---:|:---:|:---:|
| **[24streetdentalphoenix.com](https://24streetdentalphoenix.com)**<br>*24streetdentalphoenix.com* | `Private Practice` | 🟢 **Live** | 1088 ms | ✓ | [Manifest ↗](https://24streetdentalphoenix.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/24streetdentalphoenix.com) |
| **[abahanavillas.com](https://abahanavillas.com)**<br>*abahanavillas.com* | `Rental Income` | 🟢 **Live** | 344 ms | ✓ | [Manifest ↗](https://abahanavillas.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/abahanavillas.com) |
| **[anomalyarmor.ai](https://anomalyarmor.ai)**<br>*AnomalyArmor* | `SaaS subscription` | 🟢 **Live** | 711 ms | 43 | [Manifest ↗](https://anomalyarmor.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/anomalyarmor.ai) |
| **[bircle.ai](https://bircle.ai)**<br>*bircle.ai* | `SaaS subscription` | 🟢 **Live** | 172 ms | ✓ | [Manifest ↗](https://bircle.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/bircle.ai) |
| **[citationlab.ai](https://citationlab.ai)**<br>*CitationLab* | `SaaS subscription` | 🟢 **Live** | 143 ms | ✓ | [Manifest ↗](https://citationlab.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/citationlab.ai) |
| **[gococoa.ai](https://gococoa.ai)**<br>*cocoa-discovery-only* | `Consulting Services` | 🟢 **Live** | 155 ms | ✓ | [Manifest ↗](https://gococoa.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/gococoa.ai) |
| **[hordus.ai](https://hordus.ai)**<br>*hordus.ai* | `SaaS subscription` | 🟢 **Live** | 487 ms | 2 | [Manifest ↗](https://hordus.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/hordus.ai) |
| **[icube.ai](https://icube.ai)**<br>*icube.ai* | `SaaS subscription` | 🟢 **Live** | 1296 ms | ✓ | [Manifest ↗](https://icube.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/icube.ai) |
| **[integrativepeptides.ai](https://integrativepeptides.ai)**<br>*Royal MCP* | `Wholesale` | 🟢 **Live** | 1752 ms | ✓ | [Manifest ↗](https://integrativepeptides.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/integrativepeptides.ai) |
| **[internetofsustainability.ai](https://internetofsustainability.ai)**<br>*internetofsustainability.ai* | `SaaS_subscription` | 🟢 **Live** | 195 ms | ✓ | [Manifest ↗](https://internetofsustainability.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/internetofsustainability.ai) |
| **[kime.ai](https://kime.ai)**<br>*kime.ai* | `SaaS subscription` | 🟢 **Live** | 99 ms | ✓ | [Manifest ↗](https://kime.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/kime.ai) |
| **[mcpanalytics.ai](https://mcpanalytics.ai)**<br>*mcpanalytics.ai* | `SaaS subscription` | 🟢 **Live** | 768 ms | 28 | [Manifest ↗](https://mcpanalytics.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/mcpanalytics.ai) |
| **[trollwall.ai](https://trollwall.ai)**<br>*ai.trollwall/mcp* | `SaaS subscription` | 🟢 **Live** | 303 ms | ✓ | [Manifest ↗](https://trollwall.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/trollwall.ai) |
| **[biliki.ai](https://biliki.ai)**<br>*biliki.ai* | `Tour Package Sales` | 🔴 *Down* | - | ✓ | [Manifest ↗](https://biliki.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/biliki.ai) |

### 🔒 Cybersecurity & Infrastructure (15)

| Server / Host | Business Model | Status | Latency | Tools | Manifest | DomainScope Dossier |
|---|---|:---:|:---:|:---:|:---:|:---:|
| **[abckeys.net](https://abckeys.net)**<br>*abckeys.net* | `Service-based` | 🟢 **Live** | 107 ms | ✓ | [Manifest ↗](https://abckeys.net/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/abckeys.net) |
| **[ajwill.ai](https://ajwill.ai)**<br>*ajwill.ai* | `Consulting Services` | 🟢 **Live** | 103 ms | ✓ | [Manifest ↗](https://ajwill.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ajwill.ai) |
| **[certiv.ai](https://certiv.ai)**<br>*certiv.ai* | `Unknown` | 🟢 **Live** | 692 ms | ✓ | [Manifest ↗](https://certiv.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/certiv.ai) |
| **[getfast.ai](https://getfast.ai)**<br>*fit.kailo/kailo* | `SaaS subscription` | 🟢 **Live** | 286 ms | 62 | [Manifest ↗](https://getfast.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/getfast.ai) |
| **[imper.ai](https://imper.ai)**<br>*imper.ai* | `SaaS subscription` | 🟢 **Live** | 597 ms | ✓ | [Manifest ↗](https://imper.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/imper.ai) |
| **[racprojects.ai](https://racprojects.ai)**<br>*rac-projects-ai* | `SaaS subscription` | 🟢 **Live** | 630 ms | 5 | [Manifest ↗](https://racprojects.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/racprojects.ai) |
| **[refty.ai](https://refty.ai)**<br>*refty.ai* | `SaaS subscription` | 🟢 **Live** | 329 ms | ✓ | [Manifest ↗](https://refty.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/refty.ai) |
| **[sageox.ai](https://sageox.ai)**<br>*ai.sageox/sageox* | `Unknown` | 🟢 **Live** | 177 ms | 8 | [Manifest ↗](https://sageox.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/sageox.ai) |
| **[salespeak.ai](https://salespeak.ai)**<br>*salespeak.ai* | `SaaS subscription` | 🟢 **Live** | 143 ms | 1 | [Manifest ↗](https://salespeak.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/salespeak.ai) |
| **[securelend.ai](https://securelend.ai)**<br>*SecureLend* | `SaaS subscription` | 🟢 **Live** | 121 ms | ✓ | [Manifest ↗](https://securelend.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/securelend.ai) |
| **[securityrisk.ai](https://securityrisk.ai)**<br>*securityrisk.ai* | `SaaS subscription` | 🟢 **Live** | 99 ms | ✓ | [Manifest ↗](https://securityrisk.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/securityrisk.ai) |
| **[shiken.ai](https://shiken.ai)**<br>*ai.shiken/shiken* | `SaaS subscription` | 🟢 **Live** | 173 ms | 12 | [Manifest ↗](https://shiken.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/shiken.ai) |
| **[superschema.ai](https://superschema.ai)**<br>*SuperSchema MCP* | `SaaS subscription` | 🟢 **Live** | 270 ms | 3 | [Manifest ↗](https://superschema.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/superschema.ai) |
| **[telq.ai](https://telq.ai)**<br>*Telqai public information* | `B2B Services` | 🟢 **Live** | 141 ms | ✓ | [Manifest ↗](https://telq.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/telq.ai) |
| **[askyourdocs.ai](https://askyourdocs.ai)**<br>*askyourdocs.ai* | `Open Source` | 🔴 *Down* | - | ✓ | [Manifest ↗](https://askyourdocs.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/askyourdocs.ai) |

### 🛒 E-Commerce & Commercial Services (28)

| Server / Host | Business Model | Status | Latency | Tools | Manifest | DomainScope Dossier |
|---|---|:---:|:---:|:---:|:---:|:---:|
| **[07131.net](https://07131.net)**<br>*07131.net* | `E-commerce` | 🟢 **Live** | 206 ms | ✓ | [Manifest ↗](https://07131.net/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/07131.net) |
| **[18bw.app](https://18bw.app)**<br>*18bw.app* | `E-commerce` | 🟢 **Live** | 5120 ms | ✓ | [Manifest ↗](https://18bw.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/18bw.app) |
| **[24presse.com](https://24presse.com)**<br>*Royal MCP* | `Press Release Distribution Services` | 🟢 **Live** | 814 ms | ✓ | [Manifest ↗](https://24presse.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/24presse.com) |
| **[26home.co.il](https://26home.co.il)**<br>*26home.co.il* | `E-commerce` | 🟢 **Live** | 328 ms | ✓ | [Manifest ↗](https://26home.co.il/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/26home.co.il) |
| **[2work.ro](https://2work.ro)**<br>*Royal MCP* | `Professional Services` | 🟢 **Live** | 877 ms | ✓ | [Manifest ↗](https://2work.ro/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/2work.ro) |
| **[35punto.com](https://35punto.com)**<br>*35punto.com* | `E-commerce` | 🟢 **Live** | 193 ms | ✓ | [Manifest ↗](https://35punto.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/35punto.com) |
| **[3dstisk.cz](https://3dstisk.cz)**<br>*3dstisk.cz* | `E-commerce` | 🟢 **Live** | 224 ms | ✓ | [Manifest ↗](https://3dstisk.cz/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/3dstisk.cz) |
| **[3saf.com](https://3saf.com)**<br>*3saf.com* | `E-commerce` | 🟢 **Live** | 97 ms | 1 | [Manifest ↗](https://3saf.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/3saf.com) |
| **[4587fun.com](https://4587fun.com)**<br>*4587fun.com* | `E-commerce sales` | 🟢 **Live** | 1489 ms | ✓ | [Manifest ↗](https://4587fun.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/4587fun.com) |
| **[529atlanta.com](https://529atlanta.com)**<br>*Royal MCP* | `Ticket sales and bar revenue` | 🟢 **Live** | 128 ms | ✓ | [Manifest ↗](https://529atlanta.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/529atlanta.com) |
| **[99minds.io](https://99minds.io)**<br>*99minds.io* | `SaaS subscription` | 🟢 **Live** | 222 ms | ✓ | [Manifest ↗](https://99minds.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/99minds.io) |
| **[aafricaastore.com](https://aafricaastore.com)**<br>*aafricaastore.com* | `E-commerce` | 🟢 **Live** | 363 ms | ✓ | [Manifest ↗](https://aafricaastore.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aafricaastore.com) |
| **[abadystore.com](https://abadystore.com)**<br>*abadystore.com* | `E-commerce` | 🟢 **Live** | 122 ms | 1 | [Manifest ↗](https://abadystore.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/abadystore.com) |
| **[aberlawfirm.com](https://aberlawfirm.com)**<br>*Royal MCP* | `Hourly billing and retainer services` | 🟢 **Live** | 407 ms | ✓ | [Manifest ↗](https://aberlawfirm.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aberlawfirm.com) |
| **[createprints.ai](https://createprints.ai)**<br>*ai.createprints/createprints-mcp-server* | `E-commerce` | 🟢 **Live** | 722 ms | ✓ | [Manifest ↗](https://createprints.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/createprints.ai) |
| **[dreamstolife.ai](https://dreamstolife.ai)**<br>*dreamstolife.ai* | `SaaS subscription` | 🟢 **Live** | 127 ms | ✓ | [Manifest ↗](https://dreamstolife.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/dreamstolife.ai) |
| **[finsi.ai](https://finsi.ai)**<br>*finsi-mcp* | `SaaS subscription` | 🟢 **Live** | 488 ms | 4 | [Manifest ↗](https://finsi.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/finsi.ai) |
| **[freakout.ai](https://freakout.ai)**<br>*freakout.ai* | `SaaS subscription` | 🟢 **Live** | 91 ms | ✓ | [Manifest ↗](https://freakout.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/freakout.ai) |
| **[genzdealz.ai](https://genzdealz.ai)**<br>*genzdealz.ai* | `Discounts and Affiliate Marketing` | 🟢 **Live** | 639 ms | ✓ | [Manifest ↗](https://genzdealz.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/genzdealz.ai) |
| **[kimaru.ai](https://kimaru.ai)**<br>*Royal MCP* | `SaaS subscription` | 🟢 **Live** | 100 ms | ✓ | [Manifest ↗](https://kimaru.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/kimaru.ai) |
| **[lovetales.ai](https://lovetales.ai)**<br>*lovetales.ai* | `E-commerce` | 🟢 **Live** | 322 ms | ✓ | [Manifest ↗](https://lovetales.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/lovetales.ai) |
| **[merchantflow.ai](https://merchantflow.ai)**<br>*merchantflow.ai* | `SaaS subscription` | 🟢 **Live** | 353 ms | ✓ | [Manifest ↗](https://merchantflow.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/merchantflow.ai) |
| **[openhouse.ai](https://openhouse.ai)**<br>*Royal MCP* | `SaaS subscription` | 🟢 **Live** | 449 ms | ✓ | [Manifest ↗](https://openhouse.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/openhouse.ai) |
| **[performa.ai](https://performa.ai)**<br>*performa.ai* | `SaaS subscription` | 🟢 **Live** | 193 ms | ✓ | [Manifest ↗](https://performa.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/performa.ai) |
| **[promofy.ai](https://promofy.ai)**<br>*Royal MCP* | `SaaS subscription` | 🟢 **Live** | 386 ms | ✓ | [Manifest ↗](https://promofy.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/promofy.ai) |
| **[0575.net](https://0575.net)**<br>*0575.net* | `Commission-based marketplace` | 🔴 *Down* | - | ✓ | [Manifest ↗](https://0575.net/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/0575.net) |
| **[571xz.com](https://571xz.com)**<br>*571xz.com* | `Commission-based, One-piece Order Service` | 🔴 *Down* | - | ✓ | [Manifest ↗](https://571xz.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/571xz.com) |
| **[sourcingx.ai](https://sourcingx.ai)**<br>*sourcingx.ai* | `SaaS subscription` | 🔴 *Down* | - | ✓ | [Manifest ↗](https://sourcingx.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/sourcingx.ai) |

### 🛠️ Developer Platforms, DevOps & Web3 (103)

| Server / Host | Business Model | Status | Latency | Tools | Manifest | DomainScope Dossier |
|---|---|:---:|:---:|:---:|:---:|:---:|
| **[123-flowers.co.uk](https://123-flowers.co.uk)**<br>*123-flowers.co.uk* | `E-commerce` | 🟢 **Live** | 379 ms | ✓ | [Manifest ↗](https://123-flowers.co.uk/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/123-flowers.co.uk) |
| **[1erlei.de](https://1erlei.de)**<br>*1erlei.de* | `Non-profit` | 🟢 **Live** | 159 ms | ✓ | [Manifest ↗](https://1erlei.de/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/1erlei.de) |
| **[1inch.dev](https://1inch.dev)**<br>*1inch MCP* | `SaaS subscription` | 🟢 **Live** | 199 ms | 9 | [Manifest ↗](https://1inch.dev/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/1inch.dev) |
| **[212medya.com.tr](https://212medya.com.tr)**<br>*212medya.com.tr* | `Project-based and retainer services` | 🟢 **Live** | 140 ms | ✓ | [Manifest ↗](https://212medya.com.tr/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/212medya.com.tr) |
| **[21st.dev](https://21st.dev)**<br>*21st.dev* | `SaaS subscription` | 🟢 **Live** | 185 ms | ✓ | [Manifest ↗](https://21st.dev/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/21st.dev) |
| **[27bw.app](https://27bw.app)**<br>*27bw.app* | `SaaS subscription` | 🟢 **Live** | 5196 ms | ✓ | [Manifest ↗](https://27bw.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/27bw.app) |
| **[2ask.ch](https://2ask.ch)**<br>*2ask.ch* | `SaaS subscription` | 🟢 **Live** | 623 ms | ✓ | [Manifest ↗](https://2ask.ch/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/2ask.ch) |
| **[360tool.app](https://360tool.app)**<br>*360tool.app* | `SaaS subscription` | 🟢 **Live** | 655 ms | ✓ | [Manifest ↗](https://360tool.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/360tool.app) |
| **[36bw.app](https://36bw.app)**<br>*36bw.app* | `SaaS subscription` | 🟢 **Live** | 5196 ms | ✓ | [Manifest ↗](https://36bw.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/36bw.app) |
| **[3ddevice.com.ua](https://3ddevice.com.ua)**<br>*ua.com.3ddevice/catalog* | `E-commerce and Services` | 🟢 **Live** | 91 ms | ✓ | [Manifest ↗](https://3ddevice.com.ua/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/3ddevice.com.ua) |
| **[3igate.ai](https://3igate.ai)**<br>*3igate.ai* | `SaaS subscription` | 🟢 **Live** | 161 ms | ✓ | [Manifest ↗](https://3igate.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/3igate.ai) |
| **[4apps.ch](https://4apps.ch)**<br>*4apps.ch* | `SaaS subscription` | 🟢 **Live** | 1497 ms | ✓ | [Manifest ↗](https://4apps.ch/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/4apps.ch) |
| **[4peaks.am](https://4peaks.am)**<br>*Royal MCP* | `Membership fees` | 🟢 **Live** | 915 ms | ✓ | [Manifest ↗](https://4peaks.am/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/4peaks.am) |
| **[5ocakgazetesi.com](https://5ocakgazetesi.com)**<br>*5ocakgazetesi.com* | `Advertising and Subscription` | 🟢 **Live** | 210 ms | ✓ | [Manifest ↗](https://5ocakgazetesi.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/5ocakgazetesi.com) |
| **[aapinsurance.com](https://aapinsurance.com)**<br>*AAP Insurance Program* | `Membership-based insurance program` | 🟢 **Live** | 624 ms | ✓ | [Manifest ↗](https://aapinsurance.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aapinsurance.com) |
| **[aaronknight.com.au](https://aaronknight.com.au)**<br>*your-mcp-server-name* | `Freelance Services` | 🟢 **Live** | 446 ms | ✓ | [Manifest ↗](https://aaronknight.com.au/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aaronknight.com.au) |
| **[actual.ai](https://actual.ai)**<br>*Actual AI Architecture Advisor MCP* | `SaaS subscription` | 🟢 **Live** | 174 ms | 2 | [Manifest ↗](https://actual.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/actual.ai) |
| **[agency-swarm.ai](https://agency-swarm.ai)**<br>*Agency Swarm Docs MCP* | `Open-source` | 🟢 **Live** | 218 ms | 2 | [Manifest ↗](https://agency-swarm.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/agency-swarm.ai) |
| **[aigon.ai](https://aigon.ai)**<br>*aigon.ai* | `Unknown` | 🟢 **Live** | 1566 ms | ✓ | [Manifest ↗](https://aigon.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aigon.ai) |
| **[allooloo.ai](https://allooloo.ai)**<br>*Capital Markets Knowledge Graph — apex router* | `SaaS subscription` | 🟢 **Live** | 262 ms | 5 | [Manifest ↗](https://allooloo.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/allooloo.ai) |
| **[alphacorp.ai](https://alphacorp.ai)**<br>*alphacorp.ai* | `Project-based consulting and services` | 🟢 **Live** | 169 ms | ✓ | [Manifest ↗](https://alphacorp.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/alphacorp.ai) |
| **[alpic.ai](https://alpic.ai)**<br>*alpic.ai* | `SaaS subscription` | 🟢 **Live** | 185 ms | ✓ | [Manifest ↗](https://alpic.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/alpic.ai) |
| **[apertis.ai](https://apertis.ai)**<br>*apertis.ai* | `SaaS subscription` | 🟢 **Live** | 120 ms | ✓ | [Manifest ↗](https://apertis.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/apertis.ai) |
| **[arne.ai](https://arne.ai)**<br>*arne.ai* | `Freelance/Contract` | 🟢 **Live** | 172 ms | 6 | [Manifest ↗](https://arne.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/arne.ai) |
| **[askmarvin.ai](https://askmarvin.ai)**<br>*Marvin Docs MCP* | `Open-source with API key requirement` | 🟢 **Live** | 228 ms | 2 | [Manifest ↗](https://askmarvin.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/askmarvin.ai) |
| **[awesomeskill.ai](https://awesomeskill.ai)**<br>*awesomeskill.ai* | `Open-source and community-driven` | 🟢 **Live** | 211 ms | ✓ | [Manifest ↗](https://awesomeskill.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/awesomeskill.ai) |
| **[backbuild.ai](https://backbuild.ai)**<br>*backbuild.ai* | `SaaS subscription` | 🟢 **Live** | 102 ms | ✓ | [Manifest ↗](https://backbuild.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/backbuild.ai) |
| **[beatbandit.ai](https://beatbandit.ai)**<br>*beatbandit.ai* | `SaaS subscription` | 🟢 **Live** | 174 ms | 1 | [Manifest ↗](https://beatbandit.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/beatbandit.ai) |
| **[biel.ai](https://biel.ai)**<br>*biel.ai* | `SaaS subscription` | 🟢 **Live** | 395 ms | 1 | [Manifest ↗](https://biel.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/biel.ai) |
| **[bily.ai](https://bily.ai)**<br>*bily.ai* | `SaaS subscription` | 🟢 **Live** | 92 ms | 2 | [Manifest ↗](https://bily.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/bily.ai) |
| **[blockint.ai](https://blockint.ai)**<br>*blockint.ai* | `SaaS subscription` | 🟢 **Live** | 291 ms | 5 | [Manifest ↗](https://blockint.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/blockint.ai) |
| **[bopen.ai](https://bopen.ai)**<br>*bopen.ai* | `SaaS subscription` | 🟢 **Live** | 200 ms | 16 | [Manifest ↗](https://bopen.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/bopen.ai) |
| **[braininfra.ai](https://braininfra.ai)**<br>*braininfra.ai* | `B2B SaaS` | 🟢 **Live** | 892 ms | ✓ | [Manifest ↗](https://braininfra.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/braininfra.ai) |
| **[brono.ai](https://brono.ai)**<br>*brono.ai* | `SaaS subscription` | 🟢 **Live** | 284 ms | ✓ | [Manifest ↗](https://brono.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/brono.ai) |
| **[caffeine.ai](https://caffeine.ai)**<br>*caffeine.ai* | `SaaS subscription` | 🟢 **Live** | 474 ms | ✓ | [Manifest ↗](https://caffeine.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/caffeine.ai) |
| **[callva.ai](https://callva.ai)**<br>*callva.ai* | `SaaS subscription` | 🟢 **Live** | 901 ms | 1 | [Manifest ↗](https://callva.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/callva.ai) |
| **[carshippers.ai](https://carshippers.ai)**<br>*ai.carshippers/content* | `Service` | 🟢 **Live** | 592 ms | 2 | [Manifest ↗](https://carshippers.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/carshippers.ai) |
| **[cerebrium.ai](https://cerebrium.ai)**<br>*Cerebrium Docs MCP* | `SaaS_subscription` | 🟢 **Live** | 164 ms | 2 | [Manifest ↗](https://cerebrium.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/cerebrium.ai) |
| **[chatprd.ai](https://chatprd.ai)**<br>*ChatPRD* | `SaaS subscription` | 🟢 **Live** | 367 ms | ✓ | [Manifest ↗](https://chatprd.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/chatprd.ai) |
| **[clickoptions.ai](https://clickoptions.ai)**<br>*clickoptions.ai* | `Cryptocurrency Trading Platform` | 🟢 **Live** | 266 ms | ✓ | [Manifest ↗](https://clickoptions.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/clickoptions.ai) |
| **[cloptima.ai](https://cloptima.ai)**<br>*cloptima.ai* | `SaaS_subscription` | 🟢 **Live** | 1132 ms | ✓ | [Manifest ↗](https://cloptima.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/cloptima.ai) |
| **[cms.ai](https://cms.ai)**<br>*cms.ai* | `Unknown` | 🟢 **Live** | 217 ms | ✓ | [Manifest ↗](https://cms.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/cms.ai) |
| **[councilof.ai](https://councilof.ai)**<br>*csoai-gspc-mcp* | `Donations and grants` | 🟢 **Live** | 140 ms | ✓ | [Manifest ↗](https://councilof.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/councilof.ai) |
| **[cpwe.ai](https://cpwe.ai)**<br>*Guardian Posse* | `SaaS subscription` | 🟢 **Live** | 795 ms | ✓ | [Manifest ↗](https://cpwe.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/cpwe.ai) |
| **[damore.ai](https://damore.ai)**<br>*damore.ai* | `Consulting Services` | 🟢 **Live** | 1015 ms | 1 | [Manifest ↗](https://damore.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/damore.ai) |
| **[dasha.ai](https://dasha.ai)**<br>*dasha.ai* | `SaaS subscription` | 🟢 **Live** | 459 ms | ✓ | [Manifest ↗](https://dasha.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/dasha.ai) |
| **[deformity.ai](https://deformity.ai)**<br>*deformity.ai* | `SaaS subscription` | 🟢 **Live** | 388 ms | ✓ | [Manifest ↗](https://deformity.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/deformity.ai) |
| **[deployit.ai](https://deployit.ai)**<br>*ai.deployit/product-expert* | `SaaS subscription` | 🟢 **Live** | 163 ms | ✓ | [Manifest ↗](https://deployit.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/deployit.ai) |
| **[dial8.ai](https://dial8.ai)**<br>*dial8.ai* | `SaaS subscription` | 🟢 **Live** | 257 ms | ✓ | [Manifest ↗](https://dial8.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/dial8.ai) |
| **[divinci.ai](https://divinci.ai)**<br>*divinci.ai* | `SaaS subscription` | 🟢 **Live** | 103 ms | ✓ | [Manifest ↗](https://divinci.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/divinci.ai) |
| **[docuwriter.ai](https://docuwriter.ai)**<br>*docuwriter.ai* | `SaaS subscription` | 🟢 **Live** | 195 ms | ✓ | [Manifest ↗](https://docuwriter.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/docuwriter.ai) |
| **[domainsuggest.ai](https://domainsuggest.ai)**<br>*com.youspot/youspot* | `SaaS subscription` | 🟢 **Live** | 408 ms | 111 | [Manifest ↗](https://domainsuggest.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/domainsuggest.ai) |
| **[dubvoice.ai](https://dubvoice.ai)**<br>*dubvoice.ai* | `SaaS subscription` | 🟢 **Live** | 362 ms | 5 | [Manifest ↗](https://dubvoice.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/dubvoice.ai) |
| **[enverge.ai](https://enverge.ai)**<br>*enverge.ai* | `SaaS subscription with pay-per-use pricing for AI compute resources` | 🟢 **Live** | 180 ms | 2 | [Manifest ↗](https://enverge.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/enverge.ai) |
| **[erayaha.ai](https://erayaha.ai)**<br>*io.github.erayaha/mcp-server* | `SaaS subscription` | 🟢 **Live** | 98 ms | 4 | [Manifest ↗](https://erayaha.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/erayaha.ai) |
| **[everydev.ai](https://everydev.ai)**<br>*everydev.ai* | `SaaS subscription` | 🟢 **Live** | 369 ms | ✓ | [Manifest ↗](https://everydev.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/everydev.ai) |
| **[ezugc.ai](https://ezugc.ai)**<br>*ai.ezugc/mcp* | `SaaS subscription` | 🟢 **Live** | 297 ms | 29 | [Manifest ↗](https://ezugc.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ezugc.ai) |
| **[flaex.ai](https://flaex.ai)**<br>*flaex.ai* | `SaaS subscription` | 🟢 **Live** | 394 ms | ✓ | [Manifest ↗](https://flaex.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/flaex.ai) |
| **[getbluejay.ai](https://getbluejay.ai)**<br>*getbluejay.ai* | `SaaS subscription` | 🟢 **Live** | 317 ms | ✓ | [Manifest ↗](https://getbluejay.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/getbluejay.ai) |
| **[gmgn.ai](https://gmgn.ai)**<br>*gmgn.ai* | `Subscription-based SaaS platform with additional transaction fees` | 🟢 **Live** | 313 ms | ✓ | [Manifest ↗](https://gmgn.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/gmgn.ai) |
| **[grep.ai](https://grep.ai)**<br>*grep-public-api-v2* | `SaaS subscription` | 🟢 **Live** | 930 ms | 50 | [Manifest ↗](https://grep.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/grep.ai) |
| **[guild.ai](https://guild.ai)**<br>*Guild.ai* | `SaaS subscription` | 🟢 **Live** | 354 ms | 4 | [Manifest ↗](https://guild.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/guild.ai) |
| **[haimaker.ai](https://haimaker.ai)**<br>*haimaker.ai* | `SaaS subscription` | 🟢 **Live** | 137 ms | ✓ | [Manifest ↗](https://haimaker.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/haimaker.ai) |
| **[hivekind.ai](https://hivekind.ai)**<br>*Hivekind* | `SaaS subscription` | 🟢 **Live** | 401 ms | ✓ | [Manifest ↗](https://hivekind.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/hivekind.ai) |
| **[infrasure.ai](https://infrasure.ai)**<br>*infrasure* | `SaaS subscription` | 🟢 **Live** | 406 ms | 18 | [Manifest ↗](https://infrasure.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/infrasure.ai) |
| **[jobplans.ai](https://jobplans.ai)**<br>*jobplans.ai* | `SaaS subscription` | 🟢 **Live** | 102 ms | 9 | [Manifest ↗](https://jobplans.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/jobplans.ai) |
| **[kapa.ai](https://kapa.ai)**<br>*ai.kapa/kapa-docs* | `SaaS subscription` | 🟢 **Live** | 331 ms | ✓ | [Manifest ↗](https://kapa.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/kapa.ai) |
| **[kapso.ai](https://kapso.ai)**<br>*kapso.ai* | `SaaS subscription` | 🟢 **Live** | 773 ms | ✓ | [Manifest ↗](https://kapso.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/kapso.ai) |
| **[koso.ai](https://koso.ai)**<br>*ai.koso/koso* | `SaaS subscription` | 🟢 **Live** | 683 ms | ✓ | [Manifest ↗](https://koso.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/koso.ai) |
| **[layerr.ai](https://layerr.ai)**<br>*layerr-marketing* | `SaaS subscription` | 🟢 **Live** | 202 ms | 4 | [Manifest ↗](https://layerr.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/layerr.ai) |
| **[letz.ai](https://letz.ai)**<br>*letz.ai* | `Freemium Subscription` | 🟢 **Live** | 156 ms | ✓ | [Manifest ↗](https://letz.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/letz.ai) |
| **[lindo.ai](https://lindo.ai)**<br>*lindo.ai* | `SaaS subscription` | 🟢 **Live** | 94 ms | ✓ | [Manifest ↗](https://lindo.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/lindo.ai) |
| **[lovedby.ai](https://lovedby.ai)**<br>*LovedByAI* | `SaaS subscription` | 🟢 **Live** | 552 ms | 1 | [Manifest ↗](https://lovedby.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/lovedby.ai) |
| **[markdown2pdf.ai](https://markdown2pdf.ai)**<br>*markdown2pdf.ai Docs MCP* | `SaaS subscription` | 🟢 **Live** | 209 ms | 2 | [Manifest ↗](https://markdown2pdf.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/markdown2pdf.ai) |
| **[mcp-eval.ai](https://mcp-eval.ai)**<br>*mcp-eval Docs MCP* | `Open Source` | 🟢 **Live** | 208 ms | 2 | [Manifest ↗](https://mcp-eval.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/mcp-eval.ai) |
| **[meetcamille.ai](https://meetcamille.ai)**<br>*MeetCamille.ai - Documentation Docs MCP* | `Premium Subscription, Token Staking` | 🟢 **Live** | 233 ms | 2 | [Manifest ↗](https://meetcamille.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/meetcamille.ai) |
| **[meetsquad.ai](https://meetsquad.ai)**<br>*meetsquad.ai* | `SaaS subscription` | 🟢 **Live** | 166 ms | ✓ | [Manifest ↗](https://meetsquad.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/meetsquad.ai) |
| **[miamiweb.ai](https://miamiweb.ai)**<br>*miamiweb.ai* | `Project-based` | 🟢 **Live** | 178 ms | ✓ | [Manifest ↗](https://miamiweb.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/miamiweb.ai) |
| **[mnml.ai](https://mnml.ai)**<br>*mnml.ai* | `SaaS subscription` | 🟢 **Live** | 257 ms | ✓ | [Manifest ↗](https://mnml.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/mnml.ai) |
| **[modelscope.ai](https://modelscope.ai)**<br>*modelscope.ai* | `SaaS subscription` | 🟢 **Live** | 1230 ms | ✓ | [Manifest ↗](https://modelscope.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/modelscope.ai) |
| **[modflow.ai](https://modflow.ai)**<br>*modflow.ai* | `SaaS subscription` | 🟢 **Live** | 562 ms | 7 | [Manifest ↗](https://modflow.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/modflow.ai) |
| **[monaos.ai](https://monaos.ai)**<br>*monaos.ai* | `SaaS subscription` | 🟢 **Live** | 287 ms | ✓ | [Manifest ↗](https://monaos.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/monaos.ai) |
| **[muapi.ai](https://muapi.ai)**<br>*muapi.ai* | `SaaS subscription` | 🟢 **Live** | 506 ms | ✓ | [Manifest ↗](https://muapi.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/muapi.ai) |
| **[premierstudio.ai](https://premierstudio.ai)**<br>*premierstudio.ai* | `Custom Development Services` | 🟢 **Live** | 124 ms | ✓ | [Manifest ↗](https://premierstudio.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/premierstudio.ai) |
| **[promenaut.ai](https://promenaut.ai)**<br>*promenaut* | `SaaS subscription` | 🟢 **Live** | 399 ms | 3 | [Manifest ↗](https://promenaut.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/promenaut.ai) |
| **[promptroot.ai](https://promptroot.ai)**<br>*promptroot.ai* | `Freemium` | 🟢 **Live** | 158 ms | ✓ | [Manifest ↗](https://promptroot.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/promptroot.ai) |
| **[proofof.ai](https://proofof.ai)**<br>*csoai-gspc-mcp* | `SaaS subscription` | 🟢 **Live** | 332 ms | ✓ | [Manifest ↗](https://proofof.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/proofof.ai) |
| **[roboflow.ai](https://roboflow.ai)**<br>*roboflow.ai* | `SaaS subscription` | 🟢 **Live** | 228 ms | ✓ | [Manifest ↗](https://roboflow.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/roboflow.ai) |
| **[sam3.ai](https://sam3.ai)**<br>*sam3.ai* | `SaaS subscription` | 🟢 **Live** | 115 ms | 3 | [Manifest ↗](https://sam3.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/sam3.ai) |
| **[scorable.ai](https://scorable.ai)**<br>*scorable.ai* | `SaaS subscription` | 🟢 **Live** | 219 ms | ✓ | [Manifest ↗](https://scorable.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/scorable.ai) |
| **[sitegpt.ai](https://sitegpt.ai)**<br>*SiteGPT MCP Server* | `SaaS subscription` | 🟢 **Live** | 112 ms | 17 | [Manifest ↗](https://sitegpt.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/sitegpt.ai) |
| **[slng.ai](https://slng.ai)**<br>*slng.ai* | `SaaS subscription` | 🟢 **Live** | 161 ms | ✓ | [Manifest ↗](https://slng.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/slng.ai) |
| **[smartbench.ai](https://smartbench.ai)**<br>*smartbench.ai* | `SaaS subscription` | 🟢 **Live** | 97 ms | ✓ | [Manifest ↗](https://smartbench.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/smartbench.ai) |
| **[smry.ai](https://smry.ai)**<br>*smry* | `Free to Use` | 🟢 **Live** | 97 ms | 9 | [Manifest ↗](https://smry.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/smry.ai) |
| **[smushlabs.ai](https://smushlabs.ai)**<br>*smushlabs.ai* | `SaaS subscription` | 🟢 **Live** | 101 ms | 4 | [Manifest ↗](https://smushlabs.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/smushlabs.ai) |
| **[sqd.ai](https://sqd.ai)**<br>*sqd.ai* | `SaaS subscription` | 🟢 **Live** | 185 ms | 1 | [Manifest ↗](https://sqd.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/sqd.ai) |
| **[squiggle.ai](https://squiggle.ai)**<br>*Squiggle Docs MCP* | `SaaS subscription` | 🟢 **Live** | 431 ms | 2 | [Manifest ↗](https://squiggle.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/squiggle.ai) |
| **[unhosted.ai](https://unhosted.ai)**<br>*ai.unhosted/predictions* | `Subscription-based SaaS` | 🟢 **Live** | 459 ms | ✓ | [Manifest ↗](https://unhosted.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/unhosted.ai) |
| **[vapi.ai](https://vapi.ai)**<br>*vapi.ai* | `SaaS subscription` | 🟢 **Live** | 177 ms | ✓ | [Manifest ↗](https://vapi.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/vapi.ai) |
| **[vast.ai](https://vast.ai)**<br>*Vast.ai Documentation MCP* | `SaaS subscription (pay-per-use)` | 🟢 **Live** | 195 ms | ✓ | [Manifest ↗](https://vast.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/vast.ai) |
| **[waveapp.ai](https://waveapp.ai)**<br>*waveapp.ai* | `Book Sales` | 🟢 **Live** | 349 ms | 2 | [Manifest ↗](https://waveapp.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/waveapp.ai) |
| **[zoomeye.ai](https://zoomeye.ai)**<br>*zoomeye.ai* | `Subscription-based access to cybersecurity tools` | 🟢 **Live** | 1556 ms | 2 | [Manifest ↗](https://zoomeye.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/zoomeye.ai) |
| **[intsig.ai](https://intsig.ai)**<br>*intsig.ai* | `SaaS subscription` | 🔴 *Down* | - | ✓ | [Manifest ↗](https://intsig.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/intsig.ai) |

### 🤖 Autonomous Agents & Workflow Automation (61)

| Server / Host | Business Model | Status | Latency | Tools | Manifest | DomainScope Dossier |
|---|---|:---:|:---:|:---:|:---:|:---:|
| **[1518.com](https://1518.com)**<br>*1518.com AI entrypoint catalog* | `Freemium (free services with optional paid features)` | 🟢 **Live** | 801 ms | ✓ | [Manifest ↗](https://1518.com/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/1518.com) |
| **[1stsupplement.com](https://1stsupplement.com)**<br>*1stsupplement.com* | `E-commerce` | 🟢 **Live** | 612 ms | ✓ | [Manifest ↗](https://1stsupplement.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/1stsupplement.com) |
| **[2muchcoffee.com](https://2muchcoffee.com)**<br>*2muchcoffee.com* | `Custom Software Development` | 🟢 **Live** | 188 ms | ✓ | [Manifest ↗](https://2muchcoffee.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/2muchcoffee.com) |
| **[2ndface.info](https://2ndface.info)**<br>*2ndface.info* | `Service-based` | 🟢 **Live** | 97 ms | ✓ | [Manifest ↗](https://2ndface.info/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/2ndface.info) |
| **[7be.io](https://7be.io)**<br>*7be.io* | `Subscription-based with listing options` | 🟢 **Live** | 433 ms | 5 | [Manifest ↗](https://7be.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/7be.io) |
| **[aaronlynn.com](https://aaronlynn.com)**<br>*aaronlynn.com* | `Consulting Services, Course Sales, Affiliate Marketing` | 🟢 **Live** | 172 ms | 5 | [Manifest ↗](https://aaronlynn.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aaronlynn.com) |
| **[abantpack.com](https://abantpack.com)**<br>*abantpack.com* | `Manufacturing and Sales` | 🟢 **Live** | 535 ms | ✓ | [Manifest ↗](https://abantpack.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/abantpack.com) |
| **[agenticplug.ai](https://agenticplug.ai)**<br>*agenticplug.ai* | `SaaS subscription` | 🟢 **Live** | 173 ms | 5 | [Manifest ↗](https://agenticplug.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/agenticplug.ai) |
| **[agentmesh.ai](https://agentmesh.ai)**<br>*agentmesh.ai* | `SaaS subscription` | 🟢 **Live** | 130 ms | ✓ | [Manifest ↗](https://agentmesh.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/agentmesh.ai) |
| **[aimdoc.ai](https://aimdoc.ai)**<br>*ai.aimdoc/agent-gateway* | `SaaS subscription` | 🟢 **Live** | 199 ms | ✓ | [Manifest ↗](https://aimdoc.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aimdoc.ai) |
| **[aimsoo.ai](https://aimsoo.ai)**<br>*aeo-aimsoo.ai* | `SaaS subscription` | 🟢 **Live** | 257 ms | ✓ | [Manifest ↗](https://aimsoo.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aimsoo.ai) |
| **[alva.ai](https://alva.ai)**<br>*Alva Public Discovery MCP* | `Subscription-based SaaS` | 🟢 **Live** | 301 ms | 3 | [Manifest ↗](https://alva.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/alva.ai) |
| **[animam.ai](https://animam.ai)**<br>*animam.ai* | `SaaS subscription` | 🟢 **Live** | 220 ms | ✓ | [Manifest ↗](https://animam.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/animam.ai) |
| **[bolta.ai](https://bolta.ai)**<br>*bolta* | `SaaS subscription` | 🟢 **Live** | 240 ms | ✓ | [Manifest ↗](https://bolta.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/bolta.ai) |
| **[boolsai.ai](https://boolsai.ai)**<br>*Boolsai* | `SaaS subscription` | 🟢 **Live** | 171 ms | ✓ | [Manifest ↗](https://boolsai.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/boolsai.ai) |
| **[briefhq.ai](https://briefhq.ai)**<br>*ai.briefhq/brief* | `SaaS subscription` | 🟢 **Live** | 141 ms | ✓ | [Manifest ↗](https://briefhq.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/briefhq.ai) |
| **[civicstar.ai](https://civicstar.ai)**<br>*Boardwalk AI Catalog* | `Subscription` | 🟢 **Live** | 183 ms | ✓ | [Manifest ↗](https://civicstar.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/civicstar.ai) |
| **[cloudlayer.ai](https://cloudlayer.ai)**<br>*Cloudlayer AI Agentic Discovery* | `SaaS subscription` | 🟢 **Live** | 710 ms | 5 | [Manifest ↗](https://cloudlayer.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/cloudlayer.ai) |
| **[complyhub.ai](https://complyhub.ai)**<br>*complyhub.ai* | `SaaS subscription` | 🟢 **Live** | 119 ms | 1 | [Manifest ↗](https://complyhub.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/complyhub.ai) |
| **[content-center.ai](https://content-center.ai)**<br>*content-center.ai* | `SaaS subscription` | 🟢 **Live** | 425 ms | 1 | [Manifest ↗](https://content-center.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/content-center.ai) |
| **[dreamlit.ai](https://dreamlit.ai)**<br>*dreamlit.ai* | `SaaS subscription` | 🟢 **Live** | 360 ms | 11 | [Manifest ↗](https://dreamlit.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/dreamlit.ai) |
| **[duvo.ai](https://duvo.ai)**<br>*Duvo MCP* | `SaaS subscription` | 🟢 **Live** | 359 ms | 4 | [Manifest ↗](https://duvo.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/duvo.ai) |
| **[fimo.ai](https://fimo.ai)**<br>*ai.fimo/project* | `SaaS subscription` | 🟢 **Live** | 137 ms | ✓ | [Manifest ↗](https://fimo.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/fimo.ai) |
| **[fin.ai](https://fin.ai)**<br>*fin.ai* | `SaaS subscription` | 🟢 **Live** | 202 ms | 13 | [Manifest ↗](https://fin.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/fin.ai) |
| **[finseo.ai](https://finseo.ai)**<br>*ai.finseo/visibility* | `SaaS subscription` | 🟢 **Live** | 273 ms | ✓ | [Manifest ↗](https://finseo.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/finseo.ai) |
| **[getcargo.ai](https://getcargo.ai)**<br>*Cargo* | `SaaS subscription` | 🟢 **Live** | 396 ms | ✓ | [Manifest ↗](https://getcargo.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/getcargo.ai) |
| **[getcivicstar.ai](https://getcivicstar.ai)**<br>*Boardwalk AI Catalog* | `SaaS subscription` | 🟢 **Live** | 347 ms | ✓ | [Manifest ↗](https://getcivicstar.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/getcivicstar.ai) |
| **[gowarm.ai](https://gowarm.ai)**<br>*com.gowarmcrm/mcp* | `SaaS subscription` | 🟢 **Live** | 458 ms | 5 | [Manifest ↗](https://gowarm.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/gowarm.ai) |
| **[homesage.ai](https://homesage.ai)**<br>*homesage.ai* | `SaaS subscription` | 🟢 **Live** | 106 ms | ✓ | [Manifest ↗](https://homesage.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/homesage.ai) |
| **[ipcopilot.ai](https://ipcopilot.ai)**<br>*ipcopilot.ai* | `SaaS subscription` | 🟢 **Live** | 121 ms | 5 | [Manifest ↗](https://ipcopilot.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ipcopilot.ai) |
| **[jasper.ai](https://jasper.ai)**<br>*jasper.ai* | `SaaS subscription` | 🟢 **Live** | 101 ms | 7 | [Manifest ↗](https://jasper.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/jasper.ai) |
| **[joai.ai](https://joai.ai)**<br>*JoAi* | `SaaS subscription` | 🟢 **Live** | 139 ms | 7 | [Manifest ↗](https://joai.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/joai.ai) |
| **[kaito.ai](https://kaito.ai)**<br>*Kaito* | `SaaS subscription` | 🟢 **Live** | 434 ms | 20 | [Manifest ↗](https://kaito.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/kaito.ai) |
| **[keenagents.ai](https://keenagents.ai)**<br>*keenagents.ai* | `SaaS subscription` | 🟢 **Live** | 159 ms | ✓ | [Manifest ↗](https://keenagents.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/keenagents.ai) |
| **[klipy.ai](https://klipy.ai)**<br>*klipy.ai* | `SaaS subscription` | 🟢 **Live** | 249 ms | ✓ | [Manifest ↗](https://klipy.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/klipy.ai) |
| **[konverte.ai](https://konverte.ai)**<br>*konverte.ai* | `SaaS subscription` | 🟢 **Live** | 394 ms | 5 | [Manifest ↗](https://konverte.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/konverte.ai) |
| **[kroonen.ai](https://kroonen.ai)**<br>*kroonen-ai* | `Consulting Services` | 🟢 **Live** | 122 ms | ✓ | [Manifest ↗](https://kroonen.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/kroonen.ai) |
| **[layer.ai](https://layer.ai)**<br>*Layer* | `SaaS subscription` | 🟢 **Live** | 183 ms | ✓ | [Manifest ↗](https://layer.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/layer.ai) |
| **[mallary.ai](https://mallary.ai)**<br>*ai.mallary/mallary* | `SaaS subscription` | 🟢 **Live** | 212 ms | 19 | [Manifest ↗](https://mallary.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/mallary.ai) |
| **[momentic.ai](https://momentic.ai)**<br>*ai.momentic/mcp* | `SaaS subscription` | 🟢 **Live** | 170 ms | 26 | [Manifest ↗](https://momentic.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/momentic.ai) |
| **[novita.ai](https://novita.ai)**<br>*novita.ai* | `SaaS subscription (pay-per-use)` | 🟢 **Live** | 191 ms | ✓ | [Manifest ↗](https://novita.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/novita.ai) |
| **[ora.ai](https://ora.ai)**<br>*ora* | `SaaS subscription` | 🟢 **Live** | 453 ms | 13 | [Manifest ↗](https://ora.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ora.ai) |
| **[orq.ai](https://orq.ai)**<br>*orq.ai MCP Server* | `SaaS subscription` | 🟢 **Live** | 154 ms | 3 | [Manifest ↗](https://orq.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/orq.ai) |
| **[outlit.ai](https://outlit.ai)**<br>*Outlit* | `SaaS subscription` | 🟢 **Live** | 718 ms | 46 | [Manifest ↗](https://outlit.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/outlit.ai) |
| **[parallel.ai](https://parallel.ai)**<br>*ai.parallel/search-mcp* | `SaaS subscription` | 🟢 **Live** | 265 ms | ✓ | [Manifest ↗](https://parallel.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/parallel.ai) |
| **[paz.ai](https://paz.ai)**<br>*Paz.ai Public API MCP* | `SaaS subscription` | 🟢 **Live** | 476 ms | 6 | [Manifest ↗](https://paz.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/paz.ai) |
| **[pocketos.ai](https://pocketos.ai)**<br>*pocketos.ai* | `SaaS subscription` | 🟢 **Live** | 204 ms | 5 | [Manifest ↗](https://pocketos.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/pocketos.ai) |
| **[puppyone.ai](https://puppyone.ai)**<br>*puppyone* | `SaaS subscription` | 🟢 **Live** | 593 ms | 7 | [Manifest ↗](https://puppyone.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/puppyone.ai) |
| **[reducto.ai](https://reducto.ai)**<br>*reducto* | `SaaS subscription` | 🟢 **Live** | 197 ms | 9 | [Manifest ↗](https://reducto.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/reducto.ai) |
| **[ricord.ai](https://ricord.ai)**<br>*Ricord* | `SaaS subscription` | 🟢 **Live** | 298 ms | 14 | [Manifest ↗](https://ricord.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ricord.ai) |
| **[rocketgrowth.ai](https://rocketgrowth.ai)**<br>*RocketGrowth* | `SaaS subscription` | 🟢 **Live** | 104 ms | ✓ | [Manifest ↗](https://rocketgrowth.ai/.well-known/ai-catalog.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/rocketgrowth.ai) |
| **[rogiq.ai](https://rogiq.ai)**<br>*rogiq.ai* | `SaaS subscription` | 🟢 **Live** | 142 ms | ✓ | [Manifest ↗](https://rogiq.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/rogiq.ai) |
| **[runthebulls.ai](https://runthebulls.ai)**<br>*CocoFintel MCP* | `SaaS subscription` | 🟢 **Live** | 478 ms | ✓ | [Manifest ↗](https://runthebulls.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/runthebulls.ai) |
| **[secondary.ai](https://secondary.ai)**<br>*Secondary AI* | `SaaS subscription` | 🟢 **Live** | 445 ms | 5 | [Manifest ↗](https://secondary.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/secondary.ai) |
| **[spelunking.ai](https://spelunking.ai)**<br>*ai.spelunking/hub* | `Advertising` | 🟢 **Live** | 295 ms | 3 | [Manifest ↗](https://spelunking.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/spelunking.ai) |
| **[taskaid.ai](https://taskaid.ai)**<br>*ai.taskaid/taskaid* | `SaaS subscription` | 🟢 **Live** | 170 ms | 7 | [Manifest ↗](https://taskaid.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/taskaid.ai) |
| **[theagoralabs.ai](https://theagoralabs.ai)**<br>*theagora* | `Free for design partners, potential revenue from enterprise use` | 🟢 **Live** | 129 ms | ✓ | [Manifest ↗](https://theagoralabs.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/theagoralabs.ai) |
| **[ticketdesk.ai](https://ticketdesk.ai)**<br>*ai.ticketdesk/mcp* | `SaaS subscription` | 🟢 **Live** | 107 ms | ✓ | [Manifest ↗](https://ticketdesk.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ticketdesk.ai) |
| **[tinkerer.ai](https://tinkerer.ai)**<br>*AI Tinkerers Agents MCP* | `SaaS subscription` | 🟢 **Live** | 1201 ms | ✓ | [Manifest ↗](https://tinkerer.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/tinkerer.ai) |
| **[townspot.ai](https://townspot.ai)**<br>*townspot.ai* | `Unknown` | 🟢 **Live** | 468 ms | ✓ | [Manifest ↗](https://townspot.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/townspot.ai) |
| **[unriddle.ai](https://unriddle.ai)**<br>*unriddle.ai* | `SaaS subscription` | 🟢 **Live** | 415 ms | ✓ | [Manifest ↗](https://unriddle.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/unriddle.ai) |

---

## 🏢 Distribution by Business Delivery Model

Classified by DomainScope's firmographic model inference:

- **SaaS subscription**: **267 servers**
- **Unknown**: **28 servers**
- **E-commerce**: **14 servers**
- **Advertising**: **13 servers**
- **Consulting Services**: **11 servers**
- **SaaS_subscription**: **9 servers**
- **Subscription**: **5 servers**
- **Non-profit**: **5 servers**
- **Subscription-based**: **4 servers**
- **Service-based**: **4 servers**
- **B2B Sales**: **3 servers**
- **Subscription-based SaaS**: **3 servers**
- **Rental Services**: **2 servers**
- **Gaming Revenue**: **2 servers**
- **Freemium**: **2 servers**
- **Personal Blog**: **2 servers**
- **Tuition Fees**: **2 servers**
- **Membership fees**: **2 servers**
- **B2B Services**: **2 servers**
- **Services**: **2 servers**
- **Professional Services**: **2 servers**
- **Freemium Subscription**: **2 servers**
- **B2B SaaS**: **2 servers**
- **Open Source**: **2 servers**
- **SaaS subscription (pay-per-use)**: **2 servers**
- **Retail Sales**: **1 servers**
- **B2C Sales**: **1 servers**
- **AI Services & Solutions**: **1 servers**
- **Email subscription**: **1 servers**
- **Freemium with Subscription**: **1 servers**
- **Marketplace, Brokerage**: **1 servers**
- **Advertising, Affiliate Marketing**: **1 servers**
- **Ticket Sales**: **1 servers**
- **Free, Non-Profit**: **1 servers**
- **Donations, grants, and tuition fees**: **1 servers**
- **Subscription-based and Pay-per-view**: **1 servers**
- **Pay-per-service**: **1 servers**
- **Medical Services**: **1 servers**
- **B2B service**: **1 servers**
- **Subscription-based and Pay-per-minute**: **1 servers**
- **Lead Generation**: **1 servers**
- **Subscription-based Dating Service**: **1 servers**
- **Subscription-based with pay-per-minute shows**: **1 servers**
- **Paid Services**: **1 servers**
- **Betting Commission**: **1 servers**
- **Event-based**: **1 servers**
- **Rental and Sales**: **1 servers**
- **Event Organization**: **1 servers**
- **Freight Brokerage**: **1 servers**
- **Non-profit Organization**: **1 servers**
- **Tuition fees and partnerships**: **1 servers**
- **Accommodation and Activity Bookings**: **1 servers**
- **Open-source software development, decentralized finance platform**: **1 servers**
- **Open-source protocol with decentralized governance**: **1 servers**
- **Project-based Services**: **1 servers**
- **Affinity marketing**: **1 servers**
- **Advertising (CPM)**: **1 servers**
- **Freemium (with in-app purchases)**: **1 servers**
- **Freemium with premium subscriptions**: **1 servers**
- **Freemium (with potential premium features)**: **1 servers**
- **Freemium (App Store)**: **1 servers**
- **SaaS subscription with free and paid plans**: **1 servers**
- **Freemium with Premium Subscription**: **1 servers**
- **Subscription-based (Club Jam) and Consulting Services**: **1 servers**
- **Non-profit, funded by grants or sponsorships**: **1 servers**
- **Freemium (with premium features)**: **1 servers**
- **Commission-based**: **1 servers**
- **Service-based subscription**: **1 servers**
- **Hardware Sales**: **1 servers**
- **Premium Subscription**: **1 servers**
- **Subscription or Freemium**: **1 servers**
- **Selling Software**: **1 servers**
- **Subscription-based service**: **1 servers**
- **Paid subscriptions and courses**: **1 servers**
- **Advertising & Sponsored Content**: **1 servers**
- **Subscription-based with profit sharing**: **1 servers**
- **Advertising, Subscription**: **1 servers**
- **Private Practice**: **1 servers**
- **Rental Income**: **1 servers**
- **Wholesale**: **1 servers**
- **Press Release Distribution Services**: **1 servers**
- **E-commerce sales**: **1 servers**
- **Ticket sales and bar revenue**: **1 servers**
- **Hourly billing and retainer services**: **1 servers**
- **Discounts and Affiliate Marketing**: **1 servers**
- **Project-based and retainer services**: **1 servers**
- **E-commerce and Services**: **1 servers**
- **Advertising and Subscription**: **1 servers**
- **Membership-based insurance program**: **1 servers**
- **Freelance Services**: **1 servers**
- **Open-source**: **1 servers**
- **Project-based consulting and services**: **1 servers**
- **Freelance/Contract**: **1 servers**
- **Open-source with API key requirement**: **1 servers**
- **Open-source and community-driven**: **1 servers**
- **Service**: **1 servers**
- **Cryptocurrency Trading Platform**: **1 servers**
- **Donations and grants**: **1 servers**
- **SaaS subscription with pay-per-use pricing for AI compute resources**: **1 servers**
- **Subscription-based SaaS platform with additional transaction fees**: **1 servers**
- **Premium Subscription, Token Staking**: **1 servers**
- **Project-based**: **1 servers**
- **Custom Development Services**: **1 servers**
- **Free to Use**: **1 servers**
- **Book Sales**: **1 servers**
- **Subscription-based access to cybersecurity tools**: **1 servers**
- **Freemium (free services with optional paid features)**: **1 servers**
- **Custom Software Development**: **1 servers**
- **Subscription-based with listing options**: **1 servers**
- **Consulting Services, Course Sales, Affiliate Marketing**: **1 servers**
- **Manufacturing and Sales**: **1 servers**
- **Free for design partners, potential revenue from enterprise use**: **1 servers**
- **Government Services**: **1 servers**
- **Job Board**: **1 servers**
- **Tour Package Sales**: **1 servers**
- **Commission-based marketplace**: **1 servers**
- **Commission-based, One-piece Order Service**: **1 servers**

---

## 🔄 Automated Liveness & Fleet Updating

This repository is continuously synchronized on our self-hosted bare-metal infrastructure (Woodpecker CI + systemd automation on `0docker.com` / `0mcp.com`):
1. **Continuous Crawler**: Ingests newly discovered MCP domains from [DomainScope's](https://domainscope.scrapetheworld.org) 13M+ domain corpus.
2. **Firmographic Enrichment**: Enriches and classifies each server using DomainScope's corporate graph.
3. **Real-World HTTP Probes**: Verifies endpoint availability, protocol compliance, latency, and tool declarations.
4. **Local CI/CD Pipeline**: Validated on every commit via [Woodpecker CI](https://ci.0exec.com) ([`.woodpecker.yml`](.woodpecker.yml)).
5. **Autonomous Sync Daemon**: Scheduled via [`systemd/mcp-directory-sync.timer`](systemd/mcp-directory-sync.timer) executing [`scripts/fleet-sync-cron.sh`](scripts/fleet-sync-cron.sh).

## 🤝 Contributing & Submitting a Server

Host your MCP server card at `https://yourdomain.com/.well-known/mcp/server-card.json` or `/.well-known/ai-catalog.json`. DomainScope's crawler will discover it automatically, or submit an issue / PR!

**Maintained by [DomainScope](https://domainscope.scrapetheworld.org) & Badita Florin** · *Licensed under MIT*.
