import importlib.util
import io
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path
from types import SimpleNamespace


SCRIPT_PATH = Path(__file__).with_name("create_android_project.py")
SPEC = importlib.util.spec_from_file_location("create_android_project", SCRIPT_PATH)
GENERATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GENERATOR)


class IncrementalApplyTest(unittest.TestCase):
    def make_fixture(self):
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        host = root / "host"
        module = host / "app"
        staging = root / "staging"
        (module / "src" / "main" / "java" / "com" / "example" / "host").mkdir(
            parents=True
        )
        (module / "src" / "main" / "AndroidManifest.xml").write_text(
            '<manifest xmlns:android="http://schemas.android.com/apk/res/android">\n'
            "    <application />\n"
            "</manifest>\n",
            encoding="utf-8",
        )
        (module / "build.gradle").write_text(
            "plugins { id 'com.android.application' }\n\ndependencies {\n}\n",
            encoding="utf-8",
        )
        (staging / "controllers").mkdir(parents=True)
        args = SimpleNamespace(
            host_project=host,
            app_module="app",
            package_name="com.example.host",
            force=True,
        )
        return temporary, module, staging, args

    def test_repeated_identical_apply_is_idempotent(self):
        temporary, module, staging, args = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        source = staging / "controllers" / "Controller.java"
        source.write_text("final class Controller {}\n", encoding="utf-8")
        composition = {"permissions": ["android.permission.CAMERA"]}

        first = GENERATOR.apply_incremental_patch(
            staging, args, composition, ["Controller.java"]
        )
        second = GENERATOR.apply_incremental_patch(
            staging, args, composition, ["Controller.java"]
        )

        self.assertEqual(1, len(first["applied_files"]))
        self.assertTrue(first["gradle_changed"])
        self.assertEqual(["android.permission.CAMERA"], first["manifest_permissions_added"])
        self.assertTrue(second["idempotent"])
        self.assertEqual(1, len(second["unchanged_files"]))
        manifest = (module / "src" / "main" / "AndroidManifest.xml").read_text(
            encoding="utf-8"
        )
        gradle = (module / "build.gradle").read_text(encoding="utf-8")
        self.assertEqual(1, manifest.count("android.permission.CAMERA"))
        self.assertEqual(1, gradle.count("NvAndroidStreamingSdk.jar"))

    def test_conflict_preflight_stops_before_copying_any_file(self):
        temporary, module, staging, args = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        package_dir = module / "src" / "main" / "java" / "com" / "example" / "host"
        (staging / "controllers" / "New.java").write_text(
            "final class New {}\n", encoding="utf-8"
        )
        (staging / "controllers" / "Conflict.java").write_text(
            "final class Conflict { int generated; }\n", encoding="utf-8"
        )
        (package_dir / "Conflict.java").write_text(
            "final class Conflict { int host; }\n", encoding="utf-8"
        )

        with self.assertRaisesRegex(SystemExit, "Conflicting host files"):
            GENERATOR.apply_incremental_patch(
                staging,
                args,
                {"permissions": ["android.permission.CAMERA"]},
                ["New.java", "Conflict.java"],
            )

        self.assertFalse((package_dir / "New.java").exists())
        manifest = (module / "src" / "main" / "AndroidManifest.xml").read_text(
            encoding="utf-8"
        )
        gradle = (module / "build.gradle").read_text(encoding="utf-8")
        self.assertNotIn("android.permission.CAMERA", manifest)
        self.assertNotIn("NvAndroidStreamingSdk.jar", gradle)


class ApiOnlyUsageTest(unittest.TestCase):
    def test_clip_editor_emits_track_selection_support(self):
        sources = GENERATOR.java_template_sources(
            {"resolved_modules": ["clip-editor"], "simple_code_units": []}
        )

        self.assertTrue(
            any(source.endswith("MeisheTrackSelection.java") for source in sources)
        )

    def test_editor_shell_emits_host_ownership_support(self):
        sources = GENERATOR.java_template_sources(
            {"resolved_modules": ["editor-shell"], "simple_code_units": []}
        )

        for expected in (
            "MeisheEditorHostContract.java",
            "MeisheTimelineOwnership.java",
            "MeisheEditorSessionController.java",
        ):
            self.assertTrue(any(source.endswith(expected) for source in sources))

    def test_selected_modules_emit_real_calls(self):
        source = GENERATOR.build_api_only_usage(
            "com.example.api",
            {
                "resolved_modules": [
                    "app-runtime",
                    "timeline-state-store",
                    "timeline-preview",
                    "caption-editor",
                    "capture-camera",
                    "asset-package-service",
                    "template-engine",
                    "export-compile",
                ]
            },
        )

        for expected in (
            "createTimelineWithMedia",
            "connectPreview",
            "addCaption",
            "startCapturePreview",
            "installAssetPackage",
            "queryTemplateFootages",
            "export(",
        ):
            self.assertIn(expected, source)
        self.assertNotIn("Instantiate the generated controllers", source)


