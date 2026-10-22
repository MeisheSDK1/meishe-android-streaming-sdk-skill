import sys
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from demo_knowledge_builder import evidence_only_disposition, infer_api_domains, invocation_arities


class InvocationAritiesTest(unittest.TestCase):
    def test_counts_string_literal_arguments(self):
        code = 'fx.setMenuVal("Segment Type", "Background");'

        self.assertEqual({2}, invocation_arities(code, "setMenuVal"))

    def test_counts_nested_expression_as_one_argument(self):
        code = 'track.addClip(path, Math.max(0, inPointUs), trimInUs, trimOutUs);'

        self.assertEqual({4}, invocation_arities(code, "addClip"))

    def test_distinguishes_empty_and_single_string_calls(self):
        code = 'context.stop(); context.setTheme("demo");'

        self.assertEqual({0}, invocation_arities(code, "stop"))
        self.assertEqual({1}, invocation_arities(code, "setTheme"))


class P3MemberClassificationTest(unittest.TestCase):
    def test_streaming_capture_member_uses_capture_domain(self):
        row = {
            "owner": "NvsStreamingContext",
            "member_name": "setExposureCompensation",
        }

        self.assertEqual(["capture-recording"], infer_api_domains(row))

    def test_caption_span_is_classified_as_value_object(self):
        row = {
            "owner": "NvsCaptionSpan",
            "member_name": "getStart",
            "kind": "method",
            "domain_ids": ["caption-editing"],
        }

        reason_code, reason = evidence_only_disposition(row)

        self.assertEqual("caption-editing.value_object_contract", reason_code)
        self.assertIn("value-object", reason)

    def test_field_retention_uses_domain_specific_constant_reason(self):
        row = {
            "owner": "NvsAssetPackageManager",
            "member_name": "ASSET_PACKAGE_TYPE_ARSCENE",
            "kind": "field",
            "domain_ids": ["asset-packages"],
        }

        reason_code, reason = evidence_only_disposition(row)

        self.assertEqual("asset-packages.typed_constant", reason_code)
        self.assertNotIn("no exact compiled/generated unit", reason.lower())


if __name__ == "__main__":
    unittest.main()
