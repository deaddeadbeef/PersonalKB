---
tags: [study, llm, inference, local-llm, model-selection, evaluation, deployment]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [core, practice]
---

# Local LLM Workload to Model Selection Playbook

> **One-line summary** Choose a local LLM by workload contract, evidence, and hardware fit: define the job, pick the smallest plausible candidate, prove compatibility, run a quality gate, and keep only measured winners.

Use this before [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]], [[LLM/Study/Local LLM Hardware Sizing Runner|Local LLM Hardware Sizing Runner]], [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]], and [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]]. Those notes prove memory, custody, and compatibility. This note decides which candidates are worth proving. Use [[LLM/Study/Local LLM Model Selection Runner|Local LLM Model Selection Runner]] when the candidate card should become repeatable JSON, Markdown, CSV, and JSONL shortlist evidence.

Use it during [[LLM/Study/Local LLM Hands-On Practicum Sequence|Local LLM Hands-On Practicum Sequence]] Stage 2, before spending time downloading, converting, or benchmarking a model. Use [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] after the endpoint works to decide whether the candidate actually passes.

## Selection Rule

There is no universal best local model.

The right first local model is:

1. small enough to load with memory headroom
2. instruction-tuned enough for the task interface
3. compatible with the intended runtime and artifact format
4. allowed by its license and data boundary
5. good enough on the workload-specific quality gate
6. fast enough for the latency or batch target
7. operationally simple enough to maintain

Leaderboards, parameter count, and social consensus are weak evidence. A model that is great for chat can fail JSON. A model that is strong for coding can fail citation discipline. A model that is excellent in FP16 can fail after aggressive quantization.

The selection question is:

> What is the smallest local candidate that passes this workload's quality, latency, memory, privacy, and operations gates?

## Workload Contract First

Fill this before choosing a model name.

| Field | Decision |
|---|---|
| Workload name |  |
| User-visible task | chat / coding / summarization / extraction / RAG / tool loop / batch processing / research |
| Data boundary | public / personal / private / regulated / offline-only |
| Required output shape | prose / JSON / table / code / citations / tool calls / embeddings |
| Context shape | short prompt / long document / multi-turn / RAG chunks / tool results |
| Latency target | interactive / patient interactive / batch / overnight |
| Quality gate | known-answer / schema / code tests / citation audit / human rubric / pairwise comparison |
| Failure cost | annoyance / rework / data leak / wrong action / unsafe automation |
| Maintenance target | one-off experiment / personal endpoint / shared service / capstone proof |

If this table is vague, the model choice will be vague.

## Workload Families

| Workload | What the model must do | Candidate priority | Failure to test early |
|---|---|---|---|
| Private chat | follow instructions, stay useful, stay local | simple instruct/chat model that fits easily | verbose but wrong answers, weak refusal boundary |
| Coding helper | reason about code, obey format, write tests | code-tuned or strong general instruct model | plausible broken code, missed constraints, context loss |
| Summarization/extraction | preserve facts and output structure | model with strong instruction following and low hallucination | invented details, invalid table/JSON, missed fields |
| RAG assistant | use provided context and cite support | model with faithful grounding; separate embedding/reranker choice | parametric-memory override, fake citations |
| Tool loop | choose action, produce valid args, use result | model/runtime with reliable structured output or tool-call support | unsafe action, invalid args, retry loop |
| Long-context reading | use relevant span under token pressure | model/runtime with context and KV-cache headroom | ignores distant evidence, slow prefill, truncation |
| Batch document work | process many items predictably | smaller model with stable throughput and simple failure recovery | slow total throughput, silent bad rows |
| Serving experiment | learn runtime behavior | model family available across two runtimes/formats | changing model and runtime at the same time |

This is the practical form of the HELM lesson: model selection is multi-objective. Accuracy alone does not decide robustness, calibration, safety, latency, memory, or workload fit.

## Candidate Ladder

Start with candidate slots, not model hype.

| Slot | Purpose | What it proves |
|---|---|---|
| Baseline small candidate | Prove the endpoint and workflow cheaply | The serving path works and the workload is measurable |
| Practical local candidate | Best expected balance for the real hardware | The task can be done locally with acceptable latency and quality |
| Stretch local candidate | Higher quality or longer context at higher cost | Whether more memory/latency buys enough quality |
| Specialized candidate | Code, RAG, tool, math, multilingual, or embedding-specific | Whether task specialization beats a general chat model |
| External reference | Hosted model, prior answer, or human answer | The local model is compared against a useful standard |

Do not start with the stretch candidate. If it fails, you will not know whether the cause is model quality, memory, quantization, runtime, template, or route. Start with a small baseline, prove the path, then scale or specialize.

