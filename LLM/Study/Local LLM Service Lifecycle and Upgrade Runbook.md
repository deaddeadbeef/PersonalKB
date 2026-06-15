---
tags: [study, llm, local-llm, operations, lifecycle, upgrade, rollback]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM Service Lifecycle and Upgrade Runbook

> **One-line summary** A local LLM server is maintainable only when startup mode, pinned runtime and model versions, cache paths, health checks, backups, upgrade steps, rollback steps, and post-change validation are written before the next change.

Use this after [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] proves the endpoint and [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]] proves model state, timings, logs, metrics, and resource pressure. Use [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner|Local LLM Service Lifecycle and Upgrade Runner]] when the change-freeze card, baseline artifacts, backup route, rollback route, and before/after/rollback decision need repeatable JSON, CSV, Markdown, and JSONL evidence.

Use [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] before and after each lifecycle change so "the update helped" means a measured row changed. Use [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]] when a restart, update, model move, or rollback changes behavior.

Use [[LLM/Study/Local LLM Docker GPU Container Serving Lab|Local LLM Docker GPU Container Serving Lab]] before this runbook if the service is a Dockerized vLLM/SGLang provider or Open WebUI. The Docker lab proves the image tag, GPU runtime, cache mount, loopback mapping, Compose file, Open WebUI volume/secret boundary, and first rollback/teardown command that this lifecycle runbook later maintains.

This runbook turns a working endpoint into an owned service. The academic mechanism is still the same: serving systems manage memory, queues, KV cache, prefix caches, latency, and quality trade-offs. The lifecycle layer decides how those choices survive restarts, upgrades, model-cache moves, prompt-cache moves, UI updates, and rollback.

## What This Runbook Decides

It answers seven maintenance questions:

1. Which binary, package, container image, app version, or git commit is running?
2. Which model artifact, revision, digest, quantization, and local cache path is being served?
3. How does the server start after reboot: manual shell, desktop app, startup task, systemd service, Docker/Compose, or another supervisor?
4. Which environment variables, ports, auth settings, data volumes, and model-cache locations are part of the service contract?
5. What must be backed up before changing runtime, model, UI, cache, or config?
6. What exact test proves the service is healthy after a restart, upgrade, or rollback?
7. What is the fastest safe way back to the previous working state?

Do not upgrade a local LLM stack from memory. Upgrade from a card.

## Lifecycle Surfaces

| Surface | What can drift | Evidence to record |
| --- | --- | --- |
| Runtime | App version, Python package, container tag, binary build, CUDA/ROCm/driver dependency. | Version command, image tag, pip freeze, installer file, commit, or release tag. |
| Model artifact | Model id, revision, digest, quantization, local filename, cache path. | Model list, model card, license, revision/tag/digest, hash when available, local path. |
| Prompt/KV cache | File prompt-cache path, slot-save directory, prefix-cache setting, cache salt/isolation, hierarchical cache storage. | Launch flags, env vars, cache path, metrics, and privacy boundary. |
| Startup mode | Manual command, desktop toggle, background service, systemd unit, Docker service. | Startup command, service name, environment file, working directory, restart policy. |
| Endpoint | Host, port, route, API mode, auth, TLS/proxy boundary. | Listener proof, base URL, route test, bind address, security decision. |
| UI/data layer | Open WebUI database, uploaded files, user settings, secrets, provider config. | Volume path, backup path, `WEBUI_SECRET_KEY` handling, restore test note. |
| Client contract | Model id expected by apps, OpenAI-compatible feature set, streaming behavior. | API contract card, client harness run, harmless failure row. |
| Operations evidence | Logs, metrics, resource counters, benchmark rows, quality rows. | Observability run folder, benchmark log, quality harness, troubleshooting rows. |

## Change Freeze Card

Fill this before changing anything.

