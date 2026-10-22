import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_DIRECTORY = Path(__file__).resolve().parent
SKILL_DIRECTORY = SCRIPT_DIRECTORY.parent
GENERATOR_PATH = SCRIPT_DIRECTORY / "create_android_project.py"
LOCALIZATION_PATH = (
    SKILL_DIRECTORY / "references" / "ui-localization-zh-cn.json"
)

BLUEPRINT_MARKERS = {
    "short-video-editor": ("Select media and create project", "选择媒体并创建项目"),
    "beauty-camera": ("Initializing camera...", "正在初始化相机…"),
    "camera-plus-editor": ("Camera Plus Editor", "拍摄与编辑"),
    "asset-center-demo": ("Local materials", "本地素材"),
    "template-mimo-cutsame-app": ("Template Studio", "模板工作台"),
    "pip-editor": ("PIP Editor", "画中画编辑器"),
    "quick-splicing-app": ("Quick Splicing", "快速拼接"),
    "full-sdk-demo": ("Full SDK Demo", "SDK 全功能演示"),
    "incremental-integration": ("Incremental Integration", "增量接入"),
}

JAVA_STRING_PATTERN = re.compile(r'"((?:\\.|[^"\\])*)"')
XML_UI_VALUE_PATTERN = re.compile(
    r'android:(?:text|hint|contentDescription|title)="([^"]*)"'
    r"|<string\b[^>]*>(.*?)</string>"
)
USER_VISIBLE_STATEMENT_PATTERN = re.compile(
    r"(?:"
    r"\bset(?:Text|Hint|Title|Message|ContentDescription|PositiveButton|NegativeButton|NeutralButton|Status)\s*\("
    r"|\bToast\.makeText\s*\("
    r"|\bui\.setStatus\s*\("
    r"|\bfailures?\.add\s*\("
    r"|\bthrow new IOException\s*\("
    r"|\b\w*(?:Status|Message|Title|Summary|Label)\w*\s*="
    r")"
)
ALLOWED_UI_IDENTIFIERS = {
    "AAR",
    "Android",
    "AR",
    "Context",
    "CutSame",
    "D",
    "ID",
    "incremental",
    "JAR",
    "LiveWindow",
    "Mimo",
    "PIP",
    "SDK",
    "Skill",
    "Transform",
    "URI",
    "ZIP",
    "shotInfos",
}


def generated_source_text(project_directory):
    parts = []
    for path in sorted(project_directory.rglob("*")):
        if path.is_file() and path.suffix.lower() in {".java", ".xml"}:
            parts.append(path.read_text(encoding="utf-8"))
    return "\n".join(parts)


def enclosing_java_statement(source_text, literal_start):
    statement_start = max(
        source_text.rfind(";", 0, literal_start),
        source_text.rfind("{", 0, literal_start),
        source_text.rfind("}", 0, literal_start),
    )
    statement_end = source_text.find(";", literal_start)
    if statement_end < 0:
        statement_end = len(source_text)
    return source_text[statement_start + 1 : statement_end + 1]


def english_ui_words(value):
    if re.fullmatch(r"[a-z][A-Za-z0-9]*", value):
        return []
    sanitized = value
    sanitized = re.sub(r"\\[nrtbf\"'\\]", "", sanitized)
    sanitized = re.sub(r"--[a-z0-9-]+", "", sanitized)
    sanitized = re.sub(r"\b[\w-]+\.(?:json|xml|template|jar|aar|zip|lic)\b", "", sanitized)
    sanitized = re.sub(r"\.(?:json|xml|template|jar|aar|zip|lic)\b", "", sanitized)
    sanitized = re.sub(r"\b[a-zA-Z_$][\w$]*\s*\([^)]*\)", "", sanitized)
    sanitized = re.sub(r"\b[a-z]+(?:-[a-z0-9]+)+\b", "", sanitized)
    sanitized = re.sub(r"%[-+#0-9.]*[a-zA-Z]", "", sanitized)
    words = re.findall(r"[A-Za-z][A-Za-z0-9]*", sanitized)
    return [
        word
        for word in words
        if word not in ALLOWED_UI_IDENTIFIERS and not re.fullmatch(r"R\d+", word)
    ]


