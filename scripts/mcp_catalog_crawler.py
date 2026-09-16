#!/usr/bin/env python3
"""
scripts/mcp_catalog_crawler.py
DomainScope MCP & AI Manifest Crawler and Batch Processing Pipeline.

Crawls input domain lists concurrently, probes well-known AI and MCP endpoints:
  - /.well-known/mcp/server-card.json
  - /.well-known/ai-catalog.json
  - /.well-known/mcp
  - /llms.txt
  - /llms-full.txt

Inputs supported:
  - Database: PostgreSQL (direct psycopg or streaming psql) or SQLite
  - Files: Raw text (one domain per line), CSV, TSV
  - CLI: Space-separated domain arguments
  - STDIN: Piped domain stream

Validates payloads, tracks response latency, and outputs structured batch files
for DomainScope queue ingestion and directory indexing. Supports durable checkpoints
to pause and resume cleanly.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
import signal
import sqlite3
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Set, Tuple

USER_AGENT = "DomainScope-MCPCrawler/1.0 (+https://domainscope.scrapetheworld.org/mcp-directory)"
DEFAULT_TIMEOUT = 3.5
DEFAULT_CONCURRENCY = 20

# Standard AI / MCP discovery endpoints to probe per domain
PROBE_PATHS = [
    ("/.well-known/mcp/server-card.json", "mcp_server_card"),
    ("/.well-known/ai-catalog.json", "ai_catalog"),
    ("/.well-known/mcp", "mcp_endpoint"),
    ("/llms.txt", "llms_txt"),
    ("/llms-full.txt", "llms_full_txt"),
]


# ==============================================================================
# SOLID Component 1: Data Models & Entities
# ==============================================================================

@dataclass
class DiscoveredArtifact:
    artifact_type: str
    url: str
    status_code: int
    latency_ms: int
    content_length: int
    valid_json: bool = False
    tools_count: Optional[int] = None
    server_name: Optional[str] = None
    description: Optional[str] = None
    protocol_version: Optional[str] = None
    raw_preview: Optional[str] = None


@dataclass
class DomainCrawlResult:
    domain: str
    inspected_at: str
    has_ai_presence: bool
    artifacts: List[DiscoveredArtifact] = field(default_factory=list)
    min_latency_ms: Optional[int] = None
    primary_mcp_url: Optional[str] = None
    primary_catalog_url: Optional[str] = None
    primary_llms_url: Optional[str] = None
    total_tools_declared: int = 0
    error: Optional[str] = None


# ==============================================================================
# SOLID Component 2: Normalizer (Single Responsibility)
# ==============================================================================

class DomainNormalizer:
    """Normalizes raw input strings into clean, canonical domain names."""

    @staticmethod
    def normalize(raw: str) -> Optional[str]:
        if not raw:
            return None
        text = raw.strip().lower()
        # Strip scheme if present
        if "://" in text:
            parsed = urllib.parse.urlparse(text)
            text = parsed.netloc or parsed.path
        # Strip path, port, credentials
        text = text.split("/")[0].split("?")[0].split("#")[0]
        if "@" in text:
            text = text.split("@")[-1]
        if ":" in text:
            text = text.split(":")[0]
        text = text.rstrip(".")
        if not text or "." not in text or " " in text:
            return None
        return text


# ==============================================================================
# SOLID Component 3: Database Domain Sources (DIP & OCP)
# ==============================================================================

def load_env_file(path: Optional[Path] = None) -> Dict[str, str]:
    """Lightweight .env parser without external dependencies."""
    candidates = [
        path,
        Path(".env"),
        Path("../.env"),
        Path(__file__).resolve().parent.parent / ".env",
    ]
    env_vars: Dict[str, str] = {}
    for cand in candidates:
        if cand and cand.is_file():
            try:
                for line in cand.read_text(encoding="utf-8").splitlines():
                    line = line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    key, val = line.split("=", 1)
                    env_vars[key.strip()] = val.strip().strip("'\"")
                break
            except Exception:
                pass
    return env_vars


class BaseDatabaseSource(ABC):
    """Abstract interface for database domain sources."""

    @abstractmethod
    def stream_domains(
        self,
        query: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Iterator[str]:
        """Streams un-normalized domain strings from database."""
        pass


class SQLiteDomainSource(BaseDatabaseSource):
    """Fetches domains from a SQLite database file."""

    def __init__(self, db_path: str):
        self.db_path = db_path

    def stream_domains(
        self,
        query: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Iterator[str]:
        if not os.path.exists(self.db_path):
            raise FileNotFoundError(f"SQLite database file not found: {self.db_path}")

        sql = query or "SELECT name FROM domains"
        if "LIMIT" not in sql.upper() and limit:
            sql += f" LIMIT {int(limit)}"
            if offset:
                sql += f" OFFSET {int(offset)}"
        elif "OFFSET" not in sql.upper() and offset:
            sql += f" OFFSET {int(offset)}"

        conn = sqlite3.connect(self.db_path)
        try:
            cur = conn.cursor()
            cur.execute(sql)
            for row in cur:
                if row and row[0]:
                    yield str(row[0])
        finally:
            conn.close()


class PostgresDomainSource(BaseDatabaseSource):
    """
    Fetches domains from PostgreSQL.
    Adapts automatically between native driver (psycopg / psycopg2) and streaming psql CLI.
    """

    def __init__(self, dsn: str):
        self.dsn = dsn

    def stream_domains(
        self,
        query: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Iterator[str]:
        sql = query or "SELECT name FROM domains"
        if "LIMIT" not in sql.upper() and limit:
            sql += f" LIMIT {int(limit)}"
            if offset:
                sql += f" OFFSET {int(offset)}"
        elif "OFFSET" not in sql.upper() and offset:
            sql += f" OFFSET {int(offset)}"

        # Ensure statement ends with semicolon for CLI compatibility
        if not sql.rstrip().endswith(";"):
            sql = sql.rstrip() + ";"

        # Attempt 1: Native psycopg (v3) or psycopg2 if available
        try:
            import psycopg  # type: ignore
            conn = psycopg.connect(self.dsn)
            with conn.cursor() as cur:
                cur.execute(sql)
                for row in cur:
                    if row and row[0]:
                        yield str(row[0])
            conn.close()
            return
        except ImportError:
            pass
        except Exception as exc:
            raise RuntimeError(f"PostgreSQL query failed via psycopg: {exc}") from exc

        try:
            import psycopg2  # type: ignore
            conn = psycopg2.connect(self.dsn)
            with conn.cursor() as cur:
                cur.execute(sql)
                for row in cur:
                    if row and row[0]:
                        yield str(row[0])
            conn.close()
            return
        except ImportError:
            pass
        except Exception as exc:
            raise RuntimeError(f"PostgreSQL query failed via psycopg2: {exc}") from exc

        # Attempt 2: psql CLI streaming adapter
        psql_path = shutil.which("psql")
        if psql_path:
            env = os.environ.copy()
            env["PGCONNECT_TIMEOUT"] = "5"
            cmd = [psql_path, self.dsn, "-t", "-A", "-c", sql]
            proc = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                env=env,
            )
            assert proc.stdout is not None
            for line in proc.stdout:
                val = line.strip()
                if val:
                    yield val
            proc.wait()
            if proc.returncode != 0:
                err = proc.stderr.read() if proc.stderr else "Unknown error"
                raise RuntimeError(f"psql command failed (code {proc.returncode}): {err.strip()}")
            return

        # Attempt 3: Docker fallback container
        docker_path = shutil.which("docker")
        if docker_path:
            cmd = [
                docker_path,
                "run",
                "--rm",
                "-i",
                "--net=host",
                "postgres:16-alpine",
                "psql",
                self.dsn,
                "-t",
                "-A",
                "-c",
                sql,
            ]
            proc = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
            )
            assert proc.stdout is not None
            for line in proc.stdout:
                val = line.strip()
                if val:
                    yield val
            proc.wait()
            if proc.returncode != 0:
                err = proc.stderr.read() if proc.stderr else "Unknown error"
                raise RuntimeError(f"Docker psql failed (code {proc.returncode}): {err.strip()}")
            return

        raise RuntimeError(
            "No PostgreSQL driver or CLI found. Please install psycopg2/psycopg, or ensure 'psql' / 'docker' is in PATH."
        )


class DatabaseSourceFactory:
    """Factory creating the appropriate database domain source."""

    @staticmethod
    def create(
        dsn_or_path: Optional[str] = None,
        env_file_path: Optional[Path] = None,
    ) -> BaseDatabaseSource:
        target = dsn_or_path

        # If no explicit connection provided, inspect environment and .env
        if not target:
            file_env = load_env_file(env_file_path)
            target = (
                os.environ.get("POSTGRES_DSN")
                or os.environ.get("DATABASE_URL")
                or file_env.get("POSTGRES_DSN")
                or file_env.get("DATABASE_URL")
            )
            if not target:
                sqlite_env = os.environ.get("SQLITE_PATH") or file_env.get("SQLITE_PATH")
                if sqlite_env:
                    target = sqlite_env

        if not target:
            raise ValueError(
                "No database connection specified. Provide --db <dsn> or define POSTGRES_DSN / DATABASE_URL in .env"
            )

        # Classify by schema / prefix / extension
        lower = target.lower()
        if lower.startswith("postgres://") or lower.startswith("postgresql://"):
            return PostgresDomainSource(target)
        elif lower.startswith("sqlite://"):
            clean_path = target[len("sqlite://") :]
            return SQLiteDomainSource(clean_path)
        elif lower.endswith(".db") or lower.endswith(".sqlite") or lower.endswith(".sqlite3") or os.path.exists(target):
            return SQLiteDomainSource(target)
        elif "host=" in lower or "dbname=" in lower:
            return PostgresDomainSource(target)
        else:
            # Default to Postgres if connection string contains standard parameters
            return PostgresDomainSource(target)


# ==============================================================================
# SOLID Component 4: HTTP Probe Client (Single Responsibility)
# ==============================================================================

class ProbeClient:
    """Executes resilient HTTP GET probes against prospective endpoints."""

    def __init__(self, timeout: float = DEFAULT_TIMEOUT, user_agent: str = USER_AGENT):
        self.timeout = timeout
        self.user_agent = user_agent
        self.ssl_context = ssl.create_default_context()
        self.ssl_context.check_hostname = False
        self.ssl_context.verify_mode = ssl.CERT_NONE

    def probe_url(self, url: str) -> Tuple[int, int, bytes, Dict[str, str]]:
        """
        Fetches an endpoint and returns (status_code, latency_ms, content_bytes, headers).
        """
        start_time = time.perf_counter()
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": self.user_agent,
                "Accept": "application/json, text/plain, text/markdown, */*",
                "Connection": "close",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout, context=self.ssl_context) as resp:
                elapsed_ms = int((time.perf_counter() - start_time) * 1000)
                status_code = resp.status
                body = resp.read(256 * 1024)
                headers = {k.lower(): v for k, v in resp.headers.items()}
                return status_code, elapsed_ms, body, headers
        except urllib.error.HTTPError as exc:
            elapsed_ms = int((time.perf_counter() - start_time) * 1000)
            body = b""
            try:
                body = exc.read(8 * 1024)
            except Exception:
                pass
            return exc.code, elapsed_ms, body, {}
        except Exception:
            elapsed_ms = int((time.perf_counter() - start_time) * 1000)
            return 0, elapsed_ms, b"", {}


# ==============================================================================
# SOLID Component 5: Manifest & Content Analyzer (Single Responsibility)
# ==============================================================================

class ManifestAnalyzer:
    """Parses and validates MCP server cards, AI catalogs, and llms.txt."""

    @staticmethod
    def analyze_payload(
        artifact_type: str,
        url: str,
        status_code: int,
        latency_ms: int,
        body: bytes,
        headers: Dict[str, str],
    ) -> Optional[DiscoveredArtifact]:
        if status_code != 200 or not body:
            return None

        content_length = len(body)
        raw_preview = body[:200].decode("utf-8", errors="replace").strip()

        # Case 1: llms.txt or markdown documentation
        if artifact_type in {"llms_txt", "llms_full_txt"}:
            text = body.decode("utf-8", errors="replace")
            if len(text.strip()) > 20 and not text.strip().startswith("<!DOCTYPE html"):
                return DiscoveredArtifact(
                    artifact_type=artifact_type,
                    url=url,
                    status_code=status_code,
                    latency_ms=latency_ms,
                    content_length=content_length,
                    raw_preview=raw_preview,
                )
            return None

        # Case 2: JSON manifests (server-card.json, ai-catalog.json, mcp endpoint)
        try:
            payload = json.loads(body.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return None

        if not isinstance(payload, dict):
            return None

        tools_count = None
        server_name = None
        description = None
        protocol_version = None

        if artifact_type == "mcp_server_card":
            server_name = payload.get("name") or payload.get("title")
            description = payload.get("description")
            protocol_version = str(payload.get("protocol_version") or payload.get("version") or "")
            tools = payload.get("tools")
            if isinstance(tools, list):
                tools_count = len(tools)
            elif isinstance(payload.get("capabilities", {}).get("tools"), dict):
                tools_count = 1

        elif artifact_type == "ai_catalog":
            server_name = payload.get("name") or payload.get("title")
            description = payload.get("description")
            services = payload.get("services") or payload.get("tools") or payload.get("endpoints")
            if isinstance(services, list):
                tools_count = len(services)
            elif isinstance(services, dict):
                tools_count = len(services)

        elif artifact_type == "mcp_endpoint":
            server_name = payload.get("name")
            description = payload.get("description")
            if "tools" in payload and isinstance(payload["tools"], list):
                tools_count = len(payload["tools"])

        return DiscoveredArtifact(
            artifact_type=artifact_type,
            url=url,
            status_code=status_code,
            latency_ms=latency_ms,
            content_length=content_length,
            valid_json=True,
            tools_count=tools_count,
            server_name=str(server_name) if server_name else None,
            description=str(description)[:255] if description else None,
            protocol_version=protocol_version if protocol_version else None,
            raw_preview=raw_preview,
        )


# ==============================================================================
# SOLID Component 6: Domain Inspector (Single Responsibility)
# ==============================================================================

class DomainInspector:
    """Coordinates probe execution for a single domain across prospective endpoints."""

    def __init__(self, client: ProbeClient, analyzer: ManifestAnalyzer):
        self.client = client
        self.analyzer = analyzer

    def inspect(self, domain: str) -> DomainCrawlResult:
        now_iso = datetime.now(timezone.utc).isoformat()
        artifacts: List[DiscoveredArtifact] = []
        latencies: List[int] = []

        schemes = ["https"]

        for path, artifact_type in PROBE_PATHS:
            for scheme in schemes:
                url = f"{scheme}://{domain}{path}"
                status_code, latency_ms, body, headers = self.client.probe_url(url)
                if status_code == 200:
                    artifact = self.analyzer.analyze_payload(
                        artifact_type, url, status_code, latency_ms, body, headers
                    )
                    if artifact:
                        artifacts.append(artifact)
                        latencies.append(latency_ms)
                        break

        has_ai = len(artifacts) > 0
        min_lat = min(latencies) if latencies else None

        primary_mcp = None
        primary_catalog = None
        primary_llms = None
        total_tools = 0

        for a in artifacts:
            if a.artifact_type in {"mcp_server_card", "mcp_endpoint"} and not primary_mcp:
                primary_mcp = a.url
            if a.artifact_type == "ai_catalog" and not primary_catalog:
                primary_catalog = a.url
            if a.artifact_type in {"llms_txt", "llms_full_txt"} and not primary_llms:
                primary_llms = a.url
            if a.tools_count:
                total_tools += a.tools_count

        return DomainCrawlResult(
            domain=domain,
            inspected_at=now_iso,
            has_ai_presence=has_ai,
            artifacts=artifacts,
            min_latency_ms=min_lat,
            primary_mcp_url=primary_mcp,
            primary_catalog_url=primary_catalog,
            primary_llms_url=primary_llms,
            total_tools_declared=total_tools,
        )


# ==============================================================================
# SOLID Component 7: Batch Output Writer & Checkpointer
# ==============================================================================

class BatchWriter:
    """Manages writing structured batch files and durable checkpoint state."""

    def __init__(self, output_dir: Path, checkpoint_file: Optional[Path] = None):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.checkpoint_file = checkpoint_file or (output_dir / ".checkpoint.json")

        self.discovered_file = self.output_dir / "discovered_mcp_servers.jsonl"
        self.indexing_batch_json = self.output_dir / "domainscope_indexing_batch.json"
        self.indexing_batch_tsv = self.output_dir / "domainscope_indexing_batch.tsv"
        self.summary_file = self.output_dir / "crawl_summary.json"

        self.discovered_count = 0
        self.total_processed = 0

    def load_checkpoint(self) -> Set[str]:
        if self.checkpoint_file.exists():
            try:
                data = json.loads(self.checkpoint_file.read_text(encoding="utf-8"))
                return set(data.get("completed_domains", []))
            except Exception:
                pass
        return set()

    def record_discovered(self, result: DomainCrawlResult) -> None:
        self.discovered_count += 1
        with self.discovered_file.open("a", encoding="utf-8") as f:
            data = asdict(result)
            f.write(json.dumps(data) + "\n")

    def save_checkpoint(self, completed_domains: Set[str], last_index: int) -> None:
        tmp_file = self.checkpoint_file.with_suffix(".tmp")
        payload = {
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "total_completed": len(completed_domains),
            "last_index": last_index,
            "discovered_count": self.discovered_count,
            "completed_domains": list(completed_domains),
        }
        tmp_file.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        tmp_file.replace(self.checkpoint_file)

    def finalize_batches(
        self,
        all_results: List[DomainCrawlResult],
        total_scanned: int,
        elapsed_seconds: float,
    ) -> None:
        discovered = [r for r in all_results if r.has_ai_presence]

        # 1. DomainScope Indexing Batch (JSON format for bulk ingestion API)
        batch_payload = {
            "batch_id": f"mcp_batch_{int(time.time())}",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "total_domains": len(discovered),
            "domains": [
                {
                    "domain": r.domain,
                    "has_mcp": r.primary_mcp_url is not None,
                    "has_ai_catalog": r.primary_catalog_url is not None,
                    "has_llms_txt": r.primary_llms_url is not None,
                    "mcp_endpoint": r.primary_mcp_url,
                    "ai_catalog_url": r.primary_catalog_url,
                    "llms_url": r.primary_llms_url,
                    "tools_count": r.total_tools_declared,
                    "latency_ms": r.min_latency_ms,
                    "inspected_at": r.inspected_at,
                    "artifacts": [asdict(a) for a in r.artifacts],
                }
                for r in discovered
            ],
        }
        self.indexing_batch_json.write_text(json.dumps(batch_payload, indent=2), encoding="utf-8")

        # 2. DomainScope Indexing Batch (TSV format for high-throughput pipeline)
        with self.indexing_batch_tsv.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter="\t")
            writer.writerow([
                "domain",
                "has_mcp",
                "has_ai_catalog",
                "has_llms_txt",
                "tools_count",
                "min_latency_ms",
                "primary_manifest",
            ])
            for r in discovered:
                primary = r.primary_mcp_url or r.primary_catalog_url or r.primary_llms_url or ""
                writer.writerow([
                    r.domain,
                    "1" if r.primary_mcp_url else "0",
                    "1" if r.primary_catalog_url else "0",
                    "1" if r.primary_llms_url else "0",
                    r.total_tools_declared,
                    r.min_latency_ms or 0,
                    primary,
                ])

        # 3. Execution Summary Report
        latencies = [r.min_latency_ms for r in discovered if r.min_latency_ms is not None]
        p50 = sorted(latencies)[len(latencies) // 2] if latencies else 0
        p95 = sorted(latencies)[int(len(latencies) * 0.95)] if latencies else 0

        summary = {
            "status": "completed",
            "total_domains_scanned": total_scanned,
            "total_ai_domains_discovered": len(discovered),
            "hit_rate_percentage": round((len(discovered) / total_scanned * 100), 2) if total_scanned else 0,
            "elapsed_seconds": round(elapsed_seconds, 2),
            "throughput_domains_per_second": round(total_scanned / max(0.1, elapsed_seconds), 1),
            "latency_p50_ms": p50,
            "latency_p95_ms": p95,
            "output_artifacts": {
                "discovered_jsonl": str(self.discovered_file),
                "indexing_batch_json": str(self.indexing_batch_json),
                "indexing_batch_tsv": str(self.indexing_batch_tsv),
            },
        }
        self.summary_file.write_text(json.dumps(summary, indent=2), encoding="utf-8")


# ==============================================================================
# SOLID Component 8: Orchestrator & CLI Runner
# ==============================================================================

class CrawlerOrchestrator:
    """Coordinates batch domain ingestion, concurrent workers, and graceful shutdown."""

    def __init__(
        self,
        domains: List[str],
        writer: BatchWriter,
        concurrency: int = DEFAULT_CONCURRENCY,
        timeout: float = DEFAULT_TIMEOUT,
    ):
        self.domains = domains
        self.writer = writer
        self.concurrency = concurrency
        self.timeout = timeout
        self.shutdown_requested = False

        signal.signal(signal.SIGINT, self._handle_signal)
        signal.signal(signal.SIGTERM, self._handle_signal)

    def _handle_signal(self, signum, frame):
        print(f"\n[!] Signal {signum} received. Finishing current workers and saving checkpoint...")
        self.shutdown_requested = True

    def run(self) -> Tuple[int, int]:
        completed_set = self.writer.load_checkpoint()
        unprocessed = [(idx, d) for idx, d in enumerate(self.domains) if d not in completed_set]

        print(f"[*] Starting MCP Catalog Crawler:")
        print(f"    Total input domains:      {len(self.domains)}")
        print(f"    Previously completed:     {len(completed_set)}")
        print(f"    Pending processing:       {len(unprocessed)}")
        print(f"    Concurrency:              {self.concurrency} workers")
        print(f"    Probe timeout:            {self.timeout}s per request")
        print(f"    Output Directory:         {self.writer.output_dir}")

        client = ProbeClient(timeout=self.timeout)
        analyzer = ManifestAnalyzer()
        inspector = DomainInspector(client, analyzer)

        start_time = time.time()
        discovered_results: List[DomainCrawlResult] = []
        processed_in_run = 0

        with ThreadPoolExecutor(max_workers=self.concurrency) as executor:
            future_to_meta = {
                executor.submit(inspector.inspect, domain): (idx, domain)
                for idx, domain in unprocessed
            }

            for future in as_completed(future_to_meta):
                if self.shutdown_requested:
                    break

                idx, domain = future_to_meta[future]
                try:
                    result = future.result()
                    completed_set.add(domain)
                    processed_in_run += 1

                    if result.has_ai_presence:
                        discovered_results.append(result)
                        self.writer.record_discovered(result)
                        arts = [a.artifact_type for a in result.artifacts]
                        print(f"  [+] Discovered: {domain} -> {arts} (lat: {result.min_latency_ms}ms, tools: {result.total_tools_declared})")

                    if processed_in_run % 100 == 0:
                        self.writer.save_checkpoint(completed_set, idx)
                        sys.stdout.write(f"\r    Progress: {processed_in_run}/{len(unprocessed)} domains inspected ({len(discovered_results)} discovered)...")
                        sys.stdout.flush()

                except Exception as exc:
                    print(f"  [-] Error inspecting {domain}: {exc}", file=sys.stderr)
                    completed_set.add(domain)

        elapsed = time.time() - start_time
        self.writer.save_checkpoint(completed_set, len(self.domains))
        self.writer.finalize_batches(discovered_results, processed_in_run, elapsed)

        print(f"\n[✓] Crawl complete in {elapsed:.1f}s.")
        print(f"    Domains Inspected:   {processed_in_run}")
        print(f"    Discovered AI/MCP:   {len(discovered_results)}")
        print(f"    Indexing batch TSV:  {self.writer.indexing_batch_tsv}")
        print(f"    Indexing batch JSON: {self.writer.indexing_batch_json}")
        print(f"    Summary Report:      {self.writer.summary_file}")

        return processed_in_run, len(discovered_results)


# ==============================================================================
# CLI Entrypoint & Domain Stream Loader
# ==============================================================================

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="DomainScope MCP & AI Manifest Crawler and Batch Processing Pipeline."
    )
    # Database input options
    db_group = parser.add_argument_group("Database Input Options")
    db_group.add_argument(
        "--from-db",
        action="store_true",
        help="Pull input domains directly from database (reads POSTGRES_DSN or DATABASE_URL from .env/env).",
    )
    db_group.add_argument(
        "--db",
        help="Database connection DSN or path (e.g. postgres://... or sqlite:///path/to/db.sqlite or /path/to/db.db).",
    )
    db_group.add_argument(
        "--db-query",
        default=None,
        help="Custom SQL query to select domain names (default: 'SELECT name FROM domains').",
    )
    db_group.add_argument(
        "--db-limit",
        type=int,
        default=None,
        help="Maximum number of rows to select from database.",
    )
    db_group.add_argument(
        "--db-offset",
        type=int,
        default=None,
        help="Pagination offset for database select query.",
    )

    # File / CLI input options
    input_group = parser.add_argument_group("File & CLI Input Options")
    input_group.add_argument(
        "--input",
        "-i",
        help="Path to domain list file (one domain per line or CSV/TSV).",
    )
    input_group.add_argument(
        "--domains",
        "-d",
        nargs="+",
        help="Space-separated list of individual domains to crawl.",
    )

    # Execution & Output options
    parser.add_argument(
        "--output-dir",
        "-o",
        default="data/mcp_batches/batch_" + datetime.now().strftime("%Y%m%d_%H%M%S"),
        help="Output directory for generated batch files.",
    )
    parser.add_argument(
        "--limit",
        "-l",
        type=int,
        default=None,
        help="Maximum total domains to inspect in this crawl run.",
    )
    parser.add_argument(
        "--concurrency",
        "-c",
        type=int,
        default=DEFAULT_CONCURRENCY,
        help=f"Concurrent worker threads (default: {DEFAULT_CONCURRENCY}).",
    )
    parser.add_argument(
        "--timeout",
        "-t",
        type=float,
        default=DEFAULT_TIMEOUT,
        help=f"Timeout in seconds per probe (default: {DEFAULT_TIMEOUT}s).",
    )
    return parser.parse_args()


def load_domains(args: argparse.Namespace) -> List[str]:
    raw_domains: List[str] = []
    normalizer = DomainNormalizer()
    seen: Set[str] = set()
    cleaned: List[str] = []

    # Case 1: Ingest from Database
    if args.from_db or args.db:
        print(f"[*] Ingesting domains from database...")
        db_source = DatabaseSourceFactory.create(args.db)
        count = 0
        for raw in db_source.stream_domains(
            query=args.db_query,
            limit=args.db_limit or args.limit,
            offset=args.db_offset,
        ):
            norm = normalizer.normalize(raw)
            if norm and norm not in seen:
                seen.add(norm)
                cleaned.append(norm)
                count += 1
                if args.limit and len(cleaned) >= args.limit:
                    break
        print(f"    Selected {count} unique domains from database.")
        return cleaned

    # Case 2: Individual domains passed via CLI
    if args.domains:
        raw_domains.extend(args.domains)

    # Case 3: Ingest from file
    if args.input:
        in_path = Path(args.input)
        if not in_path.exists():
            raise FileNotFoundError(f"Input file not found: {in_path}")
        with in_path.open("r", encoding="utf-8") as f:
            for line in f:
                item = line.strip()
                if item and not item.startswith("#"):
                    if "\t" in item:
                        item = item.split("\t")[0]
                    elif "," in item:
                        item = item.split(",")[0]
                    raw_domains.append(item)

    # Case 4: Standard fallback to STDIN if piped
    if not raw_domains and not sys.stdin.isatty():
        for line in sys.stdin:
            item = line.strip()
            if item:
                raw_domains.append(item)

    # Normalize and deduplicate preserving order
    for item in raw_domains:
        norm = normalizer.normalize(item)
        if norm and norm not in seen:
            seen.add(norm)
            cleaned.append(norm)
            if args.limit and len(cleaned) >= args.limit:
                break

    return cleaned


def main() -> int:
    args = parse_args()
    domains = load_domains(args)

    if not domains:
        print("[!] No domains provided. Use --from-db, --db, --input, --domains, or pipe domains via STDIN.")
        print("    Example (DB):   python3 scripts/mcp_catalog_crawler.py --from-db --limit 100")
        print("    Example (CLI):  python3 scripts/mcp_catalog_crawler.py --domains stripe.com huggingface.co cloudflare.com")
        return 1

    writer = BatchWriter(output_dir=Path(args.output_dir))
    orchestrator = CrawlerOrchestrator(
        domains=domains,
        writer=writer,
        concurrency=args.concurrency,
        timeout=args.timeout,
    )
    orchestrator.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
