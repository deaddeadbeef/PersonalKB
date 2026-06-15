---
tags: [study, llm, inference, local-llm, ollama, evidence, proof, windows]
up: "[[LLM/Study/LLM Mastery Dashboard]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-16
last-machine-check: 2026-06-16T06:22:09+08:00
---

# Local LLM First Inference Proof - 2026-06-16

> **One-line summary** This workstation now has a working local Ollama endpoint on loopback: model store, runtime install, model pull, runtime health, native response, OpenAI-compatible response, first response debrief, endpoint audit, and loopback security/privacy proof all have saved evidence.

This is route and loopback-boundary proof, not a quality or mastery certificate. Quality remediation, benchmark audit, lifecycle evidence, non-loopback security, and academic oral-defense proof still need their own rows.

Update: [[LLM/Study/Local LLM First Endpoint Audit and Quality Probe - 2026-06-16|Local LLM First Endpoint Audit and Quality Probe - 2026-06-16]] records endpoint evidence audit `pass`, chat/template/tokenizer compatibility `pass`, and first quality probe `hold` at 3/5. [[LLM/Study/Local LLM Quality Remediation Probe - 2026-06-16|Local LLM Quality Remediation Probe - 2026-06-16]] records focused remediation `hold`, 1/8 pass, 7/8 hold, 0 errors. [[LLM/Study/Local LLM Security and Privacy Proof - 2026-06-16|Local LLM Security and Privacy Proof - 2026-06-16]] records security/privacy runner `pass/loopback_private_ready` for the current loopback-only endpoint.

## Verdict

| Gate | Status | Evidence |
|---|---|---|
| Model store bootstrap | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-model-store-bootstrap\first-local-llm-model-store-bootstrap-model-store-bootstrap.json` |
| Post-bootstrap readiness | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-model-store-bootstrap\first-local-llm-post-bootstrap-readiness-readiness.json` |
| Windows runtime install | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-ollama-install-gate\first-local-inference-runtime-install\first-local-inference-runtime-install-runtime-install.json` |
| Selected model source check | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\first-model-source-recheck\first-model-source-recheck-selected-qwen35-2b-q4\first-model-source-recheck-selected-qwen35-2b-q4-model-source-recheck.json` |
| Model pull audit | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\first-qwen35-2b-q4-pull\first-qwen35-2b-q4-pull-first-model-pull.json` |
| Runtime health | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\first-runtime-health-qwen35-2b-q4\first-runtime-health-qwen35-2b-q4-runtime-health.json` |
| Native smoke response | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\first-smoke-request-think-false\native-generate-response.json` |
| OpenAI-compatible smoke response | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\first-smoke-request-openai-long-cap\openai-chat-response.json` |
| Combined smoke summary | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\first-smoke-request-final\first-smoke-final-qwen35-2b-q4-summary.json` |
| First response debrief | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\first-response-debrief\first-smoke-final-qwen35-2b-q4-debrief.json` |
| Endpoint audit and first quality probe | `hold` for quality | [[LLM/Study/Local LLM First Endpoint Audit and Quality Probe - 2026-06-16]] |
| Focused quality remediation | `hold` | [[LLM/Study/Local LLM Quality Remediation Probe - 2026-06-16]] |
| Security/privacy runner | `pass` for loopback | [[LLM/Study/Local LLM Security and Privacy Proof - 2026-06-16]] |

## Machine And Runtime

| Field | Value |
|---|---|
| Runtime | Ollama for Windows |
| Version | `ollama version is 0.30.8` |
| Command path | `C:\Users\fpan1\AppData\Local\Programs\Ollama\ollama.EXE` |
| Native base URL | `http://127.0.0.1:11434` |
| OpenAI-compatible base URL | `http://127.0.0.1:11434/v1` |
| Security boundary | loopback only |
| Model store | `D:\Models\ollama` via user `OLLAMA_MODELS` |
| Hugging Face cache variables | `HF_HOME=D:\Models\hf`, `HF_HUB_CACHE=D:\Models\hf\hub` |
| Installer evidence | saved `ollama-install.ps1`, SHA256 `2EC01CB2F5324DA8C89177C97FF994B9344C03F269DADE4925668C44E25532D8`, downloaded from `https://ollama.com/install.ps1` |
| Installer signature | saved output reports valid Authenticode signer `Ollama Inc.` |

## Model

