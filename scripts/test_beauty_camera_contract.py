import json
import re
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as element_tree
from pathlib import Path


SCRIPT_DIRECTORY = Path(__file__).resolve().parent
SKILL_DIRECTORY = SCRIPT_DIRECTORY.parent
GENERATOR_PATH = SCRIPT_DIRECTORY / "create_android_project.py"
ANDROID_NAMESPACE = "{http://schemas.android.com/apk/res/android}"
FULL_CAPTURE_MODULES = ",".join(
    (
        "capture-camera",
        "capture-filter",
        "capture-scene",
        "beauty-camera",
        "makeup-service",
        "ar-scene",
        "segmentation-keying",
    )
)


class DefaultBeautyCameraGenerationContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary_directory = tempfile.TemporaryDirectory()
        cls.project_directory = (
            Path(cls.temporary_directory.name) / "default-beauty-camera"
        )
        plan_result = subprocess.run(
            [
                sys.executable,
                str(GENERATOR_PATH),
                "--blueprint",
                "beauty-camera",
                "--dry-run-plan",
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=60,
        )
        if plan_result.returncode != 0:
            raise AssertionError(
                "default beauty-camera plan failed:\n"
                f"{plan_result.stdout}\n{plan_result.stderr}"
            )
        cls.generation_plan = json.loads(plan_result.stdout)

        generation_result = subprocess.run(
            [
                sys.executable,
                str(GENERATOR_PATH),
                str(cls.project_directory),
                "--package",
                "com.example.defaultcapturecontract",
                "--app-name",
                "Default Capture Contract",
                "--ui-language",
                "en",
                "--blueprint",
                "beauty-camera",
                "--no-sample-assets",
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=60,
        )
        if generation_result.returncode != 0:
            raise AssertionError(
                "default beauty-camera generation failed:\n"
                f"{generation_result.stdout}\n{generation_result.stderr}"
            )

        layout_path = (
            cls.project_directory
            / "app"
            / "src"
            / "main"
            / "res"
            / "layout"
            / "activity_main.xml"
        )
        layout_root = element_tree.fromstring(
            layout_path.read_text(encoding="utf-8")
        )
        cls.generated_control_ids = {
            identifier.rsplit("/", 1)[-1]
            for element in layout_root.iter()
            if (
                identifier := element.attrib.get(
                    f"{ANDROID_NAMESPACE}id"
                )
            )
        }

    @classmethod
    def tearDownClass(cls):
        cls.temporary_directory.cleanup()

    def test_default_blueprint_keeps_full_capture_contract(self):
        required_modules = {
            "capture-camera",
            "capture-filter",
            "capture-scene",
            "beauty-camera",
            "makeup-service",
            "ar-scene",
            "segmentation-keying",
        }
        required_control_ids = {
            "captureSceneButton",
            "makeupButton",
            "faceMeshButton",
            "focusButton",
            "flashButton",
            "zoomSeekBar",
            "exposureSeekBar",
            "pauseRecordingButton",
        }
        required_material_route_ids = {
            "java.capture.append-packaged-fx",
            "java.capture.apply-scene",
            "java.beauty.configure-ar-scene",
            "java.makeup.configure-part",
            "java.segmentation.append-background-capture",
        }

        resolved_modules = set(self.generation_plan["resolved_modules"])
        simple_code_ids = set(self.generation_plan["simple_code_ids"])
        missing_contract_parts = {
            "modules": sorted(required_modules - resolved_modules),
            "controls": sorted(required_control_ids - self.generated_control_ids),
            "material_routes": sorted(
                required_material_route_ids - simple_code_ids
            ),
        }
        missing_contract_parts = {
            category: missing
            for category, missing in missing_contract_parts.items()
            if missing
        }

        self.assertEqual(
            ["beauty-camera"],
            self.generation_plan["app_templates"],
            "The default plan must select the beauty-camera application template.",
        )
        self.assertEqual(
            {},
            missing_contract_parts,
            "Default beauty-camera generation lost part of its full capture "
            f"contract: {missing_contract_parts}",
        )


class BeautyCameraGeneratedContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary_directory = tempfile.TemporaryDirectory()
        cls.project_directory = Path(cls.temporary_directory.name) / "beauty-camera"
        completed = subprocess.run(
            [
                sys.executable,
                str(GENERATOR_PATH),
                str(cls.project_directory),
                "--package",
                "com.example.capturecontract",
                "--app-name",
                "Capture Contract",
                "--ui-language",
                "en",
                "--blueprint",
                "beauty-camera",
                "--modules",
                FULL_CAPTURE_MODULES,
                "--no-sample-assets",
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=60,
        )
        if completed.returncode != 0:
            raise AssertionError(
                "beauty-camera generation failed:\n"
                f"{completed.stdout}\n{completed.stderr}"
            )
        cls.java_directory = (
            cls.project_directory
            / "app"
            / "src"
            / "main"
            / "java"
            / "com"
            / "example"
            / "capturecontract"
        )

    @classmethod
    def tearDownClass(cls):
        cls.temporary_directory.cleanup()

    @classmethod
    def java_source(cls, file_name):
        return (cls.java_directory / file_name).read_text(encoding="utf-8")

    @classmethod
    def layout_source(cls):
        return (
            cls.project_directory
            / "app"
            / "src"
            / "main"
            / "res"
            / "layout"
            / "activity_main.xml"
        ).read_text(encoding="utf-8")

    def assert_contract_contains(self, source, marker, contract_name):
        if marker not in source:
            self.fail(f"{contract_name}: missing {marker!r}")

    def assert_contract_pattern(self, source, pattern, contract_name):
        if re.search(pattern, source, re.DOTALL) is None:
            self.fail(f"{contract_name}: missing pattern {pattern!r}")

    def test_capture_only_materials_return_to_picker_owner(self):
        source = self.java_source("MeisheAssetCenterActivity.java")
        method_start = source.index("private void useInstalledMaterial()")
        method_end = source.index(
            "private boolean launchOptionalMaterialWorkflow()", method_start
        )
        use_method = source[method_start:method_end]

        self.assert_contract_contains(
            use_method,
            "MeisheAssetCenterConfig.EXTRA_PICK_MODE",
            "capture material picker mode",
        )
        self.assert_contract_contains(
            use_method,
            "setResult(RESULT_OK, pendingMaterialResult)",
            "capture material picker result",
        )
        self.assert_contract_contains(
            use_method,
            "finish()",
            "capture material picker completion",
        )
        self.assertNotIn(
            "!MeisheMaterialApplicationKind.isCaptureOnly",
            use_method,
            "Picker mode must return Capture Scene, AR Scene, Face Mesh, and Makeup "
            "to the owning camera instead of launching a nested sample activity.",
        )

    def test_camera_opens_picker_mode_and_routes_capture_materials(self):
        source = self.java_source("MainActivity.java")

        self.assert_contract_contains(
            source,
            "MeisheAssetCenterActivity.createPickerIntent(this)",
            "camera material picker entry",
        )
        self.assert_contract_contains(
            source,
            "MeisheAssetCenterConfig.EXTRA_APPLICATION_KIND",
            "semantic material result",
        )
        for package_type in (
            "ASSET_PACKAGE_TYPE_VIDEOFX",
            "ASSET_PACKAGE_TYPE_CAPTURESCENE",
            "ASSET_PACKAGE_TYPE_ARSCENE",
            "ASSET_PACKAGE_TYPE_FACE_MESH",
            "ASSET_PACKAGE_TYPE_MAKEUP",
        ):
            self.assert_contract_contains(
                source,
                package_type,
                "camera material package routes",
            )
        for application_kind, package_type in (
            ("MeisheMaterialApplicationKind.FILTER", "ASSET_PACKAGE_TYPE_VIDEOFX"),
            (
                "MeisheMaterialApplicationKind.CAPTURE_SCENE",
                "ASSET_PACKAGE_TYPE_CAPTURESCENE",
            ),
            ("MeisheMaterialApplicationKind.AR_SCENE", "ASSET_PACKAGE_TYPE_ARSCENE"),
            (
                "MeisheMaterialApplicationKind.FACE_MESH",
                "ASSET_PACKAGE_TYPE_FACE_MESH",
            ),
            ("MeisheMaterialApplicationKind.MAKEUP", "ASSET_PACKAGE_TYPE_MAKEUP"),
        ):
            self.assert_contract_pattern(
                source,
                rf"(?:{application_kind}.{{0,600}}{package_type}"
                rf"|{package_type}.{{0,600}}{application_kind})",
                f"{application_kind} kind/type validation",
            )

        self.assert_contract_pattern(
            source,
            r"(?:CAPTURE_SCENE|ASSET_PACKAGE_TYPE_CAPTURESCENE)"
            r".{0,800}beautyController\.applyCaptureScene\s*\(",
            "Capture Scene typed dispatch",
        )
        self.assert_contract_contains(
            source,
            "beautyController.appendCapturePackagedFx(",
            "generic capture FX dispatch",
        )
        self.assert_contract_contains(
            source,
            "beautyController.applyArScenePackage(",
            "AR Scene package dispatch",
        )
        self.assert_contract_contains(
            source,
            "beautyController.configureMakeupPart(",
            "Makeup package dispatch",
        )
        self.assert_contract_contains(
            source,
            "beautyController.applyEyebrowAngleFaceMeshPackage(",
            "Face Mesh package dispatch",
        )

    def test_picker_result_waits_for_capture_preview_restart(self):
        source = self.java_source("MainActivity.java")

        for state_field in (
            "pendingMaterialPackageId",
            "pendingMaterialPackageType",
            "pendingMaterialApplicationKind",
        ):
            self.assert_contract_contains(
                source,
                state_field,
                "pending material result state",
            )
        self.assert_contract_pattern(
            source,
            r"onCaptureDevicePreviewStarted\s*\([^)]*\)\s*\{"
            r".{0,1200}applyPendingMaterialResult\s*\(\s*\)",
            "material application after preview callback",
        )
        self.assert_contract_pattern(
            source,
            r"onActivityResult\s*\([^)]*\)\s*\{"
            r".{0,5000}pendingMaterialPackageId\s*=\s*packageId"
            r".{0,1000}(?:isPreviewStarted.{0,300})?"
            r"applyPendingMaterialResult\s*\(\s*\)",
            "material result queue",
        )

    def test_full_capture_ui_exposes_resolved_module_controls(self):
        layout = self.layout_source()
        activity = self.java_source("MainActivity.java")
        control_ids = (
            "captureSceneButton",
            "makeupButton",
            "faceMeshButton",
            "focusButton",
            "flashButton",
            "zoomSeekBar",
            "exposureSeekBar",
            "pauseRecordingButton",
        )

        missing_controls = []
        for control_id in control_ids:
            if f"@+id/{control_id}" not in layout:
                missing_controls.append(f"{control_id}:layout")
            if f"R.id.{control_id}" not in activity:
                missing_controls.append(f"{control_id}:binding")

        controller_calls = (
            "captureController.getDeviceCapability(",
            "captureController.configureDeviceControls(",
            "captureController.pauseRecording(",
            "captureController.resumeRecording(",
            "requestedCameraDeviceIndex",
            "activeCameraDeviceIndex",
        )
        missing_controls.extend(
            call
            for call in controller_calls
            if call not in activity
        )
        self.assertEqual(
            [],
            missing_controls,
            f"Missing full-capture controls/calls: {missing_controls}",
        )

    def test_recording_pause_resume_and_callbacks_reach_the_sdk(self):
        controller = self.java_source("MeisheCaptureController.java")
        activity = self.java_source("MainActivity.java")

        for signature in (
            "public boolean pauseRecording()",
            "public boolean resumeRecording()",
        ):
            self.assert_contract_contains(
                controller,
                signature,
                "recording state controller",
            )
        self.assert_contract_contains(
            controller,
            "streamingContext.pauseRecording()",
            "pause recording SDK call",
        )
        self.assert_contract_contains(
            controller,
            "streamingContext.resumeRecording()",
            "resume recording SDK call",
        )

        for callback_setter in (
            "setCaptureDeviceCallback",
            "setCaptureRecordingStartedCallback",
            "setCaptureRecordingDurationCallback",
            "setCaptureRecordingFrameReachedCallback",
        ):
            self.assert_contract_contains(
                controller,
                callback_setter,
                "capture callback registration",
            )
        self.assert_contract_contains(
            activity,
            "captureController.registerCallbacks(",
            "capture callback UI binding",
        )
        for callback_type in (
            "NvsStreamingContext.CaptureDeviceCallback",
            "NvsStreamingContext.CaptureRecordingStartedCallback",
            "NvsStreamingContext.CaptureRecordingDurationCallback",
            "NvsStreamingContext.CaptureRecordingFrameReachedCallback",
        ):
            self.assert_contract_contains(
                activity,
                callback_type,
                "capture callback implementation",
            )
        for callback_method in (
            "onCaptureDevicePreviewStarted",
            "onCaptureDeviceCapsReady",
            "onCaptureRecordingFinished",
            "onCaptureRecordingError",
            "onRecordingFirstVideoFrameReached",
        ):
            self.assert_contract_contains(
                activity,
                callback_method,
                "capture callback UI state",
            )
        self.assert_contract_contains(
            activity,
            "captureController.stopRecordingSynchronously(true)",
            "recording completion callback handoff",
        )
        callbacks_cleared = (
            "captureController.clearCallbacks(" in activity
            or re.search(
                r"captureController\.registerCallbacks\s*\("
                r"\s*null\s*,\s*null\s*,\s*null\s*,\s*null\s*\)",
                activity,
                re.DOTALL,
            )
            is not None
        )
        self.assertTrue(
            callbacks_cleared,
            "capture callback teardown: callbacks are not cleared",
        )

    def test_makeup_and_face_mesh_have_concrete_ar_scene_bindings(self):
        controller = self.java_source("MeisheBeautyArController.java")
        activity = self.java_source("MainActivity.java")

        for parameter_key in (
            '"Scene Id"',
            '"Makeup Enabled"',
            '"Makeup Custom Enabled Flag"',
            '"Face Mesh Internal Enabled"',
            '"Face Mesh Eyebrow Angle Custom Package Id"',
            '"Face Mesh Eyebrow Angle Degree"',
        ):
            self.assert_contract_contains(
                controller,
                parameter_key,
                "AR Scene material parameter",
            )
        self.assert_contract_contains(
            controller,
            "public boolean applyEyebrowAngleFaceMeshPackage(",
            "Face Mesh controller",
        )
        self.assert_contract_contains(
            controller,
            "NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL",
            "Makeup custom-part enable flags",
        )
        self.assert_contract_contains(
            activity,
            "beautyController.applyArScenePackage(",
            "AR Scene activity route",
        )
        self.assert_contract_pattern(
            activity,
            r"configureMakeupPart\s*\(\s*arSceneFx\s*,\s*\"Lip\"",
            "Makeup activity route",
        )
        self.assert_contract_contains(
            activity,
            "Contact Meishe business",
            "missing Makeup resource guidance",
        )
        self.assert_contract_pattern(
            activity,
            r"ASSET_PACKAGE_TYPE_MAKEUP.{0,1000}configureMakeupPart\s*\(",
            "Makeup typed dispatch",
        )
        self.assert_contract_pattern(
            activity,
            r"ASSET_PACKAGE_TYPE_FACE_MESH.{0,1000}"
            r"applyEyebrowAngleFaceMeshPackage\s*\(",
            "Face Mesh typed dispatch",
        )

    def test_manifest_registers_capture_entry_points_and_permissions(self):
        manifest_path = (
            self.project_directory / "app" / "src" / "main" / "AndroidManifest.xml"
        )
        root = element_tree.fromstring(manifest_path.read_text(encoding="utf-8"))
        permission_names = {
            permission.attrib.get(f"{ANDROID_NAMESPACE}name")
            for permission in root.findall("uses-permission")
        }
        activities = {
            activity.attrib.get(f"{ANDROID_NAMESPACE}name")
            for activity in root.findall("./application/activity")
        }

        self.assertIn("android.permission.CAMERA", permission_names)
        self.assertIn("android.permission.RECORD_AUDIO", permission_names)
        self.assertIn(".MainActivity", activities)
        self.assertIn(".MeisheAssetCenterActivity", activities)


class BeautyCameraDocumentationContractTest(unittest.TestCase):
    def test_blueprint_links_full_capture_product_contract(self):
        blueprint_text = (
            SKILL_DIRECTORY / "references" / "app-blueprints.md"
        ).read_text(encoding="utf-8")
        contract_path = (
            SKILL_DIRECTORY / "references" / "beauty-camera-product-contract.md"
        )
        contract_text = contract_path.read_text(encoding="utf-8")

        self.assertIn("beauty-camera-product-contract.md", blueprint_text)
        for required_term in (
            "picker mode",
            "applyCaptureScene",
            "Face Mesh",
            "Makeup",
            "pauseRecording",
            "resumeRecording",
            "CaptureDeviceCallback",
            "AndroidManifest.xml",
        ):
            self.assertIn(required_term, contract_text)


if __name__ == "__main__":
    unittest.main()