def untranslated_ui_literals(project_directory):
    findings = []
    for path in sorted(project_directory.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in {".java", ".xml"}:
            continue
        source_text = path.read_text(encoding="utf-8")
        if path.suffix.lower() == ".xml":
            for match in XML_UI_VALUE_PATTERN.finditer(source_text):
                value = next(group for group in match.groups() if group is not None)
                if value.startswith("@"):
                    continue
                words = english_ui_words(value)
                if words:
                    findings.append((path, value, words))
            continue
        for match in JAVA_STRING_PATTERN.finditer(source_text):
            statement = enclosing_java_statement(source_text, match.start())
            if not USER_VISIBLE_STATEMENT_PATTERN.search(statement):
                continue
            value = match.group(1)
            words = english_ui_words(value)
            if words:
                findings.append((path, value, words))
    return findings


class BlueprintUiLocalizationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary_directory = tempfile.TemporaryDirectory()
        cls.generated_projects = {}
        root = Path(cls.temporary_directory.name)
        for language in ("en", "zh-CN"):
            language_root = root / language
            for blueprint_id in BLUEPRINT_MARKERS:
                output_directory = language_root / blueprint_id
                package_suffix = blueprint_id.replace("-", "")
                app_name = "Localization Audit" if language == "en" else "本地化审计"
                completed = subprocess.run(
                    [
                        sys.executable,
                        str(GENERATOR_PATH),
                        str(output_directory),
                        "--package",
                        f"com.example.localization.{package_suffix}",
                        "--app-name",
                        app_name,
                        "--ui-language",
                        language,
                        "--blueprint",
                        blueprint_id,
                        "--no-sample-assets",
                    ],
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    timeout=60,
                )
                if completed.returncode != 0:
                    raise AssertionError(
                        f"{language}/{blueprint_id} generation failed:\n"
                        f"{completed.stdout}\n{completed.stderr}"
                    )
                cls.generated_projects[(language, blueprint_id)] = output_directory

    @classmethod
    def tearDownClass(cls):
        cls.temporary_directory.cleanup()

    def test_all_nine_blueprints_keep_english_ui(self):
        for blueprint_id, (english_marker, _) in BLUEPRINT_MARKERS.items():
            with self.subTest(blueprint=blueprint_id):
                source_text = generated_source_text(
                    self.generated_projects[("en", blueprint_id)]
                )
                self.assertIn(english_marker, source_text)

    def test_all_nine_blueprints_have_chinese_ui_markers(self):
        for blueprint_id, (english_marker, chinese_marker) in BLUEPRINT_MARKERS.items():
            with self.subTest(blueprint=blueprint_id):
                source_text = generated_source_text(
                    self.generated_projects[("zh-CN", blueprint_id)]
                )
                self.assertIn(chinese_marker, source_text)
                self.assertNotIn(f'"{english_marker}"', source_text)

    def test_chinese_blueprints_have_no_untranslated_ui_prose(self):
        findings = []
        for blueprint_id in BLUEPRINT_MARKERS:
            project_directory = self.generated_projects[("zh-CN", blueprint_id)]
            for path, value, words in untranslated_ui_literals(project_directory):
                findings.append(
                    (
                        blueprint_id,
                        str(path.relative_to(project_directory)),
                        value,
                        words,
                    )
                )
        self.assertEqual([], findings[:40], f"Untranslated UI literals: {findings[:40]}")

    def test_sdk_literal_identifiers_are_not_translated_in_java(self):
        beauty_project = self.generated_projects[("zh-CN", "beauty-camera")]
        java_text = "\n".join(
            path.read_text(encoding="utf-8")
            for path in beauty_project.rglob("*.java")
        )
        xml_text = "\n".join(
            path.read_text(encoding="utf-8")
            for path in beauty_project.rglob("*.xml")
        )

        self.assertIn('"Whitening"', java_text)
        self.assertIn('"AR Scene"', java_text)
        self.assertNotIn('"美白"', java_text)
        self.assertIn('android:text="美白"', xml_text)

    def test_localization_map_has_unique_keys(self):
        text = LOCALIZATION_PATH.read_text(encoding="utf-8")
        pairs = json.loads(text, object_pairs_hook=lambda values: values)
        keys = [key for key, _ in pairs]

        self.assertEqual(len(keys), len(set(keys)))


if __name__ == "__main__":
    unittest.main()
