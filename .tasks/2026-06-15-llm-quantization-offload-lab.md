---
tags: [task, llm, local-llm, quantization]
status: done
date: 2026-06-15
---

# 2026-06-15 LLM Quantization Offload Lab

## Done

- Added [[LLM/Study/Local LLM Quantization and GPU Offload Lab]].
- Connected quantization concepts to local runtime choices: GGUF, AWQ, GPTQ, FP8/INT8, KV-cache precision, and GPU offload.
- Added a lab sequence for baseline memory estimation, quantization A/B, offload sweep, KV-cache/context stress, quality regression, and decision recording.
- Routed the lab through the LLM study index, top-level map, sizing guide, compatibility matrix, benchmark log, quality harness, operations/troubleshooting notes, roadmap, capstone, and self-assessment.
- Regenerated the vault index and audit summary after edits.

## Verification

- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`
- focused `rg` checks for the new note, route links, placeholder markers, and audit summary fields
