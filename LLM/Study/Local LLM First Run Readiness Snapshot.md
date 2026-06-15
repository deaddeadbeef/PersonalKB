---
tags: [study, llm, inference, local-llm, readiness, windows, evidence]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
last-machine-check: 2026-06-15T11:10:33+08:00
---

# Local LLM First Run Readiness Snapshot

> **One-line summary** This is the machine-specific readiness card for the first local LLM run: as of 2026-06-15T11:10:33+08:00, the workstation has an NVIDIA RTX 3080 Ti with 12 GB VRAM, no local LLM runtime installed, no endpoint listening, and a separate model-store readiness snapshot for the first pull.

Use this before [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]] and [[LLM/Study/Local LLM Windows First-Run Quickstart|Local LLM Windows First-Run Quickstart]]. The quickstart says what to do in general. This snapshot says what is true on this machine right now, what the lowest unproven layer is, and what exact evidence should be produced next. Before any model pull, use [[LLM/Study/Local LLM Windows Model Store and Cache Plan|Local LLM Windows Model Store and Cache Plan]] and [[LLM/Study/Local LLM Model Store Readiness Snapshot|Local LLM Model Store Readiness Snapshot]] to decide whether the default model store is acceptable or a custom cache path must be set first.

## Current State

Checked on 2026-06-15T11:10:33+08:00 from Windows PowerShell.

| Check | Result | Meaning |
|---|---|---|
| `ollama --version; ollama list` | `ollama: not found` | Ollama is not installed or is not on PATH. |
| `lms --version; lms server status` | `lms: not found` | LM Studio CLI is not installed or is not on PATH. |
| `nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader` | `NVIDIA GeForce RTX 3080 Ti, 12288 MiB, 610.47` | There is a usable NVIDIA GPU candidate for local inference. |
| Listener scan on ports `11434, 1234, 8000, 8001, 8080, 30000` | no rows returned | No common local LLM API port is currently listening. |
| Model/cache variables | `OLLAMA_MODELS`, `HF_HOME`, and `HF_HUB_CACHE` unset | Model store and Hub cache location must be decided before pulling. |
| Disk/model-store snapshot | [[LLM/Study/Local LLM Model Store Readiness Snapshot|Local LLM Model Store Readiness Snapshot]] | `C:` has 351.2 GB free, `D:` has 582.2 GB free, and no `D:\Models` root exists yet. |
| Endpoint proof | not started | No local model response has been captured yet. |

The refreshed state is unchanged at the runtime layer and now has storage evidence. The next blocker is still runtime installation after creating a run folder and choosing the model store, not model quality, endpoint routing, RAG, tools, or benchmarking.

## Readiness Decision

| Decision | Value |
|---|---|
| Lowest unproven layer | runtime installation |
| Recommended first runtime | Ollama on Windows, loopback only |
| GUI alternative | LM Studio local server on `localhost` |
| Storage decision | Use [[LLM/Study/Local LLM Model Store Readiness Snapshot|Local LLM Model Store Readiness Snapshot]]; recommended first root is `D:\Models` with `OLLAMA_MODELS=D:\Models\ollama` before the first pull |
| First model class | small instruct or reasoning model that fits comfortably before tuning |
| First candidate tags to evaluate | Use [[LLM/Study/Local LLM First Model Candidate Ladder|Local LLM First Model Candidate Ladder]]: `qwen3.5:4b` for route proof, `qwen3:4b-instruct` as text-only control, then `qwen3.5:9b` only after the first path is stable |
| Avoid as first proof | 27B+ or 30B+ models, LAN binding, RAG, tools, concurrency, prompt caching |
| First pass target | one loopback smoke response plus model id, route, listener proof, timing, and security boundary |

The RTX 3080 Ti makes a 4B-9B quantized first run realistic. It does not make long context, 27B+ models, high concurrency, or RAG quality proven. Context length still creates KV-cache pressure, and model file size is not the full memory budget.

## Immediate Next Action

Do these in order. Stop at the first failed command and write the failure owner into the evidence folder.

| Priority | Action | Evidence destination | Pass signal |
|---|---|---|---|
| 1 | Create a dated run folder from [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]]. | `run-root.txt` and `run-card.txt` | Evidence exists before installation or model pull. |
| 2 | Decide whether the default model cache path is acceptable or whether `OLLAMA_MODELS` should be set first using [[LLM/Study/Local LLM Windows Model Store and Cache Plan|Local LLM Windows Model Store and Cache Plan]] and [[LLM/Study/Local LLM Model Store Readiness Snapshot|Local LLM Model Store Readiness Snapshot]]. | `installer-choice.txt`, `model-cache-env-before.json`, or run card note | The model cache location is known before large downloads. |
| 3 | Install the first runtime through [[LLM/Study/Local LLM Windows Runtime Install Gate|Local LLM Windows Runtime Install Gate]], preferably Ollama for the Windows-native terminal proof. | installer source, command path, version output, model list, listener proof | `ollama --version` and `ollama ls` work in a new PowerShell. |
| 4 | Rerun `ollama list` and the listener scan. | `ollama-list-after-install.txt`, `listeners-before-smoke.txt` | Runtime is installed; endpoint exposure is understood. |
| 5 | Pull one small first model from [[LLM/Study/Local LLM First Model Candidate Ladder|Local LLM First Model Candidate Ladder]] and run native plus OpenAI-compatible smoke tests. | native response JSON, model tags JSON, OpenAI-compatible response JSON | Both route proof and model id proof exist, or a native-only decision is written. |
| 6 | Copy one benchmark/evidence row into the vault. | [[LLM/Study/Local LLM First Inference Evidence Pack]], [[LLM/Study/Local LLM Inference Benchmark Log]] | The first run becomes capstone evidence instead of console history. |

