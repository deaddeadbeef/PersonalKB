---
tags: [study, llm, inference, local-llm, hardware, quantization]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [practice]
---

# Local LLM Model and Hardware Sizing Guide

> **One-line summary** Model choice is a memory, latency, quality, and workload decision: estimate weights, add KV-cache headroom, choose a runtime, then prove the result with benchmarks.

Use this before [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]]. The runbook proves the endpoint; this guide helps decide what model and quantization are worth trying on the hardware you actually have. Use [[LLM/Study/Local LLM Workload to Model Selection Playbook|Local LLM Workload to Model Selection Playbook]] before this guide when the workload, candidate slot, model class, or rejection trigger is still unclear. Use [[LLM/Study/Local LLM Model Metadata Card Runner|Local LLM Model Metadata Card Runner]] when architecture, tokenizer, context, or quantization facts still need to be extracted from saved model metadata. Use [[LLM/Study/Local LLM KV Cache Sizing Runner|Local LLM KV Cache Sizing Runner]] when model architecture, context length, active sequences, or cache precision need a head-aware MHA/MQA/GQA cache estimate before hardware sizing. Use [[LLM/Study/Local LLM Hardware Sizing Runner|Local LLM Hardware Sizing Runner]] when the weight, KV-cache, overhead, context, active-sequence, and headroom estimate should become repeatable pass/hold/fail evidence. Use [[LLM/Study/Local LLM Model Selection Runner|Local LLM Model Selection Runner]] when the sizing estimate should become a ranked candidate shortlist. Use [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]] to record what the current machine, runtime boundary, disk, and port can actually support. Use [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]] before downloading to record model card, license, revision, artifact safety, and local path. Use [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]] when disk headroom, cache location, exact downloaded files, GGUF import, or conversion output may decide whether the sizing plan is reproducible. Use [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]] when the context target must be turned into prompt, history, RAG, tool, output, and safety-margin tokens. Use [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab|Local LLM Concurrency and Batch Throughput Lab]] when active sequences, queueing, or batch/offline throughput may determine the hardware fit. Use [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]] when the sizing answer still leaves open whether the file format, quantization, tokenizer, chat template, and runtime are compatible. Use [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Local LLM Quantization and GPU Offload Lab]] when the candidate fits only under quantization/offload assumptions and needs a measured choice between GGUF, AWQ, GPTQ, FP8/INT8, KV-cache precision, CPU fallback, and GPU offload.

Use [[LLM/Study/Local LLM Speculative Decoding Lab|Local LLM Speculative Decoding Lab]] before reserving memory for a draft model, EAGLE/MTP path, or n-gram speculative method. A main model that fits alone may fail once speculation adds draft weights, draft cache, verification buffers, or CUDA graph overhead.

Use [[LLM/Study/Local LLM First Model Candidate Ladder|Local LLM First Model Candidate Ladder]] when the sizing question is specifically the first RTX 3080 Ti/Ollama route proof. That note pins the baseline, control, stretch, and avoid-first model classes before the first pull.

## The Core Question

Do not start with "what is the biggest model I can run?" Start with:

1. What task must the model perform?
2. How much context does the task require?
3. Does the workload need interactive latency or batch throughput?
4. What memory budget is available after the OS, browser, Obsidian, and other apps?
5. What quality loss is acceptable from quantization?
6. Which runtime supports the model format and hardware path?

The right local model is the smallest model that passes the workload's quality bar with acceptable latency and memory headroom.

## Memory Budget Formula

Use this planning equation:

```text
required memory =
  model weight memory
  + KV-cache memory
  + runtime overhead
  + OS / UI / driver headroom
```

The first two terms are the academic core:

- **Weight memory** is mostly controlled by parameter count and numeric format. See [[LLM/2022 — Alignment and Chat/Quantization|Quantization]].
- **KV-cache memory** grows with layers, context length, hidden size, precision, and active sequences. See [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse|KV Cache and Context Reuse]].

Use [[LLM/Study/LLM Math and Tensor Shape Primer|LLM Math and Tensor Shape Primer]] if the parameter, tensor-shape, or KV-cache arithmetic needs a grounding pass before filling the sizing worksheet.

## Weight Memory Estimate

Approximate weight memory:

```text
weight memory ~= parameter count x bytes per parameter
```

| Format | Planning bytes per parameter | Meaning |
| --- | ---: | --- |
| FP16 / BF16 | 2.0 | Full half-precision inference weights |
| INT8 | 1.0 | Usually low quality loss, runtime support varies |
| INT4 / 4-bit GGUF / GPTQ / AWQ | 0.5 | Common local-inference compression target |

Examples before runtime overhead:

| Model size | FP16/BF16 weights | INT8 weights | INT4 weights |
| --- | ---: | ---: | ---: |
| 3B | ~6 GB | ~3 GB | ~1.5 GB |
| 7B | ~14 GB | ~7 GB | ~3.5 GB |
| 13B | ~26 GB | ~13 GB | ~6.5 GB |
| 34B | ~68 GB | ~34 GB | ~17 GB |
| 70B | ~140 GB | ~70 GB | ~35 GB |

