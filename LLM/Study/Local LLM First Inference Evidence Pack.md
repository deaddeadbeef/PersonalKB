---
tags: [study, llm, inference, local-llm, serving, evidence]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM First Inference Evidence Pack

> **One-line summary** The first local LLM run is complete only when you can show the machine, model, runtime, endpoint, request, response, timing, quality check, security boundary, and next decision in one evidence packet.

Use this as the first-run binder for [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]] and [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]]. Those notes explain the runtime choices and serving sequence. This note tells you exactly what to save so the run becomes capstone evidence.

Use [[LLM/Study/Local LLM Hands-On Practicum Sequence|Local LLM Hands-On Practicum Sequence]] when you want the broader ordered path around this packet. This evidence pack is the Stage 1 endpoint proof in that practicum.

For the first Windows-native proof, use [[LLM/Study/Local LLM Windows First-Run Quickstart|Local LLM Windows First-Run Quickstart]] and prefer Ollama or LM Studio. If the first run is Ollama, use [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]] to capture model-pull custody, [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]] to create the raw response files, [[LLM/Study/Local LLM First Response Debrief Card|Local LLM First Response Debrief Card]] to interpret the first response, [[LLM/Study/Local LLM First Quality Probe Suite|Local LLM First Quality Probe Suite]] for a tiny private quality signal, [[LLM/Study/Local LLM First Client Harness Runner|Local LLM First Client Harness Runner]] for the first reusable client-side inference row, and [[LLM/Study/Local LLM First Streaming Timing Runner|Local LLM First Streaming Timing Runner]] when the first client proof needs perceived-latency evidence before copying benchmark or capstone quality rows. For GGUF/CPU control, use llama.cpp or llama-cpp-python. For production-style GPU serving, use vLLM or SGLang after hardware and Linux/WSL/server support are proven. If that proof starts from Windows, use [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab|Local LLM WSL CUDA vLLM and SGLang Setup Lab]] before treating the endpoint as benchmark evidence. If the endpoint is containerized, add [[LLM/Study/Local LLM Docker GPU Container Serving Lab|Local LLM Docker GPU Container Serving Lab]] evidence before treating Docker, Open WebUI, or Compose as the serving contract.

## Evidence Packet

Create one dated note or folder per run:

```text
local-llm-runs/
  2026-06-15-first-ollama-run/
    run-card.md
    preflight.txt
    model-provenance.md
    endpoint-smoke.json
    openai-contract.md
    client-harness.jsonl
    streaming-timing.jsonl
    first-benchmark-row/
    benchmark-row.md
    first-quality-probe-suite/
    first-client-harness/
    first-streaming-timing/
    quality-row.md
    decision.md
```

If you are writing directly in Obsidian, put the same fields in a dated experiment note and link it from [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]].

## Run Card

Fill this before changing anything:

| Field | Value |
|---|---|
| Run id |  |
| Date |  |
| Goal | first chat / API proof / coding helper / RAG / tool loop / benchmark |
| Runtime | Ollama / LM Studio / llama.cpp / llama-cpp-python / vLLM / SGLang / other |
| Runtime boundary | Windows native / WSL / Docker / remote Linux / desktop GUI |
| Model id or file |  |
| Model family and size |  |
| Quantization or precision |  |
| Hardware | CPU, GPU, RAM, VRAM |
| Endpoint base URL |  |
| Native route |  |
| OpenAI-compatible route |  |
| First response debrief |  |
| Security boundary | loopback only / LAN / tunnel / remote |
| Prompt suite | smoke / known-answer / structured / long-context / RAG / tool |
| Decision target | keep / tune / replace model / replace runtime |

Pass signal: another person can reproduce which model served which request through which endpoint.

## Step 1: Preflight

Use [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]]. Save:

| Evidence | Command or source |
|---|---|
| OS and shell | PowerShell, WSL, Linux shell, Docker shell |
| CPU/RAM | Windows system info or runtime logs |
| GPU/VRAM | `nvidia-smi`, runtime UI, or explicit CPU-only note |
| Disk/model cache | free space and model cache path |
| Planned host/port | `127.0.0.1:<port>` or `localhost:<port>` |
| Listener proof | `Get-NetTCPConnection`, `Test-NetConnection`, `/api/tags`, or `/v1/models` |

Do not diagnose model quality until the runtime boundary is clear. Windows PowerShell, WSL, Docker, and a remote Linux shell can see different hardware and different localhost behavior.