Do not start RAG, tools, runtime comparison, concurrency, prompt caching, or deployment work until priority 5 has either passed or produced a named blocker.

## First Execution Card

Use [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]] when you are ready to execute these steps and save the evidence folder.

Use one dated run folder:

```powershell
$RunRoot = Join-Path $HOME ("Documents\local-llm-runs\" + (Get-Date -Format "yyyy-MM-dd-HHmm") + "-first-readiness-run")
New-Item -ItemType Directory -Force -Path $RunRoot | Out-Null
$RunRoot
```

Then execute only one path.

| Step | Action | Evidence to save |
|---|---|---|
| 1 | Install Ollama from the official Windows installer or PowerShell installer. | installer source, version, install path if changed |
| 2 | If the home drive should not store models, set `OLLAMA_MODELS` before pulling and save the storage decision from [[LLM/Study/Local LLM Windows Model Store and Cache Plan|Local LLM Windows Model Store and Cache Plan]]. | environment variable value and cache path |
| 3 | Open a new PowerShell and run `ollama --version` and `ollama list`. | `runtime-version.txt` |
| 4 | Pull a small first model from [[LLM/Study/Local LLM First Model Candidate Ladder|Local LLM First Model Candidate Ladder]], preferably `qwen3.5:4b` for route proof. | `ollama-pull.txt`, model tag |
| 5 | Run the native Ollama smoke test from [[LLM/Study/Local LLM Command Cookbook|Local LLM Command Cookbook]]. | `ollama-native-generate.json` |
| 6 | Run the OpenAI-compatible smoke test from the cookbook. | `ollama-openai-chat.json` |
| 7 | Run the listener check. | `listeners.txt` showing loopback/private boundary |
| 8 | Copy one row into [[LLM/Study/Local LLM First Inference Evidence Pack|Local LLM First Inference Evidence Pack]]. | first inference evidence row |
| 9 | Copy one row into [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]]. | benchmark row with timing fields |
| 10 | Write the decision in [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]. | keep / tune / replace runtime / replace model |

## Stop Rules

- Do not install or pull a model without saving the run folder first.
- Do not bind to `0.0.0.0` or the LAN for the first proof.
- Do not judge model quality from the smoke prompt.
- Do not change runtime, model, sampler, context, and prompt in the same comparison.
- Do not start RAG until a plain local endpoint has passed.
- Do not treat a large advertised context window as a safe target without a context and KV-cache budget row.

## Mechanism Notes

| Observation | Mechanism interpretation |
|---|---|
| Runtime not installed | The failure owner is environment/runtime setup, not model quality. |
| GPU present | Weight memory, activation overhead, and KV-cache growth become the next constraints. |
| No listener | There is no local API server yet, so client failures would be premature. |
| 4B-9B first model | This minimizes load and memory risk while proving route, model id, prompt, response, and timing. |
| Long context available in model tags | Context capacity is not free; prefill time and KV-cache memory must be measured before use. |

## Completion Gate

This readiness snapshot is complete when:

- [x] local runtime commands have been checked
- [x] GPU availability has been checked
- [x] common local LLM listener ports have been checked
- [x] first runtime choice is explicit
- [x] first model class is explicit
- [ ] Ollama or LM Studio is installed
- [ ] one model is pulled or loaded
- [ ] one loopback smoke response is saved
- [ ] one benchmark row is saved
- [ ] one capstone decision row is saved

## References

Internal routes:

- [[LLM/Study/Local LLM Windows First-Run Quickstart]]
- [[LLM/Study/Local LLM First Model Candidate Ladder]]
- [[LLM/Study/Local LLM Windows Model Store and Cache Plan]]
- [[LLM/Study/Local LLM Model Store Readiness Snapshot]]
- [[LLM/Study/Local LLM Windows Runtime Install Gate]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM Command Cookbook]]
- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]

External/current sources checked 2026-06-15:

- [Ollama Windows documentation](https://docs.ollama.com/windows)
- [Ollama Windows download page](https://ollama.com/download/windows)
- [Ollama qwen3.5 model page](https://ollama.com/library/qwen3.5)
- [Ollama qwen3 tags](https://ollama.com/library/qwen3/tags)
- [LM Studio local server documentation](https://lmstudio.ai/docs/developer/core/server)
- [LM Studio OpenAI compatibility documentation](https://lmstudio.ai/docs/developer/openai-compat)
