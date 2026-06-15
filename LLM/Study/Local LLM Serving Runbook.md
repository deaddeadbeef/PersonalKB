---
tags: [study, llm, inference, local-llm, serving, runbook]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-14
---

# Local LLM Serving Runbook

> **One-line summary** Local serving is the operational proof that you can turn model weights into a callable API, verify the endpoint, and explain the latency, memory, and quality trade-offs.

Use this after [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]] and record results in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]]. Use [[LLM/Study/Local LLM Command Cookbook|Local LLM Command Cookbook]] when you need the compact copyable commands for startup, route smoke tests, client calls, streaming, benchmark rows, and teardown proof. Use [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]] after the smoke test to capture model state, request timings, logs, metrics, and resource pressure, and use [[LLM/Study/Local LLM Observability and Operations Runner|Local LLM Observability and Operations Runner]] when that service-state evidence should be repeatable JSON, CSV, Markdown, and JSONL. Use [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook|Local LLM Service Lifecycle and Upgrade Runbook]] when a working endpoint must survive restarts, upgrades, cache moves, UI changes, and rollback. Use [[LLM/Study/Local LLM First Quality Probe Runner|Local LLM First Quality Probe Runner]] for the first five private quality artifacts, then use [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] when the first working endpoint needs a scored workload decision. The lab explains the concepts; this runbook gives the repeatable serving sequence.

For the first complete run, fill [[LLM/Study/Local LLM First Inference Evidence Pack|Local LLM First Inference Evidence Pack]] as you go. The evidence pack is the one-page binder; this runbook is the detailed serving procedure. Before the first smoke prompt, use [[LLM/Study/Local LLM First Runtime Health Snapshot|Local LLM First Runtime Health Snapshot]] when you need a no-generation proof that the runtime listener and model-list routes are ready. Use [[LLM/Study/Local LLM First Smoke Request Runner|Local LLM First Smoke Request Runner]] when the first native and OpenAI-compatible smoke requests should be captured by one repeatable script. Use [[LLM/Study/Local LLM First Response Debrief Runner|Local LLM First Response Debrief Runner]] after the response exists to convert saved timing fields, token counts, mechanism owner, quality boundary, and next action without sending another request.

Use [[LLM/Study/Local LLM Hands-On Practicum Sequence|Local LLM Hands-On Practicum Sequence]] when this runbook is part of the ordered practicum. It decides what evidence belongs before and after the endpoint smoke test.

Use [[LLM/Study/Local LLM Runtime Stack Anatomy|Local LLM Runtime Stack Anatomy]] before blaming a model or runtime. It names the layer that owns each proof: hardware, boundary, package environment, model bytes, artifact, tokenizer/template, runtime, scheduler/cache, API route, client/UI, workload, or operations.

If the first run is on Windows, use [[LLM/Study/Local LLM Windows First-Run Quickstart|Local LLM Windows First-Run Quickstart]] for a minimal PowerShell path through preflight capture, Ollama or LM Studio API proof, listener check, and first quality mini-suite. If Ollama is not installed yet, use [[LLM/Study/Local LLM Windows Runtime Install Gate|Local LLM Windows Runtime Install Gate]] before the first `ollama pull`.

After the smoke test passes, use [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] or [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner|Local LLM OpenAI-Compatible API Contract Runner]] to prove the base URL, model id, route, streaming behavior, error behavior, and feature gaps before pointing generic clients at the server. Then use [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] to turn the endpoint call into a repeatable client that logs settings, latency, streaming, errors, and benchmark rows. Use [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab|Local LLM Concurrency and Batch Throughput Lab]] when the endpoint must handle more than one active request, a local queue, or an offline batch job. Use [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]] before relying on local function calling, structured output, or agent loops.

When the goal is to choose between Ollama, LM Studio, llama.cpp, vLLM, SGLang, or a UI over one provider, use [[LLM/Study/Local LLM Runtime Comparison Lab|Local LLM Runtime Comparison Lab]] after each candidate endpoint has a smoke test. The comparison lab keeps prompts, sampler settings, context target, and output caps fixed so runtime differences do not get confused with prompt or model drift.

When serving reasoning-capable models, use [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Lab|Local LLM Reasoning Budget and Test-Time Compute Lab]] to prove the thinking-mode trigger, reasoning parser, effort levels, latency impact, final-answer quality, and trace visibility policy before treating the model as a better default.