| Field | Value |
|---|---|
| Selected tag | `qwen3.5:2b-q4_K_M` |
| Why this tag | Source recheck found the smaller fallback still matched required live snippets; the older 4B/control expected snippets had drifted. |
| Source page | `https://ollama.com/library/qwen3.5/tags` |
| Source digest snippet | `124a03c34777` |
| Runtime digest | `124a03c347777e8e4e5955c33610ae01d9d90d8c2a718bfba069c498d5c7f3c9` |
| Size | `1.9 GB` in `ollama ls`; API size `1945323638` bytes |
| Parameter size | `2.3B` |
| Quantization | `Q4_K_M` |
| Context length reported by API | `262144` |
| Capabilities reported by API | `vision`, `completion`, `tools`, `thinking` |
| License in runtime metadata | Apache License 2.0 text is present in saved `/api/show` response |

## First Responses

| Route | Request condition | Output | Status |
|---|---|---|---|
| Native `/api/generate` | `think=false`, temperature `0`, output cap `32` | `local llm ok` | `pass` |
| OpenAI-compatible `/v1/chat/completions` | temperature `0`, output cap `512` | `local llm ok` | `pass` |

The first fixed-cap smoke runner attempts with `16` and `128` tokens returned HTTP 200 but held because Qwen's thinking output consumed the cap before answer content appeared. This is why the final proof uses the documented thinking control for the native route and a larger cap for the OpenAI-compatible route.

## First Debrief

| Field | Value |
|---|---|
| Debrief status | `pass` |
| Model match | `true` |
| Text match | `true` |
| Mechanism owner | `cold load` |
| Total seconds | `0.691` |
| Load seconds | `0.405` |
| Prompt tokens/sec | `161.09` |
| Decode tokens/sec | `31.51` |
| Quality boundary | route-only until [[LLM/Study/Local LLM First Quality Probe Suite]] or [[LLM/Study/Local LLM First Quality Probe Runner]] is scored |

## What This Proves

- Ollama is installed and reachable on the Windows host.
- The custom model store is active before model pull.
- A source-checked Ollama tag was pulled into `D:\Models\ollama`.
- Native and OpenAI-compatible loopback routes can return a controlled local response.
- The first response can be interpreted through load, prefill, and decode timing fields.

## What This Does Not Prove

- No-notes academic command of LLM papers or mechanisms.
- Workload quality for coding, Japanese study, RAG, tools, long context, or structured output. The first quality probe is measured and the focused remediation pass still held.
- Loopback security/privacy now has a no-generation proof, but non-loopback security, authentication, LAN exposure, UI integration, RAG, and tool safety remain unproven.
- Stable benchmark performance under repeated runs, streaming, concurrency, or service restarts.
- Capstone readiness; the endpoint evidence and inference evidence pack audits still need to run.

## Next Actions

1. Route the arithmetic failure through [[LLM/Study/Local LLM Tool Calling and Structured Output Runner|Local LLM Tool Calling and Structured Output Runner]] or stronger-model selection before trusting calculation-like work.
2. Run [[LLM/Study/Local LLM First Inference Evidence Pack Audit Runner|Local LLM First Inference Evidence Pack Audit Runner]] only as a documented hold until quality is resolved or explicitly accepted as a limitation.
3. Keep the endpoint loopback-only until a separate LAN/auth/firewall/UI/RAG/tool proof exists.
4. Use [[LLM/Study/LLM Inference Request Lifecycle Runner|LLM Inference Request Lifecycle Runner]] to map the saved request and response into prompt assembly, tokenization, prefill, decode, stop, detokenization, and application handling.
5. Continue the academic track with [[LLM/Study/LLM Paper Oral Defense Runner|LLM Paper Oral Defense Runner]] and [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner|LLM Academic-to-Local Defense Matrix Runner]].

## References

Internal routes:

- [[LLM/Study/LLM Mastery Status Snapshot - 2026-06-16]]
- [[LLM/Study/Local LLM First Endpoint Audit and Quality Probe - 2026-06-16]]
- [[LLM/Study/Local LLM Quality Remediation Probe - 2026-06-16]]
- [[LLM/Study/Local LLM Security and Privacy Proof - 2026-06-16]]
- [[LLM/Study/LLM Mastery Dashboard]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/Local LLM Model Store Bootstrap Runner]]
- [[LLM/Study/Local LLM Windows Runtime Install Runner]]
- [[LLM/Study/Local LLM First Model Source Recheck Runner]]
- [[LLM/Study/Local LLM First Model Pull Runner]]
- [[LLM/Study/Local LLM First Runtime Health Runner]]
- [[LLM/Study/Local LLM First Smoke Request Runner]]
- [[LLM/Study/Local LLM First Response Debrief Runner]]

External/current sources checked 2026-06-16:

- [Ollama Windows documentation](https://docs.ollama.com/windows)
- [Ollama Windows download page](https://ollama.com/download/windows)
- [Ollama thinking documentation](https://docs.ollama.com/capabilities/thinking)
- [Ollama generate endpoint](https://docs.ollama.com/api/generate)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
