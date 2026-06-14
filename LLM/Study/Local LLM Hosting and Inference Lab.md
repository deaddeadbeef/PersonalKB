---
tags: [study, llm, inference, local-llm, lab]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-14
---

# Local LLM Hosting and Inference Lab

> **One-line summary** Local LLM work is the practical bridge between model theory and real systems: choose weights, choose a runtime, expose an API, measure latency/quality, and iterate.

## Outcome

After this lab you should be able to:

- choose between Ollama, LM Studio, llama.cpp, vLLM, SGLang, and Open WebUI for a concrete workload
- run a small instruct model locally
- call a local model through an HTTP API
- explain why quantization, KV cache, batching, and context length dominate local inference planning
- collect a basic benchmark: time to first token, tokens/sec, memory use, and answer quality

This lab is the Level 5 proof gate in [[LLM/Study/LLM Mastery Roadmap|LLM Mastery Roadmap]].

Save each experiment in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] so the run is reproducible and the model/runtime choice is based on evidence rather than memory.

## Mental Model

Local inference has four layers:

| Layer | Question | Study anchor |
| --- | --- | --- |
| Model weights | Which open-weight model and license fit the task? | [[Open-Weight Model Ecosystem]] |
| Numeric format | How much memory can the machine afford? | [[Quantization]] |
| Runtime | Which engine loads and schedules the model? | [[Serving Architectures and Throughput-Latency Trade-offs]] |
| Application surface | CLI, web UI, REST API, or OpenAI-compatible client? | [[Function Calling]], [[Structured Output and Constrained Generation]] |

The academic core is not separate from deployment. A local model is slow or fast because of Transformer decoding, KV-cache growth, memory bandwidth, quantization, batching, and scheduling. Read this lab alongside [[KV Cache and Context Reuse]], [[Batching and Continuous Batching]], [[Speculative Decoding]], and [[Serving Architectures and Throughput-Latency Trade-offs]].

## Runtime Choice

| Tool | Best use | API shape | Practical note |
| --- | --- | --- | --- |
| Ollama | Fast laptop/server experiments with simple model management | Native local API at `http://localhost:11434/api` | Best first stop for "can I run this model and talk to it?" |
| LM Studio | Desktop model browsing, GUI chat, and local app testing | OpenAI-compatible endpoints, commonly under `http://localhost:1234/v1` | Good for interactive exploration and quick client compatibility tests |
| llama.cpp | GGUF models, CPU/edge, Apple Silicon, and careful low-level tuning | `llama-server` can expose an OpenAI-compatible local server | Best when hardware is limited or you need exact control over local binaries and quantized files |
| vLLM | GPU-backed serving where throughput matters | OpenAI-compatible server, default local quickstart port `8000` | Learn this for production-style serving, batching, and PagedAttention |
| SGLang | High-throughput structured generation, multi-turn/programmatic workloads, and advanced serving | OpenAI/Hugging Face compatible serving | Learn this after vLLM when prefix reuse, structured generation, or large-scale serving matters |
| Open WebUI | Self-hosted chat interface over Ollama or OpenAI-compatible providers | Web app front end, provider adapters underneath | Good when you want a private ChatGPT-like surface over local or self-hosted models |

Treat Hugging Face TGI as important historically and operationally, but not the default new choice: Hugging Face documents TGI as maintenance-mode for Inference Endpoints and recommends vLLM or SGLang for new endpoint work.

## Hardware Planning

Use this rough sizing loop before downloading a model:

1. Pick the smallest model that can do the job. Start with a 3B-8B instruct model for laptop experiments, then move up only when quality fails.
2. Estimate weight memory. FP16 needs about `2 bytes x parameter count`; INT4/GGUF-style quantization is roughly one quarter of FP16 before runtime overhead.
3. Add KV-cache headroom. Context length and concurrency can dominate memory even when weights are quantized.
4. Match runtime to hardware. llama.cpp is the most forgiving for CPU and mixed CPU/GPU setups; Ollama and LM Studio simplify local use; vLLM/SGLang expect a more server-like GPU environment.
5. Benchmark the actual task. Do not assume leaderboard quality transfers to your prompts, documents, latency target, or hardware.

