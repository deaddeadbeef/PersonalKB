---
tags: [study, llm, inference, local-llm, client, benchmark, lab]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [practice]
---

# Local LLM Client Harness Lab

> **One-line summary** A local model run is reproducible only when the client captures request settings, timing, response text, errors, and benchmark fields in the same shape every time.

Use this after [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] proves the endpoint, [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] records the base URL, route, model id, streaming behavior, errors, and feature gaps, and [[LLM/Study/LLM Inference Request Lifecycle Lab|LLM Inference Request Lifecycle Lab]] explains one request. Use [[LLM/Study/Local LLM First Client Harness Runner|Local LLM First Client Harness Runner]] for the first small reusable Python client run before expanding into streaming, retries, multiple prompt suites, or app integration. Use [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]] when the harness must freeze sampler settings rather than rely on runtime defaults. Use [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]] when the harness must log tool calls, validation, policy decisions, execution latency, and tool-result injection. This lab turns one successful call into a repeatable client-side harness.

For private or document-grounded runs, check [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] before saving prompts, retrieved passages, outputs, or logs.

## Outcome

After this lab you should be able to:

- call one local OpenAI-compatible or runtime-specific endpoint from a repeatable script
- reuse a validated local API contract instead of hardcoding guessed routes or model ids
- keep model, base URL, route, and request settings in one configuration block
- record total latency, time to first token, prompt tokens, output tokens, and decode speed when available
- capture HTTP, model, timeout, schema, and streaming errors without losing the run row
- write one log record that feeds [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] and [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]]

## Harness Contract

| Layer | Requirement | Evidence |
| --- | --- | --- |
| Config | Runtime, base URL, route, model id, prompt id, sampling settings, stream flag, and output path are set in one place. | A copied config block or script header. |
| Request builder | The request body is created from config values, not edited by hand for every run. | Serialized JSON body or equivalent code. |
| Non-streaming path | The client can send one request and parse the final response text. | Response text, usage fields if returned, total latency. |
| Streaming path | The client can measure first content delta and final output when streaming is enabled. | TTFT, total latency, chunk count, final text. |
| Timer | Wall-clock timing starts before network send and stops after final response or error. | `latency_s`, `ttft_s`, and decode speed fields. |
| Parser | The client extracts text, token counts, stop reason, and usage fields when the runtime provides them. | Parsed record plus raw response excerpt when needed. |
| Error recorder | Failures create a structured row instead of disappearing into console text. | `status`, `error_class`, `http_status`, `retryable`, and first fix. |
| Tool recorder | Tool calls, validated arguments, policy decisions, execution results, and tool-result messages are logged when tools are enabled. | `tool_name`, `tool_args_valid`, `tool_policy`, `tool_latency_s`, and `tool_result_status`. |
| Logger | Every run appends one JSONL or CSV row with stable field names. | A run log that can be compared across model/runtime candidates. |
| Evaluator handoff | The same prompt id and output path can be scored by the quality harness. | Prompt-suite row with model/runtime, rubric scores, and decision. |

The contract is intentionally small. A notebook, PowerShell script, Python script, or app wrapper can all pass if they produce the same evidence.

## Config Block Template

Record these fields before the request leaves the client:

| Field | Example |
| --- | --- |
| `run_id` | `2026-06-14-local-chat-001` or a UUID |
| `timestamp` | Local timestamp at request start |
| `runtime` | Ollama, LM Studio, llama.cpp, vLLM, SGLang, or other |
| `base_url` | `http://localhost:1234/v1` |
| `route` | `/chat/completions` |
| `model_id` | Exact served id or local model tag |
| `endpoint_scope` | Loopback, LAN, tunnel, or remote |
| `stream` | `false` for baseline, `true` for perceived-latency test |
| `system_prompt_id` | Short name or hash, not a pasted secret |
| `prompt_id` | Prompt-suite id such as `K-01`, `S-01`, or `D-01` |
| `temperature` | `0` for deterministic baseline |
| `top_p`, `top_k`, `min_p` | Empty if unsupported or intentionally default |
| `seed` | Empty if unsupported; fixed only when reproducibility depends on sampled output |
| `penalties` | Repetition, frequency, presence, or repeat-window settings if supported |
| `max_tokens` | Explicit output cap |
| `stop` | Stop strings or empty |
| `context_tokens` | Known prompt/context token count, if available |
| `output_path` | JSONL file, CSV file, or dated experiment note |

Do not hardcode real API keys into local test scripts. Many local servers accept no authentication or a placeholder bearer token; record which one you used.

## Minimal PowerShell Non-Streaming Harness

Use this for a quick Windows-native check against an OpenAI-compatible local endpoint.

