import sys
import unittest
from pathlib import Path


SCRIPT_DIRECTORY = Path(__file__).resolve().parent
SKILL_DIRECTORY = SCRIPT_DIRECTORY.parent
REFERENCE_DIRECTORY = SKILL_DIRECTORY / "references"
sys.path.insert(0, str(SCRIPT_DIRECTORY))

import search_skill_index


def top_lookup_id(query):
    normalized_query = search_skill_index.normalize(query)
    terms = search_skill_index.split_terms(normalized_query)
    scored_entries = [
        (
            search_skill_index.score_entry(
                normalized_query,
                terms,
                entry,
            ),
            entry,
        )
        for entry in search_skill_index.load_index().get("entries", [])
    ]
    matches = [
        (score, entry) for score, entry in scored_entries if score > 0
    ]
    matches.sort(key=lambda match: (-match[0], match[1]["id"]))
    return matches[0][1]["id"] if matches else None


class SkillPolicyScenarioTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill_text = (
            SKILL_DIRECTORY / "SKILL.md"
        ).read_text(encoding="utf-8")
        cls.handoff_text = (
            REFERENCE_DIRECTORY / "execution-and-qa-handoff.md"
        ).read_text(encoding="utf-8")

    def test_representative_lookup_scenarios_keep_expected_top_route(self):
        scenarios = [
            ("我要做视频编辑器", "short-video-editor"),
            ("时间线剪辑", "timeline-editing"),
            ("相机录制", "capture-recording"),
            ("拼装字幕", "captions-stickers"),
            ("安装素材包", "asset-packages"),
            ("真机检测到人脸但 AR 场景依旧没效果", "beauty-makeup-ar"),
        ]
        for request, expected_route in scenarios:
            with self.subTest(request=request):
                self.assertEqual(expected_route, top_lookup_id(request))

    def test_existing_project_and_api_only_mode_scenarios(self):
        self.assertIn(
            "including an empty new project, treat it as an existing host",
            self.skill_text,
        )
        self.assertIn(
            "select/report blueprint id `incremental-integration` and use "
            "`--mode incremental`",
            self.skill_text,
        )
        self.assertIn(
            "use `--mode api-only` for controllers and an API sample "
            "without a product shell",
            self.skill_text,
        )

    def test_execution_and_optional_device_qa_scenarios(self):
        self.assertIn("Do not execute Gradle by default", self.skill_text)
        self.assertIn("explicitly requests automatic execution", self.skill_text)
        self.assertIn(
            "screenshot analysis are optional",
            self.skill_text,
        )
        self.assertIn("added time and token cost", self.skill_text)
        self.assertIn(
            "Gradle execution is handed back by default",
            self.handoff_text,
        )

    def test_external_material_and_application_scenarios(self):
        self.assertIn(
            "The skill contains no material binaries",
            self.skill_text,
        )
        self.assertIn(
            "obtain authorized resources from Meishe business",
            self.skill_text,
        )
        self.assertIn(
            "Material installation is not application",
            self.skill_text,
        )
        self.assertIn(
            "editable supported properties and removal",
            self.skill_text,
        )

    def test_editor_behavior_scenarios(self):
        self.assertIn(
            "Timeline resolution, the visible LiveWindow container ratio",
            self.skill_text,
        )
        self.assertIn(
            "A Trim action must choose a valid point inside the clip",
            self.skill_text,
        )
        self.assertIn(
            "Quick splicing must visibly preserve the ordered media list",
            self.skill_text,
        )
        self.assertIn(
            "Recording voiceover is incomplete until the recorded file is "
            "inserted on an audio track",
            self.skill_text,
        )

    def test_runtime_claim_scenario_keeps_evidence_levels_separate(self):
        self.assertIn(
            "Do not infer `runtime_verified` from generation, compilation",
            self.skill_text,
        )
        self.assertIn(
            "build evidence never becomes runtime evidence",
            self.skill_text,
        )
        self.assertIn(
            "generated, structurally validated, Java-compiled, Gradle-built, "
            "installed, flow-executed, and visually confirmed",
            self.skill_text,
        )


if __name__ == "__main__":
    unittest.main()
