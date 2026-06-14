---
tags: [study, llm, deployment, local-llm, decision, operations]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [practice]
---

# LLM Deployment Decision Matrix

> **One-line summary** The right deployment path is the one whose quality, latency, privacy, cost, reliability, and operational burden fit the workload after measurement.

Use this after [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]], [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]], [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]], [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook|Local LLM Service Lifecycle and Upgrade Runbook]], [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]], [[LLM/Study/Local LLM Runtime Comparison Lab|Local LLM Runtime Comparison Lab]], and [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]]. Use [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab|Local LLM Concurrency and Batch Throughput Lab]] first if the deployment depends on multiple users, local queues, batch/offline processing, or throughput targets. Use [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]] first if the deployment depends on function calling, structured output, or agent tools. Those notes collect evidence. This note turns the evidence into a deployment choice.

The question is not "local or cloud?" in the abstract. The question is which path satisfies the workload while preserving the data boundary, quality bar, latency target, cost model, and operational owner.

## Outcome

After filling this out, you should be able to:

- choose between local CPU, local GPU workstation, self-hosted GPU server, hosted API, hybrid local-RAG/cloud-model, or batch/offline inference
- explain why the choice follows from workload, data sensitivity, quality, latency, throughput, context, cost, privacy, and operations evidence
- reject at least one plausible alternative with evidence rather than preference
- link the decision back to benchmark, quality, security, troubleshooting, and capstone artifacts

## Decision Inputs

| Input | Question to answer | Evidence source |
|---|---|---|
| Workload | Chat, coding, summarization, extraction, RAG, agent, batch processing, or product API? | Project brief or capstone note |
| Data sensitivity | Public, personal, private, regulated, secret, or mixed? | [[LLM/Study/Local LLM Security and Privacy Runbook|Security and Privacy Runbook]] |
| Interactivity | Human-facing realtime, asynchronous, scheduled, or offline? | Product/workflow requirement |
| Quality threshold | What score counts as pass, hold, or fail? | [[LLM/Study/Local LLM Quality Evaluation Harness|Quality Evaluation Harness]] |
| Context length | How much prompt, retrieved context, chat history, or tool state is needed? | Benchmark row and RAG proof |
| Concurrency | One user, a few local clients, team traffic, batch queue, or public API? | [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab|Concurrency and Batch Throughput Lab]] |
| Uptime | Toy experiment, daily personal tool, team dependency, or production service? | Operational plan |
| Offline need | Must it work without internet or external provider access? | Security/privacy requirement |
| Customization | Prompt-only, RAG, LoRA, fine-tune, tool use, or policy wrapper? | [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide|Adaptation and Fine-Tuning Decision Guide]] |
| Runtime compatibility | Does the selected artifact, quantization, tokenizer, chat template, runtime, route, and workload contract fit together? | [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Runtime and Model Compatibility Matrix]] |
| Runtime comparison | Has the selected runtime beaten at least one plausible alternative under fixed prompts, sampler settings, context, output cap, benchmark rows, and quality rows? | [[LLM/Study/Local LLM Runtime Comparison Lab|Runtime Comparison Lab]] |
| Operations evidence | Do logs, runtime metrics, queue/KV/cache state, CPU/RAM, GPU/VRAM, and error rows explain the operating point? | [[LLM/Study/Local LLM Observability and Operations Runbook|Observability and Operations Runbook]] |
| Lifecycle evidence | Are startup mode, pinned versions, model/cache paths, backups, upgrade plan, rollback target, and post-change validation known? | [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook|Service Lifecycle and Upgrade Runbook]] |
| Cost model | Hardware sunk cost, electricity, rented GPU, API tokens, engineer time, or support burden? | Cost estimate |
| Operational owner | Who patches, monitors, restarts, backs up, and handles incidents? | Runbook owner |
| Audit/compliance | Are logs, prompts, documents, outputs, and model access auditable? | Security runbook and log map |
| Failure tolerance | Is a slow answer annoying, expensive, unsafe, or user-visible? | Workload risk assessment |

## Deployment Options

