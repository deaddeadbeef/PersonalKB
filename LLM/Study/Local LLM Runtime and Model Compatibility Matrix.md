---
tags: [study, llm, inference, local-llm, runtime, compatibility, quantization]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [core, practice]
last-verified: 2026-06-14
---

# Local LLM Runtime and Model Compatibility Matrix

> **One-line summary** A local LLM works only when the model architecture, file format, quantization, tokenizer, chat template, runtime, API route, and workload contract all match.

Use this after [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]] and before [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]], [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]], and [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]]. The provenance checklist answers "am I allowed and prepared to acquire this exact artifact?" This note answers "will this exact model artifact work in this exact runtime without hidden format or template mismatches?"

Pair it with [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] after the endpoint responds but before a generic client depends on the compatibility surface. Pair it with [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]] when the server responds but the model behaves unlike the advertised chat model.

When two compatibility cards are plausible, use [[LLM/Study/Local LLM Runtime Comparison Lab|Local LLM Runtime Comparison Lab]] to compare them with fixed prompts, sampler settings, context target, output cap, benchmark rows, and quality rows before choosing a deployment runtime.

## Outcome

After using this matrix you should be able to:

- identify whether a model artifact is a Hugging Face directory, Safetensors checkpoint, GGUF file, Ollama package, MLX package, GPTQ/AWQ checkpoint, FP8/INT8 checkpoint, or adapter
- choose a runtime that actually supports the artifact, quantization, hardware, and API shape
- explain why file format, tokenizer metadata, chat template, and stop conditions are part of deployment correctness
- diagnose load failures, endpoint failures, role-marker leaks, bad JSON, slow decode, and unexpected quality drops as compatibility problems instead of vague "model quality"
- record enough evidence that a future benchmark can be reproduced

## Compatibility Chain

| Layer | Question | Evidence to save |
| --- | --- | --- |
| Model family | Is the architecture supported by the runtime? | Model card, `config.json`, runtime supported-model list. |
| Artifact container | Is this Hugging Face/Safetensors, GGUF, MLX, Ollama package, or adapter? | File names, model repo tree, local path, Modelfile. |
| Numeric format | Is it FP16/BF16, INT8, INT4, GGUF quant, GPTQ, AWQ, FP8, or another scheme? | Quantization metadata, filename, runtime load log. |
| Tokenizer | Which vocabulary and normalization map text to token IDs? | Tokenizer files, GGUF metadata, token-count sanity set. |
| Chat template | How are system, user, assistant, and tool messages serialized? | Template source, rendered prompt excerpt, runtime setting. |
| Runtime engine | Which loader and scheduler will run it? | Ollama, LM Studio, llama.cpp, vLLM, SGLang, Transformers, or other engine. |
| API route | Native route or OpenAI-compatible route? | Base URL, route, request body, model id, and API contract card. |
| Workload contract | Does the task need JSON, tools, long context, RAG, citations, or streaming? | Quality harness row and benchmark log. |

If any layer is unknown, treat the run as an experiment rather than a deployment decision.

## Artifact Format Matrix

| Artifact | Common shape | Natural runtime fit | Best use | Compatibility trap |
| --- | --- | --- | --- | --- |
| Hugging Face model directory | `config.json`, tokenizer files, sharded `.safetensors` | vLLM, SGLang, Transformers, TGI-style stacks | GPU serving, research reproduction, full-precision or server quantized models | `trust_remote_code`, architecture support, tokenizer/template mismatch. |
| Safetensors weights | `.safetensors` tensors in a model directory | vLLM/SGLang/Transformers when config and tokenizer are present | Safe tensor storage and server-oriented loading | The tensor file alone is not enough; config and tokenizer still matter. |
| GGUF | Single `.gguf` file with tensors plus metadata | llama.cpp, Ollama, LM Studio; limited support in some server runtimes | Laptop, CPU, mixed CPU/GPU, edge, simple local quantized inference | Wrong quant level, missing or wrong chat template metadata, unsupported split/multi-file assumptions. |
| Ollama package | Ollama tag plus optional `Modelfile` | Ollama and UIs that connect to Ollama | Fast local model management and repeatable personal endpoint | Tag hides exact quantization/template unless recorded. |
| MLX package | Apple MLX model files | LM Studio on Apple Silicon and MLX tooling | Apple Silicon local inference | Not the Windows default path; record backend explicitly. |
| GPTQ/AWQ checkpoint | Quantized Hugging Face-style checkpoint | vLLM, SGLang, some GPU serving stacks | GPU-oriented weight-only quantized serving | Hardware and kernel support vary; not interchangeable with GGUF. |
| FP8/INT8 server checkpoint | Quantized checkpoint or runtime flag | vLLM, SGLang, hardware-specific stacks | Throughput or memory reduction on supported accelerators | Hardware compatibility and validation after quantization are mandatory. |
| LoRA or adapter | Adapter files plus base model reference | PEFT/Transformers, some runtime-specific adapter support | Adaptation without full fine-tuning | Adapter must match the exact base model family and compatible tokenizer. |