## Step 2: Model And Runtime Fit

Use [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]], [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]], and [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]].

Minimum evidence:

| Evidence | Pass signal |
|---|---|
| Model source | model card, registry page, local file path, or runtime tag |
| License/gated access | allowed for personal/local use, or risk noted |
| Artifact format | Ollama tag, GGUF, HF directory, GPTQ, AWQ, Safetensors, or other |
| Exact revision or digest | revision/tag/hash/digest or reproducibility marked partial |
| First Ollama pull gate | selected tag, pull output, `ollama ls`, `/api/tags`, and `/api/show` when Ollama is the first runtime |
| Runtime compatibility | tokenizer, chat template, quantization, route, and workload fit are known |
| WSL CUDA setup | if vLLM/SGLang from Windows, WSL GPU visibility, Python environment, loopback route, `/v1/models`, Windows client call, logs, and metrics are known |
| Docker GPU container setup | if vLLM/SGLang runs in Docker, Docker authority, container GPU proof, image tag, cache mount, loopback port, `/v1/models`, logs, metrics, and Compose proof are known |
| Memory estimate | weights plus KV-cache headroom fit the machine |

The first run may be a small model. That is fine. The point is to prove the serving loop before optimizing quality.

## Step 3: Start The Runtime

Choose one path.

| Runtime | Start proof | First endpoint |
|---|---|---|
| Ollama | `ollama pull <model>` then `ollama run <model>` | `http://localhost:11434/api/generate` |
| Ollama OpenAI-compatible | Ollama running with model available | `http://localhost:11434/v1/chat/completions` |
| LM Studio | Load model, start local server in Developer/Local Server | `http://localhost:1234/v1/chat/completions` |
| llama.cpp | `llama-server -m <model.gguf> --host 127.0.0.1 --port 8080` | OpenAI-compatible server routes from that port |
| llama-cpp-python | `python -m llama_cpp.server --model <model.gguf> --host 127.0.0.1 --port 8001` | `http://localhost:8001/v1/chat/completions` |
| vLLM | `vllm serve <model-id>` | `http://localhost:8000/v1/chat/completions` by default |
| SGLang | `python -m sglang.launch_server --model-path <model> --host 127.0.0.1 --port 30000` | `http://localhost:30000/v1/chat/completions` |

For a private first run, keep the host on loopback. Do not bind to `0.0.0.0` until [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] says why the exposure is acceptable.

## Step 4: Native Smoke Test

For Ollama native API, save the full JSON response because the timing fields are useful:

```powershell
$Body = @{
  model = "<model>"
  prompt = "Reply with exactly: local llm ok"
  stream = $false
} | ConvertTo-Json -Depth 5

Invoke-RestMethod `
  -Uri "http://localhost:11434/api/generate" `
  -Method Post `
  -ContentType "application/json" `
  -Body $Body
```

Record:

| Field | Value |
|---|---|
| Response text |  |
| `total_duration` |  |
| `load_duration` |  |
| `prompt_eval_count` |  |
| `prompt_eval_duration` |  |
| `eval_count` |  |
| `eval_duration` |  |

The response text proves the endpoint works. The timing fields separate load time, prompt processing, and decode speed.

## Step 5: OpenAI-Compatible Smoke Test

Use this when testing LM Studio, Ollama compatibility mode, llama.cpp-style servers, vLLM, SGLang, or a generic local client.

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

After this passes, use [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] to prove routes, model discovery, streaming, error shape, embeddings, tool support, and unsupported fields needed by the workload.

## Step 6: Repeatable Client Harness

Use [[LLM/Study/Local LLM First Client Harness Runner|Local LLM First Client Harness Runner]] for the first reusable Python client call, [[LLM/Study/Local LLM First Streaming Timing Runner|Local LLM First Streaming Timing Runner]] for the first streaming TTFT and event-log row, then [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] when the endpoint needs retries, multiple prompt cases, or application integration. The harness should log:

| Field | Why |
|---|---|
| runtime, base URL, route, model id | proves what was called |
| request body hash or saved redacted body | makes prompt and settings reproducible |
| non-streaming status | baseline response proof |
| streaming status, first event, and TTFT | required if the UI/client streams |
| timeout and retry policy | prevents silent hangs |
| latency fields | feeds benchmark log |
| response excerpt/path | supports quality review |
| error body | supports troubleshooting |

