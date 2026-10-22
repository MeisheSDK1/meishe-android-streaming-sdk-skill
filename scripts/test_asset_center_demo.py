import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_DIRECTORY = Path(__file__).resolve().parent
SKILL_DIRECTORY = SCRIPT_DIRECTORY.parent
GENERATOR_PATH = SCRIPT_DIRECTORY / "create_android_project.py"
BLUEPRINT_DIRECTORY = (
    SKILL_DIRECTORY
    / "assets"
    / "android-blueprint-templates"
    / "asset-center-demo"
)
ASSET_CENTER_ACTIVITY_PATH = (
    SKILL_DIRECTORY
    / "assets"
    / "android-feature-templates"
    / "asset-center"
    / "app"
    / "src"
    / "main"
    / "java"
    / "{{PACKAGE_PATH}}"
    / "MeisheAssetCenterActivity.java"
)


class AssetCenterDemoContractTest(unittest.TestCase):
    def test_blueprint_uses_real_timeline_preview_host(self):
        main_activity = (
            BLUEPRINT_DIRECTORY
            / "app"
            / "src"
            / "main"
            / "java"
            / "{{PACKAGE_PATH}}"
            / "MainActivity.java"
        ).read_text(encoding="utf-8")

        for expected in (
            "new NvsLiveWindow(this)",
            "createTimeline(PROJECT_WIDTH, PROJECT_HEIGHT)",
            "connectTimelineWithLiveWindow(timeline, liveWindow)",
            "liveWindow.setFillMode(NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT)",
            "previewWidth * (PROJECT_HEIGHT / (float) PROJECT_WIDTH)",
            "previewClip.appendPackagedFx(packageId)",
            "appliedFilter.setFilterIntensity",
            "previewClip.removeFx(appliedFilter.getIndex())",
            "MeisheAssetCenterActivity.createPickerIntent(this)",
            "MeisheMaterialApplicationKind.FILTER",
            "createGeneratedPreviewImage()",
        ):
            self.assertIn(expected, main_activity)

    def test_manifest_registers_picker_activity_separately_from_host(self):
        manifest = (
            BLUEPRINT_DIRECTORY / "app" / "src" / "main" / "AndroidManifest.xml"
        ).read_text(encoding="utf-8")

        self.assertIn('android:name=".MainActivity"', manifest)
        self.assertIn('android:name=".MeisheAssetCenterActivity"', manifest)
        self.assertEqual(1, manifest.count("android.intent.action.MAIN"))

    def test_picker_always_returns_installed_material_to_its_host(self):
        activity = ASSET_CENTER_ACTIVITY_PATH.read_text(encoding="utf-8")
        usage_method = activity.split(
            "private void useInstalledMaterial()", 1
        )[1].split("private boolean launchOptionalMaterialWorkflow()", 1)[0]

        self.assertIn("MeisheAssetCenterConfig.EXTRA_PICK_MODE", usage_method)
        self.assertIn("setResult(RESULT_OK, pendingMaterialResult)", usage_method)
        self.assertIn("finish()", usage_method)
        self.assertNotIn("isCaptureOnly", usage_method)

    def test_generated_blueprint_keeps_host_in_both_ui_languages(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            for language, marker in (
                ("en", "Applied filter to the sample Timeline clip: "),
                ("zh-CN", "已将滤镜应用到时间线示例片段："),
            ):
                with self.subTest(language=language):
                    output_directory = root / language
                    completed = subprocess.run(
                        [
                            sys.executable,
                            str(GENERATOR_PATH),
                            str(output_directory),
                            "--package",
                            f"com.example.assetcenter.{language.lower().replace('-', '')}",
                            "--app-name",
                            "素材闭环" if language == "zh-CN" else "Material Loop",
                            "--ui-language",
                            language,
                            "--blueprint",
                            "asset-center-demo",
                            "--no-sample-assets",
                        ],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        timeout=60,
                    )
                    self.assertEqual(
                        0,
                        completed.returncode,
                        f"{completed.stdout}\n{completed.stderr}",
                    )
                    generated_main = next(output_directory.rglob("MainActivity.java"))
                    generated_text = generated_main.read_text(encoding="utf-8")
                    generated_manifest = (
                        output_directory / "app" / "src" / "main" / "AndroidManifest.xml"
                    ).read_text(encoding="utf-8")
                    self.assertIn(marker, generated_text)
                    self.assertIn("appendPackagedFx(packageId)", generated_text)
                    self.assertIn(".MeisheAssetCenterActivity", generated_manifest)
                    self.assertNotIn("{{PACKAGE_NAME}}", generated_text)


if __name__ == "__main__":
    unittest.main()