Before starting the server, use [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]] to prove the model card, license, revision, artifact safety, local path, and digest are acceptable. Then use [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]] to prove the exact downloaded files, cache/local path, hash or verification result, GGUF/Ollama import, conversion command, and cleanup plan. Then use [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]] to choose a model size, quantization, context target, and runtime that fit the hardware. Use [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]] to turn the context target into a measured prompt, history, RAG, tool, output, and margin budget. Then use [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]] to verify the model artifact, tokenizer, chat template, quantization, runtime, and API route before treating load failures or bad outputs as model-quality failures.

Use [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]] to prove the actual hardware visibility, runtime boundary, disk, model cache, port, and endpoint boundary before diagnosing serving errors. If a failure crosses more than one layer, use [[LLM/Study/Local LLM Runtime Stack Anatomy|Local LLM Runtime Stack Anatomy]] to name the lowest unproven layer, then use [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]] to choose the next controlled test.

For vLLM or SGLang launched from a Windows workstation, use [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab|Local LLM WSL CUDA vLLM and SGLang Setup Lab]] before this runbook's smoke test. It records WSL 2, CUDA/GPU visibility, Python environment state, loopback host/port, `/v1/models`, and a Windows PowerShell client call so serving failures are not confused with WSL or driver failures.

For containerized vLLM or SGLang, use [[LLM/Study/Local LLM Docker GPU Container Serving Lab|Local LLM Docker GPU Container Serving Lab]] before treating the endpoint as a repeatable service. It records Docker authority, GPU container smoke, pinned image tag, cache mount, loopback port publishing, `/v1/models`, host chat smoke, logs, metrics, and Compose validation.

Use [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Local LLM Serving Internals and Scheduler Lab]] after the first endpoint works but before tuning throughput, slots, batching, chunked prefill, preemption, or queue policy. That lab separates prefill, decode, KV-cache pressure, continuous batching, and admission-control behavior.

Before exposing the endpoint beyond a one-person loopback experiment, use [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] to check binding, authentication, logging, RAG data, prompt injection, and tool permissions.

## Success Criteria

A local serving run is complete when:

- the model loads without out-of-memory errors
- the machine/runtime preflight records hardware visibility, disk headroom, model cache, and intended host/port
- model acquisition records source, license, gated access, exact artifact, revision/tag/digest, and local cache path
- a CLI or GUI chat proves the model can generate
- an HTTP endpoint returns a non-streaming response
- the same endpoint can be called by a generic OpenAI-compatible client or direct REST call
- the OpenAI-compatible API contract records base URL, route, model id, streaming behavior, harmless failure behavior, and unsupported fields needed by the workload
- tool and structured-output support are validated with schema, policy, execution, result-injection, and failure rows if the workload uses tools
- a client harness logs request settings, timing, output summary, and failure rows without manual copy/paste
- concurrency, queueing, and backpressure are measured before shared, batch, or multi-client use
- endpoint exposure, logs, RAG corpus, and tool permissions are explicit before any non-loopback use
- startup mode, pinned runtime/model state, backup path, upgrade plan, and rollback target are explicit before treating the endpoint as a maintained service
- tokenizer, chat template, role boundaries, and stop policy are checked when output ignores instructions or leaks role markers
- context window, prompt tokens, retrieved/tool/history tokens, output reserve, and truncation behavior are checked for long-context workloads
- latency, tokens/sec, memory, model id, runtime, quantization, and quality notes are logged
- the first quality signal is backed by [[LLM/Study/Local LLM First Quality Probe Runner|Local LLM First Quality Probe Runner]], and the workload quality decision is backed by [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] when choosing a model for real work
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
| Compatibility evidence | Artifact, tokenizer, template, runtime, route, and workload contract |
| Acquisition evidence | Model card, license, gated access, revision/tag/digest, local path |
| Hardware | CPU, GPU, RAM, VRAM |
| Environment preflight | OS, runtime boundary, disk/model cache, hardware visibility, host/port plan |
| Context budget | Runtime limit, prompt tokens, retrieved/tool/history tokens, output reserve, safety margin |
| Tool/schema plan | Tool support, schema mode, tool-choice mode, and policy boundary if the workload uses tools |
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

Use this for LM Studio, Ollama compatibility mode, vLLM, SGLang, and compatible local servers. After the first response works, complete [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] before relying on tools, streaming, Responses API, embeddings, or client-library compatibility.

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

