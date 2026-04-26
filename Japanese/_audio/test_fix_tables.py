import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).parent))

import fix_tables


class FixTablesTests(unittest.TestCase):
    def test_removes_blank_lines_between_table_rows(self):
        before = (
            "| Japanese | English | Audio |\n"
            "|----------|---------|-------|\n"
            "| jp1 | en1 | ![[a1.mp3]] |\n"
            "\n"
            "| jp2 | en2 | ![[a2.mp3]] |\n"
            "\n"
            "| jp3 | en3 | |\n"
        )
        expected = (
            "| Japanese | English | Audio |\n"
            "|----------|---------|-------|\n"
            "| jp1 | en1 | ![[a1.mp3]] |\n"
            "| jp2 | en2 | ![[a2.mp3]] |\n"
            "| jp3 | en3 | |\n"
        )

        fixed, stats = fix_tables.fix_tables(before)

        self.assertEqual(fixed, expected)
        self.assertEqual(stats["blank_lines_removed"], 2)
        self.assertEqual(stats["audio_embeds_merged"], 0)

    def test_merges_audio_embed_into_previous_row(self):
        before = (
            "| Japanese | English | Audio |\n"
            "|----------|---------|-------|\n"
            "| jp1 | en1 | |\n"
            "![[a1.mp3]]\n"
        )
        expected = (
            "| Japanese | English | Audio |\n"
            "|----------|---------|-------|\n"
            "| jp1 | en1 | ![[a1.mp3]] |\n"
        )

        fixed, stats = fix_tables.fix_tables(before)

        self.assertEqual(fixed, expected)
        self.assertEqual(stats["blank_lines_removed"], 0)
        self.assertEqual(stats["audio_embeds_merged"], 1)

    def test_preserves_blank_line_after_table(self):
        before = (
            "Intro\n"
            "\n"
            "| A | B |\n"
            "|---|---|\n"
            "| 1 | 2 |\n"
            "\n"
            "Paragraph\n"
        )

        fixed, stats = fix_tables.fix_tables(before)

        self.assertEqual(fixed, before)
        self.assertEqual(stats["blank_lines_removed"], 0)
        self.assertEqual(stats["audio_embeds_merged"], 0)


if __name__ == "__main__":
    unittest.main()