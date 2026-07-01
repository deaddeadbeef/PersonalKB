---
tags: [study, llm, inference, local-llm, wsl, cuda, vllm, sglang, serving]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM WSL CUDA vLLM and SGLang Setup Lab

> **One-line summary** This lab proves the Windows-to-WSL GPU path for production-style local serving before you ask vLLM or SGLang to load a model.

Use this after [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]], [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]], and [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]] when the next runtime candidate is vLLM or SGLang from a Windows machine.

Then use [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] for the endpoint smoke test, [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] for client compatibility, [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]] for metrics/logs, and [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Local LLM Serving Internals and Scheduler Lab]] before tuning batching, queueing, prefix cache, or scheduler settings.

If the next step is a containerized service rather than a WSL Python process, continue into [[LLM/Study/Local LLM Docker GPU Container Serving Lab|Local LLM Docker GPU Container Serving Lab]] after this lab. The Docker lab proves the container GPU boundary, pinned provider image, model/cache mount, loopback port publishing, Compose file, logs, metrics, and Open WebUI routing.

## Outcome

After this lab you should be able to:

- prove Windows, WSL, the NVIDIA driver, and the Linux runtime all see the same GPU boundary
- install vLLM and SGLang in separate Python environments so dependency problems are diagnosable
- launch one OpenAI-compatible endpoint on loopback from WSL
- call that endpoint from both WSL and Windows PowerShell
- record the model id, base URL, `/v1/models` response, smoke response, logs, metrics, and teardown command
- name the failed layer when setup breaks: Windows driver, WSL kernel, WSL GPU visibility, Python environment, CUDA/PyTorch, runtime install, model artifact, port binding, localhost forwarding, or client route

## Decision Rule

Do not debug vLLM or SGLang model quality until these are all true:

1. Windows `nvidia-smi` works.
2. WSL is version 2 and the target distro starts cleanly.
3. Inside WSL, `nvidia-smi` works from the same shell that will launch the server.
4. The Python environment and package install are inside WSL, not mixed with Windows Python.
5. The server binds to loopback for the first run.
6. `/v1/models` works before `/v1/chat/completions`.
7. Windows PowerShell can call the WSL loopback endpoint or the run records the forwarding blocker explicitly.

If one item fails, stop and repair that layer before changing model, quantization, prompt, or client library.

## Phase 0: Boundary Card

Fill this before installing anything new.

| Field | Value |
| --- | --- |
| Run id |  |
| Date/time |  |
| Windows version |  |
| WSL version/status |  |
| WSL distro |  |
| GPU model and VRAM |  |
| Windows driver version |  |
| WSL `nvidia-smi` result | Pass / Hold / Fail |
| Runtime candidate | vLLM / SGLang / both |
| Model id/path |  |
| Artifact/provenance link |  |
| Compatibility card link |  |
| First endpoint host:port | `127.0.0.1:8000` / `127.0.0.1:30000` / other |
| Windows client path | PowerShell / Python / app |
| Security boundary | loopback only / other with reason |

## Phase 1: Windows Host Proof

Run these in PowerShell.

```powershell
wsl --status
wsl -l -v
nvidia-smi

Get-NetTCPConnection -State Listen |
  Where-Object { $_.LocalPort -in 8000,30000 } |
  Select-Object LocalAddress, LocalPort, OwningProcess
```

Pass signal:

- the intended distro is WSL 2
- the NVIDIA driver is visible from Windows
- the intended server port is free, or the owning process is named before changing ports

If Windows `nvidia-smi` fails, this is not a vLLM/SGLang problem yet. Fix the Windows driver path first.

## Phase 2: WSL GPU Proof

Open the target WSL distro. Run the proof from the same shell that will launch the server.

```bash
date -Is
uname -a
cat /etc/os-release
python3 --version
which python3
df -h
free -h
which nvidia-smi || true
nvidia-smi
```

Optional CUDA/PyTorch check after PyTorch is installed:

```bash
python - <<'PY'
import torch
print("torch", torch.__version__)
print("cuda_available", torch.cuda.is_available())
print("device_count", torch.cuda.device_count())
if torch.cuda.is_available():
    print("device_0", torch.cuda.get_device_name(0))
PY
```

Pass signal: WSL sees the GPU from the server shell. If Windows sees the GPU but WSL does not, keep the failure in the WSL/CUDA layer.

## Phase 3: Python Environment Plan

Use separate environments for vLLM and SGLang unless you are deliberately testing dependency compatibility.

The conservative layout:

