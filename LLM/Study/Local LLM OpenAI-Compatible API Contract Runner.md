---
tags: [study, llm, inference, local-llm, api, openai-compatible, contract, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM OpenAI-Compatible API Contract Runner

> **One-line summary** Probe `/v1/models`, non-streaming chat, streaming chat, and one harmless wrong-model failure with a standard-library Python runner before trusting a local endpoint as OpenAI-compatible.

Use this after [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] explains the manual checks and after [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] proves that a local endpoint answers at all. Use the result before [[LLM/Study/Local LLM First Client Harness Runner|Local LLM First Client Harness Runner]], [[LLM/Study/Local LLM First Streaming Timing Runner|Local LLM First Streaming Timing Runner]], and [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] so client code starts from measured route behavior rather than guessed compatibility.

This runner sends real local HTTP requests when pointed at an actual endpoint. Do not run it until the model id, base URL, auth boundary, and evidence folder are fixed. For verification or dry runs, point `LOCAL_LLM_BASE_URL` at a fake loopback fixture server.

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| Saved `/v1/models` result | The client can discover or verify the served model id through the OpenAI-style model-list route. | That every runtime must expose `/v1/models`; native model-list proof may still be acceptable. |
| Saved non-streaming chat request and response | The selected model id can answer through `/v1/chat/completions` and the assistant content path is extractable. | Quality, tool calling, embeddings, or long-context behavior. |
| Saved streaming events | The route emits parseable stream chunks and a final text can be reconstructed. | UI latency under load or production streaming cancellation behavior. |
| Harmless wrong-model failure | The client can capture a diagnosable error before real work. | Full error taxonomy. |
| Contract summary JSON/Markdown/JSONL | The result can feed the first client harness, streaming runner, benchmark row builder, and capstone workbook. | Operational monitoring. |

Academic bridge: "OpenAI-compatible" is an interface claim, not a model-quality claim. This runner isolates the serving contract: discovery, request schema, response schema, streaming event shape, and error envelope. That separation keeps API compatibility from being confused with loss, benchmark quality, sampler tuning, RAG grounding, or deployment safety.

## Fixed Conditions

Write these before running:

| Field | Value |
|---|---|
| Run folder |  |
| Manual contract lab |  |
| Runtime | Ollama / LM Studio / llama.cpp / vLLM / SGLang / other |
| Base URL | `http://127.0.0.1:11434/v1` for Ollama compatibility mode |
| Model id |  |
| API key behavior | placeholder local token / real token / none / proxy |
| Expected text | `api contract ok` |
| Streaming required? | yes / no |
| Boundary | loopback / LAN / tunnel / remote |
| Next gate | first client harness / streaming timing / troubleshooting / security review |

If the endpoint is exposed beyond loopback, complete [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] first. Do not put private documents, secrets, tokens, or RAG corpus text into this probe.

## Standard-Library Runner

Save this as `openai-compatible-contract-runner.py` inside the run folder. It uses only Python's standard library.

```python
import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path


def env_bool(name, default):
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() not in {"0", "false", "no", "off"}


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def append_jsonl(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(data, ensure_ascii=True) + "\n")


def write_text(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(str(value or "") + "\n", encoding="utf-8")


def md_cell(value):
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True)
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def normalize_text(value):
    return " ".join(str(value or "").strip().lower().split())


def join_url(base_url, route):
    return f"{base_url.rstrip('/')}/{route.lstrip('/')}"


def content_to_text(content):
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict):
                parts.append(str(item.get("text") or item.get("content") or ""))
            else:
                parts.append(str(item))
        return "".join(parts)
    return str(content or "")


def extract_chat_text(data):
    if not isinstance(data, dict):
        return ""
    choices = data.get("choices") if isinstance(data.get("choices"), list) else []
    first = choices[0] if choices and isinstance(choices[0], dict) else {}
    message = first.get("message") if isinstance(first.get("message"), dict) else {}
    return content_to_text(message.get("content"))


def extract_finish_reason(data):
    if not isinstance(data, dict):
        return ""
    choices = data.get("choices") if isinstance(data.get("choices"), list) else []
    first = choices[0] if choices and isinstance(choices[0], dict) else {}
    return str(first.get("finish_reason") or "")


def model_ids(data):
    if not isinstance(data, dict):
        return []
    rows = data.get("data") if isinstance(data.get("data"), list) else []
    ids = []
    for row in rows:
        if isinstance(row, dict) and row.get("id"):
            ids.append(str(row["id"]))
        elif isinstance(row, str):
            ids.append(row)
    return ids


def result_error_text(result):
    data = result.get("json") if isinstance(result, dict) else None
    if isinstance(data, dict):
        error = data.get("error")
        if isinstance(error, dict):
            return str(error.get("message") or error.get("type") or error)
        if error:
            return str(error)
    return str(result.get("error") or result.get("error_class") or result.get("raw_excerpt") or "")


def request_json(method, url, body=None, timeout_s=30, headers=None):
    payload = None if body is None else json.dumps(body).encode("utf-8")
    request_headers = {"Accept": "application/json"}
    if body is not None:
        request_headers["Content-Type"] = "application/json"
    if headers:
        request_headers.update(headers)

    request = urllib.request.Request(url, data=payload, headers=request_headers, method=method)
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(request, timeout=timeout_s) as response:
            raw = response.read().decode("utf-8", errors="replace")
            elapsed_s = time.perf_counter() - started
            try:
                parsed = json.loads(raw) if raw else {}
            except json.JSONDecodeError:
                parsed = {"raw": raw}
            return {
                "url": url,
                "status": "pass",
                "http_status": getattr(response, "status", None),
                "elapsed_s": round(elapsed_s, 3),
                "json": parsed,
                "raw_excerpt": " ".join(raw.split())[:700],
            }
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        elapsed_s = time.perf_counter() - started
        try:
            parsed = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            parsed = {"raw": raw}
        return {
            "url": url,
            "status": "error",
            "http_status": exc.code,
            "elapsed_s": round(elapsed_s, 3),
            "error_class": "HTTPError",
            "json": parsed,
            "raw_excerpt": " ".join(raw.split())[:700],
        }
    except Exception as exc:
        elapsed_s = time.perf_counter() - started
        return {
            "url": url,
            "status": "error",
            "elapsed_s": round(elapsed_s, 3),
            "error_class": type(exc).__name__,
            "error": str(exc),
        }


def post_stream(url, body, timeout_s, headers, event_path):
    payload = json.dumps(body).encode("utf-8")
    request_headers = {
        "Accept": "text/event-stream",
        "Content-Type": "application/json",
    }
    request_headers.update(headers)
    request = urllib.request.Request(url, data=payload, headers=request_headers, method="POST")

    started = time.perf_counter()
    events = []
    text_parts = []
    first_event_s = None
    first_content_delta_s = None
    final_seen = False
    usage = None

    try:
        with urllib.request.urlopen(request, timeout=timeout_s) as response:
            for raw_line in response:
                elapsed_s = round(time.perf_counter() - started, 3)
                line = raw_line.decode("utf-8", errors="replace").strip()
                if not line:
                    continue
                if first_event_s is None:
                    first_event_s = elapsed_s

                data_text = line[5:].strip() if line.startswith("data:") else line
                event = {"elapsed_s": elapsed_s, "raw": line}

                if data_text == "[DONE]":
                    event["done_marker"] = True
                    final_seen = True
                    events.append(event)
                    continue

                try:
                    parsed = json.loads(data_text)
                except json.JSONDecodeError:
                    event["parse_error"] = "JSONDecodeError"
                    events.append(event)
                    continue

                event["json"] = parsed
                if isinstance(parsed, dict) and isinstance(parsed.get("usage"), dict):
                    usage = parsed["usage"]

                choices = parsed.get("choices") if isinstance(parsed, dict) and isinstance(parsed.get("choices"), list) else []
                first = choices[0] if choices and isinstance(choices[0], dict) else {}
                delta = first.get("delta") if isinstance(first.get("delta"), dict) else {}
                message = first.get("message") if isinstance(first.get("message"), dict) else {}
                content = content_to_text(delta.get("content") if delta else message.get("content"))
                finish_reason = first.get("finish_reason")

                if content:
                    text_parts.append(content)
                    event["content"] = content
                    if first_content_delta_s is None:
                        first_content_delta_s = elapsed_s
                if finish_reason:
                    event["finish_reason"] = finish_reason
                    final_seen = True
                events.append(event)

        elapsed_s = round(time.perf_counter() - started, 3)
        write_json(event_path, events)
        final_text = "".join(text_parts)
        return {
            "url": url,
            "status": "pass",
            "http_status": None,
            "elapsed_s": elapsed_s,
            "first_event_s": first_event_s,
            "first_content_delta_s": first_content_delta_s,
            "chunk_count": len(events),
            "content_chunk_count": len([event for event in events if event.get("content")]),
            "final_seen": final_seen,
            "final_text": final_text,
            "usage": usage or {},
            "events_path": str(event_path),
        }
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        elapsed_s = time.perf_counter() - started
        try:
            parsed = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            parsed = {"raw": raw}
        result = {
            "url": url,
            "status": "error",
            "http_status": exc.code,
            "elapsed_s": round(elapsed_s, 3),
            "error_class": "HTTPError",
            "json": parsed,
            "raw_excerpt": " ".join(raw.split())[:700],
            "events_path": str(event_path),
        }
        write_json(event_path, [{"error": result}])
        return result
    except Exception as exc:
        elapsed_s = time.perf_counter() - started
        result = {
            "url": url,
            "status": "error",
            "elapsed_s": round(elapsed_s, 3),
            "error_class": type(exc).__name__,
            "error": str(exc),
            "events_path": str(event_path),
        }
        write_json(event_path, [{"error": result}])
        return result


def write_markdown(path, record):
    lines = [
        f"# OpenAI-Compatible Contract - {record['run_id']}",
        "",
        f"Status: `{record['status']}`",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Runtime | {md_cell(record['runtime'])} |",
        f"| Base URL | {md_cell(record['base_url'])} |",
        f"| Model | {md_cell(record['model'])} |",
        f"| Boundary | {md_cell(record['boundary'])} |",
        f"| Expected text | {md_cell(record['expected_text'])} |",
        f"| Model list | {md_cell(record['probes']['models']['decision'])} |",
        f"| Non-streaming chat | {md_cell(record['probes']['non_streaming_chat']['decision'])} |",
        f"| Streaming chat | {md_cell(record['probes']['streaming_chat']['decision'])} |",
        f"| Wrong-model failure | {md_cell(record['probes']['wrong_model_failure']['decision'])} |",
        f"| Compatible decision | {md_cell(record['compatible_decision'])} |",
        f"| Missing layers | {md_cell(', '.join(record['missing_layers']))} |",
        f"| Next action | {md_cell(record['next_action'])} |",
        "",
        "## Probe Files",
        "",
        "| Probe | Request | Response/Event | Output |",
        "|---|---|---|---|",
    ]
    for probe in record["probe_rows"]:
        lines.append(
            f"| {md_cell(probe['probe'])} | {md_cell(probe.get('request_path'))} | "
            f"{md_cell(probe.get('response_path') or probe.get('events_path'))} | {md_cell(probe.get('output_path'))} |"
        )
    lines.extend([
        "",
        "## Non-Streaming Output",
        "",
        "```text",
        record["probes"]["non_streaming_chat"].get("assistant_text", ""),
        "```",
        "",
        "## Streaming Output",
        "",
        "```text",
        record["probes"]["streaming_chat"].get("final_text", ""),
        "```",
    ])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