For the current Windows RTX 3080 Ti first run, use [[LLM/Study/Local LLM First Model Candidate Ladder|Local LLM First Model Candidate Ladder]] to pick the source-checked baseline, control, stretch, and avoid-first candidate classes before pulling a model.

## First Candidate Decision Flow

```text
Define workload
  -> choose required output shape
  -> set context and latency target
  -> estimate hardware band
  -> pick smallest plausible instruct/chat candidate
  -> record source, license, artifact, and runtime fit
  -> serve on loopback
  -> run benchmark and quality harness
  -> keep, tune, scale, specialize, or reject
```

The first model is not the final answer. It is the control condition.

## Candidate Card

Copy this into the run note before download.

| Field | Value |
|---|---|
| Candidate id |  |
| Candidate slot | baseline / practical / stretch / specialized / reference |
| Workload |  |
| Required output shape |  |
| Context target |  |
| Latency target |  |
| Data boundary |  |
| Model family |  |
| Model class | base / instruct / chat / code / reasoning / embedding / reranker |
| Source registry or local path |  |
| Current model-card date checked |  |
| License and use boundary |  |
| Artifact options | Ollama tag / GGUF / HF safetensors / GPTQ / AWQ / FP8 / adapter |
| Runtime candidates | Ollama / LM Studio / llama.cpp / vLLM / SGLang / other |
| Expected quantization |  |
| Expected weight memory |  |
| Expected KV-cache risk | low / medium / high |
| Hardware sizing runner output |  |
| Chat template or tokenizer risk | low / medium / high / unknown |
| Tool/JSON/citation risk | low / medium / high / not needed |
| Why this is the smallest plausible candidate |  |
| Why not smaller |  |
| Why not larger yet |  |
| Rejection trigger | quality / latency / memory / license / compatibility / maintenance |

The "current model-card date checked" field matters because model cards, license terms, quantized derivatives, and runtime support change. The vault should store the decision evidence, not pretend a model name is timeless.

## Scenario Playbooks

### Windows Private Assistant

Start here when the goal is a personal local chat endpoint.

| Decision | Default stance |
|---|---|
| Candidate slot | baseline small candidate |
| Runtime | Ollama or LM Studio |
| Artifact | runtime tag or GGUF |
| Context | short-to-medium |
| Quality gate | known-answer, instruction following, concise answer |
| Stop condition | endpoint works, quality is acceptable, loopback boundary is clear |

Do not optimize server throughput before the first endpoint works. Use [[LLM/Study/Local LLM Windows First-Run Quickstart|Local LLM Windows First-Run Quickstart]] and [[LLM/Study/Local LLM First Inference Evidence Pack|Local LLM First Inference Evidence Pack]].

### Coding Helper

Coding helpers fail differently from general chat.

| Test early | Pass signal |
|---|---|
| Edit a small function | patch is syntactically valid and minimal |
| Explain an error | names the failing layer and next check |
| Write a test | test targets the behavior, not only a happy path |
| Follow repository constraints | does not invent tools or ignore existing style |

If the model produces plausible but unverified code, it has not passed. Pair the quality row with real command output from the target repo when possible.

### Vault or Document RAG

RAG selection has two model choices: the generator and the retrieval stack.

| Component | Selection question |
|---|---|
| Embedding model | Does it retrieve the expected source in top-k? |
| Reranker | Does it improve first relevant rank enough to justify latency? |
| Generator | Does it answer only from supplied context and cite support? |
| Context budget | Do retrieved chunks fit without hiding the answer? |

Use [[LLM/Study/Local Embedding and Reranker Hosting Lab|Local Embedding and Reranker Hosting Lab]] and [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab|Local RAG Retrieval Evaluation and Reranking Lab]] before calling the generator bad.

### Structured Output or Tool Loop

For structured local work, model selection is not only language quality.

| Required proof | Why |
|---|---|
| Valid JSON or schema output | malformed output breaks automation |
| Tool-call argument validation | model output is untrusted input |
| External policy check | the model must not grant itself permission |
| Bounded retries | local loops can hang or repeat bad calls |
| Result-grounded final answer | tool use matters only if the result is used correctly |

Prefer the candidate that is reliably valid and safe over the candidate that sounds smarter but breaks the contract.

### Batch Document Processing

Batch work can accept slower per-token speed if the run is predictable.

| Decision | Default stance |
|---|---|
| Candidate | smaller stable model before larger fragile one |
| Runtime | simple CLI/server path with recoverable failures |
| Prompt | deterministic extraction or summary template |
| Quality gate | sampled human review plus schema checks |
| Benchmark | total documents/hour, error count, retry count |

CPU inference can be acceptable here when privacy/offline control matters more than interactive latency.

### GPU Serving Candidate

For vLLM, SGLang, or containerized serving, selection includes runtime economics.

