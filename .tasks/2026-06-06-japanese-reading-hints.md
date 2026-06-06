# Japanese Audio Reading-Hint Audit

## Goal

Improve local Japanese audio authenticity by checking pronunciation-manifest entries against explicit romaji hints embedded in source text.

## Scope

- Work in the isolated `japanese-audio-reading-audit` branch.
- Add a repeatable audit for source entries such as `一か月 (ikkagetsu)` where kanji may be read incorrectly by generic TTS.
- Fix only high-confidence mismatches and regenerate only affected clips.
- Preserve the active Obsidian vault dirty tree and keep Obsidian running for sync.

## Result

- Added `Japanese/_audio/audit_reading_hints.py`.
- Added `_ops/reports/japanese-audio-reading-hints-audit.txt`.
- Forced `gap-058-(ikkagetsu).mp3` to synthesize from `いっかげつ`.
- Forced `gap-184-(akeru)-open.mp3` to synthesize from `あける`; the regenerated output matched the existing clip bytes, but the manifest now locks the intended reading.

## Verification Evidence

- `python Japanese\_audio\build_pronunciation_manifest.py --check`
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`
- Manifest inventory: 1,810 manifest entries, 1,810 MP3 files, 0 missing, 0 extra, 0 zero-size.
- `ffprobe` durations for `gap-058-(ikkagetsu).mp3` and `gap-184-(akeru)-open.mp3` were present and non-empty.
- `python _ops\personal_kb.py audit`
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`
