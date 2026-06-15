---
tags: [study, llm, inference, local-llm, commands, cookbook, windows]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM Command Cookbook

> **One-line summary** This is the copyable command layer for local LLM inference: start a local server, prove the route, call it from a client, log timing, and decide which deeper lab owns the next failure.

Use this when you already know the intended runtime and need exact commands. Use [[LLM/Study/Local LLM Windows First-Run Quickstart|Local LLM Windows First-Run Quickstart]] for the first guided Windows pass, [[LLM/Study/Local LLM Windows Runtime Install Gate|Local LLM Windows Runtime Install Gate]] before the first Ollama model pull, [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]] for pull/list/tags/show evidence, [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] for the full procedure, and [[LLM/Study/Local LLM Hands-On Practicum Sequence|Local LLM Hands-On Practicum Sequence]] for the order of evidence artifacts.

This note is a cookbook, not a model recommendation list. Replace placeholders such as `<model>`, `<served-model-id>`, `<model.gguf>`, and `<hf-model-id>` with values proven in [[LLM/Study/Local LLM Workload to Model Selection Playbook|Local LLM Workload to Model Selection Playbook]], [[LLM/Study/Local LLM Model Selection Runner|Local LLM Model Selection Runner]], [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]], and [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]].

## Command Rules

| Rule | Reason |
|---|---|
| Save outputs under one run folder | Later benchmark and capstone rows need reproducible evidence. |
| Keep the first endpoint on `127.0.0.1` or `localhost` | Local inference is still an application server with private prompts and logs; use [[LLM/Study/Local LLM Security and Privacy Runner|Local LLM Security and Privacy Runner]] before non-loopback use. |
| Change only one variable between runs | Runtime, model, quantization, prompt, sampler, and context can each explain a result. |
| Prove `/v1/models` before `/v1/chat/completions` | The served model id must match the id sent by the client. |
| Treat a smoke response as route proof only | Quality still needs [[LLM/Study/Local LLM First Quality Probe Suite]] and then [[LLM/Study/Local LLM Quality Evaluation Harness]]. |
| Put failures in the evidence log | A failed command is useful if it names the layer that failed. |

## Run Folder

```powershell
$RunRoot = Join-Path $HOME ("Documents\local-llm-runs\" + (Get-Date -Format "yyyy-MM-dd-HHmm") + "-command-cookbook")
New-Item -ItemType Directory -Force -Path $RunRoot | Out-Null
$RunRoot
```

Every command below assumes `$RunRoot` exists. Keep one folder per model/runtime comparison.

## Windows Preflight

```powershell
Get-CimInstance Win32_OperatingSystem |
  Select-Object Caption, Version, OSArchitecture, FreePhysicalMemory |
  Format-List | Tee-Object -FilePath "$RunRoot\preflight-os.txt"

Get-CimInstance Win32_ComputerSystem |
  Select-Object Manufacturer, Model, TotalPhysicalMemory |
  Format-List | Tee-Object -FilePath "$RunRoot\preflight-system.txt"

Get-CimInstance Win32_Processor |
  Select-Object Name, NumberOfCores, NumberOfLogicalProcessors |
  Format-List | Tee-Object -FilePath "$RunRoot\preflight-cpu.txt"

Get-CimInstance Win32_VideoController |
  Select-Object Name, AdapterRAM, DriverVersion |
  Format-List | Tee-Object -FilePath "$RunRoot\preflight-gpu.txt"

Get-PSDrive -PSProvider FileSystem |
  Select-Object Name, Root, Used, Free |
  Format-Table | Tee-Object -FilePath "$RunRoot\preflight-disk.txt"

if (Get-Command nvidia-smi -ErrorAction SilentlyContinue) {
  nvidia-smi | Tee-Object -FilePath "$RunRoot\nvidia-smi.txt"
} else {
  "nvidia-smi not found; record CPU-only, integrated GPU, AMD, or WSL path explicitly." |
    Tee-Object -FilePath "$RunRoot\nvidia-smi.txt"
}
```