These are planning numbers, not a guarantee that the model will load. Real files include metadata, scale factors, alignment, runtime allocations, and sometimes non-weight buffers.

## KV-Cache Estimate

The simplified KV-cache formula from [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse|KV Cache and Context Reuse]] is:

```text
KV cache ~= 2 x layers x sequence length x hidden size x bytes per element x active sequences
```

Practical implications:

- Doubling context length roughly doubles KV-cache memory.
- Doubling active sequences or concurrency roughly doubles KV-cache memory.
- Quantizing weights does not automatically remove KV-cache pressure.
- MQA/GQA models reduce KV-cache size by sharing key/value heads.
- Prefix caching helps repeated system prompts, but only when prefixes are actually shared.

For a 7B-style model with 32 layers, hidden size 4096, FP16 cache, and one 2048-token sequence, the vault's KV-cache note estimates roughly 1 GB of KV-cache memory. Longer context or more active requests can make cache memory dominate the run.

For modern GQA/MQA models, prefer the head-aware estimate in [[LLM/Study/Local LLM KV Cache Sizing Runner|Local LLM KV Cache Sizing Runner]]:

```text
head_dim = hidden_size / num_attention_heads
KV cache ~= layers x context tokens x active sequences x 2 x num_key_value_heads x head_dim x bytes per element
```

That distinction matters because weight quantization and GQA/MQA are different levers. A 4-bit model can still fail at long context if the KV cache is FP16 and the active sequence count is too high; a GQA model can use less cache than an MHA model with the same hidden size because it stores fewer key/value heads.

## Hardware Planning Bands

Treat these as starting hypotheses to benchmark, not promises.

| Available hardware | Sensible first experiment | Avoid first |
| --- | --- | --- |
| CPU-only laptop with enough RAM | Small GGUF model in llama.cpp/Ollama; low context; batch/offline tasks | Large models, high context, interactive coding assistant expectations |
| 8 GB VRAM GPU | 3B-8B model with 4-bit quantization; short-to-medium prompts | 13B+ without strong quantization and tight context |
| 12-16 GB VRAM GPU | 7B-13B quantized model; maybe stronger 8B/14B class depending on runtime | Long-context concurrency without measuring KV cache |
| 24 GB VRAM GPU | 13B-34B quantized experiments or high-quality 7B-14B serving with headroom | Assuming 70B-class models will be comfortable |
| 48 GB+ VRAM / multi-GPU | Larger quantized models, vLLM/SGLang, concurrency experiments | Treating single-user laptop assumptions as production guidance |

If the model barely fits, it has not really fit. You still need headroom for prompt length, output length, the runtime, driver allocations, and other applications.

## Model Selection Loop

1. Pick the workload: chat, coding, summarization, extraction, RAG, agent loop, or batch document processing.
2. Set quality gates before testing: correctness, citation discipline, valid JSON, code passes tests, or human preference.
3. Choose a small baseline model first; for the current Windows/Ollama first run, use [[LLM/Study/Local LLM First Model Candidate Ladder|Local LLM First Model Candidate Ladder]].
4. Record acquisition provenance and license with [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]].
5. Run [[LLM/Study/Local LLM KV Cache Sizing Runner|Local LLM KV Cache Sizing Runner]] when GQA/MQA, long context, active sequences, or KV-cache precision could decide whether the candidate fits.
6. Run [[LLM/Study/Local LLM Hardware Sizing Runner|Local LLM Hardware Sizing Runner]] before pulling or serving if the model, context, active sequences, or headroom are not already proven.
7. Record the actual download/cache/import/conversion evidence with [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]].
8. Choose the least aggressive quantization that fits the memory budget.
9. Run the endpoint proof in [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]].
10. Log the run in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]].
11. If quality fails, scale model size or improve prompt/RAG before blaming hardware.
12. If latency fails, reduce model size, context, output length, or change runtime.
13. If memory fails, reduce model size, quantize more, reduce context/concurrency, or move to a different machine.

## Choosing Quantization

| Choice | Use when | Watch for |
| --- | --- | --- |
| FP16/BF16 | You have enough VRAM and need a clean quality baseline | High memory cost |
| INT8 | You need memory relief with lower quality risk | Runtime and kernel support |
| INT4 / 4-bit | You need local feasibility on consumer hardware | Quality loss, especially on hard reasoning or exact formatting |
| GGUF | You want llama.cpp/Ollama-style CPU or mixed CPU/GPU local deployment | File-specific performance and offload settings |
| GPTQ/AWQ | You want GPU-oriented quantized deployment | Runtime compatibility and calibration quality |

The key lesson from [[LLM/2022 — Alignment and Chat/Quantization|Quantization]] is that quantization is not just file compression. It changes the numerical representation and must be validated on the real task. Use [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Local LLM Quantization and GPU Offload Lab]] to turn this sizing estimate into a benchmarked decision: baseline quant, practical quant, aggressive quant, GPU-offload sweep, KV-cache precision test, and workload quality gate.

