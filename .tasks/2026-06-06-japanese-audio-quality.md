# Japanese Audio Quality Pass

## Goal

Keep Obsidian sync available while improving the Japanese learning path with accurate local audio.

## Current Pass

- Preserve the active vault dirty tree by working in `continue-japanese-audio-learning`.
- Fix remaining corrupted Japanese source text that feeds pronunciation clips.
- Regenerate only affected audio after the manifest is corrected.
- Run the standard vault and audio verification before merging back.

## Result

- Repaired `adj-007-atsui.mp3` from `暮い` to `暑い`.
- Repaired the N5 ぐ -> いで example from `泣ぐ -> 泣いで` to `泳ぐ -> 泳いで`.
- Renamed `verb-018-kyuu-gu.mp3` to `verb-018-oyogu.mp3`.
- Regenerated `adj-007-atsui.mp3`, `verb-018-oyogu.mp3`, and `verb-019-oyoide.mp3`.

## Verification Evidence

- `python Japanese\_audio\build_pronunciation_manifest.py --check`
- Manifest inventory: 1,810 manifest entries, 1,810 MP3 files, 0 missing, 0 extra, 0 zero-size.
- Bad-text search: 0 live Markdown/JSON matches for `暮い`, `泣ぐ`, `泣いで`, or `verb-018-kyuu-gu`.
- `ffprobe` durations for the three regenerated MP3 files were present and non-empty.
- `python _ops\personal_kb.py audit`
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`
