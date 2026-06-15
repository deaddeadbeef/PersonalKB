---
tags: [study, llm, inference, local-llm, windows, storage, cache, ollama, hugging-face]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM Windows Model Store and Cache Plan

> **One-line summary** Decide where model weights, runtime stores, artifact caches, conversion outputs, and evidence logs live before the first large local LLM download.

Use this before [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]], [[LLM/Study/Local LLM Windows First-Run Quickstart|Local LLM Windows First-Run Quickstart]], and [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]]. The endpoint run sheet proves the first model call. The artifact lab proves exact downloaded bytes. This note prevents a more basic failure: pulling multi-GB model artifacts into an unknown or hard-to-clean location. For this workstation's latest read-only storage evidence, use [[LLM/Study/Local LLM Model Store Readiness Snapshot|Local LLM Model Store Readiness Snapshot]].

This is a storage decision note, not an installer. Do not install a runtime, pull a model, or delete a cache until the target path, free disk, owner, and rollback plan are written into the run folder.

## Outcome

After this plan you should be able to:

- choose the default runtime store or an explicit model root before a pull
- separate runtime stores, Hugging Face caches, GGUF/source mirrors, conversion outputs, private corpora, and evidence logs
- prove the current environment variables and free disk from PowerShell
- avoid filling the Windows home drive with hidden duplicate model caches
- record enough path evidence to reproduce, clean up, or move the first local LLM setup

## Storage Layers

| Layer | Examples | Should contain | Should not contain |
|---|---|---|---|
| Runtime model store | Ollama model store, LM Studio managed models | Runtime-owned model packages and metadata | Prompt logs, RAG documents, benchmark notes |
| Hugging Face cache | `HF_HOME`, `HF_HUB_CACHE`, per-command `--cache-dir` | Hub snapshots, blobs, refs, downloaded model files | Hand-edited conversion experiments |
| Source mirror | `D:\Models\source\<model>` | Human-visible copies for inspection or conversion | Floating unpinned downloads mixed across revisions |
| GGUF/artifact directory | `D:\Models\gguf`, `D:\Models\converted` | Accepted single-file artifacts and derived outputs | Unknown files without source or hash |
| Evidence folder | `Documents\local-llm-runs\<date>-...` | Run cards, command output, request/response JSON, benchmark rows | Model weights or private corpora |
| RAG/private corpus store | Project-specific private document directory | Documents, chunks, embedding indexes, access notes | Runtime caches or downloaded base weights |

The practical rule: model weights are infrastructure state; evidence folders are audit state; private corpora are data-boundary state. Keeping those separate makes cleanup and security decisions much easier.

## First Decision

Before the first pull, answer this card.

| Field | Value |
|---|---|
| Runtime path | Ollama / LM Studio / llama.cpp / vLLM / SGLang / other |
| First model tag or artifact |  |
| Expected download size |  |
| Default store acceptable? | yes / no / unknown |
| Chosen model root | default / `D:\Models\...` / external drive / other |
| Free disk on target drive |  |
| Cache variables to set before download | none / `OLLAMA_MODELS` / `HF_HOME` / `HF_HUB_CACHE` / runtime setting |
| Evidence folder |  |
| Cleanup if rejected | `ollama rm`, `hf cache rm --dry-run`, delete local mirror, or hold |
| Data boundary | public model only / personal prompts / private corpus / mixed |

Pass signal: a future run can explain why the model was downloaded to that location and how to remove or reproduce it.

## Pre-Pull PowerShell Evidence

Run this before installing, pulling, mirroring, or converting model artifacts.

```powershell
$RunRoot = Join-Path $HOME ("Documents\local-llm-runs\" + (Get-Date -Format "yyyy-MM-dd-HHmm") + "-model-store-plan")
New-Item -ItemType Directory -Force -Path $RunRoot | Out-Null
$RunRoot | Tee-Object -FilePath "$RunRoot\run-root.txt"

Get-PSDrive -PSProvider FileSystem |
  Select-Object Name, Root,
    @{Name="FreeGB";Expression={[math]::Round($_.Free / 1GB, 1)}},
    @{Name="UsedGB";Expression={[math]::Round($_.Used / 1GB, 1)}} |
  Format-Table |
  Tee-Object -FilePath "$RunRoot\disk-before-model-pull.txt"

[pscustomobject]@{
  OLLAMA_MODELS_user = [Environment]::GetEnvironmentVariable("OLLAMA_MODELS", "User")
  OLLAMA_MODELS_process = $env:OLLAMA_MODELS
  HF_HOME_user = [Environment]::GetEnvironmentVariable("HF_HOME", "User")
  HF_HOME_process = $env:HF_HOME
  HF_HUB_CACHE_user = [Environment]::GetEnvironmentVariable("HF_HUB_CACHE", "User")
  HF_HUB_CACHE_process = $env:HF_HUB_CACHE
} | ConvertTo-Json |
  Tee-Object -FilePath "$RunRoot\model-cache-env-before.json"
```

