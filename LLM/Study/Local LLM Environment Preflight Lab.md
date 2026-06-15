---
tags: [study, llm, inference, local-llm, environment, hardware, lab]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [practice]
---

# Local LLM Environment Preflight Lab

> **One-line summary** Local inference starts with proving the machine, runtime path, storage, accelerator, and network boundary before diagnosing model quality.

Use this before [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]], [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]], and [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]]. The provenance checklist decides whether the candidate artifact is allowed and reproducible; the sizing guide estimates what should fit; this lab records what the current machine and runtime can actually see. If the next action is the first Windows model pull, use [[LLM/Study/Local LLM Windows Model Store and Cache Plan|Local LLM Windows Model Store and Cache Plan]] before downloading so the cache path and disk owner are explicit.

Pair this with [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] when any endpoint listens on a port, and with [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] when the preflight evidence becomes part of a model/runtime comparison.

If the runtime path is vLLM or SGLang from a Windows machine, continue into [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab|Local LLM WSL CUDA vLLM and SGLang Setup Lab]] after this generic preflight. That lab proves the Windows driver, WSL 2 distro, WSL `nvidia-smi`, Python environment, loopback forwarding, `/v1/models`, and first OpenAI-compatible response before scheduler or throughput work begins. If the serving path uses Docker, run [[LLM/Study/Local LLM Docker GPU Container Serving Lab|Local LLM Docker GPU Container Serving Lab]] after WSL/Linux GPU proof to verify the Docker authority, NVIDIA container runtime, image tag, model/cache mount, loopback port mapping, provider endpoint, Compose contract, and Open WebUI route.

## Outcome

After this lab you should be able to:

- identify the OS, shell, CPU, RAM, GPU, VRAM, driver/runtime path, disk, and model cache location
- tell whether the intended runtime is using CPU, GPU, WSL, Docker, or a desktop backend
- confirm the local endpoint port is free before launch and bound only where intended after launch
- capture enough environment evidence to explain load failures, slow decode, OOMs, and connection errors
- decide whether to proceed with serving, choose a smaller model, change runtime, or fix the environment first

## Preflight Contract

| Layer | Evidence to capture | Why it matters |
| --- | --- | --- |
| Machine identity | Hostname, OS, shell, date, run id | Makes later benchmark rows attributable. |
| CPU/RAM | CPU name, core count, total RAM, free RAM | CPU-only and mixed offload paths depend on memory bandwidth and RAM headroom. |
| GPU/VRAM | GPU name, VRAM, driver visibility, utilization command output | GPU serving fails if the runtime cannot see the accelerator. |
| Runtime boundary | Windows native, WSL, Docker, remote Linux, desktop GUI | A GPU visible to Windows is not automatically visible to WSL or a container. |
| Disk/model store | Model cache path, free disk, model file size, format | Large model files and duplicate caches can exhaust disk before inference starts. |
| Runtime commands | Runtime version or command availability | Prevents debugging a missing install as a model failure. |
| Network port | Intended host, port, route, listener before/after launch | Distinguishes process, route, bind-address, and firewall failures. |
| Security boundary | Loopback/LAN/tunnel, auth decision, logging policy | A local server becomes a data boundary when it listens. |
| Baseline prompt | One tiny known prompt and expected reply shape | Proves the environment before running hard prompts. |

Do not paste secrets, tokens, private prompts, or retrieved documents into environment logs. The preflight log should describe the environment, not leak the workload.

## Decision Rule

Do not blame the model until the preflight answers these questions:

1. Can the runtime see the intended hardware path?
2. Is there enough RAM/VRAM/disk headroom for the chosen model and context?
3. Is the server actually listening on the intended host and port?
4. Is the client using the same base URL, route, and model id that the server exposes?
5. Is the endpoint boundary safe for the data you plan to send?

If any answer is unknown, record the setup as **hold** and fix the environment before comparing model quality.

## Windows PowerShell Snapshot

Use this when the local experiment starts from Windows, Ollama, LM Studio, llama.cpp, or a Windows client calling WSL.

