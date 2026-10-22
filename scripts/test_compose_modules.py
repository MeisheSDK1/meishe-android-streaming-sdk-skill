"""Observable behavior tests for natural-language module composition."""

import importlib.util
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parent / "compose_modules.py"
SPEC = importlib.util.spec_from_file_location("compose_modules_under_test", SCRIPT_PATH)
COMPOSE_MODULES = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(COMPOSE_MODULES)


class NaturalLanguageCompositionTest(unittest.TestCase):
    def compose(self, query, mode="new-app", modules="", blueprint=""):
        return COMPOSE_MODULES.compose_request(
            query=query,
            mode=mode,
            modules=modules,
            blueprint=blueprint,
        )

    def test_complete_editor_selects_one_editor_blueprint_without_other_products(self):
        for query in (
            "创建一个包含完整编辑功能的 Android 应用",
            "build a full editing app with captions and watermark",
        ):
            with self.subTest(query=query):
                composition = self.compose(query)

                self.assertEqual(composition["blueprints"], ["short-video-editor"])
                self.assertIn("editor-shell", composition["resolved_modules"])
                self.assertIn("clip-editor", composition["resolved_modules"])
                self.assertIn("timeline-preview", composition["resolved_modules"])
                self.assertNotIn("capture-camera", composition["resolved_modules"])
                self.assertNotIn("ar-scene", composition["resolved_modules"])
                self.assertNotIn("template-engine", composition["resolved_modules"])
                self.assertNotIn("pip-editor", composition["resolved_modules"])

    def test_complete_capture_selects_full_capture_chain_without_editor_modules(self):
        for query in (
            "创建一个包含完整拍摄功能的 Android 应用",
            "build an app with all capture features",
        ):
            with self.subTest(query=query):
                composition = self.compose(query)

                self.assertEqual(composition["blueprints"], ["beauty-camera"])
                for module_id in COMPOSE_MODULES.FULL_CAPTURE_MODULE_IDS:
                    self.assertIn(module_id, composition["resolved_modules"])
                self.assertNotIn("editor-shell", composition["resolved_modules"])
                self.assertNotIn("timeline-state-store", composition["resolved_modules"])
                self.assertNotIn("clip-editor", composition["resolved_modules"])
                self.assertNotIn("filter-editor", composition["resolved_modules"])

    def test_incremental_mode_always_uses_incremental_blueprint(self):
        composition = self.compose(
            "在现有 Android 项目接入完整拍摄能力",
            mode="incremental",
            blueprint="beauty-camera",
        )

        self.assertEqual(composition["blueprints"], ["incremental-integration"])
        self.assertIn("capture-camera", composition["resolved_modules"])
        self.assertNotIn("editor-shell", composition["resolved_modules"])

    def test_new_app_automatically_selects_only_one_primary_blueprint(self):
        composition = self.compose("制作带字幕和贴纸的视频编辑应用")

        self.assertEqual(composition["blueprints"], ["short-video-editor"])

    def test_query_can_explicitly_name_multiple_blueprints(self):
        composition = self.compose(
            "分别生成 short-video-editor 和 beauty-camera 两个蓝图"
        )

        self.assertEqual(
            composition["blueprints"],
            ["short-video-editor", "beauty-camera"],
        )

    def test_mentioning_multiple_blueprints_without_requesting_both_keeps_one(self):
        composition = self.compose(
            "比较 short-video-editor 和 beauty-camera 的差异"
        )

        self.assertEqual(composition["blueprints"], ["short-video-editor"])

    def test_blueprint_argument_can_explicitly_select_multiple_blueprints(self):
        composition = self.compose(
            "",
            blueprint="short-video-editor,beauty-camera",
        )

        self.assertEqual(
            composition["blueprints"],
            ["short-video-editor", "beauty-camera"],
        )

    def test_exact_api_only_keeps_member_level_scope(self):
        composition = self.compose(
            "NvsStreamingContext.createTimeline",
            mode="api-only",
        )

        self.assertEqual(composition["blueprints"], [])
        self.assertEqual(composition["resolved_modules"], [])
        self.assertIn("java.timeline.create", composition["simple_code_ids"])

    def test_explicit_modules_are_not_removed_by_product_intent_filter(self):
        composition = self.compose(
            "创建完整编辑应用",
            modules="capture-camera",
        )

        self.assertIn("capture-camera", composition["resolved_modules"])


if __name__ == "__main__":
    unittest.main()
