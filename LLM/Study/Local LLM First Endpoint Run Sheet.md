---
tags: [study, llm, inference, local-llm, ollama, windows, run-sheet, evidence]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM First Endpoint Run Sheet

> **One-line summary** This is the fill-in execution sheet for the first local LLM endpoint: install or open the runtime, pull one small model, prove the native and OpenAI-compatible loopback routes, save the evidence files, and write the pass/hold/fail decision.

Use this after [[LLM/Study/Local LLM First Run Readiness Snapshot|Local LLM First Run Readiness Snapshot]] and while executing [[LLM/Study/Local LLM Windows First-Run Quickstart|Local LLM Windows First-Run Quickstart]]. The readiness snapshot says the current machine state. The quickstart explains the full path. Use [[LLM/Study/Local LLM First Run Command Plan Runner|Local LLM First Run Command Plan Runner]] first when you want the exact PowerShell sequence, run folder, and evidence filenames generated before execution. This run sheet is the one-session checklist that turns the path into files you can link from [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]].

This sheet is not endpoint proof until the evidence files exist. A checked box without a saved command output does not count. Before the first pull, use [[LLM/Study/Local LLM Windows Model Store and Cache Plan|Local LLM Windows Model Store and Cache Plan]], [[LLM/Study/Local LLM Model Store Readiness Snapshot|Local LLM Model Store Readiness Snapshot]], and [[LLM/Study/Local LLM Windows Runtime Install Gate|Local LLM Windows Runtime Install Gate]] to decide where model bytes live and prove the runtime install. Then use [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]] to capture the selected model tag, pull output, list/tags/show metadata, and pass/hold/fail handoff. Use [[LLM/Study/Local LLM First Runtime Health Runner|Local LLM First Runtime Health Runner]] or [[LLM/Study/Local LLM First Runtime Health Snapshot|Local LLM First Runtime Health Snapshot]] before endpoint smoke testing when you want no-generation proof that the listener and model-list routes are ready. Use [[LLM/Study/Local LLM First Smoke Request Runner|Local LLM First Smoke Request Runner]] when you want the native and OpenAI-compatible smoke requests saved by one standard runner. Use [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner|Local LLM First Endpoint Evidence Audit Runner]] after response debrief to check whether the run folder is complete enough to promote.

## Run Contract

| Field | Value |
|---|---|
| Run date |  |
| Run folder |  |
| Runtime | Ollama on Windows |
| First model | `qwen3.5:4b` from [[LLM/Study/Local LLM First Model Candidate Ladder|Local LLM First Model Candidate Ladder]] unless the model page or local constraints force a smaller tag |
| Storage snapshot | [[LLM/Study/Local LLM Model Store Readiness Snapshot]] |
| Runtime install gate | [[LLM/Study/Local LLM Windows Runtime Install Gate]] |
| Command plan | [[LLM/Study/Local LLM First Run Command Plan Runner]] |
| Model pull gate | [[LLM/Study/Local LLM First Model Pull Gate]] |
| Runtime health snapshot | [[LLM/Study/Local LLM First Runtime Health Snapshot]] |
| Runtime health runner | [[LLM/Study/Local LLM First Runtime Health Runner]] |
| Smoke request runner | [[LLM/Study/Local LLM First Smoke Request Runner]] |
| Endpoint evidence audit | [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner]] |
| Model store decision | default / custom `OLLAMA_MODELS` / hold |
| Native base URL | `http://localhost:11434` |
| OpenAI-compatible base URL | `http://localhost:11434/v1` |
| Security boundary | loopback only |
| Smoke prompt | `Reply with exactly: local llm ok` |
| Decision target | debrief / keep / tune / replace runtime / replace model / stop |

## Step 0: Create Evidence Folder

Run this first. Do not install, pull, or serve before the folder exists.

```powershell
$RunRoot = Join-Path $HOME ("Documents\local-llm-runs\" + (Get-Date -Format "yyyy-MM-dd-HHmm") + "-first-endpoint")
New-Item -ItemType Directory -Force -Path $RunRoot | Out-Null
$RunRoot | Tee-Object -FilePath "$RunRoot\run-root.txt"
```