If the target drive has less than the first model size plus room for one duplicate copy, conversion scratch, and evidence logs, choose a smaller model or a different target drive before continuing.

## Ollama Model Store Plan

Official Ollama documentation says Windows models are stored under the user profile by default and that `OLLAMA_MODELS` changes the model location. Decide before the first `ollama pull`; moving after download is more error-prone than setting the location first.

Use the default only when:

- the home/profile drive has enough free space for the first model, at least one replacement candidate, and failed partial downloads
- you are comfortable with Ollama owning the model store there
- you are not trying to share a model directory with Hugging Face, LM Studio, or conversion experiments

Use an explicit model root when the C drive is small, you want model bytes on a data drive, or you expect repeated experiments.

```powershell
$ModelRoot = "D:\Models\ollama"
New-Item -ItemType Directory -Force -Path $ModelRoot | Out-Null
[Environment]::SetEnvironmentVariable("OLLAMA_MODELS", $ModelRoot, "User")

"OLLAMA_MODELS=$ModelRoot" |
  Tee-Object -FilePath "$RunRoot\ollama-model-store-choice.txt"
```

After changing the user environment variable, open a new PowerShell and restart the Ollama app/service if it was already running. Then verify from the shell that will pull the model:

```powershell
$RunRoot = "<paste-run-folder-path>"

[pscustomobject]@{
  OLLAMA_MODELS_user = [Environment]::GetEnvironmentVariable("OLLAMA_MODELS", "User")
  OLLAMA_MODELS_process = $env:OLLAMA_MODELS
} | ConvertTo-Json |
  Tee-Object -FilePath "$RunRoot\ollama-model-store-after.json"

ollama --version | Tee-Object -FilePath "$RunRoot\ollama-version-storage-check.txt"
ollama list | Tee-Object -FilePath "$RunRoot\ollama-list-before-pull.txt"
```

Do not infer the active model store only from the variable. Also record `ollama list`, the chosen pull command, and `ollama show` or API show output after the model is pulled.

## Hugging Face Cache Plan

Hugging Face Hub cache location is configurable with `HF_HOME`, `HF_HUB_CACHE`, or a per-command cache argument. Use this path when the first artifact comes from the Hub, a GGUF repo, Transformers, vLLM, SGLang, or a conversion workflow.

Recommended policy:

- use a dedicated Hub cache such as `D:\Models\hf` for reusable snapshots
- use `--local-dir` for a human-visible mirror that will be inspected or converted
- do not edit files inside the shared Hub cache
- pin revisions for benchmark or conversion work
- keep private corpora and prompt logs out of the Hub cache

Example setup:

```powershell
$env:HF_HOME = "D:\Models\hf"
$env:HF_HUB_CACHE = "D:\Models\hf\hub"
New-Item -ItemType Directory -Force -Path $env:HF_HUB_CACHE | Out-Null

[Environment]::SetEnvironmentVariable("HF_HOME", $env:HF_HOME, "User")
[Environment]::SetEnvironmentVariable("HF_HUB_CACHE", $env:HF_HUB_CACHE, "User")
```

Example evidence before download:

```powershell
hf cache ls | Tee-Object -FilePath "$RunRoot\hf-cache-before.txt"
hf download <org-or-user>/<repo> --revision <commit-or-tag> --dry-run |
  Tee-Object -FilePath "$RunRoot\hf-download-dry-run.txt"
```

For exact download, verification, file lists, GGUF choice, or conversion, continue into [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]].

## LM Studio Model Store Plan

LM Studio can serve local models from the Developer/local-server flow, including OpenAI-compatible endpoints. Treat its model directory as a runtime-managed store unless you deliberately import or point it at a controlled artifact.

Before using it as the first runtime:

| Check | Evidence |
|---|---|
| Model directory | Screenshot or note from LM Studio settings/model-management UI |
| Downloaded model id | exact model id shown by LM Studio or `/v1/models` |
| Server base URL | usually local loopback for the first proof |
| Network setting | localhost only for first run |
| Duplicate cache risk | whether the same model also exists in Ollama, HF cache, or GGUF directory |

Do not assume a GUI chat works as an API proof. The storage plan only proves where bytes live. The endpoint proof still needs [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]] or [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]].

## Disk Budget Worksheet

Use conservative space planning because first runs often create duplicates: registry cache, runtime package, local mirror, converted GGUF, failed partial file, and benchmark evidence.

| Item | Example value | Record |
|---|---|---|
| First runtime package | Ollama tag or LM Studio model |  |
| First model artifact | model tag, GGUF, or HF snapshot |  |
| Candidate replacement | smaller/larger control model |  |
| Conversion scratch | source snapshot plus output GGUF |  |
| Evidence/logs | run folder, request/response JSON, screenshots |  |
| Safety margin | at least enough for one failed or duplicate artifact |  |
| Target free disk after pull |  |

Hold if the target drive cannot absorb the first model plus one duplicate candidate. A model download failure caused by disk pressure is an environment failure, not a model-quality result.

## Cleanup And Rollback

Never blindly delete a cache directory. First identify whether the path is a runtime store, shared cache, local mirror, converted artifact, or evidence folder.

| Store | Safer first action |
|---|---|
| Ollama | `ollama list`, `ollama show <model>`, then `ollama rm <model>` for rejected models |
| Hugging Face cache | `hf cache ls`, `hf cache rm <repo> --dry-run`, `hf cache prune --dry-run` |
| Local mirror | verify source/revision/hash is captured, then remove only the rejected mirror directory |
| Converted artifact | keep accepted output hashes; remove rejected outputs only after compatibility decision |
| Evidence folder | keep small command outputs even when the model is rejected |

If cleanup would remove the only evidence for a benchmark, copy the decision card into the vault first.

## Failure Triage

| Symptom | Likely layer | First check |
|---|---|---|
| C drive fills during first pull | Default model/cache path | Check `OLLAMA_MODELS`, `HF_HOME`, `HF_HUB_CACHE`, and disk evidence from the run folder. |
| Runtime cannot find a model after moving paths | Runtime process did not inherit new environment | Restart shell and runtime, then record env variables and model list again. |
| Same model appears in multiple places | Duplicate runtime store/cache/mirror | Decide which copy is authoritative before serving or benchmarking. |
| Download succeeds but benchmark cannot be reproduced | Floating tag/revision or hidden runtime package | Record exact tag, revision, digest, `ollama show`, or Hub snapshot path. |
| Cleanup deletes needed model | Cache/store confusion | Restore from source if pinned; otherwise mark provenance as partial and reacquire cleanly. |
| Private files appear in model directory | Data-boundary leak | Move corpora/logs to a project data store and rerun security/privacy checks. |

## Completion Gate

This plan is complete when you have:

- [ ] a run folder with disk evidence
- [ ] environment variable evidence before the first pull
- [ ] an explicit default-vs-custom model-store decision
- [ ] target drive free-space decision
- [ ] runtime store, Hub cache, artifact mirror, and evidence folder separated
- [ ] cleanup method identified before download
- [ ] private corpus/log boundary separated from model stores
- [ ] handoff to [[LLM/Study/Local LLM First Endpoint Run Sheet|First Endpoint Run Sheet]] or [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Artifact Download Cache and Conversion Lab]]

## References

Internal:

- [[LLM/Study/Local LLM First Run Readiness Snapshot]]
- [[LLM/Study/Local LLM Model Store Readiness Snapshot]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM Windows First-Run Quickstart]]
- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]

External/current docs checked 2026-06-15:

- [Ollama Windows documentation](https://docs.ollama.com/windows)
- [Ollama FAQ: model storage and OLLAMA_MODELS](https://docs.ollama.com/faq)
- [Hugging Face Hub environment variables](https://huggingface.co/docs/huggingface_hub/en/package_reference/environment_variables)
- [Hugging Face Hub cache management](https://huggingface.co/docs/huggingface_hub/en/guides/manage-cache)
- [LM Studio local server documentation](https://lmstudio.ai/docs/developer/core/server)
