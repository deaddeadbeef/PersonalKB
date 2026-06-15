---
tags: [study, llm, inference, local-llm, ollama, model-acquisition, provenance, first-run, evidence]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-16
---

# Local LLM First Model Pull Gate

> **One-line summary** Before the first inference call, freeze the selected Ollama tag, prove where the bytes will land, pull only one small baseline model, capture model metadata, and decide whether the artifact is ready for endpoint smoke testing.

Use this after [[LLM/Study/Local LLM Windows Runtime Install Gate|Local LLM Windows Runtime Install Gate]] passes and before [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]]. The install gate proves the runtime exists, and [[LLM/Study/Local LLM Windows Runtime Install Runner|Local LLM Windows Runtime Install Runner]] makes that proof machine-checkable. This pull gate proves the first model artifact is the one you meant to download. Use [[LLM/Study/Local LLM First Model Source Recheck Runner|Local LLM First Model Source Recheck Runner]] immediately before this gate when model-page facts need a dated pass/hold/fail row. Use [[LLM/Study/Local LLM Runtime Compatibility Runner|Local LLM Runtime Compatibility Runner]] before this gate when artifact format, quantization, tokenizer, chat template, route, or model-id support is not already proven. Use [[LLM/Study/Local LLM First Model Pull Runner|Local LLM First Model Pull Runner]] after this gate when the saved source-recheck, install-runner, pull/list/tags/show artifacts should become repeatable pass/hold/fail evidence. Use [[LLM/Study/Local LLM First Runtime Health Snapshot|Local LLM First Runtime Health Snapshot]] after this gate when you want one no-inference proof that the listener, native model list, running-model list, and OpenAI-compatible model list agree before the first prompt.

This is not a quality test. It is a custody and readiness gate for the first model bytes.

## Outcome

After this gate you should know:

- the exact first model tag, fallback tag, and reason for choosing it
- whether the model store decision is default, custom `OLLAMA_MODELS`, or hold
- whether the source page still matches the expected size, modality, and context claim
- whether the pull completed into the intended local store
- what Ollama reports through `ollama ls`, `/api/tags`, and `/api/show`
- whether a no-inference health snapshot should be saved before endpoint smoke
- whether the next action is endpoint smoke, smaller model, storage fix, provenance hold, or troubleshooting

## Gate Rule

Do not run `ollama pull` until all three are true:

| Required proof | Source |
|---|---|
| Runtime works from a new shell | [[LLM/Study/Local LLM Windows Runtime Install Gate]] |
| Runtime install readiness is machine-checked | [[LLM/Study/Local LLM Windows Runtime Install Runner]] |
| Model store decision is not hold | [[LLM/Study/Local LLM Model Store Readiness Snapshot]] |
| First model slot is chosen | [[LLM/Study/Local LLM First Model Candidate Ladder]] |
| Current source facts are rechecked | [[LLM/Study/Local LLM First Model Source Recheck Runner]] |
| Runtime/model compatibility is not hold | [[LLM/Study/Local LLM Runtime Compatibility Runner]] |

The first pull changes one variable: model tag. Do not also change runtime, endpoint route, context length, sampler, chat template, or LAN exposure in the same pass.

## Current First-Pull Decision

Applied source check and pull on 2026-06-16:

| Slot | Tag | Source facts to recheck before pull | Use |
|---|---|---|---|
| Applied first proof | `qwen3.5:2b-q4_K_M` | Tags page showed digest `124a03c34777`, 1.9GB, 256K context, Text/Image input; local `/api/tags` showed digest `124a03c347777e8e4e5955c33610ae01d9d90d8c2a718bfba069c498d5c7f3c9`. | First route-proof model, now proven in [[LLM/Study/Local LLM First Inference Proof - 2026-06-16]]. |
| Older baseline candidate | `qwen3.5:4b` | Initial source recheck reached the page but did not find the older expected `parameters 4.66B` and `quantization Q4_K_M` snippets. | Recheck before any future 4B pull; do not assume the old snippet set is still page-visible. |
| Text-only control | `qwen3:4b-instruct` | Initial source recheck reached the page but did not find the older expected `parameters 4.02B` and `quantization Q4_K_M` snippets. | Recheck before a control pull; use it only if the current source facts pass. |
| Stretch | `qwen3.5:9b` | Tags page shows digest `6488c96fa5fa`, 6.6GB, 256K context, Text/Image input. | Only after baseline endpoint proof exists. |
| Avoid first | 27B and larger tags | Some tags exceed this machine's 12GB VRAM before KV cache and overhead. | Not first-run material. |

The advertised context window is not a local context budget. Huge context labels do not prove KV-cache headroom, prompt-eval latency, or quality on this machine.

## Step 0: Create Evidence Folder

```powershell
$RunRoot = Join-Path $HOME ("Documents\local-llm-runs\" + (Get-Date -Format "yyyy-MM-dd-HHmm") + "-first-model-pull-gate")
New-Item -ItemType Directory -Force -Path $RunRoot | Out-Null
$RunRoot | Tee-Object -FilePath "$RunRoot\run-root.txt"
```

Save the decision card before pulling:

```powershell
@"
date=$(Get-Date -Format o)
gate=Local LLM First Model Pull Gate
runtime=Ollama on Windows
selected_model=qwen3.5:4b
fallback_model=qwen3.5:2b
source_page=https://ollama.com/library/qwen3.5/tags
source_checked_at=2026-06-16
source_recheck_output=<path-to-model-source-recheck-json>
runtime_install_runner_output=<path-to-runtime-install-json>
expected_size=3.4GB
expected_context=256K
expected_input=Text, Image
expected_source_digest=2a654d98e6fb
model_store_decision=<default-or-custom-OLLAMA_MODELS-or-hold>
next_gate=Local LLM First Endpoint Run Sheet
"@ | Set-Content "$RunRoot\model-pull-decision.txt"
```

Pass signal: a future run can see what you intended to pull before any download changed local state.

## Step 1: Capture Pre-Pull Runtime And Store State

Open a new PowerShell after the install gate and run:

```powershell
$RunRoot = "<paste-run-folder-path>"

ollama --version | Tee-Object -FilePath "$RunRoot\ollama-version-before-pull.txt"
ollama ls | Tee-Object -FilePath "$RunRoot\ollama-ls-before-pull.txt"

@"
OLLAMA_MODELS=$env:OLLAMA_MODELS
USERPROFILE=$env:USERPROFILE
LOCALAPPDATA=$env:LOCALAPPDATA
"@ | Tee-Object -FilePath "$RunRoot\ollama-env-before-pull.txt"

Get-PSDrive -PSProvider FileSystem |
  Select-Object Name, Root, Used, Free |
  Format-Table |
  Tee-Object -FilePath "$RunRoot\disk-before-pull.txt"
```

If `OLLAMA_MODELS` is custom, record it:

```powershell
if ($env:OLLAMA_MODELS) {
  Get-Item -LiteralPath $env:OLLAMA_MODELS -ErrorAction SilentlyContinue |
    Format-List FullName, Exists, CreationTime, LastWriteTime |
    Tee-Object -FilePath "$RunRoot\ollama-model-store-before-pull.txt"
} else {
  "OLLAMA_MODELS not set; using Ollama default model store." |
    Tee-Object -FilePath "$RunRoot\ollama-model-store-before-pull.txt"
}
```

Hold signal: the store path is unknown, the drive is too full, or `ollama --version` only works in the old shell. Return to the install or model-store gate before pulling.

## Step 2: Recheck The Source Page

Before a real pull, run [[LLM/Study/Local LLM First Model Source Recheck Runner|Local LLM First Model Source Recheck Runner]] or manually open the current model page or tags page and compare:

| Field | Expected for baseline | If different |
|---|---|---|
| Tag exists | `qwen3.5:4b` | Do not guess a larger replacement. Use fallback or hold. |
| Size | about 3.4GB | Re-estimate disk/time and record the new value. |
| Input | Text/Image | Decide whether multimodal defaults matter for a text-only smoke. |
| Context | 256K advertised | Still use a tiny first prompt. |
| Digest on page | `2a654d98e6fb` | Record the new source digest before pull. |
| License/source availability | page reachable | If unclear, mark provenance partial. |

The source page is not local proof. It only freezes the expected remote artifact before the pull.

## Step 3: Pull Exactly One Baseline Model

```powershell
$RunRoot = "<paste-run-folder-path>"
$Model = "qwen3.5:4b"
$Model | Tee-Object -FilePath "$RunRoot\selected-model.txt"

ollama pull $Model |
  Tee-Object -FilePath "$RunRoot\ollama-pull.txt"
```

Do not run `ollama run` yet. First prove what the runtime now sees:

```powershell
ollama ls |
  Tee-Object -FilePath "$RunRoot\ollama-ls-after-pull.txt"

Invoke-RestMethod "http://localhost:11434/api/tags" |
  ConvertTo-Json -Depth 10 |
  Tee-Object -FilePath "$RunRoot\ollama-api-tags-after-pull.json"
```

Pass signal: `ollama ls` and `/api/tags` include the selected model or a clearly equivalent resolved tag.

Hold signal: pull output shows an error, a different tag resolved, the model store filled the wrong drive, or `/api/tags` cannot see the model.

## Step 4: Capture Model Metadata Before Inference

Use `/api/show` to capture model details, template, parameters, capabilities, license, and model metadata exposed by the runtime:

```powershell
$RunRoot = "<paste-run-folder-path>"
$Model = Get-Content "$RunRoot\selected-model.txt"

$ShowBody = @{ model = $Model; verbose = $false } | ConvertTo-Json -Depth 4
$ShowBody | Tee-Object -FilePath "$RunRoot\ollama-show-request.json"

Invoke-RestMethod `
  -Uri "http://localhost:11434/api/show" `
  -Method Post `
  -ContentType "application/json" `
  -Body $ShowBody |
  ConvertTo-Json -Depth 20 |
  Tee-Object -FilePath "$RunRoot\ollama-show-response.json"
```

Also check whether anything is already loaded into memory:

```powershell
Invoke-RestMethod "http://localhost:11434/api/ps" |
  ConvertTo-Json -Depth 10 |
  Tee-Object -FilePath "$RunRoot\ollama-ps-before-smoke.json"
```

Interpretation:

| Runtime field | Academic link | Why it matters locally |
|---|---|---|
| `details.parameter_size` | model capacity | Larger models usually improve capability but increase memory and load time. |
| `details.quantization_level` | compression/quantization | Smaller weights can fit local VRAM but may change quality and backend behavior. |
| `template` | chat formatting | Wrong role/template handling can look like model weakness. |
| `model_info` attention and context fields | architecture and KV cache | Context length and KV-head design affect prefill, decode, and memory pressure. |
| `capabilities` | modality and route expectations | Text, vision, tools, or thinking support must match the workload. |
| `license` | acquisition boundary | Local use is still governed by model terms. |

## Step 5: Pass, Hold, Fail

| Decision | Evidence | Next route |
|---|---|---|
| Pass | pull output saved, `ollama ls` shows model, `/api/tags` shows model, `/api/show` saved, store path matches decision | [[LLM/Study/Local LLM First Runtime Health Snapshot]] before [[LLM/Study/Local LLM First Endpoint Run Sheet]] |
| Hold | source page changed, storage unclear, disk low, pull partial, tag mismatch, metadata missing, license unclear | [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]] or [[LLM/Study/Local LLM Troubleshooting Decision Tree]] |
| Fail | runtime cannot pull/list/show any selected model, or model store is wrong and must be reset | Roll back, fix install/store/runtime, then rerun this gate |