## Runtime Fit Matrix

| Runtime | Model input to prefer | API surface | Best first use | First thing to verify |
| --- | --- | --- | --- | --- |
| Ollama | Ollama library tag, GGUF, or supported Safetensors import | Native API and OpenAI-compatible routes | First Windows/local proof and repeatable personal endpoint | `ollama list`, model tag, `Modelfile`, context setting, loopback-only binding. |
| LM Studio | GGUF on Windows/Linux/macOS, MLX on Apple Silicon | OpenAI-compatible local server plus GUI | Desktop exploration and local app compatibility | Loaded model id, backend, server port, context and GPU-offload settings. |
| llama.cpp | GGUF | CLI and `llama-server` | Low-level control, CPU, edge, exact local-file serving | GGUF metadata, chat template, GPU offload, context, thread settings. |
| vLLM | Hugging Face model id/path, server quantized checkpoints, supported GGUF cases | OpenAI-compatible server | GPU serving, batching, throughput, PagedAttention practice | Supported architecture, quantization/hardware chart, CUDA/WSL/Linux readiness. |
| SGLang | Hugging Face model id/path, server quantized checkpoints | OpenAI-compatible server and programmatic serving | Structured generation, prefix-heavy workloads, high-throughput serving | Offline vs online quantization path, chat template selection, hardware backend. |
| Open WebUI | Provider endpoint, not model weights directly | Browser UI over Ollama or compatible APIs | Private chat interface after provider endpoint works | Provider health first; do not debug UI before proving the model API. |

## Decision Rules

| If you have | Start with | Why |
| --- | --- | --- |
| A Windows laptop and want the first private assistant proof | Ollama or LM Studio with a small GGUF or built-in tag | Lowest setup friction and easy local endpoint testing. |
| A raw Hugging Face model repo and a server GPU | vLLM or SGLang | They understand Hugging Face-style configs, tokenizers, and server scheduling. |
| A single quantized `.gguf` file | llama.cpp, Ollama, or LM Studio | GGUF is the native path for llama.cpp-family local inference. |
| A GPTQ/AWQ/FP8 checkpoint | vLLM or SGLang, after checking hardware support | These formats depend on runtime kernels and accelerator support. |
| A local UI need after the endpoint works | Open WebUI | It is an interface over providers, not the primary loader to debug first. |
| A fine-tuned adapter | The base model's training/runtime stack first | The adapter is not a standalone model and must match the base. |

Do not convert formats as the first fix. First prove what artifact you have, what runtime supports it, and which mismatch the failure suggests.

## Failure Diagnosis

| Symptom | Likely mismatch | Controlled check |
| --- | --- | --- |
| Runtime refuses to load model | Unsupported architecture, wrong artifact format, missing config, or missing tokenizer | Inspect repo tree, model card, config, and runtime support list. |
| `model not found` from API | Served id differs from requested id | List models through runtime-native route or `/v1/models`. |
| Endpoint 404s | Native route vs OpenAI-compatible route confusion | Verify base URL, `/v1`, and route path from [[LLM/Study/Local LLM Serving Runbook|Serving Runbook]] and [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|API Contract Lab]]. |
| Output continues the prompt | Base model, raw completion route, or missing chat template | Run [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]]. |
| Output prints role labels | Wrong template, duplicated role markers, or missing assistant prefix | Save rendered prompt evidence or runtime template setting. |
| JSON/tool output is close but invalid | Prompt-only structure without constrained decoding or schema validation | Use structured-output validation and record stop policy. |
| Same prompt is much longer on another model | Tokenizer difference | Count tokens for the sanity set before comparing latency. |
| Model loads but quality is worse than expected | Over-aggressive quantization, wrong instruct template, wrong model class, or task mismatch | Compare a higher-precision baseline and a template check before changing runtime. |
| OOM on short prompt | Weight memory, runtime buffers, or GPU allocation | Recalculate weight memory and runtime overhead. |
| OOM only on long prompt or concurrent run | KV-cache pressure | Reduce context/concurrency and rerun with the same model. |
| Slow first token | Prefill, long context, retrieval bloat, queueing, or no prefix reuse | Record prompt tokens and TTFT separately. |
| Slow later tokens | Decode memory bandwidth, model size, poor offload, or weak quantization kernels | Compare tokens/sec, quantization, and GPU/CPU utilization. |

