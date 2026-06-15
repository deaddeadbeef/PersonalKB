---
tags: [study, llm, inference, local-llm, windows, storage, cache, readiness, evidence]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
last-machine-check: 2026-06-15T11:10:33+08:00
---

# Local LLM Model Store Readiness Snapshot

> **One-line summary** As of 2026-06-15T11:10:33+08:00, this Windows workstation has enough disk for a first small local model, no local LLM runtime on PATH, no model/cache variables set, no model directories created, and no common local LLM endpoint listening.

Use this after [[LLM/Study/Local LLM Windows Model Store and Cache Plan|Local LLM Windows Model Store and Cache Plan]] and before [[LLM/Study/Local LLM Model Store Bootstrap Runner|Local LLM Model Store Bootstrap Runner]], [[LLM/Study/Local LLM Windows Runtime Install Gate|Local LLM Windows Runtime Install Gate]], and [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]]. The model-store plan says what to decide. This snapshot records what is true on this machine before the first installer or model pull. Rerun [[LLM/Study/Local LLM First Run Readiness Runner|Local LLM First Run Readiness Runner]] when directory, environment, listener, runtime, or GPU state may have changed.

This note is read-only evidence. It did not install Ollama, LM Studio, Hugging Face CLI, create `D:\Models`, set environment variables, start a server, or pull a model.

## Current Machine Evidence

Checked from Windows PowerShell on 2026-06-15T11:10:33+08:00.

| Check | Result | Meaning |
|---|---|---|
| File-system free space | `C:` 351.2 GB free; `D:` 582.2 GB free | Either drive can hold the first small model; `D:` is the cleaner target for model artifacts because it has more free space and keeps large model stores out of the user profile. |
| `OLLAMA_MODELS` | user and process values are unset | Ollama would use its default store unless the variable is set before the first pull. |
| `HF_HOME` | user and process values are unset | Hugging Face tooling would use its default cache unless configured. |
| `HF_HUB_CACHE` | user and process values are unset | Hugging Face Hub cache root is not pinned yet. |
| `ollama` command | not found on PATH | Runtime install is still the lowest unproven layer. |
| `lms` command | not found on PATH | LM Studio CLI/server path is not available from this shell. |
| `hf` command | not found on PATH | Hugging Face CLI is not available from this shell. |
| `python` command | available at `C:\Users\fpan1\AppData\Local\Microsoft\WindowsApps\python.exe` | Python launcher presence does not prove a model-serving environment. |
| `nvidia-smi` | available at `C:\Windows\system32\nvidia-smi.exe` | NVIDIA GPU tooling is visible from Windows. |
| GPU summary | `NVIDIA GeForce RTX 3080 Ti, 12288 MiB, 610.47` | A 12 GB VRAM first-run path is plausible for the small-model ladder. |
| Common local LLM listener scan | no rows on ports `11434`, `1234`, `8000`, `8001`, `8080`, `30000` | No local LLM endpoint is currently listening on common ports. |
| Existing Ollama model directory | `C:\Users\fpan1\.ollama\models` does not exist | No default Ollama model store exists yet. |
| Existing custom model directories | `D:\Models`, `D:\Models\ollama`, `D:\Models\hf`, and `D:\Models\gguf` do not exist | The custom model root has not been created yet. |
| Evidence root | `C:\Users\fpan1\Documents\local-llm-runs` does not exist | The first run folder still needs to be created before install or pull. |

## Storage Decision

| Decision | Value |
|---|---|
| Recommended first model root | `D:\Models` |
| Recommended Ollama store | `D:\Models\ollama` |
| Recommended Hugging Face root | `D:\Models\hf` |
| Recommended GGUF/artifact folder | `D:\Models\gguf` |
| Evidence folder root | `C:\Users\fpan1\Documents\local-llm-runs` |
| First runtime path | Ollama on Windows, loopback only |
| First model choice | Use [[LLM/Study/Local LLM First Model Candidate Ladder|Local LLM First Model Candidate Ladder]], starting with `qwen3.5:4b` unless the source page or local constraints change |
| Current decision status | proceed to create run folder and set storage variables; hold on model pull until runtime install evidence exists |

Rationale: the default store would probably work for a small first pull because `C:` has free space, but a custom `D:\Models` root is cleaner for repeated experiments, avoids hiding large model bytes under the user profile, and separates runtime stores, Hub cache, GGUF artifacts, conversion outputs, and run evidence.

## Next Execution Steps

Do these in order. Stop at the first failure and route it to [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]].