```powershell
$RunId = [guid]::NewGuid().ToString()
$StartedAt = Get-Date
$Timer = [System.Diagnostics.Stopwatch]::StartNew()

$BaseUrl = "http://localhost:1234/v1"
$Route = "/chat/completions"
$Model = "<served-model-id>"
$PromptId = "K-01"

$Body = @{
  model = $Model
  messages = @(
    @{ role = "system"; content = "Answer briefly and do not invent facts." }
    @{ role = "user"; content = "Reply with exactly: local llm ok" }
  )
  temperature = 0
  max_tokens = 32
  stream = $false
} | ConvertTo-Json -Depth 8

try {
  $Response = Invoke-RestMethod `
    -Uri "$BaseUrl$Route" `
    -Method Post `
    -ContentType "application/json" `
    -Headers @{ Authorization = "Bearer local" } `
    -Body $Body `
    -TimeoutSec 120

  $Timer.Stop()
  $Text = $Response.choices[0].message.content
  $Usage = $Response.usage
  $Status = "pass"
  $ErrorClass = ""
  $HttpStatus = ""
}
catch {
  $Timer.Stop()
  $Text = ""
  $Usage = $null
  $Status = "fail"
  $ErrorClass = $_.Exception.GetType().Name
  $HttpStatus = if ($_.Exception.Response) { [int]$_.Exception.Response.StatusCode } else { "" }
}

$Record = [ordered]@{
  run_id = $RunId
  timestamp = $StartedAt.ToString("s")
  runtime = "local-openai-compatible"
  base_url = $BaseUrl
  route = $Route
  model_id = $Model
  prompt_id = $PromptId
  stream = $false
  temperature = 0
  max_tokens = 32
  latency_s = [math]::Round($Timer.Elapsed.TotalSeconds, 3)
  prompt_tokens = $Usage.prompt_tokens
  output_tokens = $Usage.completion_tokens
  status = $Status
  error_class = $ErrorClass
  http_status = $HttpStatus
  response_excerpt = if ($Text.Length -gt 160) { $Text.Substring(0, 160) } else { $Text }
}

$Record | ConvertTo-Json -Depth 8 -Compress | Add-Content -Path ".\local_llm_runs.jsonl"
```

Pass signal: the log row is useful even when the request fails.

## Minimal Python Non-Streaming Harness

Use the Python standard library when you want a portable script without client SDK assumptions.

```python
import json
import time
import uuid
import urllib.error
import urllib.request

BASE_URL = "http://localhost:1234/v1"
ROUTE = "/chat/completions"
MODEL = "<served-model-id>"
PROMPT_ID = "K-01"
OUTPUT_PATH = "local_llm_runs.jsonl"

payload = {
    "model": MODEL,
    "messages": [
        {"role": "system", "content": "Answer briefly and do not invent facts."},
        {"role": "user", "content": "Reply with exactly: local llm ok"},
    ],
    "temperature": 0,
    "max_tokens": 32,
    "stream": False,
}

run_id = str(uuid.uuid4())
started_at = time.strftime("%Y-%m-%dT%H:%M:%S%z")
started = time.perf_counter()
status = "pass"
error_class = ""
http_status = ""
text = ""
usage = {}

try:
    request = urllib.request.Request(
        BASE_URL + ROUTE,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": "Bearer local"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        raw = response.read().decode("utf-8")
    data = json.loads(raw)
    text = data["choices"][0]["message"]["content"]
    usage = data.get("usage", {})
except urllib.error.HTTPError as exc:
    status = "fail"
    error_class = "HTTPError"
    http_status = exc.code
    text = exc.read().decode("utf-8", errors="replace")[:160]
except Exception as exc:
    status = "fail"
    error_class = type(exc).__name__
    text = str(exc)[:160]
finally:
    elapsed_s = time.perf_counter() - started

record = {
    "run_id": run_id,
    "timestamp": started_at,
    "runtime": "local-openai-compatible",
    "base_url": BASE_URL,
    "route": ROUTE,
    "model_id": MODEL,
    "prompt_id": PROMPT_ID,
    "stream": False,
    "temperature": payload["temperature"],
    "max_tokens": payload["max_tokens"],
    "latency_s": round(elapsed_s, 3),
    "prompt_tokens": usage.get("prompt_tokens"),
    "output_tokens": usage.get("completion_tokens"),
    "status": status,
    "error_class": error_class,
    "http_status": http_status,
    "response_excerpt": text[:160],
}

with open(OUTPUT_PATH, "a", encoding="utf-8") as handle:
    handle.write(json.dumps(record, ensure_ascii=False) + "\n")
```

Pass signal: another machine can change only `BASE_URL`, `MODEL`, and `PROMPT_ID` and still produce the same schema.

## Streaming Timing Harness

Streaming clients are runtime-specific because server-sent-event chunk shape can vary. Keep the measurement contract stable even if the parser changes.

| Step | Record |
| --- | --- |
| Request start | Start timestamp before network send. |
| First event | First HTTP/SSE event timestamp, even if it contains metadata only. |
| First content delta | Timestamp of the first non-empty user-visible text delta. This is TTFT for the interface. |
| Final event | Timestamp when the stream ends normally or errors. |
| Chunk count | Number of received chunks or events. |
| Final text | Concatenated content deltas after applying role/tool/schema rules. |
| Interruption | Network close, JSON parse failure, server error event, or timeout. |

