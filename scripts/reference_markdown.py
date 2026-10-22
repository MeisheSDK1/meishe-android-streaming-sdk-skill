#!/usr/bin/env python3
"""Generate and validate clickable contents sections for long references."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import unicodedata
from dataclasses import dataclass, replace
from pathlib import Path
from urllib.parse import unquote


LONG_REFERENCE_MINIMUM_LINES = 100
CONTENTS_MARKER_START = "<!-- BEGIN GENERATED CONTENTS -->"
CONTENTS_MARKER_END = "<!-- END GENERATED CONTENTS -->"
CONTENTS_TITLES = {"contents", "table of contents"}
ATX_HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*$")
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
CONTENT_LINK_RE = re.compile(r"^\s*-\s+\[(.*)\]\(#([^)]+)\)\s*$")
INLINE_LINK_RE = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
REFERENCE_LINK_RE = re.compile(r"!?\[([^\]]*)\]\[[^\]]*\]")
HTML_TAG_RE = re.compile(r"<[^>]+>")


@dataclass(frozen=True)
class MarkdownHeading:
    level: int
    title: str
    line_number: int
    anchor: str = ""


def skill_directory() -> Path:
    return Path(__file__).resolve().parents[1]


def _without_html_comments(line: str, in_comment: bool) -> tuple[str, bool]:
    visible_parts = []
    remaining = line
    while remaining:
        if in_comment:
            comment_end = remaining.find("-->")
            if comment_end < 0:
                return "".join(visible_parts), True
            remaining = remaining[comment_end + 3 :]
            in_comment = False
            continue
        comment_start = remaining.find("<!--")
        if comment_start < 0:
            visible_parts.append(remaining)
            break
        visible_parts.append(remaining[:comment_start])
        remaining = remaining[comment_start + 4 :]
        in_comment = True
    return "".join(visible_parts), in_comment


def parse_markdown_headings(text: str) -> list[MarkdownHeading]:
    headings = []
    fence_character = ""
    fence_length = 0
    in_comment = False
    for line_number, line in enumerate(text.splitlines(), 1):
        visible_line, in_comment = _without_html_comments(line, in_comment)
        fence_match = FENCE_RE.match(visible_line)
        if fence_character:
            if (
                fence_match
                and fence_match.group(1)[0] == fence_character
                and len(fence_match.group(1)) >= fence_length
            ):
                fence_character = ""
                fence_length = 0
            continue
        if fence_match:
            fence_character = fence_match.group(1)[0]
            fence_length = len(fence_match.group(1))
            continue
        if visible_line.startswith("    ") or visible_line.startswith("\t"):
            continue
        heading_match = ATX_HEADING_RE.match(visible_line)
        if not heading_match:
            continue
        title = re.sub(r"[ \t]+#+[ \t]*$", "", heading_match.group(2)).strip()
        if title:
            headings.append(
                MarkdownHeading(
                    level=len(heading_match.group(1)),
                    title=title,
                    line_number=line_number,
                )
            )
    return headings


def plain_heading_text(title: str) -> str:
    plain_text = html.unescape(title)
    plain_text = INLINE_LINK_RE.sub(r"\1", plain_text)
    plain_text = REFERENCE_LINK_RE.sub(r"\1", plain_text)
    plain_text = HTML_TAG_RE.sub("", plain_text)
    plain_text = plain_text.replace("`", "")
    return plain_text.strip()


def heading_anchor_base(title: str) -> str:
    plain_text = plain_heading_text(title).casefold()
    anchor_characters = []
    pending_space = False
    for character in plain_text:
        if character.isspace():
            pending_space = bool(anchor_characters)
            continue
        category = unicodedata.category(character)
        if character.isalnum() or character in {"-", "_"} or category.startswith("M"):
            if pending_space and anchor_characters[-1] != "-":
                anchor_characters.append("-")
            anchor_characters.append(character)
        pending_space = False
    anchor = "".join(anchor_characters).strip("-")
    return anchor or "section"


def headings_with_anchors(text: str) -> list[MarkdownHeading]:
    anchor_counts: dict[str, int] = {}
    anchored_headings = []
    for heading in parse_markdown_headings(text):
        anchor_base = heading_anchor_base(heading.title)
        duplicate_index = anchor_counts.get(anchor_base, 0)
        anchor_counts[anchor_base] = duplicate_index + 1
        anchor = (
            anchor_base
            if duplicate_index == 0
            else f"{anchor_base}-{duplicate_index}"
        )
        anchored_headings.append(replace(heading, anchor=anchor))
    return anchored_headings


def _remove_generated_contents(text: str) -> tuple[str, bool]:
    start_index = text.find(CONTENTS_MARKER_START)
    end_index = text.find(CONTENTS_MARKER_END)
    if start_index < 0 and end_index < 0:
        return text, False
    if start_index < 0 or end_index < start_index:
        return text, False
    end_index += len(CONTENTS_MARKER_END)
    if end_index < len(text) and text[end_index] == "\n":
        end_index += 1
    return text[:start_index] + text[end_index:], True


def _remove_legacy_contents(text: str) -> tuple[str, bool]:
    lines = text.splitlines()
    headings = parse_markdown_headings(text)
    contents_heading = next(
        (
            heading
            for heading in headings
            if heading.level == 2
            and plain_heading_text(heading.title).casefold() in CONTENTS_TITLES
        ),
        None,
    )
    if contents_heading is None:
        return text, False
    section_end = len(lines)
    for heading in headings:
        if (
            heading.line_number > contents_heading.line_number
            and heading.level <= contents_heading.level
        ):
            section_end = heading.line_number - 1
            break
    section_start = contents_heading.line_number - 1
    updated_lines = lines[:section_start] + lines[section_end:]
    return "\n".join(updated_lines), True


def remove_contents_section(text: str) -> str:
    text_without_generated, removed_generated = _remove_generated_contents(text)
    if removed_generated:
        return text_without_generated
    text_without_legacy, _ = _remove_legacy_contents(text)
    return text_without_legacy


def _insert_contents_block(text: str, contents_lines: list[str]) -> str:
    lines = text.splitlines()
    first_h2 = next(
        (heading for heading in parse_markdown_headings(text) if heading.level == 2),
        None,
    )
    if first_h2 is None:
        return text
    insertion_index = first_h2.line_number - 1
    prefix = lines[:insertion_index]
    suffix = lines[insertion_index:]
    while prefix and not prefix[-1].strip():
        prefix.pop()
    while suffix and not suffix[0].strip():
        suffix.pop(0)
    block = [
        CONTENTS_MARKER_START,
        "## Contents",
        "",
        *contents_lines,
        CONTENTS_MARKER_END,
    ]
    return "\n".join([*prefix, "", *block, "", *suffix]).rstrip() + "\n"


def render_markdown_contents(
    text: str,
    minimum_lines: int = LONG_REFERENCE_MINIMUM_LINES,
) -> str:
    normalized_text = text.replace("\r\n", "\n").replace("\r", "\n")
    text_without_contents = remove_contents_section(normalized_text)
    if len(text_without_contents.splitlines()) <= minimum_lines:
        return normalized_text if normalized_text.endswith("\n") else normalized_text + "\n"
    if not any(
        heading.level == 2 for heading in parse_markdown_headings(text_without_contents)
    ):
        return (
            text_without_contents
            if text_without_contents.endswith("\n")
            else text_without_contents + "\n"
        )

    contents_skeleton = _insert_contents_block(text_without_contents, [])
    target_headings = [
        heading
        for heading in headings_with_anchors(contents_skeleton)
        if heading.level == 2 and plain_heading_text(heading.title) != "Contents"
    ]
    contents_lines = [
        f"- [{_escape_link_label(plain_heading_text(heading.title))}](#{heading.anchor})"
        for heading in target_headings
    ]
    return _insert_contents_block(text_without_contents, contents_lines)


def _escape_link_label(label: str) -> str:
    return label.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


def markdown_contents_gaps(
    text: str,
    reference_name: str,
    minimum_lines: int = LONG_REFERENCE_MINIMUM_LINES,
) -> list[dict]:
    if len(text.splitlines()) <= minimum_lines:
        return []
    gaps = []
    headings = headings_with_anchors(text)
    contents_headings = [
        heading
        for heading in headings
        if heading.level == 2 and heading.title.strip() == "Contents"
    ]
    if len(contents_headings) != 1:
        return [
            {
                "file": reference_name,
                "kind": "contents_count",
                "expected": 1,
                "actual": len(contents_headings),
            }
        ]
    contents_heading = contents_headings[0]
    h2_headings = [heading for heading in headings if heading.level == 2]
    if h2_headings[0] != contents_heading:
        gaps.append(
            {
                "file": reference_name,
                "kind": "contents_position",
                "reason": "Contents must be the first H2 heading.",
                "line": contents_heading.line_number,
            }
        )
    if contents_heading.line_number > 40:
        gaps.append(
            {
                "file": reference_name,
                "kind": "contents_position",
                "reason": "Contents must appear within the first 40 lines.",
                "line": contents_heading.line_number,
            }
        )
    if text.count(CONTENTS_MARKER_START) != 1 or text.count(CONTENTS_MARKER_END) != 1:
        gaps.append(
            {
                "file": reference_name,
                "kind": "contents_markers",
                "reason": "Generated Contents markers must appear exactly once.",
            }
        )
    legacy_headings = [
        heading
        for heading in h2_headings
        if plain_heading_text(heading.title).casefold() == "table of contents"
    ]
    if legacy_headings:
        gaps.append(
            {
                "file": reference_name,
                "kind": "legacy_contents",
                "lines": [heading.line_number for heading in legacy_headings],
            }
        )

    lines = text.splitlines()
    section_end = len(lines)
    for heading in h2_headings:
        if heading.line_number > contents_heading.line_number:
            section_end = heading.line_number - 1
            break
    contents_lines = lines[contents_heading.line_number:section_end]
    actual_fragments = []
    unexpected_lines = []
    for line_number, line in enumerate(
        contents_lines,
        contents_heading.line_number + 1,
    ):
        stripped = line.strip()
        if not stripped or stripped in {CONTENTS_MARKER_START, CONTENTS_MARKER_END}:
            continue
        link_match = CONTENT_LINK_RE.match(line)
        if link_match:
            actual_fragments.append(unquote(link_match.group(2)))
        else:
            unexpected_lines.append(line_number)
    if unexpected_lines:
        gaps.append(
            {
                "file": reference_name,
                "kind": "contents_format",
                "lines": unexpected_lines,
            }
        )

    expected_fragments = [
        heading.anchor for heading in h2_headings if heading != contents_heading
    ]
    if not expected_fragments:
        gaps.append(
            {
                "file": reference_name,
                "kind": "contents_targets",
                "reason": "Long reference has no navigable H2 section.",
            }
        )
    elif actual_fragments != expected_fragments:
        gaps.append(
            {
                "file": reference_name,
                "kind": "contents_links",
                "expected": expected_fragments,
                "actual": actual_fragments,
            }
        )
    return gaps


def reference_contents_gaps(
    references_directory: Path,
    minimum_lines: int = LONG_REFERENCE_MINIMUM_LINES,
) -> list[dict]:
    gaps = []
    for reference_path in sorted(references_directory.glob("*.md")):
        gaps.extend(
            markdown_contents_gaps(
                reference_path.read_text(encoding="utf-8"),
                reference_path.name,
                minimum_lines,
            )
        )
    return gaps


def write_reference_contents(
    references_directory: Path,
    minimum_lines: int = LONG_REFERENCE_MINIMUM_LINES,
) -> list[str]:
    updated_files = []
    for reference_path in sorted(references_directory.glob("*.md")):
        original_text = reference_path.read_text(encoding="utf-8")
        updated_text = render_markdown_contents(original_text, minimum_lines)
        if updated_text != original_text:
            reference_path.write_text(updated_text, encoding="utf-8")
            updated_files.append(reference_path.name)
    return updated_files


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--references-dir",
        type=Path,
        default=skill_directory() / "references",
        help="Reference directory to maintain.",
    )
    parser.add_argument(
        "--minimum-lines",
        type=int,
        default=LONG_REFERENCE_MINIMUM_LINES,
        help="Only require Contents when a Markdown file exceeds this line count.",
    )
    parser.add_argument("--write", action="store_true", help="Write generated Contents.")
    parser.add_argument("--check", action="store_true", help="Fail on navigation gaps.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    references_directory = args.references_dir.resolve()
    updated_files = (
        write_reference_contents(references_directory, args.minimum_lines)
        if args.write
        else []
    )
    gaps = (
        reference_contents_gaps(references_directory, args.minimum_lines)
        if args.check
        else []
    )
    result = {
        "references_directory": str(references_directory),
        "minimum_lines": args.minimum_lines,
        "updated_count": len(updated_files),
        "updated_files": updated_files,
        "gap_count": len(gaps),
        "gaps": gaps,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if args.check and gaps:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