1. Open [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]].
2. Use [[LLM/Study/Local LLM Model Store Bootstrap Runner|Local LLM Model Store Bootstrap Runner]] in dry-run mode to review the dated run folder, `D:\Models` directories, and cache variable actions.
3. If the dry-run plan is correct, rerun the bootstrap runner with `--apply` to create `D:\Models\ollama`, `D:\Models\hf`, `D:\Models\hf\hub`, and `D:\Models\gguf`, then set `OLLAMA_MODELS`, `HF_HOME`, and `HF_HUB_CACHE` as user variables.
4. Open a new PowerShell and rerun [[LLM/Study/Local LLM First Run Readiness Runner|Local LLM First Run Readiness Runner]] to prove the new shell sees the storage decision.
5. Use [[LLM/Study/Local LLM Windows Runtime Install Gate|Local LLM Windows Runtime Install Gate]] to install the first runtime and capture `ollama --version` from a new PowerShell.
6. Only after the runtime works, pull one first model from [[LLM/Study/Local LLM First Model Candidate Ladder|Local LLM First Model Candidate Ladder]].
7. Save native and OpenAI-compatible loopback response evidence.

## Copyable Decision Card

Paste this into the first endpoint run folder.

```text
snapshot=Local LLM Model Store Readiness Snapshot
checked_at=2026-06-15T11:10:33+08:00
runtime_installed=no
ollama_on_path=no
lms_on_path=no
hf_on_path=no
gpu=NVIDIA GeForce RTX 3080 Ti, 12288 MiB, driver 610.47
common_llm_listeners=none on 11434,1234,8000,8001,8080,30000
OLLAMA_MODELS=unset
HF_HOME=unset
HF_HUB_CACHE=unset
C_free_gb=351.2
D_free_gb=582.2
chosen_model_root=D:\Models
chosen_ollama_store=D:\Models\ollama
chosen_hf_root=D:\Models\hf
chosen_gguf_dir=D:\Models\gguf
decision=create run folder, create model roots, set OLLAMA_MODELS before first pull
hold_until=ollama version and model list are captured after install
```

## Evidence Commands Used

```powershell
Get-PSDrive -PSProvider FileSystem |
  Select-Object Name,Root,
    @{Name='FreeGB';Expression={[math]::Round($_.Free / 1GB, 1)}},
    @{Name='UsedGB';Expression={[math]::Round($_.Used / 1GB, 1)}} |
  Format-Table -AutoSize

[pscustomobject]@{
  OLLAMA_MODELS_user = [Environment]::GetEnvironmentVariable('OLLAMA_MODELS','User')
  OLLAMA_MODELS_process = $env:OLLAMA_MODELS
  HF_HOME_user = [Environment]::GetEnvironmentVariable('HF_HOME','User')
  HF_HOME_process = $env:HF_HOME
  HF_HUB_CACHE_user = [Environment]::GetEnvironmentVariable('HF_HUB_CACHE','User')
  HF_HUB_CACHE_process = $env:HF_HUB_CACHE
} | ConvertTo-Json

"ollama","lms","hf","python","nvidia-smi" | ForEach-Object {
  $cmd = Get-Command $_ -ErrorAction SilentlyContinue
  [pscustomobject]@{command=$_; available=[bool]$cmd; path=if($cmd){$cmd.Source}else{$null}}
} | Format-Table -AutoSize

nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader

Get-NetTCPConnection -State Listen -ErrorAction SilentlyContinue |
  Where-Object { $_.LocalPort -in 11434,1234,8000,8001,8080,30000 } |
  Select-Object LocalAddress,LocalPort,OwningProcess |
  Format-Table -AutoSize

$paths = @(
  'C:\Users\fpan1\.ollama\models',
  'D:\Models',
  'D:\Models\ollama',
  'D:\Models\hf',
  'D:\Models\gguf',
  'C:\Users\fpan1\Documents\local-llm-runs'
)
$paths | ForEach-Object { [pscustomobject]@{path=$_; exists=(Test-Path $_)} } |
  Format-Table -AutoSize
```

## Completion Gate

This snapshot is complete when:

- [x] disk free space is recorded
- [x] model/cache environment variables are recorded
- [x] runtime command availability is recorded
- [x] GPU visibility is recorded
- [x] listener scan is recorded
- [x] existing model/evidence directories are recorded
- [x] first storage decision is explicit
- [ ] run folder exists
- [ ] `D:\Models` subdirectories exist
- [ ] `OLLAMA_MODELS` is set and verified from a new shell
- [ ] runtime install evidence exists
- [ ] first model pull evidence exists

## References

- [[LLM/Study/Local LLM Windows Model Store and Cache Plan]]
- [[LLM/Study/Local LLM First Run Readiness Snapshot]]
- [[LLM/Study/Local LLM First Run Readiness Runner]]
- [[LLM/Study/Local LLM Model Store Bootstrap Runner]]
- [[LLM/Study/Local LLM First Model Candidate Ladder]]
- [[LLM/Study/Local LLM Windows Runtime Install Gate]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM Windows First-Run Quickstart]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
