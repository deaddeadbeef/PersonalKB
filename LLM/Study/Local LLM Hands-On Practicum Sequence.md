---
tags: [study, llm, inference, local-llm, practicum, hosting, capstone]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [practice]
---

# Local LLM Hands-On Practicum Sequence

> **One-line summary** This is the ordered practice path for turning local LLM knowledge into proof: first endpoint, reproducible request, controlled runtime, measured quality, RAG/tool extension, and maintained service.

Use this after [[LLM/Study/LLM Mastery Roadmap|LLM Mastery Roadmap]] gives the full learning map and before filling [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]. The individual labs are reference notes. This note is the sequence to execute.

The goal is not to read every local-inference note in one sitting. The goal is to leave behind a chain of evidence that proves you can host a local model, call it through an API, explain its behavior, and decide whether it is good enough for a workload.

## Practicum Rule

Every exercise must leave one artifact:

- a card
- a command output
- a raw response
- a benchmark row
- a quality row
- a decision row
- a troubleshooting row

If there is no artifact, it was only a reading session. Reading helps, but it does not prove local inference competence.

## Prerequisites

Before starting the applied sequence, make sure you can explain:

| Skill | Route |
|---|---|
| Tokens, logits, probabilities, loss, attention, KV cache | [[LLM/Study/LLM Math and Tensor Shape Primer]] |
| How one request flows through prompt assembly, prefill, decode, sampling, and stopping | [[LLM/Study/LLM Inference Request Lifecycle Lab]] |
| Why metrics prove different claims | [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]] |
| Which local layer owns a failure | [[LLM/Study/Local LLM Runtime Stack Anatomy]] |

You do not need full paper mastery before the first local run. You do need enough theory to explain what the evidence means.

## Sequence Overview

| Stage | Exercise | Main proof |
|---|---|---|
| 0 | Machine and boundary preflight | Readiness and preflight snapshot |
| 1 | First loopback endpoint | Raw local response |
| 2 | Model custody and compatibility | Provenance and compatibility cards |
| 3 | Repeatable client call | First client runner row, then client harness row |
| 4 | Request controls | Sampler, context, and template rows |
| 5 | Benchmark and first quality | Benchmark plus first quality or quality-harness decision |
| 6 | Runtime comparison | Decision card with rejected alternative |
| 7 | Service hardening | Observability, security, lifecycle rows |
| 8 | RAG extension | Retrieval, citation, refusal, and failure artifacts |
| 9 | Tool or structured-output extension | Schema, validation, policy, execution, and quality rows |
| 10 | Capstone handoff | Capstone project blueprint and one evidence ledger with gaps named |

Stop after any stage if the evidence fails. Use the failed row to choose the next controlled change.

## Stage 0: Preflight The Machine

Route:

- [[LLM/Study/Local LLM First Run Readiness Snapshot]]
- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Runtime Stack Anatomy]]

Save:

| Artifact | Minimum fields |
|---|---|
| Readiness snapshot | Runtime install state, GPU, listener ports, first runtime choice, first model class, next proof action |
| Preflight snapshot | OS, shell, CPU/RAM, GPU/VRAM or CPU-only note, disk, model cache path, intended host/port |
| Stack Anatomy Card | Boundary, hardware proof, lowest unproven layer, next action |

Pass signal: you know whether the run is Windows native, WSL, Docker, remote Linux, or desktop GUI, and you know which hardware that boundary can actually see.

Do not download models before this. Otherwise you cannot tell whether a later failure belongs to hardware, runtime boundary, cache path, or model choice.

## Stage 1: First Loopback Endpoint

Route:

- [[LLM/Study/Local LLM Windows First-Run Quickstart]]
- [[LLM/Study/Local LLM First Model Pull Gate]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM Command Cookbook]]
- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Serving Runbook]]

Default path:

1. Use Ollama or LM Studio for the first Windows-native proof.
2. Keep binding on loopback.
3. Use [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]] to pull exactly one small instruct model and save list/tags/show metadata.
4. Send one deterministic smoke prompt.
5. Save the raw response before judging quality.
6. Use [[LLM/Study/Local LLM First Quality Probe Suite|Local LLM First Quality Probe Suite]] before treating smoke output as quality evidence.

Use [[LLM/Study/Local LLM Command Cookbook|Local LLM Command Cookbook]] when this stage needs copyable commands for the run folder, listener check, Ollama native route, OpenAI-compatible route, Python client, or teardown proof.

Use [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]] when the stage needs one fill-in folder with the install/open path, model pull, native response, OpenAI-compatible response, benchmark row, and decision row.

Save:

| Artifact | Minimum fields |
|---|---|
| First inference evidence pack | Runtime, model id, base URL, route, request body, response text, timing, safe binding |
| Endpoint smoke row | Native route or OpenAI-compatible route, status, raw response, error if any |
| First decision | keep / tune / stronger model / different runtime / stop |

Pass signal: another person could reproduce which model served which request through which endpoint.

## Stage 2: Prove Model Custody And Compatibility

Route:

- [[LLM/Study/Local LLM Workload to Model Selection Playbook]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]

Save:

| Artifact | Minimum fields |
|---|---|
| Candidate card | Workload, candidate slot, model class, source, license, artifact options, runtime candidates, rejection trigger |
| Provenance card | Model card, license/gated access, intended use, revision/tag/file, unsafe-file decision |
| Artifact card | Cache/local path, file list, hash or verification, import or conversion command |
| Sizing row | Weight memory, KV-cache risk, runtime overhead, context target, headroom |
| Compatibility card | Artifact format, quantization, tokenizer, chat template, runtime, model id, route, workload |

Pass signal: you can explain why this exact artifact should load in this exact runtime for this exact workload.

## Stage 3: Make The Client Call Reproducible

Route:

- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/Local LLM First Streaming Timing Runner]]
- [[LLM/Study/Local LLM Client Harness Lab]]

Save:

| Artifact | Minimum fields |
|---|---|
| API contract card | Base URL, route, model id, non-streaming response, streaming decision, error shape, unsupported fields |
| Client harness row | Config, request settings, status, latency, raw excerpt, parsed output, error class |
| Streaming timing row | First event, TTFT, chunk counts, final output, total latency, usage gap, and stream error if any |

Pass signal: the same script can rerun the same request without relying on UI memory or manual clicking.

## Stage 4: Freeze Request Controls

Route:

- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]

Save:

| Artifact | Minimum fields |
|---|---|
| Template/tokenizer row | Tokenizer source, chat template source, stop/EOS policy, prompt token count |
| Sampler row | Temperature, top-p/top-k/min-p if used, penalties, seed behavior, stop strings, output cap |
| Context budget row | Runtime context limit, rendered prompt tokens, history/RAG/tool overhead, output reserve, safety margin |
| Request lifecycle row | TTFT, decode tokens/sec or equivalent, prompt tokens, output tokens, stop reason |

Pass signal: benchmark or quality changes can be attributed to the model/runtime, not hidden prompt, sampler, template, or context drift.

## Stage 5: Benchmark And Judge Quality

Route:

- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM First Benchmark Row Builder]]
- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/Study/Local LLM First Quality Probe Suite]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]

Save:

| Artifact | Minimum fields |
|---|---|
| First benchmark-row builder output | Benchmark JSON, Markdown copy row, missing-layer list, and next controlled action |
| Benchmark row | Model, runtime, quantization, hardware, context, TTFT, tokens/sec, memory, prompt class |
| Metric card | Claim, metric family, workload, what the metric proves, what it misses |
| Quality row | Prompt id, rubric scores, pass/hold/fail, failure owner, next action |

Pass signal: you can say whether the endpoint is acceptable for one workload, not just whether it responds.

## Stage 6: Compare Or Tune One Runtime Layer

Route:

- [[LLM/Study/Local LLM Quantization and GPU Offload Lab]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab]]
- [[LLM/Study/Local LLM Speculative Decoding Lab]]

Choose one change:

| Change | Do not change at the same time |
|---|---|
| Quantization/offload | Prompt suite, sampler, model family |
| Runtime | Model artifact, prompt suite, context target |
| Concurrency | Model, prompt suite, sampler, output cap |
| Prompt cache | Shared prefix, route, model, sampler |
| Speculative decoding | Main model, prompt, sampler, output cap |

Save:

| Artifact | Minimum fields |
|---|---|
| Decision card | Baseline, changed layer, measured result, quality result, rejected alternative, keep/disable/hold |

Pass signal: the change has a measured reason to keep it, reverse it, or test the next layer.

## Stage 7: Harden The Service Boundary

Route:

- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]]
- [[LLM/Study/LLM Deployment Decision Matrix]]

Save:

| Artifact | Minimum fields |
|---|---|
| Observability row | Loaded model, route, request timing, logs/metrics, resource pressure, error evidence, next controlled action |
| Security row | Bind address, auth, logs, RAG data class, tool boundary, exposure decision |
| Lifecycle card | Startup mode, pinned runtime/model state, cache/data paths, backup, upgrade plan, rollback target |
| Deployment memo | Workload, accepted path, rejected alternative, owner, next review trigger |