RUN_ROOT = Path(os.environ.get("LOCAL_LLM_RUN_ROOT", ".")).expanduser().resolve()
RUNTIME = os.environ.get("LOCAL_LLM_RUNTIME", "openai-compatible-local")
BASE_URL = os.environ.get("LOCAL_LLM_BASE_URL", "http://127.0.0.1:11434/v1").rstrip("/")
MODEL = os.environ.get("LOCAL_LLM_MODEL", "<served-model-id>")
API_KEY = os.environ.get("LOCAL_LLM_API_KEY", "local")
BOUNDARY = os.environ.get("LOCAL_LLM_BOUNDARY", "loopback or recorded boundary")
TIMEOUT_S = float(os.environ.get("LOCAL_LLM_TIMEOUT_S", "60"))
RUN_STREAM = env_bool("LOCAL_LLM_RUN_STREAM", True)
RUN_BAD_MODEL = env_bool("LOCAL_LLM_RUN_BAD_MODEL", True)
EXPECTED_TEXT = os.environ.get("LOCAL_LLM_EXPECT_TEXT", "api contract ok")
MAX_TOKENS = int(os.environ.get("LOCAL_LLM_MAX_TOKENS", "32"))
TEMPERATURE = float(os.environ.get("LOCAL_LLM_TEMPERATURE", "0"))