| Runtime | Environment | Reason |
| --- | --- | --- |
| vLLM | `~/venvs/vllm` or `.venv-vllm` | vLLM depends on specific PyTorch/CUDA wheels and serving packages. |
| SGLang | `~/venvs/sglang` or `.venv-sglang` | SGLang may install different kernels, Torch versions, or backend packages. |
| Client test | either runtime env or a tiny client env | Keeps endpoint tests separate from server package failures if needed. |

`uv` is a good default when available because current vLLM and SGLang docs recommend it for installation speed and backend selection. `venv` plus `pip` is acceptable if that is the simpler environment boundary.

Example vLLM environment:

```bash
python3 -m venv ~/venvs/vllm
source ~/venvs/vllm/bin/activate
python -m pip install -U pip
python -m pip install uv
uv pip install vllm --torch-backend=auto
python -m pip freeze > vllm-freeze.txt
```

Example SGLang environment:

```bash
python3 -m venv ~/venvs/sglang
source ~/venvs/sglang/bin/activate
python -m pip install -U pip
python -m pip install uv
uv pip install sglang
python -m pip freeze > sglang-freeze.txt
```

If the install fails, record:

- Python version
- command used
- full error tail
- CUDA/driver evidence
- whether the failed package was Torch, runtime core, runtime kernel, or an optional dependency

Do not install Linux NVIDIA display drivers inside WSL as a first fix. WSL CUDA relies on the Windows-side driver path plus WSL support; follow the Microsoft/NVIDIA WSL CUDA docs for driver/toolkit boundaries.

## Phase 4: vLLM OpenAI-Compatible Smoke

Use a small compatible model first. The goal is endpoint proof, not maximum quality.

In WSL:

```bash
source ~/venvs/vllm/bin/activate
vllm serve <model-id> \
  --host 127.0.0.1 \
  --port 8000
```

In another WSL shell:

```bash
curl -s http://127.0.0.1:8000/v1/models
curl -s http://127.0.0.1:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "<served-model-id>",
    "messages": [{"role": "user", "content": "Reply with exactly: local llm ok"}],
    "temperature": 0,
    "max_tokens": 16
  }'
```

From Windows PowerShell:

```powershell
$BaseUrl = "http://127.0.0.1:8000/v1"
$Model = "<served-model-id>"
$Body = @{
  model = $Model
  messages = @(@{ role = "user"; content = "Reply with exactly: local llm ok" })
  temperature = 0
  max_tokens = 16
} | ConvertTo-Json -Depth 6

Invoke-RestMethod `
  -Uri "$BaseUrl/chat/completions" `
  -Method Post `
  -ContentType "application/json" `
  -Body $Body
```

Pass signal: `/v1/models` returns the served id, the WSL chat smoke works, and the Windows client can call the same loopback endpoint or records the forwarding failure.

## Phase 5: SGLang OpenAI-Compatible Smoke

Use a small compatible model first. In WSL:

```bash
source ~/venvs/sglang/bin/activate
python3 -m sglang.launch_server \
  --model-path <model-id-or-path> \
  --host 127.0.0.1 \
  --port 30000
```

In another WSL shell:

```bash
curl -s http://127.0.0.1:30000/v1/models
curl -s http://127.0.0.1:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "<served-model-id>",
    "messages": [{"role": "user", "content": "Reply with exactly: local llm ok"}],
    "temperature": 0,
    "max_tokens": 16
  }'
```

From Windows PowerShell:

```powershell
$BaseUrl = "http://127.0.0.1:30000/v1"
$Model = "<served-model-id>"
$Body = @{
  model = $Model
  messages = @(@{ role = "user"; content = "Reply with exactly: local llm ok" })
  temperature = 0
  max_tokens = 16
} | ConvertTo-Json -Depth 6

Invoke-RestMethod `
  -Uri "$BaseUrl/chat/completions" `
  -Method Post `
  -ContentType "application/json" `
  -Body $Body
```

Pass signal: the server announces readiness, `/v1/models` returns the served model, and the chat smoke works from WSL and Windows.

## Phase 6: Metrics, Logs, And Resource Pressure

Before calling the setup usable, capture:

```bash
nvidia-smi
curl -s http://127.0.0.1:<port>/metrics | head -40
ss -ltnp | grep -E ':(8000|30000)\b'
```

Save these artifacts:

| Artifact | Why |
| --- | --- |
| launch command | Reproduces model id, host, port, and runtime flags. |
| package freeze | Reproduces Python dependency state. |
| `/v1/models` response | Proves the served model id. |
| smoke response | Proves OpenAI-compatible inference. |
| server log tail | Shows load, CUDA, scheduler, and warning context. |
| `nvidia-smi` during load/request | Shows GPU visibility and pressure. |
| `/metrics` response or unsupported note | Feeds observability and scheduler labs. |
| Windows PowerShell response | Proves Windows-to-WSL client route. |

