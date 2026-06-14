---
tags: [study, llm, inference, local-llm, benchmark]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [practice]
---

# Local LLM Inference Benchmark Log

> **One-line summary** A local LLM run only proves competence when the model, runtime, hardware, prompts, latency, memory, and quality notes are recorded well enough to reproduce the result.

Use this note with [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]]. The lab explains how to run local models; this note captures the evidence that the run worked and what trade-offs it exposed.

For endpoint setup and smoke tests, use [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] before filling in the measurements here.

## When To Use This

Use the log whenever you:

- load a new model or quantization
- compare runtimes such as Ollama, LM Studio, llama.cpp, vLLM, or SGLang
- change context length, GPU offload, batching, sampling settings, or prompt format
- decide whether a local model is good enough for a real workload
- need proof for the Level 5 gate in [[LLM/Study/LLM Mastery Roadmap|LLM Mastery Roadmap]]

The goal is not to find a universal best model. The goal is to make a workload-specific decision from reproducible evidence.

## Run Metadata

Create one row per run.

| Field | Record |
| --- | --- |
| Date/time | Local date and time of the run |
| Objective | What decision this run should inform |
| Model id | Repository/model name or local filename |
| Model family | Llama, Qwen, Mistral, Gemma, DeepSeek, Phi, etc. |
| Parameter size | 1.5B, 3B, 7B, 8B, 14B, etc. |
| Runtime | Ollama, LM Studio, llama.cpp, vLLM, SGLang, Open WebUI frontend, or other |
| API base URL | Local endpoint, if served over HTTP |
| Quantization/format | FP16, BF16, INT8, AWQ, GPTQ, GGUF quant, or unknown |
| Hardware | CPU, GPU, RAM, VRAM, storage notes |
| OS/environment | Windows, WSL, Linux, macOS, Docker, driver/CUDA notes |
| Context setting | Max context and prompt token count if known |
| Sampling settings | Temperature, top-p, top-k, max output tokens |
| Prompt class | Chat, coding, summarization, extraction, RAG, long-context, agent/tool |
| Concurrency | Single request, batch size, concurrent users, or request rate |
| Source commit/config | Script, command, config file, or runtime settings used |

## Measurements

| Metric | How to read it |
| --- | --- |
| Load time | Time from starting runtime/model load to ready state |
| Time to first token (TTFT) | User-visible wait before generation begins |
| Total latency | Wall-clock request time from submit to final token |
| Decode speed | Output tokens per second after the first token |
| Time per output token (TPOT) | Inverse of decode speed; useful when comparing systems papers |
| Prompt tokens | Tokens consumed by prompt, retrieved context, or system prefix |
| Output tokens | Tokens generated in the response |
| Peak RAM | Highest observed system memory use during the run |
| Peak VRAM | Highest observed GPU memory use during the run |
| CPU/GPU utilization | Whether the bottleneck looks compute-bound, memory-bound, or idle |
| Error/retry count | Runtime crashes, OOMs, malformed outputs, timeouts, or refusal surprises |
| Quality score | Short rubric result, not just "felt good" |

Keep the same prompt, sampling settings, and output-token cap when comparing two runtimes or quantizations. Change one variable at a time unless the experiment is explicitly a full-stack comparison.

## Prompt Suite

Run at least three prompts. Use more when choosing a model for real work.

| Prompt type | What it tests | Pass signal |
| --- | --- | --- |
| Known-fact sanity check | Basic factuality on a topic you can verify | Correct answer without invented specifics |
| Coding or structured output | Instruction following and formatting | Valid code/JSON/table matching the requested schema |
| Long-context stress test | KV-cache pressure and context assembly | Uses the relevant context without losing the task |
| RAG/document-grounded query | Retrieval plus citation discipline | Cites provided evidence and refuses unsupported claims |
| Summarization/extraction | Compression and detail retention | Preserves key facts and omits irrelevant material |
| Constraint-following safety check | Boundary handling without harmful detail | Follows the allowed constraint and avoids unsafe assistance |

## Decision Rubric

| Result | Use when |
| --- | --- |
| Pass | Quality is sufficient, latency is acceptable, memory headroom remains, and the run is reproducible |
| Hold | Quality is promising but one bottleneck needs another run, such as context size, quantization, or prompt design |
| Fail | The model cannot load, misses the core task, violates the output contract, or is too slow for the workload |

Write the acceptance threshold before benchmarking. A chat assistant, RAG analyst, coding helper, batch summarizer, and production API all have different latency and quality requirements.

## Blank Log Entry

Copy this block into a dated run note or append it below a project-specific experiment note.

| Field | Value |
| --- | --- |
| Date/time |  |
| Objective |  |
| Model id |  |
| Runtime/API |  |
| Quantization/format |  |
| Hardware |  |
| Context/prompt tokens |  |
| Output-token cap |  |
| Prompt class |  |
| Load time |  |
| TTFT |  |
| Total latency |  |
| Decode tokens/sec |  |
| Peak RAM/VRAM |  |
| Quality score |  |
| Decision | Pass / Hold / Fail |
| Notes |  |

## Troubleshooting Links

- If memory is the blocker, review [[LLM/2022 — Alignment and Chat/Quantization|Quantization]] and [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse|KV Cache and Context Reuse]].
- If single-user latency is the blocker, review [[LLM/2024–2025 — Frontier and Efficiency/Speculative Decoding|Speculative Decoding]] and the TTFT/TPOT split above.
- If multi-user throughput is the blocker, review [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching|Batching and Continuous Batching]].
- If runtime choice is unclear, review [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs|Serving Architectures and Throughput-Latency Trade-offs]].
- If quality is unclear, review [[LLM/2023 — Open Models and Agents/LLM-as-Judge|LLM-as-Judge]] and [[LLM/2022 — Alignment and Chat/Human Evaluation and Preference Studies|Human Evaluation and Preference Studies]].

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/LLM Mastery Roadmap]]
- [[LLM/2022 — Alignment and Chat/Quantization]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2023 — Open Models and Agents/LLM-as-Judge]]
