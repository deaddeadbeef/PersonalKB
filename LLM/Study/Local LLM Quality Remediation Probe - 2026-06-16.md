---
tags: [study, llm, local-llm, ollama, quality, evaluation, remediation, evidence]
up: "[[LLM/Study/LLM Mastery Dashboard]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice]
last-verified: 2026-06-16
last-machine-check: 2026-06-16T06:22:09+08:00
---

# Local LLM Quality Remediation Probe - 2026-06-16

> **One-line summary** The first focused remediation pass did not clear the quality hold: output-cap changes and stricter prompts did not fix `K-01`, and `C-01` only passed when the exact target bullet template was supplied. Later proofs remediated `K-01` with a calculator tool loop and `C-01` with explicit structured IDs plus deterministic rendering.

This extends [[LLM/Study/Local LLM First Endpoint Audit and Quality Probe - 2026-06-16|Local LLM First Endpoint Audit and Quality Probe - 2026-06-16]]. It is quality diagnosis, not quality readiness.

## Verdict

| Gate | Status | Evidence |
|---|---|---|
| Quality remediation runner | `hold` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\quality-remediation-runner\20260616-062209-quality-remediation-quality-remediation-results.json` |
| Markdown result | `hold` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\quality-remediation-runner\20260616-062209-quality-remediation-quality-remediation-results.md` |
| CSV result | `hold` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\quality-remediation-runner\20260616-062209-quality-remediation-quality-remediation-results.csv` |
| JSONL log | `hold` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\quality-remediation-runner\quality-remediation-runs.jsonl` |
| Runner script | `pass` compile | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\quality-remediation-runner.py` |

## Result Summary

| Field | Value |
|---|---|
| Run id | `20260616-062209-quality-remediation` |
| Status | `hold` |
| Runtime | Ollama |
| Model | `qwen3.5:2b-q4_K_M` |
| Route | `http://127.0.0.1:11434/api/chat` |
| Boundary | `loopback` |
| Thinking mode | `false` |
| Temperature | `0` |
| Cases | `8` focused variants over `K-01` and `C-01` |
| Pass / hold / error | `1` / `7` / `0` |
| Next action | Try model/tool remediation before claiming quality readiness. |

## Probe Outcomes

| Probe | Variable changed | Decision | What happened |
|---|---|---|---|
| `K-01-original-256` | none; original prompt with stricter scoring | `hold` | Started with `answer=508`, self-corrected later, and hit length. |
| `K-01-cap512` | output cap only: `256` to `512` | `hold` | More room produced more self-correction, but still began with `answer=508` and hit length. |
| `K-01-strict-prompt-256` | prompt contract only | `hold` | Returned one line, but kept the wrong `answer=508`. |
| `K-01-guided-prompt-128` | prompt scaffold with arithmetic decomposition | `hold` | Returned `answer=84` and a confused reason. |
| `C-01-original-256` | none; original prompt with strict scoring | `hold` | Returned three long bullet lines instead of two five-word bullets. |
| `C-01-cap64` | output cap only: `256` to `64` | `hold` | Still produced three bullet lines and was truncated. |
| `C-01-strict-prompt-128` | prompt contract only | `hold` | Returned five bullet lines instead of two. |
| `C-01-template-prompt-64` | prompt scaffold with exact target lines | `pass` | Copied two five-word bullet lines exactly. |

## Interpretation

- Increasing the output cap did not remediate the arithmetic or constraint failures.
- Stricter prompting did not remediate `K-01`; the current model repeatedly produced incorrect arithmetic and contradictory self-correction.
- Stricter prompting alone did not remediate `C-01`; exact-template prompting did, which means a heavily constrained scaffold can force this narrow format but does not prove general instruction-following quality.
- The endpoint, chat template, tokenizer, and loopback security layers are already proven enough for this diagnosis. The likely owner is quality/model capability for `K-01`, with prompt/control fragility for `C-01`.

## What This Proves

- The first quality hold is real and reproducible enough to block workload-quality claims.
- `qwen3.5:2b-q4_K_M` should not be promoted as quality-ready from the first run.
- Arithmetic-like tasks should route to a deterministic tool, a stronger model, or a separate model-selection comparison before this local setup supports real work.
- Strict formatting tasks need either exact templates, structured-output controls, or a stronger instruction-following model before they count as reliable.

## Follow-Up

[[LLM/Study/Local LLM Calculator Tool Remediation Proof - 2026-06-16|Local LLM Calculator Tool Remediation Proof - 2026-06-16]] resolved the arithmetic branch of this hold for `K-01` by using a native Ollama calculator tool loop:

- deterministic calculator output: `410`
- bad expression denial: passed before execution
- native model tool-call emission: passed
- native tool-result follow-up: returned `answer=410; reason=The calculation of 17 multiplied by 23 plus 19 results in 410.`
- direct ad hoc tool-result finalization: held because it copied placeholder-shaped text

[[LLM/Study/Local LLM Structured Format Remediation Proof - 2026-06-16|Local LLM Structured Format Remediation Proof - 2026-06-16]] resolved the strict-format branch of this hold for `C-01` by making the model emit validated IDs and letting the application render the final bullets:

- original free text: held with three long bullets
- free-form structured fields: held with off-topic six-word fields
- loose enum selection: held with invented labels
- explicit enum selection plus renderer: passed with `- Route proof verifies endpoint reachability` and `- Quality proof verifies useful behavior`
- bad-shape denial: passed before rendering

The remaining quality owner is now evidence reconciliation: future quality or evidence-pack audits must state which rows are model-owned, tool-owned, or renderer-owned.

## What This Does Not Prove

- That every larger local model would fail the same probes.
- That tool calling, RAG, or structured-output remediation would fail.
- That the current model is useless; JSON, extraction, grounded refusal, route proof, endpoint audit, and loopback security already passed.
- That the first inference evidence pack can pass; it should remain blocked or explicitly held until quality remediation has a defensible route.

## Next Actions

1. Use [[LLM/Study/Local LLM Calculator Tool Remediation Proof - 2026-06-16|Local LLM Calculator Tool Remediation Proof - 2026-06-16]] as the accepted `K-01` arithmetic remediation route.
2. Use [[LLM/Study/Local LLM Structured Format Remediation Proof - 2026-06-16|Local LLM Structured Format Remediation Proof - 2026-06-16]] as the accepted `C-01` strict-format remediation route.
3. Use [[LLM/Study/LLM Inference Request Lifecycle Runner|LLM Inference Request Lifecycle Runner]] before claiming the full first-run packet, so the endpoint, tool, schema, validation, rendering, and final output phases are explicit.
4. Do not run [[LLM/Study/Local LLM First Inference Evidence Pack Audit Runner|Local LLM First Inference Evidence Pack Audit Runner]] as a pass attempt until the audit input distinguishes model-owned, tool-owned, and renderer-owned rows.

## References

Internal routes:

- [[LLM/Study/Local LLM First Endpoint Audit and Quality Probe - 2026-06-16]]
- [[LLM/Study/Local LLM First Quality Probe Runner]]
- [[LLM/Study/Local LLM First Quality Probe Suite]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Decoding and Sampling Controls Runner]]
- [[LLM/Study/Local LLM Calculator Tool Remediation Proof - 2026-06-16]]
- [[LLM/Study/Local LLM Structured Format Remediation Proof - 2026-06-16]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]]
- [[LLM/Study/Local LLM Model Selection Runner]]
- [[LLM/Study/Local LLM Runtime Comparison Runner]]
- [[LLM/Study/Local LLM First Inference Evidence Pack Audit Runner]]
