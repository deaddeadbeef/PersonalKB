---
tags: [study, llm, inference, local-llm, quantization, hardware, benchmark]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [core, practice, deep-dive]
last-verified: 2026-06-15
---

# Local LLM Quantization and GPU Offload Lab

> **One-line summary** Quantization and GPU offload are not just "make it fit" settings: choose a numeric format, prove the artifact/runtime path, sweep offload and KV-cache precision, then accept only the setup that passes both speed and quality gates.

Use this after [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]], [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]], and [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]]. Those notes answer what artifact you have, whether it can fit, and which runtime can load it. This lab answers which quantization/offload setting should actually be kept.

Pair it with [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] for latency and memory rows, [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] for quality rows, [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]] for loaded-model state and resource evidence, and [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]] for the final keep/change decision. Use [[LLM/Study/Local LLM Quantization and GPU Offload Evidence Runner|Local LLM Quantization and GPU Offload Evidence Runner]] after the lab rows exist so the baseline, support proof, memory, offload, KV-cache, benchmark, quality, rejected alternative, and decision card become repeatable pass/hold/fail evidence.

Use [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]] before judging long-context results. Weight quantization can make the model fit while the KV cache still fails at the target context or concurrency. Use [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Local LLM Prompt Cache and KV Reuse Lab]] and [[LLM/Study/Local LLM Speculative Decoding Lab|Local LLM Speculative Decoding Lab]] only after the quantization/offload baseline is stable.

## What This Lab Decides

This lab decides one practical question:

> For this workload, hardware, runtime, context target, and quality bar, which quantization and GPU-offload setting should I run?

It does not decide a universal best quant. A Q4 GGUF can be the right Windows laptop choice. An AWQ/GPTQ checkpoint can be the right GPU-serving choice. A smaller BF16 model can beat a larger INT4 model when the workload is exact formatting, math, coding, tool JSON, or rare-domain retrieval.

## Mechanism Model

Quantization changes the numeric representation used to store or compute model state.

| Object | What is compressed | Why it helps | Main risk |
| --- | --- | --- | --- |
| Weights | Model parameters | Lower memory footprint and less memory bandwidth per token | Quality loss, runtime/kernel mismatch, dequant overhead |
| Activations | Intermediate tensors during computation | Can improve GPU throughput on supported kernels | Hardware support and calibration sensitivity |
| KV cache | Attention keys and values for prior tokens | Lower long-context and concurrency memory | Context-sensitive quality loss |
| Runtime buffers | Engine-specific workspaces, graphs, queues, cache pages | May improve scheduling or kernels | Hidden memory overhead |

The academic connection is [[LLM/2022 — Alignment and Chat/Quantization|Quantization]]: lower precision saves memory and bandwidth, but error distribution matters. GPTQ, AWQ, SmoothQuant, LLM.int8(), GGUF K-quants, FP8, and INT8/INT4 server formats are different answers to "where can precision be removed without breaking the task?"

## Choice Map

Start with the runtime and artifact, not with a bit-width slogan.

| Situation | First candidate | Why | Do not skip |
| --- | --- | --- | --- |
| Windows desktop first proof | Ollama or LM Studio with a small GGUF/Ollama tag | Low friction and local API proof | `ollama ps` or LM Studio load evidence showing CPU/GPU split |
| Explicit GGUF file, CPU or mixed CPU/GPU | llama.cpp, Ollama, or LM Studio | GGUF is native to the llama.cpp ecosystem | Quant name, context, GPU offload, template evidence |
| GPU serving with Hugging Face-style checkpoint | vLLM or SGLang | Better fit for batching, CUDA kernels, and server quantization | Supported quantization/hardware table and exact launch command |
| Pre-quantized AWQ/GPTQ checkpoint | vLLM or SGLang, then benchmark | These are not interchangeable with GGUF | Runtime support, hardware support, calibration/source quality |
| Long-context workload | Least aggressive weight quant that fits plus KV-cache test | KV memory can dominate after weights fit | Context budget and KV-cache precision row |
| Exact JSON/tool/coding workload | Higher-precision baseline or less aggressive quant | Small numeric damage can show up as format/correctness loss | Quality harness before accepting speed |

## Lab 0 - Freeze The Baseline

Before changing quantization or offload, freeze the comparison surface.