Key theory links:

- [[chunk-llm-214 KV Cache Memory Bandwidth Bottleneck]] explains why decode speed is often memory-bandwidth-bound.
- [[chunk-llm-208 GPTQ Standard for Open-Source Deployment]] and [[chunk-llm-211 AWQ INT4 Edge Deployment Performance]] explain why 4-bit deployment became practical.
- [[chunk-llm-117 PagedAttention Eliminates KV Fragmentation]] and [[chunk-llm-118 vLLM Continuous Batching Throughput]] explain why production servers care so much about KV-cache memory management.
- [[chunk-llm-260 Prompt caching reduces input token costs 50-90 percent by reusing KV cache for repeated prefixes]] explains why repeated system prompts and agent loops need prefix reuse.

## Lab 1: Fast Local Chat With Ollama

Use this when the goal is to get a model running quickly.

```powershell
ollama pull <model>
ollama run <model>
```

Call the local API from PowerShell:

```powershell
$body = @{
  model = "<model>"
  prompt = "Explain KV cache in one paragraph."
  stream = $false
} | ConvertTo-Json

Invoke-RestMethod `
  -Uri "http://localhost:11434/api/generate" `
  -Method Post `
  -Body $body `
  -ContentType "application/json"
```

What to observe:

- startup time: how long before the model responds
- generation speed: whether output feels interactive
- memory pressure: RAM/VRAM while the model is loaded
- quality: whether the answer is correct on topics you know well

## Lab 2: Desktop API Compatibility With LM Studio

Use this when you want a GUI plus a local API for existing OpenAI-style clients.

1. Download or load a local model in LM Studio.
2. Start the local server from the Developer/Local Server area.
3. Point a client at the local base URL instead of the cloud provider.

Python client shape:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="local",
)

response = client.chat.completions.create(
    model="<loaded-model-id>",
    messages=[{"role": "user", "content": "Give me a 3-bullet local LLM checklist."}],
)

print(response.choices[0].message.content)
```

What to observe:

- whether your existing client code works after changing only `base_url`
- reported tokens/sec and time-to-first-token if the UI exposes them
- context limit and quantization metadata for the loaded model

## Lab 3: GGUF and Low-Level Control With llama.cpp

Use this when you want to understand the runtime rather than hide it.

```powershell
llama-cli -m C:\models\<model>.gguf -p "Explain grouped-query attention."
```

Expose a local server:

```powershell
llama-server -m C:\models\<model>.gguf --host 127.0.0.1 --port 8080
```

Then query it with an OpenAI-compatible client or direct HTTP call, depending on the server build and route support.

What to observe:

- how quantization level changes speed and quality
- how many layers can be offloaded to GPU, if any
- whether CPU-only speed is acceptable for batch, reading, or coding tasks
- how context length affects memory and responsiveness

## Lab 4: Production-Style Serving With vLLM

Use this when the goal is GPU-backed serving rather than a desktop chat session. For serious vLLM work, assume a Linux/WSL or server environment with a supported accelerator.

```powershell
vllm serve Qwen/Qwen2.5-1.5B-Instruct
```

Query the local OpenAI-compatible endpoint:

```powershell
Invoke-RestMethod `
  -Uri "http://localhost:8000/v1/chat/completions" `
  -Method Post `
  -ContentType "application/json" `
  -Body '{
    "model": "Qwen/Qwen2.5-1.5B-Instruct",
    "messages": [{"role": "user", "content": "Summarize PagedAttention in two sentences."}]
  }'