## Compatibility Evidence Card

Copy this into a benchmark row or capstone run note.

| Field | Value |
| --- | --- |
| Workload |  |
| Model id or local file |  |
| Source URL or local path |  |
| License and data boundary |  |
| Revision, tag, or digest |  |
| Acquisition/provenance card |  |
| Architecture/model family |  |
| Artifact container | HF directory / Safetensors / GGUF / Ollama tag / MLX / adapter |
| Quantization | FP16 / BF16 / INT8 / INT4 / GGUF quant / GPTQ / AWQ / FP8 / unknown |
| Tokenizer source |  |
| Chat template source |  |
| Stop/EOS policy |  |
| Runtime and version |  |
| Hardware path | CPU / CUDA / ROCm / Metal / WSL / remote GPU |
| API base URL and route |  |
| OpenAI-compatible? | Yes / No / Partial |
| First smoke-test output |  |
| Failure layer, if any | artifact / quantization / tokenizer / template / runtime / route / quality / memory |
| Benchmark row link |  |

## Mini-Lab

1. Choose one small instruct model available both as a Hugging Face-style model and as a GGUF quantization.
2. Fill the compatibility evidence card for the GGUF path before loading it.
3. Serve it with Ollama, LM Studio, or llama.cpp and run the exact prompt from [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]].
4. Fill the evidence card for the Hugging Face/Safetensors path before loading it.
5. Serve it with vLLM or SGLang if hardware allows, or mark the hardware blocker explicitly.
6. Run the same prompt, same `temperature`, same max output tokens, and same context target.
7. Record differences in route, model id, prompt tokens, TTFT, tokens/sec, memory, and output correctness in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]].
8. If behavior differs, diagnose the layer before changing two variables at once.

## Completion Gate

This matrix is complete for one local deployment decision when you have:

- [ ] a compatibility evidence card
- [ ] a model/runtime choice justified by artifact format and quantization support
- [ ] tokenizer and chat-template evidence or an explicit "runtime does not expose this" note
- [ ] a successful native or OpenAI-compatible endpoint smoke test
- [ ] an API contract card when a generic OpenAI-compatible client will call the endpoint
- [ ] a benchmark row with prompt tokens, TTFT, tokens/sec, memory, and quality notes
- [ ] one diagnosed failure or an explicit no-failure row
- [ ] a decision to keep, convert, re-quantize, change runtime, change model, or change workload requirement

## References

Internal evidence:

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/2022 — Alignment and Chat/Quantization]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]

Supporting chunks:

- [[chunk-llm-117 PagedAttention Eliminates KV Fragmentation]]
- [[chunk-llm-118 vLLM Continuous Batching Throughput]]
- [[chunk-llm-120 vLLM De Facto Serving Framework]]
- [[chunk-llm-208 GPTQ Standard for Open-Source Deployment]]
- [[chunk-llm-211 AWQ INT4 Edge Deployment Performance]]
- [[chunk-llm-214 KV Cache Memory Bandwidth Bottleneck]]

Current external docs checked 2026-06-14:

- [Hugging Face Safetensors](https://huggingface.co/docs/safetensors/index)
- [Hugging Face GGUF on the Hub](https://huggingface.co/docs/hub/en/gguf)
- [llama.cpp README](https://github.com/ggml-org/llama.cpp)
- [Ollama Modelfile reference](https://docs.ollama.com/modelfile)
- [LM Studio documentation](https://lmstudio.ai/docs/app)
- [vLLM Hugging Face integration](https://docs.vllm.ai/en/latest/design/huggingface_integration/)
- [vLLM quantization](https://docs.vllm.ai/en/latest/features/quantization/)
- [SGLang documentation](https://docs.sglang.io/)
- [SGLang quantization](https://docs.sglang.ai/advanced_features/quantization.html)
