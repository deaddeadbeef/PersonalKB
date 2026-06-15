---
tags: [study, llm, inference, local-llm, windows, quickstart]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM Windows First-Run Quickstart

> **One-line summary** On Windows, the fastest credible first local LLM proof is: capture preflight evidence, run a small model with Ollama or LM Studio, call the loopback HTTP API from PowerShell, save the response and timing fields, then decide whether to keep, tune, or switch runtime.

Use this note when you want the shortest path from "I have Windows" to "I have a local model answering through an API." For this workstation, open [[LLM/Study/Local LLM First Run Readiness Snapshot|Local LLM First Run Readiness Snapshot]] first so runtime, GPU, listener, and first-model assumptions are explicit before installing or pulling anything. If you only need the copyable command layer, use [[LLM/Study/Local LLM Command Cookbook|Local LLM Command Cookbook]]. After the first response works, expand the evidence with [[LLM/Study/Local LLM First Inference Evidence Pack|Local LLM First Inference Evidence Pack]], [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]], and [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]].

## Runtime Choice For The First Hour

| Situation | Start here | Why |
|---|---|---|
| You want the fastest Windows-native terminal proof | Ollama | Native Windows installer, simple model pull/run loop, native API on `localhost:11434`. |
| You want GUI model browsing plus OpenAI-style client tests | LM Studio | Windows desktop app, Developer server, OpenAI-compatible base URL commonly on `localhost:1234/v1`. |
| You already have a GGUF file or need CPU/mixed-offload control | llama.cpp or llama-cpp-python | More control, but more setup and compatibility work. |
| You want production-style GPU serving | [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab|vLLM or SGLang under WSL/Linux/server]] | Treat this as a second pass; prove WSL 2, CUDA visibility, Python env, loopback endpoint, `/v1/models`, and Windows client routing before benchmarking. |

Default first path: **Ollama on loopback**. Use LM Studio instead if you prefer a GUI or need to test a desktop app against an OpenAI-compatible endpoint.

## Step 0: Create A Run Folder

```powershell
$RunRoot = Join-Path $HOME ("Documents\local-llm-runs\" + (Get-Date -Format "yyyy-MM-dd-HHmm") + "-windows-first-run")
New-Item -ItemType Directory -Force -Path $RunRoot | Out-Null
$RunRoot
```

Save every command output from this quickstart in that folder. Later, link the folder or copied evidence rows from [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]].

## Step 1: Capture Windows Preflight

```powershell
Get-CimInstance Win32_OperatingSystem |
  Select-Object Caption, Version, OSArchitecture, FreePhysicalMemory |
  Format-List | Out-File "$RunRoot\preflight.txt"

Get-CimInstance Win32_ComputerSystem |
  Select-Object Manufacturer, Model, TotalPhysicalMemory |
  Format-List | Out-File "$RunRoot\preflight.txt" -Append

Get-CimInstance Win32_Processor |
  Select-Object Name, NumberOfCores, NumberOfLogicalProcessors |
  Format-List | Out-File "$RunRoot\preflight.txt" -Append

Get-CimInstance Win32_VideoController |
  Select-Object Name, AdapterRAM, DriverVersion |
  Format-List | Out-File "$RunRoot\preflight.txt" -Append

Get-PSDrive -PSProvider FileSystem |
  Select-Object Name, Root, Used, Free |
  Format-Table | Out-File "$RunRoot\disk.txt"

if (Get-Command nvidia-smi -ErrorAction SilentlyContinue) {
  nvidia-smi | Out-File "$RunRoot\nvidia-smi.txt"
} else {
  "nvidia-smi not found; record CPU-only or non-NVIDIA GPU path explicitly." | Out-File "$RunRoot\nvidia-smi.txt"
}
```

Pass signal: the run record says whether this is Windows-native, WSL, Docker, or remote Linux, and whether the runtime can see the GPU you expect.

## Step 2A: Ollama Fast Path

Install or update Ollama from the official Windows installer or script. If you use the script path, read the source/risk posture first just as you would for any installer:

```powershell
irm https://ollama.com/install.ps1 | iex
```

Then open a new PowerShell and verify the CLI:

```powershell
ollama --version
ollama list
```

Pull a small instruct model that fits your hardware. Copy the exact model tag from the Ollama library or your local `ollama list` output.

```powershell
$Model = "<ollama-model-tag>"
ollama pull $Model
ollama run $Model
```