| Field | Record |
| --- | --- |
| Workload | Chat, coding, summarization, extraction, RAG, tool use, batch, or agent loop |
| Acceptance gate | Required quality dimensions and latency/memory target |
| Hardware | CPU, RAM, GPU model, VRAM, driver/CUDA/ROCm/Metal/Vulkan/WSL boundary |
| Runtime | Ollama, LM Studio, llama.cpp, vLLM, SGLang, Transformers, or other |
| Artifact | HF repo/path, GGUF file, Ollama tag, AWQ/GPTQ checkpoint, FP8/INT8 checkpoint |
| Model family and size | Llama/Qwen/Mistral/Gemma/DeepSeek/Phi/etc.; parameter class |
| Context target | Prompt tokens, output reserve, context length, active sequences |
| Prompt suite | Smoke, real workload, structured output, long-context/RAG if relevant |
| Sampler | Temperature, top-p/top-k/min-p, penalties, seed support, stops, output cap |
| Baseline | Highest precision or least aggressive quant that can reasonably run |

If the baseline cannot run, write why: no VRAM, no RAM, unsupported architecture, missing tokenizer, license gate, or runtime path not available. A failed baseline is still evidence.

## Lab 1 - Estimate Memory Before Loading

Use the sizing guide first:

```text
required memory =
  weight memory
  + KV-cache memory
  + runtime overhead
  + OS / UI / driver headroom
```

Planning weight memory:

```text
weight memory ~= parameter count x bytes per parameter
```

| Format | Planning bytes per parameter | Typical local interpretation |
| --- | ---: | --- |
| FP16 / BF16 | 2.0 | Clean baseline when VRAM allows |
| INT8 / Q8 | 1.0 | Lower quality risk, still substantial memory |
| INT4 / Q4 / AWQ / GPTQ | 0.5 | Common local feasibility target |
| Lower than 4-bit | < 0.5 | Treat as high-risk until the workload passes |

Do not stop at file size. Runtime allocations, tensor scales, KV cache, CUDA graphs, prompt-cache pages, speculative buffers, and UI overhead can push a "fits on paper" model into OOM.

## Lab 2 - Pick Candidate Quantizations

Use at least two candidates when possible:

| Candidate | Purpose |
| --- | --- |
| Baseline | FP16/BF16, Q8, or the least compressed artifact you can run |
| Practical | The quantization that should fit comfortably |
| Aggressive | The smallest or fastest plausible artifact |
| Alternative model | Smaller higher-precision model, used to test whether bigger quantized is actually better |

Keep the model family, instruct tuning, chat template, prompt suite, sampler, and output cap fixed. If you compare `Qwen 7B Q4` to `Mistral 7B Q4`, you are comparing model families, not only quantization.

## Lab 3 - Prove Runtime Compatibility

Fill this before benchmarking:

| Layer | Evidence |
| --- | --- |
| Artifact container | GGUF, HF/Safetensors, Ollama tag, AWQ, GPTQ, FP8, INT8, adapter |
| Quantization | Filename, model card, GGUF metadata, runtime load log, or config |
| Tokenizer/template | GGUF metadata, tokenizer files, model card, rendered prompt, or runtime template setting |
| Hardware path | CPU, CUDA, ROCm, Metal, Vulkan, WSL, Docker, remote GPU |
| Offload control | GPU layers, GPU percentage, processor split, tensor parallelism, or "runtime automatic" |
| KV-cache precision | Default and tested cache type when runtime exposes it |
| Endpoint | Native route or OpenAI-compatible route |
| Failure owner | Artifact / quantization / tokenizer / template / runtime / route / memory / quality |

Compatibility is pass/fail before quality is interpreted. A quantized model that answers with role markers may be a template failure, not a quantization failure.

## Lab 4 - GPU Offload Sweep

Run a small sweep that changes only offload.

| Sweep row | What to try | Evidence |
| --- | --- | --- |
| CPU-only or no offload | Disable GPU use or set GPU layers to 0 when supported | Load log, RAM, TTFT, tokens/sec |
| Partial offload | Fit safely under VRAM with headroom | CPU/GPU split, RAM/VRAM, tokens/sec |
| Max safe offload | Push as much weight to GPU as possible without paging/OOM | Peak VRAM, stability, output speed |
| Dedicated-memory mode | If the runtime exposes it, avoid slow shared GPU memory | Dedicated vs shared memory notes |

Interpretation:

| Observation | Likely meaning | Next action |
| --- | --- | --- |
| More offload improves tokens/sec | Decode was memory/compute limited on CPU | Keep the fastest setting with headroom |
| More offload hurts or stalls | VRAM pressure, shared memory, PCIe transfer, weak GPU path, or wrong backend | Back off and record peak memory |
| CPU-only has better quality than GPU-offloaded run | Usually sampler/template drift, not offload itself | Verify same request and runtime path |
| Max offload loads but long prompts fail | Weights fit but KV cache/context does not | Run KV-cache/context sweep |

