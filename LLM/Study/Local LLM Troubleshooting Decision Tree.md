---
tags: [study, llm, inference, local-llm, troubleshooting, diagnostics]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [practice]
---

# Local LLM Troubleshooting Decision Tree

> **One-line summary** Local LLM failures are diagnosable when each symptom is mapped to one layer: environment, model fit, server, route, client, prompt, tokenizer, RAG, quality, or security.

Use this after [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]] and alongside [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]]. The preflight proves the machine and runtime boundary. The serving runbook proves the endpoint. Use [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]] when the symptom may come from model source, license gate, revision, cache path, unsafe file type, or unclear artifact identity. Use [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] when a generic client, `/v1` route, streaming path, or feature flag fails. Use [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]] when the symptom may come from artifact format, quantization, tokenizer, chat template, runtime, route, or workload mismatch. Use [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]] when failures appear only on long prompts, RAG, tools, or multi-turn history. This note decides where to look when the run still fails.

The rule is simple: change one layer at a time, keep a short evidence record, and do not call a model "bad" until the environment, route, prompt format, and evaluation harness have been checked.

## Diagnostic Order

Run the checks in this order unless the error message clearly names a lower layer.

| Step | Question | If no, go to |
| --- | --- | --- |
| 1 | Does the machine/runtime preflight prove the intended CPU/GPU/RAM/disk path? | [[LLM/Study/Local LLM Environment Preflight Lab|Environment preflight]] |
| 2 | Is the chosen artifact allowed, pinned, downloaded into a known path, and safe enough to load? | [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|acquisition checklist]] |
| 3 | Does the chosen model fit the memory, context, artifact format, quantization, tokenizer, and runtime? | [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Sizing guide]] and [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|compatibility matrix]] |
| 4 | Is the server process running and listening on the intended host/port? | Server/process branch |
| 5 | Does the endpoint route and model id match the runtime's exposed API? | Route/model branch |
| 6 | Is the OpenAI-compatible API contract known for this route and model id? | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|API contract lab]] |
| 7 | Can a minimal non-streaming request return text? | [[LLM/Study/Local LLM Client Harness Lab|Client harness]] |
| 8 | Does the same request behave after streaming, parsing, stops, and schema constraints? | [[LLM/Study/LLM Inference Request Lifecycle Lab|Request lifecycle]] |
| 9 | Does instruction following fail because of tokenizer, chat template, roles, or stops? | [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat template lab]] |
| 10 | Is the answer slow but otherwise valid? | Performance branch and [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|context budget lab]] |
| 11 | Is the answer fast but wrong, unsupported, or unusable? | [[LLM/Study/Local LLM Quality Evaluation Harness|Quality harness]] |
| 12 | Does retrieval, citation, or private data change the failure? | [[LLM/Study/Local RAG Assistant Lab|RAG lab]] and [[LLM/Study/Local LLM Security and Privacy Runbook|security runbook]] |

Pass signal: the diagnosis names the failed layer and the next controlled change.

## Symptom Router