Pass signal: the evidence says what hardware and runtime boundary the server can actually see.

## Listener Check

```powershell
Get-NetTCPConnection -State Listen |
  Where-Object { $_.LocalPort -in 11434,1234,8000,8001,8080,30000 } |
  Select-Object LocalAddress, LocalPort, OwningProcess |
  Format-Table |
  Tee-Object -FilePath "$RunRoot\listeners.txt"
```

Pass signal: the first proof is bound to loopback. If the listener is on `0.0.0.0`, stop and use [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] plus [[LLM/Study/Local LLM Security and Privacy Runner|Local LLM Security and Privacy Runner]] before exposing the server.

## Ollama Native Smoke

Use this for the fastest terminal proof.

```powershell
ollama --version
ollama ls
```

```powershell
$Model = "<ollama-model-tag>"
ollama pull $Model
ollama run $Model
```

In a second PowerShell:

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

$Response | ConvertTo-Json -Depth 10 |
  Tee-Object -FilePath "$RunRoot\ollama-native-generate.json"
```

Record:

| Field | Claim |
|---|---|
| `response` | The model generated text. |
| `total_duration` | End-to-end request time. |
| `load_duration` | Cold or warm model-load contribution. |
| `prompt_eval_count` and `prompt_eval_duration` | Prompt token count and prefill/prompt processing evidence. |
| `eval_count` and `eval_duration` | Output token count and decode evidence. |

Useful Ollama process commands:

```powershell
ollama ps
ollama stop <ollama-model-tag>
```

## Ollama OpenAI-Compatible Smoke

```powershell
Invoke-RestMethod "http://localhost:11434/api/tags" |
  ConvertTo-Json -Depth 10 |
  Tee-Object -FilePath "$RunRoot\ollama-tags.json"
```

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

$Response | ConvertTo-Json -Depth 10 |
  Tee-Object -FilePath "$RunRoot\ollama-openai-chat.json"
```

Pass signal: the same local Ollama model can be called through the native endpoint and the OpenAI-compatible endpoint, or the run explicitly chooses native-only.

## Shared OpenAI-Compatible Smoke

Use this for LM Studio, llama-cpp-python, vLLM, SGLang, or any OpenAI-compatible local server after the server is running.

```powershell
$BaseUrl = "http://localhost:<port>/v1"
$Model = "<served-model-id>"

Invoke-RestMethod "$BaseUrl/models" |
  ConvertTo-Json -Depth 10 |
  Tee-Object -FilePath "$RunRoot\models.json"
```

```powershell
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

$Response | ConvertTo-Json -Depth 10 |
  Tee-Object -FilePath "$RunRoot\openai-compatible-chat.json"
```

Common local base URLs:

| Runtime | `$BaseUrl` |
|---|---|
| Ollama OpenAI-compatible | `http://localhost:11434/v1` |
| LM Studio | `http://localhost:1234/v1` |
| llama-cpp-python server | `http://localhost:8001/v1` if launched on port `8001` |
| vLLM | `http://localhost:8000/v1` |
| SGLang | `http://localhost:30000/v1` |

## LM Studio Server Smoke

Start the server from the Developer tab, or from a terminal if the `lms` CLI is available:

```powershell
lms --help
lms server start
```

Then use the shared OpenAI-compatible smoke with:

```powershell
$BaseUrl = "http://localhost:1234/v1"
```

Pass signal: `/v1/models` returns the loaded model id, and that exact id works in `/v1/chat/completions`.

## llama-cpp-python Server Smoke

Use this when you have a GGUF file and want an OpenAI-compatible local server.

```powershell
python -m venv "$RunRoot\venv-llama-cpp"
& "$RunRoot\venv-llama-cpp\Scripts\Activate.ps1"
python -m pip install --upgrade pip
python -m pip install "llama-cpp-python[server]"
```

