"""Audit Japanese audio embed resolution and MP3 format compatibility."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


SCRIPT_PATH = Path(__file__).resolve()
DEFAULT_AUDIO_DIR = SCRIPT_PATH.parent
DEFAULT_JAPANESE_ROOT = DEFAULT_AUDIO_DIR.parent
DEFAULT_VAULT_ROOT = DEFAULT_JAPANESE_ROOT.parent
DEFAULT_REPORT_PATH = DEFAULT_VAULT_ROOT / "_ops" / "reports" / "japanese-audio-integrity-audit.txt"
DEFAULT_MANIFEST_PATH = DEFAULT_AUDIO_DIR / "pronunciation_manifest.json"

EMBED_RE = re.compile(r"!\[\[([^\]]+\.mp3)(?:#[^\]]*)?\]\]")
EXCLUDED_DIRS = {"_audio", "_raw", "_chunks", "_queries", "_templates"}
EXPECTED_CODEC = "mp3"
EXPECTED_SAMPLE_RATE = "48000"
EXPECTED_CHANNELS = 1
EXPECTED_BIT_RATE = "96000"
URL_SENSITIVE_FILENAME_RE = re.compile(r"[\s+#%?&]")

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_JAPANESE_ROOT,
        help="Japanese wiki root; defaults to the parent of this script's _audio directory.",
    )
    parser.add_argument(
        "--audio-dir",
        type=Path,
        help="Audio directory; defaults to <root>/_audio.",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        help="Pronunciation manifest path; defaults to <audio-dir>/pronunciation_manifest.json.",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=DEFAULT_REPORT_PATH,
        help="Report output path.",
    )
    parser.add_argument("--no-report", action="store_true", help="Run without writing a report file.")
    parser.add_argument("--skip-ffprobe", action="store_true", help="Skip MP3 stream format checks.")
    return parser.parse_args(argv)


def collect_markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS]
        for filename in filenames:
            if filename.endswith(".md"):
                files.append(Path(dirpath) / filename)
    return sorted(files)


def normalize_embed_target(target: str) -> str:
    return Path(target.replace("\\", "/").split("#", 1)[0]).name


def collect_embeds(root: Path) -> list[dict[str, Any]]:
    embeds: list[dict[str, Any]] = []
    for md_path in collect_markdown_files(root):
        try:
            lines = md_path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeDecodeError) as exc:
            embeds.append(
                {
                    "file": str(md_path.relative_to(root)),
                    "line": 0,
                    "target": "",
                    "filename": "",
                    "error": f"read failed: {exc}",
                }
            )
            continue
        for line_number, line in enumerate(lines, 1):
            for match in EMBED_RE.finditer(line):
                target = match.group(1)
                embeds.append(
                    {
                        "file": str(md_path.relative_to(root)),
                        "line": line_number,
                        "target": target,
                        "filename": normalize_embed_target(target),
                        "error": "",
                    }
                )
    return embeds


def load_manifest(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, list):
        raise ValueError(f"{path} must contain a JSON list")
    return data


def ffprobe_stream(path: Path, ffprobe: str) -> tuple[dict[str, Any] | None, str]:
    command = [
        ffprobe,
        "-v",
        "error",
        "-select_streams",
        "a:0",
        "-show_entries",
        "stream=codec_name,sample_rate,channels,bit_rate",
        "-of",
        "json",
        str(path),
    ]
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result.returncode != 0:
        return None, result.stderr.strip() or f"ffprobe exited {result.returncode}"
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        return None, f"invalid ffprobe JSON: {exc}"
    streams = payload.get("streams")
    if not streams:
        return None, "no audio stream"
    stream = streams[0]
    if not isinstance(stream, dict):
        return None, "malformed audio stream"
    return stream, ""


def stream_issue(stream: dict[str, Any]) -> str:
    problems: list[str] = []
    if str(stream.get("codec_name")) != EXPECTED_CODEC:
        problems.append(f"codec={stream.get('codec_name')!r}")
    if str(stream.get("sample_rate")) != EXPECTED_SAMPLE_RATE:
        problems.append(f"sample_rate={stream.get('sample_rate')!r}")
    if int(stream.get("channels") or 0) != EXPECTED_CHANNELS:
        problems.append(f"channels={stream.get('channels')!r}")
    if str(stream.get("bit_rate")) != EXPECTED_BIT_RATE:
        problems.append(f"bit_rate={stream.get('bit_rate')!r}")
    return ", ".join(problems)


def build_report(lines: list[str], title: str, items: list[str]) -> None:
    lines.extend(["", title])
    if items:
        lines.extend(f"  {item}" for item in items)
    else:
        lines.append("  (none)")


def display_path(path: Path, base: Path) -> str:
    try:
        return str(path.relative_to(base)).replace("\\", "/")
    except ValueError:
        return str(path)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = args.root.resolve()
    audio_dir = args.audio_dir.resolve() if args.audio_dir else root / "_audio"
    manifest_path = args.manifest.resolve() if args.manifest else audio_dir / "pronunciation_manifest.json"
    report_path = args.report.resolve()
    vault_root = root.parent

    if not root.exists():
        print(f"ERROR: Japanese root does not exist: {root}", file=sys.stderr)
        return 1
    if not audio_dir.exists():
        print(f"ERROR: audio directory does not exist: {audio_dir}", file=sys.stderr)
        return 1
    if not manifest_path.exists():
        print(f"ERROR: manifest does not exist: {manifest_path}", file=sys.stderr)
        return 1

    embeds = collect_embeds(root)
    embed_read_errors = [f"{item['file']}: {item['error']}" for item in embeds if item["error"]]
    embedded_names = [item["filename"] for item in embeds if item["filename"]]
    embedded_name_set = set(embedded_names)

    mp3_paths = sorted(audio_dir.glob("*.mp3"))
    mp3_names = {path.name for path in mp3_paths}
    manifest = load_manifest(manifest_path)
    manifest_names = {str(row.get("filename")) for row in manifest if row.get("filename")}

    missing_embeds = [
        f"{item['file']}:{item['line']} -> {item['target']}"
        for item in embeds
        if item["filename"] and item["filename"] not in mp3_names
    ]
    manifest_missing_mp3 = sorted(name for name in manifest_names if name not in mp3_names)
    mp3_not_in_manifest = sorted(name for name in mp3_names if name not in manifest_names)
    embedded_not_in_manifest = sorted(name for name in embedded_name_set if name not in manifest_names)
    url_sensitive_mp3_names = sorted(name for name in mp3_names if URL_SENSITIVE_FILENAME_RE.search(name))
    url_sensitive_manifest_names = sorted(
        name for name in manifest_names if URL_SENSITIVE_FILENAME_RE.search(name)
    )
    url_sensitive_embeds = [
        f"{item['file']}:{item['line']} -> {item['target']}"
        for item in embeds
        if item["filename"] and URL_SENSITIVE_FILENAME_RE.search(item["filename"])
    ]

    duplicate_embeds = [
        f"{filename} embedded {count} times"
        for filename, count in sorted(Counter(embedded_names).items())
        if count > 1
    ]

    ffprobe_failures: list[str] = []
    format_issues: list[str] = []
    ffprobe_checked = 0
    if not args.skip_ffprobe:
        ffprobe = shutil.which("ffprobe")
        if not ffprobe:
            ffprobe_failures.append("ffprobe executable not found")
        else:
            for path in mp3_paths:
                stream, error = ffprobe_stream(path, ffprobe)
                if error:
                    ffprobe_failures.append(f"{path.name}: {error}")
                    continue
                ffprobe_checked += 1
                issue = stream_issue(stream or {})
                if issue:
                    format_issues.append(f"{path.name}: {issue}")

    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_lines = [
        "JAPANESE AUDIO INTEGRITY AUDIT",
        "=" * 80,
        f"Generated: {generated_at}",
        f"Japanese root: {display_path(root, vault_root)}",
        f"Audio directory: {display_path(audio_dir, vault_root)}",
        f"Manifest: {display_path(manifest_path, vault_root)}",
        "",
        "SUMMARY",
        f"  Markdown MP3 embeds       : {len(embedded_names)}",
        f"  Unique embedded MP3 files : {len(embedded_name_set)}",
        f"  MP3 files in _audio       : {len(mp3_names)}",
        f"  Pronunciation entries     : {len(manifest_names)}",
        f"  Missing embedded MP3 files: {len(missing_embeds)}",
        f"  Manifest rows missing MP3 : {len(manifest_missing_mp3)}",
        f"  MP3 files not in manifest : {len(mp3_not_in_manifest)}",
        f"  Embedded files not manifest: {len(embedded_not_in_manifest)}",
        f"  Markdown read errors      : {len(embed_read_errors)}",
        f"  URL-sensitive MP3 names   : {len(url_sensitive_mp3_names)}",
        f"  URL-sensitive manifest rows: {len(url_sensitive_manifest_names)}",
        f"  URL-sensitive embeds      : {len(url_sensitive_embeds)}",
        f"  ffprobe checked MP3 files : {ffprobe_checked}",
        f"  ffprobe failures          : {len(ffprobe_failures)}",
        f"  Format issues             : {len(format_issues)}",
        "",
        "EXPECTED MP3 FORMAT",
        f"  codec_name={EXPECTED_CODEC}",
        f"  sample_rate={EXPECTED_SAMPLE_RATE}",
        f"  channels={EXPECTED_CHANNELS}",
        f"  bit_rate={EXPECTED_BIT_RATE}",
    ]

    build_report(report_lines, "MISSING EMBEDDED MP3 FILES", missing_embeds)
    build_report(report_lines, "MANIFEST ROWS MISSING MP3", manifest_missing_mp3)
    build_report(report_lines, "MP3 FILES NOT IN MANIFEST", mp3_not_in_manifest)
    build_report(report_lines, "EMBEDDED FILES NOT IN MANIFEST", embedded_not_in_manifest)
    build_report(report_lines, "MARKDOWN READ ERRORS", embed_read_errors)
    build_report(report_lines, "URL-SENSITIVE MP3 NAMES", url_sensitive_mp3_names)
    build_report(report_lines, "URL-SENSITIVE MANIFEST ROWS", url_sensitive_manifest_names)
    build_report(report_lines, "URL-SENSITIVE EMBEDS", url_sensitive_embeds)
    build_report(report_lines, "FFPROBE FAILURES", ffprobe_failures)
    build_report(report_lines, "FORMAT ISSUES", format_issues)
    build_report(report_lines, "DUPLICATE EMBED COUNTS", duplicate_embeds[:100])

    if not args.no_report:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print("Japanese Audio Integrity Audit")
    print(f"  Markdown MP3 embeds       : {len(embedded_names)}")
    print(f"  Unique embedded MP3 files : {len(embedded_name_set)}")
    print(f"  MP3 files in _audio       : {len(mp3_names)}")
    print(f"  Pronunciation entries     : {len(manifest_names)}")
    print(f"  Missing embedded MP3 files: {len(missing_embeds)}")
    print(f"  Manifest rows missing MP3 : {len(manifest_missing_mp3)}")
    print(f"  MP3 files not in manifest : {len(mp3_not_in_manifest)}")
    print(f"  Embedded files not manifest: {len(embedded_not_in_manifest)}")
    print(f"  URL-sensitive MP3 names   : {len(url_sensitive_mp3_names)}")
    print(f"  URL-sensitive manifest rows: {len(url_sensitive_manifest_names)}")
    print(f"  URL-sensitive embeds      : {len(url_sensitive_embeds)}")
    print(f"  ffprobe checked MP3 files : {ffprobe_checked}")
    print(f"  ffprobe failures          : {len(ffprobe_failures)}")
    print(f"  Format issues             : {len(format_issues)}")
    print("  Report                    : " + ("not written (--no-report)" if args.no_report else str(report_path)))

    failures = (
        missing_embeds
        or manifest_missing_mp3
        or mp3_not_in_manifest
        or embedded_not_in_manifest
        or embed_read_errors
        or url_sensitive_mp3_names
        or url_sensitive_manifest_names
        or url_sensitive_embeds
        or ffprobe_failures
        or format_issues
    )
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
