---
tags: [study, llm, inference, local-llm, docker, gpu, cuda, vllm, sglang, open-webui, serving]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM Docker GPU Container Serving Lab

> **One-line summary** This lab proves that Docker, the GPU runtime, model/cache mounts, loopback ports, vLLM or SGLang, and Open WebUI all work together before you treat a containerized local LLM as a service.

Use this after [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]], [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]], [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]], and, on Windows GPU workstations, [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab|Local LLM WSL CUDA vLLM and SGLang Setup Lab]].

Then use [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] for endpoint smoke tests, [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] before generic client wiring, [[LLM/Study/Local Open WebUI Provider Integration Runner|Local Open WebUI Provider Integration Runner]] when Open WebUI becomes the user-facing route, [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]] for logs/metrics/resource pressure, [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook|Local LLM Service Lifecycle and Upgrade Runbook]] for startup/backup/rollback, and [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] before exposing anything beyond loopback.

## Outcome

After this lab you should be able to:

- decide whether Docker Desktop WSL 2 integration or a Linux Docker Engine is the active Docker authority
- prove the host Docker engine works before model serving
- prove a CUDA container can see the GPU with `--gpus all`
- run either vLLM or SGLang in a pinned container image with a known model/cache mount
- bind the host port to loopback while the process inside the container listens on `0.0.0.0`
- call `/v1/models` and `/v1/chat/completions` from the host
- collect logs, `docker stats`, container `nvidia-smi`, listener evidence, and `/metrics` or a metrics-gap note
- connect Open WebUI only after the provider endpoint is already proven
- save a Compose file as the service contract for future lifecycle work

## Decision Rule

Do not debug model quality, prompt behavior, batching, or scheduler settings until these are all true:

1. The intended Docker engine is clear: Docker Desktop WSL 2 backend, Linux Docker Engine inside WSL, or remote Linux Docker Engine.
2. `docker version` and `docker info` work from the shell that will launch the provider.
3. The host GPU is visible from the host boundary that owns Docker.
4. A CUDA test container sees the GPU with `docker run --gpus all ... nvidia-smi`.
5. The model/cache mount is readable inside the provider container.
6. The provider container publishes only the intended host loopback port.
7. `/v1/models` works from the host before `/v1/chat/completions`.
8. Open WebUI is connected after provider proof, not used as the first diagnostic surface.

If one item is unknown, record the result as **hold** and repair that layer before changing model, quantization, prompt, or runtime flags.

## Phase 0: Container Boundary Card

Fill this before running a provider container.

| Field | Value |
| --- | --- |
| Run id |  |
| Date/time |  |
| Host OS | Windows / WSL / Linux / remote |
| Docker authority | Docker Desktop WSL 2 / Linux Docker Engine / remote Docker |
| Docker context |  |
| GPU model and VRAM |  |
| Host GPU command result |  |
| Container GPU command result |  |
| Runtime candidate | vLLM / SGLang / both |
| Provider image and tag/digest |  |
| Open WebUI image and tag/digest |  |
| Model id/path and revision |  |
| Host model/cache mount |  |
| Container model/cache path |  |
| Provider host port | `127.0.0.1:8000` / `127.0.0.1:30000` / other |
| Container listen address | `0.0.0.0:<port>` |
| Client base URL |  |
| Secrets source | `.env.local` / local secret store / none |
| Security boundary | loopback only / other with reason |

## Phase 1: Choose One Docker Authority

Do not mix Docker Desktop and an unmanaged Docker Engine inside WSL unless you are deliberately comparing Docker authorities.

| Path | Use when | First proof |
| --- | --- | --- |
| Docker Desktop WSL 2 backend | Windows is the workstation and Docker Desktop owns containers. | Docker Desktop running, WSL integration enabled, `docker context ls`, GPU container smoke. |
| Linux Docker Engine in WSL | You intentionally installed Docker inside WSL and will run commands from that distro. | `systemctl status docker` or equivalent, NVIDIA Container Toolkit configured, GPU container smoke. |
| Remote Linux Docker Engine | The model server is on a Linux host. | SSH shell, Docker daemon, NVIDIA driver/runtime, firewall/bind plan. |

Windows host checks:

```powershell
wsl --status
wsl -l -v
docker version
docker context ls
docker info
nvidia-smi
```

