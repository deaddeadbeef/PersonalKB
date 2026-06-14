---
status: done
topic: llm
created: 2026-06-14
---

# LLM Model Acquisition And Provenance Slice

## Goal

Add the missing "before download" checklist for local LLM work: model card, license, gated access, exact revision, artifact format, unsafe file types, cache path, digest/provenance, and whether the artifact is allowed for the target workload.

## Scope

- Add [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]].
- Wire it into the local hosting, preflight, sizing, compatibility, serving, security, troubleshooting, roadmap, capstone, self-assessment, and inference review paths.
- Regenerate the PersonalKB index and audit reports after edits.

## Verification

- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`
- Spot-check backlinks and generated audit counts.
