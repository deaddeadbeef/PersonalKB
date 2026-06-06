#!/usr/bin/env python3
"""
Audit script for Japanese learning wiki audio-text mismatches.
Scans all .md files for ![[*.mp3]] embeds, extracts context,
and flags suspicious cases where audio clips may not match surrounding text.
"""

import os
import re
import sys
import argparse
from collections import defaultdict
from pathlib import Path
from datetime import datetime

# ── Configuration ──────────────────────────────────────────────────────────
SCRIPT_PATH = Path(__file__).resolve()
DEFAULT_AUDIO_DIR = SCRIPT_PATH.parent
DEFAULT_WIKI_ROOT = DEFAULT_AUDIO_DIR.parent
DEFAULT_REPORT_PATH = DEFAULT_AUDIO_DIR / "audit-mismatch-report.txt"
WIKI_ROOT = DEFAULT_WIKI_ROOT
AUDIO_DIR = DEFAULT_AUDIO_DIR
REPORT_PATH = DEFAULT_REPORT_PATH
CONTEXT_LINES = 3          # lines before/after for context extraction
MATCH_WINDOW = 5           # lines before/after for romaji match search
EXCLUDED_DIRS = {"_audio", "_raw", "_chunks", "_queries", "_templates"}

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ── Romaji-to-kana lookup (Phase 4) ──────────────────────────────────────
ROMAJI_TO_HIRAGANA = {
    'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お',
    'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ',
    'sa': 'さ', 'shi': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ',
    'ta': 'た', 'chi': 'ち', 'tsu': 'つ', 'te': 'て', 'to': 'と',
    'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
    'ha': 'は', 'hi': 'ひ', 'fu': 'ふ', 'he': 'へ', 'ho': 'ほ',
    'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も',
    'ya': 'や', 'yu': 'ゆ', 'yo': 'よ',
    'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ',
    'wa': 'わ', 'wo': 'を', 'n': 'ん',
    'ga': 'が', 'gi': 'ぎ', 'gu': 'ぐ', 'ge': 'げ', 'go': 'ご',
    'za': 'ざ', 'ji': 'じ', 'zu': 'ず', 'ze': 'ぜ', 'zo': 'ぞ',
    'da': 'だ', 'di': 'ぢ', 'du': 'づ', 'de': 'で', 'do': 'ど',
    'ba': 'ば', 'bi': 'び', 'bu': 'ぶ', 'be': 'べ', 'bo': 'ぼ',
    'pa': 'ぱ', 'pi': 'ぴ', 'pu': 'ぷ', 'pe': 'ぺ', 'po': 'ぽ',
    'kya': 'きゃ', 'kyu': 'きゅ', 'kyo': 'きょ',
    'sha': 'しゃ', 'shu': 'しゅ', 'sho': 'しょ',
    'cha': 'ちゃ', 'chu': 'ちゅ', 'cho': 'ちょ',
    'nya': 'にゃ', 'nyu': 'にゅ', 'nyo': 'にょ',
    'hya': 'ひゃ', 'hyu': 'ひゅ', 'hyo': 'ひょ',
    'mya': 'みゃ', 'myu': 'みゅ', 'myo': 'みょ',
    'rya': 'りゃ', 'ryu': 'りゅ', 'ryo': 'りょ',
    'gya': 'ぎゃ', 'gyu': 'ぎゅ', 'gyo': 'ぎょ',
    'ja': 'じゃ', 'ju': 'じゅ', 'jo': 'じょ',
    'bya': 'びゃ', 'byu': 'びゅ', 'byo': 'びょ',
    'pya': 'ぴゃ', 'pyu': 'ぴゅ', 'pyo': 'ぴょ',
}

# Build katakana map (hiragana codepoints + 0x60)
ROMAJI_TO_KATAKANA = {}
for _rom, _hira in ROMAJI_TO_HIRAGANA.items():
    _kata = ''.join(chr(ord(c) + 0x60) if 0x3041 <= ord(c) <= 0x3096 else c for c in _hira)
    ROMAJI_TO_KATAKANA[_rom] = _kata

