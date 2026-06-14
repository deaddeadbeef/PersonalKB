---
tags: [study, llm, local-llm, observability, operations, metrics]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM Observability and Operations Runbook

> **One-line summary** A local LLM server is operable only when every quality or performance claim is backed by request logs, timing metrics, resource pressure, error evidence, and an explicit next action.

Use this after [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] proves the endpoint and before trusting rows in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]]. Use [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook|Local LLM Service Lifecycle and Upgrade Runbook]] when the operations evidence is being captured before or after a restart, upgrade, cache move, UI update, or rollback. Use [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab|Local LLM Concurrency and Batch Throughput Lab]] when the question is saturation under load. Use [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Local LLM Quantization and GPU Offload Lab]] when the metric depends on quantization, GPU/CPU split, offload level, or KV-cache precision. Use [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Local LLM Prompt Cache and KV Reuse Lab]] when a performance claim depends on repeated-prefix reuse rather than just a warm loaded model. Use [[LLM/Study/Local LLM Speculative Decoding Lab|Local LLM Speculative Decoding Lab]] when a performance claim depends on draft-model, EAGLE, MTP, n-gram, or accepted-token evidence. Use [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]] when an observed metric points to a failed layer.

Use [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Local LLM Serving Internals and Scheduler Lab]] when the operations row needs a mechanism owner: queue, prefill, decode, KV cache, slots, continuous batching, chunked prefill, prefix cache, preemption, or admission control.

This runbook turns academic serving concepts from [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs|Serving Architectures and Throughput-Latency Trade-offs]], [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching|Batching and Continuous Batching]], and [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse|KV Cache and Context Reuse]] into local evidence you can inspect.

## What This Runbook Decides

It answers four operational questions:

1. Is the server actually running the intended model, quantization, context length, and route?
2. Is latency caused by load time, queueing, prefill, decode, streaming, client overhead, or resource pressure?
3. Is the machine limited by VRAM/RAM capacity, memory bandwidth, CPU/GPU utilization, context length, or concurrency?
4. What single controlled change should be tried next?

Do not treat "it feels slow" as evidence. Slow must become a row: request id, prompt class, model, runtime, TTFT, TPOT or tokens/sec, queue/concurrency, memory, error text, and decision.

## Metric Vocabulary

| Metric | Meaning | Usually points to |
| --- | --- | --- |
| TTFT | Time from request start to first generated token. | Load time, queue wait, prompt prefill, long context, cold model. |
| TPOT | Average time per later output token. | Decode speed, memory bandwidth, quantization, model size, active sequences. |
| ITL | Inter-token latency during streaming. | Streaming jitter, scheduler behavior, client buffering. |
| End-to-end latency | Full request duration. | Combined queue, prefill, decode, network/client overhead. |
| Prompt tokens | Tokens consumed before generation. | Context pressure and prefill cost. |
| Generation tokens | Output tokens generated. | Decode cost and output cap. |
| Requests running | Active server-side requests. | Concurrency and scheduler pressure. |
| Requests waiting/deferred | Queued work not yet decoding. | Backpressure, overload, max-concurrency limit. |
| KV-cache usage | Fraction or amount of cache consumed by active sequences. | Context length, concurrency, prompt caching, OOM risk. |
| Prefix/cache hit rate | Reuse of repeated prompt prefixes. | System-prompt or agent-loop efficiency. |
| GPU/VRAM | Utilization and memory occupancy. | GPU saturation, OOM risk, CPU fallback. |
| CPU/RAM | Host-side load and memory pressure. | CPU-only inference, tokenizer bottleneck, paging. |
| Error rate | Failed, timed-out, cancelled, or refused requests. | Endpoint contract, overload, policy, timeout, malformed payload. |

## Runtime Observability Map

| Runtime | Minimum state proof | Metrics or logs to capture | First local check |
| --- | --- | --- | --- |
| Ollama | `/api/ps`, `/api/tags`, model name, digest, size, VRAM size if present, context length if present. | `total_duration`, `load_duration`, `prompt_eval_count`, `prompt_eval_duration`, `eval_count`, `eval_duration` from responses; client wall clock; process resource usage. | `Invoke-RestMethod http://localhost:11434/api/ps` |
| LM Studio | `lms server status`, loaded model from UI or `lms ps`, base URL and port. | `lms log stream`, `--stats` when available, server logs, OpenAI-compatible response usage, client timing. | `lms server status --json --quiet` |
| llama.cpp server | startup command, model path, context, slots, `/slots`, route, `--metrics` flag if enabled. | `/metrics` Prometheus exporter, `/slots` per-slot state, prompt/generation token counters, requests processing/deferred. | `curl http://127.0.0.1:8080/slots` |
| vLLM | `vllm serve` command, model id, served route, engine version, model config. | `/metrics` Prometheus endpoint, request histograms, running/waiting requests, KV-cache usage, prefix-cache counters, logs. | `curl http://127.0.0.1:8000/metrics` |
| SGLang | launch command, model path, port, max running requests, metrics flag. | `/metrics` with `--enable-metrics`, token counters, token usage, cache hit rate, TTFT histograms, benchmark output. | `curl http://127.0.0.1:30000/metrics` |