```powershell
$RunId = [guid]::NewGuid().ToString()
$StartedAt = Get-Date

[pscustomobject]@{
  run_id = $RunId
  timestamp = $StartedAt.ToString("s")
  computer = $env:COMPUTERNAME
  user = $env:USERNAME
  powershell = $PSVersionTable.PSVersion.ToString()
} | ConvertTo-Json

Get-CimInstance Win32_OperatingSystem |
  Select-Object Caption, Version, OSArchitecture,
    @{Name="TotalMemoryGB";Expression={[math]::Round($_.TotalVisibleMemorySize / 1MB, 1)}},
    @{Name="FreeMemoryGB";Expression={[math]::Round($_.FreePhysicalMemory / 1MB, 1)}}

Get-CimInstance Win32_Processor |
  Select-Object Name, NumberOfCores, NumberOfLogicalProcessors

Get-CimInstance Win32_VideoController |
  Select-Object Name,
    @{Name="AdapterRAMGB";Expression={[math]::Round($_.AdapterRAM / 1GB, 1)}},
    DriverVersion

Get-PSDrive -PSProvider FileSystem |
  Select-Object Name,
    @{Name="FreeGB";Expression={[math]::Round($_.Free / 1GB, 1)}},
    @{Name="UsedGB";Expression={[math]::Round($_.Used / 1GB, 1)}}

"ollama","python","wsl","docker","nvidia-smi" | ForEach-Object {
  $cmd = Get-Command $_ -ErrorAction SilentlyContinue
  [pscustomobject]@{ command = $_; available = [bool]$cmd; path = $cmd.Source }
}
```

Optional checks when they are relevant:

```powershell
nvidia-smi
wsl --status
docker version
```

Pass signal: the snapshot identifies which runtime path is plausible before any model is downloaded or served.

## Linux, WSL, Or Server Snapshot

Use this inside WSL, Docker host shells, or Linux servers where vLLM, SGLang, or llama.cpp may run.

```bash
date -Is
hostname
uname -a
cat /etc/os-release
free -h
df -h
lscpu | head -40
python3 --version
which python3
which nvidia-smi || true
nvidia-smi || true
docker version || true
```

For listener and port checks:

```bash
ss -ltnp
curl -s http://127.0.0.1:<port>/v1/models
```

Pass signal: the shell where the server will run can see the expected accelerator, Python/runtime path, disk, and listening port.

## Port And Bind Plan

Plan the port before launch, then verify it after launch.

| Field | Record |
| --- | --- |
| Runtime | Ollama, LM Studio, llama.cpp, vLLM, SGLang, Open WebUI, or other |
| Intended host | `127.0.0.1` for a private local experiment |
| Intended port | 11434, 1234, 8000, 8001, 8080, 30000, or chosen port |
| Intended route | Native route or OpenAI-compatible `/v1/...` route |
| Auth decision | None only for loopback experiments, otherwise explicit |
| Client base URL | Exact base URL the client will use |
| Listener before launch | Empty or expected existing process |
| Listener after launch | Process is bound to intended address and port |

Windows listener checks:

```powershell
Get-NetTCPConnection -State Listen |
  Where-Object { $_.LocalPort -in 11434,1234,8000,8001,8080,30000 } |
  Select-Object LocalAddress, LocalPort, OwningProcess

Test-NetConnection -ComputerName 127.0.0.1 -Port <port>
```

Linux listener checks:

```bash
ss -ltnp | grep -E ':(11434|1234|8000|8001|8080|30000)\b'
curl -s http://127.0.0.1:<port>/v1/models
```

If the server binds to `0.0.0.0`, LAN, VPN, proxy, or tunnel, stop and run the shared-service checklist in [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]].

## Model Store And Provenance

Before serving a model, record where the weights came from and where they live.

| Field | Record |
| --- | --- |
| Model id or file | Hugging Face id, Ollama tag, LM Studio id, or local GGUF path |
| Source | Registry, local file, internal artifact, or converted model |
| License/usage boundary | Allowed local use, research use, commercial use, or unknown |
| Format | GGUF, safetensors, GPTQ, AWQ, FP16/BF16, INT8, or other |
| Quantization | Exact quant name if known |
| File size | Size on disk before loading |
| Cache path | Runtime model cache or explicit model directory |
| Checksum | Hash if available or required by workflow |
| Sensitive data | Whether the model, adapter, or prompt data is private |

For Windows cache and model-store placement before the first pull, use [[LLM/Study/Local LLM Windows Model Store and Cache Plan|Local LLM Windows Model Store and Cache Plan]]. For the full acquisition checklist, use [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]]. This connects practical setup to [[LLM/2023 — Open Models and Agents/Open-Weight Model Ecosystem|Open-Weight Model Ecosystem]] and [[LLM/2022 — Alignment and Chat/Quantization|Quantization]]. Open weights give deployment control, but license, format, and runtime compatibility still matter.

## Runtime Path Matrix

