---
tags: [study, llm, inference, local-llm, streaming, latency, client, harness, evidence]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-16
---

# Local LLM First Streaming Timing Runner

> **One-line summary** After the first non-streaming client call works, run this streaming harness to measure first event, first visible content delta, chunk count, final text, total latency, usage fields, and stream errors.

Use this after [[LLM/Study/Local LLM First Client Harness Runner|Local LLM First Client Harness Runner]] proves one reusable non-streaming call and [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] or [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner|Local LLM OpenAI-Compatible API Contract Runner]] says the local `/v1/chat/completions` route can stream. Use [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] after this when streaming needs retries, prompt suites, tool traces, UI integration, or benchmark automation.

The purpose is narrow: prove what the user actually feels during streaming without confusing perceived latency with total latency or model quality.

Current dated proof: [[LLM/Study/Local LLM OpenAI-Compatible Streaming Timing Proof - 2026-06-16|Local LLM OpenAI-Compatible Streaming Timing Proof - 2026-06-16]] records first SSE event, first visible content, total latency, reasoning chunks, final output, usage, and done-marker evidence for the `SMOKE-01` OpenAI-compatible route.

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| First SSE event time | The server started sending a stream. | The user saw useful text. |
| First content delta / TTFT | The first visible assistant text arrived. | Full answer speed or quality. |
| Chunk count and content chunk count | The client parsed streamed events. | Runtime throughput under load. |
| Final output text | The streamed deltas reconstruct an answer. | The answer is correct. |
| Total latency | The complete streamed response finished. | Which phase caused the delay. |
| Usage fields if emitted | The runtime exposed token counts for this path. | Universal OpenAI compatibility. |
| Structured error row | Stream failures can be diagnosed later. | The server is healthy. |

Streaming improves perceived latency when the first useful text arrives early. It does not make the model smarter, and it may not increase total tokens per second.

## Fixed Conditions

Write these before running:

| Field | Value |
|---|---|
| Run folder |  |
| API contract card |  |
| Non-streaming client row |  |
| Runtime | Ollama / LM Studio / llama.cpp / vLLM / SGLang / other |
| Base URL | `http://127.0.0.1:11434/v1` for Ollama OpenAI-compatible route |
| Route | `/chat/completions` |
| Model id |  |
| Prompt id | `K-01` / `S-01` / workload prompt id |
| Temperature | `0` |
| Max tokens | `128` for first streaming proof, or `512` when a thinking-capable model needs enough room to reach final visible content |
| Include usage request | `LOCAL_LLM_INCLUDE_USAGE=1` only if the contract says the runtime supports it |
| Log policy | redacted excerpt / full local-only output / no private content |

Do not compare streaming rows until prompt text, model id, sampler settings, output cap, route, client, and cold/warm state are named.

## Standard-Library OpenAI-Compatible SSE Runner

This version uses only Python's standard library. Save it as `first-streaming-timing.py` inside the run folder.