| Field | Value |
| --- | --- |
| Change id |  |
| Date/time |  |
| Owner |  |
| Reason for change | security / bug / speed / quality / compatibility / storage / UI / experiment |
| Workload affected |  |
| Current runtime and version |  |
| Target runtime and version |  |
| Current model id/revision/digest |  |
| Target model id/revision/digest |  |
| Model artifact/cache path |  |
| Prompt/KV cache path or policy |  |
| Startup mode and service name |  |
| Startup command or container command |  |
| Environment variables |  |
| Bind address and port |  |
| Auth/secrets |  |
| UI/data volume |  |
| Baseline health check |  |
| Baseline benchmark row |  |
| Baseline quality row |  |
| Backup location |  |
| Rollback target |  |
| Post-change validation suite |  |
| Abort condition |  |

Pass signal: a different person could restore the previous service from this card without guessing which model, path, port, or container tag mattered.

## Runtime Lifecycle Map

| Runtime | Pin before change | Startup/service notes | Health and state proof | Rollback handle |
| --- | --- | --- | --- | --- |
| Ollama | Ollama version, model tag/digest, `OLLAMA_MODELS`, `OLLAMA_HOST`, model cache path. | Windows uses user/system environment variables; Linux service config can be edited with systemd override files. | `/api/version`, `/api/tags`, `/api/ps`, one native `/api/generate` smoke test, listener proof. | Previous installer/package, old environment variables, existing model cache, `ollama pull` tag/digest. |
| LM Studio | App version, `lms` CLI version, loaded model id/path, TTL/eviction settings. | Desktop app can host a local server; `llmster` is the Linux background-service path for headless startup. | `lms server status`, `lms ps`, OpenAI-compatible `/v1/models`, smoke test, logs. | Previous app version, old model file/path, previous TTL/server config. |
| llama.cpp | Binary commit/release, build flags, model file path, GGUF quantization, launch flags. | Usually a pinned binary or built checkout plus explicit `llama-server` command. | Listener proof, model route proof, `/slots` and `/metrics` if enabled, smoke test. | Previous binary/build folder, previous command, previous GGUF file. |
| vLLM | `vllm` package version or `vllm/vllm-openai` image tag, model id/revision, CUDA/ROCm path, cache mount. | Prefer an explicit container tag or locked Python environment for service work. | `/v1/models`, `/metrics`, logs, one OpenAI-compatible smoke test, GPU/resource proof. | Previous image tag or venv, same cache mount, old launch command. |
| SGLang | Package/image version, launch command, model path/id, metrics flag, scheduler settings. | Pin the Python environment or container and keep launch flags in source control. | `/v1/models` or route proof, `/metrics` when enabled, benchmark row, logs. | Previous environment/container and launch command. |
| Open WebUI | Container/app version tag, volume path, provider settings, `WEBUI_SECRET_KEY`, backup path. | Treat it as a stateful UI in front of providers, not as a disposable shell. | Container logs, UI version, provider connection, test prompt through provider. | Previous image tag, restored volume backup, same secret key, previous provider config. |

For desktop experimentation, a manual command can be acceptable. For any daily tool, team dependency, or capstone service proof, use a repeatable startup mode and write the restart test.

## Lab 0: Inventory Before Change

Create a dated lifecycle folder:

```powershell
$run = Get-Date -Format "yyyyMMdd-HHmmss"
$root = "D:\LLM-Runs\$run-lifecycle"
New-Item -ItemType Directory -Force $root | Out-Null
```

Capture only the commands that match the runtime.

Ollama:

```powershell
ollama --version | Set-Content "$root\ollama-version.txt"
Invoke-RestMethod http://localhost:11434/api/version |
  ConvertTo-Json -Depth 8 |
  Set-Content "$root\ollama-api-version.json"
Invoke-RestMethod http://localhost:11434/api/tags |
  ConvertTo-Json -Depth 8 |
  Set-Content "$root\ollama-tags.json"
Invoke-RestMethod http://localhost:11434/api/ps |
  ConvertTo-Json -Depth 8 |
  Set-Content "$root\ollama-ps.json"
```