OUT_DIR = RUN_ROOT / "openai-compatible-contract-runner"
REQUEST_DIR = OUT_DIR / "requests"
RESPONSE_DIR = OUT_DIR / "responses"
OUTPUT_DIR = OUT_DIR / "outputs"
EVENT_DIR = OUT_DIR / "events"
for directory in (REQUEST_DIR, RESPONSE_DIR, OUTPUT_DIR, EVENT_DIR):
    directory.mkdir(parents=True, exist_ok=True)

run_id = f"{time.strftime('%Y%m%d-%H%M%S')}-openai-contract"
timestamp = time.strftime("%Y-%m-%dT%H:%M:%S%z")
headers = {"Authorization": f"Bearer {API_KEY}"}

models_url = join_url(BASE_URL, "/models")
chat_url = join_url(BASE_URL, "/chat/completions")

model_request = {"method": "GET", "url": models_url, "headers": {"Authorization": "Bearer <redacted>"}}
model_request_path = REQUEST_DIR / f"{run_id}-models-request.json"
model_response_path = RESPONSE_DIR / f"{run_id}-models-response.json"
write_json(model_request_path, model_request)
model_result = request_json("GET", models_url, timeout_s=TIMEOUT_S, headers=headers)
write_json(model_response_path, model_result)
ids = model_ids(model_result.get("json"))
if model_result["status"] == "pass" and MODEL in ids:
    model_decision = "pass"
