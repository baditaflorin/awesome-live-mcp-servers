#!/usr/bin/env python3
"""
scripts/test_mcp_catalog_crawler.py
Unit tests for DomainScope MCP & AI Manifest Crawler and Batch Pipeline.
"""

import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock

from scripts.mcp_catalog_crawler import (
    BatchWriter,
    DiscoveredArtifact,
    DomainCrawlResult,
    DomainInspector,
    DomainNormalizer,
    ManifestAnalyzer,
    ProbeClient,
)


class TestDomainNormalizer(unittest.TestCase):
    def test_clean_domains(self):
        self.assertEqual(DomainNormalizer.normalize("example.com"), "example.com")
        self.assertEqual(DomainNormalizer.normalize("  EXAMPLE.COM  "), "example.com")
        self.assertEqual(DomainNormalizer.normalize("https://sub.domain.org/path/test?q=1"), "sub.domain.org")
        self.assertEqual(DomainNormalizer.normalize("http://user:pass@host.io:8080/"), "host.io")
        self.assertEqual(DomainNormalizer.normalize("foo.co.uk."), "foo.co.uk")

    def test_invalid_domains(self):
        self.assertIsNone(DomainNormalizer.normalize(""))
        self.assertIsNone(DomainNormalizer.normalize("   "))
        self.assertIsNone(DomainNormalizer.normalize("localhost"))
        self.assertIsNone(DomainNormalizer.normalize("invalid string with space"))


class TestManifestAnalyzer(unittest.TestCase):
    def test_mcp_server_card_parsing(self):
        card = {
            "name": "Cloudflare MCP Server",
            "description": "Cloudflare worker tool execution",
            "protocol_version": "2024-11-05",
            "tools": [
                {"name": "fetch_worker", "description": "Fetches worker"},
                {"name": "deploy_worker", "description": "Deploys worker"},
            ],
        }
        raw_bytes = json.dumps(card).encode("utf-8")
        artifact = ManifestAnalyzer.analyze_payload(
            artifact_type="mcp_server_card",
            url="https://cloudflare.com/.well-known/mcp/server-card.json",
            status_code=200,
            latency_ms=150,
            body=raw_bytes,
            headers={"content-type": "application/json"},
        )
        self.assertIsNotNone(artifact)
        self.assertTrue(artifact.valid_json)
        self.assertEqual(artifact.server_name, "Cloudflare MCP Server")
        self.assertEqual(artifact.tools_count, 2)
        self.assertEqual(artifact.protocol_version, "2024-11-05")

    def test_ai_catalog_parsing(self):
        catalog = {
            "title": "Hugging Face AI Catalog",
            "description": "Hosted models and tools catalog",
            "services": ["model-inference", "embeddings-generator", "dataset-reader"],
        }
        raw_bytes = json.dumps(catalog).encode("utf-8")
        artifact = ManifestAnalyzer.analyze_payload(
            artifact_type="ai_catalog",
            url="https://huggingface.co/.well-known/ai-catalog.json",
            status_code=200,
            latency_ms=120,
            body=raw_bytes,
            headers={"content-type": "application/json"},
        )
        self.assertIsNotNone(artifact)
        self.assertEqual(artifact.server_name, "Hugging Face AI Catalog")
        self.assertEqual(artifact.tools_count, 3)

    def test_llms_txt_parsing(self):
        text = b"# LLMS.txt Documentation\n\nThis API provides standard LLM context and tool calls."
        artifact = ManifestAnalyzer.analyze_payload(
            artifact_type="llms_txt",
            url="https://example.com/llms.txt",
            status_code=200,
            latency_ms=80,
            body=text,
            headers={"content-type": "text/plain"},
        )
        self.assertIsNotNone(artifact)
        self.assertEqual(artifact.artifact_type, "llms_txt")

    def test_html_error_rejected_as_llms_txt(self):
        html = b"<!DOCTYPE html><html><body>404 Not Found</body></html>"
        artifact = ManifestAnalyzer.analyze_payload(
            artifact_type="llms_txt",
            url="https://example.com/llms.txt",
            status_code=200,
            latency_ms=80,
            body=html,
            headers={"content-type": "text/html"},
        )
        self.assertIsNone(artifact)

    def test_invalid_json_handled_safely(self):
        corrupted = b"{broken json: true"
        artifact = ManifestAnalyzer.analyze_payload(
            artifact_type="mcp_server_card",
            url="https://example.com/.well-known/mcp/server-card.json",
            status_code=200,
            latency_ms=80,
            body=corrupted,
            headers={"content-type": "application/json"},
        )
        self.assertIsNone(artifact)