Pass signal: the endpoint can be reused without guessing how it starts, what it exposes, where data goes, or how to roll back.

## Stage 8: Add RAG Only After The Base Endpoint Is Proven

Route:

- [[LLM/Study/Local Embedding and Reranker Hosting Lab]]
- [[LLM/Study/Local RAG Assistant Lab]]
- [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab]]
- [[LLM/Study/Local RAG Minimal Python Harness]]

Save:

| Artifact | Minimum fields |
|---|---|
| Corpus manifest | Source boundary, document ids, chunk policy, data class |
| Embedding/reranker card | Model id, route, vector dimension, normalization, batching, privacy |
| Retrieval evaluation row | Query id, expected source, top-k, first relevant rank, rerank/hybrid decision |
| Generation row | Context ids, answer, citations, unsupported-question refusal |
| RAG failure row | Retrieval miss / low rank / context assembly / generation / citation / refusal |

Pass signal: you can tell whether a bad answer is a retrieval problem, context assembly problem, generation problem, or citation/evaluation problem.

## Stage 9: Add Tools Or Structured Output

Route:

- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]

Save:

| Artifact | Minimum fields |
|---|---|
| Tool schema | Allowed tool, argument schema, privilege boundary |
| Validation row | Raw model output, parsed args, validation result |
| Policy row | Allow/deny decision outside the model |
| Execution row | Tool result, injected result, final answer, bounded retry/stop rule |
| Tool quality row | Correct tool, correct args, safe decision, supported final answer |

Pass signal: the model proposes actions, but the application controls authorization, execution, and audit evidence.

## Stage 10: Capstone Handoff

Route:

- [[LLM/Study/Local LLM Capstone Project Blueprint]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mastery Self-Assessment Exam]]

Save one capstone note or folder that links:

| Proof area | Required link |
|---|---|
| First endpoint | Evidence pack and raw response |
| Runtime stack | Stack Anatomy Card |
| Model custody | Provenance and artifact cards |
| Compatibility | Runtime/model compatibility card |
| API | Contract card, first client runner row, and client harness row |
| Request controls | Template, sampler, context, request lifecycle rows |
| Measurement | Benchmark, metric, and quality rows |
| Service | Observability, security, lifecycle, deployment rows |
| Extension | RAG or tool artifact set |
| Exam | Self-assessment score and missed-question remediation |

Pass signal: the capstone workbook has proof links, not just status text.

## If You Get Stuck

| Situation | Next route |
|---|---|
| Endpoint will not start | [[LLM/Study/Local LLM Troubleshooting Decision Tree]] |
| GPU is invisible | [[LLM/Study/Local LLM Environment Preflight Lab]] or [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab]] |
| Docker path is confusing | [[LLM/Study/Local LLM Docker GPU Container Serving Lab]] |
| Route or model id fails | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]] |
| Output ignores instructions | [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]] |
| Benchmark is unstable | [[LLM/Study/Decoding and Sampling Controls Lab]] |
| First smoke output has no quality signal | [[LLM/Study/Local LLM First Quality Probe Suite]] |
| Quality is bad but speed is fine | [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| RAG answer is unsupported | [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab]] |
| Tool call is unsafe or malformed | [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]] |

## Completion Gate

This practicum sequence is complete when you have:

- [ ] one local endpoint proof
- [ ] one model custody and compatibility proof
- [ ] one reusable client harness row
- [ ] one controlled sampler/template/context row
- [ ] one benchmark row
- [ ] one first quality probe row or quality row
- [ ] one diagnosed failure or explicit no-failure row
- [ ] one service security or lifecycle row if the endpoint will be reused
- [ ] one RAG or tool extension artifact if the goal is more than chat
- [ ] one capstone handoff note shaped by [[LLM/Study/Local LLM Capstone Project Blueprint|Local LLM Capstone Project Blueprint]] with links to the evidence

## References

Internal routes:

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/LLM Mastery Roadmap]]
- [[LLM/Study/Local LLM Capstone Project Blueprint]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mastery Self-Assessment Exam]]
- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Runtime Stack Anatomy]]
- [[LLM/Study/Local LLM Windows First-Run Quickstart]]
- [[LLM/Study/Local LLM First Model Pull Gate]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM First Quality Probe Suite]]
- [[LLM/Study/Local LLM Workload to Model Selection Playbook]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/Local LLM First Streaming Timing Runner]]
- [[LLM/Study/Local LLM First Benchmark Row Builder]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM First Benchmark Row Builder]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]]
- [[LLM/Study/Local RAG Assistant Lab]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
