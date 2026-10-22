#!/usr/bin/env python3
"""Extract candidate SDK simple-code evidence from an external Meishe Demo root.

This script is build-time only. It may read an external SdkDemo folder when the
skill author is refreshing bundled references. Generated apps and normal skill
use must not depend on this script or on the external Demo path.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import sys
for _stream in (sys.stdout, sys.stderr):
    if _stream is not None and hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

SDK_TOKEN_RE = re.compile(r"\b(Nvs[A-Za-z0-9_]+)\b")
METHOD_RE = re.compile(
    r"^\s*(?:public|private|protected)?\s*(?:static\s+)?(?:final\s+)?[\w<>\[\], ?]+\s+(\w+)\s*\([^;]*\)\s*\{"
)

def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demo-root", type=Path, required=True, help="External SdkDemo root to scan.")
    parser.add_argument("--output", type=Path, help="Optional JSON output path. Defaults to stdout.")
    parser.add_argument("--max-files", type=int, default=0, help="Optional limit for quick inspection.")
    return parser.parse_args()

def iter_source_files(root):
    ignored_parts = {"build", ".gradle", ".idea", "captures", "outputs"}
    for suffix in ("*.java", "*.kt"):
        for path in root.rglob(suffix):
            if ignored_parts & set(path.parts):
                continue
            yield path

def nearest_method(lines, index):
    for line_index in range(index, max(-1, index - 80), -1):
        match = METHOD_RE.match(lines[line_index])
        if match:
            return match.group(1)
    return "<unknown>"

def extract_file(root, path):
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    lines = text.splitlines()
    candidates = []
    for index, line in enumerate(lines):
        tokens = sorted(set(SDK_TOKEN_RE.findall(line)))
        if not tokens and "com.meicam" not in line:
            continue
        start = max(0, index - 2)
        end = min(len(lines), index + 3)
        candidates.append(
            {
                "source_label": f"{path.relative_to(root).as_posix()}:{index + 1}",
                "method": nearest_method(lines, index),
                "api_classes": tokens,
                "line": line.strip(),
                "context": [value.rstrip() for value in lines[start:end]],
            }
        )
    return candidates

def main():
    args = parse_args()
    root = args.demo_root.resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Missing demo root: {root}")
    all_candidates = []
    scanned_files = 0
    for source_file in iter_source_files(root):
        scanned_files += 1
        all_candidates.extend(extract_file(root, source_file))
        if args.max_files and scanned_files >= args.max_files:
            break
    result = {
        "demo_root": str(root),
        "scanned_files": scanned_files,
        "candidate_count": len(all_candidates),
        "candidates": all_candidates,
        "note": "Build-time extraction only. Source labels are provenance; skill use must not read this external path.",
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    from demo_knowledge_builder import main as build_standalone_knowledge

    build_standalone_knowledge()