Save a short run card:

```powershell
@"
date=$(Get-Date -Format o)
runtime=Ollama on Windows
model=qwen3.5:4b
storage_snapshot=Local LLM Model Store Readiness Snapshot
runtime_install_gate=Local LLM Windows Runtime Install Gate
runtime_health_snapshot=Local LLM First Runtime Health Snapshot
runtime_health_runner=Local LLM First Runtime Health Runner
smoke_request_runner=Local LLM First Smoke Request Runner
endpoint_evidence_audit=Local LLM First Endpoint Evidence Audit Runner
native_base_url=http://localhost:11434
openai_base_url=http://localhost:11434/v1
security_boundary=loopback only
model_store_decision=<default-or-custom-path-or-hold>
"@ | Set-Content "$RunRoot\run-card.txt"
```

Pass signal: `$RunRoot` exists and contains `run-root.txt` and `run-card.txt`.

## Step 1: Capture Pre-Install Machine State

```powershell
Get-CimInstance Win32_OperatingSystem |
  Select-Object Caption, Version, OSArchitecture, FreePhysicalMemory |
  Format-List | Tee-Object -FilePath "$RunRoot\preinstall-os.txt"

Get-CimInstance Win32_ComputerSystem |
  Select-Object Manufacturer, Model, TotalPhysicalMemory |
  Format-List | Tee-Object -FilePath "$RunRoot\preinstall-system.txt"

Get-CimInstance Win32_Processor |
  Select-Object Name, NumberOfCores, NumberOfLogicalProcessors |
  Format-List | Tee-Object -FilePath "$RunRoot\preinstall-cpu.txt"

Get-CimInstance Win32_VideoController |
  Select-Object Name, AdapterRAM, DriverVersion |
  Format-List | Tee-Object -FilePath "$RunRoot\preinstall-gpu.txt"

if (Get-Command nvidia-smi -ErrorAction SilentlyContinue) {
  nvidia-smi | Tee-Object -FilePath "$RunRoot\nvidia-smi-before.txt"
} else {
  "nvidia-smi not found" | Tee-Object -FilePath "$RunRoot\nvidia-smi-before.txt"
}
```

Record whether a runtime is already available:

```powershell
if (Get-Command ollama -ErrorAction SilentlyContinue) {
  ollama --version | Tee-Object -FilePath "$RunRoot\ollama-version-before.txt"
  ollama list | Tee-Object -FilePath "$RunRoot\ollama-list-before.txt"
} else {
  "ollama not found" | Tee-Object -FilePath "$RunRoot\ollama-version-before.txt"
}
```

Pass signal: this proves whether the run starts from a clean install state or an existing runtime state.

## Step 2: Install Or Open Ollama

Choose one path and save which path you used.

Use [[LLM/Study/Local LLM Windows Runtime Install Gate|Local LLM Windows Runtime Install Gate]] for the full install/PATH/env/listener proof. Do not pull a model until that gate is pass.

| Path | When | Evidence |
|---|---|---|
| Windows installer | Preferred when you want the GUI/tray app and normal PATH setup. | installer source and version after install |
| PowerShell installer | Fast terminal path from the official download page. | command source and version after install |
| Existing install | Use only if Step 1 found `ollama`. | existing version and model list |

PowerShell installer path:

```powershell
"installer_command=irm https://ollama.com/install.ps1 | iex" |
  Tee-Object -FilePath "$RunRoot\installer-choice.txt"

irm https://ollama.com/install.ps1 | iex
```

Open a new PowerShell after installation, then return to this run folder:

```powershell
$RunRoot = "<paste-run-folder-path>"
ollama --version | Tee-Object -FilePath "$RunRoot\ollama-version-after.txt"
ollama list | Tee-Object -FilePath "$RunRoot\ollama-list-after-install.txt"
```

Pass signal: `ollama --version` works from a new PowerShell. If it does not, the failure owner is install/PATH, not model quality.