LM Studio:

```powershell
lms --version | Set-Content "$root\lms-version.txt"
lms server status --json --quiet | Set-Content "$root\lmstudio-server-status.json"
lms ps --json | Set-Content "$root\lmstudio-ps.json"
```

Docker service:

```powershell
docker ps --format "{{.Image}} {{.Names}} {{.Ports}}" |
  Set-Content "$root\docker-ps.txt"
docker compose config |
  Set-Content "$root\docker-compose-rendered.yml"
```

Python environment:

```powershell
python -m pip freeze |
  Set-Content "$root\pip-freeze.txt"
```

Listener and process proof on Windows:

```powershell
Get-NetTCPConnection -State Listen |
  Where-Object { $_.LocalPort -in 11434,1234,8000,8080,30000 } |
  Export-Csv "$root\listeners-before.csv" -NoTypeInformation

Get-Process | Where-Object {
  $_.ProcessName -match 'ollama|lmstudio|llama|vllm|sglang|python|docker'
} | Select-Object ProcessName,Id,Path,CPU,WorkingSet64 |
  Export-Csv "$root\processes-before.csv" -NoTypeInformation
```

Write the baseline row into [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] before the change.

## Lab 1: Prove Startup Mode

Manual startup proof:

| Field | Value |
| --- | --- |
| Shell | PowerShell / WSL / Linux shell / terminal profile |
| Working directory |  |
| Command |  |
| Environment variables |  |
| Model/cache path |  |
| Endpoint |  |
| Restart test | stop process, start command, call health/smoke route |

Windows startup proof:

| Field | Value |
| --- | --- |
| Runtime | Ollama / LM Studio / llama.cpp / Docker Desktop / other |
| How it starts | app login item / scheduled task / Windows service / manual |
| Env vars source | user env / system env / service config / compose file |
| Port proof | listener CSV |
| Stop/start command |  |
| Reboot proof, if needed |  |

Linux/systemd proof:

```text
Service name:
Unit file or override path:
Environment file:
ExecStart:
Restart policy:
Working directory:
User:
Logs command:
```

Docker or Compose proof:

```text
Compose file:
Image tag:
Container name:
Volume mounts:
Ports:
Environment:
Restart policy:
Health/smoke command:
```

Do not rely on "it opens when I click the app" for a service you need to preserve. Write down the exact startup boundary.

## Lab 2: Backup And Pin

Back up what cannot be reconstructed quickly.

| Asset | Backup or pin method | Notes |
| --- | --- | --- |
| Model cache | Record `OLLAMA_MODELS`, Hugging Face cache mount, GGUF folder, LM Studio model folder, or vLLM cache mount. | Large; backup only accepted artifacts or record a re-download plan with exact revision. |
| Runtime | Installer, package lock, container image tag, binary release, git commit, or venv export. | Keep previous version until validation passes. |
| Open WebUI data | Back up the Docker volume or mounted data directory. | Preserve `WEBUI_SECRET_KEY`; changing it can break existing encrypted values. |
| Config | Compose file, systemd unit, env vars, launch script, firewall/proxy notes. | Store without leaking secrets into synced/public notes. |
| Client config | Base URL, model id, route, feature assumptions. | Needed when model ids or ports change. |
| Evidence | Baseline benchmark, quality, and observability folders. | This is how you prove the change was good or bad. |

For sensitive prompts, logs, uploaded files, or RAG corpora, keep backups inside the local privacy boundary defined by [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]].

## Lab 3: Upgrade One Layer

Change one layer at a time:

1. Runtime binary/package/container.
2. Model artifact/revision/quantization.
3. UI layer such as Open WebUI.
4. Startup/service wrapper.
5. Client app or SDK.
6. Driver/CUDA/ROCm environment.

