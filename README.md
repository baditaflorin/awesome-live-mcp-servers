# Awesome Live MCP Servers 🌐⚡

> **The definitive, live-benchmarked directory of public & remote Model Context Protocol (MCP) servers and streamable AI manifests on the internet.**
>
> Concurrently probed, latency-benchmarked, and enriched by **[DomainScope at Scrape the World](https://domainscope.scrapetheworld.org)**.

[![Total Servers](https://img.shields.io/badge/MCP_Servers-1271-purple?style=for-the-badge&logo=anthropic)](data/mcp-servers.json)
[![Live Reachable](https://img.shields.io/badge/Handshake_Verified-406-emerald?style=for-the-badge)](data/mcp-servers.json)
[![Scanned Corpus](https://img.shields.io/badge/Scanned_Corpus-462k_Domains_Scanned-blue?style=for-the-badge)](https://domainscope.scrapetheworld.org/mcp-directory)
[![Enriched by DomainScope](https://img.shields.io/badge/Intelligence-DomainScope_Graph-00D26A?style=for-the-badge&logo=databricks)](https://domainscope.scrapetheworld.org)
[![CI: Woodpecker](https://img.shields.io/badge/CI-Woodpecker_Self--Hosted-2088FF?style=for-the-badge&logo=linux)](https://ci.0exec.com)

Unlike typical GitHub lists that catalog local code repositories requiring terminal installation (`npx`, `docker`, virtual environments), this repository is the **world's largest autonomous directory of live, running, publicly reachable Model Context Protocol (MCP) servers and streamable AI endpoints**.

---

## ⚡ What Makes This Directory Different

| Feature | Standard "Awesome MCP" Repositories | **Awesome Live MCP Servers 🌐⚡** |
|---|---|---|
| **What it lists** | GitHub source code repos for `localhost` execution | **Live, running, public HTTP endpoints** (`https://.../api/mcp`) |
| **Setup required** | `npx`, Node.js, Python venvs, Docker, local configuration | **Zero-Install URL**: Directly connect in Cursor, Claude, or Windsurf |
| **Maintenance** | Manual pull requests (frequently unmaintained or rotting) | **Autonomous & Self-Evolving**: Continuously crawled across 13M+ domains |
| **Verification** | Unverified code links with unknown server health | **Live-Probed Telemetry**: Concurrently benchmarked reachability & response latencies |
| **Firmographics** | Flat markdown files with arbitrary tags | **DomainScope at Scrape the World**: Multi-dimensional market verticals & company dossiers |

---

## 🤖 Self-Evolving Autonomous Engine

This directory is **not maintained by waiting for manual pull requests**. It is continuously discovered, updated, and verified by an autonomous internet-scale data pipeline:
1. **462k domains scanned** (of DomainScope's 13M+): ingests high-priority cohorts (developer documentation platforms, open-source repositories, API surfaces, AI ecosystem domains) from DomainScope's 13M+ domain graph.
2. **Standard & Streamable Detection**: Probes standard cards (`/.well-known/mcp/server-card.json`), streamable HTTP POST endpoints (`/api/mcp`), and AI catalogs (`/.well-known/ai-catalog.json`).
3. **Live Health & Latency Telemetry**: Concurrently benchmarks round-trip latency (P50/P95) and verifies HTTP 200/204/401/403 states across 32 threads.
4. **Firmographic Enrichment**: Enriches every host with DomainScope's verified business models, market taxonomy, and tech stack detection.

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

| Vertical Category | Live Online | Total Servers | Scope | Full Directory |
|---|:---:|:---:|---|:---:|
| **🛠️ Developer Platforms, DevOps & Web3** | 🟢 **177** | **415** | Developer tooling, APIs, CI/CD, cloud orchestration, web3, and IDE integrations. | [**Browse All (415) ↗**](directory/developer-platforms.md) |
| **🤖 Autonomous Agents & Workflow Automation** | 🟢 **78** | **315** | AI agent swarms, automated assistants, reasoning runtimes, and autonomous pipelines. | [**Browse All (315) ↗**](directory/autonomous-agents.md) |
| **💼 Enterprise SaaS & B2B Solutions** | 🟢 **64** | **269** | Enterprise cloud services, workflow software, corporate knowledge, and B2B platforms. | [**Browse All (269) ↗**](directory/enterprise-saas.md) |
| **🌐 Web Search, Crawling & Data Extraction** | 🟢 **52** | **104** | Web scrapers, search indices, document parsing, content extraction, and search tools. | [**Browse All (104) ↗**](directory/web-search-crawling.md) |
| **🛒 E-Commerce & Commercial Services** | 🟢 **8** | **67** | Online storefronts, retail catalogs, merchant operations, and commerce tools. | [**Browse All (67) ↗**](directory/ecommerce.md) |
| **📊 Enterprise Intelligence & Analytics** | 🟢 **9** | **52** | Data pipelines, market intelligence, telemetry monitoring, BI, and metrics. | [**Browse All (52) ↗**](directory/analytics.md) |
| **🔒 Cybersecurity & Infrastructure** | 🟢 **17** | **37** | Auth, threat detection, secret management, identity verification, TLS, and audit. | [**Browse All (37) ↗**](directory/cybersecurity.md) |
| **🧠 AI Foundations & Model Inference** | 🟢 **1** | **12** | Model serving endpoints, foundation labs, LLM hosting providers, and inference runtimes. | [**Browse All (12) ↗**](directory/ai-foundations.md) |

---

## 🌟 Featured Multi-Tool & High-Capacity Servers (100 Highlighted)

> Live remote servers offering verified multi-tool suites (`tools_count > 0`) or community-submitted Streamable HTTP endpoints.
>
> 💡 **Explore the complete registry**: Click into any vertical category table above, or query the full datasets in [`data/mcp-servers.json`](data/mcp-servers.json) and [`data/mcp-servers.csv`](data/mcp-servers.csv).

| Server / Host | Category | Business Model | Status | Latency | Tools | Manifest | DomainScope Dossier |
|---|---|---|:---:|:---:|:---:|:---:|:---:|
| **[a2milk.vn](https://a2milk.vn)**<br>*a2milk.vn* | 🌐 Web Search, Crawling & Data Extraction | `Retail Sales` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://a2milk.vn/.well-known/mcp/) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/a2milk.vn) |
| **[a2nutrition.com.au](https://a2nutrition.com.au)**<br>*a2nutrition.com.au* | 🌐 Web Search, Crawling & Data Extraction | `B2C Sales` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://a2nutrition.com.au/.well-known/mcp/) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/a2nutrition.com.au) |
| **[advances.in](https://advances.in)**<br>*advances-in-psychology* | 🌐 Web Search, Crawling & Data Extraction | `Subscription/Article Processing Charges (APCs)` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://advances.in/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/advances.in) |
| **[aegean.ai](https://aegean.ai)**<br>*aegean.ai Docs MCP* | 🌐 Web Search, Crawling & Data Extraction | `AI Services & Solutions` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://aegean.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aegean.ai) |
| **[alphasignal.ai](https://alphasignal.ai)**<br>*ai.alphasignal/news* | 🌐 Web Search, Crawling & Data Extraction | `Email subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://api.alphasignal.ai/mcp/server-card) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/alphasignal.ai) |
| **[artisangrowthstrategies.com](https://artisangrowthstrategies.com)**<br>*com.artisangrowthstrategies/knowledge* | 🌐 Web Search, Crawling & Data Extraction | `Professional Services (Consulting)` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.artisangrowthstrategies.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/artisangrowthstrategies.com) |
| **[biooart.com](https://biooart.com)**<br>*com.myhuiban.www/conference-partner* | 🌐 Web Search, Crawling & Data Extraction | `Event Organizing` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.myhuiban.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/biooart.com) |
| **[blockbear.app](https://blockbear.app)**<br>*Block Bear Docs MCP* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://blockbear.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/blockbear.app) |
| **[bsncraft.com](https://bsncraft.com)**<br>*BusinessCraft Docs MCP* | 🌐 Web Search, Crawling & Data Extraction | `Software Licensing` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://bsncraft.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/bsncraft.com) |
| **[bsvradar.com](https://bsvradar.com)**<br>*BSV Radar Directory* | 🌐 Web Search, Crawling & Data Extraction | `Community-driven engagement, advertising, and potential partnerships with BSV ecosystem projects` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://bsvradar.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/bsvradar.com) |
| **[buharex.com](https://buharex.com)**<br>*Buharex Catalog* | 🌐 Web Search, Crawling & Data Extraction | `E-commerce` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.buharx.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/buharex.com) |
| **[buharx.com](https://buharx.com)**<br>*Buharex Catalog* | 🌐 Web Search, Crawling & Data Extraction | `Domain registration and management services` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.buharx.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/buharx.com) |
| **[buscamed.com](https://buscamed.com)**<br>*com.buscamed/storefront* | 🌐 Web Search, Crawling & Data Extraction | `E-commerce` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://buscamed.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/buscamed.com) |
| **[chronotab.app](https://chronotab.app)**<br>*Chronotab Docs MCP* | 🌐 Web Search, Crawling & Data Extraction | `Freemium (with optional premium features)` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://chronotab.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/chronotab.app) |
| **[concya.com](https://concya.com)**<br>*concya* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.concya.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/concya.com) |
| **[constitucion.ai](https://constitucion.ai)**<br>*com.kemenystudio/buyer-commerce* | 🌐 Web Search, Crawling & Data Extraction | `Non-profit` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://kemenystudio.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/constitucion.ai) |
| **[curlec.com](https://curlec.com)**<br>*Razorpay Docs MCP* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://curlec.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/curlec.com) |
| **[davidbuenov.com](https://davidbuenov.com)**<br>*Model Context Protocol (MCP) Remote Server* | 🌐 Web Search, Crawling & Data Extraction | `Unknown` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://davidbuenov.com/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/davidbuenov.com) |
| **[dchub.cloud](https://dchub.cloud)**<br>*DC Hub MCP Server* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://dchub.cloud/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/dchub.cloud) |
| **[dynamikorbits.com](https://dynamikorbits.com)**<br>*dynamik-public* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://api.dynamikorbits.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/dynamikorbits.com) |
| **[easyrealty.app](https://easyrealty.app)**<br>*EasyRealty* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://easyrealty.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/easyrealty.app) |
| **[etla.fi](https://etla.fi)**<br>*Etla* | 🌐 Web Search, Crawling & Data Extraction | `Research Grants and Projects` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://etla.fi/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/etla.fi) |
| **[flevy.com](https://flevy.com)**<br>*Flevy* | 🌐 Web Search, Crawling & Data Extraction | `Marketplace with both free and paid resources` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://flevy.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/flevy.com) |
| **[fluege.de](https://fluege.de)**<br>*de.fluege/flights* | 🌐 Web Search, Crawling & Data Extraction | `Commission-based ( earns money by redirecting users to airline websites)` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.fluege.de/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/fluege.de) |
| **[frase.io](https://frase.io)**<br>*io.frase/mcp* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.frase.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/frase.io) |
| **[getcatalog.ai](https://getcatalog.ai)**<br>*ai.getcatalog/site* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.getcatalog.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/getcatalog.ai) |
| **[globalesim.app](https://globalesim.app)**<br>*Global eSIM MCP* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://globalesim.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/globalesim.app) |
| **[greenbook.org](https://greenbook.org)**<br>*GreenBook MCP Server* | 🌐 Web Search, Crawling & Data Extraction | `Directory Listing Service` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.greenbook.org/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/greenbook.org) |
| **[grosswald.org](https://grosswald.org)**<br>*grosswald-data* | 🌐 Web Search, Crawling & Data Extraction | `Subscription/Access-based` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.grosswald.org/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/grosswald.org) |
| **[hypepaper.app](https://hypepaper.app)**<br>*app.hypepaper/hypepaper* | 🌐 Web Search, Crawling & Data Extraction | `Unknown` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://hypepaper.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/hypepaper.app) |
| **[infino.ai](https://infino.ai)**<br>*Infino Docs MCP* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://infino.ai/docs/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/infino.ai) |
| **[instant.ai](https://instant.ai)**<br>*ai.instant/domain-search* | 🌐 Web Search, Crawling & Data Extraction | `E-commerce` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://instant.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/instant.ai) |
| **[instant.ca](https://instant.ca)**<br>*ai.instant/domain-search* | 🌐 Web Search, Crawling & Data Extraction | `Domain Name Registration Fees` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://instant.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/instant.ca) |
| **[listingbooster.ai](https://listingbooster.ai)**<br>*listingbooster-public-discovery* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://listingbooster.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/listingbooster.ai) |
| **[mainstreetwealth.ai](https://mainstreetwealth.ai)**<br>*main-street-wealth-mcp* | 🌐 Web Search, Crawling & Data Extraction | `Commission-based` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://mainstreetwealth.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/mainstreetwealth.ai) |
| **[maldivesindependent.com](https://maldivesindependent.com)**<br>*maldives-independent-mcp* | 🌐 Web Search, Crawling & Data Extraction | `Advertising` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://maldivesindependent.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/maldivesindependent.com) |
| **[multidrive.app](https://multidrive.app)**<br>*multidrive* | 🌐 Web Search, Crawling & Data Extraction | `Freeware with potential premium features` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://multidrive.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/multidrive.app) |
| **[name.ai](https://name.ai)**<br>*name-ai* | 🌐 Web Search, Crawling & Data Extraction | `Marketplace, Brokerage` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://name.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/name.ai) |
| **[nomadlist.com](https://nomadlist.com)**<br>*Nomads.com* | 🌐 Web Search, Crawling & Data Extraction | `Advertising, Affiliate Marketing` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://nomads.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/nomadlist.com) |
| **[padlet.help](https://padlet.help)**<br>*help.padlet/padlet-helpdocs* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://padlet.help/api/mcp/server-card) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/padlet.help) |
| **[plantis.ai](https://plantis.ai)**<br>*The AI Conductor Framework Docs MCP* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://plantis.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/plantis.ai) |
| **[preetham.org](https://preetham.org)**<br>*preetham kyanam Docs MCP* | 🌐 Web Search, Crawling & Data Extraction | `Freelance/Independent` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://preetham.org/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/preetham.org) |
| **[prosperconsulting.ai](https://prosperconsulting.ai)**<br>*ai.prosperconsulting/public* | 🌐 Web Search, Crawling & Data Extraction | `Consulting Services` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://prosperconsulting.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/prosperconsulting.ai) |
| **[servmeco.com](https://servmeco.com)**<br>*servme-content* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://servmeco.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/servmeco.com) |
| **[silkdata.tech](https://silkdata.tech)**<br>*silkdata-search* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://silkdata.tech/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/silkdata.tech) |
| **[startuphub.ai](https://startuphub.ai)**<br>*StartupHub.ai* | 🌐 Web Search, Crawling & Data Extraction | `Advertising & Sponsored Content` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.startuphub.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/startuphub.ai) |
| **[tooldirectory.ai](https://tooldirectory.ai)**<br>*tooldirectory-ai* | 🌐 Web Search, Crawling & Data Extraction | `Advertising, Affiliate Marketing` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://tooldirectory.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/tooldirectory.ai) |
| **[truetone.ai](https://truetone.ai)**<br>*truetone-ai* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.truetone.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/truetone.ai) |
| **[vaaya.ai](https://vaaya.ai)**<br>*vaaya* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://vaaya.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/vaaya.ai) |
| **[visibilio.ai](https://visibilio.ai)**<br>*visibilio-content-hub* | 🌐 Web Search, Crawling & Data Extraction | `SaaS_subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://visibilio.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/visibilio.ai) |
| **[windowsforum.com](https://windowsforum.com)**<br>*WindowsForum MCP Server* | 🌐 Web Search, Crawling & Data Extraction | `Advertising` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://windowsforum.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/windowsforum.com) |
| **[xerpa.ai](https://xerpa.ai)**<br>*xerpa-site-mcp* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://xerpa.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/xerpa.ai) |
| **[100ke.ai](https://100ke.ai)**<br>*100K Experts Content* | 💼 Enterprise SaaS & B2B Solutions | `Free, Non-Profit` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://100ke.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/100ke.ai) |
| **[3byggetilbud.dk](https://3byggetilbud.dk)**<br>*3byggetilbud-site* | 💼 Enterprise SaaS & B2B Solutions | `Lead Generation` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://3byggetilbud.dk/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/3byggetilbud.dk) |
| **[9punto5.cl](https://9punto5.cl)**<br>*cl.9punto5/application-preparation* | 💼 Enterprise SaaS & B2B Solutions | `Event-based` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://9punto5.cl/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/9punto5.cl) |
| **[aave.com](https://aave.com)**<br>*com.aave/mcp* | 💼 Enterprise SaaS & B2B Solutions | `Open-source software development, decentralized finance platform` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://mcp.aave.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aave.com) |
| **[aave.org](https://aave.org)**<br>*com.aave/mcp* | 💼 Enterprise SaaS & B2B Solutions | `Open-source protocol with decentralized governance` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://aave.org/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aave.org) |
| **[ajansspor.com](https://ajansspor.com)**<br>*com.ajansspor/news* | 💼 Enterprise SaaS & B2B Solutions | `Advertising` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://ajansspor.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ajansspor.com) |
| **[armorathletics.com](https://armorathletics.com)**<br>*armor-athletics* | 💼 Enterprise SaaS & B2B Solutions | `Membership fees (monthly plans, drop-ins, punch cards, and personal training sessions)` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://armorathletics.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/armorathletics.com) |
| **[auftrag.ai](https://auftrag.ai)**<br>*Auftrag One* | 💼 Enterprise SaaS & B2B Solutions | `Subscription-based SaaS` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://auftragone.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/auftrag.ai) |
| **[bodyland.nl](https://bodyland.nl)**<br>*mensbodyland-discovery* | 💼 Enterprise SaaS & B2B Solutions | `Appointment-based Services` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://bodyland.nl/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/bodyland.nl) |
| **[brito.ai](https://brito.ai)**<br>*ai.brito/website* | 💼 Enterprise SaaS & B2B Solutions | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://brito.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/brito.ai) |
| **[cars-data.com](https://cars-data.com)**<br>*cars-data.com Car Specs MCP* | 💼 Enterprise SaaS & B2B Solutions | `Advertising` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://cars-data.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/cars-data.com) |
| **[chavesnamao.com.br](https://chavesnamao.com.br)**<br>*chavesnamao-mcp* | 💼 Enterprise SaaS & B2B Solutions | `Advertising` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://chavesnamao.com.br/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/chavesnamao.com.br) |
| **[checkatrade.com](https://checkatrade.com)**<br>*com.checkatrade/consumer-mcp* | 💼 Enterprise SaaS & B2B Solutions | `Subscription-based leads generation` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.checkatrade.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/checkatrade.com) |
| **[clairemed.ai](https://clairemed.ai)**<br>*Claire Knowledge MCP* | 💼 Enterprise SaaS & B2B Solutions | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://clairemed.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/clairemed.ai) |
| **[coastalecoheatair.com](https://coastalecoheatair.com)**<br>*Coastal Eco Heating & Air* | 💼 Enterprise SaaS & B2B Solutions | `Service Fee` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://coastalecoheatair.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/coastalecoheatair.com) |
| **[conversion.com.br](https://conversion.com.br)**<br>*conversion-public-content* | 💼 Enterprise SaaS & B2B Solutions | `Project-based consulting and retainer services` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.conversion.com.br/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/conversion.com.br) |
| **[datreal.com](https://datreal.com)**<br>*Datreal.com MCP Server* | 💼 Enterprise SaaS & B2B Solutions | `Subscription-based` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://datreal.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/datreal.com) |
| **[directcare.ai](https://directcare.ai)**<br>*directcare-ai* | 💼 Enterprise SaaS & B2B Solutions | `Subscription-based` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.directcare.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/directcare.ai) |
| **[domainsales.ai](https://domainsales.ai)**<br>*connect* | 💼 Enterprise SaaS & B2B Solutions | `E-commerce` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://youspot.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/domainsales.ai) |
| **[durhamdenturesandimplants.com](https://durhamdenturesandimplants.com)**<br>*Durham Dentures and Implants* | 💼 Enterprise SaaS & B2B Solutions | `Private Practice` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://durhamdenturesandimplants.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/durhamdenturesandimplants.com) |
| **[duyet.net](https://duyet.net)**<br>*duyet-mcp-server* | 💼 Enterprise SaaS & B2B Solutions | `B2B SaaS` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://duyet.net/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/duyet.net) |
| **[ec-eco-10060.com](https://ec-eco-10060.com)**<br>*SPARKS CPG Knowledge Graph* | 💼 Enterprise SaaS & B2B Solutions | `regulatory_standardization` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://ec-eco-10060.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ec-eco-10060.com) |
| **[edenspiekermann.com](https://edenspiekermann.com)**<br>*edenspiekermann-public* | 💼 Enterprise SaaS & B2B Solutions | `Project-based and retainer services` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.edenspiekermann.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/edenspiekermann.com) |
| **[engineeringleaders.cz](https://engineeringleaders.cz)**<br>*elc-toolkit* | 💼 Enterprise SaaS & B2B Solutions | `Volunteer-driven` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.engineeringleaders.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/engineeringleaders.cz) |
| **[every.to](https://every.to)**<br>*every-to* | 💼 Enterprise SaaS & B2B Solutions | `Subscription-based (includes access to articles, software products, and community)` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://every.to/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/every.to) |
| **[fertilityscience.ai](https://fertilityscience.ai)**<br>*FertilityScience* | 💼 Enterprise SaaS & B2B Solutions | `Subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://fertilityscience.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/fertilityscience.ai) |
| **[finartha.ai](https://finartha.ai)**<br>*finartha* | 💼 Enterprise SaaS & B2B Solutions | `Subscription-based services` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://finartha.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/finartha.ai) |
| **[flamel.ai](https://flamel.ai)**<br>*flamel-public-content* | 💼 Enterprise SaaS & B2B Solutions | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.flamel.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/flamel.ai) |
| **[fonestorm.ai](https://fonestorm.ai)**<br>*fonestorm-ai* | 💼 Enterprise SaaS & B2B Solutions | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://fonestorm.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/fonestorm.ai) |
| **[fplai.app](https://fplai.app)**<br>*FPLai Content MCP* | 💼 Enterprise SaaS & B2B Solutions | `Subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://fplai.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/fplai.app) |
| **[guitarwiz.app](https://guitarwiz.app)**<br>*guitarwiz-mcp* | 💼 Enterprise SaaS & B2B Solutions | `Freemium (with in-app purchases)` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://guitarwiz.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/guitarwiz.app) |
| **[hypercube.ai](https://hypercube.ai)**<br>*pinecone-marketing* | 💼 Enterprise SaaS & B2B Solutions | `SaaS_subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.pinecone.io/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/hypercube.ai) |
| **[idescat.cat](https://idescat.cat)**<br>*cat.idescat/mcp* | 💼 Enterprise SaaS & B2B Solutions | `Public Funding` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://api.idescat.cat/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/idescat.cat) |
| **[ironwise.app](https://ironwise.app)**<br>*ironwise* | 💼 Enterprise SaaS & B2B Solutions | `Membership subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://ironwise.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ironwise.app) |
| **[launchdub.ai](https://launchdub.ai)**<br>*launchdubai-book* | 💼 Enterprise SaaS & B2B Solutions | `Professional Services` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://launchdub.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/launchdub.ai) |
| **[lifescenario.ai](https://lifescenario.ai)**<br>*ai.lifescenario/info* | 💼 Enterprise SaaS & B2B Solutions | `Subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://lifescenario.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/lifescenario.ai) |
| **[loops.so](https://loops.so)**<br>*so.loops/mcp* | 💼 Enterprise SaaS & B2B Solutions | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://loops.so/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/loops.so) |
| **[mentimeter.com](https://mentimeter.com)**<br>*mentimeter-content* | 💼 Enterprise SaaS & B2B Solutions | `SaaS subscription with free and paid plans` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.mentimeter.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/mentimeter.com) |
| **[muenchener-verein.de](https://muenchener-verein.de)**<br>*Münchener Verein MCP* | 💼 Enterprise SaaS & B2B Solutions | `Premium-based` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.muenchener-verein.de/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/muenchener-verein.de) |
| **[neteon.ai](https://neteon.ai)**<br>*neteon-ai* | 💼 Enterprise SaaS & B2B Solutions | `Hardware Sales` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://neteon.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/neteon.ai) |
| **[otomoto.pl](https://otomoto.pl)**<br>*Otomoto* | 💼 Enterprise SaaS & B2B Solutions | `Advertising (Classified Ads)` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.otomoto.pl:443/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/otomoto.pl) |
| **[phish.in](https://phish.in)**<br>*phishin* | 💼 Enterprise SaaS & B2B Solutions | `Donation-based` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://phish.in/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/phish.in) |
| **[plaved.tech](https://plaved.tech)**<br>*plaved-tech* | 💼 Enterprise SaaS & B2B Solutions | `Consulting Services` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://plaved.tech/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/plaved.tech) |
| **[playlistable.io](https://playlistable.io)**<br>*Playlistable* | 💼 Enterprise SaaS & B2B Solutions | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://playlistable.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/playlistable.io) |
| **[pocket.science](https://pocket.science)**<br>*pocket-science-mcp* | 💼 Enterprise SaaS & B2B Solutions | `SaaS subscription, Hardware sales` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://pocket.science/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/pocket.science) |
| **[pointhacks.com.au](https://pointhacks.com.au)**<br>*com.pointhacks/mcp* | 💼 Enterprise SaaS & B2B Solutions | `Affiliate Marketing (credit card referrals)` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://www.pointhacks.com.au/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/pointhacks.com.au) |
| **[raconte.ai](https://raconte.ai)**<br>*ai.raconte/raconte* | 💼 Enterprise SaaS & B2B Solutions | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://raconte.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/raconte.ai) |
| **[radianthealth.app](https://radianthealth.app)**<br>*radianthealth-mcp* | 💼 Enterprise SaaS & B2B Solutions | `SaaS subscription` | 🟢 **Verified** | - | ✓ | [Manifest ↗](https://radianthealth.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/radianthealth.app) |

---

## 🏢 Distribution by Business Delivery Model

Classified by DomainScope's firmographic model inference:

- **SaaS subscription**: **606 servers**
- **Advertising**: **42 servers**
- **Open Source**: **33 servers**
- **E-commerce**: **25 servers**
- **Consulting Services**: **21 servers**
- **B2B SaaS**: **16 servers**
- **Non-profit**: **14 servers**
- **SaaS_subscription**: **14 servers**
- **Unknown**: **8 servers**
- **Transaction fees**: **8 servers**
- **Subscription-based**: **7 servers**
- **Subscription**: **7 servers**
- **Freemium**: **7 servers**
- **Services**: **7 servers**
- **Freemium (with in-app purchases)**: **6 servers**
- **Subscription-based SaaS**: **5 servers**
- **Professional Services**: **5 servers**
- **Open-source**: **5 servers**
- **Personal Blog**: **5 servers**
- **Commission-based**: **4 servers**
- **Freelance Services**: **4 servers**
- **Freelance/Contract Work**: **4 servers**
- **Advertising and Affiliate Marketing**: **4 servers**
- **Advertising, Affiliate Marketing**: **3 servers**
- **Service Fee**: **3 servers**
- **Private Practice**: **3 servers**
- **Project-based and retainer services**: **3 servers**
- **Public Funding**: **3 servers**
- **B2B Sales**: **3 servers**
- **Freemium with Premium Subscription**: **3 servers**
- **Open-source, community-driven**: **3 servers**
- **Ticket Sales**: **3 servers**
- **Medical Services**: **3 servers**
- **Custom Software Development Services**: **3 servers**
- **Project-based and Retainer Models**: **3 servers**
- **Freelance/Independent**: **2 servers**
- **Lead Generation**: **2 servers**
- **SaaS subscription with free and paid plans**: **2 servers**
- **Donation-based**: **2 servers**
- **Unknown (likely not monetized)**: **2 servers**
- **Venture Capital**: **2 servers**
- **Donations and grants**: **2 servers**
- **Rental Income**: **2 servers**
- **Coaching Services**: **2 servers**
- **Not specified**: **2 servers**
- **Personal Branding**: **2 servers**
- **Project-based Consulting**: **2 servers**
- **Open Source (No direct revenue)**: **2 servers**
- **SaaS subscription (pay-per-use)**: **2 servers**
- **Not applicable**: **2 servers**
- **Non-profit (No revenue generation)**: **2 servers**
- **Marketing Services**: **2 servers**
- **Service-based subscription**: **2 servers**
- **Tuition Fees**: **2 servers**
- **Project-based Services**: **2 servers**
- **Service-based**: **2 servers**
- **Freemium with premium subscriptions**: **2 servers**
- **Tuition-based**: **2 servers**
- **Paid Services**: **2 servers**
- **Donations/Contributions**: **2 servers**
- **Public Service**: **2 servers**
- **Donations and community support**: **2 servers**
- **B2B Services**: **2 servers**
- **Project-based**: **2 servers**
- **Custom Projects**: **2 servers**
- **Retail Sales**: **1 servers**
- **B2C Sales**: **1 servers**
- **Subscription/Article Processing Charges (APCs)**: **1 servers**
- **AI Services & Solutions**: **1 servers**
- **Email subscription**: **1 servers**
- **Professional Services (Consulting)**: **1 servers**
- **Event Organizing**: **1 servers**
- **Software Licensing**: **1 servers**
- **Community-driven engagement, advertising, and potential partnerships with BSV ecosystem projects**: **1 servers**
- **Domain registration and management services**: **1 servers**
- **Freemium (with optional premium features)**: **1 servers**
- **Research Grants and Projects**: **1 servers**
- **Marketplace with both free and paid resources**: **1 servers**
- **Commission-based ( earns money by redirecting users to airline websites)**: **1 servers**
- **Directory Listing Service**: **1 servers**
- **Subscription/Access-based**: **1 servers**
- **Domain Name Registration Fees**: **1 servers**
- **Freeware with potential premium features**: **1 servers**
- **Marketplace, Brokerage**: **1 servers**
- **Advertising & Sponsored Content**: **1 servers**
- **Free, Non-Profit**: **1 servers**
- **Event-based**: **1 servers**
- **Open-source software development, decentralized finance platform**: **1 servers**
- **Open-source protocol with decentralized governance**: **1 servers**
- **Membership fees (monthly plans, drop-ins, punch cards, and personal training sessions)**: **1 servers**
- **Appointment-based Services**: **1 servers**
- **Subscription-based leads generation**: **1 servers**
- **Project-based consulting and retainer services**: **1 servers**
- **regulatory_standardization**: **1 servers**
- **Volunteer-driven**: **1 servers**
- **Subscription-based (includes access to articles, software products, and community)**: **1 servers**
- **Subscription-based services**: **1 servers**
- **Membership subscription**: **1 servers**
- **Premium-based**: **1 servers**
- **Hardware Sales**: **1 servers**
- **Advertising (Classified Ads)**: **1 servers**
- **SaaS subscription, Hardware sales**: **1 servers**
- **Affiliate Marketing (credit card referrals)**: **1 servers**
- **Subscription-based (Substack)**: **1 servers**
- **Service Subscription**: **1 servers**
- **Subscription-based with additional services**: **1 servers**
- **Premium Subscription with Free Access to Basic Features**: **1 servers**
- **Commission-based fee structure for successful investments facilitated through the platform**: **1 servers**
- **Project-based and subscription services**: **1 servers**
- **Grant-funded**: **1 servers**
- **SaaS subscription with tiered pricing plans**: **1 servers**
- **Subscription-based online courses**: **1 servers**
- **Paid subscriptions and courses**: **1 servers**
- **Restaurant and Grocery Sales**: **1 servers**
- **Direct retail sales (in-person) with additional revenue from catering, custom cakes, and prepared foods**: **1 servers**
- **Consultation Services**: **1 servers**
- **Commission-based marketplace**: **1 servers**
- **E-commerce and Services**: **1 servers**
- **Personal Blog/Projects**: **1 servers**
- **SaaS subscription with free trial**: **1 servers**
- **Open-source and community support**: **1 servers**
- **Open-source with API key requirement**: **1 servers**
- **Non-profit/Open Source**: **1 servers**
- **Stablecoin issuance and infrastructure services**: **1 servers**
- **SaaS subscription with free individual site lookups**: **1 servers**
- **Project-based and retainer fees**: **1 servers**
- **Advertising, Commission-based Bookings**: **1 servers**
- **Service**: **1 servers**
- **Cryptocurrency Trading Platform**: **1 servers**
- **Freemium API access with paid tiers for higher usage and advanced features**: **1 servers**
- **Content_monetization_through_affiliate_partnerships_and_personal_projects**: **1 servers**
- **SaaS subscription with pay-per-use pricing for AI compute resources**: **1 servers**
- **Subscription-based SaaS platform with additional transaction fees**: **1 servers**
- **Non-commercial (personal notes)**: **1 servers**
- **Advertising/Sponsorship**: **1 servers**
- **Software as a Service (SaaS)**: **1 servers**
- **Premium Subscription, Token Staking**: **1 servers**
- **Tour Package Sales**: **1 servers**
- **Open Source/Community Supported**: **1 servers**
- **Project-based and Subscription-based Services**: **1 servers**
- **Non-profit (No affiliation with Home Assistant)**: **1 servers**
- **Donation-based (open source)**: **1 servers**
- **Open Source/Community Support**: **1 servers**
- **Community-driven (No revenue)**: **1 servers**
- **Subscription-based Courses, Premium Membership (Suraasa Plus)**: **1 servers**
- **Advertising & Book Sales**: **1 servers**
- **Donations/Open Source**: **1 servers**
- **Token-based platform**: **1 servers**
- **Yield Farming, Trading Fees**: **1 servers**
- **Book Sales**: **1 servers**
- **Advertising (no ads mentioned, so it might be donation-based or other)**: **1 servers**
- **Subscription-based with listing options**: **1 servers**
- **Community-driven (free membership, open specifications, and public resources with potential for future monetization via .agent TLD or related services)**: **1 servers**
- **API usage and potential premium features**: **1 servers**
- **Services and Consulting**: **1 servers**
- **Premium subscriptions and data licensing**: **1 servers**
- **Unspecified**: **1 servers**
- **Licensing**: **1 servers**
- **mixed (consulting, open-source tools, experimental projects, and proprietary AI/software solutions for higher education)**: **1 servers**
- **Freelance/Contract**: **1 servers**
- **Listing Fees**: **1 servers**
- **Accommodation and Activity Fees**: **1 servers**
- **Print Subscription, Advertising**: **1 servers**
- **SaaS subscription with managed advertising**: **1 servers**
- **content_aggregation_and_engagement**: **1 servers**
- **Project-based and retainer models for services**: **1 servers**
- **SaaS subscription, Pay-per-session**: **1 servers**
- **SaaS subscription (likely)**: **1 servers**
- **API subscription**: **1 servers**
- **Freemium Subscription**: **1 servers**
- **Advertising (Substack)**: **1 servers**
- **Volunteer-driven, no revenue generation**: **1 servers**
- **Transaction fees, service charges**: **1 servers**
- **Data licensing and API services**: **1 servers**
- **E-learning platform with paid courses**: **1 servers**
- **Training and Services**: **1 servers**
- **Job Board Listing Fees**: **1 servers**
- **Job Board Advertising**: **1 servers**
- **Freemium with Subscription**: **1 servers**
- **Insurance Premiums**: **1 servers**
- **Subscription-based Research and API Access**: **1 servers**
- **Freemium (App Store)**: **1 servers**
- **Subscription-based with free delivery and discounts**: **1 servers**
- **Market Research Services**: **1 servers**
- **Subscription-based with additional fees for non-member deliveries**: **1 servers**
- **Subscription-based with optional premium service (Knuspr Xtra)**: **1 servers**
- **Research Services & Membership Packages**: **1 servers**
- **Transaction fees, liquidity mining rewards**: **1 servers**
- **Freemium (with optional paid subscription)**: **1 servers**
- **Open Source Software**: **1 servers**
- **E-commerce Subscription + Delivery Fees**: **1 servers**
- **Government Funded**: **1 servers**
- **Subscription-based access to cybersecurity tools**: **1 servers**
- **B2B service**: **1 servers**
- **Gaming Revenue**: **1 servers**
- **Rental and Sales**: **1 servers**
- **Freight Brokerage**: **1 servers**
- **Tuition fees and partnerships**: **1 servers**
- **Affinity marketing**: **1 servers**
- **Medical Device Sales**: **1 servers**
- **Advertising (CPM)**: **1 servers**
- **Merchandising, Ticket Sales, Music Streaming Royalties**: **1 servers**
- **Pay-per-service**: **1 servers**
- **Sales of agricultural products**: **1 servers**
- **Project-based fees**: **1 servers**
- **Angel Investing, Advisory Services**: **1 servers**
- **Custom Order**: **1 servers**
- **Premiums and investments**: **1 servers**
- **Dining**: **1 servers**
- **Day passes, lunch reservations, room bookings**: **1 servers**
- **Freemium (Free tools with premium services)**: **1 servers**
- **Freelance/Commission-based**: **1 servers**
- **Freemium (free basic features with optional premium tools, no explicit subscription revenue model mentioned)**: **1 servers**
- **SaaS subscription (Software as a Service)**: **1 servers**
- **Utility Services**: **1 servers**
- **Membership fees, interest on loans, service charges**: **1 servers**
- **Brokerage Fees**: **1 servers**
- **Listing and Brokerage Fees**: **1 servers**
- **Subscription-based with free trials and courses**: **1 servers**
- **freelance_consulting**: **1 servers**
- **Online course sales and digital content distribution**: **1 servers**
- **Subscription-based (assumed)**: **1 servers**
- **Fee-for-service**: **1 servers**
- **Licensing and Sales of Technology**: **1 servers**
- **SaaS subscription, done-for-you services (e.g., social media posts), and AI-powered tool licensing**: **1 servers**
- **Memberships, Apparel Sales**: **1 servers**
- **E-commerce & Subscription**: **1 servers**
- **B2B/B2C Sales**: **1 servers**
- **Freemium (in-app purchases)**: **1 servers**
- **Ticket sales, commercial activities (bookshop)**: **1 servers**
- **SaaS subscription with pay-less-as-you-grow pricing**: **1 servers**
- **Sales of Hardware and Software Solutions**: **1 servers**
- **Pay-what-you-want**: **1 servers**
- **Donations, Government Funding**: **1 servers**
- **Government funding and membership fees**: **1 servers**
- **Government-funded**: **1 servers**
- **Advertising (inferred)**: **1 servers**
- **Personal Branding/Content Creation**: **1 servers**
- **Freemium subscription with premium features and ads**: **1 servers**
- **Advertising, Subscription**: **1 servers**
- **Sponsored Events & Content**: **1 servers**
- **B2G (Business-to-Government)**: **1 servers**
- **Banking Services**: **1 servers**
- **Product Sales**: **1 servers**
- **Non-profit, event-based**: **1 servers**
- **Domain Name Sales and Registrations**: **1 servers**
- **Asset Management Fees**: **1 servers**
- **Subscription-based with free trial available**: **1 servers**
- **Freemium (app is free, with optional premium features)**: **1 servers**
- **Freemium subscription with premium features**: **1 servers**
- **Broadcasting and Streaming**: **1 servers**
- **Advertising, Subscriptions**: **1 servers**
- **SaaS subscription (Premium/Premium Protect)**: **1 servers**
- **Freemium (Free with optional donations)**: **1 servers**
- **Consulting fees, Commission-based revenue**: **1 servers**
- **Media & Content**: **1 servers**
- **Premiums**: **1 servers**
- **Premium Theme Sales, Subscriptions (Pro Plans)**: **1 servers**
- **Subscription-based service with monthly fees**: **1 servers**
- **Subscription-based, Pay-per-use**: **1 servers**
- **Rental Services**: **1 servers**
- **Freemium (with potential premium features)**: **1 servers**
- **Commission-based fees on trades**: **1 servers**
- **Project-based, Outsourcing**: **1 servers**
- **Wholesale/Distribution (B2B) with retail sales through dispensaries (B2C)**: **1 servers**
- **SaaS subscription (with potential API integrations and marketplace services)**: **1 servers**
- **SaaS subscription, Partnerships**: **1 servers**
- **Wholesale**: **1 servers**
- **SaaS subscription with free, starter, pro, and premium plans**: **1 servers**
- **SaaS subscription with premium features**: **1 servers**
- **Open-source/Freeware**: **1 servers**
- **Donations and listener support**: **1 servers**
- **E-commerce (product sales) and service-based (consultations, sessions, and readings)**: **1 servers**
- **Freemium (Freebies & Premium Assets)**: **1 servers**
- **Freemium with subscription plans**: **1 servers**
- **B2B SaaS subscription**: **1 servers**
- **Non-profit/Research**: **1 servers**
- **Press Release Distribution Services**: **1 servers**
- **Ticket sales and bar revenue**: **1 servers**
- **Hourly billing and retainer services**: **1 servers**
- **Subscription-based online classes and workshops**: **1 servers**
- **Earned Rewards**: **1 servers**
- **Managed Services**: **1 servers**
- **Unknown (likely independent, non-commercial)**: **1 servers**
- **Tuition fees and course enrollment payments**: **1 servers**
- **B2B wholesale distribution and bulk supply**: **1 servers**
- **Discount Retail**: **1 servers**
- **Affiliate Marketing**: **1 servers**
- **Content-driven with potential affiliate or referral partnerships for financial products**: **1 servers**
- **Service-based (project contracts and labor)**: **1 servers**
- **E-commerce with local pickup**: **1 servers**
- **Software as a Service (SaaS) subscription**: **1 servers**
- **E-commerce, subscription-based premium features**: **1 servers**
- **Premium Memberships, Donations**: **1 servers**
- **Commission-based (charges a fee per order)**: **1 servers**
- **Chauffeur Service Bookings**: **1 servers**
- **Donations, Adoptions, Grants**: **1 servers**
- **Pay-What-You-Wish (tips-based)**: **1 servers**
- **Commission-based Trading**: **1 servers**
- **E-commerce with physical stores**: **1 servers**
- **Membership fees**: **1 servers**
- **Membership-based insurance program**: **1 servers**
- **Freemium (free with optional premium features)**: **1 servers**
- **SaaS subscription (free with paid plans)**: **1 servers**
- **one-time payment per service (transactional)**: **1 servers**
- **SaaS subscription & API usage**: **1 servers**
- **Service-based (custom development, equipment sales, and rentals)**: **1 servers**
- **Freemium_with_advertising_and_content_sponsorship**: **1 servers**
- **SaaS subscription (software-as-a-service)**: **1 servers**
- **SaaS subscription (with free tier)**: **1 servers**
- **Advertising and Sponsorships**: **1 servers**
- **Freelance services, source code sales, tutorials**: **1 servers**
- **SaaS subscription and pay-per-use messaging services**: **1 servers**
- **Freemium with subscription and one-time credit packs (SaaS-based)**: **1 servers**
- **SaaS subscription with affordable pricing plans**: **1 servers**
- **One-Time Purchase**: **1 servers**
- **Freemium/SaaS subscription**: **1 servers**
- **Cloud Services Subscription**: **1 servers**
- **B2B**: **1 servers**
- **SaaS subscription with free tier**: **1 servers**
- **B2B SaaS subscription with additional revenue from transaction fees**: **1 servers**
- **Freelance Consulting**: **1 servers**
- **Freemium (with optional paid plans)**: **1 servers**
- **SaaS subscription ($29/month or $249/year)**: **1 servers**
- **Freemium with premium extensions**: **1 servers**
- **Subscription and Certifications**: **1 servers**
- **Freelance or Personal Project**: **1 servers**
- **SaaS subscription with free community edition**: **1 servers**
- **Subscription-based with free trials available**: **1 servers**
- **Custom Development Services**: **1 servers**
- **Open-source and sponsorships**: **1 servers**
- **SaaS subscription (Free version available)**: **1 servers**
- **Open Source with Optional Premium Features**: **1 servers**
- **Free to Use**: **1 servers**
- **Project-based consulting and services**: **1 servers**
- **Non-profit/Advertising**: **1 servers**
- **Community-powered**: **1 servers**
- **Freemium (Free tier with paid PRO features)**: **1 servers**
- **Cryptocurrency Rewards**: **1 servers**
- **SaaS subscription and PAYG**: **1 servers**
- **Custom Software Development**: **1 servers**
- **Consulting Services, Course Sales, Affiliate Marketing**: **1 servers**
- **Manufacturing and Sales**: **1 servers**
- **Investment, Strategic Acquisitions**: **1 servers**
- **Pay-per-use**: **1 servers**
- **Open-Source Software with Enterprise Offerings**: **1 servers**
- **Free Resource Sharing**: **1 servers**
- **Non-profit (No registration required)**: **1 servers**
- **Open-source and community-driven**: **1 servers**
- **Freemium (free tier with paid upgrades for advanced features)**: **1 servers**
- **consulting_and_content_creation**: **1 servers**
- **Cloud Offering with Free Trial**: **1 servers**
- **Advertising (free listings with optional premium features)**: **1 servers**
- **Freemium (with optional paid features)**: **1 servers**
- **Class and Rental Fees**: **1 servers**
- **Subscription-based services (SaaS), project-based consulting, and managed services**: **1 servers**
- **Paid Software**: **1 servers**
- **Venture Capital, Startup Investment**: **1 servers**
- **SaaS subscription with free tutorials**: **1 servers**
- **Freelance Writing Services**: **1 servers**
- **Advertisement-based**: **1 servers**
- **Open-source contributions**: **1 servers**
- **SaaS subscription with free tier available**: **1 servers**
- **Subscription-based Web Hosting Services**: **1 servers**
- **Commission-based sales of luxury properties**: **1 servers**
- **Decentralized Platform**: **1 servers**
- **Community Support and Sponsorship**: **1 servers**
- **Decentralized Network, Token-based Incentives**: **1 servers**
- **Software Sales**: **1 servers**
- **Recruitment Services**: **1 servers**
- **Selling Software**: **1 servers**
- **Freemium (Free while in beta) with potential future monetization via Coil and Interledger Protocol**: **1 servers**
- **SaaS subscription (free credits)**: **1 servers**
- **Open Source with Optional Paid Features**: **1 servers**
- **Free for design partners, potential revenue from enterprise use**: **1 servers**
- **Interest income from savings accounts**: **1 servers**
- **Freelance or Personal Projects**: **1 servers**
- **In-game purchases and potentially partnerships for rewards**: **1 servers**
- **Project-based and subscription-based services**: **1 servers**
- **Email Marketing**: **1 servers**
- **Open Source & Donations**: **1 servers**
- **API Access Subscription**: **1 servers**
- **SaaS subscription with freemium model**: **1 servers**

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

---

## 📚 Citation, Research & Press Attribution

If you use this dataset, telemetry benchmarks, or directory in academic research, articles, industry analyses, or publications, please cite it as follows:

### Markdown / Plain Text
> Badita, F. (2026). *Awesome Live MCP Servers: The Autonomous Internet-Scale Registry of Remote Model Context Protocol Servers*. DomainScope at Scrape the World. https://github.com/baditaflorin/awesome-live-mcp-servers

### BibTeX
```bibtex
@misc{badita2026awesomelivemcpservers,
  author = {Badita, Florin},
  title = {Awesome Live MCP Servers: The Autonomous Internet-Scale Registry of Remote Model Context Protocol Servers},
  institution = {DomainScope at Scrape the World},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/baditaflorin/awesome-live-mcp-servers}},
  url = {https://github.com/baditaflorin/awesome-live-mcp-servers}
}
```

---

## 📬 Contact, Press & Research Inquiries

For media interviews, research collaborations, custom dataset slices, or partnership inquiries:
- **Author / Maintainer**: Florin Badita
- **Email**: [`florin@badita.org`](mailto:florin@badita.org)
- **Initiative**: [DomainScope at Scrape the World](https://domainscope.scrapetheworld.org)
- **License**: [MIT License](LICENSE)

**Maintained by Florin Badita & [DomainScope at Scrape the World](https://domainscope.scrapetheworld.org)** · *Licensed under MIT*.
