---
tags: [study, llm, inference, local-llm, serving, runbook]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-14
---

# Local LLM Serving Runbook

> **One-line summary** Local serving is the operational proof that you can turn model weights into a callable API, verify the endpoint, and explain the latency, memory, and quality trade-offs.

Use this after [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]] and record results in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]]. Use [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] when the first working endpoint needs a scored quality decision. The lab explains the concepts; this runbook gives the repeatable serving sequence.

After the smoke test passes, use [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] to turn the endpoint call into a repeatable client that logs settings, latency, streaming, errors, and benchmark rows.

Before starting the server, use [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]] to choose a model size, quantization, context target, and runtime that fit the hardware.

Use [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]] to prove the actual hardware visibility, runtime boundary, disk, model cache, port, and endpoint boundary before diagnosing serving errors. If a failure crosses more than one layer, use [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]] to name the failed layer and next controlled test.

Before exposing the endpoint beyond a one-person loopback experiment, use [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] to check binding, authentication, logging, RAG data, prompt injection, and tool permissions.

## Success Criteria

A local serving run is complete when:

- the model loads without out-of-memory errors
- the machine/runtime preflight records hardware visibility, disk headroom, model cache, and intended host/port
- a CLI or GUI chat proves the model can generate
- an HTTP endpoint returns a non-streaming response
- the same endpoint can be called by a generic OpenAI-compatible client or direct REST call
- a client harness logs request settings, timing, output summary, and failure rows without manual copy/paste
- endpoint exposure, logs, RAG corpus, and tool permissions are explicit before any non-loopback use
- tokenizer, chat template, role boundaries, and stop policy are checked when output ignores instructions or leaks role markers
- latency, tokens/sec, memory, model id, runtime, quantization, and quality notes are logged
- the quality decision is backed by [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] when choosing a model for real work
- you can explain the result using [[LLM/2022 — Alignment and Chat/Quantization|Quantization]], [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse|KV Cache and Context Reuse]], and [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs|Serving Architectures and Throughput-Latency Trade-offs]]

## Runtime Decision Path

| If the goal is | Start with | Why |
| --- | --- | --- |
| Fastest Windows laptop proof | Ollama or LM Studio | Simple install, model management, local chat, and HTTP API |
| GUI model browsing plus app compatibility | LM Studio | Local server exposes OpenAI-compatible endpoints on the desktop |
| GGUF, CPU, edge, or exact low-level control | llama.cpp or llama-cpp-python server | Best fit for quantized local files and constrained hardware |
| GPU throughput and production-style scheduling | vLLM | OpenAI-compatible serving plus batching-oriented infrastructure |
| Structured generation or prefix-heavy server workloads | SGLang | OpenAI-compatible serving plus structured/prefix-aware serving patterns |
| Private chat UI over one or more local providers | Open WebUI | Frontend that connects to Ollama and OpenAI-compatible APIs |

Choose the smallest model that can pass the task, then scale up only when quality fails. Treat a larger quantized model and a smaller higher-precision model as competing hypotheses, not as automatically equivalent choices.

## Safety Boundary

Start on loopback only: `127.0.0.1` or `localhost`. Do not bind a model server to `0.0.0.0`, expose it to the LAN, or tunnel it publicly until you have authentication, firewall rules, and a reason to accept the data-leak risk.

Local LLMs are still application servers. Prompts, retrieved documents, generated outputs, and logs may contain private data.

For the full checklist, see [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]].

## Endpoint Map

| Runtime | First endpoint to verify | Notes |
| --- | --- | --- |
| Ollama native API | `http://localhost:11434/api/generate` | Native API returns useful timing fields such as prompt and eval durations |
| Ollama OpenAI-compatible API | `http://localhost:11434/v1/chat/completions` | Good when testing OpenAI-compatible clients against Ollama |
| LM Studio | `http://localhost:1234/v1/chat/completions` | Port `1234` is the common local-server example in LM Studio docs |
| llama-cpp-python server | configurable, for example `http://localhost:8001/v1/chat/completions` | Installable Python server wrapper for GGUF/local model files |
| vLLM | `http://localhost:8000/v1/chat/completions` | Default quickstart server is OpenAI-compatible on local port `8000` |
| SGLang | commonly `http://localhost:30000/v1/chat/completions` | Launch-server examples use local port `30000`; set host/port explicitly |
| Open WebUI | browser UI plus provider settings | Connect it to Ollama or any compatible local server after the provider endpoint works |