```powershell
python -m llama_cpp.server `
  --model "<path-to-model.gguf>" `
  --host 127.0.0.1 `
  --port 8001
```

In a second PowerShell, use the shared OpenAI-compatible smoke with:

```powershell
$BaseUrl = "http://localhost:8001/v1"
$Model = "<served-model-id-or-alias>"
```

If the model ignores roles or stop conditions, do not benchmark yet. Go to [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]] and prove the template path first.

## WSL vLLM Smoke

Use [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab|Local LLM WSL CUDA vLLM and SGLang Setup Lab]] for the full environment proof. The cookbook command is only the route proof after WSL, CUDA, Python, and model access are known.

Inside WSL/Linux:

```bash
nvidia-smi
vllm serve <hf-model-id> --host 127.0.0.1 --port 8000
```

From Windows PowerShell:

```powershell
$BaseUrl = "http://localhost:8000/v1"
$Model = "<hf-model-id>"
Invoke-RestMethod "$BaseUrl/models" |
  ConvertTo-Json -Depth 10 |
  Tee-Object -FilePath "$RunRoot\vllm-models.json"
```

Then run the shared OpenAI-compatible chat smoke.

If Windows cannot reach the WSL server, prove the failed layer before changing the model: WSL process, host binding, port forwarding, firewall, then client route.

## WSL SGLang Smoke

Use this after the WSL/CUDA/Python setup is proven.

Inside WSL/Linux:

```bash
nvidia-smi
python3 -m sglang.launch_server \
  --model-path <hf-model-id-or-local-path> \
  --host 127.0.0.1 \
  --port 30000
```

From Windows PowerShell:

```powershell
$BaseUrl = "http://localhost:30000/v1"
$Model = "<hf-model-id-or-served-model-id>"
Invoke-RestMethod "$BaseUrl/models" |
  ConvertTo-Json -Depth 10 |
  Tee-Object -FilePath "$RunRoot\sglang-models.json"
```

Then run the shared OpenAI-compatible chat smoke.

## Docker Host Proof

Use [[LLM/Study/Local LLM Docker GPU Container Serving Lab|Local LLM Docker GPU Container Serving Lab]] for exact image, cache mount, GPU runtime, and Compose evidence. The cookbook host proof is:

```powershell
docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Ports}}\t{{.Status}}" |
  Tee-Object -FilePath "$RunRoot\docker-ps.txt"

docker logs --tail 120 <container-name> |
  Tee-Object -FilePath "$RunRoot\docker-logs-tail.txt"
```

Then call the published loopback port:

```powershell
$BaseUrl = "http://localhost:<published-port>/v1"
Invoke-RestMethod "$BaseUrl/models" |
  ConvertTo-Json -Depth 10 |
  Tee-Object -FilePath "$RunRoot\docker-models.json"
```

Pass signal: the container, image tag, mount path, GPU visibility, published port, `/v1/models`, and chat smoke are all recorded in the same run folder.

## Python Client Smoke

Use this when you need proof that a normal OpenAI-compatible client can call the local endpoint.

```powershell
python -m venv "$RunRoot\venv-client"
& "$RunRoot\venv-client\Scripts\Activate.ps1"
python -m pip install --upgrade pip
python -m pip install openai
```

```powershell
@'
import json
import os
import time
from openai import OpenAI

base_url = os.environ["LOCAL_LLM_BASE_URL"]
model = os.environ["LOCAL_LLM_MODEL"]

client = OpenAI(base_url=base_url, api_key="local")

started = time.perf_counter()
response = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "Reply with exactly: local llm ok"}],
    temperature=0,
    max_tokens=16,
)
elapsed = time.perf_counter() - started

