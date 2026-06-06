---
tags: [japanese, audio, qa, pronunciation, obsidian]
up: "[[Japanese Study Index]]"
confidence: verified
tier-coverage: [core, practice]
---

# Japanese Audio QA Status

This page records what the local audio system has proved and what still needs a native, official, tutor, or accent-reference check.

## Current Evidence

As of 2026-06-07, local playback support is verified:

| Check | Current result |
| --- | --- |
| Markdown MP3 embeds | 2210 |
| Unique embedded MP3 files | 1759 |
| Local MP3 files in `Japanese/_audio/` | 1810 |
| Pronunciation-manifest entries | 1810 |
| Missing embedded MP3 files | 0 |
| Manifest rows missing MP3 files | 0 |
| MP3 files not in manifest | 0 |
| Embedded files not in manifest | 0 |
| MP3 files checked by `ffprobe` | 1810 |
| MP3 format issues | 0 |
| Reading-hint audit findings | 0 |
| Source-repair pronunciation overrides | 0 |
| Expected reading overrides | 26 |
| Source-aware STT dry-run sample | 61 clips selected from `pronunciation_manifest.json`; 0 validation problems |
| Live STT transcription check | Not run in current environment; `AZURE_SPEECH_KEY` is required |

The 26 expected reading overrides are deliberate: topic/object/direction particles, counter suffixes, `開ける`, and `聲の形` need readings that differ from their written form.

The source-aware STT report replaces the older filename-derived check. It compares speech recognition output against `pronunciation_manifest.json` `text` and `display_text`, not against filenames such as `gap-084-phrase.mp3`.

## What This Proves

- Local audio embeds resolve to existing MP3 files.
- The local MP3 inventory matches `pronunciation_manifest.json`.
- The MP3 files use the Obsidian-compatible format: MP3, 48 kHz, mono, 96 kbps.
- Current source-repair debt is cleared from the pronunciation manifest.
- Reading-hint checks currently find no unresolved romaji-hint conflicts.
- The STT spot-check tooling now uses source text from `pronunciation_manifest.json` instead of filename-derived hints.

## What This Does Not Prove

- TTS is not the final authority for pitch accent.
- TTS is not the final authority for long-sentence rhythm.
- TTS is not the final authority for keigo, register, humor, or natural delivery.
- A dry-run STT sample plan does not prove clip pronunciation; it only proves the STT audit will use the correct expected source text.
- Even live STT is only a triage signal. Native/course/tutor/reference audio remains the pronunciation authority.
- Native-source Phase 5 work still needs a named source segment, assignment block, output, and tutor/native feedback.

Use [[Pronunciation and Audio Accuracy]] to decide when a local clip is safe for drills. Use [[Authentic Audio Source Setup]], [[Phase 5 Audio Assignment Ladder]], and the phase authentic audio spines when pronunciation, rhythm, pitch, or register matters. Use [[Authentic Audio Evidence Log]] to keep the weekly proof trail.

## Commands

Run these from the vault root when checking audio:

```powershell
python Japanese\_audio\audit_audio_integrity.py --no-report
python Japanese\_audio\build_pronunciation_manifest.py --check
python Japanese\_audio\audit_reading_hints.py --fail-on-findings
python Japanese\_audio\stt_spot_check.py
```

Use the first command when a clip is missing, Obsidian reports a playback error, or the MP3 format is suspect. Use `python Japanese\_audio\stt_spot_check.py --live` only when `AZURE_SPEECH_KEY` is available and you want Azure Speech-to-Text triage against manifest source text.

## Reports

- `_ops/reports/japanese-audio-integrity-audit.txt`
- `_ops/reports/japanese-audio-pronunciation-audit.txt`
- `_ops/reports/japanese-audio-reading-hints-audit.txt`
- `Japanese/_audio/stt-spot-check-report.txt`

## References

- [[Pronunciation and Audio Accuracy]]
- [[Authentic Audio Source Setup]]
- [[Authentic Audio Evidence Log]]
- [[Pronunciation Correction Log]]
- [[Listening Overview]]
- [[Phase 1 Authentic Audio Spine]]
- [[Phase 2 Authentic Audio Spine]]
- [[Phase 3 Authentic Audio Spine]]
- [[Phase 4 Authentic Audio Spine]]
- [[Phase 5 Authentic Audio Spine]]
- [[Phase 5 Audio Assignment Ladder]]
