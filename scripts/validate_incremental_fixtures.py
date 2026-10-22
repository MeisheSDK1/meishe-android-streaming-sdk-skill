#!/usr/bin/env python3
"""Validate incremental generation against Java/Kotlin and Groovy/KTS hosts."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    if _stream is not None and hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

AGP_VERSION = "8.13.2"
KOTLIN_VERSION = "2.2.20"

def parse_args():
    repo_root = Path(__file__).resolve().parents[4]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-root",
        type=Path,
        default=repo_root
        / ".tmp"
        / "incremental-fixtures"
        / ("run-" + datetime.now().strftime("%Y%m%d-%H%M%S")),
    )
    parser.add_argument(
        "--sdk-root",
        type=Path,
        required=True,
        help="Extracted Meishe Android SDK root containing lib/, extrasdk/, and samples/.",
    )
    parser.add_argument("--skip-build", action="store_true")
    parser.add_argument(
        "--modules",
        default="timeline-state-store",
        help="Comma-separated module ids to apply to each host fixture.",
    )
    parser.add_argument(
        "--verify-idempotency",
        action="store_true",
        help="Apply the same patch twice and require the second apply to be idempotent.",
    )
    return parser.parse_args()

def skill_dir():
    return Path(__file__).resolve().parents[1]

def repo_root():
    return Path(__file__).resolve().parents[4]

def run_command(args, cwd, label):
    result = subprocess.run(
        args,
        cwd=cwd,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if result.returncode != 0:
        print(f"\n--- {label} failed ({result.returncode}) ---")
        print("\n".join(result.stdout.splitlines()[-160:]))
        raise SystemExit(result.returncode)
    return result.stdout

def ensure_empty_target(path):
    if path.exists() and any(path.iterdir()):
        raise SystemExit(f"Output root is not empty: {path}")
    path.mkdir(parents=True, exist_ok=True)

def package_for(name):
    return "com.example.incremental." + name.replace("-", "")

def write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")

def convert_root_to_kts(host_dir, app_name, uses_kotlin):
    settings_gradle = host_dir / "settings.gradle"
    build_gradle = host_dir / "build.gradle"
    if settings_gradle.exists():
        settings_gradle.unlink()
    if build_gradle.exists():
        build_gradle.unlink()
    write_text(
        host_dir / "settings.gradle.kts",
        f"""
        pluginManagement {{
            repositories {{
                google()
                mavenCentral()
                gradlePluginPortal()
            }}
        }}
        dependencyResolutionManagement {{
            repositoriesMode.set(RepositoriesMode.PREFER_PROJECT)
            repositories {{
                google()
                mavenCentral()
            }}
        }}
        rootProject.name = "{app_name}"
        include(":app")
        """,
    )
    kotlin_plugin = (
        f'    id("org.jetbrains.kotlin.android") version "{KOTLIN_VERSION}" apply false\n'
        if uses_kotlin
        else ""
    )
    write_text(
        host_dir / "build.gradle.kts",
        f"""
        plugins {{
            id("com.android.application") version "{AGP_VERSION}" apply false
        {kotlin_plugin.rstrip()}
        }}
        """,
    )

def convert_root_to_groovy_kotlin(host_dir):
    build_gradle = host_dir / "build.gradle"
    text = build_gradle.read_text(encoding="utf-8")
    marker = f'        classpath "com.android.tools.build:gradle:{AGP_VERSION}"'
    kotlin_line = f'        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:{KOTLIN_VERSION}"'
    if kotlin_line not in text:
        text = text.replace(marker, marker + "\n" + kotlin_line, 1)
    build_gradle.write_text(text, encoding="utf-8")

def write_app_build_kts(app_dir, package_name, uses_kotlin):
    kotlin_plugin = '    id("org.jetbrains.kotlin.android")\n' if uses_kotlin else ""
    kotlin_target = (
        """
        tasks.withType<org.jetbrains.kotlin.gradle.tasks.KotlinCompile>().configureEach {
            compilerOptions {
                jvmTarget.set(org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_1_8)
            }
        }
        """
        if uses_kotlin
        else ""
    )
    write_text(
        app_dir / "build.gradle.kts",
        f"""
        plugins {{
            id("com.android.application")
        {kotlin_plugin.rstrip()}
        }}

        android {{
            namespace = "{package_name}"
            compileSdk = 35

            defaultConfig {{
                applicationId = "{package_name}"
                minSdk = 19
                targetSdk = 35
                versionCode = 1
                versionName = "1.0"

                ndk {{
                    abiFilters += "arm64-v8a"
                }}
            }}

            compileOptions {{
                sourceCompatibility = JavaVersion.VERSION_1_8
                targetCompatibility = JavaVersion.VERSION_1_8
            }}
        }}

        repositories {{
            google()
            mavenCentral()
            flatDir {{
                dirs("libs")
            }}
        }}

        dependencies {{
            implementation(fileTree(mapOf("dir" to "libs", "include" to listOf("*.jar", "*.aar"))))
        }}

        {kotlin_target.strip()}
        """,
    )
    groovy_file = app_dir / "build.gradle"
    if groovy_file.exists():
        groovy_file.unlink()

def add_kotlin_host_activity(app_dir, package_name):
    package_path = Path(*package_name.split("."))
    java_activity = app_dir / "src" / "main" / "java" / package_path / "MainActivity.java"
    if java_activity.exists():
        java_activity.unlink()
    write_text(
        app_dir / "src" / "main" / "java" / package_path / "MainActivity.kt",
        f"""
        package {package_name}

        import android.app.Activity
        import android.os.Bundle

        class MainActivity : Activity() {{
            override fun onCreate(savedInstanceState: Bundle?) {{
                super.onCreate(savedInstanceState)
            }}
        }}
        """,
    )

def convert_app_to_kotlin_groovy(app_dir):
    build_gradle = app_dir / "build.gradle"
    text = build_gradle.read_text(encoding="utf-8")
    plugin_line = 'apply plugin: "org.jetbrains.kotlin.android"'
    if plugin_line not in text:
        text = text.replace('apply plugin: "com.android.application"', 'apply plugin: "com.android.application"\n' + plugin_line, 1)
    target_block = """