Manual one-off `curl` is enough for a smoke test. It is not enough for repeatable model selection.

## Step 7: First Benchmark Row

If the run folder already contains `first-client-harness/client-runs.jsonl` or `first-streaming-timing/streaming-runs.jsonl`, use [[LLM/Study/Local LLM First Benchmark Row Builder|Local LLM First Benchmark Row Builder]] to create a benchmark JSON file, Markdown copy row, and missing-layer list before copying a row into the benchmark log.

Copy one row into [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]]:

| Run id | Runtime | Model | Quantization | Hardware | Prompt class | Prompt tokens | Output tokens | TTFT | Tokens/sec | Peak RAM/VRAM | Quality decision | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | smoke / known-answer / coding / RAG / long-context |  |  |  |  |  | Pass/Hold/Fail |  |

For the first run, use at least:

- a smoke prompt with exact expected output
- one known-answer prompt you can judge yourself
- one structured-output or coding prompt

Do not call the model good because it answered the smoke prompt. The smoke prompt only proves the serving path.

## Step 8: Quality And Decision

Use [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] for a pass/hold/fail decision.

| Decision | Meaning | Next action |
|---|---|---|
| Pass | Endpoint, quality, latency, memory, and safety boundary fit the target workload. | Keep this model/runtime and move to RAG/tool/deployment evidence. |
| Hold | The loop works, but one bottleneck is unresolved. | Tune one variable: model, quantization, context, sampling, prompt, or runtime. |
| Fail | The endpoint crashes, is too slow, too weak, unsafe, or not compatible enough. | Replace model/runtime or narrow the workload. |

Write one sentence explaining the bottleneck using academic terms: weight memory, KV-cache pressure, prefill, decode, quantization loss, chat-template mismatch, retrieval miss, or evaluation failure.

## Completion Gate

This evidence pack is complete when you have:

- [ ] a filled run card
- [ ] preflight evidence from the same runtime boundary that served the model
- [ ] model acquisition/provenance evidence
- [ ] model/runtime compatibility evidence
- [ ] WSL CUDA setup proof when using vLLM or SGLang from Windows
- [ ] Docker GPU container proof when using containerized vLLM, SGLang, or Open WebUI
- [ ] a successful native or OpenAI-compatible smoke response
- [ ] first response debrief row with route claim, timing interpretation, mechanism, and next action
- [ ] a route/model-id proof such as `/api/tags`, `/v1/models`, runtime UI, or server log
- [ ] one client-harness row or an explicit note that the run is smoke-test only
- [ ] first client harness runner evidence or an explicit note that the run is native-only
- [ ] first streaming timing row or an explicit note that streaming is unsupported/not required
- [ ] first benchmark-row builder output or an explicit note that the run is benchmark-pending
- [ ] one benchmark row
- [ ] one first quality probe or quality decision
- [ ] one security/logging boundary decision
- [ ] one next decision: keep, tune, replace model, replace runtime, add RAG, add tools, or write deployment memo

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Hands-On Practicum Sequence]]
- [[LLM/Study/Local LLM Windows First-Run Quickstart]]
- [[LLM/Study/Local LLM First Model Pull Gate]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM First Response Debrief Card]]
- [[LLM/Study/Local LLM First Quality Probe Suite]]
- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/Local LLM First Streaming Timing Runner]]
- [[LLM/Study/Local LLM First Benchmark Row Builder]]
- [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab]]
- [[LLM/Study/Local LLM Docker GPU Container Serving Lab]]
- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local RAG Minimal Python Harness]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]]

Current external docs checked 2026-06-15:

- [Ollama API introduction](https://docs.ollama.com/api/introduction)
- [Ollama generate endpoint](https://docs.ollama.com/api/generate)
- [Ollama usage metrics](https://docs.ollama.com/api/usage)
- [Ollama list models](https://docs.ollama.com/api/tags)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
- [LM Studio local API server](https://lmstudio.ai/docs/developer/core/server)
- [LM Studio OpenAI compatibility endpoints](https://lmstudio.ai/docs/developer/openai-compat)
- [llama.cpp HTTP server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- [llama-cpp-python OpenAI-compatible server](https://llama-cpp-python.readthedocs.io/en/latest/server/)
- [vLLM quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/)
- [vLLM OpenAI-compatible server](https://docs.vllm.ai/en/v0.18.0/serving/openai_compatible_server/)
