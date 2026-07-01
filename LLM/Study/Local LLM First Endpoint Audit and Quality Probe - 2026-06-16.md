---
tags: [study, llm, inference, local-llm, ollama, endpoint, audit, quality, evidence]
up: "[[LLM/Study/LLM Mastery Dashboard]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice]
last-verified: 2026-06-16
last-machine-check: 2026-06-16T06:22:09+08:00
---

# Local LLM First Endpoint Audit and Quality Probe - 2026-06-16

> **One-line summary** The first Ollama endpoint evidence now audits cleanly, but the first quality probe is a real hold: `qwen3.5:2b-q4_K_M` passed 3 of 5 private probes after `think=false`, and failed arithmetic/format discipline plus strict constraint following.

This note extends [[LLM/Study/Local LLM First Inference Proof - 2026-06-16|Local LLM First Inference Proof - 2026-06-16]]. It upgrades the endpoint from route proof to audited endpoint proof, but it does not upgrade the model to workload-quality ready.

Security update: [[LLM/Study/Local LLM Security and Privacy Proof - 2026-06-16|Local LLM Security and Privacy Proof - 2026-06-16]] now records security/privacy runner `pass/loopback_private_ready` for the current loopback-only endpoint. That does not change the quality hold.

Remediation update: [[LLM/Study/Local LLM Quality Remediation Probe - 2026-06-16|Local LLM Quality Remediation Probe - 2026-06-16]] reran the held `K-01` and `C-01` families with output-cap and prompt-contract variants. It stayed `hold`: `1` pass, `7` hold, `0` error.

## Verdict

| Gate | Status | Evidence |
|---|---|---|
| Chat template and tokenizer compatibility | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\chat-template-tokenizer-compatibility-runs\chat-template-qwen35-2b-q4-2026-06-16\chat-template-qwen35-2b-q4-2026-06-16-chat-template-compatibility.json` |
| First endpoint evidence audit | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\first-endpoint-evidence-audit\first-endpoint-audit-qwen35-2b-q4-2026-06-16\first-endpoint-audit-qwen35-2b-q4-2026-06-16-first-endpoint-evidence-audit.json` |
| First quality probe, initial run | `hold` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\first-quality-probe-runner\20260616-055256-first-quality-probe-quality-probe-results.json` |
| First quality probe, `think=false` rerun | `hold` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\first-quality-probe-runner\20260616-055447-first-quality-probe-quality-probe-results.json` |
| Focused quality remediation | `hold` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\quality-remediation-runner\20260616-062209-quality-remediation-quality-remediation-results.json` |
| Security/privacy runner | `pass` for loopback | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\security-privacy-runner\20260616-060509-security-results.json` |
| Runner repair | `pass` | [[LLM/Study/Local LLM First Quality Probe Runner]] now records `LOCAL_LLM_THINK` and sends `think` in `/api/chat` requests. |

## Endpoint Audit

The first endpoint evidence audit passed after the run folder received root-level support artifacts for the default audit globs:

| Support artifact | Purpose |
|---|---|
| `run-card.md` | Stable run identity: runtime, model, base URLs, boundary, evidence root, next decision. |
| `decision.md` | Endpoint decision: keep only for first quality probing, not deployment. |
| `first-smoke-summary-pass.json` | Root-level alias to the final passing smoke summary. |
| `ollama-native-response.json` | Root-level alias to the passing native response. |
| `openai-compatible-chat.json` | Root-level alias to the passing OpenAI-compatible response. |

Audit output:

| Metric | Value |
|---|---|
| Status | `pass` |
| Decision | `first_endpoint_evidence_ready` |
| Gate count | `12` |
| Pass count | `11` |
| Hold count | `0` |
| Fail count | `0` |
| Critical gap count | `0` |
| Finding count | `0` |

## Compatibility Control

The compatibility runner passed `9` of `9` rows:

