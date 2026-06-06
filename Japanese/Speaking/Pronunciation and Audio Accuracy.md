---
tags: [japanese, speaking, pronunciation, audio, quality]
up: "[[Speaking Overview]]"
confidence: policy
tier-coverage: [intuition, core, practice]
---

# Pronunciation and Audio Accuracy

> Use this page when deciding whether an audio clip is good enough to learn from. The short rule: native/official audio is the model, local TTS is the drill layer, and accent dictionaries are the referee when pitch or reading is uncertain.

## Source Priority

| Need | First choice | Use local TTS for |
| --- | --- | --- |
| Phrase rhythm and intonation | [[Phase 1 Authentic Audio Spine]] or tutor/native recording | Repeating the exact phrase after checking it against native audio |
| Isolated word pronunciation | Native speaker recording, Forvo, course audio, or dictionary audio | Fast review and recall once the reading is known |
| Pitch accent | NHK accent dictionary, OJAD, or course/tutor feedback | Awareness drills only; do not treat TTS pitch as authoritative |
| Particles and kana traps | Native audio plus local clips with explicit reading hints | High-repetition drills for は/へ/を, long vowels, small っ, and ん |
| New generated clip | Pronunciation manifest plus a native/source check when the item is ambiguous | Controlled playback in Obsidian after the check passes |

Local audio is useful because it is always available inside Obsidian. It is not a substitute for human-recorded speech.

## Trust Rules

Treat a local clip as safe for daily practice when all of these are true:

- The displayed Japanese and the synthesized reading are both known.
- Particles, counters, names, and ambiguous kanji have explicit reading hints when needed.
- The phrase is short enough that TTS prosody will not become the main model.
- A native/official source confirms the general rhythm, or the clip is only an isolated-sound drill.
- The clip exists in [[Audio Index]] and passes the local manifest/audit scripts.

Treat a clip as suspect when any of these are true:

- It contains table fragments, English placeholders, empty symbols, or OCR-looking text.
- The written form can be read more than one way and no reading hint is recorded.
- It teaches pitch accent, connected-speech rhythm, keigo, names, counters, or a full sentence you will memorize.
- It sounds unlike the matching Genki, Irodori, NHK, tutor, OJAD, NHK dictionary, or Forvo reference.

## Correction Workflow

When an audio item sounds wrong:

1. Add the filename, displayed text, and what sounded wrong to [[Pronunciation Correction Log]].
2. Check the item against [[Phase 1 Authentic Audio Spine]] if it is a phrase, or against OJAD/NHK/Forvo if it is a word or pitch issue.
3. If the source text is wrong, fix the source manifest or reading hint rather than only renaming the file.
4. Regenerate the affected clip.
5. Run `python Japanese\_audio\build_pronunciation_manifest.py --check`.
6. Run `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`.
7. Mark the correction in [[Pronunciation Correction Log]] and update the relevant learner page only after the checks pass.

Do not bury a suspect clip inside a practice ladder. Either fix it, replace it with a native/official audio target, or remove it from the daily path.

## Daily Learner Check

Use this once per study session:

1. Play one native/official segment from [[Phase 1 Authentic Audio Spine]].
2. Play the matching local drill from [[Phase 1 Local Audio Practice]].
3. Record yourself once.
4. Compare only one feature: vowel length, small っ, particle reading, ら行, ん, or pitch drop.
5. Log one learner correction in the current phase review: [[Phase 1 Weekly Review]], [[Phase 2 Weekly Review]], [[Phase 3 Weekly Review]], [[Phase 4 Weekly Review]], or [[Phase 5 Weekly Review]]. If the local clip itself is suspect, add it to [[Pronunciation Correction Log]].

One correction per day is enough. Pronunciation improves by repeated accurate comparison, not by trying to fix every sound at once.

## Phase Rules

| Phase | Audio accuracy target |
| --- | --- |
| Phase 1 | Avoid false habits: kana timing, particles, long vowels, small っ, and one native audio spine |
| Phase 2 | Add difficult sounds, ら行, ん variations, vowel devoicing, and daily shadowing |
| Phase 3 | Add pitch-accent awareness and dictionary checks through [[Phase 3 Pitch Accent Practice Path]] |
| Phase 4 | Check register, keigo, rhythm, and native-speed segments against human or official-course models |
| Phase 5 | Use tutor/native feedback and native-source output checks for rhythm, register, pitch, and natural delivery |

## References

- [[Phase 1 Local Audio Practice]]
- [[Phase 1 Authentic Audio Spine]]
- [[Phase 3 Weekly Review]]
- [[Phase 4 Weekly Review]]
- [[Pronunciation Correction Log]]
- [[Pronunciation — Difficult Sounds for English Speakers]]
- [[Pitch Accent — Introduction]]
- [[Pitch Accent — Common Patterns]]
- [[Phase 3 Pitch Accent Practice Path]]
- [[Sources Index#Pronunciation Sources Checked 2026-06-06]]
