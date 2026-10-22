import re
import unittest
from pathlib import Path


SKILL_DIRECTORY = Path(__file__).resolve().parents[1]
SKILL_PATH = SKILL_DIRECTORY / "SKILL.md"
MAX_ENTRYPOINT_BYTES = 28 * 1024


class SkillEntrypointContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill_text = SKILL_PATH.read_text(encoding="utf-8")

    def test_entrypoint_stays_within_context_budget(self):
        entrypoint_size = len(self.skill_text.encode("utf-8"))
        self.assertLessEqual(entrypoint_size, MAX_ENTRYPOINT_BYTES)

    def test_referenced_files_exist(self):
        reference_paths = sorted(
            set(re.findall(r"references/([A-Za-z0-9._-]+)", self.skill_text))
        )
        self.assertGreater(len(reference_paths), 0)
        missing_paths = [
            relative_path
            for relative_path in reference_paths
            if not (SKILL_DIRECTORY / "references" / relative_path).is_file()
        ]
        self.assertEqual(missing_paths, [])

    def test_high_risk_policies_remain_in_the_entrypoint(self):
        required_fragments = {
            "ui_thread": ["NvsStreamingContext", "UI thread"],
            "gl_thread": ["NvsEffectRenderCore", "OpenGL thread"],
            "runtime_evidence": ["runtime_verified", "runtime-verification-matrix.json"],
            "ar_visual_evidence": ["AR/face", "visual evidence"],
            "external_materials": ["temp_assets/android-sample-assets", "Meishe business"],
            "user_run_gradle": ["Do not execute Gradle by default", "explicitly opts in"],
            "ui_language": ["--ui-language zh-CN", "--ui-language en"],
            "timeline_preview_ratio": ["Timeline resolution", "LiveWindow", "FILLMODE_PRESERVEASPECTFIT"],
            "host_ownership": ["HOST_OWNED", "removeTimeline", "--force"],
            "independence": ["original Demo or Doxygen", "normal knowledge dependencies"],
        }
        for policy_name, fragments in required_fragments.items():
            with self.subTest(policy=policy_name):
                for fragment in fragments:
                    self.assertIn(fragment, self.skill_text)

    def test_primary_routing_commands_remain_in_the_entrypoint(self):
        for command_name in (
            "search_skill_index.py",
            "compose_modules.py",
            "create_android_project.py",
        ):
            with self.subTest(command=command_name):
                self.assertIn(command_name, self.skill_text)

    def test_generation_modes_remain_discoverable(self):
        for mode in ("--blueprint", "--mode incremental", "--mode api-only"):
            with self.subTest(mode=mode):
                self.assertIn(mode, self.skill_text)


if __name__ == "__main__":
    unittest.main()