# ── Audio prefix → expected page-folder mapping ──────────────────────────
# Keys: audio prefix.  Values: list of wiki folder names where this prefix
# is expected to appear.  If the embed's host page lives in a folder NOT in
# this list, it is flagged as CATEGORY_MISMATCH.
PREFIX_EXPECTED_FOLDERS = {
    'hira':       ['Writing Systems'],
    'kata':       ['Writing Systems'],
    'kanjin3':    ['Writing Systems'],
    'kanjin4':    ['Writing Systems'],
    'kanjin5':    ['Writing Systems'],
    'kanjistrategy': ['Writing Systems'],
    'kanjiwork':  ['Writing Systems'],
    'radical':    ['Writing Systems'],
    'greet':      ['Speaking', 'Culture'],
    'greet2':     ['Speaking', 'Culture'],
    'greetings':  ['Speaking', 'Culture'],
    'adj':        ['Grammar'],
    'verb':       ['Grammar'],
    'particle':   ['Grammar'],
    'sentpat':    ['Grammar'],
    'pitch':      ['Speaking'],
    'pitch2':     ['Speaking'],
    'pronun':     ['Speaking'],
    'pronun2':    ['Speaking'],
}

EMBED_RE = re.compile(r'!\[\[([^\]]+\.mp3)\]\]')


# ── Helpers ───────────────────────────────────────────────────────────────

def romaji_to_kana(romaji_str: str) -> list[str]:
    """Convert romaji to [hiragana, katakana] using greedy longest-match."""
    results = []
    for mapping in [ROMAJI_TO_HIRAGANA, ROMAJI_TO_KATAKANA]:
        kana = []
        i = 0
        s = romaji_str.lower()
        while i < len(s):
            if i + 1 < len(s) and s[i] == s[i + 1] and s[i] not in 'aiueon':
                kana.append('っ' if mapping is ROMAJI_TO_HIRAGANA else 'ッ')
                i += 1
                continue
            matched = False
            for length in [3, 2, 1]:
                chunk = s[i:i + length]
                if chunk in mapping:
                    kana.append(mapping[chunk])
                    i += length
                    matched = True
                    break
            if not matched:
                kana.append(s[i])
                i += 1
        results.append(''.join(kana))
    return results


def parse_filename(clip_name: str) -> dict:
    """Parse audio filename → {prefix, num, hint, hint_parts}."""
    stem = clip_name.rsplit('.', 1)[0]
    parts = stem.split('-')

    prefix_parts, num, hint_parts = [], '', []
    found_num = False
    for p in parts:
        if not found_num and p.isdigit():
            num = p
            found_num = True
            continue
        if found_num:
            hint_parts.append(p)
        else:
            prefix_parts.append(p)

    if not found_num:
        prefix_parts = [parts[0]]
        hint_parts = parts[1:]

    return {
        'prefix': '-'.join(prefix_parts) if prefix_parts else parts[0],
        'num': num,
        'hint': '-'.join(hint_parts),
        'hint_parts': hint_parts,
    }


def clean_hint(hint: str) -> str:
    """Remove parens/symbols, lowercase."""
    return re.sub(r'[^a-zA-Z]', '', hint).lower()


def extract_romaji_tokens(hint: str) -> list[str]:
    """Split hint on hyphens; also include the fully-joined form."""
    if not hint:
        return []
    parts = [p for p in hint.split('-') if p]
    tokens = list(parts)
    if len(parts) > 1:
        tokens.append(''.join(parts))
    return tokens


def get_page_folder(file_path: str) -> str:
    """Return the top-level wiki subfolder for a file, or 'root'."""
    try:
        rel = Path(file_path).relative_to(WIKI_ROOT)
    except ValueError:
        return 'root'
    parts = rel.parts
    return parts[0] if len(parts) >= 2 else 'root'


def context_is_empty(lines: list[str]) -> bool:
    return all(not line.strip() for line in lines)