elif model_result["status"] == "pass":
    model_decision = "hold"
else:
    model_decision = "hold"

messages = [
    {"role": "system", "content": "Answer exactly as requested."},
    {"role": "user", "content": f"Reply with exactly: {EXPECTED_TEXT}"},
]
chat_body = {
    "model": MODEL,
    "messages": messages,
    "temperature": TEMPERATURE,
    "max_tokens": MAX_TOKENS,
    "stream": False,
}
chat_request_path = REQUEST_DIR / f"{run_id}-chat-request.json"
chat_response_path = RESPONSE_DIR / f"{run_id}-chat-response.json"
chat_output_path = OUTPUT_DIR / f"{run_id}-chat-output.txt"
write_json(chat_request_path, chat_body)
chat_result = request_json("POST", chat_url, body=chat_body, timeout_s=TIMEOUT_S, headers=headers)
write_json(chat_response_path, chat_result)
chat_text = extract_chat_text(chat_result.get("json"))
write_text(chat_output_path, chat_text)
if chat_result["status"] != "pass":
    chat_decision = "error"
elif normalize_text(chat_text) == normalize_text(EXPECTED_TEXT):
    chat_decision = "pass"
else:
    chat_decision = "hold"

stream_request_path = REQUEST_DIR / f"{run_id}-stream-request.json"
stream_event_path = EVENT_DIR / f"{run_id}-stream-events.json"
stream_output_path = OUTPUT_DIR / f"{run_id}-stream-output.txt"
if RUN_STREAM:
    stream_body = dict(chat_body)
    stream_body["stream"] = True
    write_json(stream_request_path, stream_body)
    stream_result = post_stream(chat_url, stream_body, TIMEOUT_S, headers, stream_event_path)
    stream_text = stream_result.get("final_text", "")
    write_text(stream_output_path, stream_text)
    if stream_result["status"] != "pass":
        stream_decision = "error"
    elif stream_result.get("content_chunk_count", 0) > 0 and normalize_text(EXPECTED_TEXT) in normalize_text(stream_text):
        stream_decision = "pass"
    else:
        stream_decision = "hold"