| Row family | Evidence |
|---|---|
| Upstream first response debrief | Health-bound debrief JSON status `pass`, runtime health decision `runtime_health_ready`, model `qwen3.5:2b-q4_K_M`. |
| Model package | `ollama show` metadata for `qwen3.5:2b-q4_K_M`, GGUF, `2.3B`, `Q4_K_M`. |
| Tokenizer and special tokens | `tokenizer.ggml.*` metadata, EOS token id `248046`, context length `262144`. |
| Chat template | Ollama modelfile reports `TEMPLATE {{ .Prompt }}`, `RENDERER qwen3.5`, and `PARSER qwen3.5`. |
| Rendered prompt | Public response does not expose rendered prompt; saved behavior controls prove `/api/chat` route behavior instead. |
| Route behavior | `/api/chat` returned `CHAT_ROUTE_OK` from system/user messages. |
| Tokenizer sanity | Five prompt-eval count controls were saved for plain English, mixed script, code identifier, JSON boundary, and special-token-looking text. |
| Stop and role boundary | JSON-mode control returned `{"ok":true}` with no role-marker leakage. |
| Benchmark/quality link | First response debrief contributes the route-only timing row; quality remains separate. |

## Quality Probe Result

The first run without an explicit thinking control held all five probes because Qwen spent the `256` token cap in `message.thinking` and emitted empty final content. The runner now sends `think=false`; the rerun reached final content and produced a real first quality signal.

| Prompt | Class | Auto decision | Observed result |
|---|---|---|---|
| `K-01` | Known-answer arithmetic | `hold` | Output began with wrong `answer=508`, later self-corrected to `410`, and hit length. |
| `S-01` | Structured output | `pass` | Valid JSON with `tokens_per_second` equal to `32.0`. |
| `X-01` | Extraction | `pass` | Extracted only server, model, and run-folder facts from supplied text. |
| `G-01` | Grounded refusal | `pass` | Returned exactly `not enough evidence`. |
| `C-01` | Constraint following | `hold` | Returned three long bullets instead of two bullets with five words each. |

Summary:

| Metric | Value |
|---|---|
| Status | `hold` |
| Endpoint audit status | `pass` |
| Case count | `5` |
| Pass count | `3` |
| Hold count | `2` |
| Error count | `0` |
| Thinking mode | `false` |
| Boundary | `loopback` |

## Interpretation

This endpoint is now credible enough for further controlled local experiments. It is not credible enough for real workload use without more evaluation.

- The endpoint layer is no longer the blocker.
- The chat/template/tokenizer layer is not the first suspected failure owner for this run.
- `think=false` is required when this runner checks final answer content for a thinking-capable model.
- The first model-quality failures are answer discipline and strict instruction following.
- The first remediation pass did not clear those failures: output-cap changes did not help, stricter prompting did not fix arithmetic, and strict constraints only passed with an exact template.
- The current security/privacy proof allows only one-person loopback experimentation, not LAN, UI, RAG, tool, or deployment handoff.
- The next controlled action should test deterministic arithmetic/tool routing, structured-output controls, or a stronger local model before changing the quality claim.

## Next Actions

1. Use [[LLM/Study/Local LLM Tool Calling and Structured Output Runner|Local LLM Tool Calling and Structured Output Runner]] to prove deterministic arithmetic/tool-result remediation before trusting calculation-like work.
2. Use [[LLM/Study/Local LLM Model Selection Runner|Local LLM Model Selection Runner]] or [[LLM/Study/Local LLM Runtime Comparison Runner|Local LLM Runtime Comparison Runner]] if a stronger local model is tested for the held prompts.
3. Keep the endpoint loopback-only; run a separate LAN/auth/firewall/UI/RAG/tool proof before any non-loopback, UI, RAG, or tool handoff.
4. Run [[LLM/Study/Local LLM First Inference Evidence Pack Audit Runner|Local LLM First Inference Evidence Pack Audit Runner]] only as a documented hold until quality is resolved or explicitly accepted as a limitation.
5. Keep [[LLM/Study/LLM Paper Oral Defense Runner|LLM Paper Oral Defense Runner]] on the academic track; endpoint proof does not prove paper-level mastery.

## References

Internal routes:

- [[LLM/Study/Local LLM First Inference Proof - 2026-06-16]]
- [[LLM/Study/Local LLM Quality Remediation Probe - 2026-06-16]]
- [[LLM/Study/Local LLM Security and Privacy Proof - 2026-06-16]]
- [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]]
- [[LLM/Study/Local LLM First Quality Probe Runner]]
- [[LLM/Study/Local LLM First Quality Probe Suite]]
- [[LLM/Study/Decoding and Sampling Controls Runner]]
- [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Runner]]
- [[LLM/Study/Local LLM Security and Privacy Runner]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
