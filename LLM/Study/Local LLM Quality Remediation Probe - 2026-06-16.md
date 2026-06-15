---
tags: [study, llm, local-llm, ollama, quality, evaluation, remediation, evidence]
up: "[[LLM/Study/LLM Mastery Dashboard]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-16
last-machine-check: 2026-06-16T06:22:09+08:00
---

# Local LLM Quality Remediation Probe - 2026-06-16

> **One-line summary** The first focused remediation pass did not clear the quality hold: output-cap changes and stricter prompts did not fix `K-01`, and `C-01` only passed when the exact target bullet template was supplied.

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

## What This Does Not Prove

- That every larger local model would fail the same probes.
- That tool calling, RAG, or structured-output remediation would fail.
- That the current model is useless; JSON, extraction, grounded refusal, route proof, endpoint audit, and loopback security already passed.
- That the first inference evidence pack can pass; it should remain blocked or explicitly held until quality remediation has a defensible route.

## Next Actions

1. Route arithmetic remediation through [[LLM/Study/Local LLM Tool Calling and Structured Output Runner|Local LLM Tool Calling and Structured Output Runner]] or a deterministic calculator/tool-result-injection proof.
2. Route general quality remediation through [[LLM/Study/Local LLM Model Selection Runner|Local LLM Model Selection Runner]] or [[LLM/Study/Local LLM Runtime Comparison Runner|Local LLM Runtime Comparison Runner]] if a stronger local model is tested.
3. Route strict-format remediation through [[LLM/Study/Decoding and Sampling Controls Runner|Decoding and Sampling Controls Runner]] plus structured-output controls before repeating the full quality probe.
4. Do not run [[LLM/Study/Local LLM First Inference Evidence Pack Audit Runner|Local LLM First Inference Evidence Pack Audit Runner]] as a pass attempt until the quality route is either remediated or explicitly accepted as a documented hold.

## References

Internal routes:

- [[LLM/Study/Local LLM First Endpoint Audit and Quality Probe - 2026-06-16]]
- [[LLM/Study/Local LLM First Quality Probe Runner]]
- [[LLM/Study/Local LLM First Quality Probe Suite]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Decoding and Sampling Controls Runner]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]]
- [[LLM/Study/Local LLM Model Selection Runner]]
- [[LLM/Study/Local LLM Runtime Comparison Runner]]
- [[LLM/Study/Local LLM First Inference Evidence Pack Audit Runner]]
