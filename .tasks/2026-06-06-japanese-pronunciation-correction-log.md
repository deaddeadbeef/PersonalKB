# Japanese Pronunciation Correction Log

Goal: add a dedicated QA log for suspect/resolved local pronunciation clips so audio corrections are visible before clips return to daily practice.

## Done

- Added `Japanese/Speaking/Pronunciation Correction Log.md`.
- Seeded the log with resolved corrections from prior audio OCR and reading-hint passes.
- Routed the log from the pronunciation QA guide, speaking/listening hubs, study index, Phase 1/2 coverage maps, and Phase 2 weekly review.

## Verification

- `python Japanese\_audio\build_pronunciation_manifest.py --check`
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`
- `python _ops\personal_kb.py audit`
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- Changed-page MP3 embed resolution check.
- `git diff --check`
