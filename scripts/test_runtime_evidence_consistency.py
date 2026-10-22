import json
import sys
import unittest
from pathlib import Path


SCRIPT_DIRECTORY = Path(__file__).resolve().parent
SKILL_DIRECTORY = SCRIPT_DIRECTORY.parent
REFERENCE_DIRECTORY = SKILL_DIRECTORY / "references"
sys.path.insert(0, str(SCRIPT_DIRECTORY))

import validate_lookup_cases


def load_json(filename):
    return json.loads((REFERENCE_DIRECTORY / filename).read_text(encoding="utf-8"))


class RuntimeEvidenceConsistencyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runtime_matrix = load_json("runtime-verification-matrix.json")
        cls.module_registry = load_json("sdk-module-registry.json")
        cls.coverage_summary = load_json("coverage-summary.json")
        cls.runtime_document = (
            REFERENCE_DIRECTORY / "runtime-verification.md"
        ).read_text(encoding="utf-8")

        cls.registered_blueprints = {
            blueprint["id"] for blueprint in cls.module_registry["blueprints"]
        }
        cls.passed_blueprints = {
            run["blueprint_id"]
            for run in cls.runtime_matrix["runs"]
            if run.get("runtime_result") == "passed"
        }
        cls.registered_features = {
            feature["feature"]
            for feature in cls.module_registry["demo_feature_coverage"]
        }
        cls.verified_features = {
            feature
            for run in cls.runtime_matrix["runs"]
            if run.get("runtime_result") in {"passed", "partial"}
            for feature in run.get("verified_features", [])
        }

    def test_runtime_counts_match_generated_coverage_summary(self):
        runtime_summary = self.coverage_summary["runtime"]
        self.assertEqual(
            len(self.passed_blueprints),
            runtime_summary["blueprints_with_passed_run_count"],
        )
        self.assertEqual(
            len(self.verified_features),
            runtime_summary["verified_feature_count"],
        )

    def test_runtime_document_uses_matrix_date_and_scope(self):
        verification_date = self.runtime_matrix["verification_date"]
        self.assertIn(
            f"Latest recorded run date: `{verification_date}`",
            self.runtime_document,
        )
        self.assertIn(
            "new-app blueprints and incremental/api-only host integration",
            self.runtime_matrix["scope"],
        )

    def test_runtime_document_reports_exact_blueprint_scope(self):
        missing_blueprints = sorted(
            self.registered_blueprints - self.passed_blueprints
        )
        expected_statement = (
            f"Physical-device evidence covers {len(self.passed_blueprints)} of "
            f"{len(self.registered_blueprints)} registered blueprints. "
            f"The missing blueprint is `{missing_blueprints[0]}`"
        )
        self.assertEqual(["asset-center-demo"], missing_blueprints)
        self.assertIn(expected_statement, self.runtime_document)

    def test_runtime_document_reports_exact_feature_scope(self):
        missing_features = sorted(
            self.registered_features - self.verified_features
        )
        expected_statement = (
            f"Runtime evidence covers {len(self.verified_features)} of "
            f"{len(self.registered_features)} registered Demo features. "
            f"The missing features are `{missing_features[0]}` and "
            f"`{missing_features[1]}`."
        )
        self.assertEqual(["edit-view", "presenter"], missing_features)
        self.assertIn(expected_statement, self.runtime_document)

    def test_runtime_matrix_summary_matches_recorded_runs(self):
        unverified_scope = " ".join(self.runtime_matrix["unverified_scope"])
        self.assertIn(
            "Eight of nine app blueprints have at least one passed "
            "physical-device run",
            unverified_scope,
        )
        self.assertIn(
            "asset-center-demo still requires a physical-device run",
            unverified_scope,
        )
        self.assertIn(
            "60 of 62 registered Demo features; edit-view and presenter "
            "remain unverified",
            unverified_scope,
        )
        self.assertNotIn(
            "All nine app blueprints now have at least one passed "
            "physical-device run",
            unverified_scope,
        )

    def test_runtime_document_reports_current_java_unit_count(self):
        java_unit_count = self.coverage_summary["simple_code"]["kinds"][
            "java_unit"
        ]
        self.assertEqual(241, java_unit_count)
        self.assertIn(
            f"Strict knowledge compilation covers all {java_unit_count} "
            "`java_unit` entries",
            self.runtime_document,
        )

    def test_runtime_document_reports_current_lookup_suite(self):
        exact_count = len(validate_lookup_cases.EXACT_API_QUERIES)
        stable_count = len(validate_lookup_cases.EXACT_STABLE_API_QUERIES)
        natural_count = len(validate_lookup_cases.NATURAL_QUERY_CASES)
        total_count = exact_count + stable_count + natural_count

        self.assertEqual(
            (74, 39, 105, 218),
            (
                exact_count,
                stable_count,
                natural_count,
                total_count,
            ),
        )
        expected_statement = (
            f"The {total_count}-case retrieval suite reports "
            f"{exact_count}/{exact_count} exact API, "
            f"{stable_count}/{stable_count} exact stable API, and "
            f"{natural_count}/{natural_count} natural-language Top-1 results "
            "(100% in every category)."
        )
        self.assertIn(expected_statement, self.runtime_document)

    def test_lookup_results_support_documented_full_pass_rates(self):
        compose_modules, search_skill_index = validate_lookup_cases.load_modules()

        for query in validate_lookup_cases.EXACT_API_QUERIES:
            with self.subTest(kind="exact_api", query=query):
                matches = compose_modules.api_matches(query, limit=1)
                self.assertTrue(matches)
                self.assertEqual(100, matches[0][0])
                self.assertEqual(query, matches[0][1].get("member"))

        for query in validate_lookup_cases.EXACT_STABLE_API_QUERIES:
            with self.subTest(kind="stable_api", query=query):
                matches = compose_modules.api_matches(query, limit=1)
                self.assertTrue(matches)
                self.assertEqual(120, matches[0][0])
                self.assertEqual(query, matches[0][1].get("stable_id"))

        for query, expected_route in validate_lookup_cases.NATURAL_QUERY_CASES:
            with self.subTest(kind="natural_language", query=query):
                actual_route, _ = validate_lookup_cases.top_natural_match(
                    search_skill_index,
                    query,
                )
                self.assertEqual(expected_route, actual_route)


if __name__ == "__main__":
    unittest.main()