| Option | Best fit | Watch for |
|---|---|---|
| Local CPU or edge | Private, offline, low-volume, batch, or small-model tasks where speed is secondary | Slow decode, limited quality, long-context pressure, thermal limits |
| Local GPU workstation | Private interactive work for one person or a small trusted group | VRAM, uptime, driver/runtime drift, heat, power, manual maintenance |
| Self-hosted GPU server | Shared private service, internal API, or production-like local deployment with an ops owner | Authentication, batching, monitoring, scaling, upgrades, incident response |
| Hosted API | Highest quality, fastest time to ship, broad model choice, elastic traffic, low infrastructure burden | Data residency, prompt retention, token cost, rate limits, vendor dependency |
| Hybrid local RAG plus hosted model | Local corpus control or local retrieval with external reasoning quality | Data boundary between retrieved context and provider, prompt logging, citation leakage |
| Batch/offline pipeline | Summaries, extraction, classification, or evaluations where latency is not user-facing | Throughput, checkpointing, retry behavior, cost per document, partial failure handling |

## Academic Mechanism To Deployment Consequence

| Mechanism | Deployment consequence |
|---|---|
| Quantization | Can make a model fit local memory, but quality must be scored after compression. |
| KV cache and context length | Long prompts and concurrent sessions raise memory cost even when weights fit. |
| Prefill vs decode | Long context mostly hurts time to first token; large models and memory bandwidth hurt per-token decode. |
| Batching and continuous batching | Shared servers can improve throughput, but single-user local workflows may not benefit. |
| Speculative decoding | Can reduce latency when the runtime supports it, but it is an implementation feature, not a deployment strategy by itself. |
| RAG and context assembly | Local retrieval can keep corpus control local, but citations, logs, and prompt injection become part of the boundary. |
| Alignment and evaluation | A deployment is acceptable only if the workload-specific quality and safety gates pass. |
| Tool use and agents | Tool execution moves risk into sandboxing, approval policy, and audit logs, not only model choice. |
| Serving architecture | Runtime, queueing, routing, monitoring, and failover determine whether the path is an experiment or a service. |

## Decision Matrix

| Axis | Local CPU/edge | Local GPU workstation | Self-hosted server | Hosted API | Hybrid |
|---|---|---|---|---|---|
| Data privacy | Strong local control if logs stay local | Strong local control with more service surfaces | Strong if access control and logs are correct | Depends on provider terms and data handling | Mixed; corpus can stay local but prompts may leave |
| Offline use | Strong | Strong | Strong inside local network | Weak | Partial |
| Quality ceiling | Usually lower for small/quantized models | Medium to high, bounded by VRAM | Medium to high, bounded by budget | Often highest and fastest moving | High if hosted model supplies reasoning |
| Latency | Often slow | Good for one or few users | Good when tuned and batched | Good but network/provider dependent | Depends on retrieval and external call |
| Throughput | Low | Low to medium | Medium to high | Elastic until rate limits | Mixed |
| Long context | Limited by memory and speed | Limited by VRAM/KV cache | Tunable but expensive | Model/API dependent | Retrieval can reduce required context if designed well |
| Cost predictability | Hardware already owned, slow time cost | Hardware/electricity/upkeep | Hardware/rental/ops cost | Token bills and rate limits | Both local ops and API tokens |
| Scaling | Poor | Limited | Possible with ops work | Easiest | Depends on split |
| Maintenance | Low infrastructure, high patience | Driver/runtime/model upkeep | Highest ops burden | Lowest infrastructure burden | Both local data stack and provider integration |
| Observability | Manual unless instrumented | Manual unless instrumented | Must be explicit | Provider plus app logs | Need both retrieval and model traces |
| Security/compliance | Small surface if offline | Endpoint and UI surface | Full service surface | Provider and app boundary | Boundary must prove what crosses providers |
| Tool/RAG fit | Good for private toy workflows | Good for private assistants | Good for shared internal assistants | Good for tool APIs, less for private corpus | Often best when corpus is private and reasoning quality matters |

## Evidence Gate

Do not choose a deployment path until these rows exist or are explicitly marked not applicable:

| Evidence | Required proof |
|---|---|
| Preflight | Machine, runtime boundary, disk, model cache, host, and port are recorded. |
| Benchmark | Model, runtime, quantization, context, TTFT, tokens/sec, memory, and prompt class are recorded. |
| Runtime compatibility | Artifact format, tokenizer, template, quantization, API route, and model id are recorded. |
| Runtime comparison | At least two plausible runtimes have controlled benchmark and quality rows, or one alternative is explicitly not applicable. |
| Concurrency/backpressure | Multi-request, queue, p95 latency, saturation, and overload behavior are measured when the workload is not strictly single-user. |
| Observability | Loaded-model state, route, request timings, logs or metrics, resource pressure, errors, and next controlled action are recorded. |
| Lifecycle/rollback | Startup mode, pinned runtime/model state, cache/data paths, backup location, upgrade procedure, rollback target, and post-change validation are recorded when the path is maintained beyond a one-off run. |
| Quality | Workload prompts have pass, hold, or fail decisions from a rubric. |
| Security boundary | Endpoint exposure, logs, RAG corpus, tools, and storage locations are known. |
| Tool loop, if relevant | Tool schema, parser/backend, validation, policy decision, execution result, loop bounds, and failure rows are recorded. |
| Troubleshooting | At least one failure row or explicit no-failure row names the layer and evidence. |
| RAG, if relevant | Corpus version, chunk policy, top-k/rank retrieval evaluation, reranking/hybrid decision, citations, refusal behavior, benchmark/quality rows, and failure modes are recorded through [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab|Local RAG Retrieval Evaluation and Reranking Lab]] and [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]]. |
| Adaptation, if relevant | Prompt, RAG, SFT, LoRA/QLoRA, DPO, distillation, continued pretraining, or no-train choice is justified from failure-mode evidence. |
| Cost/ops estimate | Hardware, API, maintenance, and owner assumptions are written down. |
| Rejected alternative | At least one plausible path is rejected with measured or policy evidence. |

## Recommendation Rules

| Choose this | When |
|---|---|
| Local CPU or edge | Privacy/offline control matters more than speed, the model passes the quality gate, and the workload is low-volume or batch. |
| Local GPU workstation | Interactive private use passes quality and latency gates, and the user accepts hardware/runtime maintenance. |
| Self-hosted server | Multiple users or workloads need privacy/control, and an owner exists for auth, monitoring, batching, updates, and incidents. |
| Hosted API | Quality, time to ship, reliability, or elasticity matter more than data residency and local control. |
| Hybrid | Local corpus, retrieval, guardrails, or auditing matter, but local model quality or latency fails. |
| Batch/offline | User-facing latency is unimportant, retry/checkpoint behavior matters, and cost per document can be measured. |

## Decision Memo Template

Copy this into [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]] or a project note.

| Field | Value |
|---|---|
| Workload |  |
| Data sensitivity |  |
| Candidate paths | local CPU / local GPU / self-hosted server / hosted API / hybrid / batch |
| Selected path |  |
| Evidence links | preflight / benchmark / observability / quality / security / RAG / troubleshooting |
| Quality result |  |
| Latency and throughput |  |
| Context and KV-cache risk |  |
| Privacy and security boundary |  |
| Cost model |  |
| Operational owner |  |
| Failure modes |  |
| Rejected alternatives |  |
| Next review trigger | new model, new workload, new data class, traffic change, cost change, or security change |

## Completion Gate

A deployment decision is complete when:

- one path is selected for one named workload
- the selected path has benchmark and quality evidence
- privacy, logging, RAG, and tool boundaries are explicit
- cost and operational owner are named
- startup, upgrade, backup, and rollback responsibilities are explicit for maintained services
- at least one plausible alternative is rejected with evidence
- the next review trigger is written down

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/LLM Mastery Roadmap]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mastery Self-Assessment Exam]]
- [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide]]
- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]]
- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local RAG Assistant Lab]]
- [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab]]
- [[LLM/Study/Local RAG Minimal Python Harness]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/2022 — Alignment and Chat/Quantization]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching]]
- [[LLM/2024–2025 — Frontier and Efficiency/Speculative Decoding]]
- [[LLM/2023 — Open Models and Agents/LLM-as-Judge]]
- [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes]]