else:
    stream_result = {
        "status": "skipped",
        "reason": "LOCAL_LLM_RUN_STREAM disabled",
        "events_path": str(stream_event_path),
        "final_text": "",
    }
    stream_decision = "skipped"
    write_json(stream_request_path, {"skipped": True, "reason": stream_result["reason"]})
    write_json(stream_event_path, [stream_result])
    write_text(stream_output_path, "")

bad_request_path = REQUEST_DIR / f"{run_id}-wrong-model-request.json"
bad_response_path = RESPONSE_DIR / f"{run_id}-wrong-model-response.json"
if RUN_BAD_MODEL:
    bad_body = dict(chat_body)
    bad_body["model"] = f"{MODEL}-missing"
    write_json(bad_request_path, bad_body)
    bad_result = request_json("POST", chat_url, body=bad_body, timeout_s=TIMEOUT_S, headers=headers)
    write_json(bad_response_path, bad_result)
    bad_json = bad_result.get("json") if isinstance(bad_result.get("json"), dict) else {}
    if bad_result["status"] == "error" or (isinstance(bad_json, dict) and bad_json.get("error")):
        bad_decision = "pass"
    else:
        bad_decision = "hold"
else:
    bad_result = {"status": "skipped", "reason": "LOCAL_LLM_RUN_BAD_MODEL disabled"}
    bad_decision = "skipped"
    write_json(bad_request_path, {"skipped": True, "reason": bad_result["reason"]})
    write_json(bad_response_path, bad_result)

missing_layers = []
if model_decision != "pass":
    missing_layers.append("model-list proof")
if chat_decision != "pass":
    missing_layers.append("non-streaming chat contract")
if RUN_STREAM and stream_decision != "pass":
    missing_layers.append("streaming event contract")
if RUN_BAD_MODEL and bad_decision != "pass":
    missing_layers.append("error contract")

if chat_decision != "pass":
    status = "error"
    compatible_decision = "not-compatible"
    next_action = "route to Local LLM Troubleshooting Decision Tree before client integration"
elif missing_layers:
    status = "hold"
    compatible_decision = "partial"
    next_action = "fill missing contract layers before the first client harness"
else:
    status = "pass"
    compatible_decision = "compatible"
    next_action = "run Local LLM First Client Harness Runner"

probe_rows = [
    {
        "probe": "models",
        "decision": model_decision,
        "request_path": str(model_request_path),
        "response_path": str(model_response_path),
        "model_ids": ids,
        "error": result_error_text(model_result) if model_decision != "pass" else "",
    },
    {
        "probe": "non_streaming_chat",
        "decision": chat_decision,
        "request_path": str(chat_request_path),
        "response_path": str(chat_response_path),
        "output_path": str(chat_output_path),
        "assistant_text": chat_text,
        "finish_reason": extract_finish_reason(chat_result.get("json")),
        "usage": chat_result.get("json", {}).get("usage") if isinstance(chat_result.get("json"), dict) else {},
        "error": result_error_text(chat_result) if chat_decision != "pass" else "",
    },
    {
        "probe": "streaming_chat",
        "decision": stream_decision,
        "request_path": str(stream_request_path),
        "events_path": str(stream_event_path),
        "output_path": str(stream_output_path),
        "first_event_s": stream_result.get("first_event_s"),
        "first_content_delta_s": stream_result.get("first_content_delta_s"),
        "chunk_count": stream_result.get("chunk_count"),
        "content_chunk_count": stream_result.get("content_chunk_count"),
        "final_seen": stream_result.get("final_seen"),
        "final_text": stream_result.get("final_text", ""),
        "error": result_error_text(stream_result) if stream_decision not in {"pass", "skipped"} else "",
    },
    {
        "probe": "wrong_model_failure",
        "decision": bad_decision,
        "request_path": str(bad_request_path),
        "response_path": str(bad_response_path),
        "http_status": bad_result.get("http_status"),
        "error": result_error_text(bad_result),
    },
]