| Symptom | First branch | Evidence to capture |
| --- | --- | --- |
| Runtime command is missing | Environment | Command availability and install path. |
| GPU is not visible | Environment | `nvidia-smi` or runtime-specific hardware output from the server shell. |
| Model download fails | Model acquisition | Model id, license/auth requirement, revision, disk space, cache path. |
| Model file exists but will not load | Model fit | Format, quantization, RAM/VRAM, runtime error text. |
| Immediate OOM | Sizing | Weight memory, runtime overhead, GPU offload, free RAM/VRAM. |
| OOM only on long prompts | KV cache/context budget | Prompt tokens, context setting, concurrency, retrieved chunk count, output reserve. |
| Port already in use | Server/process | Listener list and owning process. |
| Connection refused | Server/process | Host, port, server log, listener after launch. |
| 404 or route not found | Route/model | Base URL, route, native vs OpenAI-compatible API, and API contract card. |
| Model id not found | Route/model | Served model list and exact model id. |
| Client times out | Client/server | Timeout, prompt length, server log, partial response. |
| Non-streaming works but streaming fails | Client stream | Raw stream event sample, parser error, final chunk. |
| JSON/schema output is invalid | Request boundary | Prompt, schema, stop reason, parser error, output excerpt. |
| Output starts in wrong role or leaks markers | Chat template | Tokenizer/template/role boundary evidence. |
| Output ignores instructions | Prompt/template/model quality | Template check, stronger prompt test, quality harness row. |
| First token is slow | Performance/context budget | TTFT, prompt tokens, queue time, load time, prefill context. |
| Later tokens are slow | Performance | Output tokens/sec, model size, quantization, offload, utilization. |
| Answer is plausible but wrong | Quality | Known-answer prompt, expected answer, rubric score. |
| RAG answer invents citations | RAG/evaluation | Retrieved top-k, supporting passage, cited answer, citation check. |
| Endpoint is reachable from another device | Security | Bind address, firewall/proxy/tunnel, auth decision. |

## Server And Route Branch

Use this when the client cannot reach the model.

| Check | Pass signal | Next fix if failed |
| --- | --- | --- |
| Server process exists | Runtime process is visible in task manager/process list/logs. | Start server or inspect startup failure. |
| Listener exists | Intended host and port appear in listener list. | Fix host/port flag, GUI server toggle, or stale process. |
| Bound address is safe | Loopback for one-person local experiments. | Rebind to `127.0.0.1` or run security checklist before sharing. |
| Model is loaded | Runtime model list includes exact id or local file. | Load model, correct id, or choose supported format. |
| Route matches API mode | Native routes and OpenAI-compatible routes are not mixed. | Add `/v1`, change `/chat/completions`, or use native runtime route. |
| Minimal non-streaming call works | `temperature=0`, small `max_tokens`, tiny prompt returns text. | Remove streaming/schema/RAG until baseline works. |

Do not debug a full app until this branch passes. First make one direct REST or client-harness call work.

## Model Fit Branch

Use this when the model fails to load, crashes, or barely fits.

| Check | Academic reason | Practical fix |
| --- | --- | --- |
| Weight memory estimate | Parameters multiplied by bytes per parameter sets the floor. | Smaller model, stronger quantization, or more VRAM/RAM. |
| KV-cache estimate | Cache grows with layers, context, hidden size, precision, and active sequences. | Lower context, fewer retrieved chunks, lower concurrency. |
| Format/runtime match | GGUF, safetensors, GPTQ, AWQ, and FP16 paths are not interchangeable. | Use [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Runtime and Model Compatibility Matrix]] to select a runtime that supports the file or download the right format. |
| Quantization risk | Lower precision can preserve speed/memory while harming hard tasks. | Benchmark less aggressive quantization or smaller higher-precision model. |
| Runtime overhead | Driver and runtime allocations consume memory beyond weight files. | Leave headroom; do not treat "barely loads" as a pass. |

Use [[LLM/2022 — Alignment and Chat/Quantization|Quantization]] and [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse|KV Cache and Context Reuse]] to explain the failure, not just fix it.

## Client And Request Branch

Use this when the server works but your client does not.

| Check | Evidence | First fix |
| --- | --- | --- |
| Base URL | Exact base URL in client config. | Use the runtime's local base URL, usually including `/v1` for OpenAI-compatible clients. |
| Route | Client route or SDK method. | Match chat vs completion vs native generate route. |
| Model id | Exact id in request body. | Copy from runtime model list, not from memory. |
| Body shape | Serialized JSON request. | Reduce to model, messages, temperature, max tokens, stream false. |
| Timeout | Client timeout and prompt length. | Raise timeout only after reducing prompt and checking server logs. |
| Streaming parser | Raw event sample and first parse error. | Make non-streaming pass, then parse stream deltas. |
| Error logging | One structured row per failure. | Use [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]]. |

Pass signal: the same prompt can be called twice with the same config and produces comparable log rows.

