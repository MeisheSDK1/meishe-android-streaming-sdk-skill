import sys
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from coverage_summary import build_coverage_summary, coverage_artifact_gaps


class CoverageSummaryTest(unittest.TestCase):
    def test_api_coverage_states_partition_exact_members(self):
        summary = build_coverage_summary(SKILL_DIR)

        self.assertEqual(
            summary["api"]["member_count"],
            sum(summary["api"]["coverage"].values()),
        )

    def test_passed_and_partial_only_blueprints_partition_evidence(self):
        runtime = build_coverage_summary(SKILL_DIR)["runtime"]

        self.assertEqual(
            runtime["blueprints_with_evidence_count"],
            runtime["blueprints_with_passed_run_count"]
            + runtime["blueprints_with_partial_only_count"],
        )
        self.assertEqual(0, runtime["blueprints_with_partial_only_count"])
        self.assertEqual(
            runtime["blueprints_with_evidence_count"],
            runtime["blueprints_with_passed_run_count"],
        )

    def test_generated_coverage_artifacts_are_current(self):
        self.assertEqual([], coverage_artifact_gaps(SKILL_DIR))


if __name__ == "__main__":
    unittest.main()
