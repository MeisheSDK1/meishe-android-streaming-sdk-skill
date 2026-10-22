"""Regression tests for CLI UTF-8 stdout/stderr and explicit fallback marking."""

import json
import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SEARCH_SCRIPT = SCRIPT_DIR / "search_skill_index.py"


def run_search(*args):
    return subprocess.run(
        [sys.executable, "-B", str(SEARCH_SCRIPT), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=60,
    )


class CliUtf8StdioTest(unittest.TestCase):
    def test_text_query_output_is_utf8(self):
        result = run_search("字幕")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("字幕", result.stdout)

    def test_json_query_output_is_utf8(self):
        result = run_search("字幕", "--json")
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertIsInstance(payload, list)
        self.assertGreater(len(payload), 0)

    def test_fallback_is_explicitly_marked(self):
        text_result = run_search("zzz-nonsense-no-match")
        self.assertEqual(text_result.returncode, 0, text_result.stderr)
        self.assertIn(
            "No exact matches; showing fallback entries below.", text_result.stdout
        )
        json_result = run_search("zzz-nonsense-no-match", "--json")
        self.assertEqual(json_result.returncode, 0, json_result.stderr)
        payload = json.loads(json_result.stdout)
        self.assertGreater(len(payload), 0)
        self.assertTrue(all(entry.get("fallback") is True for entry in payload))


if __name__ == "__main__":
    unittest.main()