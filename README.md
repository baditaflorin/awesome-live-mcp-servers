# Awesome Live MCP Servers 🌐⚡

> **The definitive, live-benchmarked directory of public & remote Model Context Protocol (MCP) servers and streamable AI manifests on the internet.**
>
> Concurrently probed, latency-benchmarked, and enriched by **[DomainScope at Scrape the World](https://domainscope.scrapetheworld.org)**.

[![Total Servers](https://img.shields.io/badge/MCP_Servers-3442-purple?style=for-the-badge&logo=anthropic)](data/mcp-servers.json)
[![Live Reachable](https://img.shields.io/badge/Live_Reachable-3378%20Online-emerald?style=for-the-badge)](data/mcp-servers.json)
[![Scanned Corpus](https://img.shields.io/badge/Scanned_Corpus-1.6M+_Domains-blue?style=for-the-badge)](https://domainscope.scrapetheworld.org/mcp-directory)
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
1. **1.2M+ Domains Probed**: Ingests high-priority cohorts (developer documentation platforms, open-source repositories, API surfaces, AI ecosystem domains) from DomainScope's 13M+ domain graph.
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
| **💼 Enterprise SaaS & B2B Solutions** | 🟢 **1872** | **1910** | Enterprise cloud services, workflow software, corporate knowledge, and B2B platforms. | [**Browse All (1910) ↗**](directory/enterprise-saas.md) |
| **🛠️ Developer Platforms, DevOps & Web3** | 🟢 **767** | **779** | Developer tooling, APIs, CI/CD, cloud orchestration, web3, and IDE integrations. | [**Browse All (779) ↗**](directory/developer-platforms.md) |
| **🛒 E-Commerce & Commercial Services** | 🟢 **274** | **283** | Online storefronts, retail catalogs, merchant operations, and commerce tools. | [**Browse All (283) ↗**](directory/ecommerce.md) |
| **🤖 Autonomous Agents & Workflow Automation** | 🟢 **222** | **223** | AI agent swarms, automated assistants, reasoning runtimes, and autonomous pipelines. | [**Browse All (223) ↗**](directory/autonomous-agents.md) |
| **📊 Enterprise Intelligence & Analytics** | 🟢 **92** | **95** | Data pipelines, market intelligence, telemetry monitoring, BI, and metrics. | [**Browse All (95) ↗**](directory/analytics.md) |
| **🌐 Web Search, Crawling & Data Extraction** | 🟢 **93** | **93** | Web scrapers, search indices, document parsing, content extraction, and search tools. | [**Browse All (93) ↗**](directory/web-search-crawling.md) |
| **🔒 Cybersecurity & Infrastructure** | 🟢 **49** | **50** | Auth, threat detection, secret management, identity verification, TLS, and audit. | [**Browse All (50) ↗**](directory/cybersecurity.md) |
| **🧠 AI Foundations & Model Inference** | 🟢 **9** | **9** | Model serving endpoints, foundation labs, LLM hosting providers, and inference runtimes. | [**Browse All (9) ↗**](directory/ai-foundations.md) |

---

## 🌟 Featured Multi-Tool & High-Capacity Servers (100 Highlighted)

> Live remote servers offering verified multi-tool suites (`tools_count > 0`) or community-submitted Streamable HTTP endpoints.
>
> 💡 **Explore the complete registry**: Click into any vertical category table above, or query the full datasets in [`data/mcp-servers.json`](data/mcp-servers.json) and [`data/mcp-servers.csv`](data/mcp-servers.csv).

| Server / Host | Category | Business Model | Status | Latency | Tools | Manifest | DomainScope Dossier |
|---|---|---|:---:|:---:|:---:|:---:|:---:|
| **[outo.dev](https://outo.dev)**<br>*furnace* | 🛠️ Developer Platforms, DevOps & Web3 | `Open Source` | 🟢 **Live** | 165 ms | **475 tools** | [Manifest ↗](https://outo.dev/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/outo.dev) |
| **[zop.dev](https://zop.dev)**<br>*dev.zop/zopnight* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 730 ms | **324 tools** | [Manifest ↗](https://zop.dev/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/zop.dev) |
| **[metavert.io](https://metavert.io)**<br>*metavert.io* | 💼 Enterprise SaaS & B2B Solutions | `Consulting Services` | 🟢 **Live** | 258 ms | **121 tools** | [Manifest ↗](https://metavert.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/metavert.io) |
| **[socialpro.ai](https://socialpro.ai)**<br>*com.youspot/youspot* | 💼 Enterprise SaaS & B2B Solutions | `SaaS subscription` | 🟢 **Live** | 102 ms | **111 tools** | [Manifest ↗](https://socialpro.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/socialpro.ai) |
| **[domainsuggest.ai](https://domainsuggest.ai)**<br>*com.youspot/youspot* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 398 ms | **111 tools** | [Manifest ↗](https://domainsuggest.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/domainsuggest.ai) |
| **[domainsales.ai](https://domainsales.ai)**<br>*com.youspot/youspot* | 💼 Enterprise SaaS & B2B Solutions | `E-commerce` | 🟢 **Live** | 406 ms | **111 tools** | [Manifest ↗](https://domainsales.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/domainsales.ai) |
| **[companyresearch.ai](https://companyresearch.ai)**<br>*com.youspot/youspot* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Live** | 641 ms | **111 tools** | [Manifest ↗](https://companyresearch.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/companyresearch.ai) |
| **[emem.dev](https://emem.dev)**<br>*emem* | 🤖 Autonomous Agents & Workflow Automation | `Open Source` | 🟢 **Live** | 717 ms | **110 tools** | [Manifest ↗](https://emem.dev/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/emem.dev) |
| **[brainstorm-labs.com](https://brainstorm-labs.com)**<br>*brainstorm-labs.com* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 267 ms | **106 tools** | [Manifest ↗](https://brainstorm-labs.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/brainstorm-labs.com) |
| **[moneymatter.app](https://moneymatter.app)**<br>*moneymatter.app* | 💼 Enterprise SaaS & B2B Solutions | `Open-source/Freeware` | 🟢 **Live** | 154 ms | **103 tools** | [Manifest ↗](https://moneymatter.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/moneymatter.app) |
| **[dchub.cloud](https://dchub.cloud)**<br>*DC Hub MCP Server* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Live** | 535 ms | **92 tools** | [Manifest ↗](https://dchub.cloud/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/dchub.cloud) |
| **[colombiamove.com](https://colombiamove.com)**<br>*com.colombiamove/marketplace* | 🤖 Autonomous Agents & Workflow Automation | `Advertising (free listings with optional premium features)` | 🟢 **Live** | 673 ms | **80 tools** | [Manifest ↗](https://colombiamove.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/colombiamove.com) |
| **[stickyhive.ai](https://stickyhive.ai)**<br>*stickyhive* | 💼 Enterprise SaaS & B2B Solutions | `SaaS subscription` | 🟢 **Live** | 455 ms | **72 tools** | [Manifest ↗](https://stickyhive.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/stickyhive.ai) |
| **[getfast.ai](https://getfast.ai)**<br>*fit.kailo/kailo* | 🔒 Cybersecurity & Infrastructure | `SaaS subscription` | 🟢 **Live** | 287 ms | **62 tools** | [Manifest ↗](https://getfast.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/getfast.ai) |
| **[minddy.app](https://minddy.app)**<br>*minddy* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 403 ms | **58 tools** | [Manifest ↗](https://minddy.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/minddy.app) |
| **[aave.com](https://aave.com)**<br>*com.aave/mcp* | 💼 Enterprise SaaS & B2B Solutions | `Open-source software development, decentralized finance platform` | 🟢 **Live** | 173 ms | **53 tools** | [Manifest ↗](https://aave.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aave.com) |
| **[aave.org](https://aave.org)**<br>*com.aave/mcp* | 💼 Enterprise SaaS & B2B Solutions | `Open-source protocol with decentralized governance` | 🟢 **Live** | 268 ms | **53 tools** | [Manifest ↗](https://aave.org/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aave.org) |
| **[pydantic.dev](https://pydantic.dev)**<br>*Pydantic Logfire MCP Server* | 🛠️ Developer Platforms, DevOps & Web3 | `Open Source` | 🟢 **Live** | 106 ms | **51 tools** | [Manifest ↗](https://pydantic.dev/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/pydantic.dev) |
| **[grep.ai](https://grep.ai)**<br>*grep-public-api-v2* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 500 ms | **50 tools** | [Manifest ↗](https://grep.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/grep.ai) |
| **[snowsure.ai](https://snowsure.ai)**<br>*snowsure-live* | 🔒 Cybersecurity & Infrastructure | `SaaS subscription` | 🟢 **Live** | 503 ms | **48 tools** | [Manifest ↗](https://snowsure.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/snowsure.ai) |
| **[builtwith.com](https://builtwith.com)**<br>*BuiltWith MCP* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription with free individual site lookups` | 🟢 **Live** | 1175 ms | **48 tools** | [Manifest ↗](https://builtwith.com/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/builtwith.com) |
| **[commoditynode.com](https://commoditynode.com)**<br>*worldmonitor* | 🌐 Web Search, Crawling & Data Extraction | `Subscription-based Research and API Access` | 🟢 **Live** | 182 ms | **46 tools** | [Manifest ↗](https://commoditynode.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/commoditynode.com) |
| **[rstream.io](https://rstream.io)**<br>*io.rstream/mcp* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 219 ms | **46 tools** | [Manifest ↗](https://rstream.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/rstream.io) |
| **[outlit.ai](https://outlit.ai)**<br>*Outlit* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 1009 ms | **46 tools** | [Manifest ↗](https://outlit.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/outlit.ai) |
| **[restivity.app](https://restivity.app)**<br>*Restivity* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 373 ms | **45 tools** | [Manifest ↗](https://restivity.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/restivity.app) |
| **[vaaya.ai](https://vaaya.ai)**<br>*Vaaya* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Live** | 221 ms | **44 tools** | [Manifest ↗](https://vaaya.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/vaaya.ai) |
| **[xpoz.ai](https://xpoz.ai)**<br>*io.github.XPOZpublic/xpoz-mcp* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 286 ms | **44 tools** | [Manifest ↗](https://xpoz.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/xpoz.ai) |
| **[last9.io](https://last9.io)**<br>*last9* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 171 ms | **43 tools** | [Manifest ↗](https://last9.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/last9.io) |
| **[signalkit.ai](https://signalkit.ai)**<br>*signalkit* | 🧠 AI Foundations & Model Inference | `SaaS subscription` | 🟢 **Live** | 174 ms | **43 tools** | [Manifest ↗](https://signalkit.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/signalkit.ai) |
| **[anomalyarmor.ai](https://anomalyarmor.ai)**<br>*AnomalyArmor* | 📊 Enterprise Intelligence & Analytics | `SaaS subscription` | 🟢 **Live** | 698 ms | **43 tools** | [Manifest ↗](https://anomalyarmor.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/anomalyarmor.ai) |
| **[rxresu.me](https://rxresu.me)**<br>*rxresu.me* | 🛠️ Developer Platforms, DevOps & Web3 | `Open Source` | 🟢 **Live** | 140 ms | **42 tools** | [Manifest ↗](https://rxresu.me/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/rxresu.me) |
| **[happyscribe.com](https://happyscribe.com)**<br>*happyscribe.com* | 💼 Enterprise SaaS & B2B Solutions | `SaaS subscription` | 🟢 **Live** | 399 ms | **42 tools** | [Manifest ↗](https://happyscribe.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/happyscribe.com) |
| **[stack0.dev](https://stack0.dev)**<br>*stack0.dev* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 955 ms | **41 tools** | [Manifest ↗](https://stack0.dev/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/stack0.dev) |
| **[clueso.io](https://clueso.io)**<br>*clueso* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 277 ms | **40 tools** | [Manifest ↗](https://clueso.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/clueso.io) |
| **[juicer.io](https://juicer.io)**<br>*juicer.io* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 652 ms | **33 tools** | [Manifest ↗](https://juicer.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/juicer.io) |
| **[atlasly.app](https://atlasly.app)**<br>*atlasly.app* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 121 ms | **32 tools** | [Manifest ↗](https://atlasly.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/atlasly.app) |
| **[ola.cv](https://ola.cv)**<br>*OlaCV* | 💼 Enterprise SaaS & B2B Solutions | `Domain Name Sales and Registrations` | 🟢 **Live** | 503 ms | **32 tools** | [Manifest ↗](https://ola.cv/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ola.cv) |
| **[echowave.io](https://echowave.io)**<br>*echowave* | 🛠️ Developer Platforms, DevOps & Web3 | `Freemium` | 🟢 **Live** | 168 ms | **31 tools** | [Manifest ↗](https://echowave.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/echowave.io) |
| **[prisma.sh](https://prisma.sh)**<br>*Prisma MCP* | 🛠️ Developer Platforms, DevOps & Web3 | `Open-source and sponsorships` | 🟢 **Live** | 347 ms | **31 tools** | [Manifest ↗](https://prisma.sh/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/prisma.sh) |
| **[prisma.io](https://prisma.io)**<br>*Prisma MCP* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 356 ms | **31 tools** | [Manifest ↗](https://prisma.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/prisma.io) |
| **[mymx.dev](https://mymx.dev)**<br>*primitive* | 🧠 AI Foundations & Model Inference | `SaaS subscription` | 🟢 **Live** | 408 ms | **30 tools** | [Manifest ↗](https://mymx.dev/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/mymx.dev) |
| **[contextrepo.com](https://contextrepo.com)**<br>*Context Repo MCP Server* | 🧠 AI Foundations & Model Inference | `SaaS subscription` | 🟢 **Live** | 214 ms | **29 tools** | [Manifest ↗](https://contextrepo.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/contextrepo.com) |
| **[ezugc.ai](https://ezugc.ai)**<br>*ai.ezugc/mcp* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 564 ms | **29 tools** | [Manifest ↗](https://ezugc.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ezugc.ai) |
| **[perigon.io](https://perigon.io)**<br>*io.perigon/mcp* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 173 ms | **28 tools** | [Manifest ↗](https://perigon.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/perigon.io) |
| **[robauto.ai](https://robauto.ai)**<br>*robauto.ai* | 💼 Enterprise SaaS & B2B Solutions | `Services` | 🟢 **Live** | 254 ms | **28 tools** | [Manifest ↗](https://robauto.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/robauto.ai) |
| **[mcpanalytics.ai](https://mcpanalytics.ai)**<br>*mcpanalytics.ai* | 📊 Enterprise Intelligence & Analytics | `SaaS subscription` | 🟢 **Live** | 787 ms | **28 tools** | [Manifest ↗](https://mcpanalytics.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/mcpanalytics.ai) |
| **[gtm.ai](https://gtm.ai)**<br>*gtm.ai* | 💼 Enterprise SaaS & B2B Solutions | `SaaS subscription` | 🟢 **Live** | 99 ms | **26 tools** | [Manifest ↗](https://gtm.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/gtm.ai) |
| **[momentic.ai](https://momentic.ai)**<br>*ai.momentic/mcp* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 166 ms | **26 tools** | [Manifest ↗](https://momentic.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/momentic.ai) |
| **[screenwriter.dev](https://screenwriter.dev)**<br>*ai.momentic/mcp* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 339 ms | **26 tools** | [Manifest ↗](https://screenwriter.dev/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/screenwriter.dev) |
| **[kleap.co](https://kleap.co)**<br>*Kleap* • [Repo ↗](https://github.com/kleaphq/cli) | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 509 ms | **26 tools** | [Manifest ↗](https://kleap.co/api/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/kleap.co) |
| **[startuphub.ai](https://startuphub.ai)**<br>*startuphub.ai* | 💼 Enterprise SaaS & B2B Solutions | `Advertising & Sponsored Content` | 🟢 **Live** | 186 ms | **25 tools** | [Manifest ↗](https://startuphub.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/startuphub.ai) |
| **[rezome.ai](https://rezome.ai)**<br>*rezome-mcp* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 115 ms | **24 tools** | [Manifest ↗](https://rezome.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/rezome.ai) |
| **[fly.io](https://fly.io)**<br>*sprites* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 165 ms | **24 tools** | [Manifest ↗](https://fly.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/fly.io) |
| **[endorphinsrunning.com](https://endorphinsrunning.com)**<br>*endorphinsrunning.com* | 💼 Enterprise SaaS & B2B Solutions | `Memberships, Apparel Sales` | 🟢 **Live** | 483 ms | **24 tools** | [Manifest ↗](https://endorphinsrunning.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/endorphinsrunning.com) |
| **[webflow.com](https://webflow.com)**<br>*webflow.com* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 639 ms | **24 tools** | [Manifest ↗](https://webflow.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/webflow.com) |
| **[day-off.app](https://day-off.app)**<br>*day-off.app* | 💼 Enterprise SaaS & B2B Solutions | `SaaS subscription` | 🟢 **Live** | 92 ms | **23 tools** | [Manifest ↗](https://day-off.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/day-off.app) |
| **[getminds.ai](https://getminds.ai)**<br>*getminds.ai* | 💼 Enterprise SaaS & B2B Solutions | `Services` | 🟢 **Live** | 172 ms | **23 tools** | [Manifest ↗](https://getminds.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/getminds.ai) |
| **[supersaas.jp](https://supersaas.jp)**<br>*supersaas.jp* | 💼 Enterprise SaaS & B2B Solutions | `SaaS subscription` | 🟢 **Live** | 286 ms | **23 tools** | [Manifest ↗](https://supersaas.jp/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/supersaas.jp) |
| **[art-of-x.com](https://art-of-x.com)**<br>*art-of-x.com* | 💼 Enterprise SaaS & B2B Solutions | `SaaS subscription` | 🟢 **Live** | 503 ms | **23 tools** | [Manifest ↗](https://art-of-x.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/art-of-x.com) |
| **[openrouter.ai](https://openrouter.ai)**<br>*ai.openrouter/mcp* | 🧠 AI Foundations & Model Inference | `API Access Subscription` | 🟢 **Live** | 344 ms | **22 tools** | [Manifest ↗](https://openrouter.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/openrouter.ai) |
| **[dynamicsinfo.com](https://dynamicsinfo.com)**<br>*ai.openrouter/mcp* | 🧠 AI Foundations & Model Inference | `SaaS subscription` | 🟢 **Live** | 424 ms | **22 tools** | [Manifest ↗](https://dynamicsinfo.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/dynamicsinfo.com) |
| **[bsdxr.com](https://bsdxr.com)**<br>*bsdxr.com* | 💼 Enterprise SaaS & B2B Solutions | `Service-based (custom development, equipment sales, and rentals)` | 🟢 **Live** | 123 ms | **21 tools** | [Manifest ↗](https://bsdxr.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/bsdxr.com) |
| **[os-1.ai](https://os-1.ai)**<br>*mitosis* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 322 ms | **20 tools** | [Manifest ↗](https://os-1.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/os-1.ai) |
| **[kaito.ai](https://kaito.ai)**<br>*Kaito* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 474 ms | **20 tools** | [Manifest ↗](https://kaito.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/kaito.ai) |
| **[bargainbooks.co.za](https://bargainbooks.co.za)**<br>*bargainbooks.co.za* | 🛒 E-Commerce & Commercial Services | `Discount Retail` | 🟢 **Live** | 209 ms | **19 tools** | [Manifest ↗](https://bargainbooks.co.za/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/bargainbooks.co.za) |
| **[mallary.ai](https://mallary.ai)**<br>*ai.mallary/mallary* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 209 ms | **19 tools** | [Manifest ↗](https://mallary.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/mallary.ai) |
| **[quicknode.com](https://quicknode.com)**<br>*Quicknode MCP Server* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 241 ms | **19 tools** | [Manifest ↗](https://quicknode.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/quicknode.com) |
| **[theautomators.ai](https://theautomators.ai)**<br>*ai.theautomators/mcp* | 🛠️ Developer Platforms, DevOps & Web3 | `Services` | 🟢 **Live** | 197 ms | **18 tools** | [Manifest ↗](https://theautomators.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/theautomators.ai) |
| **[meritex.ai](https://meritex.ai)**<br>*meritex.ai* | 💼 Enterprise SaaS & B2B Solutions | `SaaS subscription` | 🟢 **Live** | 234 ms | **18 tools** | [Manifest ↗](https://meritex.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/meritex.ai) |
| **[peetchr.ai](https://peetchr.ai)**<br>*Peetchr* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 348 ms | **18 tools** | [Manifest ↗](https://peetchr.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/peetchr.ai) |
| **[infrasure.ai](https://infrasure.ai)**<br>*infrasure* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 384 ms | **18 tools** | [Manifest ↗](https://infrasure.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/infrasure.ai) |
| **[talentprism.ai](https://talentprism.ai)**<br>*TalentPrism Agent Capabilities* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 610 ms | **18 tools** | [Manifest ↗](https://talentprism.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/talentprism.ai) |
| **[tryconvert.ai](https://tryconvert.ai)**<br>*tryconvert.ai* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Live** | 806 ms | **18 tools** | [Manifest ↗](https://tryconvert.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/tryconvert.ai) |
| **[raster.app](https://raster.app)**<br>*raster.app* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 198 ms | **17 tools** | [Manifest ↗](https://raster.app/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/raster.app) |
| **[sitegpt.ai](https://sitegpt.ai)**<br>*SiteGPT MCP Server* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 235 ms | **17 tools** | [Manifest ↗](https://sitegpt.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/sitegpt.ai) |
| **[a1.gallery](https://a1.gallery)**<br>*a1.gallery* | 💼 Enterprise SaaS & B2B Solutions | `Advertising` | 🟢 **Live** | 265 ms | **17 tools** | [Manifest ↗](https://a1.gallery/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/a1.gallery) |
| **[bopen.ai](https://bopen.ai)**<br>*bopen.ai* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 200 ms | **16 tools** | [Manifest ↗](https://bopen.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/bopen.ai) |
| **[supersonik.ai](https://supersonik.ai)**<br>*supersonik* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 258 ms | **16 tools** | [Manifest ↗](https://supersonik.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/supersonik.ai) |
| **[whisperchat.ai](https://whisperchat.ai)**<br>*WhisperChat MCP Server* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 319 ms | **16 tools** | [Manifest ↗](https://whisperchat.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/whisperchat.ai) |
| **[opengrants.io](https://opengrants.io)**<br>*opengrants.io* | 💼 Enterprise SaaS & B2B Solutions | `Subscription-based SaaS` | 🟢 **Live** | 111 ms | **15 tools** | [Manifest ↗](https://opengrants.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/opengrants.io) |
| **[spaitial.ai](https://spaitial.ai)**<br>*spaitial.ai* | 💼 Enterprise SaaS & B2B Solutions | `SaaS subscription` | 🟢 **Live** | 198 ms | **15 tools** | [Manifest ↗](https://spaitial.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/spaitial.ai) |
| **[convertfleet.com](https://convertfleet.com)**<br>*convertfleet* | 🛠️ Developer Platforms, DevOps & Web3 | `Freemium with subscription and one-time credit packs (SaaS-based)` | 🟢 **Live** | 421 ms | **15 tools** | [Manifest ↗](https://convertfleet.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/convertfleet.com) |
| **[dynamicbusiness.com.au](https://dynamicbusiness.com.au)**<br>*dynamicbusiness.com.au* | 💼 Enterprise SaaS & B2B Solutions | `Print Subscription, Advertising` | 🟢 **Live** | 553 ms | **15 tools** | [Manifest ↗](https://dynamicbusiness.com.au/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/dynamicbusiness.com.au) |
| **[vokality.ai](https://vokality.ai)**<br>*vokality.ai* | 🔒 Cybersecurity & Infrastructure | `SaaS subscription` | 🟢 **Live** | 656 ms | **15 tools** | [Manifest ↗](https://vokality.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/vokality.ai) |
| **[caspio.com](https://caspio.com)**<br>*caspio.com* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 973 ms | **15 tools** | [Manifest ↗](https://caspio.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/caspio.com) |
| **[zadig-et-voltaire.com](https://zadig-et-voltaire.com)**<br>*zadig-et-voltaire-commerce* | 🛒 E-Commerce & Commercial Services | `E-commerce` | 🟢 **Live** | 173 ms | **14 tools** | [Manifest ↗](https://zadig-et-voltaire.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/zadig-et-voltaire.com) |
| **[aio-mcp.com](https://aio-mcp.com)**<br>*aio-mcp.com* | 🛒 E-Commerce & Commercial Services | `Licensing` | 🟢 **Live** | 233 ms | **14 tools** | [Manifest ↗](https://aio-mcp.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/aio-mcp.com) |
| **[wavect.io](https://wavect.io)**<br>*wavect.io* | 🛠️ Developer Platforms, DevOps & Web3 | `Project-based and subscription-based services` | 🟢 **Live** | 250 ms | **14 tools** | [Manifest ↗](https://wavect.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/wavect.io) |
| **[ricord.ai](https://ricord.ai)**<br>*Ricord* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 297 ms | **14 tools** | [Manifest ↗](https://ricord.ai/.well-known/mcp) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ricord.ai) |
| **[usesuperflow.com](https://usesuperflow.com)**<br>*superflow-free-tools* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 361 ms | **14 tools** | [Manifest ↗](https://usesuperflow.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/usesuperflow.com) |
| **[explorium.ai](https://explorium.ai)**<br>*explorium* | 🌐 Web Search, Crawling & Data Extraction | `SaaS subscription` | 🟢 **Live** | 1021 ms | **14 tools** | [Manifest ↗](https://explorium.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/explorium.ai) |
| **[fin.ai](https://fin.ai)**<br>*fin.ai* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 168 ms | **13 tools** | [Manifest ↗](https://fin.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/fin.ai) |
| **[intercom.io](https://intercom.io)**<br>*intercom.io* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 268 ms | **13 tools** | [Manifest ↗](https://intercom.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/intercom.io) |
| **[intercomcdn.com](https://intercomcdn.com)**<br>*intercomcdn.com* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 293 ms | **13 tools** | [Manifest ↗](https://intercomcdn.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/intercomcdn.com) |
| **[intercom.com](https://intercom.com)**<br>*intercom.com* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 311 ms | **13 tools** | [Manifest ↗](https://intercom.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/intercom.com) |
| **[ora.ai](https://ora.ai)**<br>*ora* | 🤖 Autonomous Agents & Workflow Automation | `SaaS subscription` | 🟢 **Live** | 467 ms | **13 tools** | [Manifest ↗](https://ora.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/ora.ai) |
| **[brainerce.com](https://brainerce.com)**<br>*brainerce* | 🛠️ Developer Platforms, DevOps & Web3 | `SaaS subscription` | 🟢 **Live** | 133 ms | **12 tools** | [Manifest ↗](https://brainerce.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/brainerce.com) |
| **[shiken.ai](https://shiken.ai)**<br>*ai.shiken/shiken* | 🔒 Cybersecurity & Infrastructure | `SaaS subscription` | 🟢 **Live** | 187 ms | **12 tools** | [Manifest ↗](https://shiken.ai/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/shiken.ai) |
| **[hackshackers.com](https://hackshackers.com)**<br>*Hacks/Hackers* | 🔒 Cybersecurity & Infrastructure | `Grant-funded` | 🟢 **Live** | 209 ms | **12 tools** | [Manifest ↗](https://hackshackers.com/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/hackshackers.com) |
| **[firstsales.io](https://firstsales.io)**<br>*firstsales* | 📊 Enterprise Intelligence & Analytics | `SaaS subscription` | 🟢 **Live** | 248 ms | **12 tools** | [Manifest ↗](https://firstsales.io/.well-known/mcp/server-card.json) | [Dossier ↗](https://domainscope.scrapetheworld.org/domains/firstsales.io) |

---

## 🏢 Distribution by Business Delivery Model

Classified by DomainScope's firmographic model inference:

- **SaaS subscription**: **990 servers**
- **Advertising**: **183 servers**
- **E-commerce**: **152 servers**
- **Unknown**: **121 servers**
- **Subscription-based**: **60 servers**
- **Open Source**: **46 servers**
- **Consulting Services**: **36 servers**
- **B2B SaaS**: **36 servers**
- **Non-profit**: **31 servers**
- **Subscription**: **19 servers**
- **Freemium**: **19 servers**
- **Transaction fees**: **19 servers**
- **SaaS_subscription**: **18 servers**
- **Freemium (with in-app purchases)**: **17 servers**
- **Project-based**: **17 servers**
- **Commission-based**: **17 servers**
- **Pay-to-Play**: **16 servers**
- **Service-based**: **16 servers**
- **Gambling Revenue**: **15 servers**
- **Services**: **14 servers**
- **Project-based services**: **13 servers**
- **Domain Sales**: **13 servers**
- **Ticket Sales**: **11 servers**
- **B2B Sales**: **11 servers**
- **Paid Services**: **11 servers**
- **Advertising and Affiliate Marketing**: **10 servers**
- **Public Funding**: **10 servers**
- **Gaming Revenue**: **10 servers**
- **Personal Blog**: **9 servers**
- **Donation-based**: **9 servers**
- **Project-based Consulting**: **9 servers**
- **Investment Opportunities**: **9 servers**
- **Project-based consulting**: **8 servers**
- **Professional Services**: **8 servers**
- **B2B**: **8 servers**
- **Project-based fees**: **7 servers**
- **Open-source**: **7 servers**
- **Commission-based marketplace**: **7 servers**
- **Donations and grants**: **6 servers**
- **Project-based Services**: **6 servers**
- **Domain Acquisition**: **6 servers**
- **B2B Services**: **6 servers**
- **Commission-based sales**: **6 servers**
- **Subscription-based SaaS**: **6 servers**
- **Subscription-based with free registration**: **6 servers**
- **Government-funded**: **6 servers**
- **Freemium Subscription**: **6 servers**
- **Retail Sales**: **5 servers**
- **Advertising, Affiliate Marketing**: **5 servers**
- **Medical Services**: **5 servers**
- **Subscription-based (premium content)**: **5 servers**
- **Service Fee**: **5 servers**
- **Project-based consulting and services**: **5 servers**
- **Donations and contributions**: **5 servers**
- **Public Service**: **5 servers**
- **Freelance Services**: **5 servers**
- **Project-based and retainer services**: **5 servers**
- **Venture Capital**: **5 servers**
- **Software Licensing**: **4 servers**
- **Freemium (with optional premium features)**: **4 servers**
- **Tuition Fees**: **4 servers**
- **Membership fees**: **4 servers**
- **Tour Package Sales**: **4 servers**
- **Project-based services and consulting fees**: **4 servers**
- **Book Sales**: **4 servers**
- **Subscription-based services**: **4 servers**
- **Rental Income**: **4 servers**
- **Tuition-based**: **4 servers**
- **Recruitment Services**: **4 servers**
- **Advertising, Subscription**: **4 servers**
- **Freelance/Contract Work**: **4 servers**
- **Freemium with Premium Subscription**: **4 servers**
- **Free to Use**: **4 servers**
- **Software as a Service (SaaS)**: **4 servers**
- **Project-based and Retainer Models**: **4 servers**
- **Government Funded**: **3 servers**
- **Freelance/Independent**: **3 servers**
- **Rental Services**: **3 servers**
- **Lead Generation**: **3 servers**
- **Event-based**: **3 servers**
- **Software as a Service (SaaS) subscription**: **3 servers**
- **Commission-based Trading**: **3 servers**
- **Freemium (free with optional premium features)**: **3 servers**
- **Lead Generation and Subscription Services**: **3 servers**
- **Managed Services**: **3 servers**
- **Project-based_service_fees**: **3 servers**
- **Investment Portfolio**: **3 servers**
- **unknown**: **3 servers**
- **B2B and B2C Sales**: **3 servers**
- **Domain Registration Fees**: **3 servers**
- **asset_sale**: **3 servers**
- **Affiliate Marketing**: **3 servers**
- **Domain Sales and Services**: **3 servers**
- **Freemium with premium subscriptions**: **3 servers**
- **Potential Investment Opportunity**: **3 servers**
- **Gaming Revenue Share**: **3 servers**
- **asset_sale_or_investment**: **3 servers**
- **Custom Software Development**: **3 servers**
- **Advertising and Sponsorships**: **3 servers**
- **Subscription-based with free trials**: **3 servers**
- **Private Practice**: **3 servers**
- **Cryptocurrency Exchange Fees**: **3 servers**
- **Donations/Contributions**: **3 servers**
- **Personal Branding**: **3 servers**
- **Software Sales**: **3 servers**
- **Service-based subscription**: **3 servers**
- **Freemium subscription with premium features**: **3 servers**
- **Not specified**: **3 servers**
- **Project-based and retainer fees**: **3 servers**
- **E-commerce sales**: **3 servers**
- **Custom Software Development Services**: **3 servers**
- **Investment and Partnership Opportunities**: **3 servers**
- **E-commerce (direct-to-consumer sales)**: **3 servers**
- **E-commerce platform fee**: **3 servers**
- **Token-based Economy**: **3 servers**
- **Token-based platform**: **3 servers**
- **Open-source, community-driven**: **3 servers**
- **B2C Sales**: **2 servers**
- **Non-profit funding**: **2 servers**
- **Event Organizing**: **2 servers**
- **Open Source Software**: **2 servers**
- **Pay-per-service**: **2 servers**
- **B2B service**: **2 servers**
- **Job Board**: **2 servers**
- **Project-based services and retainer contracts**: **2 servers**
- **Transaction Fees**: **2 servers**
- **Project-based and subscription-based services**: **2 servers**
- **Tax-funded**: **2 servers**
- **Domain Sales/Investment**: **2 servers**
- **Property listings/brokerage or lead generation**: **2 servers**
- **Service Platform**: **2 servers**
- **Professional Services (Project-Based Fees)**: **2 servers**
- **Project-based consulting and retainer services**: **2 servers**
- **domain_sale_or_lease**: **2 servers**
- **Transaction fees (domain sales/transfers)**: **2 servers**
- **Service-based (B2B)**: **2 servers**
- **SaaS subscription (Software as a Service)**: **2 servers**
- **Service Subscription**: **2 servers**
- **Advertising_and_sponsored_content**: **2 servers**
- **Freight and Logistics Services**: **2 servers**
- **Government Funding**: **2 servers**
- **Interest on Loans and Fees for Services**: **2 servers**
- **Gaming Revenue (e.g., entry fees, bets)**: **2 servers**
- **Freemium (with potential premium features)**: **2 servers**
- **Advertising and Premium Services**: **2 servers**
- **Service**: **2 servers**
- **Consultation Fees**: **2 servers**
- **Subscription and Lead Generation**: **2 servers**
- **Freemium (Free with premium features)**: **2 servers**
- **Subscription-based with additional paid features**: **2 servers**
- **Donations and sponsorships**: **2 servers**
- **Interest-based lending**: **2 servers**
- **Interest on deposits and fees for services**: **2 servers**
- **Membership fees, event sponsorships**: **2 servers**
- **Insurance Premiums**: **2 servers**
- **Marketplace**: **2 servers**
- **Potentially advertising-based or subscription-based**: **2 servers**
- **Donations and offerings**: **2 servers**
- **Commission-based bookings**: **2 servers**
- **Advertising (if any)**: **2 servers**
- **Not applicable**: **2 servers**
- **Coaching Services**: **2 servers**
- **Volunteer-driven**: **2 servers**
- **Advertising, Listing Fees**: **2 servers**
- **SaaS subscription with free and paid plans**: **2 servers**
- **Premium Subscription**: **2 servers**
- **Subscription-based with free trial available**: **2 servers**
- **Subscription-based service**: **2 servers**
- **Donations and membership fees**: **2 servers**
- **Non-commercial**: **2 servers**
- **Freemium (with premium features)**: **2 servers**
- **Freemium with paid subscriptions**: **2 servers**
- **Marketing Services**: **2 servers**
- **Asset Management Fees**: **2 servers**
- **B2B SaaS subscription**: **2 servers**
- **Retail sales of pharmaceuticals**: **2 servers**
- **Freemium (free with optional paid features)**: **2 servers**
- **Grant-funded**: **2 servers**
- **Research and Development**: **2 servers**
- **Transaction Fees, Premium Services**: **2 servers**
- **Non-profit (No revenue generation)**: **2 servers**
- **Wholesale**: **2 servers**
- **SaaS subscription (with free tier)**: **2 servers**
- **Donations and community support**: **2 servers**
- **E-commerce (direct sales)**: **2 servers**
- **E-commerce with physical stores**: **2 servers**
- **Custom Projects**: **2 servers**
- **Unknown (likely not monetized)**: **2 servers**
- **Token Economy**: **2 servers**
- **API Usage**: **2 servers**
- **Open Source (No direct revenue)**: **2 servers**
- **SaaS subscription (pay-per-use)**: **2 servers**
- **AI Services & Solutions**: **1 servers**
- **Email subscription**: **1 servers**
- **Job listing fees (likely paid by employers) and potentially premium services for job seekers**: **1 servers**
- **Content-based (educational/research-focused, likely supported by donations, grants, or minimal advertising)**: **1 servers**
- **Information_Dissemination_and_Education**: **1 servers**
- **Professional Services (Consulting)**: **1 servers**
- **Subscription-based market research reports and custom consulting services**: **1 servers**
- **Job Board Advertising**: **1 servers**
- **Domain registration and management services**: **1 servers**
- **Freemium with Subscription**: **1 servers**
- **Subscription-based Platform**: **1 servers**
- **Subscription-based Research and API Access**: **1 servers**
- **Funded by European Union research projects**: **1 servers**
- **Research Grants and Projects**: **1 servers**
- **Marketplace with both free and paid resources**: **1 servers**
- **Commission-based ( earns money by redirecting users to airline websites)**: **1 servers**
- **Non-profit/Volunteer-driven**: **1 servers**
- **Directory Listing Service**: **1 servers**
- **Subscription-based with free delivery and discounts**: **1 servers**
- **Grant funding**: **1 servers**
- **Domain Name Registration Fees**: **1 servers**
- **Market Research Services**: **1 servers**
- **Subscription-based with additional fees for non-member deliveries**: **1 servers**
- **Subscription-based with optional premium service (Knuspr Xtra)**: **1 servers**
- **Research Services & Membership Packages**: **1 servers**
- **Freemium (with optional paid subscription)**: **1 servers**
- **Freeware with potential premium features**: **1 servers**
- **Marketplace, Brokerage**: **1 servers**
- **Rewards-based survey platform**: **1 servers**
- **E-commerce Subscription + Delivery Fees**: **1 servers**
- **Subscription-based access to cybersecurity tools**: **1 servers**
- **Free, Non-Profit**: **1 servers**
- **Donations, grants, and tuition fees**: **1 servers**
- **Subscription-based and Pay-per-view**: **1 servers**
- **Service-based (contracting, labor, materials) with potential insurance billing and financing options**: **1 servers**
- **Hosting services, domain registration, and online service subscriptions**: **1 servers**
- **Grants, donations, partnerships, and community-driven fundraising**: **1 servers**
- **Subscription-based and Pay-per-minute**: **1 servers**
- **Subscription-based Dating Service**: **1 servers**
- **Service-based (consulting, calibration, training, equipment sales)**: **1 servers**
- **Content monetization (ads, affiliate marketing, sponsorships, or premium content)**: **1 servers**
- **Professional Services (consulting fees, retainers, and project-based engagements)**: **1 servers**
- **Betting**: **1 servers**
- **Job Board Listing Fees**: **1 servers**
- **Subscription-based with pay-per-minute shows**: **1 servers**
- **domain_resale**: **1 servers**
- **Betting Commission**: **1 servers**
- **transaction_fees_and_domain_sale**: **1 servers**
- **Domain sales/auction**: **1 servers**
- **Rental and Sales**: **1 servers**
- **Event Organization**: **1 servers**
- **Freight Brokerage**: **1 servers**
- **Non-profit Organization**: **1 servers**
- **Accommodation and Services**: **1 servers**
- **Tuition fees and partnerships**: **1 servers**
- **Accommodation and Activity Bookings**: **1 servers**
- **Event-based catering services**: **1 servers**
- **Subscription-based, with turnover requirements for bonuses and withdrawals**: **1 servers**
- **Donations, CSR funding**: **1 servers**
- **Open-source software development, decentralized finance platform**: **1 servers**
- **Open-source protocol with decentralized governance**: **1 servers**
- **Accelerator Program**: **1 servers**
- **Affinity marketing**: **1 servers**
- **B2B trade and supply chain services (wholesale sourcing, procurement, and export support)**: **1 servers**
- **Project-based consulting, software development services, and strategic technology partnerships**: **1 servers**
- **Subscription (membership-based access to content)**: **1 servers**
- **Room rental**: **1 servers**
- **Free Courses**: **1 servers**
- **Direct lodging services and ancillary hospitality offerings (e.g., dining, events)**: **1 servers**
- **Custom Manufacturing Services**: **1 servers**
- **Subscription/Retainer**: **1 servers**
- **Equipment Rental, Sales, and Service**: **1 servers**
- **Service-based (outsourced product development, sourcing, pricing, certifications, and quality control)**: **1 servers**
- **Project-based and maintenance services**: **1 servers**
- **Government Funding, Private Payments**: **1 servers**
- **Course enrollment/licensing**: **1 servers**
- **Subscription-based service (monthly/annual plans for internet access)**: **1 servers**
- **Service-based (contractual projects, custom solutions, and digital marketing services)**: **1 servers**
- **Donations, Sponsorships**: **1 servers**
- **Project-based services (contracting and construction)**: **1 servers**
- **Project-based and hourly rates**: **1 servers**
- **Product sales with installation and service contracts**: **1 servers**
- **Membership fees and certification programs**: **1 servers**
- **Service-based, Local Contracts**: **1 servers**
- **Medical Device Sales**: **1 servers**
- **Consulting, IT services, product curation, and hardware sales (B2B)**: **1 servers**
- **Brand marketing and advertising (likely B2B partnerships with advertisers or B2C through product sales)**: **1 servers**
- **Service-based (consulting, project-based contracts)**: **1 servers**
- **SaaS subscription, B2B service provision, and partnerships (e.g., payment solutions)**: **1 servers**
- **Subscription-based with optional in-app purchases**: **1 servers**
- **Affiliate Marketing (Performance-Based Commission)**: **1 servers**
- **Service-based (interior design, housing solutions, and product sales)**: **1 servers**
- **domain_ownership_transfer**: **1 servers**
- **Content-driven with potential monetization through affiliate partnerships, digital products, or premium memberships**: **1 servers**
- **Service-based (project or retainer fees)**: **1 servers**
- **Advertising (CPM)**: **1 servers**
- **Freemium with paid upgrades**: **1 servers**
- **Subscription/Article Processing Charges (APCs)**: **1 servers**
- **Service-based (B2B consulting and execution)**: **1 servers**
- **Professional Services (fee-for-service)**: **1 servers**
- **Job listing fees and recruitment services**: **1 servers**
- **Subscription-based platform, consulting services**: **1 servers**
- **Advertising and lead generation (promoting venues, events, and services to users)**: **1 servers**
- **Advertising and Content Subscription**: **1 servers**
- **Direct sales of agricultural products and services, consulting, and technical support**: **1 servers**
- **Freemium (free registration with optional premium features)**: **1 servers**
- **Subscription-based with membership tiers**: **1 servers**
- **SaaS subscription, custom software development services, and enterprise solutions**: **1 servers**
- **Freemium (App with optional in-app purchases)**: **1 servers**
- **Advertising, Content Monetization**: **1 servers**
- **Merchandising, Ticket Sales, Music Streaming Royalties**: **1 servers**
- **Restaurant and Grocery Sales**: **1 servers**
- **Investment_Management_Fees**: **1 servers**
- **Project-based and Service-based Revenue**: **1 servers**
- **Fee for Service**: **1 servers**
- **Public Funding/Grants**: **1 servers**
- **Online course subscriptions, certification fees, and potentially corporate training partnerships**: **1 servers**
- **Freight Forwarding Services**: **1 servers**
- **Direct sales (accommodation, dining, wellness services, events, and experiences)**: **1 servers**
- **Premium Services**: **1 servers**
- **Consulting and Services**: **1 servers**
- **Product Sales (likely B2C and B2B for contractors/architects)**: **1 servers**
- **Advertising (sponsored listings)**: **1 servers**
- **Advertising and User-Generated Content Monetization**: **1 servers**
- **Utility subscription and service fees**: **1 servers**
- **Project-based, Managed Services**: **1 servers**
- **Document Distribution**: **1 servers**
- **Advertising and Data Licensing**: **1 servers**
- **Sales of agricultural products**: **1 servers**
- **Probably Freemium with In-App Purchases**: **1 servers**
- **Subscription-based (gambling)**: **1 servers**
- **SaaS subscription, E-commerce**: **1 servers**
- **Investment Platform**: **1 servers**
- **Investment and Acquisition**: **1 servers**
- **Course fees**: **1 servers**
- **Art Sales**: **1 servers**
- **Lead Generation and Service Acquisition**: **1 servers**
- **Subscription-based leads and service listings**: **1 servers**
- **Subscription-based service with additional revenue from lead routing and service business acquisitions**: **1 servers**
- **Lead Generation, Subscription Services**: **1 servers**
- **Free Resource Sharing**: **1 servers**
- **Non-profit (No registration required)**: **1 servers**
- **Service Acquisition and Operation**: **1 servers**
- **Angel Investing, Advisory Services**: **1 servers**
- **Unknown (likely digital content, potential freemium or subscription-based services)**: **1 servers**
- **Unknown (likely freemium or subscription-based for premium content)**: **1 servers**
- **Membership fees (monthly plans, drop-ins, punch cards, and personal training sessions)**: **1 servers**
- **Ad-supported or freemium (likely free with potential monetization via ads or donations)**: **1 servers**
- **Event hosting and sponsorships**: **1 servers**
- **Project_based_consulting_and_services**: **1 servers**
- **SaaS subscription or cloud services**: **1 servers**
- **Freelance services and project-based consulting**: **1 servers**
- **Project-based commissions and collaborations (e.g., design, modeling, rendering services)**: **1 servers**
- **Software licensing, SaaS (Software as a Service), and potentially consulting or training services**: **1 servers**
- **Project-based construction and development**: **1 servers**
- **Commission-based (real estate agent fees) or listing fees**: **1 servers**
- **Unknown (potentially free portfolio hosting, freelance services, or monetization through commissions/prints)**: **1 servers**
- **Membership/subscription**: **1 servers**
- **Marketplace/Listing Fees**: **1 servers**
- **Content_creation_and_education**: **1 servers**
- **Investment/Private Equity**: **1 servers**
- **Property acquisition, development, ownership, and management (fees/revenue from leasing, sales, and asset management).**: **1 servers**
- **Transaction-based fees and service commissions**: **1 servers**
- **Service-based (event planning and coordination)**: **1 servers**
- **Professional services and consulting (project-based fees, contracts, or retainers)**: **1 servers**
- **Advertising and Sponsored Content**: **1 servers**
- **Software Licensing and Subscription**: **1 servers**
- **Project-based and Consultation Fees**: **1 servers**
- **Project-based fees and services (consulting, design, and construction management)**: **1 servers**
- **Commission-based or listing fees (common in real estate platforms)**: **1 servers**
- **domain_name_sale_or_lease**: **1 servers**
- **Subscription/Service Fees**: **1 servers**
- **Commission-based (real estate agent fees) and service fees for property listings, management, and transactions**: **1 servers**
- **Interest and fees on loans**: **1 servers**
- **Community engagement, event participation fees, and potential sponsorships/collaborations**: **1 servers**
- **Commission-based or listing fees (rental services), potentially with advertising revenue or subscription models for premium listings**: **1 servers**
- **Asset Management Fees, Property Sales**: **1 servers**
- **Commission-based sales and leasing**: **1 servers**
- **Commission-based sales and property management fees**: **1 servers**
- **Domain Sales and Leasing**: **1 servers**
- **Non-profit organization**: **1 servers**
- **Domain sales or registration services**: **1 servers**
- **Investment Management Fees, Performance Fees**: **1 servers**
- **Software as a Service (SaaS) or B2B solutions**: **1 servers**
- **Subscription-based and course fees**: **1 servers**
- **IP Licensing, Product Sales, Consulting**: **1 servers**
- **Pay-per-use (transactional purchases for QR codes and AR taggable items)**: **1 servers**
- **Open-source and sponsored projects**: **1 servers**
- **Open-source with enterprise support and services**: **1 servers**
- **Project-based consulting and outsourced engineering services**: **1 servers**
- **Professional services (fee-for-service, retainers, litigation support)**: **1 servers**
- **Project-based contracting and service delivery**: **1 servers**
- **Service-based (project fees, consultations, and design services)**: **1 servers**
- **Hourly billing and flat fees**: **1 servers**
- **Service-based (project fees, retainers, training programs)**: **1 servers**
- **Freemium (core tool free, potential premium features or monetization via ads/affiliate links in guides)**: **1 servers**
- **Content-driven with potential monetization through advertising, sponsorships, and possibly premium memberships or events**: **1 servers**
- **Content-driven with potential for advertising, sponsorships, or premium memberships**: **1 servers**
- **Commission-based domain sales, SaaS subscription (website builder, email services, marketing tools)**: **1 servers**
- **Recruitment Fees**: **1 servers**
- **Project-based Services and Software Licensing**: **1 servers**
- **Professional Services (Project-Based Consulting)**: **1 servers**
- **Project-based consulting and service contracts**: **1 servers**
- **Service-based (project fees, retainers, or contract-based work)**: **1 servers**
- **Unknown (potentially freemium, advertising, or project-based commissions)**: **1 servers**
- **Unknown (likely SaaS, digital product, or specialized software service)**: **1 servers**
- **Consulting and strategic services (diagnostic assessments, implementation, and advisory)**: **1 servers**
- **Project-based consulting and custom software development contracts**: **1 servers**
- **Software as a Service (SaaS) and potentially custom project-based services**: **1 servers**
- **Course sales and subscriptions**: **1 servers**
- **Information/Content Provision**: **1 servers**
- **Unknown (likely digital services, content creation, or consulting)**: **1 servers**
- **Tour Operator Services**: **1 servers**
- **Advertising and potentially premium memberships or services for featured projects**: **1 servers**
- **Freight transportation services (contract-based or per-load)**: **1 servers**
- **Fractional real estate investment platform (likely subscription or transaction-based fees)**: **1 servers**
- **Telecom services and infrastructure provision (B2B contracts, public tenders, and enterprise solutions)**: **1 servers**
- **Subscription-based services (internet, mobile, and home packages)**: **1 servers**
- **SaaS subscription or freemium with premium features**: **1 servers**
- **Membership_subscriptions_and_donations**: **1 servers**
- **Event organization/hosting, sponsorships, and potentially digital content monetization (e.g., ads, subscriptions, or in-game purchases)**: **1 servers**
- **Service-based (SEO optimization and traffic generation)**: **1 servers**
- **commission_based_sale**: **1 servers**
- **Project-based services and custom design work**: **1 servers**
- **Subscription and Transaction Fees**: **1 servers**
- **Project-based consulting fees and specialized services for compliance and heritage management**: **1 servers**
- **Community-driven (potentially monetized via sponsorships, memberships, or ads)**: **1 servers**
- **Project-based services and consulting**: **1 servers**
- **domain_sales_and_lease**: **1 servers**
- **Retail (food and beverage sales), event hosting, and cultural programming**: **1 servers**
- **Advertising or content-driven (potentially monetized through ads, sponsorships, or donations)**: **1 servers**
- **Donations and Workshop Fees**: **1 servers**
- **Design Consultation Fees**: **1 servers**
- **Investment Management**: **1 servers**
- **Property Management Fees, Tenant Placement Services**: **1 servers**
- **Direct sales of prefabricated homes with potential customization services**: **1 servers**
- **Content and Portfolio Hosting (Potential Monetization via Advertising, Sponsorships, or Premium Services)**: **1 servers**
- **Commission-based (for agents), listing fees, and potentially advertising revenue**: **1 servers**
- **Community Engagement/Content Creation (potentially supported by sponsorships, ads, or memberships)**: **1 servers**
- **Digital Sales**: **1 servers**
- **Project-based and retainer models**: **1 servers**
- **Dining services (direct sales of food and beverages)**: **1 servers**
- **Service-based (architectural consulting, project management, and potentially property listings with commissions or fees)**: **1 servers**
- **Advertising, Content Monetization, or Freemium (potentially offering premium resources or services)**: **1 servers**
- **SaaS subscription/paid services**: **1 servers**
- **Digital platform or service (unspecified, possibly e-commerce, content, or consulting)**: **1 servers**
- **Service-based (B2B consulting and software tools)**: **1 servers**
- **Consulting_and_project_based_services**: **1 servers**
- **Content and Education (Ad-supported, potentially affiliate marketing for brokerage services)**: **1 servers**
- **Content and resource platform (potentially with premium memberships, advertising, or affiliate partnerships)**: **1 servers**
- **Project sales and real estate development**: **1 servers**
- **Subscription (paid membership)**: **1 servers**
- **Listing Fees, Subscription Model**: **1 servers**
- **Service-based (direct patient care and medical procedures)**: **1 servers**
- **Freemium or project-based feedback service (likely monetized through premium features or enterprise plans)**: **1 servers**
- **Project-based_service_and_portfolio_display**: **1 servers**
- **Commission-based (likely from property transactions) or lead generation (ads/referrals)**: **1 servers**
- **Advertising and content monetization (likely through subscriptions, ads, or pay-per-view)**: **1 servers**
- **Freemium (with optional premium subscriptions)**: **1 servers**
- **Course subscriptions or paid training programs**: **1 servers**
- **Content and resource monetization (potentially through subscriptions, ads, or premium services)**: **1 servers**
- **Subscription-based SaaS (Software-as-a-Service) and transaction processing fees**: **1 servers**
- **Digital Media/Content (likely advertising, sponsorships, or premium content)**: **1 servers**
- **Subscription and Course Sales**: **1 servers**
- **Service-based (project fees)**: **1 servers**
- **Personal Blog (Non-commercial)**: **1 servers**
- **Professional services (consulting, commissions, and portfolio promotion)**: **1 servers**
- **Service-based (consulting, project management) and product-based (materials supply)**: **1 servers**
- **Service-based (consulting, design, legalization, and construction management) with supplementary e-commerce for home/office products**: **1 servers**
- **Workshops, books, and digital content (self-published materials)**: **1 servers**
- **Service-based (consulting, project management, or freelance opportunities)**: **1 servers**
- **Service-based (project contracts and commissions)**: **1 servers**
- **Service-based (project fees, commissions)**: **1 servers**
- **Domain name brokerage and transaction fees**: **1 servers**
- **Service-based (project fees, contracts, and retainers)**: **1 servers**
- **Service-based (architectural design, consulting, or related fields)**: **1 servers**
- **Service-based (project fees, commissions, and consulting)**: **1 servers**
- **Non-profit, community-driven**: **1 servers**
- **Community engagement, partnerships, workshops, and educational content (likely supported by grants, donations, or collaborations with organizations like Fundación UNICAP)**: **1 servers**
- **Membership_fees_and_professional_services**: **1 servers**
- **Service-based (project fees, retainers, and potential material/design product sales)**: **1 servers**
- **Service-based (project fees, consultations, and commissions)**: **1 servers**
- **Project-based consulting and professional services**: **1 servers**
- **Marketplace/Service Platform (revenue likely generated through service fees or commissions from client-architect transactions)**: **1 servers**
- **E-commerce (Paid Tests)**: **1 servers**
- **Tuition fees and course enrollment payments**: **1 servers**
- **Retail sales of artworks, event hosting fees, and workshop tuition**: **1 servers**
- **Custom Order**: **1 servers**
- **Subscription-based hosting and platform services**: **1 servers**
- **Digital content (freemium or paid courses, memberships, or online tutorials)**: **1 servers**
- **E-commerce (art sales), potential gallery commissions, and possibly artist representation or consignment**: **1 servers**
- **Membership fees and program registrations**: **1 servers**
- **E-commerce (product sales) and service-based (consultations, sessions, and readings)**: **1 servers**
- **Ticket sales and admissions**: **1 servers**
- **Freemium (free with ads, premium without)**: **1 servers**
- **Subscription-based with free trial**: **1 servers**
- **Member Dues and Donations**: **1 servers**
- **Premiums and investments**: **1 servers**
- **Dining**: **1 servers**
- **Restaurant Services**: **1 servers**
- **Subscription/Pay-to-play**: **1 servers**
- **Paid Subscription**: **1 servers**
- **Subscription-based or Freemium**: **1 servers**
- **Subscription-based or Pay-to-Play**: **1 servers**
- **Gaming Revenue (e.g., in-game purchases, subscriptions)**: **1 servers**
- **Subscription-based (Internet Radio Stations starting from $4.95 per month)**: **1 servers**
- **Day passes, lunch reservations, room bookings**: **1 servers**
- **Transaction fees (for money transfers and agent commissions), agent partnerships, and merchant platform services.**: **1 servers**
- **Appointment-based Services**: **1 servers**
- **Retail font sales**: **1 servers**
- **Subscription-based with additional revenue from advertising**: **1 servers**
- **Subscription and Per-consultation Fees**: **1 servers**
- **Freemium (Free tools with premium services)**: **1 servers**
- **Sales of Artwork**: **1 servers**
- **Freelance/Commission-based**: **1 servers**
- **Commission sales and gallery representation**: **1 servers**
- **Subscription-based services, lead generation, and service business acquisition**: **1 servers**
- **Listing Fees**: **1 servers**
- **Subscription-based with deposits**: **1 servers**
- **Non-profit, volunteer-based**: **1 servers**
- **Pay-to-play**: **1 servers**
- **B2B and B2C sales through dealer network**: **1 servers**
- **Service-based (custom development, equipment sales, and rentals)**: **1 servers**
- **Personal Blog (No apparent revenue generation)**: **1 servers**
- **Event hosting and exhibition services (ticket sales, stand rentals, sponsorships, and promotional services for exhibitors)**: **1 servers**
- **Community-driven engagement, advertising, and potential partnerships with BSV ecosystem projects**: **1 servers**
- **SaaS (Software-as-a-Service) or proprietary enterprise software licensing**: **1 servers**
- **In-app purchases, advertising, and potentially free-to-play with monetization**: **1 servers**
- **Premium membership/subscription (paid access for features like premium profiles, messaging, and advanced search tools)**: **1 servers**
- **Freemium (free membership with optional premium features)**: **1 servers**
- **Freemium (free basic profiles with optional premium features)**: **1 servers**
- **Asset Acquisition/Investment**: **1 servers**
- **Freemium_with_advertising_and_content_sponsorship**: **1 servers**
- **Domain Name Registration**: **1 servers**
- **Lead Generation and Subscription-based**: **1 servers**
- **Direct sales, installation services, maintenance contracts, and preventive care subscriptions**: **1 servers**
- **Lead Generation and Reputation Building**: **1 servers**
- **Subscription-based lead generation and service business acquisition**: **1 servers**
- **Subscription-based Leads and Listings**: **1 servers**
- **Community-driven platform with potential future monetization (unspecified)**: **1 servers**
- **Content and digital services (e.g., newsletters, guides, and online resources)**: **1 servers**
- **Lead Generation, Subscription-based**: **1 servers**
- **Lead Generation & Subscription**: **1 servers**
- **Lead Generation and Subscription**: **1 servers**
- **Subscription-based lead generation (B2B), service business acquisition (B2B), and verified contractor marketplace (B2B/B2C)**: **1 servers**
- **Subscription-based leads and services**: **1 servers**
- **Freemium (free basic features with optional premium tools, no explicit subscription revenue model mentioned)**: **1 servers**
- **SaaS subscription (software-as-a-service)**: **1 servers**
- **Subscription-based hosting services and domain registration fees**: **1 servers**
- **Volunteer-based/Community Support**: **1 servers**
- **Freemium (likely with optional premium features or ads)**: **1 servers**
- **Subscription-based with free membership options**: **1 servers**
- **Freemium (free registration with optional premium features, likely monetized through ads, membership upgrades, or premium subscriptions)**: **1 servers**
- **Freemium (Free registration with premium features)**: **1 servers**
- **Subscription-based with free and premium features**: **1 servers**
- **Freemium (free basic membership with optional premium features, likely monetized through ads, subscriptions, or premium profile upgrades)**: **1 servers**
- **Freemium (Free registration, premium features)**: **1 servers**
- **Subscription-based with free registration and premium features**: **1 servers**
- **Freemium (free basic membership with optional paid upgrades for premium features)**: **1 servers**
- **Donations, grants, or non-commercial (likely ad-free or minimal revenue)**: **1 servers**
- **Public Service/Non-profit**: **1 servers**
- **Accommodation and Activity Fees**: **1 servers**
- **Live Performances and Album Sales**: **1 servers**
- **Member contributions and revenue-generating projects**: **1 servers**
- **Sales of HVAC Products and Services**: **1 servers**
- **Volunteer-based**: **1 servers**
- **Utility Services**: **1 servers**
- **Subscription-based, Pay-to-play**: **1 servers**
- **Advertising, CONTRIB token-based services**: **1 servers**
- **Freemium with Affordable Subscriptions**: **1 servers**
- **Subscription-based leads generation**: **1 servers**
- **Subscription/Service**: **1 servers**
- **Potential Advertising or Subscription**: **1 servers**
- **Consultation and Medication Services**: **1 servers**
- **Subscription-based with tiered pricing for service providers**: **1 servers**
- **NFT sales, merchandise sales**: **1 servers**
- **Interest on Loans**: **1 servers**
- **Subscription-based classes and workshops**: **1 servers**
- **Donations and Program Fees**: **1 servers**
- **Retail pharmacy sales and services**: **1 servers**
- **Potentially Commission-based or Membership Subscription**: **1 servers**
- **Domain Acquisition and Sales**: **1 servers**
- **Domain Registration and Website Builder Subscription**: **1 servers**
- **Lead Generation and Subscription-based Services**: **1 servers**
- **Lead Generation and Service Provision**: **1 servers**
- **Subscription-based platform with transparent pricing**: **1 servers**
- **Subscription-based listings and leads**: **1 servers**
- **Subscription-based listings, lead routing, and service acquisition**: **1 servers**
- **Lead Generation, Subscription**: **1 servers**
- **Potential Investment or Acquisition**: **1 servers**
- **Membership fees, interest on loans, service charges**: **1 servers**
- **Brokerage Fees**: **1 servers**
- **Advertising (through affiliate marketing and partnerships with futures prop firms)**: **1 servers**
- **Service-based (outsourced IT management, consulting, and support contracts)**: **1 servers**
- **Advertising, content licensing, and potential future revenue streams post-acquisition or partnership**: **1 servers**
- **Subscription (B2B), Lead Generation (B2B), Business Acquisition (B2B)**: **1 servers**
- **Listing Fees, Services**: **1 servers**
- **Community-driven (likely free with optional memberships or donations)**: **1 servers**
- **Dine-in, Takeout, Delivery**: **1 servers**
- **Freemium with premium subscriptions (paid features, ads, and potential membership tiers)**: **1 servers**
- **Freemium with potential monetization through premium memberships, ads, or affiliate partnerships**: **1 servers**
- **Freemium with premium features (likely paid subscriptions, ads, or premium profile boosts)**: **1 servers**
- **Freemium with premium subscriptions (paid memberships, advanced features, and advertising)**: **1 servers**
- **Freemium (free registration with potential premium features or ads)**: **1 servers**
- **Freemium with premium subscriptions (likely monetized through membership fees, ads, or premium profile features)**: **1 servers**
- **Membership Subscriptions & Advertising**: **1 servers**
- **Freemium with premium features (likely subscription-based for advanced functionalities, ads, or paid memberships)**: **1 servers**
- **Subscription-based with free basic features**: **1 servers**
- **Freemium (free with premium subscriptions)**: **1 servers**
- **Subscription-based (free registration with potential premium features) and potentially advertising-supported**: **1 servers**
- **Freemium with premium features (e.g., advanced search, messaging, profile visibility upgrades) and potential advertising or affiliate partnerships.**: **1 servers**
- **Subscription-based (free and paid memberships) with potential monetization through premium features, ads, or affiliate partnerships.**: **1 servers**
- **Subscription-based (likely free basic access with premium features) and potentially monetized through membership fees, ads, or affiliate partnerships.**: **1 servers**
- **Freemium with premium membership options (likely subscription-based or ad-supported)**: **1 servers**
- **Freemium with premium features (likely subscription-based or ad-supported monetization for advanced services)**: **1 servers**
- **Freemium (free registration with optional premium features, likely monetized through ads, subscriptions, or premium memberships)**: **1 servers**
- **Subscription/Advertising (likely freemium with premium memberships and ads)**: **1 servers**
- **SaaS subscription (membership/lead generation for contractors) and marketplace fees (homeowners may incur costs through contractor services)**: **1 servers**
- **Potential Advertising and Subscription Revenue**: **1 servers**
- **Potential Revenue through Acquisition or Partnership**: **1 servers**
- **Donation-based, Carbon Offset Sales**: **1 servers**
- **Subscription/Enrollment Fees**: **1 servers**
- **Subscription-based Services, Custom Solutions**: **1 servers**
- **Freemium (App Store)**: **1 servers**
- **Subscription fees and transaction fees**: **1 servers**
- **Listing and Brokerage Fees**: **1 servers**
- **Advertising (through in-app ads)**: **1 servers**
- **Subscription-based with free trials and courses**: **1 servers**
- **freelance_consulting**: **1 servers**
- **Subscription-based (assumed)**: **1 servers**
- **Subscription-based (Dimers Pro) with advertising revenue**: **1 servers**
- **Freemium (Free with optional upgrades)**: **1 servers**
- **SaaS subscription, Partnerships**: **1 servers**
- **Fee-for-service**: **1 servers**
- **Venture Capital, Startup Investment**: **1 servers**
- **Licensing and Sales of Technology**: **1 servers**
- **Pharmaceutical Sales and Services**: **1 servers**
- **Potentially Token-based Economy**: **1 servers**
- **Subscription and Listing Fees**: **1 servers**
- **Lead Generation and Matchmaking**: **1 servers**
- **Potential Acquisition or Investment Opportunity**: **1 servers**
- **Subscription-based premium membership**: **1 servers**
- **Hourly Billing and Flat Fees**: **1 servers**
- **Cloud Services**: **1 servers**
- **Paid Gaming Services**: **1 servers**
- **Sales of Original Artworks and Prints**: **1 servers**
- **Personal Brand**: **1 servers**
- **Print Subscription, Advertising**: **1 servers**
- **Freemium (free basic membership with paid premium features)**: **1 servers**
- **Membership fees, journal subscriptions**: **1 servers**
- **regulatory_standardization**: **1 servers**
- **Commissioned work, exhibitions, and residencies**: **1 servers**
- **Publicly Funded**: **1 servers**
- **Memberships, Apparel Sales**: **1 servers**
- **Hourly Billing and Retainer**: **1 servers**
- **Non-profit, funded by Naver Connect Foundation**: **1 servers**
- **Energy Sales**: **1 servers**
- **E-commerce & Subscription**: **1 servers**
- **Subscription-based (includes access to articles, software products, and community)**: **1 servers**
- **Advertising, Subscription-based content**: **1 servers**
- **Freemium (free basic tier with paid premium features)**: **1 servers**
- **E-commerce (Apparel)**: **1 servers**
- **Pay-per-action**: **1 servers**
- **Merchandise Sales, Event Promotion**: **1 servers**
- **Game Sales and Licensing**: **1 servers**
- **Research and Data Compilation**: **1 servers**
- **Freemium with paid plans and token-based storage access**: **1 servers**
- **B2C and B2B**: **1 servers**
- **B2C Sales and Online Retail**: **1 servers**
- **Sales of physical products (flashcards, books) and digital products (audio mp3, app)**: **1 servers**
- **B2B/B2C Sales**: **1 servers**
- **Freemium (in-app purchases)**: **1 servers**
- **Ticket sales, commercial activities (bookshop)**: **1 servers**
- **Game sales, in-app purchases, advertising**: **1 servers**
- **Subscription-based and fee-for-service**: **1 servers**
- **Advertisement-based**: **1 servers**
- **SaaS subscription with pay-less-as-you-grow pricing**: **1 servers**
- **Subscription-based training programs**: **1 servers**
- **Premium-based Insurance Services**: **1 servers**
- **Public funding and tuition fees**: **1 servers**
- **Subscription-based premium features, Free basic plan**: **1 servers**
- **Freemium (with potential premium offerings)**: **1 servers**
- **Freemium (free app with in-app purchases)**: **1 servers**
- **Freemium with subscription plans**: **1 servers**
- **Freelance Writing**: **1 servers**
- **Advertising (inferred from similar platforms)**: **1 servers**
- **Freemium (with potential in-app purchases)**: **1 servers**
- **Ride-hailing Platform**: **1 servers**
- **Property Management Fees, Rental Income**: **1 servers**
- **Subscription/Access-based**: **1 servers**
- **Sales of Hardware and Software Solutions**: **1 servers**
- **Tour Package Sales, Car Rental Services**: **1 servers**
- **Pay-what-you-want**: **1 servers**
- **Freemium (Free with in-app purchases)**: **1 servers**
- **Prescription sales and related services**: **1 servers**
- **Commission-based trading platform**: **1 servers**
- **Advertising, Service Fee**: **1 servers**
- **App Downloads**: **1 servers**
- **Entry Fees and Facility Rental**: **1 servers**
- **Donations, Government Funding**: **1 servers**
- **Government funding and membership fees**: **1 servers**
- **Event ticket sales, sponsorships, and philanthropic initiatives**: **1 servers**
- **Manufacturing and Sales of Ice Cream Products**: **1 servers**
- **Advertising (inferred)**: **1 servers**
- **Free app with additional features available through premium subscriptions**: **1 servers**
- **Donations and Sales (books, materials)**: **1 servers**
- **Subscription-based (for parking services), Fines (for violation management)**: **1 servers**
- **Subscription and In-game purchases**: **1 servers**
- **Subscription-based (Club Jam) and Consulting Services**: **1 servers**
- **Free Streaming with Possible Donations**: **1 servers**
- **Advertising, Potential Partnerships**: **1 servers**
- **Personal Branding/Content Creation**: **1 servers**
- **Subscription-based (print guide) and Advertising (online)**: **1 servers**
- **Government Funding & Membership Fees**: **1 servers**
- **Advertising and Subscription Fees**: **1 servers**
- **Personal Website**: **1 servers**
- **Job Listing Platform**: **1 servers**
- **Fast Food Restaurant**: **1 servers**
- **Government Subsidized**: **1 servers**
- **Hourly billing and contingency fees for successful cases**: **1 servers**
- **SaaS subscription with API access**: **1 servers**
- **Public Funded**: **1 servers**
- **Transaction fees, liquidity mining rewards**: **1 servers**
- **Donations/Grants**: **1 servers**
- **Non-profit, funded by grants or sponsorships**: **1 servers**
- **Merchandising and Ticket Sales**: **1 servers**
- **Freemium subscription with premium features and ads**: **1 servers**
- **Donations and mission trips**: **1 servers**
- **Brick-and-mortar sales, franchising**: **1 servers**
- **Performance-based advertising (affiliate marketing)**: **1 servers**
- **Retail sales of pharmaceuticals and healthcare products**: **1 servers**
- **Premium app with in-app purchases**: **1 servers**
- **Freemium (free basic service with optional premium features)**: **1 servers**
- **User-generated content**: **1 servers**
- **Free entry for Auckland residents, paid admission for visitors**: **1 servers**
- **Sponsored Events & Content**: **1 servers**
- **Subscription-based (E-Paper) and Advertising**: **1 servers**
- **B2G (Business-to-Government)**: **1 servers**
- **Paid Medical Services**: **1 servers**
- **Banking Services**: **1 servers**
- **Commission-based transactions**: **1 servers**
- **Software Sales & Licensing**: **1 servers**
- **Open-source/Freeware**: **1 servers**
- **Donations and listener support**: **1 servers**
- **Donations and fundraising events**: **1 servers**
- **Advocacy and Networking**: **1 servers**
- **Premium-based**: **1 servers**
- **Public Funding, Ticket Sales**: **1 servers**
- **Freemium (with potential future monetization)**: **1 servers**
- **Donations and Course Fees**: **1 servers**
- **Monetization system (similar to OnlyFans)**: **1 servers**
- **Grant-funded and donations**: **1 servers**
- **Hardware Sales**: **1 servers**
- **Service-based revenue generation**: **1 servers**
- **Product Sales**: **1 servers**
- **Project-based and subscription services**: **1 servers**
- **Freemium (with potential ads or in-app purchases)**: **1 servers**
- **Print subscriptions and online advertising**: **1 servers**
- **Freemium (with unlimited projects and reference lists available for free)**: **1 servers**
- **Investment Portfolio Management**: **1 servers**
- **Data Aggregation and Analysis**: **1 servers**
- **Decentralized Platform**: **1 servers**
- **Fundraising through contributions from individuals, corporations, foundations, and government agencies**: **1 servers**
- **Non-profit, event-based**: **1 servers**
- **Domain Name Sales and Registrations**: **1 servers**
- **Grant-funded / Non-profit**: **1 servers**
- **Advertising (Classified Ads)**: **1 servers**
- **Donations and subscriptions**: **1 servers**
- **Tours and Experiences**: **1 servers**
- **Real-money Gaming**: **1 servers**
- **Online_courses_and_digital_products**: **1 servers**
- **Subscription-based online courses**: **1 servers**
- **Admission fees**: **1 servers**
- **Freemium (free with optional paid upgrades for premium features)**: **1 servers**
- **Subscription-based with free trials available**: **1 servers**
- **SaaS subscription, Hardware sales**: **1 servers**
- **Subscription or Freemium**: **1 servers**
- **Affiliate Marketing (credit card referrals)**: **1 servers**
- **Freemium (free consultations, paid premium services)**: **1 servers**
- **Subscription-based & Crypto Payments**: **1 servers**
- **Prescription Fulfillment**: **1 servers**
- **Selling Software**: **1 servers**
- **SaaS subscription with additional services**: **1 servers**
- **Donations**: **1 servers**
- **Freemium (app is free, with optional premium features)**: **1 servers**
- **Equipment Rental**: **1 servers**
- **Subscription-based premium features**: **1 servers**
- **Subscription-based with access to savings opportunities**: **1 servers**
- **Ticket Sales and Event Hosting**: **1 servers**
- **Membership/Subscription (if applicable)**: **1 servers**
- **Program Funding**: **1 servers**
- **Free service with possible premium features**: **1 servers**
- **Charitable donations and grants**: **1 servers**
- **Freemium (with potential premium services)**: **1 servers**
- **Subscription-based (SalusOne Premium)**: **1 servers**
- **Internal Recruitment**: **1 servers**
- **Subscription-based, Book Sales, Licensing Fees**: **1 servers**
- **Advertising & User Engagement**: **1 servers**
- **Freemium subscription with premium plans**: **1 servers**
- **Paid subscriptions and courses**: **1 servers**
- **Freemium (free basic service, premium features)**: **1 servers**
- **Public Services**: **1 servers**
- **Subscription-based and in-game purchases**: **1 servers**
- **Member dues and contributions**: **1 servers**
- **Subscription-based, Pay-per-course**: **1 servers**
- **Government funding (CDC Comprehensive Suicide Prevention Program)**: **1 servers**
- **Advertising & Sponsored Content**: **1 servers**
- **Broadcasting and Streaming**: **1 servers**
- **Subscription-based with optional VIP packages**: **1 servers**
- **Subscription and Commission**: **1 servers**
- **Commission-based (rake)**: **1 servers**
- **Subscription-based Courses, Premium Membership (Suraasa Plus)**: **1 servers**
- **Membership fees, conference attendance fees, tutorial program revenues**: **1 servers**
- **Public promotion and event organization**: **1 servers**
- **Revenue generated through gambling activities**: **1 servers**
- **Hourly Billing, Retainer Agreements**: **1 servers**
- **Membership fees and services**: **1 servers**
- **Advertising, Subscriptions**: **1 servers**
- **Commission-based (8-10% per ticket sale)**: **1 servers**
- **Subscription-based broadband and mobile services**: **1 servers**
- **Room bookings, packages, amenities, and event hosting**: **1 servers**
- **Ticket sales, donations, grants**: **1 servers**
- **Membership subscriptions and online course sales**: **1 servers**
- **Subscription-based premium content, instructor-led training programs**: **1 servers**
- **Non-profit (government funded)**: **1 servers**
- **Project-based contracting**: **1 servers**
- **SaaS subscription (Premium/Premium Protect)**: **1 servers**
- **Subscription-based (Substack)**: **1 servers**
- **Advertising, In-app purchases**: **1 servers**
- **Subscription and Premium Content**: **1 servers**
- **Platform Facilitator**: **1 servers**
- **Subscription-based with profit sharing**: **1 servers**
- **Financing Services**: **1 servers**
- **Freemium (Free with optional donations)**: **1 servers**
- **Non-profit, funded by the University of Florida**: **1 servers**
- **Service Subscription and On-demand Booking**: **1 servers**
- **Consulting fees, Commission-based revenue**: **1 servers**
- **Media & Content**: **1 servers**
- **Service-based, subscription or per-use pricing**: **1 servers**
- **B2B Sales & Distribution**: **1 servers**
- **Delivery Fees and Menu Purchases**: **1 servers**
- **Non-profit (government-funded)**: **1 servers**
- **Free service with premium features available for a fee**: **1 servers**
- **Premiums**: **1 servers**
- **Membership-based access to exclusive deals**: **1 servers**
- **Donations, Grants**: **1 servers**
- **Subscription-based with additional services**: **1 servers**
- **Subscription-based Learning Platform**: **1 servers**
- **Advertising-based revenue model with additional premium services for users**: **1 servers**
- **Listing fees, premium services subscription**: **1 servers**
- **Email Marketing**: **1 servers**
- **Premium Theme Sales, Subscriptions (Pro Plans)**: **1 servers**
- **Cryptocurrency Rewards**: **1 servers**
- **Freemium with Partner Offers**: **1 servers**
- **B2C Sales through distributors and retailers**: **1 servers**
- **Subscription-based service with monthly fees**: **1 servers**
- **Subscription-based, Pay-per-use**: **1 servers**
- **B2B Sales of Assay Kits**: **1 servers**
- **Car Sales & Leasing Services**: **1 servers**
- **Domain Registration and Hosting Services**: **1 servers**
- **Unknown (potentially content-based, educational, or freemium with possible premium services)**: **1 servers**
- **Service-based (property brokerage, valuation, and real estate development)**: **1 servers**
- **Pharmaceuticals**: **1 servers**
- **Listing Fees, Advertising**: **1 servers**
- **Non-profit (Personal Website)**: **1 servers**
- **Subscription-based premium content, potentially with advertising**: **1 servers**
- **Trading Fees and Spreads**: **1 servers**
- **Commission-based fees on trades**: **1 servers**
- **Project-based, Outsourcing**: **1 servers**
- **Wholesale/Distribution (B2B) with retail sales through dispensaries (B2C)**: **1 servers**
- **SaaS subscription (with potential API integrations and marketplace services)**: **1 servers**
- **Domain Acquisition and Monetization**: **1 servers**
- **Freemium (free membership with limited features, premium membership with additional features)**: **1 servers**
- **Service-based subscription and on-demand**: **1 servers**
- **Free Service**: **1 servers**
- **Property Management Services**: **1 servers**
- **Subscription-based cleaning services**: **1 servers**
- **Research and Development Services**: **1 servers**
- **Premium Subscription with Free Access to Basic Features**: **1 servers**
- **Commission-based fee structure for successful investments facilitated through the platform**: **1 servers**
- **Mobile Application**: **1 servers**
- **SaaS subscription with free, starter, pro, and premium plans**: **1 servers**
- **SaaS subscription with premium features**: **1 servers**
- **Donations and Support**: **1 servers**
- **Advertising (Ad Supported apps)**: **1 servers**
- **Pay-per-placement with escrow**: **1 servers**
- **SaaS subscription (with optional paid licenses)**: **1 servers**
- **Freemium (Freebies & Premium Assets)**: **1 servers**
- **Freemium (with optional subscriptions)**: **1 servers**
- **SaaS subscription with tiered pricing plans**: **1 servers**
- **Non-profit/Research**: **1 servers**
- **Data licensing and API services**: **1 servers**
- **Press Release Distribution Services**: **1 servers**
- **Ticket sales and bar revenue**: **1 servers**
- **Hourly billing and retainer services**: **1 servers**
- **Subscription-based online classes and workshops**: **1 servers**
- **Earned Rewards**: **1 servers**
- **Licensing**: **1 servers**
- **E-commerce (direct sales to consumers)**: **1 servers**
- **E-commerce (aggregated deals and promotions)**: **1 servers**
- **E-commerce platform with cash on delivery available**: **1 servers**
- **E-commerce with physical retail stores**: **1 servers**
- **Wholesale Distribution**: **1 servers**
- **Unknown (likely independent, non-commercial)**: **1 servers**
- **domain_name_auction**: **1 servers**
- **Direct-to-consumer e-commerce**: **1 servers**
- **SEO Services**: **1 servers**
- **Direct-to-consumer (D2C) or local food service (e.g., catering, delivery, or dine-in)**: **1 servers**
- **E-commerce (direct sales of products and services)**: **1 servers**
- **B2B wholesale/distribution**: **1 servers**
- **Direct-to-consumer e-commerce with product sales and customization services**: **1 servers**
- **E-commerce (potentially with commissions or markups on sales)**: **1 servers**
- **B2B wholesale distribution and bulk supply**: **1 servers**
- **E-commerce (direct sales of physical products)**: **1 servers**
- **Discount Retail**: **1 servers**
- **Commission-based (charging a percentage of sales)**: **1 servers**
- **Wholesale Sales**: **1 servers**
- **Direct retail sales (in-person) with additional revenue from catering, custom cakes, and prepared foods**: **1 servers**
- **Rent-based revenue generation through retail spaces and entertainment facilities**: **1 servers**
- **Partnership Investment**: **1 servers**
- **Acquisition, Partnership, Investment**: **1 servers**
- **Content-driven with potential affiliate or referral partnerships for financial products**: **1 servers**
- **Sales of products**: **1 servers**
- **Service-based (project contracts and labor)**: **1 servers**
- **E-commerce with local pickup**: **1 servers**
- **Sales of goods**: **1 servers**
- **Online Sales of Physical Products**: **1 servers**
- **E-commerce subscription model with proceeds contributing to sustainable farming practices**: **1 servers**
- **E-commerce transactions**: **1 servers**
- **E-commerce, subscription-based premium features**: **1 servers**
- **E-commerce (Digital products and services)**: **1 servers**
- **Auction fees and commissions**: **1 servers**
- **Premium Memberships, Donations**: **1 servers**
- **Discounts and Affiliate Marketing**: **1 servers**
- **Commission-based (charges a fee per order)**: **1 servers**
- **Chauffeur Service Bookings**: **1 servers**
- **Subscription-based with advertising revenue**: **1 servers**
- **Brick-and-mortar retail sales**: **1 servers**
- **Consultation Services**: **1 servers**
- **Membership Fees and Commissions from Sales**: **1 servers**
- **Donations, Adoptions, Grants**: **1 servers**
- **Pay-What-You-Wish (tips-based)**: **1 servers**
- **Rental Service Fee**: **1 servers**
- **Commission-based, with free listing for sellers and authentication services**: **1 servers**
- **Commission-based (through ticket sales)**: **1 servers**
- **Commission-based E-commerce**: **1 servers**
- **Wholesale and Supply**: **1 servers**
- **Sales of duty-free products**: **1 servers**
- **Delivery Service**: **1 servers**
- **Subscription-based service with premium features**: **1 servers**
- **Advertising, Subscription-based**: **1 servers**
- **Mining Pool Fees**: **1 servers**
- **Data Services Subscription**: **1 servers**
- **App Sales/Downloads**: **1 servers**
- **E-commerce and Services**: **1 servers**
- **Advertising and Subscription**: **1 servers**
- **custom_projects_and_consulting**: **1 servers**
- **Unknown (likely SaaS, open-source contributions, or developer-focused services)**: **1 servers**
- **Membership-based insurance program**: **1 servers**
- **Direct-to-consumer sales with a focus on exclusive/limited-edition products and promotional partnerships**: **1 servers**
- **Product Sales and Services**: **1 servers**
- **Service-based (consulting/agency fees)**: **1 servers**
- **Open-Source Software with Enterprise Offerings**: **1 servers**
- **Personal Blog/Projects**: **1 servers**
- **SaaS subscription or service-based (potential paid access for bot management features)**: **1 servers**
- **NFT Sales**: **1 servers**
- **SaaS subscription with free trial**: **1 servers**
- **Investment_Partnership**: **1 servers**
- **E-learning subscriptions and courses**: **1 servers**
- **Freemium (with optional paid services)**: **1 servers**
- **Cryptocurrency-based platform**: **1 servers**
- **Open-source and community support**: **1 servers**
- **E-commerce and Digital Content Sales**: **1 servers**
- **SaaS subscription (free with paid plans)**: **1 servers**
- **Freelance/Contract**: **1 servers**
- **SaaS subscription (pay-as-you-go, API-based pricing)**: **1 servers**
- **Freemium/Community-driven (likely free with potential monetization via ads or premium features)**: **1 servers**
- **Project-based consulting and custom software development services**: **1 servers**
- **Freemium or open-access (likely monetization via ads, sponsorships, or premium features in the future)**: **1 servers**
- **API services and documentation (likely monetized through API access fees, enterprise plans, or partnerships)**: **1 servers**
- **Unknown (likely SaaS, marketplace, or tool-based subscription)**: **1 servers**
- **Advertising and potentially affiliate marketing (e.g., promoting related products or services)**: **1 servers**
- **Capital deployment and performance-based participation (profit-sharing)**: **1 servers**
- **Project-based service fees (custom web development, SaaS platforms, and digital experiences)**: **1 servers**
- **Investment Management Fees**: **1 servers**
- **Associated_with_parent_organization_(Ediciones_ARQ)_;_likely_supported_by_subscriptions,_sponsorships,_or_donations_from_parent_entity**: **1 servers**
- **Content and service-based (potentially consulting, design inspiration, or educational resources)**: **1 servers**
- **Content-driven with potential for workshops, courses, or digital products (e.g., e-books, online courses)**: **1 servers**
- **Affiliate Marketing, Coaching Services**: **1 servers**
- **Investment**: **1 servers**
- **Freelance or Job Search**: **1 servers**
- **one-time payment per service (transactional)**: **1 servers**
- **B2B (Designers, Architects) and B2C (Luxury Homeowners)**: **1 servers**
- **Open-source with API key requirement**: **1 servers**
- **Open-source and community-driven**: **1 servers**
- **Non-profit/Open Source**: **1 servers**
- **Freemium (free usage with optional premium features)**: **1 servers**
- **Freemium SaaS**: **1 servers**
- **Stablecoin issuance and infrastructure services**: **1 servers**
- **SaaS subscription & API usage**: **1 servers**
- **Sponsorships and Partnerships**: **1 servers**
- **SaaS (Serverless as a Service) with potential freemium or pay-as-you-go pricing**: **1 servers**
- **Trading Fees, Membership Rebates**: **1 servers**
- **SaaS subscription with free individual site lookups**: **1 servers**
- **consulting_and_content_creation**: **1 servers**
- **Advertising, Commission-based Bookings**: **1 servers**
- **Cryptocurrency Mining Services**: **1 servers**
- **Premium Plugin Sales**: **1 servers**
- **Cryptocurrency Trading Platform**: **1 servers**
- **Token-based subscription**: **1 servers**
- **Subscription-based leads and verified listings**: **1 servers**
- **Training and Services**: **1 servers**
- **Freelance services, source code sales, tutorials**: **1 servers**
- **Trading Platform Fees**: **1 servers**
- **Investment and Partnership**: **1 servers**
- **Decentralized Governance**: **1 servers**
- **Potentially a mix of token sales, transaction fees, and partnerships**: **1 servers**
- **Cryptocurrency**: **1 servers**
- **Investment Opportunity**: **1 servers**
- **Investment/Partnership Opportunities**: **1 servers**
- **Crypto Token Sales & Services**: **1 servers**
- **Token-based economy**: **1 servers**
- **asset_sale_or_licensing**: **1 servers**
- **SaaS subscription and pay-per-use messaging services**: **1 servers**
- **SaaS (Serverless as a Service)**: **1 servers**
- **Freemium API access with paid tiers for higher usage and advanced features**: **1 servers**
- **Freemium with subscription and one-time credit packs (SaaS-based)**: **1 servers**
- **Freemium or open-source with potential monetization through premium features, sponsorships, or ads**: **1 servers**
- **SaaS subscription with affordable pricing plans**: **1 servers**
- **One-Time Purchase**: **1 servers**
- **Content_monetization_through_affiliate_partnerships_and_personal_projects**: **1 servers**
- **Advertising/Donations (if applicable)**: **1 servers**
- **Decentralized Finance Platform**: **1 servers**
- **Freemium/SaaS subscription**: **1 servers**
- **Funded by grants and donations**: **1 servers**
- **Freemium (Free listings with optional paid promotion)**: **1 servers**
- **API usage fees**: **1 servers**
- **SaaS subscription with managed advertising**: **1 servers**
- **Donation-based fundraising**: **1 servers**
- **SaaS subscription with pay-per-use pricing for AI compute resources**: **1 servers**
- **Project-based and retainer models for services**: **1 servers**
- **Sponsored Content, Premium Courses**: **1 servers**
- **Cloud Services Subscription**: **1 servers**
- **Embedded Finance, Subscription-based**: **1 servers**
- **Open Source with Optional Enterprise Plans**: **1 servers**
- **Subscription-based SaaS platform with additional transaction fees**: **1 servers**
- **Asset Management**: **1 servers**
- **SaaS subscription with free tier**: **1 servers**
- **Freemium (Free core plugin with premium extensions)**: **1 servers**
- **B2B SaaS subscription with additional revenue from transaction fees**: **1 servers**
- **Cryptocurrency Services**: **1 servers**
- **Freelance Consulting**: **1 servers**
- **Freemium (with optional paid plans)**: **1 servers**
- **Non-commercial (personal notes)**: **1 servers**
- **Membership subscription**: **1 servers**
- **SaaS subscription with a freemium model**: **1 servers**
- **Sale of properties**: **1 servers**
- **Advertising/Sponsorship**: **1 servers**
- **SaaS subscription ($29/month or $249/year)**: **1 servers**
- **Advertising and Data Services**: **1 servers**
- **Freemium with premium extensions**: **1 servers**
- **Premium Subscription, Token Staking**: **1 servers**
- **Subscription and Certifications**: **1 servers**
- **Freelance or Personal Project**: **1 servers**
- **SaaS subscription with free community edition**: **1 servers**
- **Open-source with commercial support options**: **1 servers**
- **Decentralized**: **1 servers**
- **Community Support and Sponsorship**: **1 servers**
- **Open source and community supported**: **1 servers**
- **Decentralized Network, Token-based Incentives**: **1 servers**
- **Trading Fees, Listing Fees**: **1 servers**
- **Open Source Contributions**: **1 servers**
- **Custom Development Services**: **1 servers**
- **Open-source and sponsorships**: **1 servers**
- **SaaS subscription (Free version available)**: **1 servers**
- **Sales of properties**: **1 servers**
- **Open Source with Optional Premium Features**: **1 servers**
- **Community Support/Donations**: **1 servers**
- **Open-source with example services and documentation**: **1 servers**
- **Advertising (unknown)**: **1 servers**
- **Open Source/Community Supported**: **1 servers**
- **Project-based and Subscription-based Services**: **1 servers**
- **Non-profit (No affiliation with Home Assistant)**: **1 servers**
- **Donation-based (open source)**: **1 servers**
- **Grant-funded (NIGMS)**: **1 servers**
- **Freemium (possibly with premium services)**: **1 servers**
- **Open Source/Community Support**: **1 servers**
- **Community-driven (No revenue)**: **1 servers**
- **Advertising & Book Sales**: **1 servers**
- **Donations/Open Source**: **1 servers**
- **Premium Courses & Bundles**: **1 servers**
- **Software Licensing & Support**: **1 servers**
- **Open-source, community-driven with potential for decentralized governance**: **1 servers**
- **Non-profit/Advertising**: **1 servers**
- **Yield Farming, Trading Fees**: **1 servers**
- **Rewarded Activities, Virtual Currency Exchange**: **1 servers**
- **SaaS subscription (through GitHub Sponsors)**: **1 servers**
- **Freeware**: **1 servers**
- **Trading Fees**: **1 servers**
- **Volunteer-driven, no revenue generation**: **1 servers**
- **Transaction fees, service charges**: **1 servers**
- **Community-powered**: **1 servers**
- **Non-profit; no apparent revenue generation**: **1 servers**
- **Freemium (Free tier with paid PRO features)**: **1 servers**
- **App Sales & In-app Purchases**: **1 servers**
- **Open Source with Cloud Services**: **1 servers**
- **Open-source with enterprise support**: **1 servers**
- **Advertising/Donations**: **1 servers**
- **Donations and government funding**: **1 servers**
- **Advertising (no ads mentioned, so it might be donation-based or other)**: **1 servers**
- **SaaS subscription and PAYG**: **1 servers**
- **Custom Development**: **1 servers**
- **Freemium (free services with optional paid features)**: **1 servers**
- **Subscription-based with listing options**: **1 servers**
- **Consulting Services, Course Sales, Affiliate Marketing**: **1 servers**
- **Manufacturing and Sales**: **1 servers**
- **Community-driven (free membership, open specifications, and public resources with potential for future monetization via .agent TLD or related services)**: **1 servers**
- **Investment, Strategic Acquisitions**: **1 servers**
- **Pay-per-use**: **1 servers**
- **Domain Name Sales**: **1 servers**
- **API usage and potential premium features**: **1 servers**
- **Services and Consulting**: **1 servers**
- **Premium subscriptions and data licensing**: **1 servers**
- **Unspecified**: **1 servers**
- **Project-based freelance/consulting services (revenue generated per project or campaign)**: **1 servers**
- **Distributor and Sourcing Services**: **1 servers**
- **mixed (consulting, open-source tools, experimental projects, and proprietary AI/software solutions for higher education)**: **1 servers**
- **Freemium (free tier with paid upgrades for advanced features)**: **1 servers**
- **Cloud Offering with Free Trial**: **1 servers**
- **Commission on trades, fees for services**: **1 servers**
- **Advertising (free listings with optional premium features)**: **1 servers**
- **Freemium (with optional paid features)**: **1 servers**
- **Class and Rental Fees**: **1 servers**
- **Paid Software**: **1 servers**
- **SaaS subscription with free tutorials**: **1 servers**
- **Freelance Writing Services**: **1 servers**
- **content_aggregation_and_engagement**: **1 servers**
- **Open-source contributions**: **1 servers**
- **SaaS subscription with free tier available**: **1 servers**
- **Subscription-based Web Hosting Services**: **1 servers**
- **Commission-based sales of luxury properties**: **1 servers**
- **SaaS subscription, Pay-per-session**: **1 servers**
- **SaaS subscription (likely)**: **1 servers**
- **API subscription**: **1 servers**
- **Freemium (Free while in beta) with potential future monetization via Coil and Interledger Protocol**: **1 servers**
- **SaaS subscription (free credits)**: **1 servers**
- **Open Source with Optional Paid Features**: **1 servers**
- **Advertising (Substack)**: **1 servers**
- **Free for design partners, potential revenue from enterprise use**: **1 servers**
- **Interest income from savings accounts**: **1 servers**
- **Freelance or Personal Projects**: **1 servers**
- **In-game purchases and potentially partnerships for rewards**: **1 servers**
- **E-learning platform with paid courses**: **1 servers**
- **Open Source & Donations**: **1 servers**
- **API Access Subscription**: **1 servers**
- **SaaS subscription with freemium model**: **1 servers**
- **Government Services**: **1 servers**
- **Project-based and consulting services**: **1 servers**
- **Content and consulting (mix of free resources, paid workshops, and consulting services)**: **1 servers**
- **Commission-based and subscription fees**: **1 servers**
- **Content-driven (likely supported by advertising, sponsorships, or donations)**: **1 servers**
- **Service fees for maintenance, avionics upgrades, and pre-purchase aircraft inspections**: **1 servers**
- **Subscription and Pay-to-Play**: **1 servers**
- **content_creation_and_engagement**: **1 servers**
- **Unknown (potentially ad-supported, freemium, or content-driven with potential monetization through partnerships or premium content)**: **1 servers**
- **Advertising (promoting local businesses)**: **1 servers**
- **Premium Features (e.g., private shows, tips)**: **1 servers**
- **Freemium (with premium services)**: **1 servers**
- **Peer-to-Peer Rental Platform**: **1 servers**
- **Freemium (可能)**: **1 servers**
- **Freemium subscription model (with ads)**: **1 servers**
- **Sales of Educational Robots and Programming Tools**: **1 servers**
- **SaaS subscription, Consulting services**: **1 servers**
- **Commission-based, One-piece Order Service**: **1 servers**
- **Hosting services and managed solutions (subscription-based)**: **1 servers**
- **Direct sales (B2C) and B2B (wholesale to interior designers and contractors), with a focus on custom production and installation services**: **1 servers**
- **Community support and resource sharing**: **1 servers**

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
