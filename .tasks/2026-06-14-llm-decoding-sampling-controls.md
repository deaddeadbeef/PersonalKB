---
status: done
topic: llm
created: 2026-06-14
---

# LLM Decoding And Sampling Controls Slice

## Goal

Add the missing study layer between "one request lifecycle" and "benchmark/quality evaluation": a dedicated lab for decoding and sampling controls that connects logits, filters, penalties, stopping, structured output, and runtime-specific local LLM parameters.

## Scope

- Add [[LLM/Study/Decoding and Sampling Controls Lab]].
- Wire it into the LLM study index, main LLM hub, roadmap, capstone workbook, self-assessment exam, request lifecycle lab, benchmark log, client harness, API contract lab, quality harness, and inference review drill.
- Regenerate the PersonalKB index and audit reports after edits.

## Verification

- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`
- Spot-check backlinks and generated audit counts.