## Lab 5 - KV-Cache Precision And Context Stress

Only run this after a weight/offload setting is stable.

| Row | Test | Pass signal |
| --- | --- | --- |
| Default KV cache | Runtime default precision and context target | No OOM, acceptable quality |
| Lower KV precision | q8/fp8/int8 or runtime-supported lower precision | Memory drops without visible quality loss |
| Aggressive KV precision | q4 or equivalent if supported | Only keep if long-context quality passes |
| Context ladder | Short, target, and stress prompt lengths | TTFT and memory scale as expected |
| Concurrency ladder | 1, 2, 4 requests if workload needs it | No hidden OOM or queue collapse |

KV-cache quantization is not the same as weight quantization. A model can have Q4 weights and F16 cache, or higher precision weights with quantized cache. Record both.

## Lab 6 - Quality Regression Harness

For each quant/offload candidate, run the same quality prompts:

| Prompt id | What it catches |
| --- | --- |
| SMOKE-01 | Endpoint and template shape |
| JSON-01 | Exact structured output |
| CODE-01 | Syntax and small correctness |
| MATH-01 | Arithmetic or symbolic precision |
| FACT-01 | Verifiable facts and calibration |
| RAG-01 | Evidence use and citation discipline |
| LONG-01 | Long-context recall and instruction retention |
| WORK-01 | The real task you care about |

Mark the first quantization that fails. If Q4 fails but Q5/Q6 passes, keep the least compressed artifact that fits the latency and memory target. If a smaller higher-precision model beats the larger quantized model on the workload, use the smaller model.

## Runtime-Specific Evidence

### Ollama

Record:

- `ollama show --modelfile <model>`
- `ollama ps` after load, especially the `PROCESSOR` split
- context setting such as `num_ctx` or `OLLAMA_CONTEXT_LENGTH`
- `OLLAMA_FLASH_ATTENTION` and `OLLAMA_KV_CACHE_TYPE` if tested
- native timing fields from API responses when available

Ollama's FAQ documents `ollama ps` as the way to see whether a model is on CPU, GPU, or split, and documents KV-cache type as a server option when Flash Attention is enabled.

### LM Studio

Record:

- model file or Hub id and selected quantization
- loaded model id from `/v1/models`
- per-model settings: context length, GPU offload, Flash Attention, and any JIT/on-demand loading behavior
- GPU controls if a multi-GPU or dedicated-memory setting is used
- first-request load time separately from warm request latency

LM Studio's own release notes describe per-model settings for context length and GPU offload, plus GPU controls that can disable devices, choose allocation strategy, and limit model weights to dedicated GPU memory.

### llama.cpp

Record:

- binary version or commit and build backend such as CUDA, Vulkan, Metal, or CPU
- `--list-devices` output when device selection matters
- exact `llama-cli` or `llama-server` command
- GGUF filename and quantization
- `--n-gpu-layers` / `-ngl`, `--device`, context length, thread settings, and server port
- load log showing model buffers, compute buffers, KV cache, and GPU layers

The llama.cpp build docs show backend-specific builds such as CUDA and note that GPU acceleration can be disabled with `--device none`; Metal builds can explicitly set `--n-gpu-layers 0`.

### vLLM

Record:

- model path/repo, quantization method, tensor parallel size, dtype, and served model id
- supported hardware row for the chosen quantization
- whether GGUF is being used through the current plugin path and tokenizer workaround
- `/metrics` evidence for latency, running/waiting requests, and KV/cache metrics when enabled

vLLM's quantization docs list supported formats and hardware support. Its GGUF docs currently warn that GGUF support is experimental/under-optimized and requires the GGUF plugin path.

### SGLang

Record:

- `python -m sglang.launch_server` command
- `--model-path`, `--quantization`, host/port, tensor/data parallel settings if any
- offline pre-quantized path versus online quantization path
- backend/platform support row
- benchmark and quality rows after quantization

SGLang's quantization docs distinguish offline quantization from online dynamic quantization, recommend offline quantization for performance/usability, and explicitly warn that quantized models need post-quantization benchmark validation.

## Measurement Table

Create one row per candidate and prompt class.

| Run id | Runtime | Model/artifact | Quant | Offload | KV cache | Context | Prompt id | TTFT | Tok/s | Peak RAM | Peak VRAM | Quality | Decision |
| --- | --- | --- | --- | --- | --- | ---: | --- | ---: | ---: | --- | --- | --- | --- |
|  |  |  |  | CPU / partial / max | f16/q8/q4/etc. |  |  |  |  |  |  | pass/hold/fail | keep/tune/reject |