tasks.withType(org.jetbrains.kotlin.gradle.tasks.KotlinCompile).configureEach {
    compilerOptions {
        jvmTarget.set(org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_1_8)
    }
}
"""
    if "JvmTarget.JVM_1_8" not in text:
        text = text.rstrip() + target_block
    build_gradle.write_text(text, encoding="utf-8")

def generate_host(host_dir, package_name, app_name, sdk_root):
    script = skill_dir() / "scripts" / "create_android_project.py"
    run_command(
        [
            sys.executable,
            str(script),
            str(host_dir),
            "--package",
            package_name,
            "--app-name",
            app_name,
            "--sdk-root",
            str(sdk_root),
            "--force",
        ],
        repo_root(),
        f"generate {host_dir.name}",
    )

def apply_incremental(host_dir, package_name, modules):
    script = skill_dir() / "scripts" / "create_android_project.py"
    run_command(
        [
            sys.executable,
            str(script),
            "--mode",
            "incremental",
            "--host-project",
            str(host_dir),
            "--app-module",
            "app",
            "--modules",
            modules,
            "--package",
            package_name,
            "--app-name",
            host_dir.name,
            "--apply",
            "--force",
        ],
        repo_root(),
        f"apply incremental {host_dir.name}",
    )

def verify_patch(host_dir, package_name):
    manifest_path = host_dir / "meishe-integration-staging" / "patch-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    apply_result = manifest.get("apply_result", {})
    applied_files = apply_result.get("applied_files", [])
    unchanged_files = apply_result.get("unchanged_files", [])
    if not applied_files and not unchanged_files:
        raise SystemExit(f"No files were applied or retained for {host_dir.name}")
    app_dir = host_dir / "app"
    gradle_candidates = [app_dir / "build.gradle", app_dir / "build.gradle.kts"]
    gradle_text = "\n".join(
        path.read_text(encoding="utf-8") for path in gradle_candidates if path.exists()
    )
    if "NvAndroidStreamingSdk.jar" not in gradle_text:
        raise SystemExit(f"NvAndroidStreamingSdk.jar dependency was not patched for {host_dir.name}")
    package_dir = app_dir / "src" / "main" / "java" / Path(*package_name.split("."))
    for filename in manifest.get("controllers", []):
        if not (package_dir / filename).is_file():
            raise SystemExit(f"Missing applied controller {filename} for {host_dir.name}")

def build_fixture(host_dir):
    gradlew = "gradlew.bat" if os.name == "nt" else "./gradlew"
    run_command(
        [str(host_dir / gradlew), ":app:assembleDebug", "--stacktrace", "--no-daemon"],
        host_dir,
        f"build {host_dir.name}",
    )
    apk = host_dir / "app" / "build" / "outputs" / "apk" / "debug" / "app-debug.apk"
    if not apk.is_file():
        raise SystemExit(f"Missing debug APK for {host_dir.name}: {apk}")

def prepare_variant(
    output_root,
    name,
    source_language,
    gradle_style,
    sdk_root,
    modules,
    verify_idempotency,
):
    package_name = package_for(name)
    host_dir = output_root / name
    app_name = "Incremental " + name
    generate_host(host_dir, package_name, app_name, sdk_root)
    app_dir = host_dir / "app"
    uses_kotlin = source_language == "kotlin"
    if gradle_style == "kts":
        convert_root_to_kts(host_dir, app_name, uses_kotlin)
        write_app_build_kts(app_dir, package_name, uses_kotlin)
    elif uses_kotlin:
        convert_root_to_groovy_kotlin(host_dir)
        convert_app_to_kotlin_groovy(app_dir)
    if uses_kotlin:
        add_kotlin_host_activity(app_dir, package_name)
    apply_incremental(host_dir, package_name, modules)
    verify_patch(host_dir, package_name)
    if verify_idempotency:
        apply_incremental(host_dir, package_name, modules)
        verify_patch(host_dir, package_name)
        manifest_path = host_dir / "meishe-integration-staging" / "patch-manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if not manifest.get("apply_result", {}).get("idempotent"):
            raise SystemExit(f"Repeated patch was not idempotent for {host_dir.name}")
    return host_dir

def main():
    args = parse_args()
    output_root = args.output_root.resolve()
    sdk_root = args.sdk_root.resolve()
    ensure_empty_target(output_root)
    variants = [
        ("java-groovy", "java", "groovy"),
        ("java-kts", "java", "kts"),
        ("kotlin-groovy", "kotlin", "groovy"),
        ("kotlin-kts", "kotlin", "kts"),
    ]
    hosts = []
    for name, source_language, gradle_style in variants:
        host_dir = prepare_variant(
            output_root,
            name,
            source_language,
            gradle_style,
            sdk_root,
            args.modules,
            args.verify_idempotency,
        )
        hosts.append(host_dir)
        print(f"prepared {name}")
    if not args.skip_build:
        for host_dir in hosts:
            build_fixture(host_dir)
            print(f"built {host_dir.name}")
    print("incremental fixture validation passed")

if __name__ == "__main__":
    main()
