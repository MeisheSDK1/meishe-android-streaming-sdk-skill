import sys
import unittest
from pathlib import Path


SCRIPT_DIRECTORY = Path(__file__).resolve().parent
SKILL_DIRECTORY = SCRIPT_DIRECTORY.parent
REFERENCE_DIRECTORY = SKILL_DIRECTORY / "references"
sys.path.insert(0, str(SCRIPT_DIRECTORY))

from coverage_summary import build_coverage_summary, expected_artifacts
from reference_markdown import (
    CONTENTS_MARKER_END,
    CONTENTS_MARKER_START,
    markdown_contents_gaps,
    reference_contents_gaps,
    render_markdown_contents,
)


class ReferenceMarkdownContentsTest(unittest.TestCase):
    def test_long_references_have_front_contents(self):
        self.assertEqual([], reference_contents_gaps(REFERENCE_DIRECTORY))

    def test_heading_parser_handles_unicode_fences_and_duplicates(self):
        fixture = "\n".join(
            [
                "# 示例",
                "",
                "说明",
                "",
                "## 中文 标题",
                "",
                "## Source: `md_ch/Mainpage.md`",
                "",
                "```markdown",
                "## Ignored",
                "```",
                "",
                "## Repeat",
                "",
                "## Repeat",
                "",
            ]
        )

        rendered = render_markdown_contents(fixture, minimum_lines=0)

        self.assertIn("- [中文 标题](#中文-标题)", rendered)
        self.assertIn(
            "- [Source: md_ch/Mainpage.md](#source-md_chmainpagemd)",
            rendered,
        )
        self.assertIn("- [Repeat](#repeat)", rendered)
        self.assertIn("- [Repeat](#repeat-1)", rendered)
        self.assertNotIn("- [Ignored]", rendered)
        self.assertEqual([], markdown_contents_gaps(rendered, "fixture.md", 0))

    def test_contents_generation_is_idempotent(self):
        fixture = "\n".join(
            [
                "# Reference",
                "",
                "Intro",
                "",
                "## First",
                "",
                "Body",
                "",
                "## Second",
                "",
            ]
        )

        first_render = render_markdown_contents(fixture, minimum_lines=0)
        second_render = render_markdown_contents(first_render, minimum_lines=0)

        self.assertEqual(first_render, second_render)
        self.assertEqual(1, first_render.count(CONTENTS_MARKER_START))
        self.assertEqual(1, first_render.count(CONTENTS_MARKER_END))

    def test_short_references_are_not_given_generated_contents(self):
        fixture = "# Short\n\n## Section\n\nBody\n"

        self.assertEqual(fixture, render_markdown_contents(fixture))

    def test_generated_markdown_outputs_keep_contents_when_long(self):
        summary = build_coverage_summary(SKILL_DIRECTORY)
        markdown_artifacts = {
            path.name: content
            for path, content in expected_artifacts(
                SKILL_DIRECTORY,
                summary,
            ).items()
            if path.suffix == ".md"
        }

        for reference_name, content in markdown_artifacts.items():
            with self.subTest(reference=reference_name):
                self.assertEqual(
                    [],
                    markdown_contents_gaps(content, reference_name),
                )


if __name__ == "__main__":
    unittest.main()
