from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(r"D:\Vaults\PersonalKB\Japanese")
AUDIO_EMBED_RE = re.compile(r"!\[\[[^\]]+\.mp3\]\]")


def is_table_row(line: str) -> bool:
    return line.strip().startswith("|")


def is_audio_embed(line: str) -> bool:
    return bool(AUDIO_EMBED_RE.fullmatch(line.strip()))


def is_separator_row(line: str) -> bool:
    stripped = line.strip()
    if not stripped.startswith("|"):
        return False
    body = stripped.strip("|").replace(" ", "")
    return bool(body) and set(body) <= {"-", ":"}


def merge_audio_embed_into_row(row: str, embed: str) -> str:
    leading = row[: len(row) - len(row.lstrip())]
    stripped = row.strip()
    parts = stripped.split("|")
    cells = parts[1:-1] if stripped.endswith("|") else parts[1:]
    if not cells:
        return row

    if cells[-1].strip():
        cells[-1] = cells[-1].rstrip() + f" {embed} "
    else:
        cells[-1] = f" {embed} "

    return leading + "|" + "|".join(cells) + "|"


def fix_tables(content: str) -> tuple[str, dict[str, int]]:
    newline = "\r\n" if "\r\n" in content else "\n"
    had_trailing_newline = content.endswith(("\n", "\r"))
    lines = content.splitlines()
    result: list[str] = []
    blank_lines_removed = 0
    audio_embeds_merged = 0
    i = 0

    while i < len(lines):
        line = lines[i]
        if not is_table_row(line):
            result.append(line)
            i += 1
            continue

        result.append(line)
        i += 1

        while i < len(lines):
            current = lines[i]
            stripped = current.strip()

            if stripped == "":
                j = i
                removed = 0
                while j < len(lines) and lines[j].strip() == "":
                    removed += 1
                    j += 1

                if j < len(lines) and (is_table_row(lines[j]) or is_audio_embed(lines[j])):
                    blank_lines_removed += removed
                    i = j
                    continue
                break

            if is_audio_embed(current):
                if result and not is_separator_row(result[-1]):
                    result[-1] = merge_audio_embed_into_row(result[-1], stripped)
                    audio_embeds_merged += 1
                    i += 1
                    continue
                break

            if is_table_row(current):
                result.append(current)
                i += 1
                continue

            break

    fixed = newline.join(result)
    if had_trailing_newline:
        fixed += newline

    return fixed, {
        "blank_lines_removed": blank_lines_removed,
        "audio_embeds_merged": audio_embeds_merged,
    }


def iter_markdown_files(root: Path):
    yield from sorted(root.rglob("*.md"))


def process_file(path: Path) -> dict[str, int | bool]:
    original = path.read_text(encoding="utf-8")
    fixed, stats = fix_tables(original)
    modified = fixed != original
    if modified:
        path.write_text(fixed, encoding="utf-8")
    return {
        "modified": modified,
        "blank_lines_removed": stats["blank_lines_removed"],
        "audio_embeds_merged": stats["audio_embeds_merged"],
    }


def main() -> int:
    files_scanned = 0
    files_modified = 0
    blank_lines_removed = 0
    audio_embeds_merged = 0

    for path in iter_markdown_files(ROOT):
        files_scanned += 1
        stats = process_file(path)
        if stats["modified"]:
            files_modified += 1
        blank_lines_removed += int(stats["blank_lines_removed"])
        audio_embeds_merged += int(stats["audio_embeds_merged"])

    print(f"Scanned {files_scanned} markdown files under {ROOT}")
    print(f"Modified {files_modified} files")
    print(f"Removed {blank_lines_removed} blank lines within tables")
    print(f"Merged {audio_embeds_merged} standalone audio embeds")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())