| Path | First proof | Common trap |
| --- | --- | --- |
| Windows native desktop | Runtime GUI/CLI opens, model list visible, loopback API responds | Assuming GUI chat success means API route and model id are correct. |
| Windows native CLI | Command exists, model loads, process appears in listener list if serving | Mixing model caches between tools and testing the wrong model. |
| WSL server | WSL shell sees Python/runtime and GPU if needed | Windows client base URL, firewall, or localhost forwarding differs from server shell. |
| Docker server | Container sees model path, port mapping, and GPU if needed; use [[LLM/Study/Local LLM Docker GPU Container Serving Lab|Docker GPU Container Serving Lab]] for the full proof. | Host has GPU but container has no accelerator access. |
| Remote Linux server | SSH shell sees accelerator, disk, and listener | Exposing API before auth, firewall, and logs are planned. |

The practical rule: run the preflight from the same boundary that will load the model. A Windows PowerShell check does not prove Docker GPU access; a WSL check does not prove a Windows desktop GUI can use the same model file.

## Failure Triage

| Symptom | Likely layer | First check |
| --- | --- | --- |
| `nvidia-smi` missing or errors | GPU driver or runtime boundary | Confirm whether this experiment is CPU-only, Windows GPU, WSL GPU, container GPU, or remote GPU. |
| Runtime says CPU only | Backend selection or GPU visibility | Check runtime logs and hardware visibility from the server shell. |
| Model download fails | Network, disk, model id, license gate, or cache path | Verify model id, free disk, auth requirement, and cache directory. |
| Model file exists but will not load | Format/runtime mismatch or memory shortage | Check format support, quantization, RAM/VRAM, and runtime error text. |
| Immediate OOM | Weight memory or driver/runtime overhead | Use smaller model, stronger quantization, lower GPU offload, or more headroom. |
| OOM only on long prompts | KV-cache pressure | Reduce context, concurrency, or retrieved chunks. |
| Port already in use | Existing runtime or stale process | Identify owning process before changing ports. |
| Connection refused | Server process not listening | Check process, bind address, port, and client base URL. |
| 404 on client route | Wrong route or missing `/v1` | Compare native API route versus OpenAI-compatible route. |
| Endpoint reachable from another device unexpectedly | Bind/firewall/proxy issue | Stop server, bind to loopback, and run the security runbook. |
| Slow first token | Prefill, long context, queueing, or cold load | Record prompt tokens, load time, TTFT, and server logs. |
| Slow later tokens | Decode bottleneck or weak backend | Check model size, quantization, GPU offload, memory bandwidth, and utilization. |

## Preflight Log Template

Copy this into a run note before the first endpoint smoke test.

| Field | Value |
| --- | --- |
| Preflight run id |  |
| Date/time |  |
| Host / OS / shell |  |
| Runtime boundary | Windows native / WSL / Docker / remote Linux / desktop GUI |
| CPU / RAM |  |
| GPU / VRAM / driver visibility |  |
| Free disk and model cache |  |
| Runtime commands available |  |
| Candidate model / format / quantization |  |
| Expected memory risk | Low / Medium / High |
| Intended host:port |  |
| Intended API route |  |
| Auth and logging decision |  |
| Listener before launch |  |
| Listener after launch |  |
| First smoke prompt |  |
| Preflight decision | Pass / Hold / Fail |
| Next action | Serve / resize model / fix runtime / fix security boundary |

## Completion Gate

This lab is complete when you have:

- [ ] one hardware/OS/runtime snapshot from the environment that will load the model
- [ ] one disk/model-store/provenance row
- [ ] one explicit host, port, route, auth, and logging decision
- [ ] one listener check before launch and one after launch
- [ ] one endpoint smoke test from [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]]
- [ ] one benchmark row that carries the environment fields into [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]]
- [ ] one written decision: proceed, choose smaller model, change runtime, or fix environment first

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Windows Model Store and Cache Plan]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab]]
- [[LLM/Study/Local LLM Docker GPU Container Serving Lab]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/2022 — Alignment and Chat/Quantization]]
- [[LLM/2023 — Open Models and Agents/Open-Weight Model Ecosystem]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching]]
- [[chunk-llm-214 KV Cache Memory Bandwidth Bottleneck]]
- [[chunk-llm-208 GPTQ Standard for Open-Source Deployment]]
- [[chunk-llm-211 AWQ INT4 Edge Deployment Performance]]
- [[chunk-llm-117 PagedAttention Eliminates KV Fragmentation]]