```python
import json
import os
import time
import uuid
import urllib.error
import urllib.request
from pathlib import Path


def usage_value(usage, *keys):
    if not isinstance(usage, dict):
        return None
    for key in keys:
        if key in usage:
            return usage[key]
    return None


RUN_ROOT = Path(os.environ.get("LOCAL_LLM_RUN_ROOT", ".")).resolve()
BASE_URL = os.environ.get("LOCAL_LLM_BASE_URL", "http://127.0.0.1:11434/v1").rstrip("/")
ROUTE = os.environ.get("LOCAL_LLM_ROUTE", "/chat/completions")
MODEL = os.environ.get("LOCAL_LLM_MODEL", "<served-model-id>")
PROMPT_ID = os.environ.get("LOCAL_LLM_PROMPT_ID", "K-01")
AUTH_TOKEN = os.environ.get("LOCAL_LLM_API_KEY", "ollama")
INCLUDE_USAGE = os.environ.get("LOCAL_LLM_INCLUDE_USAGE", "0") == "1"

HARNESS_DIR = RUN_ROOT / "first-streaming-timing"
REQUEST_DIR = HARNESS_DIR / "requests"
EVENT_DIR = HARNESS_DIR / "events"
OUTPUT_DIR = HARNESS_DIR / "outputs"
for directory in (REQUEST_DIR, EVENT_DIR, OUTPUT_DIR):
    directory.mkdir(parents=True, exist_ok=True)

PROMPTS = {
    "SMOKE-01": {
        "system": "Answer the user exactly.",
        "user": "Reply with exactly: local llm ok",
        "prompt_class": "route smoke",
    },
    "K-01": {
        "system": "Answer the user exactly. Keep reasoning to one short sentence.",
        "user": "Compute 17 * 23 + 19. Return exactly: answer=<number>; reason=<one short sentence>.",
        "prompt_class": "known-answer arithmetic",
    },
    "S-01": {
        "system": "Return only valid JSON. Do not wrap it in markdown.",
        "user": "A local model produced 128 output tokens in 4 seconds. Return JSON with keys tokens, seconds, tokens_per_second, and caveat.",
        "prompt_class": "structured output",
    },
    "G-01": {
        "system": "Use only the supplied text. If the answer is absent, follow the requested refusal string exactly.",
        "user": "Using only this text: The model tag is qwen3.5:4b. What GPU is being used? If the answer is not present, say exactly: not enough evidence.",
        "prompt_class": "grounded refusal",
    },
}

case = PROMPTS[PROMPT_ID]
run_id = f"{time.strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:8]}"
request_path = REQUEST_DIR / f"{run_id}-{PROMPT_ID}.json"
events_path = EVENT_DIR / f"{run_id}-{PROMPT_ID}.jsonl"
output_path = OUTPUT_DIR / f"{run_id}-{PROMPT_ID}.txt"
log_path = HARNESS_DIR / "streaming-runs.jsonl"

payload = {
    "model": MODEL,
    "messages": [
        {"role": "system", "content": case["system"]},
        {"role": "user", "content": case["user"]},
    ],
    "temperature": 0,
    "max_tokens": int(os.environ.get("LOCAL_LLM_MAX_TOKENS", "128")),
    "stream": True,
}
if INCLUDE_USAGE:
    payload["stream_options"] = {"include_usage": True}

request_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

started_at = time.strftime("%Y-%m-%dT%H:%M:%S%z")
started = time.perf_counter()
status = "pass"
error_class = ""
http_status = ""
finish_reason = None
usage = {}
first_event_s = None
ttft_s = None
event_count = 0
content_chunk_count = 0
thinking_chunk_count = 0
tool_call_chunk_count = 0
done_seen = False
parts = []

try:
    request = urllib.request.Request(
        BASE_URL + ROUTE,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {AUTH_TOKEN}",
            "Accept": "text/event-stream",
        },
        method="POST",
    )
    with events_path.open("w", encoding="utf-8") as events_file:
        with urllib.request.urlopen(request, timeout=120) as response:
            http_status = getattr(response, "status", "")
            for raw_line in response:
                line = raw_line.decode("utf-8", errors="replace").strip()
                if not line or line.startswith(":"):
                    continue
                if not line.startswith("data:"):
                    continue

                data_text = line[len("data:") :].strip()
                if first_event_s is None:
                    first_event_s = time.perf_counter() - started
                if data_text == "[DONE]":
                    done_seen = True
                    break

                event_count += 1
                events_file.write(data_text + "\n")
                event = json.loads(data_text)
                usage = event.get("usage") or usage

                choices = event.get("choices") or []
                if not choices:
                    continue
                choice = choices[0]
                finish_reason = choice.get("finish_reason") or finish_reason
                delta = choice.get("delta") or {}

                content = delta.get("content") or ""
                if content:
                    if ttft_s is None:
                        ttft_s = time.perf_counter() - started
                    content_chunk_count += 1
                    parts.append(content)

                if delta.get("thinking") or delta.get("reasoning"):
                    thinking_chunk_count += 1
                if delta.get("tool_calls"):
                    tool_call_chunk_count += 1
except urllib.error.HTTPError as exc:
    status = "error"
    error_class = "HTTPError"
    http_status = exc.code
    error_body = exc.read().decode("utf-8", errors="replace")
    events_path.write_text(error_body, encoding="utf-8")
except Exception as exc:
    status = "error"
    error_class = type(exc).__name__
    events_path.write_text(json.dumps({"error": str(exc)}, indent=2), encoding="utf-8")
finally:
    total_latency_s = time.perf_counter() - started

text = "".join(parts)
if status == "pass" and not parts:
    status = "hold"
    error_class = "NoContentDelta"
elif status == "pass" and not done_seen:
    status = "hold"
    error_class = "NoDoneMarker"

output_path.write_text(text, encoding="utf-8")
response_excerpt = " ".join(text.split())[:200]

record = {
    "run_id": run_id,
    "timestamp": started_at,
    "runtime": "local-openai-compatible",
    "base_url": BASE_URL,
    "route": ROUTE,
    "model_id": MODEL,
    "prompt_id": PROMPT_ID,
    "prompt_class": case["prompt_class"],
    "stream": True,
    "temperature": payload["temperature"],
    "max_tokens": payload["max_tokens"],
    "include_usage_requested": INCLUDE_USAGE,
    "request_path": str(request_path),
    "events_path": str(events_path),
    "output_path": str(output_path),
    "first_event_s": round(first_event_s, 3) if first_event_s is not None else None,
    "ttft_s": round(ttft_s, 3) if ttft_s is not None else None,
    "total_latency_s": round(total_latency_s, 3),
    "event_count": event_count,
    "content_chunk_count": content_chunk_count,
    "thinking_chunk_count": thinking_chunk_count,
    "tool_call_chunk_count": tool_call_chunk_count,
    "done_seen": done_seen,
    "finish_reason": finish_reason,
    "prompt_tokens": usage_value(usage, "prompt_tokens", "input_tokens"),
    "output_tokens": usage_value(usage, "completion_tokens", "output_tokens"),
    "total_tokens": usage_value(usage, "total_tokens"),
    "status": status,
    "error_class": error_class,
    "http_status": http_status,
    "response_excerpt": response_excerpt,
}

with log_path.open("a", encoding="utf-8") as handle:
    handle.write(json.dumps(record, ensure_ascii=True) + "\n")

print(json.dumps(record, indent=2, ensure_ascii=True))
```