class TestBatchWriterAndCheckpoints(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_checkpoint_lifecycle(self):
        writer = BatchWriter(output_dir=self.test_dir)
        completed = writer.load_checkpoint()
        self.assertEqual(len(completed), 0)

        # Save checkpoint
        domains = {"a.com", "b.com"}
        writer.save_checkpoint(domains, 2)

        # Reload
        reloaded = writer.load_checkpoint()
        self.assertEqual(reloaded, domains)

    def test_batch_file_generation(self):
        writer = BatchWriter(output_dir=self.test_dir)
        art = DiscoveredArtifact(
            artifact_type="mcp_server_card",
            url="https://test.ai/.well-known/mcp/server-card.json",
            status_code=200,
            latency_ms=120,
            content_length=500,
            valid_json=True,
            tools_count=4,
            server_name="Test MCP",
        )
        res = DomainCrawlResult(
            domain="test.ai",
            inspected_at="2026-09-16T11:00:00Z",
            has_ai_presence=True,
            artifacts=[art],
            min_latency_ms=120,
            primary_mcp_url=art.url,
            total_tools_declared=4,
        )

        writer.record_discovered(res)
        writer.finalize_batches(all_results=[res], total_scanned=1, elapsed_seconds=0.5)

        # Verify JSONL
        self.assertTrue(writer.discovered_file.exists())
        lines = writer.discovered_file.read_text().strip().splitlines()
        self.assertEqual(len(lines), 1)

        # Verify Indexing Batch JSON
        self.assertTrue(writer.indexing_batch_json.exists())
        batch_data = json.loads(writer.indexing_batch_json.read_text())
        self.assertEqual(batch_data["total_domains"], 1)
        self.assertEqual(batch_data["domains"][0]["domain"], "test.ai")

        # Verify Indexing Batch TSV
        self.assertTrue(writer.indexing_batch_tsv.exists())
        tsv_content = writer.indexing_batch_tsv.read_text()
        self.assertIn("test.ai\t1\t0\t0\t4\t120", tsv_content)

        # Verify Summary Report
        self.assertTrue(writer.summary_file.exists())
        summary = json.loads(writer.summary_file.read_text())
        self.assertEqual(summary["total_domains_scanned"], 1)
        self.assertEqual(summary["total_ai_domains_discovered"], 1)


class TestDomainInspectorMocked(unittest.TestCase):
    def test_inspector_aggregates_artifacts(self):
        client = MagicMock(spec=ProbeClient)
        # Returns 200 for mcp server card, 404 for others
        def mock_probe(url):
            if "server-card.json" in url:
                return 200, 110, b'{"name": "Mock", "tools": [{"name": "t1"}]}', {"content-type": "application/json"}
            return 404, 50, b"", {}

        client.probe_url.side_effect = mock_probe
        analyzer = ManifestAnalyzer()
        inspector = DomainInspector(client, analyzer)

        result = inspector.inspect("mocktest.org")
        self.assertTrue(result.has_ai_presence)
        self.assertEqual(result.domain, "mocktest.org")
        self.assertEqual(result.primary_mcp_url, "https://mocktest.org/.well-known/mcp/server-card.json")
        self.assertEqual(result.total_tools_declared, 1)
        self.assertEqual(result.min_latency_ms, 110)


if __name__ == "__main__":
    unittest.main()