class ExternalSampleAssetsTest(unittest.TestCase):
    def test_discovers_workspace_temp_assets_bundle(self):
        with tempfile.TemporaryDirectory() as temporary_dir:
            workspace = Path(temporary_dir)
            skill = workspace / ".codex" / "skills" / "meishe-skill"
            bundle = workspace / "temp_assets" / "android-sample-assets"
            (bundle / "app" / "src" / "main" / "assets").mkdir(parents=True)

            resolved = GENERATOR.resolve_sample_assets_dir(skill)

            self.assertEqual(bundle.resolve(), resolved)

    def test_rejects_explicit_bundle_without_android_asset_layout(self):
        with tempfile.TemporaryDirectory() as temporary_dir:
            invalid_bundle = Path(temporary_dir) / "materials"
            invalid_bundle.mkdir()

            with self.assertRaisesRegex(SystemExit, "Invalid --sample-assets-dir"):
                GENERATOR.resolve_sample_assets_dir(SCRIPT_PATH.parent, invalid_bundle)

    def test_missing_bundle_notice_routes_user_to_meishe_business(self):
        stderr = io.StringIO()

        with redirect_stderr(stderr):
            GENERATOR.print_sample_asset_notice("en")

        notice = stderr.getvalue()
        self.assertIn("not bundled inside this skill", notice)
        self.assertIn("Contact Meishe business", notice)
        self.assertIn("--sample-assets-dir", notice)

    def test_missing_bundle_notice_matches_chinese_request(self):
        notice = GENERATOR.sample_asset_notice("zh-CN")

        self.assertIn("Skill 内不再内置任何素材资源", notice)
        self.assertIn("联系美摄商务", notice)


class UiLocalizationTest(unittest.TestCase):
    def test_localizes_android_string_resource_body(self):
        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            skill = root / "skill"
            output = root / "output"
            (skill / "references").mkdir(parents=True)
            (output / "res" / "values").mkdir(parents=True)
            (skill / "references" / "ui-localization-zh-cn.json").write_text(
                '{"Previous step": "\\u4e0a\\u4e00\\u6b65"}', encoding="utf-8"
            )
            strings_file = output / "res" / "values" / "strings.xml"
            strings_file.write_text(
                '<resources><string name="editor_undo">Previous step</string></resources>',
                encoding="utf-8",
            )

            changed_files = GENERATOR.localize_tree(output, skill, "zh-CN")

            self.assertEqual(1, changed_files)
            self.assertIn(">\u4e0a\u4e00\u6b65<", strings_file.read_text(encoding="utf-8"))


class UserBuildHandoffTest(unittest.TestCase):
    def test_powershell_build_block_is_complete_and_copy_paste_ready(self):
        with tempfile.TemporaryDirectory() as temporary_dir:
            commands = GENERATOR.render_user_build_commands(
                Path(temporary_dir) / "Android Project",
                "app",
                shell_kind="powershell",
            )

        self.assertIn("Set-Location -LiteralPath $projectPath", commands)
        self.assertIn("'.\\gradlew.bat' ':app:assembleDebug'", commands)
        self.assertIn("if ($LASTEXITCODE -ne 0)", commands)
        self.assertIn("app\\build\\outputs\\apk", commands)
        self.assertNotIn("<project", commands)

    def test_posix_build_block_supports_nested_module(self):
        with tempfile.TemporaryDirectory() as temporary_dir:
            commands = GENERATOR.render_user_build_commands(
                temporary_dir,
                "features/editor",
                shell_kind="posix",
            )

        self.assertIn("./gradlew ':features:editor:assembleDebug'", commands)
        self.assertIn("features/editor/build/outputs/apk", commands)

    def test_rejects_unsafe_gradle_module_path(self):
        with self.assertRaisesRegex(SystemExit, "Invalid Gradle app module path"):
            GENERATOR.render_user_build_commands(
                Path.cwd(),
                "app'; Remove-Item",
                shell_kind="powershell",
            )


class ExecutionPolicyDocumentationTest(unittest.TestCase):
    def test_default_handoff_and_optional_qa_are_persisted(self):
        skill_directory = SCRIPT_PATH.parent.parent
        skill_text = (skill_directory / "SKILL.md").read_text(encoding="utf-8")
        handoff_text = (
            skill_directory / "references" / "execution-and-qa-handoff.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Do not execute Gradle by default", skill_text)
        self.assertIn("explicitly opts in", skill_text)
        self.assertIn("Automatic device QA is recommended", handoff_text)
        self.assertIn("Do not leave placeholders", handoff_text)
        self.assertIn("Do not build the staging project and host project separately", handoff_text)


if __name__ == "__main__":
    unittest.main()
