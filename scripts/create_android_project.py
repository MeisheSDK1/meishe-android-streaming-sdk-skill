#!/usr/bin/env python3
"""Create a standalone Android project from this skill's Meishe templates."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    if _stream is not None and hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_dir", nargs="?", type=Path)
    parser.add_argument("--package", default="com.example.meisheapp", dest="package_name")
    parser.add_argument("--app-name", default="MeisheApp")
    parser.add_argument("--compile-sdk", default="35")
    parser.add_argument("--target-sdk", default="35")
    parser.add_argument("--min-sdk", default="19")
    parser.add_argument("--agp-version", default="8.13.2")
    parser.add_argument(
        "--ui-language",
        default="en",
        choices=("en", "zh-CN"),
        help="Language for generated user-visible UI text. Match the language used in the request.",
    )
    parser.add_argument(
        "--features",
        default="",
        help="Comma/space-separated optional feature templates to overlay. Use --list-features.",
    )
    parser.add_argument(
        "--blueprint",
        default="",
        help="Composable app blueprint id(s), comma/space-separated. Use scripts/compose_modules.py --list.",
    )
    parser.add_argument(
        "--modules",
        default="",
        help="Composable module id(s), comma/space-separated. Dependencies are resolved automatically.",
    )
    parser.add_argument(
        "--mode",
        default="new-app",
        choices=("new-app", "incremental", "api-only"),
        help="Composition mode used for blueprint/module planning.",
    )
    parser.add_argument(
        "--host-project",
        type=Path,
        help="Existing Android project root for --mode incremental.",
    )
    parser.add_argument(
        "--app-module",
        default="app",
        help="Host Android app module name for --mode incremental. Defaults to app.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply an incremental staging patch into --host-project/--app-module. Default only stages files.",
    )
    parser.add_argument(
        "--dry-run-plan",
        action="store_true",
        help="Resolve blueprint/module dependencies, permissions, resources, templates, and snippets without writing files.",
    )
    parser.add_argument(
        "--no-sample-assets",
        action="store_true",
        help="Generate without copying an external lightweight sample asset bundle.",
    )
    parser.add_argument(
        "--sample-assets-dir",
        type=Path,
        help=(
            "Optional authorized external sample bundle root containing app/src/main/assets. "
            "This repository auto-discovers temp_assets/android-sample-assets."
        ),
    )
    parser.add_argument(
        "--sdk-root",
        type=Path,
        help="Optional extracted Meishe Android LTS face-package root. Copies NvAndroidStreamingSdk.jar and selected native libraries from mapped relative paths.",
    )
    parser.add_argument(
        "--license",
        type=Path,
        help="Optional authorized Meishe license file to copy to app/src/main/assets/meishesdk.lic. Bundled Demo licenses are evaluation-scope references only.",
    )
    parser.add_argument(
        "--abis",
        default="arm64-v8a",
        help="Comma/space-separated ABIs to copy from --sdk-root. Supported: arm64-v8a, armeabi-v7a.",
    )
    parser.add_argument(
        "--include-extra-sdk",
        action="store_true",
        help="When --sdk-root is set, also copy extrasdk/sdk/android *.jar and *.aar files to app/libs.",
    )
    parser.add_argument(
        "--human-models-dir",
        type=Path,
        help="Optional facemode directory, or parent containing facemode/. In the official face package use samples/android/SdkDemo/app/src/main/assets/facemode.",
    )
    parser.add_argument("--list-features", action="store_true")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()

def validate_package_name(package_name):
    pattern = r"^[a-zA-Z][a-zA-Z0-9_]*(\.[a-zA-Z][a-zA-Z0-9_]*)+$"
    if not re.match(pattern, package_name):
        raise SystemExit(f"Invalid Android package name: {package_name}")

def validate_sdk_levels(args):
    values = {
        "--compile-sdk": args.compile_sdk,
        "--target-sdk": args.target_sdk,
        "--min-sdk": args.min_sdk,
    }
    parsed = {}
    for name, value in values.items():
        try:
            parsed[name] = int(value)
        except ValueError as exc:
            raise SystemExit(f"{name} must be an integer: {value}") from exc
        if parsed[name] <= 0:
            raise SystemExit(f"{name} must be positive: {value}")
    if parsed["--min-sdk"] > parsed["--target-sdk"]:
        raise SystemExit("--min-sdk cannot be greater than --target-sdk")

def normalized_gradle_module_path(app_module):
    normalized = str(app_module).strip().replace("\\", ":").replace("/", ":").strip(":")
    if not normalized or not re.fullmatch(r"[A-Za-z0-9_.-]+(?::[A-Za-z0-9_.-]+)*", normalized):
        raise SystemExit(f"Invalid Gradle app module path: {app_module}")
    return normalized

def render_user_build_commands(project_dir, app_module="app", shell_kind=None):
    project_path = str(Path(project_dir).resolve())
    gradle_module = normalized_gradle_module_path(app_module)
    gradle_task = f":{gradle_module}:assembleDebug"
    if shell_kind is None:
        shell_kind = "powershell" if os.name == "nt" else "posix"
    if shell_kind == "powershell":
        quoted_project_path = "'" + project_path.replace("'", "''") + "'"
        module_directory = gradle_module.replace(":", "\\")
        apk_relative_path = f"{module_directory}\\build\\outputs\\apk"
        return "\n".join(
            [
                f"$projectPath = {quoted_project_path}",
                "Set-Location -LiteralPath $projectPath",
                f"& '.\\gradlew.bat' '{gradle_task}' '--console=plain' '--warning-mode' 'summary'",
                "if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }",
                (
                    "Get-ChildItem -LiteralPath (Join-Path $projectPath "
                    f"'{apk_relative_path}') -Recurse -Filter '*.apk' | "
                    "Select-Object -ExpandProperty FullName"
                ),
            ]
        )
    if shell_kind == "posix":
        quoted_project_path = "'" + project_path.replace("'", "'\"'\"'") + "'"
        module_directory = gradle_module.replace(":", "/")
        apk_relative_path = f"{module_directory}/build/outputs/apk"
        return "\n".join(
            [
                f"project_path={quoted_project_path}",
                'cd "$project_path"',
                f"./gradlew '{gradle_task}' --console=plain --warning-mode summary",
                f'find "$project_path/{apk_relative_path}" -type f -name \'*.apk\' -print',
            ]
        )
    raise SystemExit(f"Unsupported build-command shell: {shell_kind}")

def print_user_build_handoff(project_dir, app_module="app"):
    print("Gradle was not executed. Build handoff for the user (copy/paste as one block):")
    print(render_user_build_commands(project_dir, app_module))
    print(
        "Automatic physical-device screenshot QA is recommended but opt-in because it "
        "increases elapsed time and token usage."
    )

def replacement_map(args):
    return {
        "{{PACKAGE_NAME}}": args.package_name,
        "{{PACKAGE_PATH}}": args.package_name.replace(".", "/"),
        "{{APP_NAME}}": args.app_name,
        "{{COMPILE_SDK}}": args.compile_sdk,
        "{{TARGET_SDK}}": args.target_sdk,
        "{{MIN_SDK}}": args.min_sdk,
        "{{AGP_VERSION}}": args.agp_version,
        "{{EXTRA_DEPENDENCIES}}": (
            '    implementation "androidx.appcompat:appcompat:1.0.0"'
            if args.include_extra_sdk
            else ""
        ),
    }

def render_text(text, replacements):
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text

def available_features(feature_template_dir):
    if not feature_template_dir.exists():
        return {}
    return {
        feature_dir.name: feature_dir
        for feature_dir in sorted(feature_template_dir.iterdir())
        if feature_dir.is_dir()
    }

def parse_features(raw_features, feature_dirs):
    names = [name for name in re.split(r"[\s,]+", raw_features.strip()) if name]
    selected = []
    seen = set()
    for name in names:
        if name in seen:
            continue
        if name not in feature_dirs:
            allowed = ", ".join(feature_dirs) or "(none)"
            raise SystemExit(f"Unknown feature template: {name}. Available: {allowed}")
        selected.append(name)
        seen.add(name)
    return selected

def parse_abis(raw_abis):
    abi_names = [name for name in re.split(r"[\s,]+", raw_abis.strip()) if name]
    allowed = {"arm64-v8a", "armeabi-v7a"}
    selected = []
    for abi in abi_names:
        if abi not in allowed:
            raise SystemExit(f"Unsupported ABI: {abi}. Supported: {', '.join(sorted(allowed))}")
        if abi not in selected:
            selected.append(abi)
    return selected or ["arm64-v8a"]

def render_tree(source_dir, output_dir, replacements):
    for source in source_dir.rglob("*"):
        if source.is_dir():
            continue
        relative = source.relative_to(source_dir).as_posix()
        relative = render_text(relative, replacements)
        target = output_dir / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            text = source.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            shutil.copy2(source, target)
        else:
            target.write_text(render_text(text, replacements), encoding="utf-8")


JAVA_SDK_LITERAL_IDENTIFIERS = frozenset(
    {
        "AR Scene",
        "Fade",
        "Strength",
        "Whitening",
    }
)


def localize_tree(output_dir, skill_dir, ui_language):
    if ui_language == "en":
        return 0
    translation_path = skill_dir / "references" / f"ui-localization-{ui_language.lower()}.json"
    if not translation_path.is_file():
        raise SystemExit(f"Missing UI localization map: {translation_path}")
    translations = json.loads(translation_path.read_text(encoding="utf-8"))
    def localize_quoted_value(match):
        quoted_value = match.group(0)
        source_value = quoted_value[1:-1]
        if (
            target.suffix.lower() == ".java"
            and source_value in JAVA_SDK_LITERAL_IDENTIFIERS
        ):
            return quoted_value
        localized_value = translations.get(source_value, source_value)
        return f'"{localized_value}"'

    def localize_android_string_value(match):
        opening_tag, source_value, closing_tag = match.groups()
        localized_value = translations.get(source_value, source_value)
        return f"{opening_tag}{localized_value}{closing_tag}"

    changed_files = 0
    for target in output_dir.rglob("*"):
        if not target.is_file() or target.suffix.lower() not in {".java", ".xml"}:
            continue
        text = target.read_text(encoding="utf-8")
        localized = re.sub(r'"(?:\\.|[^"\\])*"', localize_quoted_value, text)
        if target.suffix.lower() == ".xml":
            localized = re.sub(
                r"(<string\b[^>]*>)(.*?)(</string>)",
                localize_android_string_value,
                localized,
                flags=re.DOTALL,
            )
        if localized != text:
            target.write_text(localized, encoding="utf-8")
            changed_files += 1
    return changed_files

def copy_tree(source_dir, output_dir):
    if not source_dir.exists():
        raise SystemExit(f"Missing source directory: {source_dir}")
    for source in source_dir.rglob("*"):
        if source.is_dir():
            continue
        relative = source.relative_to(source_dir)
        target = output_dir / relative
        copy_file(source, target)

def local_sample_assets_dir(skill_dir):
    return skill_dir.parents[2] / "temp_assets" / "android-sample-assets"

def resolve_sample_assets_dir(skill_dir, configured_dir=None):
    candidate = configured_dir if configured_dir is not None else local_sample_assets_dir(skill_dir)
    candidate = candidate.expanduser().resolve()
    expected_assets_dir = candidate / "app" / "src" / "main" / "assets"
    if candidate.is_dir() and expected_assets_dir.is_dir():
        return candidate
    if configured_dir is not None:
        raise SystemExit(
            "Invalid --sample-assets-dir. Expected an authorized bundle containing "
            f"app/src/main/assets: {candidate}"
        )
    return None

def sample_asset_notice(ui_language):
    if ui_language == "zh-CN":
        return (
            "提示：Skill 内不再内置任何素材资源。请联系美摄商务获取已授权素材，"
            "然后通过 --sample-assets-dir <素材包根目录> 指定；当前将不带示例素材继续生成。"
        )
    return (
        "NOTICE: Material assets are not bundled inside this skill. "
        "Contact Meishe business to obtain authorized material resources, then pass "
        "--sample-assets-dir <bundle-root>. Continuing without sample assets."
    )

def print_sample_asset_notice(ui_language):
    print(sample_asset_notice(ui_language), file=sys.stderr)

def copy_path(source_or_target):
    if os.name != "nt":
        return source_or_target
    resolved = str(source_or_target.resolve())
    if resolved.startswith("\\\\?\\"):
        return resolved
    if resolved.startswith("\\\\"):
        return "\\\\?\\UNC\\" + resolved.lstrip("\\")
    return "\\\\?\\" + resolved

def copy_file(source_file, target_file):
    source_copy_path = copy_path(source_file)
    target_copy_path = copy_path(target_file)
    if not os.path.isfile(source_copy_path):
        raise SystemExit(f"Missing source file: {source_file}")
    os.makedirs(copy_path(target_file.parent), exist_ok=True)
    shutil.copy2(source_copy_path, target_copy_path)

def copy_sdk_runtime(sdk_root, output_dir, abis, include_effect_sdk, include_extra_sdk):
    sdk_root = sdk_root.resolve()
    copy_file(
        sdk_root / "lib" / "android_jar" / "NvAndroidStreamingSdk.jar",
        output_dir / "app" / "libs" / "NvAndroidStreamingSdk.jar",
    )
    native_sources = {
        "arm64-v8a": sdk_root / "lib" / "android_arm64" / "libNvStreamingSdkCore.so",
        "armeabi-v7a": sdk_root / "lib" / "android_armv7" / "libNvStreamingSdkCore.so",
    }
    for abi in abis:
        copy_file(
            native_sources[abi],
            output_dir / "app" / "src" / "main" / "jniLibs" / abi / "libNvStreamingSdkCore.so",
        )
    effectlib = sdk_root / "extrasdk" / "sdk" / "android" / "effectlib.jar"
    if include_effect_sdk:
        copy_file(effectlib, output_dir / "app" / "libs" / "effectlib.jar")
    if include_extra_sdk:
        extra_dir = sdk_root / "extrasdk" / "sdk" / "android"
        if not extra_dir.exists():
            raise SystemExit(f"Missing extra SDK directory: {extra_dir}")
        for source in extra_dir.iterdir():
            if source.suffix.lower() in {".jar", ".aar"}:
                copy_file(source, output_dir / "app" / "libs" / source.name)

def copy_human_models(models_dir, output_dir):
    source_dir = models_dir.resolve()
    if (source_dir / "facemode").is_dir():
        source_dir = source_dir / "facemode"
    copy_tree(source_dir, output_dir / "app" / "src" / "main" / "assets" / "facemode")

def ensure_manifest_permissions(manifest_path, permission_names):
    text = manifest_path.read_text(encoding="utf-8")
    missing_lines = []
    for permission_name in permission_names:
        line = f'    <uses-permission android:name="{permission_name}" />'
        if permission_name not in text:
            missing_lines.append(line)
    if not missing_lines:
        return []
    marker = '<manifest xmlns:android="http://schemas.android.com/apk/res/android">'
    if marker not in text:
        raise SystemExit(f"Cannot inject permissions; manifest marker not found: {manifest_path}")
    text = text.replace(marker, marker + "\n" + "\n".join(missing_lines), 1)
    manifest_path.write_text(text, encoding="utf-8")
    return [
        permission_name
        for permission_name in permission_names
        if any(permission_name in line for line in missing_lines)
    ]

def compose_generation_plan(args, skill_dir):
    if not args.blueprint and not args.modules and args.mode == "new-app":
        return None
    scripts_dir = skill_dir / "scripts"
    scripts_dir_text = str(scripts_dir)
    if scripts_dir_text not in sys.path:
        sys.path.insert(0, scripts_dir_text)
    from compose_modules import compose_request

    return compose_request(
        query="",
        modules=args.modules or ("app-runtime" if args.mode in {"incremental", "api-only"} else ""),
        blueprint=args.blueprint,
        mode=args.mode,
    )

def merge_unique(*collections):
    result = []
    seen = set()
    for collection in collections:
        for item in collection or []:
            if item not in seen:
                result.append(item)
                seen.add(item)
    return result

MODULE_SUPPORT_SOURCES = {
    "asset-center-service": [
        "assets/android-feature-templates/asset-center/app/src/main/java/{{PACKAGE_PATH}}/MeisheAssetCenterConfig.java",
        "assets/android-feature-templates/asset-center/app/src/main/java/{{PACKAGE_PATH}}/MeisheLocalMaterialCatalog.java",
        "assets/android-feature-templates/asset-center/app/src/main/java/{{PACKAGE_PATH}}/MeisheLocalMaterialOperations.java",
        "assets/android-feature-templates/asset-center/app/src/main/java/{{PACKAGE_PATH}}/MeisheMaterialApplicationKind.java",
    ],
    "clip-editor": [
        "assets/android-blueprint-templates/short-video-editor/app/src/main/java/{{PACKAGE_PATH}}/MeisheTrackSelection.java",
    ],
    "editor-shell": [
        "assets/android-blueprint-templates/short-video-editor/app/src/main/java/{{PACKAGE_PATH}}/MeisheEditorHostContract.java",
        "assets/android-blueprint-templates/short-video-editor/app/src/main/java/{{PACKAGE_PATH}}/MeisheTimelineOwnership.java",
        "assets/android-blueprint-templates/short-video-editor/app/src/main/java/{{PACKAGE_PATH}}/MeisheProjectExtensionCodec.java",
        "assets/android-blueprint-templates/short-video-editor/app/src/main/java/{{PACKAGE_PATH}}/MeisheEditorProject.java",
        "assets/android-blueprint-templates/short-video-editor/app/src/main/java/{{PACKAGE_PATH}}/MeisheEditorSessionController.java",
        "assets/android-blueprint-templates/short-video-editor/app/src/main/java/{{PACKAGE_PATH}}/MeisheAppliedMaterial.java",
        "assets/android-blueprint-templates/short-video-editor/app/src/main/java/{{PACKAGE_PATH}}/MeisheMaterialApplicationKind.java",
    ],
}

def java_template_sources(composition):
    sources = []
    for unit in composition.get("simple_code_units", []):
        source = unit.get("template_source")
        if source and source.endswith(".java"):
            sources.append(source)
    for module_id in composition.get("resolved_modules", []):
        sources.extend(MODULE_SUPPORT_SOURCES.get(module_id, []))
    sources.append("assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheThreading.java")
    return merge_unique(sources)

def render_java_sources(source_paths, skill_dir, output_root, replacements):
    rendered_files = []
    for source_label in source_paths:
        source = skill_dir / source_label
        if not source.is_file():
            continue
        relative_name = Path(render_text(source_label, replacements)).name
        target = output_root / relative_name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render_text(source.read_text(encoding="utf-8"), replacements), encoding="utf-8")
        rendered_files.append(str(target.relative_to(output_root)).replace("\\", "/"))
    return rendered_files

def write_patch_manifest(output_dir, args, composition, rendered_files, mode):
    manifest = {
        "schema_version": 2,
        "mode": mode,
        "host_project": str(args.host_project.resolve()) if args.host_project else "",
        "app_module": args.app_module,
        "package_name": args.package_name,
        "ui_language": args.ui_language,
        "resolved_modules": composition.get("resolved_modules", []),
        "blueprints": composition.get("blueprints", []),
        "simple_code_ids": composition.get("simple_code_ids", []),
        "controllers": rendered_files,
        "permissions": composition.get("permissions", []),
        "resource_keys": composition.get("resource_keys", []),
        "gradle_dependencies": ["implementation files('libs/NvAndroidStreamingSdk.jar')"],
        "apply_policy": "staging-only unless --apply is supplied",
        "host_contract": {
            "language": "Java sources generated under src/main/java; Kotlin hosts can call them directly.",
            "manifest": "permissions are additive",
            "gradle": "Groovy and KTS dependency blocks are patched additively",
            "resources": "resolve SDK jars, native libraries, and models from an extracted official Android LTS face package; production licenses remain explicitly authorized inputs",
        },
    }
    (output_dir / "patch-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return manifest

def find_gradle_file(module_dir):
    for name in ("build.gradle", "build.gradle.kts"):
        path = module_dir / name
        if path.is_file():
            return path
    return None

def ensure_gradle_file_dependency(gradle_path):
    if gradle_path is None:
        return False
    text = gradle_path.read_text(encoding="utf-8")
    if "NvAndroidStreamingSdk.jar" in text:
        return False
    dependency = (
        '    implementation(files("libs/NvAndroidStreamingSdk.jar"))'
        if gradle_path.suffix == ".kts"
        else "    implementation files('libs/NvAndroidStreamingSdk.jar')"
    )
    match = re.search(r"dependencies\s*\{", text)
    if match:
        insert_at = text.find("\n", match.end())
        text = text[: insert_at + 1] + dependency + "\n" + text[insert_at + 1:]
    else:
        text = text.rstrip() + "\n\ndependencies {\n" + dependency + "\n}\n"
    gradle_path.write_text(text, encoding="utf-8")
    return True

def apply_incremental_patch(staging_dir, args, composition, rendered_files):
    if args.host_project is None:
        raise SystemExit("--host-project is required when --apply is used.")
    host_project = args.host_project.resolve()
    module_dir = host_project / args.app_module
    if not module_dir.is_dir():
        raise SystemExit(f"Missing host app module: {module_dir}")
    package_dir = module_dir / "src" / "main" / "java" / args.package_name.replace(".", os.sep)
    pending_files = []
    unchanged_files = []
    conflicting_files = []
    for relative in rendered_files:
        source = staging_dir / "controllers" / relative
        target = package_dir / relative
        target_label = str(target.relative_to(module_dir)).replace("\\", "/")
        if not target.exists():
            pending_files.append((source, target, target_label))
        elif source.read_bytes() == target.read_bytes():
            unchanged_files.append(target_label)
        else:
            conflicting_files.append(target_label)
    if conflicting_files:
        raise SystemExit(
            "Conflicting host files were not modified: "
            + ", ".join(conflicting_files)
            + ". Resolve or rename them before applying the patch."
        )

    applied_files = []
    for source, target, target_label in pending_files:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        applied_files.append(target_label)
    manifest_path = module_dir / "src" / "main" / "AndroidManifest.xml"
    manifest_permissions_added = []
    if manifest_path.is_file() and composition.get("permissions"):
        manifest_permissions_added = ensure_manifest_permissions(
            manifest_path,
            composition.get("permissions", []),
        )
    gradle_changed = ensure_gradle_file_dependency(find_gradle_file(module_dir))
    return {
        "applied_files": applied_files,
        "unchanged_files": unchanged_files,
        "manifest_permissions_added": manifest_permissions_added,
        "gradle_changed": gradle_changed,
        "idempotent": not applied_files and not manifest_permissions_added and not gradle_changed,
    }

def render_incremental_project(args, skill_dir, composition, replacements):
    if args.host_project is None:
        raise SystemExit("--host-project is required for --mode incremental.")
    output_dir = (
        args.output_dir.resolve()
        if args.output_dir is not None
        else args.host_project.resolve() / "meishe-integration-staging"
    )
    if output_dir.exists() and any(output_dir.iterdir()) and not args.force:
        raise SystemExit(f"Staging directory is not empty: {output_dir}. Use --force to overwrite staging files.")
    controllers_dir = output_dir / "controllers"
    controllers_dir.mkdir(parents=True, exist_ok=True)
    rendered_files = render_java_sources(
        java_template_sources(composition),
        skill_dir,
        controllers_dir,
        replacements,
    )
    localize_tree(controllers_dir, skill_dir, args.ui_language)
    manifest = write_patch_manifest(output_dir, args, composition, rendered_files, "incremental")
    if args.apply:
        apply_result = apply_incremental_patch(output_dir, args, composition, rendered_files)
        manifest["apply_result"] = apply_result
        (output_dir / "patch-manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print(f"Created incremental integration staging at {output_dir}")
    print(f"Controllers staged: {', '.join(rendered_files) or '-'}")
    print("Patch manifest: patch-manifest.json")
    if args.apply:
        print_user_build_handoff(args.host_project, args.app_module)
    else:
        print("Gradle handoff is deferred until the reviewed staging patch is applied to the host project.")

def build_api_only_usage(package_name, composition):
    modules = set(composition.get("resolved_modules", []))
    imports = {
        "android.app.Activity",
        "com.meicam.sdk.NvsStreamingContext",
    }
    body = [
        "public final class ApiOnlyUsage {",
        "    private final Activity activity;",
        "    private final MeisheSdkManager sdkManager;",
        "",
        "    public ApiOnlyUsage(Activity activity) {",
        "        if (activity == null) {",
        "            throw new IllegalArgumentException(\"activity is required\");",
        "        }",
        "        this.activity = activity;",
        "        this.sdkManager = new MeisheSdkManager(activity.getApplicationContext());",
        "    }",
        "",
        "    public NvsStreamingContext initialize() {",
        "        return sdkManager.initialize() ? sdkManager.getStreamingContext() : null;",
        "    }",
    ]

    if "timeline-state-store" in modules:
        imports.add("com.meicam.sdk.NvsTimeline")
        body.extend([
            "",
            "    public NvsTimeline createTimelineWithMedia(String mediaPath, int width, int height) {",
            "        NvsStreamingContext context = initialize();",
            "        if (context == null || mediaPath == null || mediaPath.isEmpty()) {",
            "            return null;",
            "        }",
            "        MeisheTimelineController controller = new MeisheTimelineController(context);",
            "        NvsTimeline timeline = controller.createTimeline(width, height);",
            "        return timeline != null && controller.appendClip(mediaPath) != null ? timeline : null;",
            "    }",
        ])

    if "timeline-preview" in modules:
        imports.update({"com.meicam.sdk.NvsLiveWindow", "com.meicam.sdk.NvsTimeline"})
        body.extend([
            "",
            "    public boolean connectPreview(NvsTimeline timeline, NvsLiveWindow liveWindow) {",
            "        NvsStreamingContext context = initialize();",
            "        if (context == null || timeline == null || liveWindow == null) {",
            "            return false;",
            "        }",
            "        MeishePlaybackController playback = new MeishePlaybackController(context);",
            "        playback.connectTimeline(timeline, liveWindow);",
            "        playback.seek(timeline, 0, playback.buildSeekFlags(true, true, false));",
            "        return true;",
            "    }",
        ])

    if "caption-editor" in modules:
        imports.update({"com.meicam.sdk.NvsTimeline", "com.meicam.sdk.NvsTimelineCaption"})
        body.extend([
            "",
            "    public NvsTimelineCaption addCaption(NvsTimeline timeline, String text) {",
            "        if (timeline == null || text == null || text.isEmpty()) {",
            "            return null;",
            "        }",
            "        long durationUs = Math.max(100_000L, Math.min(3_000_000L, timeline.getDuration()));",
            "        MeisheCaptionStickerController captions = new MeisheCaptionStickerController();",
            "        NvsTimelineCaption caption = captions.addCaption(timeline, text, 0, durationUs, null);",
            "        captions.applyReadableDefaultStyle(caption);",
            "        return caption;",
            "    }",
        ])

    if "capture-camera" in modules:
        imports.add("com.meicam.sdk.NvsLiveWindow")
        body.extend([
            "",
            "    public boolean startCapturePreview(NvsLiveWindow liveWindow, int deviceIndex) {",
            "        NvsStreamingContext context = initialize();",
            "        return context != null && liveWindow != null",
            "                && new MeisheCaptureController(context, liveWindow).startPreview(deviceIndex);",
            "    }",
        ])

    if "asset-package-service" in modules:
        body.extend([
            "",
            "    public int installAssetPackage(",
            "            String packagePath,",
            "            String licensePath,",
            "            int packageType,",
            "            MeisheAssetInstaller.InstallCallback callback) {",
            "        NvsStreamingContext context = initialize();",
            "        return context == null ? -1 : new MeisheAssetInstaller(context).installAsynchronously(",
            "                packagePath, licensePath, packageType, callback);",
            "    }",
        ])

    if "template-engine" in modules:
        imports.update({"com.meicam.sdk.NvsAssetPackageManager", "java.util.List"})
        body.extend([
            "",
            "    public List<NvsAssetPackageManager.NvsTemplateFootageDesc> queryTemplateFootages(",
            "            String templatePackageId) {",
            "        NvsStreamingContext context = initialize();",
            "        return new MeisheTemplateWorkflowController().getTemplateFootages(",
            "                context, templatePackageId);",
            "    }",
        ])

    if "export-compile" in modules:
        imports.add("com.meicam.sdk.NvsTimeline")
        body.extend([
            "",
            "    public boolean export(",
            "            NvsTimeline timeline,",
            "            String outputPath,",
            "            NvsStreamingContext.CompileCallback callback,",
            "            NvsStreamingContext.CompileCallback2 completionCallback) {",
            "        NvsStreamingContext context = initialize();",
            "        if (context == null || timeline == null || callback == null || completionCallback == null) {",
            "            return false;",
            "        }",
            "        MeisheExportController exporter = new MeisheExportController(context);",
            "        exporter.registerCompileCallbacks(callback, completionCallback);",
            "        return exporter.export(timeline, outputPath);",
            "    }",
        ])

    body.extend(["}", ""])
    import_lines = [f"import {name};" for name in sorted(imports)]
    return "\n".join([f"package {package_name};", "", *import_lines, "", *body])

def render_api_only_project(args, skill_dir, composition, replacements):
    if args.output_dir is None:
        raise SystemExit("output_dir is required for --mode api-only.")
    output_dir = args.output_dir.resolve()
    if output_dir.exists() and any(output_dir.iterdir()) and not args.force:
        raise SystemExit(f"Output directory is not empty: {output_dir}. Use --force to overwrite api-only files.")
    controllers_dir = output_dir / "controllers"
    sample_dir = output_dir / "sample"
    deps_dir = output_dir / "deps"
    controllers_dir.mkdir(parents=True, exist_ok=True)
    sample_dir.mkdir(parents=True, exist_ok=True)
    deps_dir.mkdir(parents=True, exist_ok=True)
    rendered_files = render_java_sources(
        java_template_sources(composition),
        skill_dir,
        controllers_dir,
        replacements,
    )
    localize_tree(controllers_dir, skill_dir, args.ui_language)
    sample_text = build_api_only_usage(args.package_name, composition)
    (sample_dir / "ApiOnlyUsage.java").write_text(sample_text, encoding="utf-8")
    (deps_dir / "README.md").write_text(
        "\n".join(
            [
                "# Dependencies",
                "",
                "- Add `NvAndroidStreamingSdk.jar` to the host app `libs/` directory.",
                "- Add native libraries under `src/main/jniLibs/<abi>/`.",
                "- Add `meishesdk.lic` to `src/main/assets/`.",
                "- Add optional models/packages listed in `patch-manifest.json` resource keys.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    write_patch_manifest(output_dir, args, composition, rendered_files, "api-only")
    print(f"Created API-only output at {output_dir}")
    print(f"Controllers: {', '.join(rendered_files) or '-'}")

def print_generation_plan(composition):
    print(json.dumps(composition, ensure_ascii=False, indent=2))

def main():
    args = parse_args()
    skill_dir = Path(__file__).resolve().parents[1]
    template_dir = skill_dir / "assets" / "android-template"
    feature_template_dir = skill_dir / "assets" / "android-feature-templates"
    blueprint_template_dir = skill_dir / "assets" / "android-blueprint-templates"
    feature_dirs = available_features(feature_template_dir)
    if args.list_features:
        if feature_dirs:
            print("Available optional feature templates:")
            for name in feature_dirs:
                print(f"- {name}")
        else:
            print("No optional feature templates are available.")
        return
    composition = compose_generation_plan(args, skill_dir)
    if args.dry_run_plan:
        print_generation_plan(composition or {
            "requested_blueprints": [],
            "requested_modules": [],
            "resolved_modules": [],
            "api_recipes": [],
            "resource_keys": [],
            "permissions": [],
            "template_features": [],
            "app_templates": [],
            "simple_code_refs": [],
            "simple_code_ids": [],
            "simple_code_units": [],
            "call_order": [],
            "lifecycle": [],
            "failure_handling": [],
            "warnings": ["No --blueprint or --modules supplied; nothing to compose."],
        })
        return
    validate_package_name(args.package_name)
    validate_sdk_levels(args)
    if not args.app_name.strip():
        raise SystemExit("--app-name cannot be empty")
    replacements = replacement_map(args)
    if args.mode == "incremental":
        render_incremental_project(args, skill_dir, composition, replacements)
        return
    if args.mode == "api-only":
        render_api_only_project(args, skill_dir, composition, replacements)
        return
    if args.output_dir is None:
        raise SystemExit("output_dir is required unless --list-features is used.")
    output_dir = args.output_dir.resolve()
    composed_features = composition.get("template_features", []) if composition else []
    selected_features = parse_features(" ".join([args.features, " ".join(composed_features)]), feature_dirs)
    selected_app_templates = composition.get("app_templates", []) if composition else []
    if args.mode != "new-app":
        selected_app_templates = []
    if len(selected_app_templates) > 1:
        raise SystemExit(
            "Multiple app UI templates were selected: "
            + ", ".join(selected_app_templates)
            + ". Select one app blueprint and compose additional capabilities with --modules."
        )
    selected_abis = parse_abis(args.abis)
    if not template_dir.exists():
        raise SystemExit(f"Missing template directory: {template_dir}")
    if output_dir.exists() and not output_dir.is_dir():
        raise SystemExit(f"Output path exists and is not a directory: {output_dir}")
    if output_dir.exists() and any(output_dir.iterdir()) and not args.force:
        raise SystemExit(f"Output directory is not empty: {output_dir}. Use --force to overwrite template files.")
    sample_assets_dir = None
    if not args.no_sample_assets:
        sample_assets_dir = resolve_sample_assets_dir(skill_dir, args.sample_assets_dir)
        if sample_assets_dir is None:
            print_sample_asset_notice(args.ui_language)
    render_tree(template_dir, output_dir, replacements)
    if selected_app_templates:
        app_template = blueprint_template_dir / selected_app_templates[0]
        if not app_template.is_dir():
            raise SystemExit(f"Missing app blueprint template: {app_template}")
        render_tree(app_template, output_dir, replacements)
    if sample_assets_dir is not None:
        copy_tree(sample_assets_dir, output_dir)
    for feature in selected_features:
        render_tree(feature_dirs[feature], output_dir, replacements)
    localized_file_count = localize_tree(output_dir, skill_dir, args.ui_language)
    permission_names = composition.get("permissions", []) if composition else []
    if permission_names:
        ensure_manifest_permissions(output_dir / "app" / "src" / "main" / "AndroidManifest.xml", permission_names)
    if args.sdk_root is not None:
        copy_sdk_runtime(
            args.sdk_root,
            output_dir,
            selected_abis,
            include_effect_sdk="beauty-ar" in selected_features or args.include_extra_sdk,
            include_extra_sdk=args.include_extra_sdk,
        )
    if args.license is not None:
        copy_file(args.license, output_dir / "app" / "src" / "main" / "assets" / "meishesdk.lic")
    if args.human_models_dir is not None:
        copy_human_models(args.human_models_dir, output_dir)
    print(f"Created Android project template at {output_dir}")
    if composition:
        blueprint_ids = ", ".join(composition.get("requested_blueprints", [])) or "-"
        module_ids = ", ".join(composition.get("resolved_modules", [])) or "-"
        resource_keys = ", ".join(composition.get("resource_keys", [])) or "-"
        simple_code_ids = ", ".join(composition.get("simple_code_ids", [])) or "-"
        print(f"Applied blueprints: {blueprint_ids}")
        print(f"Resolved modules: {module_ids}")
        print(f"Resource keys: {resource_keys}")
        print(f"Simple code ids: {simple_code_ids}")
    if selected_app_templates:
        print(f"Applied app blueprint template: {selected_app_templates[0]}")
    if selected_features:
        print(f"Applied optional feature templates: {', '.join(selected_features)}")
    print(f"Generated UI language: {args.ui_language} ({localized_file_count} localized files).")
    if sample_assets_dir is not None:
        print(f"Copied authorized external sample assets from {sample_assets_dir}.")
    if args.sdk_root is None:
        print("Download https://www.meishesdk.com/downloads -> SDK下载及开发文档 -> Android LTS -> 下载SDK人脸版本, then rerun with --sdk-root <extracted-sdk-root>.")
        print("Expected core paths: lib/android_jar/NvAndroidStreamingSdk.jar and lib/android_arm64/libNvStreamingSdkCore.so.")
    if args.license is None:
        print("Add an authorized Meishe license to app/src/main/assets/meishesdk.lic, or rerun with --license. Contact Meishe business for production license acquisition.")
    needs_human_models = "beauty-ar" in selected_features or (
        composition
        and any(key in {"R8", "R9"} for key in composition.get("resource_keys", []))
    )
    if args.human_models_dir is None and needs_human_models:
        print("Human-detection models are not bundled in the skill. Use --human-models-dir <sdk-root>/samples/android/SdkDemo/app/src/main/assets/facemode from the official Android LTS face package.")
    print_user_build_handoff(output_dir, "app")

if __name__ == "__main__":
    main()