Use a tiny model for the first proof if you are unsure about RAM/VRAM. A small model that responds is better first evidence than a larger model that fails before the serving path is proven.

## Step 3A: Ollama Native API Smoke Test

Run this in a second PowerShell while Ollama is available:

```powershell
$Model = "<ollama-model-tag>"
$Body = @{
  model = $Model
  prompt = "Reply with exactly: local llm ok"
  stream = $false
} | ConvertTo-Json -Depth 5

$Response = Invoke-RestMethod `
  -Uri "http://localhost:11434/api/generate" `
  -Method Post `
  -ContentType "application/json" `
  -Body $Body

$Response | ConvertTo-Json -Depth 10 | Tee-Object -FilePath "$RunRoot\ollama-generate.json"
```

Record these fields in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]]:

| Field | Why |
|---|---|
| `response` | Proves generation happened. |
| `total_duration` | End-to-end generation time from Ollama. |
| `load_duration` | Separates cold load from generation. |
| `prompt_eval_count` | Prompt tokens processed. |
| `prompt_eval_duration` | Prefill/prompt processing time. |
| `eval_count` | Output tokens generated. |
| `eval_duration` | Decode time for output tokens. |

## Step 4A: Ollama Model List And OpenAI-Compatible Test

First prove the model registry:

```powershell
Invoke-RestMethod "http://localhost:11434/api/tags" |
  ConvertTo-Json -Depth 10 |
  Tee-Object -FilePath "$RunRoot\ollama-tags.json"
```

Then test the OpenAI-compatible route:

```powershell
$BaseUrl = "http://localhost:11434/v1"
$Model = "<ollama-model-tag>"
$Body = @{
  model = $Model
  messages = @(
    @{ role = "user"; content = "Reply with exactly: local llm ok" }
  )
  temperature = 0
  max_tokens = 16
} | ConvertTo-Json -Depth 6

$Response = Invoke-RestMethod `
  -Uri "$BaseUrl/chat/completions" `
  -Method Post `
  -ContentType "application/json" `
  -Headers @{ Authorization = "Bearer local" } `
  -Body $Body

$Response | ConvertTo-Json -Depth 10 | Tee-Object -FilePath "$RunRoot\ollama-openai-chat.json"
```

Pass signal: the native endpoint and the OpenAI-compatible endpoint both answer on loopback, or you explicitly decide to use only the native API.

## Step 2B: LM Studio GUI/API Path

Use this path when you want a desktop model browser and a local OpenAI-compatible server.

1. Install LM Studio for Windows.
2. Download a small model from the Discover tab.
3. Go to the Developer or Local Server area.
4. Start the server.
5. Keep it on localhost for the first run.

If the `lms` CLI is available, the server can also be started from a terminal:

```powershell
lms --help
lms server start
```

List served models:

```powershell
$BaseUrl = "http://localhost:1234/v1"
Invoke-RestMethod "$BaseUrl/models" |
  ConvertTo-Json -Depth 10 |
  Tee-Object -FilePath "$RunRoot\lmstudio-models.json"
```

Call the chat endpoint:

```powershell
$Model = "<served-model-id-from-models-list>"
$Body = @{
  model = $Model
  messages = @(
    @{ role = "user"; content = "Reply with exactly: local llm ok" }
  )
  temperature = 0
  max_tokens = 16
} | ConvertTo-Json -Depth 6

$Response = Invoke-RestMethod `
  -Uri "$BaseUrl/chat/completions" `
  -Method Post `
  -ContentType "application/json" `
  -Headers @{ Authorization = "Bearer local" } `
  -Body $Body

$Response | ConvertTo-Json -Depth 10 | Tee-Object -FilePath "$RunRoot\lmstudio-openai-chat.json"
```

Pass signal: the model id from `/v1/models` is the same id used in `/v1/chat/completions`.

## Step 5: Listener And Boundary Check

Keep the first endpoint private:

```powershell
Get-NetTCPConnection -State Listen |
  Where-Object { $_.LocalPort -in 11434,1234,8000,8001,8080,30000 } |
  Select-Object LocalAddress, LocalPort, OwningProcess |
  Format-Table |
  Tee-Object -FilePath "$RunRoot\listeners.txt"
```

Pass signal: the first run uses `127.0.0.1` or `localhost`. Do not enable LAN access, bind to `0.0.0.0`, or tunnel the endpoint until [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] has a reason, auth boundary, firewall decision, and logging policy.

## Step 6: First Quality Mini-Suite

Run three prompts before trusting the model:

| Prompt class | Prompt | Pass signal |
|---|---|---|
| Smoke | `Reply with exactly: local llm ok` | Exact response or explainable minor formatting difference. |
| Known answer | A fact you personally know well. | Correct, no unsupported invention. |
| Structured | `Return JSON with keys status and next_action.` | Parseable JSON or a recorded structured-output failure. |

If the model passes smoke but fails the known-answer or structured prompt, the endpoint works but the model/workload choice is not proven.

## Step 7: Write The First Decision

Copy this decision row into the evidence pack:

| Field | Value |
|---|---|
| Runtime | Ollama / LM Studio / other |
| Boundary | Windows native / WSL / Docker / remote |
| Base URL |  |
| Model id |  |
| Smoke response file |  |
| Model list file |  |
| Prompt tokens / output tokens |  |
| Timing fields |  |
| Listener proof |  |
| Quality mini-suite result | Pass / Hold / Fail |
| Next action | keep / tune sampler / try stronger model / switch runtime / add RAG / stop |

Use [[LLM/Study/LLM Mechanism-to-Inference Bridge Map|LLM Mechanism-to-Inference Bridge Map]] to name the mechanism behind the next action: tokenization, chat template, KV cache, quantization, sampling, RAG, tool boundary, evaluation, or deployment.

## When To Leave Windows Native

| Need | Move to | Why |
|---|---|---|
| Exact GGUF file control or CPU edge testing | llama.cpp / llama-cpp-python | More knobs for quantized local files and CPU/GPU offload. |
| GPU serving with batching and production-style scheduling | [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab|WSL/Linux/server with vLLM or SGLang]] | Native Windows is not the default support path for vLLM; use the WSL CUDA lab before runtime comparison. |
| Private chat UI over a local provider | Open WebUI after provider proof | The provider endpoint should work before debugging a UI. |
| RAG over private documents | Local RAG harness after endpoint proof | Retrieval adds corpus, chunking, embedding, citation, and prompt-injection risks. |

Do not move to a more complex runtime until the first loopback API proof is saved. Complexity is justified when it addresses a named bottleneck.

## Troubleshooting Order

| Symptom | First check |
|---|---|
| `Invoke-RestMethod` connection refused | Server process, listener, host, and port. |
| `/v1/chat/completions` returns 404 | Missing `/v1`, wrong route, or runtime only exposing native API. |
| Model id not found | Run `/api/tags`, `/v1/models`, or copy exact id from the runtime UI. |
| Startup OOM | Weight memory, quantization, free RAM/VRAM, GPU offload. |
| OOM only on long prompts | KV cache and context budget. |
| First token slow | Cold load, long prefill, retrieved context, queueing. |
| Later tokens slow | Decode memory bandwidth, model size, quantization/backend, CPU/GPU path. |
| Output ignores role/instructions | Chat template, tokenizer, stop policy, wrong base model. |

Use [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]] before changing more than one variable.

## Completion Gate

This quickstart is complete when you have:

- [ ] `preflight.txt`, `disk.txt`, and optional `nvidia-smi.txt`
- [ ] model id copied from `ollama list`, `/api/tags`, LM Studio UI, or `/v1/models`
- [ ] one native or OpenAI-compatible smoke response saved as JSON
- [ ] listener/boundary proof saved
- [ ] one quality mini-suite decision
- [ ] one benchmark or evidence-pack row with timing fields
- [ ] one next action that names the mechanism behind it

## References

Internal routes:

- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM Command Cookbook]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]

External/current docs checked 2026-06-15:

- [Ollama Windows documentation](https://docs.ollama.com/windows)
- [Ollama Windows download](https://ollama.com/download/windows)
- [Ollama quickstart](https://docs.ollama.com/quickstart)
- [Ollama CLI reference](https://docs.ollama.com/cli)
- [Ollama usage metrics](https://docs.ollama.com/api/usage)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
- [LM Studio app basics](https://lmstudio.ai/docs/app/basics)
- [LM Studio local API server](https://lmstudio.ai/docs/developer/core/server)
- [LM Studio OpenAI compatibility](https://lmstudio.ai/docs/developer/openai-compat)
- [LM Studio CLI](https://lmstudio.ai/docs/cli)
- [llama.cpp build docs](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md)
- [llama.cpp HTTP server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- [llama-cpp-python server](https://llama-cpp-python.readthedocs.io/en/latest/server/)
- [vLLM GPU installation note](https://docs.vllm.ai/en/stable/getting_started/installation/gpu/)
