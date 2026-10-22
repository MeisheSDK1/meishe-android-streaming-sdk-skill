#!/usr/bin/env python3
"""Validate an external offline material bundle and the skill's no-network boundary."""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path

import sys
for _stream in (sys.stdout, sys.stderr):
    if _stream is not None and hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

ASSET_PATH_RE = re.compile(r'"assets:/([^"\r\n]+)"')
FORBIDDEN_RUNTIME_TOKENS = {
    "MeisheAssetCenterClient",
    "MeisheMaterialDownloadManager",
    "MeisheMaterialService",
    "MeisheAuthHeaderProvider",
    "MeisheDemoMaterialCatalog",
    "DEFAULT_SERVICE_BASE_URL",
    "EXTRA_BASE_URL",
    "EXTRA_DEMO_MODE",
    "HttpURLConnection",
    "baseUrl",
    "api/sdkdemo",
    "mall.meishesdk",
    "retrofit2",
    "okhttp3",
    "createDemoIntent",
}
MATERIAL_SUFFIXES = {
    ".animatedsticker",
    ".animatedstickerinanimation",
    ".arscene",
    ".captionanimation",
    ".captioncontext",
    ".captionrenderer",
    ".captionstyle",
    ".capturescene",
    ".compoundcaption",
    ".facemesh",
    ".jpeg",
    ".jpg",
    ".lic",
    ".m4a",
    ".mp3",
    ".mp4",
    ".png",
    ".template",
    ".theme",
    ".ttf",
    ".videofx",
    ".videotransition",
    ".wav",
    ".webp",
}

def skill_dir() -> Path:
    return Path(__file__).resolve().parents[1]

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument(
        "--sample-assets-dir",
        type=Path,
        help="External sample bundle root containing app/src/main/assets.",
    )
    return parser.parse_args()

def is_file(path: Path) -> bool:
    if os.name == "nt":
        return os.path.isfile("\\\\?\\" + str(path.resolve()))
    return path.is_file()

def local_sample_assets_dir(root: Path) -> Path:
    return root.parents[2] / "temp_assets" / "android-sample-assets"

def resolve_sample_assets_dir(root: Path, configured_dir: Path | None) -> Path:
    candidate = configured_dir if configured_dir is not None else local_sample_assets_dir(root)
    return candidate.expanduser().resolve()

def validate(configured_dir: Path | None = None) -> dict:
    root = skill_dir()
    constants_path = (
        root
        / "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheSampleAssets.java"
    )
    catalog_path = (
        root
        / "assets/android-feature-templates/asset-center/app/src/main/java/{{PACKAGE_PATH}}/MeisheLocalMaterialCatalog.java"
    )
    activity_path = (
        root
        / "assets/android-feature-templates/asset-center/app/src/main/java/{{PACKAGE_PATH}}/MeisheAssetCenterActivity.java"
    )
    operations_path = (
        root
        / "assets/android-feature-templates/asset-center/app/src/main/java/{{PACKAGE_PATH}}/MeisheLocalMaterialOperations.java"
    )
    generator_path = root / "scripts/create_android_project.py"
    sample_assets_dir = resolve_sample_assets_dir(root, configured_dir)
    assets_root = sample_assets_dir / "app/src/main/assets"
    runtime_root = root / "assets/android-feature-templates/asset-center"
    embedded_material_files = sorted(
        str(path.relative_to(root)).replace("\\", "/")
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in MATERIAL_SUFFIXES
    )

    missing_files = []
    asset_paths = sorted(set(ASSET_PATH_RE.findall(constants_path.read_text(encoding="utf-8"))))
    for relative_path in asset_paths:
        if not is_file(assets_root / relative_path):
            missing_files.append(relative_path)

    forbidden_hits = []
    for path in runtime_root.rglob("*"):
        if not path.is_file() or path.suffix not in {".java", ".xml"}:
            continue
        text = path.read_text(encoding="utf-8")
        for token in FORBIDDEN_RUNTIME_TOKENS:
            if token in text:
                forbidden_hits.append({"file": str(path.relative_to(root)), "token": token})

    required_symbols = {
        "MeisheLocalMaterialCatalog": catalog_path,
        "installSelectedMaterial": activity_path,
        "registerFont": activity_path,
        "matchingIndexes": operations_path,
        "installBundledPackage": operations_path,
        "registerBundledFont": operations_path,
    }
    missing_symbols = [
        symbol
        for symbol, path in required_symbols.items()
        if symbol not in path.read_text(encoding="utf-8")
    ]
    generator_text = generator_path.read_text(encoding="utf-8")
    if 'if "asset-center" in selected_features' in generator_text:
        forbidden_hits.append(
            {
                "file": str(generator_path.relative_to(root)),
                "token": "asset-center permission override",
            }
        )

    result = {
        "sample_assets_dir": str(sample_assets_dir),
        "sample_assets_available": assets_root.is_dir(),
        "embedded_material_files": embedded_material_files,
        "asset_path_count": len(asset_paths),
        "missing_files": missing_files,
        "forbidden_runtime_hits": forbidden_hits,
        "missing_symbols": missing_symbols,
    }
    result["passed"] = not any(
        (embedded_material_files, missing_files, forbidden_hits, missing_symbols)
    )
    return result

def main() -> int:
    args = parse_args()
    result = validate(args.sample_assets_dir)
    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("PASS" if result["passed"] else "FAIL")
        print(f"catalog asset paths: {result['asset_path_count']}")
        for key in (
            "embedded_material_files",
            "missing_files",
            "forbidden_runtime_hits",
            "missing_symbols",
        ):
            if result[key]:
                print(f"{key}: {result[key]}")
    return 0 if result["passed"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