For the WSL version of that validation, use [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab|Local LLM WSL CUDA vLLM and SGLang Setup Lab]] and copy the successful `/v1/models` response into the API contract card.

For the Docker version of that validation, use [[LLM/Study/Local LLM Docker GPU Container Serving Lab|Local LLM Docker GPU Container Serving Lab]] and copy the successful container `/v1/models`, host chat smoke, image tag, and cache mount into the API contract card.

## Phase 4: Measure The First Useful Run

Run the prompt suite from [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] and capture:

| Measurement | Why it matters |
| --- | --- |
| Load time | Separates model-start cost from request latency |
| Time to first token | Captures prefill, scheduling, and queueing delay |
| Decode tokens/sec | Shows the speed of autoregressive generation |
| Prompt tokens | Explains why long-context runs are slower |
| Context budget margin | Shows whether the prompt leaves enough room for generation |
| Output tokens | Needed to compare total latency fairly |
| Peak RAM/VRAM | Confirms whether the setup has real headroom |
| Quality notes | Prevents "fast but wrong" from passing |

For real workload selection, turn the first quality probe runner output into scored prompt rows with [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]].

Before interpreting those rows, capture the operations evidence from [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]] or [[LLM/Study/Local LLM Observability and Operations Runner|Local LLM Observability and Operations Runner]]: loaded-model state, route, raw request/response timing, server logs or metrics, CPU/RAM and GPU/VRAM pressure, and one next controlled action.

When this endpoint will be used again after today, fill the [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook|Local LLM Service Lifecycle and Upgrade Runbook]] Change Freeze Card before changing runtime version, model artifact, startup mode, cache path, UI container, driver, or client contract.

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
| OOM only on long prompts | KV cache | Run [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]], then reduce context, batch/concurrency, or retrieved chunks |
| First token takes too long | Prefill/queueing | Shorten prompt, reduce retrieved context, check queue/concurrency, and compare prompt-token budgets |
| Tokens/sec is too low | Decode memory bandwidth | Smaller model, quantization, better GPU offload, or different runtime |
| Output ignores instructions | Model/prompt quality, wrong chat template, or tokenizer mismatch | Run [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]], then try stronger instruct model, better template, or lower quantization |
| Tool call is wrong, unsafe, or ignored | Tool/schema boundary | Run [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]], then validate schema, policy, and result injection |
| Open WebUI cannot see models | Provider config | Verify provider endpoint directly before debugging the UI |

## Completion Proof

To pass the local-serving proof gate, save:

1. The exact runtime and model id.
2. The startup command or GUI server settings.
3. A successful native or OpenAI-compatible API response.
4. At least three prompt-suite outputs.
5. One client harness row for the run, including either streaming timing or an explicit unsupported note.
6. One OpenAI-compatible API contract card, or an explicit native-API-only decision.
7. Benchmark log measurements.
8. A quality harness pass/hold/fail decision for the target workload.
9. A context-budget row when history, RAG, tools, or long prompts are part of the workload.
10. A tool-calling proof row when tools, structured output, or agent loops are part of the workload.
11. A short explanation of the bottleneck using the academic links above.
12. A decision: keep, tune, replace model, or replace runtime.

## References

Internal evidence:

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Command Cookbook]]
- [[LLM/Study/Local LLM First Runtime Health Snapshot]]
- [[LLM/Study/Local LLM First Smoke Request Runner]]
- [[LLM/Study/Local LLM First Response Debrief Runner]]
- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM Hands-On Practicum Sequence]]
- [[LLM/Study/Local LLM Windows First-Run Quickstart]]
- [[LLM/Study/Local LLM Windows Runtime Install Gate]]
- [[LLM/Study/Local LLM Runtime Stack Anatomy]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab]]
- [[LLM/Study/Local LLM Docker GPU Container Serving Lab]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Observability and Operations Runner]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM First Quality Probe Runner]]
- [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Lab]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
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
- [vLLM GPU installation](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/)
- [vLLM OpenAI-compatible server](https://docs.vllm.ai/en/stable/serving/online_serving/openai_compatible_server/)
- [SGLang OpenAI-compatible API](https://docs.sglang.io/docs/basic_usage/openai_api_completions)
- [SGLang quickstart](https://docs.sglang.io/docs/get-started/quickstart)
- [Open WebUI documentation](https://docs.openwebui.com/)
- [Open WebUI connect a provider](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/)