Linux or WSL Docker host checks:

```bash
date -Is
uname -a
cat /etc/os-release
docker version
docker context ls
docker info
which nvidia-smi || true
nvidia-smi || true
```

If Docker Desktop owns the daemon, use Docker Desktop's WSL integration and do not assume a separate WSL Docker Engine has the same containers, volumes, contexts, or GPU runtime. If a Linux Docker Engine owns the daemon, install and configure NVIDIA Container Toolkit according to the NVIDIA guide before blaming vLLM or SGLang.

## Phase 2: GPU Container Smoke

Use an explicit CUDA image tag rather than `latest`.

```bash
docker run --rm --gpus all nvidia/cuda:12.9.0-base-ubuntu22.04 nvidia-smi
```

Alternative Docker Desktop GPU sample:

```bash
docker run --rm --gpus=all nvcr.io/nvidia/k8s/cuda-sample:nbody nbody -gpu -benchmark
```

Pass signal:

- the command exits successfully
- the container output names the expected GPU
- the Docker shell and GPU path are the same boundary you will use for the provider container

Common failures:

| Symptom | Likely layer | First controlled check |
| --- | --- | --- |
| `could not select device driver "" with capabilities: [gpu]` | Docker GPU runtime not configured | Docker Desktop GPU support or NVIDIA Container Toolkit configuration. |
| Host `nvidia-smi` works but container `nvidia-smi` fails | Container runtime boundary | Check Docker context, NVIDIA runtime, Docker Desktop WSL 2 backend, or `nvidia-ctk runtime configure`. |
| Docker command hits the wrong daemon | Docker context mismatch | `docker context ls` and `docker info`; pick one authority. |
| CUDA image pulls but provider image cannot load GPU kernels | Provider image/runtime compatibility | Check provider docs, image tag, CUDA/PyTorch expectation, and GPU architecture. |

## Phase 3: Image, Cache, And Secret Plan

Pin container images the same way you pin model revisions.

| Component | Record | Why |
| --- | --- | --- |
| vLLM provider | `vllm/vllm-openai:<tag>` or digest | Avoid accidental runtime/CUDA/PyTorch changes. |
| SGLang provider | `lmsysorg/sglang:<tag>` or digest | SGLang tags may encode CUDA/backend variants; record the exact image. |
| Open WebUI | `ghcr.io/open-webui/open-webui:<tag>` or digest | The UI stores state and provider config; it is not disposable once used. |
| Hugging Face cache | host path and container mount path | Prevent duplicate downloads and prove artifact custody. |
| Model directory | host path and container mount path when not using HF cache | Keeps local files reproducible and inspectable. |
| Env file | local path, not committed | Keeps `HF_TOKEN`, provider keys, and `WEBUI_SECRET_KEY` out of the vault. |
| Compose file | path and owner | Becomes the service lifecycle contract. |

Secrets rule: do not commit `.env.local`, raw tokens, API keys, private prompts, or provider passwords. The note records that a secret exists and where it is managed, not the secret value.

Example `.env.local` shape:

```dotenv
HF_TOKEN=<set locally, do not commit>
```

Use the artifact download/cache lab to prove exact model bytes, revision, file list, hash or verification result, and cleanup plan before this lab claims reproducibility.

## Phase 4: vLLM Container Smoke

Use a small compatible model first. The goal is container/service proof, not maximum quality.

PowerShell or Bash command shape:

```powershell
docker run --rm --gpus all --name local-vllm `
  --ipc=host `
  -p 127.0.0.1:8000:8000 `
  -v <host-hf-cache>:/root/.cache/huggingface `
  --env-file .env.local `
  vllm/vllm-openai:<tag> `
  --model <model-id> `
  --host 0.0.0.0 `
  --port 8000
```

Why both addresses matter:

- inside the container, the server usually needs `--host 0.0.0.0` so Docker can publish it
- on the host, `-p 127.0.0.1:8000:8000` keeps the first run loopback-only

Host smoke:

```powershell
$BaseUrl = "http://127.0.0.1:8000/v1"
$Model = "<served-model-id>"

Invoke-RestMethod -Uri "$BaseUrl/models" -Method Get

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

Container proof while it runs:

```bash
docker logs --tail 120 local-vllm
docker exec local-vllm nvidia-smi
docker stats --no-stream local-vllm
curl -s http://127.0.0.1:8000/metrics | head -40
```

Pass signal: `/v1/models` returns the served id, the chat smoke returns the expected response shape, the container sees the GPU, logs show the selected model loaded, and the host listener is loopback-only.

## Phase 5: SGLang Container Smoke

Use the image and CUDA/backend tag recommended by the current SGLang install docs for your accelerator. Pin the exact tag or digest after the first working run.

```powershell
docker run --rm --gpus all --name local-sglang `
  --ipc=host `
  --shm-size 32g `
  -p 127.0.0.1:30000:30000 `
  -v <host-hf-cache>:/root/.cache/huggingface `
  --env-file .env.local `
  lmsysorg/sglang:<tag> `
  python3 -m sglang.launch_server `
    --model-path <model-id-or-path> `
    --host 0.0.0.0 `
    --port 30000
```

Host smoke:

```powershell
$BaseUrl = "http://127.0.0.1:30000/v1"
$Model = "<served-model-id>"

Invoke-RestMethod -Uri "$BaseUrl/models" -Method Get

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

Container proof while it runs:

```bash
docker logs --tail 120 local-sglang
docker exec local-sglang nvidia-smi
docker stats --no-stream local-sglang
curl -s http://127.0.0.1:30000/metrics | head -40
```

If `/metrics` is not enabled or not available, record the flag/version/documentation reason instead of inventing scheduler evidence.

## Phase 6: Compose Service Contract

After one provider works with `docker run`, move one provider into Compose. Do not define vLLM and SGLang as simultaneous defaults unless you have VRAM and port plans for both.

Example vLLM Compose contract:

```yaml
services:
  vllm:
    image: vllm/vllm-openai:<tag>
    command:
      - --model
      - <model-id>
      - --host
      - 0.0.0.0
      - --port
      - "8000"
    ports:
      - "127.0.0.1:8000:8000"
    volumes:
      - type: bind
        source: <host-hf-cache>
        target: /root/.cache/huggingface
    env_file:
      - .env.local
    ipc: host
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
    restart: unless-stopped
```

Compose proof:

```bash
docker compose config
docker compose up -d
docker compose ps
docker compose logs --tail 120 vllm
curl -s http://127.0.0.1:8000/v1/models
docker compose down
```

Record whether `count` or `device_ids` is used for the GPU reservation. Do not set both for the same service.

## Phase 7: Open WebUI Over A Proven Provider

Open WebUI is a UI over providers. Do not use it to decide whether vLLM or SGLang loaded correctly; first prove the provider with host `curl` or PowerShell.

Common provider URLs:

| Open WebUI location | Provider URL shape |
| --- | --- |
| Open WebUI running on the host | `http://127.0.0.1:8000/v1` or `http://127.0.0.1:30000/v1` |
| Open WebUI container, provider published on host | `http://host.docker.internal:8000/v1` or `http://host.docker.internal:30000/v1` |
| Same Compose network as provider service | `http://vllm:8000/v1` or `http://sglang:30000/v1` |

Example standalone UI container:

```powershell
docker run -d --name open-webui `
  -p 127.0.0.1:3000:8080 `
  -v open-webui:/app/backend/data `
  --env-file .env.open-webui `
  ghcr.io/open-webui/open-webui:<tag>
```

Open WebUI evidence to save:

| Evidence | Why |
| --- | --- |
| Image tag/digest | UI updates can change settings and providers. |
| Volume name/path | Chat history, users, uploaded files, and provider settings are state. |
| `WEBUI_SECRET_KEY` management note | Changing it can break encrypted values. |
| Provider base URL | Differentiates host, container, and Compose network routing. |
| Test prompt through UI | Proves the UI reaches the already-proven provider. |
| Backup/restore note | Required before treating the UI as persistent. |

After saving these artifacts, run [[LLM/Study/Local Open WebUI Provider Integration Runner|Local Open WebUI Provider Integration Runner]] so the Open WebUI transcript is tied to the intended provider, expected model, loopback boundary, persistent data path, and secret-key handling before it supports app, lifecycle, or capstone evidence.

## Phase 8: Observability And Teardown

Before calling the container setup usable, capture:

```bash
docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Ports}}\t{{.Status}}"
docker logs --tail 120 <provider-container>
docker stats --no-stream <provider-container>
docker inspect <provider-container>
docker exec <provider-container> nvidia-smi
curl -s http://127.0.0.1:<provider-port>/v1/models
curl -s http://127.0.0.1:<provider-port>/metrics | head -40
```

Windows listener check:

```powershell
Get-NetTCPConnection -State Listen |
  Where-Object { $_.LocalPort -in 8000,30000,3000,8080 } |
  Select-Object LocalAddress, LocalPort, OwningProcess
```

Teardown:

```bash
docker stop local-vllm local-sglang open-webui 2>/dev/null || true
docker rm local-vllm local-sglang 2>/dev/null || true
```

Do not delete model caches, named Open WebUI volumes, or Compose volumes unless the cleanup plan explicitly says those artifacts are disposable.

## Failure Triage

| Symptom | Failed layer | First controlled check |
| --- | --- | --- |
| Docker works in PowerShell but not WSL | Docker authority/context | `docker context ls`, Docker Desktop WSL integration, or Linux Docker Engine status. |
| Host sees GPU but CUDA container does not | Docker GPU runtime | Docker Desktop GPU support or NVIDIA Container Toolkit configuration. |
| Provider container exits during load | Model/runtime/image | `docker logs`, image tag, model id/revision, cache mount, HF token, VRAM. |
| Provider logs ready but host curl refused | Port publish or listener | `docker ps`, `docker inspect`, host `127.0.0.1:<port>`, container listen address. |
| `/v1/models` works but chat route fails | Served model id or API contract | Copy model id from `/v1/models`; run API contract lab. |
| WebUI cannot connect but host curl works | Container network route | Use `host.docker.internal` or same-network service name; verify provider URL in WebUI. |
| Endpoint reachable from LAN unexpectedly | Bind or firewall | Stop container, rebind `127.0.0.1:host_port:container_port`, run security runbook. |
| Metrics missing | Runtime flag/version | Check provider docs and record unsupported/flag-required note. |
| Update breaks working setup | Lifecycle/rollback | Restore previous image tag, Compose file, model/cache path, and Open WebUI volume/secret. |

## Completion Gate

This lab is complete when you have:

- [ ] one Docker authority decision
- [ ] `docker version`, `docker info`, and Docker context evidence
- [ ] host GPU proof from the Docker-owning boundary
- [ ] CUDA container `nvidia-smi` or explicit CPU-only/no-GPU blocker
- [ ] pinned provider image tag or digest
- [ ] model/cache mount proof
- [ ] one vLLM or SGLang container launch bound to host loopback
- [ ] `/v1/models` response from the host
- [ ] one OpenAI-compatible chat smoke response from the host
- [ ] container logs, `docker stats`, listener proof, and container `nvidia-smi`
- [ ] `/metrics` response or explicit unsupported/flag-required note
- [ ] Compose file validated with `docker compose config`
- [ ] Open WebUI connected only after provider proof, or explicitly skipped
- [ ] Open WebUI provider integration runner output saved when UI transcript or provider routing evidence is used
- [ ] teardown/rollback command and preserved-state decision
- [ ] next action: keep container path, compare runtimes, add lifecycle service, add UI, fix Docker/GPU layer, or return to non-container serving

## References

Internal evidence:

- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local Open WebUI Provider Integration Runner]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/LLM Deployment Decision Matrix]]

Current external docs checked 2026-06-15:

- [Docker Desktop GPU support](https://docs.docker.com/desktop/features/gpu/)
- [Docker Desktop WSL 2 backend](https://docs.docker.com/desktop/features/wsl/)
- [Docker Compose GPU support](https://docs.docker.com/compose/how-tos/gpu-support/)
- [NVIDIA Container Toolkit install guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
- [vLLM Docker deployment](https://docs.vllm.ai/en/stable/deployment/docker/)
- [vLLM OpenAI-compatible server](https://docs.vllm.ai/en/stable/serving/online_serving/)
- [SGLang installation and Docker images](https://docs.sglang.io/docs/get-started/install)
- [SGLang OpenAI-compatible APIs](https://docs.sglang.io/docs/basic_usage/openai_api)
- [Open WebUI quick start](https://docs.openwebui.com/getting-started/quick-start/)
- [Open WebUI connect a provider](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/)