## Step 3: Pull One First Model

Use the smallest useful model first. The current recommended first tag for this machine is `qwen3.5:4b`; verify it against [[LLM/Study/Local LLM First Model Candidate Ladder|Local LLM First Model Candidate Ladder]] and [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]] before pulling. If `model_store_decision` is still `hold`, complete [[LLM/Study/Local LLM Windows Model Store and Cache Plan|Local LLM Windows Model Store and Cache Plan]] and copy the decision card from [[LLM/Study/Local LLM Model Store Readiness Snapshot|Local LLM Model Store Readiness Snapshot]] before running `ollama pull`.

```powershell
$RunRoot = "<paste-run-folder-path>"
$Model = "qwen3.5:4b"
$Model | Tee-Object -FilePath "$RunRoot\model-tag.txt"
ollama pull $Model | Tee-Object -FilePath "$RunRoot\ollama-pull.txt"
ollama list | Tee-Object -FilePath "$RunRoot\ollama-list-after-pull.txt"
```

Pass signal: `ollama list` shows the model tag or an equivalent resolved local tag.

Hold signal: pull fails, disk fills, model tag is unavailable, or the model is much larger than expected. Go to [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]] before changing multiple variables. If the failure will affect later benchmark, quality, operations, or deployment evidence, save it with [[LLM/Study/Local LLM Failure Triage Runner|Local LLM Failure Triage Runner]].

## Step 4: Prove Listener Boundary

```powershell
$Ports = 11434,1234,8000,8001,8080,30000
Get-NetTCPConnection -State Listen -ErrorAction SilentlyContinue |
  Where-Object { $_.LocalPort -in $Ports } |
  Select-Object LocalAddress, LocalPort, OwningProcess |
  Format-Table |
  Tee-Object -FilePath "$RunRoot\listeners-before-smoke.txt"
```

Pass signal: Ollama is reachable on localhost or loopback. If the listener is exposed on `0.0.0.0`, stop and use [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]].

## Step 4.5: Capture No-Inference Runtime Health

Use [[LLM/Study/Local LLM First Runtime Health Runner|Local LLM First Runtime Health Runner]] before the first smoke request if you need repeatable pass/hold/fail server-state evidence. Use [[LLM/Study/Local LLM First Runtime Health Snapshot|Local LLM First Runtime Health Snapshot]] when you only need the compact snapshot. Save the health JSON and Markdown inside this run folder.

Pass signal: the health snapshot names the native base URL, OpenAI-compatible base URL, expected model, installed model ids, loaded model ids or idle state, OpenAI-compatible model ids, missing layer, and next action.

Hold signal: the listener exists but `/api/tags`, `/api/ps`, or `/v1/models` disagrees with the selected model. Diagnose runtime route or model-id mismatch before sending a generation request.

## Step 4.75: Optional Standard Smoke Runner

Use [[LLM/Study/Local LLM First Smoke Request Runner|Local LLM First Smoke Request Runner]] if you want Steps 5 and 6 captured by one standard-library Python script. The runner saves native and OpenAI-compatible request files, response files, extracted output text, summary JSON/Markdown, and a JSONL row.

Pass signal: the runner summary says both enabled routes are `pass`, the expected text matches, and the next action is response debrief.

## Step 5: Native Ollama Smoke

```powershell
$RunRoot = "<paste-run-folder-path>"
$Model = Get-Content "$RunRoot\model-tag.txt"
$Body = @{
  model = $Model
  prompt = "Reply with exactly: local llm ok"
  stream = $false
} | ConvertTo-Json -Depth 5

$Body | Tee-Object -FilePath "$RunRoot\ollama-native-request.json"

$Response = Invoke-RestMethod `
  -Uri "http://localhost:11434/api/generate" `
  -Method Post `
  -ContentType "application/json" `
  -Body $Body

$Response | ConvertTo-Json -Depth 10 |
  Tee-Object -FilePath "$RunRoot\ollama-native-response.json"
```

Pass signal: `ollama-native-response.json` contains a generated response plus timing fields such as total duration, prompt-eval count, and eval count.