## Phase 0: Record The Run Plan

Before starting the server, write these fields into [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]]:

| Field | Example |
| --- | --- |
| Objective | "Can this 7B quantized model answer coding questions locally?" |
| Model id/file | Hugging Face id, Ollama tag, LM Studio id, or GGUF filename |
| Runtime | Ollama, LM Studio, llama-cpp-python, vLLM, SGLang |
| Quantization/format | Q4_K_M, GPTQ, AWQ, FP16, BF16, unknown |
| Hardware | CPU, GPU, RAM, VRAM |
| Environment preflight | OS, runtime boundary, disk/model cache, hardware visibility, host/port plan |
| API base URL | The local base URL you expect to call |
| Prompt suite | Known fact, coding/structured output, long-context, RAG, summarization |

The run plan prevents the common mistake of changing model, runtime, prompt, and sampling all at once.

## Phase 1: Ollama Native Smoke Test

Use this when you want the fastest local API proof.

```powershell
ollama pull <model>
ollama run <model>
```

In a second PowerShell window:

```powershell
$Model = "<model>"
$Body = @{
  model = $Model
  prompt = "Reply with exactly: local llm ok"
  stream = $false
} | ConvertTo-Json -Depth 5

Invoke-RestMethod `
  -Uri "http://localhost:11434/api/generate" `
  -Method Post `
  -ContentType "application/json" `
  -Body $Body
```

Evidence to save:

- response text
- `total_duration`
- `load_duration`
- `prompt_eval_count`
- `eval_count`
- `eval_duration`

Those fields give a first approximation of load time, prompt processing, and decode speed.

## Phase 2: OpenAI-Compatible Smoke Test

Use this for LM Studio, Ollama compatibility mode, vLLM, SGLang, and compatible local servers.

```powershell
$BaseUrl = "http://localhost:1234/v1"
$Model = "<served-model-id>"
$Body = @{
  model = $Model
  messages = @(
    @{ role = "user"; content = "Reply with exactly: local llm ok" }
  )
  temperature = 0
  max_tokens = 16
} | ConvertTo-Json -Depth 6

Invoke-RestMethod `
  -Uri "$BaseUrl/chat/completions" `
  -Method Post `
  -ContentType "application/json" `
  -Headers @{ Authorization = "Bearer local" } `
  -Body $Body
```

Swap only `$BaseUrl` and `$Model` when comparing runtimes:

| Runtime | `$BaseUrl` |
| --- | --- |
| Ollama OpenAI-compatible | `http://localhost:11434/v1` |
| LM Studio | `http://localhost:1234/v1` |
| llama-cpp-python server | `http://localhost:8001/v1` if launched on port `8001` |
| vLLM | `http://localhost:8000/v1` |
| SGLang | `http://localhost:30000/v1` |

If the endpoint fails, verify in this order:

1. The server process is running.
2. The model is actually loaded or served under the model id you sent.
3. The base URL includes `/v1` for OpenAI-compatible routes.
4. The route is `/chat/completions`, not the runtime's native route.
5. The server is listening on loopback and the expected port.

## Phase 3: Runtime-Specific Start Points

| Runtime | Start point | First proof |
| --- | --- | --- |
| Ollama | `ollama pull <model>` then `ollama run <model>` | Native `/api/generate`, then optional `/v1/chat/completions` |
| LM Studio | Load a model in the GUI, start the local server | `http://localhost:1234/v1/chat/completions` |
| llama-cpp-python | `pip install llama-cpp-python[server]`; launch with an explicit `--model`, `--host`, and `--port` | OpenAI-compatible response from the chosen port |
| vLLM | `vllm serve <model-id>` in a GPU-ready Linux/WSL/server environment | `/v1/models`, then `/v1/chat/completions` on port `8000` |
| SGLang | `python -m sglang.launch_server --model-path <model> --host 127.0.0.1 --port 30000` | `/v1/chat/completions` on port `30000` |
| Open WebUI | Start the UI after the provider endpoint works | Provider appears in the UI and can answer the same smoke-test prompt |

