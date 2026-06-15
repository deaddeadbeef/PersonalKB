---
tags: [study, llm, local-llm, inference, lifecycle, ollama, evidence, proof]
up: "[[LLM/Study/LLM Mastery Dashboard]]"
confidence: verified
tier-coverage: [core, practice]
last-verified: 2026-06-16
last-machine-check: 2026-06-16T07:05:33+08:00
---

# Local LLM Request Lifecycle Proof - 2026-06-16

> **One-line summary** A saved local Ollama native request now has a full eight-phase lifecycle trace from client request through prompt assembly, tokenization, prefill, decode, stop, detokenization, and application handling; the OpenAI-compatible trace is useful route evidence but still lacks native prefill timing.

This note is request-lifecycle proof for the first local endpoint. It uses saved request and response artifacts; it did not send a new generation request. Use it with [[LLM/Study/LLM Inference Request Lifecycle Runner|LLM Inference Request Lifecycle Runner]], [[LLM/Study/LLM Inference Request Lifecycle Lab|LLM Inference Request Lifecycle Lab]], and [[LLM/Study/Local LLM End-to-End Mental Model|Local LLM End-to-End Mental Model]].

## Verdict

| Gate | Status | Evidence |
|---|---|---|
| Native request lifecycle | `pass/lifecycle_trace_ready` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\request-lifecycle-runner\20260616-0708-request-lifecycle-native-smoke\20260616-0708-request-lifecycle-native-smoke-lifecycle-results.json` |
| Native phase CSV | `pass`, 8 phase rows, 0 findings | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\request-lifecycle-runner\20260616-0708-request-lifecycle-native-smoke\20260616-0708-request-lifecycle-native-smoke-lifecycle-phases.csv` |
| Native Markdown summary | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\request-lifecycle-runner\20260616-0708-request-lifecycle-native-smoke\20260616-0708-request-lifecycle-native-smoke-lifecycle-results.md` |
| OpenAI-compatible contrast | `hold/lifecycle_trace_partial` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\request-lifecycle-runner\20260616-0708-request-lifecycle-openai-compatible-smoke\20260616-0708-request-lifecycle-openai-compatible-smoke-lifecycle-results.json` |

## Native Lifecycle Trace

| Phase | Status | Evidence | Meaning |
|---|---|---|---|
| Client request | `pass` | `model=qwen3.5:2b-q4_K_M`; `stream=False`; sampler `temperature=0`, `num_predict=32`, `think=false` | The saved request preserves the exact local model and deterministic controls. |
| Prompt assembly | `pass` | prompt text `Reply with exactly: local llm ok`; `prompt_chars=32` | The request under test is inspectable before tokenization. |
| Tokenization | `pass` | `prompt_tokens=20` | The input is small enough that this is route proof, not long-context proof. |
| Prefill | `pass` | `prefill_s=0.1242`; `prompt_tokens_per_s=161.0903`; `load_s=0.4054` | The input-side compute is separated from cold load and decode. |
| Decode loop | `pass` | `output_tokens=5`; `decode_s=0.1587`; `decode_tokens_per_s=31.5113` | The output-side token production is measured separately. |
| Stop condition | `pass` | `finish_reason=stop`; `done=True` | Generation ended cleanly rather than by parse failure or cap-only truncation. |
| Detokenization and parse | `pass` | output `local llm ok`; exact text match `true` | The returned text crossed the application boundary for this route-smoke task. |
| Application handling | `pass` | `phase_holds=0`; `findings=0` | The next owner is benchmark, quality, or capstone evidence rather than request reconstruction. |

## OpenAI-Compatible Contrast

The OpenAI-compatible route returned the same visible text and preserved model, message, prompt token, completion token, sampler, stop, and output evidence. It held at the lifecycle level because the saved response did not expose native `prompt_eval_duration`, TTFT, or equivalent prefill timing.

| Phase | Status | Evidence |
|---|---|---|
| Client request | `pass` | `max_tokens=512`, `temperature=0` |
| Prompt assembly | `pass` | one user message, `prompt_chars=38` |
| Tokenization | `pass` | `prompt_tokens=18` |
| Prefill | `hold` | no prefill timing or TTFT evidence |
| Decode loop | `pass` | `completion_tokens=156`, but no decode duration |
| Application handling | `hold` | prefill timing is missing |

This is not an endpoint failure. It means the native route is the stronger source for request-phase timing, while the OpenAI-compatible route remains useful for client compatibility and token accounting.

## What This Proves

- The first local endpoint proof now has one saved request/response pair mapped across all eight lifecycle phases.
- The native Ollama response can separate cold load, prefill, decode, stop, and output handling for the controlled `local llm ok` smoke task.
- The request lifecycle runner now captures nested Ollama `options` values, so sampler evidence includes `temperature`, `num_predict`, and `think`.
- The local inference explanation can distinguish route proof, timing proof, compatibility proof, and quality proof instead of treating a chat response as one undifferentiated success.

## What This Does Not Prove

- It does not prove long-context behavior, streaming TTFT, concurrency, prompt-cache reuse, or scheduler behavior.
- It does not prove workload quality; the quality boundary remains the first quality probe plus the calculator and structured-format remediation notes.
- It does not prove OpenAI-compatible prefill/decode timing. That requires streaming timing, a native timing route, server trace evidence, or a client harness with measured TTFT.
- It does not prove academic mastery; a no-notes paper defense and academic-to-local defense matrix are still pending.

## Next Actions

1. Treat the request-lifecycle runner gate as passed for the native first-smoke request in [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]].
2. Use [[LLM/Study/Local LLM First Streaming Timing Runner|Local LLM First Streaming Timing Runner]] or [[LLM/Study/Local LLM First Client Harness Runner|Local LLM First Client Harness Runner]] to add client-side TTFT for the OpenAI-compatible route.
3. Run the first inference evidence-pack audit only after it explicitly reconciles route proof, native lifecycle proof, OpenAI-compatible compatibility, first-quality hold, calculator tool ownership, structured renderer ownership, and loopback security.
4. Continue the academic track with [[LLM/Study/LLM Paper Oral Defense Runner|LLM Paper Oral Defense Runner]] and [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner|LLM Academic-to-Local Defense Matrix Runner]].

## References

Internal routes:

- [[LLM/Study/LLM Mastery Dashboard]]
- [[LLM/Study/LLM Mastery Status Snapshot - 2026-06-16]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/Local LLM First Inference Proof - 2026-06-16]]
- [[LLM/Study/Local LLM First Endpoint Audit and Quality Probe - 2026-06-16]]
- [[LLM/Study/Local LLM Quality Remediation Probe - 2026-06-16]]
- [[LLM/Study/Local LLM Calculator Tool Remediation Proof - 2026-06-16]]
- [[LLM/Study/Local LLM Structured Format Remediation Proof - 2026-06-16]]
- [[LLM/Study/Local LLM Security and Privacy Proof - 2026-06-16]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/LLM Inference Request Lifecycle Runner]]
- [[LLM/Study/Local LLM End-to-End Mental Model]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]

Evidence files:

- `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\first-smoke-request-think-false\native-generate-request.json`
- `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\first-smoke-request-think-false\native-generate-response.json`
- `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\first-smoke-request-openai-long-cap\openai-chat-request.json`
- `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\first-smoke-request-openai-long-cap\openai-chat-response.json`
