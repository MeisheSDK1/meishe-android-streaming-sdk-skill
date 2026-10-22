#!/usr/bin/env python3
"""Search the compact Meishe Android Streaming SDK API skill lookup index."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import sys
for _stream in (sys.stdout, sys.stderr):
    if _stream is not None and hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

GENERIC_TERMS = {"android", "api", "sdk"}

def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="*", help="User request or SDK/API terms.")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--list", action="store_true", dest="list_entries")
    parser.add_argument("--compact", action="store_true", help="Truncate simple-code id lists; keep routing fields.")
    return parser.parse_args()

def normalize(value):
    return value.casefold()

def split_terms(query):
    raw_terms = re.split("[\\s,\\uFF0C\\u3001|;:\\uFF1A()\\uFF08\\uFF09\\[\\]{}<>]+", query)
    return [
        term.casefold()
        for term in raw_terms
        if term.strip() and term.casefold() not in GENERIC_TERMS
    ]

def load_index():
    skill_dir = Path(__file__).resolve().parents[1]
    index_path = skill_dir / "references" / "skill-lookup-index.json"
    with index_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)

def text_fields(entry):
    fields = [entry["id"], entry["title"], entry["category"]]
    for key in (
        "aliases",
        "api_classes",
        "feature_refs",
        "api_refs",
        "snippet_refs",
        "official_refs",
        "resource_keys",
        "optional_template_features",
        "module_ids",
        "blueprint_ids",
        "simple_code_refs",
        "simple_code_ids",
    ):
        fields.extend(entry.get(key, []))
    return [normalize(str(field)) for field in fields]

def score_entry(query, terms, entry):
    fields = text_fields(entry)
    joined = " ".join(fields)
    score = 0
    if query and query in fields:
        score += 150
    elif query and query in joined:
        score += 30
    for term in terms:
        for field in fields:
            if term == field:
                score += 18
            elif term in field:
                score += 8
            elif field in term and len(field) > 1:
                score += 6
    return score

def compact_entry(entry, score=None, fallback=False, compact=False):
    result = {
        "id": entry["id"],
        "title": entry["title"],
        "category": entry["category"],
        "resource_keys": entry.get("resource_keys", []),
        "snippet_refs": entry.get("snippet_refs", []),
        "api_refs": entry.get("api_refs", []),
        "official_refs": entry.get("official_refs", []),
        "optional_template_features": entry.get("optional_template_features", []),
        "module_ids": entry.get("module_ids", []),
        "blueprint_ids": entry.get("blueprint_ids", []),
        "simple_code_refs": entry.get("simple_code_refs", []),
        "simple_code_ids": entry.get("simple_code_ids", []),
    }
    if score is not None:
        result["score"] = score
    if fallback:
        result["fallback"] = True
    if compact and result.get("simple_code_ids"):
        result["simple_code_ids_total"] = len(result["simple_code_ids"])
        result["simple_code_ids"] = result["simple_code_ids"][:20]
    return result

def print_entry(index, entry, rank=None, score=None, compact=False):
    prefix = f"{rank}. " if rank is not None else "- "
    score_text = f" score={score}" if score is not None else ""
    print(f"{prefix}{entry['id']} - {entry['title']} ({entry['category']}){score_text}")
    print(f"   resources: {', '.join(entry.get('resource_keys', [])) or '-'}")
    print(f"   snippets: {', '.join(entry.get('snippet_refs', [])) or '-'}")
    print(f"   api refs: {', '.join(entry.get('api_refs', [])) or '-'}")
    print(f"   official refs: {', '.join(entry.get('official_refs', [])) or '-'}")
    modules = entry.get("module_ids", [])
    if modules:
        print(f"   modules: {', '.join(modules)}")
    blueprints = entry.get("blueprint_ids", [])
    if blueprints:
        print(f"   blueprints: {', '.join(blueprints)}")
    simple_code_refs = entry.get("simple_code_refs", [])
    if simple_code_refs:
        print(f"   simple code refs: {', '.join(simple_code_refs)}")
    simple_code_ids = entry.get("simple_code_ids", [])
    if simple_code_ids:
        if compact:
            print(f"   simple code ids: {len(simple_code_ids)} total (rerun without --compact to list)")
        else:
            print(f"   simple code ids: {', '.join(simple_code_ids)}")
    templates = entry.get("optional_template_features", [])
    if templates:
        print(f"   optional templates: {', '.join(templates)}")

def main():
    args = parse_args()
    index = load_index()
    entries = index.get("entries", [])
    if args.list_entries:
        if args.as_json:
            print(json.dumps([compact_entry(entry) for entry in entries], ensure_ascii=False, indent=2))
        else:
            for entry in entries:
                print_entry(index, entry)
        return

    query = normalize(" ".join(args.query).strip())
    if not query:
        raise SystemExit("Provide a query or use --list.")
    if args.limit <= 0:
        raise SystemExit("--limit must be positive.")
    terms = split_terms(query)
    scored = [(score_entry(query, terms, entry), entry) for entry in entries]
    matches = [(score, entry) for score, entry in scored if score > 0]
    matches.sort(key=lambda item: (-item[0], item[1]["id"]))
    used_fallback = False
    if not matches:
        used_fallback = True
        fallback_ids = {"core-lifecycle", "timeline-editing", "preview-playback-export"}
        matches = [(0, entry) for entry in entries if entry["id"] in fallback_ids]
    matches = matches[: args.limit]
    if args.as_json:
        print(json.dumps([compact_entry(entry, score, fallback=used_fallback, compact=args.compact) for score, entry in matches], ensure_ascii=False, indent=2))
    else:
        print(f"Query: {query}")
        print("Read `resource-requirements-index.md` for the listed resource keys before generating runtime-dependent features.")
        if used_fallback:
            print("No exact matches; showing fallback entries below.")
        for rank, (score, entry) in enumerate(matches, start=1):
            print_entry(index, entry, rank=rank, score=score, compact=args.compact)

if __name__ == "__main__":
    main()