Hold signal: the route fails, hangs, returns an error body, or produces no timing fields. Save the error and diagnose the route/runtime layer before changing the model.

## Step 6: OpenAI-Compatible Smoke

```powershell
$RunRoot = "<paste-run-folder-path>"
$BaseUrl = "http://localhost:11434/v1"
$Model = Get-Content "$RunRoot\model-tag.txt"

Invoke-RestMethod "http://localhost:11434/api/tags" |
  ConvertTo-Json -Depth 10 |
  Tee-Object -FilePath "$RunRoot\ollama-tags.json"

$Body = @{
  model = $Model
  messages = @(
    @{ role = "user"; content = "Reply with exactly: local llm ok" }
  )
  temperature = 0
  max_tokens = 16
} | ConvertTo-Json -Depth 6

$Body | Tee-Object -FilePath "$RunRoot\openai-chat-request.json"

$Response = Invoke-RestMethod `
  -Uri "$BaseUrl/chat/completions" `
  -Method Post `
  -ContentType "application/json" `
  -Headers @{ Authorization = "Bearer ollama" } `
  -Body $Body

$Response | ConvertTo-Json -Depth 10 |
  Tee-Object -FilePath "$RunRoot\openai-chat-response.json"
```

Pass signal: the model id in `ollama-tags.json` works through `/v1/chat/completions`.

Important distinction: OpenAI-compatible route proof does not mean every OpenAI feature is supported. Use [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] before connecting a generic client.

## Step 7: Save Benchmark Row

Before copying the benchmark row, use [[LLM/Study/Local LLM First Response Debrief Card|Local LLM First Response Debrief Card]] or [[LLM/Study/Local LLM First Response Debrief Runner|Local LLM First Response Debrief Runner]] to convert the native response's nanosecond timing fields and decide whether the response is route-only, benchmark-ready, or blocked by missing metrics. If the route is healthy, use [[LLM/Study/Local LLM First Quality Probe Suite|Local LLM First Quality Probe Suite]] or [[LLM/Study/Local LLM First Quality Probe Runner|Local LLM First Quality Probe Runner]] before claiming any quality signal.

| Run id | Runtime | Model | Quantization | Hardware | Prompt class | Prompt tokens | Output tokens | TTFT | Tokens/sec | Peak RAM/VRAM | Quality decision | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | Ollama Windows | `qwen3.5:4b` | Ollama default | RTX 3080 Ti 12 GB | smoke |  |  |  |  |  | Hold until quality harness | native and OpenAI-compatible route proof only |

The smoke benchmark proves route and rough timing. It does not prove workload quality.

## Step 8: Decision Row

Copy this row into [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]] or a dated capstone note.

| Field | Answer |
|---|---|
| Endpoint proof status | pass / hold / fail |
| Evidence folder |  |
| Runtime and version |  |
| Model tag |  |
| Runtime health snapshot |  |
| Smoke request summary |  |
| Native response file |  |
| OpenAI-compatible response file |  |
| First response debrief file |  |
| First response debrief runner output |  |
| First quality probe runner output |  |
| Listener boundary | loopback / exposed / unclear |
| Mechanism named | install/PATH / model artifact / route / prefill / decode / KV cache / quality |
| Decision | keep / tune / replace runtime / replace model / stop |
| Next proof | first quality probe / first client harness runner / model provenance / troubleshooting |

## Step 8.5: Audit The First Endpoint Folder

Use [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner|Local LLM First Endpoint Evidence Audit Runner]] after the debrief output exists. The audit should pass or explicitly hold before this run sheet is linked as endpoint proof.

Pass signal: the audit output says `first_endpoint_evidence_ready` and links the run card, preflight, runtime install state, model pull or custody, runtime health, smoke response, debrief, and decision artifacts.

Hold signal: the audit names the first missing gate and routes it to the note that should produce the missing file.

## Failure Forks

| Failure | Likely owner | Next route |
|---|---|---|
| `ollama` command unavailable after install | install path or terminal PATH refresh | rerun version check in a new shell, then inspect Ollama Windows paths |
| `ollama pull` fails | network, disk, model tag, or registry | [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab]] |
| native API fails but CLI works | server process, listener, route, or localhost | [[LLM/Study/Local LLM Serving Runbook]] |
| OpenAI-compatible route fails but native works | compatibility route or model id mismatch | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]] |
| response is fast but wrong | model quality, sampler, or prompt | [[LLM/Study/Local LLM First Quality Probe Suite]] first, then [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| response is slow | cold load, prefill, decode, offload, or memory pressure | [[LLM/Study/LLM Inference Request Lifecycle Lab]] |

## Completion Gate

This run sheet is complete only when:

- [ ] `run-card.txt` exists
- [ ] pre-install machine evidence exists
- [ ] `ollama-version-after.txt` exists
- [ ] model pull gate evidence exists, or this run sheet includes equivalent pull/list/tags/show output
- [ ] `ollama-list-after-pull.txt` contains the selected model
- [ ] `listeners-before-smoke.txt` shows the endpoint boundary
- [ ] `ollama-native-request.json` and `ollama-native-response.json` exist
- [ ] `ollama-tags.json`, `openai-chat-request.json`, and `openai-chat-response.json` exist
- [ ] [[LLM/Study/Local LLM First Response Debrief Card|Local LLM First Response Debrief Card]], [[LLM/Study/Local LLM First Response Debrief Runner|Local LLM First Response Debrief Runner]], or equivalent debrief row interprets the first response
- [ ] [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner|Local LLM First Endpoint Evidence Audit Runner]] checks the run folder before it supports the capstone workbook
- [ ] [[LLM/Study/Local LLM First Quality Probe Suite|Local LLM First Quality Probe Suite]], [[LLM/Study/Local LLM First Quality Probe Runner|Local LLM First Quality Probe Runner]], or equivalent note records whether smoke output has any first quality signal
- [ ] benchmark row is copied or linked
- [ ] decision row is copied or linked
- [ ] any failure is routed to exactly one next diagnostic note and saved with [[LLM/Study/Local LLM Failure Triage Runner|Local LLM Failure Triage Runner]] when downstream evidence depends on the rerun

## References

Internal routes:

- [[LLM/Study/Local LLM First Run Readiness Snapshot]]
- [[LLM/Study/Local LLM First Model Candidate Ladder]]
- [[LLM/Study/Local LLM Windows Model Store and Cache Plan]]
- [[LLM/Study/Local LLM Model Store Readiness Snapshot]]
- [[LLM/Study/Local LLM Windows Runtime Install Gate]]
- [[LLM/Study/Local LLM First Run Command Plan Runner]]
- [[LLM/Study/Local LLM First Model Pull Gate]]
- [[LLM/Study/Local LLM First Runtime Health Snapshot]]
- [[LLM/Study/Local LLM First Runtime Health Runner]]
- [[LLM/Study/Local LLM First Smoke Request Runner]]
- [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner]]
- [[LLM/Study/Local LLM Failure Triage Runner]]
- [[LLM/Study/Local LLM Windows First-Run Quickstart]]
- [[LLM/Study/Local LLM Command Cookbook]]
- [[LLM/Study/Local LLM First Response Debrief Card]]
- [[LLM/Study/Local LLM First Response Debrief Runner]]
- [[LLM/Study/Local LLM First Quality Probe Suite]]
- [[LLM/Study/Local LLM First Quality Probe Runner]]
- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]

External/current sources checked 2026-06-15:

- [Ollama Windows documentation](https://docs.ollama.com/windows)
- [Ollama Windows download page](https://ollama.com/download/windows)
- [Ollama quickstart](https://docs.ollama.com/quickstart)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
- [Ollama qwen3.5:4b model page](https://ollama.com/library/qwen3.5:4b)
- [Ollama qwen3.5:9b model page](https://ollama.com/library/qwen3.5:9b)
- [Ollama qwen3:4b-instruct model page](https://ollama.com/library/qwen3:4b-instruct)