Streaming improves perceived latency when first content appears early. It does not automatically improve total latency, output quality, or tokens/sec.

## Error Contract

Force at least one harmless failure, such as a wrong model id or wrong route, so the harness proves it can log errors.

| Error | Likely layer | Record | First fix |
| --- | --- | --- | --- |
| Connection refused | Server process or port | `status=fail`, connection error, base URL | Start server, verify port, check loopback binding. |
| 404 route | API route | HTTP status, route, base URL | Add `/v1`, switch `/chat/completions` vs runtime-native route. |
| Model not loaded | Runtime/model registry | Error body excerpt, model id | List served models and copy exact id. |
| Timeout | Runtime, prompt length, hardware, or network | Timeout seconds, prompt class, context tokens | Shorten prompt, raise timeout, inspect server logs. |
| JSON parse error | Response shape or interrupted stream | Raw excerpt path and parser error | Save raw event sample, update parser. |
| Context length | Prompt assembly/KV cache | Prompt tokens if known, context setting | Reduce context or choose larger context setting. |
| OOM or HTTP 500 | Runtime/hardware | Error body, model id, quantization, context | Smaller model, stronger quantization, lower context, lower concurrency. |
| Invalid schema | Application boundary | Parse/validation result and output excerpt | Tighten prompt, add validation, or use constrained decoding. |
| Tool denied | Policy boundary | Tool name, denied argument, policy reason | Return a safe denial or ask for approval; do not execute. |
| Stream interrupted | Client/server stream layer | Last successful chunk and partial text length | Retry once only if the workload allows it and record the retry. |

## Run Log JSONL Schema

Use stable field names so the benchmark and quality notes can read the same row.

| Field | Meaning |
| --- | --- |
| `run_id` | Unique run key shared by benchmark and quality rows. |
| `timestamp` | Request start time. |
| `runtime` | Runtime or server wrapper. |
| `base_url` | Endpoint base URL, redacted if needed. |
| `route` | API route. |
| `model_id` | Exact served model id. |
| `prompt_id` | Prompt-suite key. |
| `prompt_class` | Known fact, schema, RAG, long context, coding, summarization, etc. |
| `stream` | Whether the request used streaming. |
| `sampling` | Temperature, top-p, top-k, max tokens, stop strings, seed if supported. |
| `context` | Context token count, retrieved corpus version, or prompt source note. |
| `latency_s` | Total wall-clock latency. |
| `ttft_s` | First user-visible content delta for streaming runs. |
| `prompt_tokens` | Prompt token count if provided or measured. |
| `output_tokens` | Output token count if provided or measured. |
| `decode_tokens_per_s` | Output tokens divided by decode time when available. |
| `status` | `pass`, `hold`, `fail`, or `error`. |
| `error_class` | Structured error name for failed runs. |
| `response_excerpt` | Short redacted excerpt or link to private output. |
| `quality_decision` | Pass/hold/fail after rubric scoring, if available. |
| `tool_trace` | Tool call metadata, validation result, policy decision, execution status, and result token count when tools are enabled. |
| `notes` | One-line interpretation or next fix. |

For private work, store redacted excerpts or local-only output paths instead of full prompt/output text. The point is reproducibility, not leaking the corpus into logs.

## Benchmark Mapping

| Client harness field | Benchmark log field |
| --- | --- |
| `run_id` | Source commit/config or run identifier |
| `model_id` | Model id |
| `runtime` | Runtime/API |
| `sampling` | Sampling settings |
| `context` | Context/prompt tokens |
| `latency_s` | Total latency |
| `ttft_s` | Time to first token |
| `decode_tokens_per_s` | Decode tokens/sec |
| `prompt_tokens` | Prompt tokens |
| `output_tokens` | Output tokens |
| `status`, `error_class` | Error/retry count and notes |
| `quality_decision` | Quality score and decision |

The benchmark row is the decision surface. The JSONL row is the raw run evidence.

## Quality Harness Handoff

Every prompt-suite case in [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] should be callable through the same client.

| Quality harness field | Client harness source |
| --- | --- |
| Prompt id | `prompt_id` |
| Model/runtime | `model_id` and `runtime` |
| Output path/link | JSONL row, local text file, or experiment note |
| Expected behavior | Prompt-suite definition, not generated by the model under test |
| Latency score | `latency_s`, `ttft_s`, and decode speed |
| Failure mode | `error_class`, parse result, rubric notes |
| Decision | Human or evaluator rubric result |

Do not change prompt wording, sampling settings, or retrieved context while scoring two model/runtime candidates unless that change is the experiment.

## Completion Gate

This lab is complete when you have:

- [ ] one config block for a chosen local endpoint
- [ ] one non-streaming call logged to JSONL or CSV
- [ ] one streaming call measured, or an explicit note that the runtime/client path does not support streaming
- [ ] one intentional harmless error case logged without crashing the harness
- [ ] one benchmark row created from the harness fields
- [ ] one quality-harness prompt-suite row that reuses the same client
- [ ] one security/logging decision checked before saving private prompts, retrieved documents, or outputs

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