def search_context_for_match(context_lines: list[str],
                              romaji_tokens: list[str],
                              kana_versions: list[str]) -> bool:
    """Return True if any romaji token or kana appears in the context.
    
    IMPORTANT: Strip ![[...]] embed references before matching so that
    the filename itself doesn't cause a false positive.
    """
    stripped = [re.sub(r'!\[\[[^\]]*\]\]', '', line) for line in context_lines]
    context_lower = ' '.join(stripped).lower()
    context_raw = ' '.join(stripped)

    for token in romaji_tokens:
        tc = clean_hint(token)
        if not tc:
            continue
        if len(tc) <= 1:
            if re.search(r'(?:^|[\s|(/])' + re.escape(tc) + r'(?:$|[\s|)/,.])',
                         context_lower):
                return True
        else:
            if tc in context_lower:
                return True

    for kana in kana_versions:
        if kana and kana in context_raw:
            return True

    return False


def collect_md_files(root: Path) -> list[Path]:
    md_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS]
        for fn in filenames:
            if fn.endswith('.md'):
                md_files.append(Path(dirpath) / fn)
    return sorted(md_files)


# ── Main ──────────────────────────────────────────────────────────────────

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_WIKI_ROOT,
        help="Japanese wiki root; defaults to the parent of this script's _audio directory.",
    )
    parser.add_argument(
        "--report",
        type=Path,
        help="Report output path; defaults to <root>/_audio/audit-mismatch-report.txt.",
    )
    parser.add_argument(
        "--no-report",
        action="store_true",
        help="Run the audit without writing the report file.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    global WIKI_ROOT, AUDIO_DIR, REPORT_PATH

    args = parse_args(argv)
    WIKI_ROOT = args.root.resolve()
    AUDIO_DIR = WIKI_ROOT / "_audio"
    REPORT_PATH = args.report.resolve() if args.report else AUDIO_DIR / "audit-mismatch-report.txt"

    if not WIKI_ROOT.exists():
        print(f"ERROR: wiki root does not exist: {WIKI_ROOT}", file=sys.stderr)
        return 1
    if not AUDIO_DIR.exists():
        print(f"ERROR: audio directory does not exist: {AUDIO_DIR}", file=sys.stderr)
        return 1

    print("Audio-Text Mismatch Audit")
    print(f"Wiki root: {WIKI_ROOT}")
    print("Scanning...\n")

    md_files = collect_md_files(WIKI_ROOT)
    print(f"  Markdown files: {len(md_files)}")

    # ── Phase 1: extract all embeds ───────────────────────────────────────
    embeds = []

    for md_path in md_files:
        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                lines = [l.rstrip('\n') for l in f.readlines()]
        except (UnicodeDecodeError, OSError) as exc:
            print(f"  WARN: cannot read {md_path}: {exc}", file=sys.stderr)
            continue

        for line_idx, line in enumerate(lines):
            for m in EMBED_RE.finditer(line):
                clip = m.group(1)
                s = max(0, line_idx - CONTEXT_LINES)
                e = min(len(lines), line_idx + CONTEXT_LINES + 1)
                sw = max(0, line_idx - MATCH_WINDOW)
                ew = min(len(lines), line_idx + MATCH_WINDOW + 1)
                embeds.append({
                    'file_path': str(md_path),
                    'rel_path': str(md_path.relative_to(WIKI_ROOT)),
                    'line_number': line_idx + 1,
                    'clip_name': clip,
                    'embed_line': line,
                    'context_before': lines[s:line_idx],
                    'context_after': lines[line_idx + 1:e],
                    'wide_context': lines[sw:ew],
                })

    print(f"  Audio embeds:   {len(embeds)}\n")

    # ── Phase 2 + 3: analyse each embed ──────────────────────────────────
    flags = {
        'NO_CONTEXT': [],
        'CATEGORY_MISMATCH': [],
        'POSSIBLE_WRONG_CLIP': [],
        'DUPLICATE_ON_PAGE': [],
    }

    # Duplicate detection per page
    page_clips = defaultdict(list)
    for em in embeds:
        page_clips[em['file_path']].append(em['clip_name'])

    dup_flagged = set()
    for fpath, clips in page_clips.items():
        counts = defaultdict(int)
        for c in clips:
            counts[c] += 1
        for c, cnt in counts.items():
            if cnt > 1:
                rel = str(Path(fpath).relative_to(WIKI_ROOT))
                key = (rel, c)
                if key not in dup_flagged:
                    dup_flagged.add(key)
                    flags['DUPLICATE_ON_PAGE'].append({
                        'file': rel, 'clip': c, 'count': cnt,
                    })

    for em in embeds:
        clip = em['clip_name']
        parsed = parse_filename(clip)
        prefix = parsed['prefix']
        hint = parsed['hint']

        # ── NO_CONTEXT ──
        combined = em['context_before'] + em['context_after']
        meaningful = [
            l for l in combined
            if l.strip() and not re.match(r'^[\s|:-]+$', l.strip())
        ]
        if not meaningful:
            flags['NO_CONTEXT'].append({
                'file': em['rel_path'], 'line': em['line_number'],
                'clip': clip, 'context': combined,
            })

        # ── CATEGORY_MISMATCH ──
        folder = get_page_folder(em['file_path'])
        if prefix in PREFIX_EXPECTED_FOLDERS and folder != 'root':
            if folder not in PREFIX_EXPECTED_FOLDERS[prefix]:
                flags['CATEGORY_MISMATCH'].append({
                    'file': em['rel_path'], 'line': em['line_number'],
                    'clip': clip, 'prefix': prefix,
                    'folder': folder,
                    'expected_folders': PREFIX_EXPECTED_FOLDERS[prefix],
                })

        # ── POSSIBLE_WRONG_CLIP ──
        # Skip gap/nontbl with generic or non-romaji hints
        is_generic = prefix in ('gap', 'nontbl') and (
            not hint
            or re.match(r'^[^a-zA-Z]*$', hint)
            or any(kw in hint.lower() for kw in [
                'drop', 'add', 'plain', 'phrase', 'combine',
            ])
        )
        if hint and not is_generic:
            romaji_tokens = extract_romaji_tokens(hint)
            all_kana = []
            for tok in romaji_tokens:
                tc = clean_hint(tok)
                if tc and tc.isalpha():
                    all_kana.extend(romaji_to_kana(tc))
            full_clean = clean_hint(hint.replace('-', ''))
            if full_clean and full_clean.isalpha():
                all_kana.extend(romaji_to_kana(full_clean))

            found = search_context_for_match(
                em['wide_context'], romaji_tokens, all_kana)

            if not found:
                ctx_display = []
                for wl in em['wide_context']:
                    marker = '>>>' if wl == em['embed_line'] else '   '
                    ctx_display.append(f"  {marker} {wl}")

                flags['POSSIBLE_WRONG_CLIP'].append({
                    'file': em['rel_path'], 'line': em['line_number'],
                    'clip': clip,
                    'expected_romaji': hint,
                    'expected_kana': all_kana[:2],
                    'context': ctx_display,
                })

    # ── Write report ──────────────────────────────────────────────────────
    total_flagged = sum(len(v) for v in flags.values())
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sep = '=' * 78

    rpt = []
    rpt.append(sep)
    rpt.append("JAPANESE WIKI AUDIO-TEXT MISMATCH AUDIT REPORT")
    rpt.append(f"Generated: {ts}")
    rpt.append(f"Wiki root: {WIKI_ROOT}")
    rpt.append(sep)
    rpt.append("")
    rpt.append("-" * 78)
    rpt.append("SUMMARY")
    rpt.append("-" * 78)
    rpt.append(f"  Markdown files scanned:    {len(md_files)}")
    rpt.append(f"  Total audio embeds found:  {len(embeds)}")
    rpt.append(f"  Total issues flagged:      {total_flagged}")
    rpt.append("")
    rpt.append("  By category:")
    for cat in ['NO_CONTEXT', 'CATEGORY_MISMATCH',
                'POSSIBLE_WRONG_CLIP', 'DUPLICATE_ON_PAGE']:
        rpt.append(f"    {cat:30s} {len(flags[cat]):>4d}")
    rpt.append("")

    # NO_CONTEXT
    rpt.append("-" * 78)
    rpt.append(f"NO_CONTEXT ({len(flags['NO_CONTEXT'])} cases)")
    rpt.append("Embeds where surrounding lines are empty/whitespace only")
    rpt.append("-" * 78)
    for item in flags['NO_CONTEXT']:
        rpt.append(f"  [{item['file']}:{item['line']}] {item['clip']}")
    if not flags['NO_CONTEXT']:
        rpt.append("  (none)")
    rpt.append("")

    # CATEGORY_MISMATCH
    rpt.append("-" * 78)
    rpt.append(f"CATEGORY_MISMATCH ({len(flags['CATEGORY_MISMATCH'])} cases)")
    rpt.append("Audio prefix appears on a page outside its expected folder")
    rpt.append("-" * 78)
    for item in flags['CATEGORY_MISMATCH']:
        rpt.append(f"  [{item['file']}:{item['line']}] {item['clip']}")
        rpt.append(f"    prefix '{item['prefix']}' expected in "
                    f"{item['expected_folders']}, found in '{item['folder']}'")
    if not flags['CATEGORY_MISMATCH']:
        rpt.append("  (none)")
    rpt.append("")

    # POSSIBLE_WRONG_CLIP
    rpt.append("-" * 78)
    rpt.append(f"POSSIBLE_WRONG_CLIP ({len(flags['POSSIBLE_WRONG_CLIP'])} cases)")
    rpt.append("Romaji hint from filename doesn't match text within 5 lines")
    rpt.append("-" * 78)
    for item in flags['POSSIBLE_WRONG_CLIP']:
        rpt.append(f"  [{item['file']}:{item['line']}] {item['clip']}")
        rpt.append(f"    Expected romaji: {item['expected_romaji']}")
        if item['expected_kana']:
            rpt.append(f"    Expected kana:   {' / '.join(item['expected_kana'])}")
        rpt.append("    Context:")
        for cl in item['context']:
            rpt.append(f"    {cl}")
        rpt.append("")
    if not flags['POSSIBLE_WRONG_CLIP']:
        rpt.append("  (none)")
    rpt.append("")

    # DUPLICATE_ON_PAGE
    rpt.append("-" * 78)
    rpt.append(f"DUPLICATE_ON_PAGE ({len(flags['DUPLICATE_ON_PAGE'])} cases)")
    rpt.append("Same clip embedded multiple times on one page")
    rpt.append("-" * 78)
    for item in flags['DUPLICATE_ON_PAGE']:
        rpt.append(f"  [{item['file']}] {item['clip']} (x{item['count']})")
    if not flags['DUPLICATE_ON_PAGE']:
        rpt.append("  (none)")
    rpt.append("")
    rpt.append(sep)
    rpt.append("END OF REPORT")
    rpt.append(sep)

    if not args.no_report:
        REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(REPORT_PATH, 'w', encoding='utf-8') as f:
            f.write('\n'.join(rpt))

    # ── Stdout summary ────────────────────────────────────────────────────
    print("-" * 60)
    print("AUDIT COMPLETE")
    print("-" * 60)
    print(f"  Files scanned:         {len(md_files)}")
    print(f"  Total embeds:          {len(embeds)}")
    print(f"  Total flagged:         {total_flagged}")
    print(f"    NO_CONTEXT:          {len(flags['NO_CONTEXT'])}")
    print(f"    CATEGORY_MISMATCH:   {len(flags['CATEGORY_MISMATCH'])}")
    print(f"    POSSIBLE_WRONG_CLIP: {len(flags['POSSIBLE_WRONG_CLIP'])}")
    print(f"    DUPLICATE_ON_PAGE:   {len(flags['DUPLICATE_ON_PAGE'])}")
    print("-" * 60)
    if args.no_report:
        print("Report: not written (--no-report)")
    else:
        print(f"Report: {REPORT_PATH}")

    if flags['POSSIBLE_WRONG_CLIP']:
        print(f"\nTop POSSIBLE_WRONG_CLIP (first 15):")
        for item in flags['POSSIBLE_WRONG_CLIP'][:15]:
            print(f"  {item['clip']}  @ {item['file']}:{item['line']}")
            print(f"    expected: {item['expected_romaji']}")

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
