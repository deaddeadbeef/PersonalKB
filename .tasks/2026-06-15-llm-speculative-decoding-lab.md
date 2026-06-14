# 2026-06-15 - LLM speculative decoding lab

## Goal

Add a local LLM speculative-decoding lab so draft-model, EAGLE, MTP, n-gram, and runtime-specific speculative paths are measured against a no-spec baseline before they are enabled for local inference.

## Scope

- Add `LLM/Study/Local LLM Speculative Decoding Lab.md`.
- Replace placeholder speculative-decoding references with actual chunks, papers, and runtime docs.
- Route the lab through the LLM MOC, study index, decoding controls, benchmark log, runtime comparison, compatibility matrix, sizing, concurrency, observability, lifecycle, troubleshooting, deployment matrix, roadmap, capstone workbook, and self-assessment exam.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

## Verification

- External docs checked: core speculative-decoding papers, vLLM speculative decoding/draft model docs, llama.cpp speculative decoding docs, SGLang speculative decoding docs, LM Studio app and SDK speculative decoding docs, Ollama Modelfile reference, and TensorRT-LLM speculative decoding tutorial.
- Regenerated `index.md` with `python _ops\personal_kb.py index`.
- Regenerated `_ops/reports/audit-summary.json` with `python _ops\personal_kb.py audit`.
- Audit result: 4,860 files, 2,989 markdown files, 849 candidate articles, 938 broken-link occurrences.