Add raw evidence paths or excerpts in the benchmark log. Do not trust a row that lacks the exact model artifact, quantization, offload setting, context, and prompt id.

## Decision Card

Copy this into a run note, benchmark log, or capstone row.

| Field | Value |
| --- | --- |
| Workload |  |
| Quality gate |  |
| Hardware |  |
| Runtime |  |
| Candidate artifacts |  |
| Baseline quantization |  |
| Accepted quantization |  |
| Rejected quantization(s) |  |
| GPU offload setting |  |
| KV-cache precision |  |
| Context target |  |
| Benchmark rows |  |
| Quality rows |  |
| Memory headroom |  |
| Failure owner, if any | weight memory / KV cache / runtime / template / quality / route |
| Decision | keep / less aggressive quant / stronger quant / smaller model / different runtime / more hardware |
| Review trigger | new model, new runtime version, new driver, new context target, new workload |

## Failure Triage

| Symptom | Likely owner | Controlled next check |
| --- | --- | --- |
| OOM at load | Weight memory, runtime buffers, or offload | Smaller quant, lower offload, lower context, inspect load log |
| OOM only on long prompt | KV cache | Lower context, lower active sequences, test KV-cache precision |
| `unsupported quantization` | Runtime/artifact mismatch | Check runtime quantization docs and artifact metadata |
| `model not found` | Served id or route | List models through native route or `/v1/models` |
| Slow first token | Prefill, cold load, context, queue | Short vs long prompt, cold vs warm, prompt-cache lab if repeated prefixes matter |
| Slow later tokens | Decode memory bandwidth, offload, weak kernel, model size | Offload sweep, quant sweep, hardware utilization |
| Fast but worse answers | Quantization, template, sampler, or model-task fit | Higher-precision A/B plus quality harness |
| Quality fails only on JSON/tool output | Format control and post-training sensitivity | Decoding controls and structured-output lab |
| Works in GUI but not client | API contract | OpenAI-compatible API contract lab |

## Completion Gate

This lab is complete when:

- [ ] model artifact, quantization, tokenizer/template, runtime, context, and hardware path are recorded
- [ ] baseline memory estimate and actual load memory are compared
- [ ] at least two quantization candidates are tested or a blocker explains why not
- [ ] GPU offload has a CPU/partial/max-safe row when the runtime exposes offload
- [ ] KV-cache precision/context row exists when long context or concurrency matters
- [ ] benchmark rows include TTFT, tokens/sec or TPOT, prompt/output tokens, RAM/VRAM, and error class
- [ ] quality rows compare the same prompt suite across candidates
- [ ] one candidate is accepted or rejected with a named reason
- [ ] [[LLM/Study/Local LLM Quantization and GPU Offload Evidence Runner|Local LLM Quantization and GPU Offload Evidence Runner]] passes or routes every missing quantization/offload proof to the correct remediation note
- [ ] the decision is routed into [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]]

## References

Internal routes:

- [[LLM/Sources/Sources Index]]
- [[LLM/2022 — Alignment and Chat/Quantization]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Evidence Runner]]
- [[LLM/Study/LLM Deployment Decision Matrix]]

Academic references:

- [GPTQ](https://arxiv.org/abs/2210.17323)
- [AWQ](https://arxiv.org/abs/2306.00978)
- [SmoothQuant](https://arxiv.org/abs/2211.10438)
- [LLM.int8()](https://arxiv.org/abs/2208.07339)

Current external docs checked 2026-06-15:

- [Hugging Face Hub GGUF](https://huggingface.co/docs/hub/en/gguf)
- [Hugging Face Transformers GGUF](https://huggingface.co/docs/transformers/en/gguf)
- [Ollama FAQ](https://docs.ollama.com/faq)
- [Ollama Modelfile reference](https://docs.ollama.com/modelfile)
- [llama.cpp build docs](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md)
- [vLLM quantization](https://docs.vllm.ai/en/latest/features/quantization/)
- [vLLM GGUF](https://docs.vllm.ai/en/latest/features/quantization/gguf/)
- [SGLang quantization](https://sgl-project.github.io/advanced_features/quantization.html)
- [LM Studio 0.3.5 release notes](https://lmstudio.ai/blog/lmstudio-v0.3.5)
- [LM Studio 0.3.14 GPU controls](https://lmstudio.ai/blog/lmstudio-v0.3.14)