## Prompt, Template, And Tokenizer Branch

Use this when the endpoint responds but behavior looks wrong.

| Symptom | Likely layer | First test |
| --- | --- | --- |
| Assistant answers as the user | Role/template boundary | Inspect rendered chat template or switch to runtime-supported chat route. |
| System prompt is ignored | Prompt assembly or model alignment | Use a tiny instruction-following prompt with temperature 0. |
| Output includes `<|assistant|>` or role tokens | Chat template/tokenizer mismatch | Run [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]]. |
| Output cuts off too early | Stop sequence or max token cap | Remove custom stops, raise cap, inspect stop reason. |
| JSON has extra prose | Request boundary | Add schema validation or constrained decoding if supported. |
| Repeated runs vary too much | Sampling | Lower temperature, fix seed if supported, keep prompt unchanged. |

Do not fix prompt-format bugs by switching models first. A stronger model can hide a broken template without making the system understood.

## Performance Branch

Separate cold start, prefill, and decode.

| Measurement | If high or weak | Likely cause | First change |
| --- | --- | --- | --- |
| Load time | Slow first request only | Cold load, disk, model initialization | Warm model or separate load time from request latency. |
| TTFT | Slow before first token | Prompt length, prefill, queueing, prefix miss | Count the rendered context budget, shorten prompt, reduce retrieved context, check queue. |
| Decode tokens/sec | Slow after first token | Model size, memory bandwidth, backend/offload, quantization | Smaller model, better offload, quantization, runtime change. |
| Peak RAM/VRAM | Near limit | Weights, KV cache, runtime overhead | More headroom, lower context, lower concurrency. |
| Quality score | Low despite speed | Model/task fit, prompt, RAG, quantization | Run quality harness before declaring performance pass. |

The academic explanation should reference [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs|Serving Architectures and Throughput-Latency Trade-offs]], [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching|Batching and Continuous Batching]], and [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse|KV Cache and Context Reuse]].

## Quality And RAG Branch

Use this when the local model is callable and fast enough but the answer is not acceptable.

| Failure | First distinction | Evidence |
| --- | --- | --- |
| Wrong known fact | Model capability vs prompt ambiguity | Known-answer prompt, expected answer, generated answer. |
| Invalid format | Instruction following vs schema enforcement | Parser/validator output and request settings. |
| Weak code answer | Model capability vs missing execution feedback | Test result or compile error, not just subjective quality. |
| RAG misses answer | Retrieval failure vs model hallucination | Expected source, retrieved top-k, answer support. |
| Correct passage retrieved but answer wrong | Generation/grounding failure | Retrieved context plus generated claim mapping. |
| Citations are fake or loose | Citation boundary failure | Each citation mapped to supporting passage. |
| Refusal is too broad | Safety/task boundary | Prompt, policy boundary, and expected allowed answer. |

Use [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] for scoring and [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]] for retrieval-specific diagnosis.

## Diagnostic Record Template

Copy one row for each failure.

| Field | Value |
| --- | --- |
| Run id |  |
| Symptom |  |
| Failed layer | Environment / sizing / server / route / client / prompt / tokenizer / performance / quality / RAG / security |
| Evidence |  |
| Ruled-out layers |  |
| One change made |  |
| Result after change | Pass / Hold / Fail |
| Benchmark row updated |  |
| Quality row updated |  |
| Next action |  |

## Completion Gate

This decision tree is complete for a local run when you have:

- [ ] one diagnosed failure or explicit "no failure observed" row
- [ ] the failed layer named without changing multiple variables at once
- [ ] evidence copied from the preflight, server logs, client harness, benchmark, or quality harness
- [ ] one controlled fix or next test
- [ ] benchmark and quality records updated if the failure affects performance or model choice
- [ ] security runbook checked if the failure involves bind address, logs, RAG data, tools, or exposure

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local RAG Assistant Lab]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/2022 — Alignment and Chat/Quantization]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching]]