For desktop use, Ollama and LM Studio can be sufficient with API state, response timings, logs, and OS resource counters. For production-style serving, prefer vLLM, SGLang, or llama.cpp with Prometheus-style metrics enabled so queue, cache, and request histograms are visible.

## Lab 0: Create An Evidence Folder

Create one folder per run:

```powershell
$run = Get-Date -Format "yyyyMMdd-HHmmss"
$root = "D:\LLM-Runs\$run-observability"
New-Item -ItemType Directory -Force $root | Out-Null
```

Record the invariant fields first:

| Field | Value |
| --- | --- |
| Run id |  |
| Date/time |  |
| Machine |  |
| Runtime and version |  |
| Startup command |  |
| Model id/path |  |
| Quantization |  |
| Context length |  |
| Endpoint/base URL |  |
| Prompt suite |  |
| Sampling settings |  |
| Output cap |  |
| Concurrency/request rate |  |
| Observer commands |  |

The invariant fields prevent false comparisons. If model, quantization, context, sampling, output cap, runtime, or hardware changes, it is a new run.

## Lab 1: Prove Model State

Ollama:

```powershell
Invoke-RestMethod http://localhost:11434/api/tags |
  ConvertTo-Json -Depth 8 |
  Set-Content "$root\ollama-tags.json"

Invoke-RestMethod http://localhost:11434/api/ps |
  ConvertTo-Json -Depth 8 |
  Set-Content "$root\ollama-ps.json"
```

LM Studio:

```powershell
lms server status --json --quiet | Set-Content "$root\lmstudio-server-status.json"
lms ps --json | Set-Content "$root\lmstudio-ps.json"
```

llama.cpp:

```powershell
Invoke-RestMethod http://127.0.0.1:8080/slots |
  ConvertTo-Json -Depth 8 |
  Set-Content "$root\llamacpp-slots.json"
```

vLLM or SGLang:

```powershell
Invoke-WebRequest http://127.0.0.1:8000/metrics -OutFile "$root\vllm-metrics-before.txt"
Invoke-WebRequest http://127.0.0.1:30000/metrics -OutFile "$root\sglang-metrics-before.txt"
```

Use only the relevant commands. A valid state proof names what is loaded, where it is served, and which settings affect memory and scheduling.

## Lab 2: Capture One Request With Timings

Run a single non-streaming request first. Save the exact request body, response, and wall-clock time.

```powershell
$body = @{
  model = "<model>"
  prompt = "Explain why KV cache affects local LLM memory in three sentences."
  stream = $false
  options = @{
    temperature = 0.2
    num_predict = 160
  }
} | ConvertTo-Json -Depth 6

$body | Set-Content "$root\request.json"

$sw = [Diagnostics.Stopwatch]::StartNew()
$response = Invoke-RestMethod `
  -Uri "http://localhost:11434/api/generate" `
  -Method Post `
  -Body $body `
  -ContentType "application/json"
$sw.Stop()

$response | ConvertTo-Json -Depth 8 | Set-Content "$root\response.json"
[pscustomobject]@{
  wall_ms = $sw.ElapsedMilliseconds
  total_duration_ns = $response.total_duration
  load_duration_ns = $response.load_duration
  prompt_eval_count = $response.prompt_eval_count
  prompt_eval_duration_ns = $response.prompt_eval_duration
  eval_count = $response.eval_count
  eval_duration_ns = $response.eval_duration
} | ConvertTo-Json | Set-Content "$root\timing-summary.json"
```

For OpenAI-compatible endpoints, record client wall time and response usage fields. If streaming is used, record first-chunk time separately from final completion time.

## Lab 3: Observe System Pressure

Use the lightest observer that answers the question.

Windows process and listening-port snapshot:

```powershell
Get-Process | Where-Object {
  $_.ProcessName -match 'ollama|lmstudio|llama|vllm|sglang|python'
} | Select-Object ProcessName,Id,CPU,WorkingSet64,PrivateMemorySize64 |
  Export-Csv "$root\process-snapshot.csv" -NoTypeInformation

Get-NetTCPConnection -State Listen |
  Where-Object { $_.LocalPort -in 11434,1234,8000,8080,30000 } |
  Export-Csv "$root\listeners.csv" -NoTypeInformation
```

NVIDIA GPU snapshot if available:

```powershell
nvidia-smi `
  --query-gpu=timestamp,name,driver_version,utilization.gpu,utilization.memory,memory.total,memory.used,memory.free,power.draw,temperature.gpu `
  --format=csv `
  -f "$root\nvidia-smi.csv"
