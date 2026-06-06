---
tags: [japanese, speaking, pronunciation, audio, qa, log]
up: "[[Pronunciation and Audio Accuracy]]"
confidence: policy
tier-coverage: [practice]
---

# Pronunciation Correction Log

> Use this page when a local audio clip sounds wrong, has an ambiguous reading, or disagrees with native/official audio. The goal is to keep suspect clips out of daily practice until they are checked, fixed, or replaced.

## How To Use This Log

Add an entry before changing learner-facing practice pages. Keep the entry short and evidence-based.

1. Record the filename, displayed text, and what sounded wrong.
2. Mark the status as `suspect`, `checking`, `fixed`, `replaced`, or `removed`.
3. Check the item against [[Pronunciation and Audio Accuracy]].
4. If the source text or reading hint is wrong, fix the manifest/source text before regenerating audio.
5. Run the manifest and reading-hint checks before returning the clip to a daily path.

Do not use this page as a pronunciation diary. Normal learner corrections belong in [[Authentic Audio Evidence Log]], [[Phase 1 Weekly Review]], [[Phase 2 Weekly Review]], [[Phase 3 Weekly Review]], [[Phase 4 Weekly Review]], [[Phase 5 Weekly Review]], or [[Advanced Output and Register Feedback Log]]. This page is for clip-quality issues.

## Open Suspect Clips

No open suspect clips are currently recorded here.

| Status | Filename | Displayed text | Issue | Next check |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Resolved Corrections

These entries are resolved corrections already recorded in the vault maintenance log and audio audit reports.

| Date | Filename | Issue | Resolution | Evidence |
| --- | --- | --- | --- | --- |
| 2026-06-06 | `adj-007-atsui.mp3` | OCR text made the hot adjective unsafe for audio practice | Repaired `暮い` to `暑い`, regenerated the clip, and kept the manifest override stable | `log.md`; `_ops/reports/japanese-audio-pronunciation-audit.txt` |
| 2026-06-06 | `verb-018-oyogu.mp3`, `verb-019-oyoide.mp3` | Verb example was harvested as `泣ぐ -> 泣いで`, which is not the intended ぐ -> いで example | Repaired the example to `泳ぐ -> 泳いで`, renamed the misleading file, and regenerated affected audio | `log.md`; `_ops/reports/japanese-audio-pronunciation-audit.txt` |
| 2026-06-06 | `gap-058-(ikkagetsu).mp3` | Duration counter reading needed to be locked explicitly | Forced `一か月` to synthesize from `いっかげつ` | `log.md`; `_ops/reports/japanese-audio-reading-hints-audit.txt` |
| 2026-06-06 | `gap-184-(akeru)-open.mp3` | Transitive `開ける` reading needed to be locked explicitly | Forced the manifest TTS text to `あける` | `log.md`; `_ops/reports/japanese-audio-reading-hints-audit.txt` |

## Verification Commands

Use these commands after a correction:

```powershell
python Japanese\_audio\build_pronunciation_manifest.py --check
python Japanese\_audio\audit_reading_hints.py --fail-on-findings
python _ops\personal_kb.py audit
python _ops\personal_kb.py index
python _ops\personal_kb.py audit
git diff --check
```

## Return-To-Practice Rule

A corrected local clip can return to [[Phase 1 Local Audio Practice]], a Phase 2 content page, or another daily path only when:

- The manifest check passes.
- The reading-hint audit has zero findings.
- The clip file exists and is non-empty.
- The learner-facing page points to an authentic model when rhythm, pitch, counters, names, keigo, or full-sentence memorization matter.
- The correction is recorded here if it was a clip-quality issue.

## References

- [[Pronunciation and Audio Accuracy]]
- [[Audio Index]]
- [[Authentic Audio Evidence Log]]
- [[Phase 1 Audio Coverage Map]]
- [[Phase 2 Audio Coverage Map]]
- [[Phase 5 Audio Coverage Map]]
- [[Phase 1 Weekly Review]]
- [[Phase 2 Weekly Review]]
- [[Phase 3 Weekly Review]]
- [[Phase 4 Weekly Review]]
- [[Phase 5 Weekly Review]]
- [[Advanced Output and Register Feedback Log]]
- `log.md`
- `_ops/reports/japanese-audio-pronunciation-audit.txt`
- `_ops/reports/japanese-audio-reading-hints-audit.txt`