print(json.dumps({
    "base_url": base_url,
    "model": model,
    "elapsed_seconds": elapsed,
    "content": response.choices[0].message.content,
    "finish_reason": response.choices[0].finish_reason,
}, indent=2))
'@ | Set-Content -Encoding UTF8 "$RunRoot\chat_smoke.py"

$env:LOCAL_LLM_BASE_URL = "http://localhost:<port>/v1"
$env:LOCAL_LLM_MODEL = "<served-model-id>"
python "$RunRoot\chat_smoke.py" |
  Tee-Object -FilePath "$RunRoot\python-client-chat.json"
```

Pass signal: the same endpoint works through a reusable client, not only through a one-off REST call.

## Streaming Smoke

Use streaming only after the non-streaming route works.

```powershell
@'
import json
import os
import time
from openai import OpenAI

client = OpenAI(base_url=os.environ["LOCAL_LLM_BASE_URL"], api_key="local")
model = os.environ["LOCAL_LLM_MODEL"]

started = time.perf_counter()
first_token_at = None
chunks = []

stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "Count from one to five."}],
    temperature=0,
    max_tokens=32,
    stream=True,
)

for event in stream:
    delta = event.choices[0].delta.content or ""
    if delta and first_token_at is None:
        first_token_at = time.perf_counter()
    chunks.append(delta)

finished = time.perf_counter()

print(json.dumps({
    "model": model,
    "ttft_seconds": None if first_token_at is None else first_token_at - started,
    "elapsed_seconds": finished - started,
    "text": "".join(chunks),
}, indent=2))
'@ | Set-Content -Encoding UTF8 "$RunRoot\stream_smoke.py"

$env:LOCAL_LLM_BASE_URL = "http://localhost:<port>/v1"
$env:LOCAL_LLM_MODEL = "<served-model-id>"
python "$RunRoot\stream_smoke.py" |
  Tee-Object -FilePath "$RunRoot\python-client-stream.json"
```

Record unsupported streaming as evidence too. A runtime can still be usable if the workload only needs non-streaming responses.

## Minimal Benchmark Row

Use this after route proof and before runtime comparison.

```powershell
$BenchmarkPath = "$RunRoot\benchmark.csv"
$Runtime = "<runtime>"
$Model = "<served-model-id>"
$Quantization = "<quantization-or-unknown>"
$BaseUrl = "http://localhost:<port>/v1"

$Body = @{
  model = $Model
  messages = @(
    @{ role = "user"; content = "Write three bullet points about why KV cache matters." }
  )
  temperature = 0
  max_tokens = 128
} | ConvertTo-Json -Depth 6

