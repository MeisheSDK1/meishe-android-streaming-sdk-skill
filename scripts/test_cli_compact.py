"""Regression tests for --compact routing output that keeps routing fields."""

import json
import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SEARCH_SCRIPT = SCRIPT_DIR / "search_skill_index.py"
COMPOSE_SCRIPT = SCRIPT_DIR / "compose_modules.py"


def run(script, *args):
    return subprocess.run(
        [sys.executable, "-B", str(script), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=120,
    )


class SearchCompactTest(unittest.TestCase):
    def test_text_keeps_routing_fields_and_truncates_ids(self):
        result = run(SEARCH_SCRIPT, "--compact", "caption")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("captions-stickers", result.stdout)
        self.assertIn("resources:", result.stdout)
        self.assertIn("modules:", result.stdout)
        self.assertIn("blueprints:", result.stdout)
        self.assertIn("simple code ids:", result.stdout)
        self.assertNotIn("java.caption.add", result.stdout)

    def test_json_reports_total_and_truncates_ids(self):
        result = run(SEARCH_SCRIPT, "--compact", "--json", "caption")
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertGreater(len(payload), 0)
        entry = payload[0]
        self.assertIn("simple_code_ids", entry)
        self.assertIn("simple_code_ids_total", entry)
        self.assertLessEqual(len(entry["simple_code_ids"]), 20)
        self.assertGreaterEqual(
            entry["simple_code_ids_total"], len(entry["simple_code_ids"])
        )

    def test_default_json_stays_full(self):
        result = run(SEARCH_SCRIPT, "--json", "caption")
        self.assertEqual(result.returncode, 0, result.stderr)
        entry = json.loads(result.stdout)[0]
        self.assertNotIn("simple_code_ids_total", entry)


class ComposeCompactTest(unittest.TestCase):
    def test_text_omits_full_id_and_call_order(self):
        result = run(
            COMPOSE_SCRIPT, "--compact", "--query", "capture camera", "--mode", "new-app"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Resource keys:", result.stdout)
        self.assertIn("Simple code ids:", result.stdout)
        self.assertNotIn("Call order:", result.stdout)

    def test_json_reports_counts_and_drops_units(self):
        result = run(
            COMPOSE_SCRIPT,
            "--compact",
            "--query",
            "capture camera",
            "--mode",
            "new-app",
            "--json",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertIn("simple_code_ids_total", payload)
        self.assertIn("simple_code_units_count", payload)
        self.assertIn("call_order_count", payload)
        self.assertNotIn("simple_code_units", payload)
        self.assertNotIn("call_order", payload)


if __name__ == "__main__":
    unittest.main()