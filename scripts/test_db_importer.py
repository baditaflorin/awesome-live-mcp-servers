import unittest
from unittest import mock

import db_importer
import mcp_card_importer as imp


def rec(domain, reachable=True):
    return dict(domain=domain, identifier=f"https://{domain}/.well-known/mcp/server-card.json",
                server_card_url=f"https://{domain}/.well-known/mcp/server-card.json", server_name="Acme",
                server_version="1", server_title="", server_description="it's fine", website_url="",
                protocol_versions=["2025-06-18"], mcp_endpoint_reachable=reachable, endpoint="", transport="",
                tools_count=0)


class DatabaseImporterTest(unittest.TestCase):
    def test_only_validated_domains_are_written(self):
        writes = []
        d = db_importer.DatabaseImporter("postgres://x", workers=2)
        d._apply = writes.append
        with mock.patch.object(imp, "verify", side_effect=lambda dom: rec(dom) if dom == "good.com" else None):
            written, checked = d.import_domains(["good.com", "html-soft200.com", "good.com"])
        self.assertEqual((written, checked), (1, 2))
        self.assertEqual(len(writes), 1)
        self.assertIn("good.com", writes[0])
        self.assertNotIn("html-soft200.com", writes[0])
        self.assertIn("it''s fine", writes[0])  # SQL-escaped
        self.assertIn("ON CONFLICT (domain_id, identifier) DO UPDATE", writes[0])

    def test_nothing_validated_means_no_write(self):
        d = db_importer.DatabaseImporter("postgres://x")
        d._apply = mock.Mock()
        with mock.patch.object(imp, "verify", return_value=None):
            self.assertEqual(d.import_domains(["a.com"]), (0, 1))
        d._apply.assert_not_called()

    def test_parse_card_rejects_non_cards(self):
        self.assertIsNone(imp.parse_card({"error": "not found"}))
        self.assertIsNone(imp.parse_card({"name": "just an api", "version": "1"}))
        self.assertIsNotNone(imp.parse_card({"serverInfo": {"name": "x"}, "endpoint": "https://x/mcp"}))


if __name__ == "__main__":
    unittest.main()