$Elapsed = Measure-Command {
  $Response = Invoke-RestMethod `
    -Uri "$BaseUrl/chat/completions" `
    -Method Post `
    -ContentType "application/json" `
    -Headers @{ Authorization = "Bearer local" } `
    -Body $Body
}

[pscustomobject]@{
  timestamp = (Get-Date).ToString("s")
  runtime = $Runtime
  model = $Model
  quantization = $Quantization
  base_url = $BaseUrl
  elapsed_ms = [math]::Round($Elapsed.TotalMilliseconds, 0)
  response_file = "benchmark-response.json"
} | Export-Csv -Path $BenchmarkPath -NoTypeInformation -Append

$Response | ConvertTo-Json -Depth 10 |
  Tee-Object -FilePath "$RunRoot\benchmark-response.json"
```

Then copy the row into [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] with any runtime-native token counts, TTFT, tokens/sec, RAM/VRAM, prompt class, and quality notes.

## Teardown Checklist

| Runtime | Stop or cleanup proof |
|---|---|
| Ollama | `ollama ps`, then `ollama stop <model>` if you want to unload the model. |
| LM Studio | Stop the server in the Developer tab or the CLI surface you used to start it. |
| llama-cpp-python | Stop the terminal process, then rerun the listener check. |
| vLLM/SGLang in WSL | Stop the WSL/Linux server process, then rerun Windows listener and `/v1/models` checks. |
| Docker | `docker ps`, stop the named container if this was a disposable run, then rerun listener check. |

Save the post-stop listener check:

```powershell
Get-NetTCPConnection -State Listen |
  Where-Object { $_.LocalPort -in 11434,1234,8000,8001,8080,30000 } |
  Select-Object LocalAddress, LocalPort, OwningProcess |
  Format-Table |
  Tee-Object -FilePath "$RunRoot\listeners-after-stop.txt"
```

## Diagnostic Commands

| Symptom | Command | Next route |
|---|---|---|
| Connection refused | `Get-NetTCPConnection -State Listen` | [[LLM/Study/Local LLM Troubleshooting Decision Tree]] |
| Wrong model id | `Invoke-RestMethod "$BaseUrl/models"` or `ollama list` | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]] or [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]] |
| Route 404 | Check `$BaseUrl` includes `/v1` and route is `/chat/completions` | [[LLM/Study/Local LLM Serving Runbook]] |
| Startup OOM | `nvidia-smi`, Task Manager, runtime logs | [[LLM/Study/Local LLM Model and Hardware Sizing Guide]] |
| Long-prompt OOM | Count prompt/history/RAG/tool tokens | [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]] or [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]] |
| Slow first token | Compare prompt tokens, retrieved context, queue, and prefix reuse | [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]] |
| Shared use is slow or unstable | Run a fixed concurrency ladder and compare p95 latency, throughput, errors, and saturation | [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner]] |
| Repeated-prefix prompt is still slow | Run shared-prefix and changed-prefix controls with TTFT or metrics | [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner]] |
| Speculative decoding is slower or unproven | Compare no-spec and spec-enabled profiles with fixed prompts and metrics | [[LLM/Study/Local LLM Speculative Decoding Runner]] |
| Service state, metrics, slots, logs, or resource pressure are unclear | Run a no-generation observability snapshot before changing the service | [[LLM/Study/Local LLM Observability and Operations Runner]] |
| Restart, upgrade, model-cache move, UI update, or rollback is planned | Validate the lifecycle manifest, baseline artifacts, backup, and rollback target before changing anything | [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner]] |
| Slow later tokens | Compare model size, quantization, offload, backend, and memory bandwidth | [[LLM/Study/Local LLM Quantization and GPU Offload Lab]] |
| Streaming broken | Run non-streaming smoke and record unsupported or malformed streaming | [[LLM/Study/Local LLM First Streaming Timing Runner]] |
| Output ignores roles | Verify tokenizer, chat template, EOS, and stop policy | [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]] |
| Tool call wrong or unsafe | Validate schema, policy, tool-choice, and result injection | [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]] or [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]] |

## Evidence Destinations