| Proof | Route |
|---|---|
| GPU visibility and driver boundary | [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab]] or [[LLM/Study/Local LLM Docker GPU Container Serving Lab]] |
| Artifact/runtime support | [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]] |
| Scheduler behavior | [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]] |
| Concurrency and saturation | [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]] |
| Lifecycle and rollback | [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]] |

Do not treat a single smoke response as a serving decision. A GPU server candidate needs queueing, cache, security, and lifecycle evidence.

## Selection Evidence Ladder

| Gate | Evidence |
|---|---|
| Workload gate | Workload contract and required output shape |
| Candidate gate | Candidate card with model class, source, license, artifact, runtime, and rejection trigger |
| Sizing gate | Weight memory, KV-cache risk, runtime overhead, and headroom |
| Custody gate | Model card, license, exact revision/tag/file, local path, and safe-file decision |
| Compatibility gate | Artifact, tokenizer, template, quantization, runtime, route, and workload contract |
| Endpoint gate | Loopback smoke response and served model id |
| Control gate | Sampler, context, template, and output cap fixed |
| Benchmark gate | TTFT, tokens/sec, memory, context, and prompt class |
| Quality gate | Prompt-suite score and pass/hold/fail decision |
| Operations gate | Security, observability, lifecycle, and rollback if reused |

Skip gates only when the run is explicitly exploratory. Do not convert exploratory results into a deployment decision later without filling the missing evidence.

## Pass, Hold, Fail

| Decision | Use when | Next action |
|---|---|---|
| Pass | Candidate meets quality, latency, memory, compatibility, and data-boundary gates | Keep it for this workload and record the review trigger |
| Hold | One bottleneck is fixable with a controlled change | Tune exactly one layer: prompt, sampler, context, quantization, runtime, or model size |
| Fail | Required quality, route, license, safety, latency, or memory condition is not met | Reject the candidate and record the failure owner |

Record why the rejected candidate failed. Rejected alternatives are part of a defensible model decision.

## Academic Anchors

| Academic idea | Practical consequence |
|---|---|
| HELM-style multi-metric evaluation | Do not choose by one benchmark or one leaderboard score |
| Chinchilla and inference economics | Smaller well-trained models can be better local choices than larger barely-fit models |
| Quantization | Compression must be tested on the workload, not assumed harmless |
| KV cache and prefill/decode split | Context and concurrency can break a model that fits by weight size alone |
| Instruction tuning | A base model can be capable but poor at following the desired interface |
| RAG evaluation | Bad answers can be retrieval, reranking, context, citation, or generation failures |
| Tool-use research | The application must validate and govern actions outside the model |

Use [[LLM/Study/LLM Mechanism-to-Inference Bridge Map|LLM Mechanism-to-Inference Bridge Map]] to turn these ideas into local controls and proof artifacts.

## Common Mistakes

| Mistake | Why it fails |
|---|---|
| Starting from the largest model that might load | It hides whether failures are memory, template, runtime, or quality issues |
| Choosing from a leaderboard only | The benchmark may not match the workload, hardware, quantization, or safety boundary |
| Ignoring license and artifact custody | A model that works technically may still be wrong for the use case |
| Treating "OpenAI-compatible" as identical behavior | Local runtimes differ in streaming, tools, errors, templates, and unsupported fields |
| Evaluating after changing prompt, sampler, model, and runtime at once | No causal conclusion is possible |
| Accepting fast output without rubric scoring | Fast wrong output is a fail |
| Accepting a smoke test as model selection | A smoke test proves route reachability, not workload quality |

## Completion Gate

This playbook is complete for one candidate decision when you have:

- [ ] workload contract
- [ ] candidate card
- [ ] model selection runner output if there is more than one candidate or if the decision must be repeated later
- [ ] sizing estimate
- [ ] acquisition/provenance evidence
- [ ] runtime/model compatibility evidence
- [ ] endpoint smoke response
- [ ] sampler/template/context controls
- [ ] benchmark row
- [ ] quality harness row
- [ ] pass/hold/fail decision
- [ ] rejected alternative or explicit reason comparison was skipped
- [ ] review trigger for a new model, runtime, hardware, workload, license, or data boundary

## References

Internal routes:

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Hands-On Practicum Sequence]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Hardware Sizing Runner]]
- [[LLM/Study/Local LLM Model Selection Runner]]
- [[LLM/Study/Local LLM First Model Candidate Ladder]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab]]
- [[LLM/Study/Local LLM Docker GPU Container Serving Lab]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]]
- [[LLM/Study/Local Embedding and Reranker Hosting Lab]]
- [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/2023 — Open Models and Agents/LLM-as-Judge]]
- [[LLM/2018–2019 — Pretrained Language Models/Knowledge and Reasoning Benchmarks]]
- [[LLM/2020–2021 — The Scaling Era/Scaling Laws]]
- [[LLM/2022 — Alignment and Chat/Quantization]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes]]
