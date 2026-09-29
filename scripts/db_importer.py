"""
db_importer.py — write crawler discoveries BACK into DomainScope Postgres.

DomainScope's database is the source of truth. The crawler used to emit only files
(domainscope_indexing_batch.json) that nothing ingested, so 3,000+ discovered servers never
reached the database. This module strictly validates each discovered domain (server card +
live MCP initialize handshake, see mcp_card_importer.py) and upserts it into
domain_mcp_servers / domain_ai_catalog in one transaction.
"""
import concurrent.futures as cf
import shutil
import subprocess
from typing import List, Tuple

import mcp_card_importer as imp


class DatabaseImporter:
    def __init__(self, dsn: str, workers: int = 16):
        self.dsn = dsn
        self.workers = workers

    def _apply(self, sql: str) -> None:
        try:  # native driver first
            import psycopg  # type: ignore
            with psycopg.connect(self.dsn) as conn:
                conn.execute(sql)
            return
        except ImportError:
            pass
        try:
            import psycopg2  # type: ignore
            conn = psycopg2.connect(self.dsn)
            try:
                with conn, conn.cursor() as cur:
                    cur.execute(sql)
            finally:
                conn.close()
            return
        except ImportError:
            pass
        psql = shutil.which("psql")
        if not psql:
            raise RuntimeError("no psycopg/psycopg2/psql available to write to Postgres")
        subprocess.run([psql, self.dsn, "-v", "ON_ERROR_STOP=1", "-X", "-q", "-f", "-"],
                       input=sql, text=True, check=True, capture_output=True)

    def import_domains(self, domains: List[str]) -> Tuple[int, int]:
        """Validate and upsert. Returns (validated_and_written, checked)."""
        domains = sorted(set(domains))
        if not domains:
            return 0, 0

        def safe(d):
            try:
                return imp.verify(d)
            except Exception:
                return None

        with cf.ThreadPoolExecutor(self.workers) as ex:
            recs = [r for r in ex.map(safe, domains) if r]
        if recs:
            self._apply(imp.to_sql(recs))
        return len(recs), len(domains)