| Evidence | Store or route to |
|---|---|
| Preflight snapshot | [[LLM/Study/Local LLM Environment Preflight Lab]] |
| First Ollama model pull | [[LLM/Study/Local LLM First Model Pull Gate]] |
| First runtime health snapshot | [[LLM/Study/Local LLM First Runtime Health Snapshot]] |
| First smoke request runner | [[LLM/Study/Local LLM First Smoke Request Runner]] |
| First response debrief | [[LLM/Study/Local LLM First Response Debrief Card]] |
| First response debrief runner | [[LLM/Study/Local LLM First Response Debrief Runner]] |
| Request lifecycle runner | [[LLM/Study/LLM Inference Request Lifecycle Runner]] |
| First quality probe | [[LLM/Study/Local LLM First Quality Probe Suite]] |
| First quality probe runner | [[LLM/Study/Local LLM First Quality Probe Runner]] |
| First raw response | [[LLM/Study/Local LLM First Inference Evidence Pack]] |
| Model selection runner | [[LLM/Study/Local LLM Model Selection Runner]] |
| Startup command and route | [[LLM/Study/Local LLM Serving Runbook]] |
| `/v1/models`, non-streaming, streaming, errors | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]] or [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]] |
| First reusable client run | [[LLM/Study/Local LLM First Client Harness Runner]] |
| First streaming timing run | [[LLM/Study/Local LLM First Streaming Timing Runner]] |
| First benchmark-row builder output | [[LLM/Study/Local LLM First Benchmark Row Builder]] |
| Sampler, seed, stop, and cap controls | [[LLM/Study/Decoding and Sampling Controls Runner]] |
| Context, history, RAG, tool, reserve, and margin budget | [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]] |
| Concurrency ladder, saturation, and batch-throughput proof | [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner]] |
| Repeated-prefix, changed-prefix, TTFT, and prompt-cache proof | [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner]] |
| No-spec/spec, decode-rate, accepted-token signal, and quality proof | [[LLM/Study/Local LLM Speculative Decoding Runner]] |
| Route, loaded-model, metrics, slots, resource, log-tail, and privacy proof | [[LLM/Study/Local LLM Observability and Operations Runner]] |
| Lifecycle manifest, baseline artifacts, backup, rollback, and post-change decision proof | [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner]] |
| Structured JSON, tool-call, result-injection, and denial proof | [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]] |
| Python wrapper output | [[LLM/Study/Local LLM Client Harness Lab]] |
| Timing and throughput row | [[LLM/Study/Local LLM Inference Benchmark Log]] |
| Quality pass/hold/fail | [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| Security boundary and logs | [[LLM/Study/Local LLM Security and Privacy Runbook]] |
| Failure row | [[LLM/Study/Local LLM Troubleshooting Decision Tree]] |
| Capstone proof | [[LLM/Study/LLM Mastery Capstone Workbook]] |

## Completion Gate

This cookbook pass is complete when you have:

- [ ] one run folder
- [ ] preflight files
- [ ] listener proof
- [ ] model list proof
- [ ] one native or OpenAI-compatible smoke response
- [ ] one client or REST call saved
- [ ] one benchmark row or explicit benchmark-pending note
- [ ] one next action tied to a specific lab

## References

Internal routes:

- [[LLM/Study/Local LLM Windows First-Run Quickstart]]
- [[LLM/Study/Local LLM Windows Runtime Install Gate]]
- [[LLM/Study/Local LLM First Model Pull Gate]]
- [[LLM/Study/Local LLM First Runtime Health Snapshot]]
- [[LLM/Study/Local LLM First Smoke Request Runner]]
- [[LLM/Study/Local LLM First Response Debrief Card]]
- [[LLM/Study/Local LLM First Response Debrief Runner]]
- [[LLM/Study/LLM Inference Request Lifecycle Runner]]
- [[LLM/Study/Local LLM First Quality Probe Suite]]
- [[LLM/Study/Local LLM First Quality Probe Runner]]
- [[LLM/Study/Local LLM Model Selection Runner]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Hands-On Practicum Sequence]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]]
- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/Local LLM First Streaming Timing Runner]]
- [[LLM/Study/Local LLM First Benchmark Row Builder]]
- [[LLM/Study/Decoding and Sampling Controls Runner]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner]]
- [[LLM/Study/Local LLM Speculative Decoding Runner]]
- [[LLM/Study/Local LLM Observability and Operations Runner]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab]]
- [[LLM/Study/Local LLM Docker GPU Container Serving Lab]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Security and Privacy Runner]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]

External/current docs checked 2026-06-15:

- [Ollama CLI reference](https://docs.ollama.com/cli)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
- [LM Studio local API server](https://lmstudio.ai/docs/developer/core/server)
- [LM Studio OpenAI compatibility](https://lmstudio.ai/docs/developer/openai-compat)
- [llama-cpp-python server](https://llama-cpp-python.readthedocs.io/en/latest/server/)
- [vLLM quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/)
- [SGLang quickstart](https://docs.sglang.io/docs/get-started/quickstart)