```

Prometheus-style scrape if enabled:

```powershell
Invoke-WebRequest http://127.0.0.1:8000/metrics -OutFile "$root\metrics-after.txt"
```

Do not over-collect private prompts. If logs include raw user text, treat them as sensitive local artifacts and do not sync them outside the trusted vault boundary.

## Lab 4: Build The First Operations Row

| Run id | Runtime | Model | Prompt class | Prompt tokens | Output tokens | TTFT | TPOT/tokens-sec | E2E | Running/waiting | KV/cache | Peak RAM/VRAM | Error | Decision |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |  |  | Pass/Hold/Fail |

Decision rules:

- Pass: the endpoint is reachable, the intended model is loaded, timings are within the workload target, resource pressure has headroom, and logs/metrics are saved.
- Hold: one bottleneck is visible but needs a controlled follow-up, such as smaller context, lower concurrency, different quantization, warmer model, or stronger runtime.
- Fail: the endpoint is not reproducible, the wrong model or route is used, resource pressure is unsafe, errors are unexplained, or raw logs violate the privacy boundary.

## Symptom To Evidence Map

| Symptom | First evidence | Likely next controlled change |
| --- | --- | --- |
| First request is slow, later requests are faster | Load duration, model keep-alive, cold/warm timing pair. | Warm model, adjust keep-alive, separate cold-start from steady-state benchmark. |
| TTFT high with long prompts | Prompt token count, prefill duration, context length, KV-cache usage. | Shorten prompt, reduce RAG chunks, use [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Prompt Cache and KV Reuse Lab]] if repeated prefixes should hit. |
| Repeated long prefix is not faster | Cache disabled, prefix mismatch, cache eviction, or model residency confused with cache reuse. | Compare cold/warm/changed-prefix rows and inspect cache metrics or slots. |
| TPOT poor but TTFT acceptable | Output token duration, GPU/CPU utilization, memory bandwidth, model size, quantization, offload, or missing/weak speculative decoding path. | [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Quantization and GPU Offload Lab]], smaller model, different runtime, or [[LLM/Study/Local LLM Speculative Decoding Lab|Speculative Decoding Lab]]. |
| Speculative decoding is slower than baseline | Low draft acceptance, draft model too large, extra memory pressure, or batching conflict. | Compare accepted-token stats, TPOT, peak RAM/VRAM, and no-spec baseline. |
| Errors appear only under concurrency | Running/waiting requests, queue depth, p95 TTFT, HTTP status/error class. | Lower max concurrency, add client queue, use backpressure, compare serving runtime. |
| VRAM climbs until failure | KV/cache usage, context length, active sequences, output cap. | Reduce context, reduce concurrency, lower output cap, smaller model, smaller KV precision if supported. |
| Model quality varies between runs | Sampler settings, seed behavior, prompt/template, output cap. | Freeze sampler, verify chat template, rerun quality harness. |
| Client says route not found | Base URL, route, runtime endpoint map, status code body. | Switch native route vs `/v1`, confirm model id and route compatibility. |
| Logs contain private data | Log command, redaction policy, storage location. | Reduce log scope, store locally, rotate/delete sensitive raw logs. |

## Completion Gate

The runbook is complete for one local setup when all are true:

- [ ] Loaded model state is saved.
- [ ] Startup command and endpoint route are saved.
- [ ] One non-streaming timing row is saved.
- [ ] One streaming TTFT row is saved when streaming is part of the workload.
- [ ] CPU/RAM and GPU/VRAM evidence is saved, or the absence of a GPU is recorded.
- [ ] Runtime-specific logs or metrics are saved.
- [ ] Any private prompt/log exposure is accounted for.
- [ ] Benchmark log receives the final pass/hold/fail row.
- [ ] Service lifecycle runbook receives a change/rollback row when the observation was caused by restart, upgrade, cache movement, UI change, or client contract change.
- [ ] Troubleshooting tree receives a failure row or explicit no-failure row.
- [ ] Next action changes one variable only.

## References

Internal:

- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Lab]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab]]
- [[LLM/Study/Local LLM Speculative Decoding Lab]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]

Current external docs checked 2026-06-15:

- [Ollama API introduction](https://docs.ollama.com/api/introduction)
- [Ollama generate endpoint](https://docs.ollama.com/api/generate)
- [Ollama list running models](https://docs.ollama.com/api/ps)
- [LM Studio server status](https://lmstudio.ai/docs/cli/serve/server-status)
- [LM Studio loaded models](https://lmstudio.ai/docs/cli/local-models/ps)
- [LM Studio log stream](https://lmstudio.ai/docs/cli/serve/log-stream)
- [LM Studio server start](https://lmstudio.ai/docs/cli/serve/server-start)
- [llama.cpp server metrics and slots](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- [vLLM metrics](https://docs.vllm.ai/en/stable/design/metrics/)
- [SGLang production metrics](https://docs.sglang.io/docs/references/production_metrics)
- [SGLang benchmark and profiling](https://sgl-project.github.io/developer_guide/benchmark_and_profiling.html)
- [NVIDIA SMI documentation](https://docs.nvidia.com/deploy/nvidia-smi/)