Copy this row into [[LLM/Study/Local LLM First Inference Evidence Pack|Local LLM First Inference Evidence Pack]] or the capstone workbook:

| Field | Value |
|---|---|
| Pull gate status | pass / hold / fail |
| Evidence folder |  |
| Selected model |  |
| Fallback model |  |
| Source page and checked date |  |
| Pull output |  |
| `ollama ls` output |  |
| `/api/tags` output |  |
| `/api/show` output |  |
| First runtime health snapshot |  |
| Model store decision | default / custom / hold |
| License/provenance status | pass / partial / hold |
| Next action | endpoint smoke / smaller model / storage fix / troubleshooting |

## Rollback Before Endpoint Smoke

If the pull is wrong and no response has been generated yet:

```powershell
$Model = Get-Content "$RunRoot\selected-model.txt"
ollama rm $Model | Tee-Object -FilePath "$RunRoot\ollama-rm-wrong-model.txt"
ollama ls | Tee-Object -FilePath "$RunRoot\ollama-ls-after-rm.txt"
```

If `OLLAMA_MODELS` was wrong, stop Ollama, fix the environment variable using [[LLM/Study/Local LLM Windows Runtime Install Gate|Local LLM Windows Runtime Install Gate]], reopen PowerShell, and rerun this gate from Step 1.

## Completion Gate

This gate is complete only when:

- [ ] `model-pull-decision.txt` exists
- [ ] `ollama-version-before-pull.txt` exists
- [ ] `disk-before-pull.txt` and model-store evidence exist
- [ ] current source page facts were checked by [[LLM/Study/Local LLM First Model Source Recheck Runner|Local LLM First Model Source Recheck Runner]] or marked partial with a hold reason
- [ ] [[LLM/Study/Local LLM Windows Runtime Install Runner|Local LLM Windows Runtime Install Runner]] output exists and reports pass before pull
- [ ] `ollama-pull.txt` exists
- [ ] `ollama-ls-after-pull.txt` includes the selected model
- [ ] `ollama-api-tags-after-pull.json` includes the selected model
- [ ] `ollama-show-response.json` exists
- [ ] [[LLM/Study/Local LLM First Model Pull Runner|Local LLM First Model Pull Runner]] output exists when pull evidence will support runtime health, endpoint smoke, benchmark, quality, or deployment decisions
- [ ] pass/hold/fail row names exactly one next route

## References

Internal routes:

- [[LLM/Study/Local LLM Windows Runtime Install Gate]]
- [[LLM/Study/Local LLM Windows Runtime Install Runner]]
- [[LLM/Study/Local LLM First Model Candidate Ladder]]
- [[LLM/Study/Local LLM First Model Source Recheck Runner]]
- [[LLM/Study/Local LLM Model Store Readiness Snapshot]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Runtime Compatibility Runner]]
- [[LLM/Study/Local LLM First Model Pull Runner]]
- [[LLM/Study/Local LLM First Runtime Health Snapshot]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]

External/current sources checked 2026-06-16:

- [Ollama qwen3.5 tags](https://ollama.com/library/qwen3.5/tags)
- [Ollama qwen3.5:4b model page](https://ollama.com/library/qwen3.5:4b)
- [Ollama qwen3.5:2b model page](https://ollama.com/library/qwen3.5:2b)
- [Ollama qwen3:4b-instruct model page](https://ollama.com/library/qwen3:4b-instruct)
- [Ollama qwen3 tags](https://ollama.com/library/qwen3/tags)
- [Ollama CLI reference](https://docs.ollama.com/cli)
- [Ollama list models API](https://docs.ollama.com/api/tags)
- [Ollama show model details API](https://docs.ollama.com/api-reference/show-model-details)
- [Ollama list running models API](https://docs.ollama.com/api/ps)
- [Ollama usage metrics](https://docs.ollama.com/api/usage)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