Upgrade sequence:

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Freeze the current card and baseline rows. | Change Freeze Card, benchmark row, quality row. |
| 2 | Stop the service cleanly. | Stop command and process/listener after stop. |
| 3 | Back up state and config. | Backup path and restore note. |
| 4 | Apply the one intended change. | New version, tag, digest, commit, env var, or config diff. |
| 5 | Start the service. | Startup log, listener proof, health/model-list proof. |
| 6 | Run smoke tests. | Native or OpenAI-compatible minimal response. |
| 7 | Run benchmark and quality mini-suite. | Before/after rows. |
| 8 | Decide pass, hold, or rollback. | Decision row with reason. |

Abort if a second unrelated variable must change to make the first change work. Record the dependency and start a new card.

## Lab 4: Rollback

Rollback is not failure. It is a designed path back to the last known good service.

| Layer | Rollback action | Validation |
| --- | --- | --- |
| Runtime package | Reinstall previous installer/package, restore old venv, or use previous container tag. | Version proof, model-list route, smoke test. |
| Model artifact | Restore previous model file/cache path or re-pull exact tag/revision. | Model id/digest/path proof, quality sanity prompt. |
| Open WebUI | Stop container, restore backup volume, start previous image tag with same secret. | UI loads, provider connects, test prompt works. |
| Startup service | Restore prior unit/compose/scheduled-task config. | Stop/start proof and listener route proof. |
| Client contract | Restore previous base URL, model id, route, timeout, and feature flags. | Client harness non-streaming and streaming rows. |
| Driver/GPU stack | Restore only from a documented system snapshot or package plan. | GPU visible, runtime loads, benchmark does not regress unexpectedly. |

Rollback completion proof:

- previous version or tag is running
- previous model id/path is visible
- previous port and route respond
- one benchmark row is close to the last known good row
- one quality mini-suite row passes or the known limitation is unchanged
- the failed upgrade has a troubleshooting row

## Lab 5: Post-Change Validation

Run this after upgrade or rollback.

| Validation | Required proof | Source note |
| --- | --- | --- |
| Health/model state | Version, model list, loaded model, listener, endpoint route. | [[LLM/Study/Local LLM Observability and Operations Runbook|Observability and Operations Runbook]] |
| Smoke response | Minimal non-streaming response from native or OpenAI-compatible route. | [[LLM/Study/Local LLM Serving Runbook|Serving Runbook]] |
| API contract | Base URL, model id, route, streaming, errors, unsupported fields. | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|API Contract Lab]] |
| Client harness | Same harness request as baseline. | [[LLM/Study/Local LLM Client Harness Lab|Client Harness Lab]] |
| Benchmark | Same prompt, sampler, context, output cap, concurrency as baseline. | [[LLM/Study/Local LLM Inference Benchmark Log|Benchmark Log]] |
| Quantization/offload | Accepted quantization, GPU offload, CPU/GPU split, KV-cache precision, memory headroom, and quality result still match the intended service state. | [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Quantization and GPU Offload Lab]] |
| Prompt cache | Cold/warm/changed-prefix rows and cache evidence still match the intended service state. | [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Prompt Cache and KV Reuse Lab]] |
| Speculative decoding | No-spec/spec rows, accepted-token evidence, memory overhead, and quality result still match the intended service state. | [[LLM/Study/Local LLM Speculative Decoding Lab|Speculative Decoding Lab]] |
| Quality | Known-answer, schema, and workload prompts still pass. | [[LLM/Study/Local LLM Quality Evaluation Harness|Quality Evaluation Harness]] |
| Security | Bind address, auth, logs, RAG corpus, tools, and UI exposure unchanged or intentionally changed. | [[LLM/Study/Local LLM Security and Privacy Runbook|Security and Privacy Runbook]] |
| Deployment decision | Cost/ops owner/review trigger still correct. | [[LLM/Study/LLM Deployment Decision Matrix|Deployment Decision Matrix]] |

Pass signal: the change card has a before row, after row, rollback target, decision, and next review trigger.

## Failure Triage