```

What to observe:

- maximum concurrent requests before latency becomes unacceptable
- TTFT versus tokens/sec
- GPU utilization during prefill and decode
- how throughput changes with batch size, context length, and output length

## Benchmark Notebook Checklist

Record each run in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]]. At minimum, capture:

| Field | Example |
| --- | --- |
| Runtime | Ollama, llama.cpp, vLLM, SGLang |
| Model | model id and parameter size |
| Quantization | FP16, INT8, Q4_K_M, AWQ, GPTQ |
| Hardware | CPU, GPU, VRAM/RAM |
| Prompt class | chat, coding, summarization, RAG, extraction |
| Context tokens | prompt size and max context |
| Output tokens | generated length |
| TTFT | seconds to first token |
| Decode speed | tokens/sec |
| Peak memory | RAM/VRAM |
| Quality notes | factuality, instruction following, formatting |

Run at least three prompt types:

1. A fact you know well, to catch hallucination.
2. A coding or structured-output task, to test instruction following.
3. A long-context task, to expose KV-cache and context-window behavior.

## Troubleshooting

| Symptom | Likely cause | First fix |
| --- | --- | --- |
| Model will not load | Not enough RAM/VRAM, unsupported format, missing runtime backend | Use a smaller or more quantized model; verify the model format matches the runtime |
| Loads but is painfully slow | CPU-only decode, too large a model, too long context | Use a smaller model, stronger quantization, GPU offload, or lower context |
| First token is slow but later tokens are fine | Expensive prefill or long prompt | Shorten prompt, use prefix caching, reduce retrieved context |
| Later tokens are slow | Decode memory bandwidth bottleneck | Try quantization, smaller model, MQA/GQA model, batching, or a serving runtime |
| Answers are weak | Wrong model/task fit or too much compression | Test a stronger model, less aggressive quantization, better prompt, or RAG |
| API client fails | Wrong base URL, wrong route, unloaded model | Check `/v1/models` or runtime-specific model list endpoint |

## Academic Spine For This Lab

Read in this order if you want the theory to match the practical knobs:

1. [[Language Model Fundamentals]] and [[Tokenization]] - why next-token prediction and tokens define the interface.
2. [[Transformer Architecture]] and [[Attention Mechanism]] - why decoding keeps reusing key/value states.
3. [[Open-Weight Model Ecosystem]] - why local weights changed who can deploy models.
4. [[Quantization]] - why model files shrink and quality can degrade.
5. [[KV Cache and Context Reuse]] - why context length and concurrency consume memory.
6. [[Batching and Continuous Batching]] - why serving many users differs from a single chat.
7. [[Serving Architectures and Throughput-Latency Trade-offs]] - why production serving is an operating point, not a single best tool.
8. [[LLM-as-Judge]] and [[Human Evaluation and Preference Studies]] - how to evaluate quality instead of trusting vibes.

## References

Internal evidence:

- [[LLM/Sources/Sources Index]]
- [[chunk-llm-117 PagedAttention Eliminates KV Fragmentation]]
- [[chunk-llm-118 vLLM Continuous Batching Throughput]]
- [[chunk-llm-120 vLLM De Facto Serving Framework]]
- [[chunk-llm-208 GPTQ Standard for Open-Source Deployment]]
- [[chunk-llm-211 AWQ INT4 Edge Deployment Performance]]
- [[chunk-llm-214 KV Cache Memory Bandwidth Bottleneck]]
- [[chunk-llm-260 Prompt caching reduces input token costs 50-90 percent by reusing KV cache for repeated prefixes]]

Current external docs checked 2026-06-14:

- [Ollama API documentation](https://docs.ollama.com/api/introduction)
- [llama.cpp README](https://github.com/ggml-org/llama.cpp)
- [vLLM quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/)
- [LM Studio OpenAI compatibility endpoints](https://lmstudio.ai/docs/developer/openai-compat)
- [Open WebUI documentation](https://docs.openwebui.com/)
- [SGLang documentation](https://docs.sglang.io/)
- [Hugging Face TGI migration note](https://huggingface.co/docs/inference-endpoints/en/engines/tgi)