## Context And Concurrency Gate

Ask these before choosing a context setting. Then turn the answer into a concrete budget with [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]].

| Question | Why it matters |
| --- | --- |
| How many prompt tokens are typical? | Long prefill increases TTFT and KV cache |
| How many output tokens are needed? | Long decode makes tokens/sec matter more |
| Is this single-user or concurrent? | Active sequences multiply KV-cache memory |
| Are prompts repetitive? | Prefix caching may help repeated system prompts |
| Will speculative decoding be enabled? | Draft model/cache/buffers can consume the headroom needed for context or concurrency |
| Is this RAG? | Retrieved chunks can blow up prompt length |
| Does the task need exact citations or JSON? | Quality may fail before memory does |

If a setup works for a 500-token prompt, that does not prove it works for a 20K-token RAG prompt.

## Runtime Fit

| Runtime | Model/hardware fit |
| --- | --- |
| Ollama | First local test, simple model pulls, laptop/server experiments |
| LM Studio | Desktop exploration, GUI model loading, quick local API compatibility |
| llama.cpp / llama-cpp-python | GGUF, CPU, edge, mixed CPU/GPU, exact local-file control |
| vLLM | GPU serving, OpenAI-compatible API, batching and throughput experiments |
| SGLang | Structured generation, prefix-heavy workloads, production-style serving experiments |
| Open WebUI | Private chat interface after the provider endpoint works |

Runtime fit is part of the model decision. A model format that works in one runtime may be awkward or unsupported in another.

## Decision Record Template

Copy this into a run note before downloading or serving a model.

| Field | Decision |
| --- | --- |
| Workload |  |
| Quality gate |  |
| Latency target |  |
| Context target |  |
| Context budget source |  |
| Concurrent requests |  |
| Hardware budget |  |
| Candidate model |  |
| Candidate quantization |  |
| Expected weight memory |  |
| Expected KV-cache risk | Low / Medium / High |
| Runtime |  |
| Why this is the smallest plausible candidate |  |
| Compatibility evidence |  |
| Benchmark prompts |  |
| Pass / hold / fail rule |  |

## Red Flags

- Choosing a model only because it is the largest that might load.
- Ignoring context length when the workload is RAG or long-document analysis.
- Comparing runtimes with different prompts, quantization, or output-token limits.
- Treating fast generation as success when the answer is wrong.
- Treating a single short chat response as proof that a model can serve the target workload.
- Forgetting that CPU inference can be acceptable for batch jobs but painful for interactive chat.

## Proof Gate

To prove you understand local model sizing, produce:

1. A memory estimate for weights.
2. A KV-cache risk assessment for the target context and concurrency.
3. A runtime/format choice with a reason.
4. A head-aware KV-cache sizing output from [[LLM/Study/Local LLM KV Cache Sizing Runner|Local LLM KV Cache Sizing Runner]] when GQA/MQA, long context, active sequences, or cache dtype could decide fit.
5. A hardware sizing runner output from [[LLM/Study/Local LLM Hardware Sizing Runner|Local LLM Hardware Sizing Runner]] when the estimate must be reused in model selection, pull, or serving decisions.
6. A prompt/history/RAG/output budget from [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]] when the workload is not a tiny prompt.
7. A machine/runtime preflight from [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]].
8. A quantization/offload decision card from [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Local LLM Quantization and GPU Offload Lab]] when fit depends on compression or GPU placement.
9. A completed endpoint smoke test from [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]].
10. A completed benchmark row in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]].
11. A decision: keep, scale up, quantize more, reduce context, or change runtime.

## References

Internal evidence:

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Workload to Model Selection Playbook]]
- [[LLM/Study/Local LLM KV Cache Sizing Runner]]
- [[LLM/Study/Local LLM Model Metadata Card Runner]]
- [[LLM/Study/Local LLM Hardware Sizing Runner]]
- [[LLM/Study/Local LLM Model Selection Runner]]
- [[LLM/Study/Local LLM First Model Candidate Ladder]]
- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/LLM Math and Tensor Shape Primer]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Lab]]
- [[LLM/Study/Local LLM Speculative Decoding Lab]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/2022 — Alignment and Chat/Quantization]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching]]
- [[LLM/2023 — Open Models and Agents/Open-Weight Model Ecosystem]]

Supporting chunks:

- [[chunk-llm-208 GPTQ Standard for Open-Source Deployment]]
- [[chunk-llm-211 AWQ INT4 Edge Deployment Performance]]
- [[chunk-llm-214 KV Cache Memory Bandwidth Bottleneck]]
- [[chunk-llm-213 Multi-Query Attention Shared KV Heads]]
- [[chunk-llm-217 GQA Mechanism Interpolating MHA and MQA]]
- [[chunk-llm-260 Prompt caching reduces input token costs 50-90 percent by reusing KV cache for repeated prefixes]]