PowerShell run:

```powershell
$env:LOCAL_LLM_RUN_ROOT = "<paste-run-folder-path>"
$env:LOCAL_LLM_BASE_URL = "http://127.0.0.1:11434/v1"
$env:LOCAL_LLM_ROUTE = "/chat/completions"
$env:LOCAL_LLM_MODEL = "<served-model-id>"
$env:LOCAL_LLM_PROMPT_ID = "K-01"
$env:LOCAL_LLM_API_KEY = "ollama"
$env:LOCAL_LLM_INCLUDE_USAGE = "0"
python .\first-streaming-timing.py
```

Pass signal: `first-streaming-timing\streaming-runs.jsonl`, request JSON, event JSONL, and output text exist. A failure still passes the harness-logging check if the JSONL row names the error class and event path.

## Native Ollama Streaming Contrast

The runner above is for OpenAI-compatible SSE. Native Ollama streaming uses newline-delimited JSON objects from `/api/chat` or `/api/generate`, not `data:` SSE messages. Do not feed native Ollama streaming into the SSE parser.

| Route | Stream shape | Final timing and usage |
|---|---|---|
| `/v1/chat/completions` | SSE `data:` messages, usually ending with `[DONE]` | Usage may be absent unless the runtime supports and honors usage streaming. |
| `/api/chat` | JSON object per line | Final object has `done: true` and runtime statistics when emitted. |
| `/api/generate` | JSON object per line | Final object has `done: true` and runtime statistics when emitted. |

If native timing fields are the goal, save the native stream separately and compare it with [[LLM/Study/Local LLM First Response Debrief Card|Local LLM First Response Debrief Card]] and [[LLM/Study/Local LLM Inference Metrics Field Guide|Local LLM Inference Metrics Field Guide]].

## Evidence Row

Copy this into a dated run note or [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]]:

| Field | Value |
|---|---|
| Run id |  |
| Script path |  |
| Base URL |  |
| Route |  |
| Model id |  |
| Prompt id |  |
| Request path |  |
| Event JSONL path |  |
| Output path |  |
| JSONL row |  |
| First event seconds |  |
| TTFT / first content delta seconds |  |
| Total latency seconds |  |
| Event count |  |
| Content chunk count |  |
| Done marker seen |  |
| Prompt tokens |  |
| Output tokens |  |
| Finish reason |  |
| Status/error |  |
| Next route | benchmark row builder / quality harness / API contract / troubleshooting |

## Failure Routing

| Symptom | Likely owner | Route |
|---|---|---|
| Connection refused | server process, port, or loopback binding | [[LLM/Study/Local LLM Serving Runbook]] |
| Non-streaming works but streaming 404s | route compatibility or runtime feature gap | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]] |
| Stream starts but no content delta arrives | model behavior, thinking/tool chunks, stop rule, or parser mismatch | [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]] |
| First event is fast but TTFT is slow | metadata arrives before visible text; prefill, queue, or thinking budget may dominate | [[LLM/Study/Local LLM Inference Metrics Field Guide]] |
| TTFT is good but total latency is high | decode speed, output cap, or long answer length | [[LLM/Study/Local LLM Inference Metrics Field Guide]] |
| Usage is absent | runtime did not emit usage for streaming path | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]] |
| Event JSONL leaks private content | logging policy | [[LLM/Study/Local LLM Security and Privacy Runbook]] |

## Completion Gate

This first streaming runner is complete only when:

- [ ] the non-streaming first client runner has a pass or diagnosable failure row
- [ ] API contract card says streaming is supported, unsupported, or partial for this runtime
- [ ] one streaming script path is recorded
- [ ] request, event JSONL, output, and run-log paths exist
- [ ] `first_event_s`, `ttft_s`, `total_latency_s`, event count, content chunk count, and status are recorded
- [ ] missing usage fields are recorded as missing instead of guessed
- [ ] one [[LLM/Study/Local LLM First Benchmark Row Builder|benchmark row builder]] or client-harness row consumes the timing fields, or a blocker route is named
- [ ] private prompts and outputs are logged according to the security decision

## References

Internal routes:

- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]]
- [[LLM/Study/Local LLM First Benchmark Row Builder]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Local LLM First Response Debrief Card]]
- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM Command Cookbook]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]

External/current sources checked 2026-06-15:

- [Ollama streaming](https://docs.ollama.com/capabilities/streaming)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
- [Ollama usage metrics](https://docs.ollama.com/api/usage)
- [Ollama chat endpoint](https://docs.ollama.com/api/chat)
- [OpenAI streaming responses guide](https://developers.openai.com/api/docs/guides/streaming-responses)
- [OpenAI Python library reference](https://developers.openai.com/api/reference/python/)
- [MDN server-sent events guide](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events)