| Symptom after change | Likely layer | First controlled action |
| --- | --- | --- |
| Service no longer starts | Runtime, service wrapper, missing env var, bad working directory. | Restore previous startup command; inspect logs; compare rendered service/compose config. |
| Model disappeared | Cache path, env var, UI provider path, re-download failed. | Check model cache path and model-list endpoint before re-pulling. |
| Model id changed | Runtime registry or client contract. | Copy exact served id, update API contract card, rerun client harness. |
| Same prompt slower | Cold load, cache/TTL, runtime version, context setting, scheduler, driver. | Compare baseline TTFT/TPOT/load metrics; run one warm and one cold request. |
| Quality regressed | Model revision, quantization, chat template, sampler, route behavior. | Freeze sampler and template; run quality harness before blaming runtime. |
| Memory or speed regressed after model/runtime change | Quantization, GPU offload, KV-cache precision, backend, or driver changed. | Run [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Quantization and GPU Offload Lab]] with the old and new service state. |
| Open WebUI loses settings | Volume path or secret changed. | Stop, restore volume backup, restore `WEBUI_SECRET_KEY`, restart previous image. |
| Endpoint exposed unexpectedly | Host binding, proxy, firewall, Docker port mapping. | Rebind to loopback; run security runbook before continuing. |
| Repeated-prefix speedup disappears | Prompt-cache path, slot state, prefix-cache flag, eviction, restart boundary, or prompt layout changed. | Run [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Prompt Cache and KV Reuse Lab]] before changing models. |
| Speculative speedup disappears or reverses | Draft model path, speculative flag, accepted-token rate, memory headroom, runtime version, or concurrency changed. | Run [[LLM/Study/Local LLM Speculative Decoding Lab|Speculative Decoding Lab]] before accepting the upgrade. |
| Rollback also fails | Backup incomplete or hidden dependency changed. | Name the missing dependency, restore the lower layer, and create a new troubleshooting row. |

## Completion Gate

This runbook is complete for one local setup when all are true:

- [ ] Change Freeze Card is filled before the change.
- [ ] Runtime version, model id/revision/digest, cache path, startup mode, endpoint, and data volume are recorded.
- [ ] Baseline benchmark, quality, and observability rows exist.
- [ ] Backup location and restore method are written before upgrade.
- [ ] [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner|Local LLM Service Lifecycle and Upgrade Runner]] output is saved when the change affects a daily-use service, UI, model cache, runtime version, startup wrapper, or rollback target.
- [ ] Upgrade changes one layer only, or a dependency split is recorded.
- [ ] Rollback target is known and tested at least once for daily-use services.
- [ ] Post-change validation includes health/model state, smoke response, client harness, benchmark, quality, and security checks.
- [ ] Any failure has a diagnostic row in [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]].
- [ ] [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]] is updated if owner, cost, uptime, privacy, or review trigger changed.

## References

Internal:

- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner]]
- [[LLM/Study/Local LLM Docker GPU Container Serving Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Lab]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab]]
- [[LLM/Study/Local LLM Speculative Decoding Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/2023 — Open Models and Agents/Open-Weight Model Ecosystem]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]

Current external docs checked 2026-06-15:

- [Ollama FAQ](https://docs.ollama.com/faq)
- [Ollama Windows documentation](https://docs.ollama.com/windows)
- [Ollama API documentation](https://docs.ollama.com/api/introduction)
- [LM Studio headless mode](https://lmstudio.ai/docs/developer/core/headless)
- [LM Studio llmster service mode](https://lmstudio.ai/docs/developer/core/headless_llmster)
- [LM Studio TTL and auto-evict](https://lmstudio.ai/docs/developer/core/ttl-and-auto-evict)
- [Open WebUI updating guide](https://docs.openwebui.com/getting-started/updating/)
- [Open WebUI backup guide](https://docs.openwebui.com/tutorials/maintenance/backups/)
- [Open WebUI quick start](https://docs.openwebui.com/getting-started/quick-start/)
- [vLLM Docker deployment](https://docs.vllm.ai/en/stable/deployment/docker/)