If `/metrics` is unavailable, record whether the runtime needs a metrics flag, a newer version, or a different endpoint. Do not infer scheduler behavior without logs, metrics, or benchmark evidence.

## Phase 7: Handoff Decisions

| If the result is | Next note |
| --- | --- |
| Endpoint works but client behavior is uncertain | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|OpenAI-compatible API contract]] |
| Endpoint works but latency/memory is unexplained | [[LLM/Study/Local LLM Observability and Operations Runbook|Observability and operations]] |
| You need throughput or multi-client use | [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Serving internals]] then [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab|Concurrency and batch throughput]] |
| Repeated-prefix prompts should be faster | [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Prompt cache and KV reuse]] |
| First endpoint works and you want a runtime decision | [[LLM/Study/Local LLM Runtime Comparison Lab|Runtime comparison]] |
| WSL GPU proof works and you want a repeatable container service | [[LLM/Study/Local LLM Docker GPU Container Serving Lab|Docker GPU container serving]] |
| Binding, auth, or logs might expose private data | [[LLM/Study/Local LLM Security and Privacy Runbook|Security and privacy]] |

## Failure Triage

| Symptom | Failed layer | First controlled check |
| --- | --- | --- |
| Windows `nvidia-smi` fails | Windows driver/GPU | Reinstall/update driver according to Microsoft/NVIDIA WSL CUDA docs. |
| WSL distro is version 1 | WSL boundary | Convert or create a WSL 2 distro before GPU serving. |
| Windows sees GPU but WSL `nvidia-smi` fails | WSL CUDA path | Check WSL updates, distro, driver/toolkit boundary, and NVIDIA WSL guide. |
| Python command is Windows path from WSL shell | Environment mix | Use WSL Python and recreate the venv inside Linux filesystem. |
| Torch says CUDA unavailable | Python/CUDA wheel | Check installed Torch backend, driver version, and package install command. |
| Runtime install fails in kernel package | Runtime dependency | Record exact package/error; check runtime docs for supported Python/CUDA/hardware. |
| Model download fails | Artifact/auth/cache | Use artifact download/cache lab; check Hugging Face token, disk, revision, and local path. |
| Server starts but `/v1/models` fails | Process/port/route | Check logs, listener, host, and base URL. |
| WSL curl works but Windows fails | localhost forwarding/firewall | Test `127.0.0.1`, `localhost`, WSL IP, firewall, and bind address without changing model. |
| `/chat/completions` returns model-not-found | Served id mismatch | Copy exact id from `/v1/models`. |
| Immediate OOM | Weights/runtime overhead | Use smaller model, lower precision/quantization if supported, or lower memory utilization. |
| OOM under concurrent or long prompts | KV cache | Reduce context, output cap, or concurrency; hand off to scheduler/concurrency labs. |

## Completion Gate

This lab is complete when you have:

- [ ] Windows WSL/GPU evidence
- [ ] WSL GPU evidence from the server shell
- [ ] separate Python environment state for the runtime tested
- [ ] one vLLM or SGLang launch command bound to loopback
- [ ] `/v1/models` response
- [ ] one WSL chat-completions smoke response
- [ ] one Windows PowerShell chat-completions smoke response or explicit forwarding blocker
- [ ] server logs and `nvidia-smi` evidence
- [ ] metrics response or explicit unsupported/flag-required note
- [ ] decision: keep runtime, compare runtimes, fix environment, choose smaller model, or stop

## References

Internal evidence:

- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Docker GPU Container Serving Lab]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]]
- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/_chunks/chunk-llm-117 PagedAttention Eliminates KV Fragmentation|chunk-llm-117]]
- [[LLM/_chunks/chunk-llm-118 vLLM Continuous Batching Throughput|chunk-llm-118]]
- [[LLM/_chunks/chunk-llm-120 vLLM De Facto Serving Framework|chunk-llm-120]]

Current external docs checked 2026-06-15:

- [Microsoft: Enable NVIDIA CUDA on WSL 2](https://learn.microsoft.com/en-us/windows/ai/directml/gpu-cuda-in-wsl)
- [NVIDIA CUDA on WSL User Guide](https://docs.nvidia.com/cuda/wsl-user-guide/index.html)
- [vLLM quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/)
- [vLLM GPU installation](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/)
- [vLLM OpenAI-compatible server](https://docs.vllm.ai/en/stable/serving/online_serving/openai_compatible_server/)
- [SGLang installation](https://docs.sglang.io/docs/get-started/install)
- [SGLang quickstart](https://docs.sglang.io/docs/get-started/quickstart)
- [SGLang OpenAI-compatible APIs](https://docs.sglang.io/docs/basic_usage/openai_api)