record = {
    "run_id": run_id,
    "timestamp": timestamp,
    "status": status,
    "compatible_decision": compatible_decision,
    "runtime": RUNTIME,
    "base_url": BASE_URL,
    "model": MODEL,
    "boundary": BOUNDARY,
    "expected_text": EXPECTED_TEXT,
    "temperature": TEMPERATURE,
    "max_tokens": MAX_TOKENS,
    "run_stream": RUN_STREAM,
    "run_bad_model": RUN_BAD_MODEL,
    "missing_layers": missing_layers,
    "next_action": next_action,
    "probes": {
        "models": probe_rows[0],
        "non_streaming_chat": probe_rows[1],
        "streaming_chat": probe_rows[2],
        "wrong_model_failure": probe_rows[3],
    },
    "probe_rows": probe_rows,
}

summary_json_path = OUT_DIR / f"{run_id}-contract-results.json"
summary_md_path = OUT_DIR / f"{run_id}-contract-results.md"
jsonl_path = OUT_DIR / "openai-contract-runs.jsonl"
write_json(summary_json_path, record)
write_markdown(summary_md_path, record)
append_jsonl(jsonl_path, record)

print(json.dumps({
    "status": status,
    "compatible_decision": compatible_decision,
    "run_id": run_id,
    "results_json": str(summary_json_path),
    "results_md": str(summary_md_path),
    "jsonl": str(jsonl_path),
    "missing_layers": missing_layers,
    "next_action": next_action,
}, indent=2, ensure_ascii=True))
```

## PowerShell Execution

Use a disposable evidence folder first:

```powershell
$env:LOCAL_LLM_RUN_ROOT = "D:\LLM-Runs\contract-$(Get-Date -Format yyyyMMdd-HHmmss)"
$env:LOCAL_LLM_BASE_URL = "http://127.0.0.1:11434/v1"
$env:LOCAL_LLM_MODEL = "<served-model-id>"
$env:LOCAL_LLM_API_KEY = "local"
$env:LOCAL_LLM_BOUNDARY = "loopback"
$env:LOCAL_LLM_EXPECT_TEXT = "api contract ok"
$env:LOCAL_LLM_RUN_STREAM = "1"
python .\openai-compatible-contract-runner.py
```

If streaming is not required for the workload, set:

```powershell
$env:LOCAL_LLM_RUN_STREAM = "0"
```

Do not change the prompt while comparing runtimes. If a runtime cannot return the exact expected text at temperature `0`, route that to the manual contract lab or troubleshooting before blaming the model.

## Result Interpretation

| Runner status | Meaning | Next route |
|---|---|---|
| `pass` | `/v1/models`, non-streaming chat, streaming if required, and wrong-model failure all produced usable evidence. | [[LLM/Study/Local LLM First Client Harness Runner]] |
| `hold` | Non-streaming chat worked, but at least one supporting contract layer is missing or partial. | Fill the missing layer in [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]] |
| `error` | The non-streaming chat contract did not pass. | [[LLM/Study/Local LLM Troubleshooting Decision Tree]] |

The model-list route is useful but not always decisive. If chat works and `/v1/models` is missing, record a runtime-native model-list proof in the manual contract card and keep the runner result as `hold` until the served model id is independently proven.

The wrong-model failure is intentional. A local server that accepts an obviously missing model id without a clear error should not be trusted by client harnesses, RAG systems, tool loops, or benchmark automation.

## Completion Gate

This runner pass is complete when you have:

- [ ] a saved `contract-results.json`
- [ ] a saved `contract-results.md`
- [ ] one appended `openai-contract-runs.jsonl` row
- [ ] `/v1/models` proof or a documented native model-list fallback
- [ ] one non-streaming `/v1/chat/completions` request and response
- [ ] one streaming result or an explicit "not required" decision
- [ ] one harmless wrong-model failure row
- [ ] a decision: `compatible`, `partial`, or `not-compatible`
- [ ] a next action routed to client harness, streaming timing, manual contract diagnosis, or troubleshooting

## References

Internal routes:

- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/Local LLM First Streaming Timing Runner]]
- [[LLM/Study/Local LLM First Benchmark Row Builder]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]

External/current docs checked 2026-06-15:

- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
- [OpenAI chat completions API reference](https://platform.openai.com/docs/api-reference/chat/create)
- [OpenAI model-list API reference](https://platform.openai.com/docs/api-reference/models/list)