For Windows-native first experiments, prefer Ollama or LM Studio. For vLLM/SGLang, expect a Linux, WSL, or server-style GPU environment and validate CUDA/driver support before diagnosing model quality.

## Phase 4: Measure The First Useful Run

Run the prompt suite from [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] and capture:

| Measurement | Why it matters |
| --- | --- |
| Load time | Separates model-start cost from request latency |
| Time to first token | Captures prefill, scheduling, and queueing delay |
| Decode tokens/sec | Shows the speed of autoregressive generation |
| Prompt tokens | Explains why long-context runs are slower |
| Output tokens | Needed to compare total latency fairly |
| Peak RAM/VRAM | Confirms whether the setup has real headroom |
| Quality notes | Prevents "fast but wrong" from passing |

For real workload selection, turn the quality notes into scored prompt rows with [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]].

Interpretation anchors:

- High load time but good decode speed usually means cold-start cost, not a bad model.
- Slow first token with normal later tokens points to long prefill, retrieval context, queueing, or no prefix reuse.
- Slow later tokens points toward decode bottlenecks: model size, memory bandwidth, quantization support, or weak hardware.
- Out-of-memory errors can come from weights, KV cache, context length, or concurrency; do not blame parameter count alone.

## Phase 5: Compare Two Runtimes

Do one controlled comparison before calling the local setup "understood":

| Compare | Keep fixed | Change |
| --- | --- | --- |
| Ollama vs LM Studio | Same model family/size if available, same prompts | Desktop runtime/API surface |
| Ollama vs llama.cpp | Same GGUF or comparable quantization if possible | Runtime control and CPU/GPU offload |
| llama.cpp vs vLLM | Same model family/size, similar precision if possible | Edge/runtime control vs GPU serving |
| vLLM vs SGLang | Same model id, same prompt suite | Serving scheduler and structured/prefix workload fit |

Record whether the difference is quality, TTFT, decode speed, memory, endpoint compatibility, or operational ergonomics.

## Failure Triage

| Symptom | Most likely layer | First action |
| --- | --- | --- |
| Server starts but `/chat/completions` 404s | Wrong route or missing `/v1` | Check native vs OpenAI-compatible route |
| Model id not found | Runtime/model registry | List models or copy exact served id from the runtime |
| Immediate out-of-memory | Weight memory or CUDA allocation | Smaller model, stronger quantization, lower GPU offload, or more VRAM |
| OOM only on long prompts | KV cache | Reduce context, batch/concurrency, or retrieved chunks |
| First token takes too long | Prefill/queueing | Shorten prompt, reduce retrieved context, check queue/concurrency |
| Tokens/sec is too low | Decode memory bandwidth | Smaller model, quantization, better GPU offload, or different runtime |
| Output ignores instructions | Model/prompt quality, wrong chat template, or tokenizer mismatch | Run [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]], then try stronger instruct model, better template, or lower quantization |
| Open WebUI cannot see models | Provider config | Verify provider endpoint directly before debugging the UI |

## Completion Proof

To pass the local-serving proof gate, save:

1. The exact runtime and model id.
2. The startup command or GUI server settings.
3. A successful native or OpenAI-compatible API response.
4. At least three prompt-suite outputs.
5. One client harness row for the run, including either streaming timing or an explicit unsupported note.
6. Benchmark log measurements.
7. A quality harness pass/hold/fail decision for the target workload.
8. A short explanation of the bottleneck using the academic links above.
9. A decision: keep, tune, replace model, or replace runtime.

## References

Internal evidence:

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/2022 — Alignment and Chat/Quantization]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2023 — Open Models and Agents/Open-Weight Model Ecosystem]]

Current external docs checked 2026-06-14:

- [Ollama API introduction](https://docs.ollama.com/api/introduction)
- [Ollama generate endpoint](https://docs.ollama.com/api/generate)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
- [LM Studio OpenAI compatibility endpoints](https://lmstudio.ai/docs/developer/openai-compat)
- [llama-cpp-python OpenAI-compatible server](https://llama-cpp-python.readthedocs.io/en/latest/server/)
- [vLLM quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/)
- [SGLang OpenAI-compatible API](https://docs.sglang.io/docs/basic_usage/openai_api_completions)
- [Open WebUI documentation](https://docs.openwebui.com/)
- [Open WebUI connect a provider](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/)
