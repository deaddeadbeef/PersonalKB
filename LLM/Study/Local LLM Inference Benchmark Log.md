---
tags: [study, llm, inference, local-llm, benchmark]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [practice]
---

# Local LLM Inference Benchmark Log

> **One-line summary** A local LLM run only proves competence when the model, runtime, hardware, prompts, latency, memory, and quality notes are recorded well enough to reproduce the result.

Use this note with [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]]. The lab explains how to run local models; this note captures the evidence that the run worked and what trade-offs it exposed.

Use [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]] to choose the candidate model, quantization, and context target before running the benchmark.

Use [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]] to capture the OS, runtime boundary, hardware visibility, disk/model cache, and host/port plan before recording performance numbers.

For endpoint setup and smoke tests, use [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] before filling in the measurements here.

Use [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]] when a benchmark row fails or looks contradictory. The decision tree should identify whether the issue belongs to environment, sizing, server, route, client, prompt, performance, quality, RAG, or security before another comparison run.

Use [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] when a smoke test needs to become repeatable evidence. The client harness should produce the request settings, latency, streaming, error, and response-excerpt fields that feed this log.

Use [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]] before comparing quality across runs where temperature, top-p, top-k, min-p, penalties, seed, stop strings, or structured-output settings might change the answer.

Use [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]] before long-context, RAG, tool, or multi-turn runs. The benchmark row should show the runtime context limit, prompt tokens, output reserve, template overhead, and any truncation policy tested.

Use [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]] when the workload depends on function calling, structured output, or agent loops. Tool-call latency, validation, policy, and execution results should be recorded separately from model generation.

For a formal quality score, use [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] to run workload prompts, rubric scores, pairwise comparisons, RAG/citation checks, and a pass/hold/fail gate.

Use [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]] after the benchmark and quality rows exist. The matrix turns measurements into a choice between local CPU, local GPU, self-hosted server, hosted API, hybrid, or batch inference.

For document-grounded workloads, use [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]] and [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]] to record corpus version, chunk policy, embedding/index configuration, retrieval results, citation support, unsupported-question refusal, and RAG-specific failure modes.

## When To Use This

Use the log whenever you:

- load a new model or quantization
- compare runtimes such as Ollama, LM Studio, llama.cpp, vLLM, or SGLang
- change context length, GPU offload, batching, sampling settings, or prompt format
- decide whether a local model is good enough for a real workload
- choose a deployment path from measured quality, latency, memory, privacy, cost, and operations evidence
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
| Acquisition/provenance | Source URL, model card, license, revision/tag/digest, and local cache path from [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Model Acquisition and Provenance Checklist]] |
| Runtime | Ollama, LM Studio, llama.cpp, vLLM, SGLang, Open WebUI frontend, or other |
| API base URL | Local endpoint, if served over HTTP |
| Quantization/format | FP16, BF16, INT8, AWQ, GPTQ, GGUF quant, or unknown |
| Hardware | CPU, GPU, RAM, VRAM, storage notes |
| OS/environment | Windows, WSL, Linux, macOS, Docker, driver/CUDA notes |
| Context setting | Max context and prompt token count if known |
| Context budget | Runtime limit, reserved output, template overhead, RAG/tool/history tokens, safety margin |
| Tool contract | Tool schema version, tool-choice mode, parser/backend, policy boundary, if tools are used |
| Sampling settings | Temperature, top-p, top-k, min-p, seed, penalties, stop strings, and max output tokens |
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
| Context-budget margin | Remaining tokens after prompt, reserved output, and safety margin |
| Peak RAM | Highest observed system memory use during the run |
| Peak VRAM | Highest observed GPU memory use during the run |
| CPU/GPU utilization | Whether the bottleneck looks compute-bound, memory-bound, or idle |
| Error/retry count | Runtime crashes, OOMs, malformed outputs, timeouts, or refusal surprises |
| Tool-call evidence | Tool-call count, argument validation, policy decision, execution latency, and result status |
| Quality score | Harness result from [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]], not just "felt good" |

Keep the same prompt, sampling settings, and output-token cap when comparing two runtimes or quantizations. Change one variable at a time unless the experiment is explicitly a full-stack comparison.

## Client Harness Rows

The benchmark row is easier to trust when it comes from a stable client harness instead of manual console notes.

| Harness field | Benchmark use |
| --- | --- |
| Run id | Tie raw request evidence to benchmark and quality rows. |
| Base URL and route | Confirm the client hit the intended endpoint. |
| Model id and runtime | Prevent comparisons against the wrong served model. |
| Prompt id and prompt class | Keep workload evidence comparable. |
| Sampling settings | Explain determinism, randomness, and format drift. |
| Status and error class | Count failures without hiding them. |
| TTFT and total latency | Separate perceived responsiveness from total wall-clock time. |
| Prompt and output tokens | Normalize prefill and decode measurements. |
| Response excerpt or output path | Give enough evidence for review without leaking private data. |

Use [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] to define the row schema before running a model comparison.

## Prompt Suite

Run at least three prompts. Use more when choosing a model for real work.

Use [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] when the prompt suite needs a scored acceptance decision rather than a quick benchmark note.

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

For model selection, make this decision from both the measurements above and the scored prompt rows in [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]]. For deployment selection, feed the accepted benchmark rows into [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]].

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
| Context budget margin |  |
| Tool-call evidence |  |
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
- If prompt length, RAG packing, history, or tool schemas are the blocker, run [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]] before changing models.
- If tool selection, argument validity, policy, or result injection is the blocker, run [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]] before calling the model bad.
- If multi-user throughput is the blocker, review [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching|Batching and Continuous Batching]].
- If runtime choice is unclear, review [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs|Serving Architectures and Throughput-Latency Trade-offs]].
- If quality is unclear, run [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]], then review [[LLM/2023 — Open Models and Agents/LLM-as-Judge|LLM-as-Judge]] and [[LLM/2022 — Alignment and Chat/Human Evaluation and Preference Studies|Human Evaluation and Preference Studies]].
- If the prompt depends on private documents, use [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]] and [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]] to separate retrieval failures from generation failures.

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/Study/Local RAG Assistant Lab]]
- [[LLM/Study/Local RAG Minimal Python Harness]]
- [[LLM/Study/LLM Mastery Roadmap]]
- [[LLM/2022 — Alignment and Chat/Quantization]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2023 — Open Models and Agents/LLM-as-Judge]]
