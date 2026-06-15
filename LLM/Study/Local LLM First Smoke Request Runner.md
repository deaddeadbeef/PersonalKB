---
tags: [study, llm, inference, local-llm, smoke-test, ollama, openai-compatible, evidence]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM First Smoke Request Runner

> **One-line summary** After install, model pull, and runtime health pass, send one controlled local inference request through the native Ollama route and one through the OpenAI-compatible route, then save every request, response, output excerpt, status, and next action.

Use this after [[LLM/Study/Local LLM First Runtime Health Snapshot|Local LLM First Runtime Health Snapshot]] says the listener and model-list routes are ready, and before [[LLM/Study/Local LLM First Response Debrief Card|Local LLM First Response Debrief Card]]. The health snapshot does not generate text. This runner does: it is the first proof that a local model can answer a prompt through the endpoint you plan to use.

For the first Windows/Ollama pass, this runner can replace the manual native and OpenAI-compatible smoke snippets in [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]]. Keep the prompt deliberately boring. The goal is route proof, timing capture, and failure ownership, not model quality.

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| Saved native request body | The exact `/api/generate` call is reproducible. | That chat templates or OpenAI compatibility work. |
| Saved native response body | Ollama generated through the native endpoint and returned timing fields when available. | Workload quality. |
| Saved OpenAI-compatible request body | A generic `/v1/chat/completions` style call can be inspected. | Full OpenAI feature coverage. |
| Saved OpenAI-compatible response body | The selected model id can answer through the compatibility route. | Streaming, tools, JSON mode, or embeddings. |
| Extracted assistant text | The route produced text rather than only an error envelope. | Correctness beyond the smoke prompt. |
| Status and missing-layer row | The next owner is route, model id, prompt/output mismatch, server, or debrief. | Production readiness. |

Academic bridge: this single response is the first visible crossing from model bytes to runtime loader to request route to prefill/decode. Native Ollama timing fields can separate load time, prompt evaluation, and decode. A non-streaming smoke cannot measure TTFT; use [[LLM/Study/Local LLM First Streaming Timing Runner|Local LLM First Streaming Timing Runner]] after the endpoint works.

## Fixed Conditions

Write these before running:

| Field | Value |
|---|---|
| Run folder |  |
| Runtime health snapshot |  |
| Runtime | Ollama / LM Studio / llama.cpp / vLLM / SGLang / other |
| Native base URL | `http://127.0.0.1:11434` for Ollama |
| OpenAI-compatible base URL | `http://127.0.0.1:11434/v1` for Ollama |
| Model id |  |
| Prompt | `Reply with exactly: local llm ok` |
| Expected text | `local llm ok` |
| Temperature | `0` |
| Max tokens | `16` |
| Security boundary | loopback only / LAN / tunnel / remote |
| Next gate | response debrief / quality probe / route diagnosis / security review |

Do not run this against a LAN, tunnel, or remote endpoint until [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] says the exposure is intentional. Do not paste secrets into the prompt.

## Standard-Library Smoke Runner

Save this as `first-smoke-request.py` inside the run folder. It uses only Python's standard library.

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
    path.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def normalize_text(value):
    return " ".join(str(value or "").strip().lower().split())


def md_cell(value):
    return str(value or "").replace("|", "\\|").replace("\n", " ")


def post_json(url, body, timeout_s, headers=None):
    payload = json.dumps(body).encode("utf-8")
    request_headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    if headers:
        request_headers.update(headers)
    request = urllib.request.Request(url, data=payload, headers=request_headers, method="POST")
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(request, timeout=timeout_s) as response:
            raw = response.read().decode("utf-8", errors="replace")
            elapsed_s = time.perf_counter() - started
            try:
                parsed = json.loads(raw) if raw else None
            except json.JSONDecodeError:
                parsed = None
            return {
                "url": url,
                "status": "pass",
                "http_status": getattr(response, "status", None),
                "elapsed_s": round(elapsed_s, 3),
                "json": parsed,
                "raw_excerpt": " ".join(raw.split())[:500],
            }
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        elapsed_s = time.perf_counter() - started
        try:
            parsed = json.loads(raw) if raw else None
        except json.JSONDecodeError:
            parsed = None
        return {
            "url": url,
            "status": "error",
            "http_status": exc.code,
            "elapsed_s": round(elapsed_s, 3),
            "error_class": "HTTPError",
            "json": parsed,
            "raw_excerpt": " ".join(raw.split())[:500],
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


def extract_native(result):
    data = result.get("json") if isinstance(result, dict) else None
    if not isinstance(data, dict):
        return {"assistant_text": "", "done": None, "done_reason": "", "timing_ns": {}}
    message = data.get("message") if isinstance(data.get("message"), dict) else {}
    text = data.get("response") or message.get("content") or ""
    timing_keys = [
        "total_duration",
        "load_duration",
        "prompt_eval_count",
        "prompt_eval_duration",
        "eval_count",
        "eval_duration",
    ]
    return {
        "assistant_text": text,
        "done": data.get("done"),
        "done_reason": data.get("done_reason", ""),
        "timing_ns": {key: data.get(key) for key in timing_keys if key in data},
    }


def extract_openai(result):
    data = result.get("json") if isinstance(result, dict) else None
    if not isinstance(data, dict):
        return {"assistant_text": "", "finish_reason": "", "usage": {}}
    choices = data.get("choices") if isinstance(data.get("choices"), list) else []
    first = choices[0] if choices and isinstance(choices[0], dict) else {}
    message = first.get("message") if isinstance(first.get("message"), dict) else {}
    content = message.get("content", "")
    if isinstance(content, list):
        content = " ".join(str(part.get("text", "")) if isinstance(part, dict) else str(part) for part in content)
    return {
        "assistant_text": content or "",
        "finish_reason": first.get("finish_reason", ""),
        "usage": data.get("usage") if isinstance(data.get("usage"), dict) else {},
    }


def route_decision(result, assistant_text, expected_text):
    if result.get("status") != "pass":
        return "error"
    if not str(assistant_text).strip():
        return "hold"
    if expected_text and normalize_text(assistant_text) != normalize_text(expected_text):
        return "hold"
    return "pass"


def write_markdown(path, record):
    lines = [
        f"# First Smoke Request - {record['run_id']}",
        "",
        f"Status: `{record['status']}`",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Runtime | {md_cell(record['runtime'])} |",
        f"| Model | {md_cell(record['model'])} |",
        f"| Native base | {md_cell(record['native_base'])} |",
        f"| OpenAI base | {md_cell(record['openai_base'])} |",
        f"| Prompt | {md_cell(record['prompt'])} |",
        f"| Expected text | {md_cell(record['expected_text'])} |",
        f"| Native decision | {md_cell(record['native']['decision'])} |",
        f"| OpenAI-compatible decision | {md_cell(record['openai']['decision'])} |",
        f"| Missing layer | {md_cell(record['missing_layer'])} |",
        f"| Next action | {md_cell(record['next_action'])} |",
        "",
        "## Native Output",
        "",
        "```text",
        record["native"]["assistant_text"],
        "```",
        "",
        "## OpenAI-Compatible Output",
        "",
        "```text",
        record["openai"]["assistant_text"],
        "```",
        "",
        "## Response Files",
        "",
        "| Route | Request | Response | Output |",
        "|---|---|---|---|",
        f"| Native | {md_cell(record['native']['request_path'])} | {md_cell(record['native']['response_path'])} | {md_cell(record['native']['output_path'])} |",
        f"| OpenAI-compatible | {md_cell(record['openai']['request_path'])} | {md_cell(record['openai']['response_path'])} | {md_cell(record['openai']['output_path'])} |",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


RUN_ROOT = Path(os.environ.get("LOCAL_LLM_RUN_ROOT", ".")).resolve()
RUNTIME = os.environ.get("LOCAL_LLM_RUNTIME", "ollama")
MODEL = os.environ.get("LOCAL_LLM_MODEL", "<served-model-id>")
NATIVE_BASE = os.environ.get("LOCAL_LLM_NATIVE_BASE", "http://127.0.0.1:11434").rstrip("/")
OPENAI_BASE = os.environ.get("LOCAL_LLM_OPENAI_BASE", "http://127.0.0.1:11434/v1").rstrip("/")
PROMPT = os.environ.get("LOCAL_LLM_SMOKE_PROMPT", "Reply with exactly: local llm ok")
EXPECTED_TEXT = os.environ.get("LOCAL_LLM_EXPECT_TEXT", "local llm ok")
API_KEY = os.environ.get("LOCAL_LLM_API_KEY", "local")
TIMEOUT_S = float(os.environ.get("LOCAL_LLM_SMOKE_TIMEOUT_S", "60"))
MAX_TOKENS = int(os.environ.get("LOCAL_LLM_MAX_TOKENS", "16"))
TEMPERATURE = float(os.environ.get("LOCAL_LLM_TEMPERATURE", "0"))
RUN_NATIVE = env_bool("LOCAL_LLM_RUN_NATIVE", True)
RUN_OPENAI = env_bool("LOCAL_LLM_RUN_OPENAI", True)

out_dir = RUN_ROOT / "first-smoke-request"
request_dir = out_dir / "requests"
response_dir = out_dir / "responses"
output_dir = out_dir / "outputs"
for directory in (request_dir, response_dir, output_dir):
    directory.mkdir(parents=True, exist_ok=True)

run_id = f"{time.strftime('%Y%m%d-%H%M%S')}-first-smoke"
timestamp = time.strftime("%Y-%m-%dT%H:%M:%S%z")

native_body = {
    "model": MODEL,
    "prompt": PROMPT,
    "stream": False,
    "options": {
        "temperature": TEMPERATURE,
        "num_predict": MAX_TOKENS,
    },
}
openai_body = {
    "model": MODEL,
    "messages": [{"role": "user", "content": PROMPT}],
    "temperature": TEMPERATURE,
    "max_tokens": MAX_TOKENS,
    "stream": False,
}

native_request_path = request_dir / f"{run_id}-native-generate-request.json"
openai_request_path = request_dir / f"{run_id}-openai-chat-request.json"
native_response_path = response_dir / f"{run_id}-native-generate-response.json"
openai_response_path = response_dir / f"{run_id}-openai-chat-response.json"
native_output_path = output_dir / f"{run_id}-native-output.txt"
openai_output_path = output_dir / f"{run_id}-openai-output.txt"

write_json(native_request_path, native_body)
write_json(openai_request_path, openai_body)

if RUN_NATIVE:
    native_result = post_json(f"{NATIVE_BASE}/api/generate", native_body, TIMEOUT_S)
else:
    native_result = {"status": "skipped", "reason": "LOCAL_LLM_RUN_NATIVE=false"}

if RUN_OPENAI:
    openai_result = post_json(
        f"{OPENAI_BASE}/chat/completions",
        openai_body,
        TIMEOUT_S,
        headers={"Authorization": f"Bearer {API_KEY}"},
    )
else:
    openai_result = {"status": "skipped", "reason": "LOCAL_LLM_RUN_OPENAI=false"}

native_extract = extract_native(native_result)
openai_extract = extract_openai(openai_result)
native_decision = "skipped" if not RUN_NATIVE else route_decision(native_result, native_extract["assistant_text"], EXPECTED_TEXT)
openai_decision = "skipped" if not RUN_OPENAI else route_decision(openai_result, openai_extract["assistant_text"], EXPECTED_TEXT)

write_json(native_response_path, native_result)
write_json(openai_response_path, openai_result)
native_output_path.write_text(native_extract["assistant_text"] + "\n", encoding="utf-8")
openai_output_path.write_text(openai_extract["assistant_text"] + "\n", encoding="utf-8")

enabled_decisions = [decision for decision in (native_decision, openai_decision) if decision != "skipped"]
if enabled_decisions and all(decision == "pass" for decision in enabled_decisions):
    status = "pass"
elif enabled_decisions and any(decision in {"pass", "hold"} for decision in enabled_decisions):
    status = "hold"
else:
    status = "error"

missing = []
if native_decision == "error":
    missing.append("native route")
elif native_decision == "hold":
    missing.append("native exact smoke text")
if openai_decision == "error":
    missing.append("openai-compatible route")
elif openai_decision == "hold":
    missing.append("openai-compatible exact smoke text")
if not missing and status == "pass":
    missing.append("none")

default_next = {
    "pass": "first response debrief",
    "hold": "compare response text and route shape before quality probes",
    "error": "diagnose listener, model id, or route before retry",
}[status]
next_action = os.environ.get("LOCAL_LLM_NEXT_ACTION", default_next)

record = {
    "run_id": run_id,
    "timestamp": timestamp,
    "status": status,
    "runtime": RUNTIME,
    "model": MODEL,
    "native_base": NATIVE_BASE,
    "openai_base": OPENAI_BASE,
    "prompt": PROMPT,
    "expected_text": EXPECTED_TEXT,
    "temperature": TEMPERATURE,
    "max_tokens": MAX_TOKENS,
    "native": {
        "decision": native_decision,
        "assistant_text": native_extract["assistant_text"],
        "done": native_extract["done"],
        "done_reason": native_extract["done_reason"],
        "timing_ns": native_extract["timing_ns"],
        "request_path": str(native_request_path),
        "response_path": str(native_response_path),
        "output_path": str(native_output_path),
        "result_status": native_result.get("status"),
        "http_status": native_result.get("http_status"),
    },
    "openai": {
        "decision": openai_decision,
        "assistant_text": openai_extract["assistant_text"],
        "finish_reason": openai_extract["finish_reason"],
        "usage": openai_extract["usage"],
        "request_path": str(openai_request_path),
        "response_path": str(openai_response_path),
        "output_path": str(openai_output_path),
        "result_status": openai_result.get("status"),
        "http_status": openai_result.get("http_status"),
    },
    "missing_layer": ", ".join(missing),
    "next_action": next_action,
}

summary_json_path = out_dir / f"{run_id}-summary.json"
summary_md_path = out_dir / f"{run_id}-summary.md"
jsonl_path = out_dir / "first-smoke-requests.jsonl"
write_json(summary_json_path, record)
write_markdown(summary_md_path, record)
with jsonl_path.open("a", encoding="utf-8") as handle:
    handle.write(json.dumps(record, ensure_ascii=True) + "\n")

print(json.dumps({
    "status": status,
    "summary_json": str(summary_json_path),
    "summary_markdown": str(summary_md_path),
    "missing_layer": record["missing_layer"],
    "next_action": next_action,
}, indent=2))
```

PowerShell run for the first Ollama pass:

```powershell
$env:LOCAL_LLM_RUN_ROOT = "<paste-run-folder-path>"
$env:LOCAL_LLM_RUNTIME = "ollama"
$env:LOCAL_LLM_MODEL = "<model-tag-from-pull-gate>"
$env:LOCAL_LLM_NATIVE_BASE = "http://127.0.0.1:11434"
$env:LOCAL_LLM_OPENAI_BASE = "http://127.0.0.1:11434/v1"
$env:LOCAL_LLM_SMOKE_PROMPT = "Reply with exactly: local llm ok"
$env:LOCAL_LLM_EXPECT_TEXT = "local llm ok"
$env:LOCAL_LLM_TEMPERATURE = "0"
$env:LOCAL_LLM_MAX_TOKENS = "16"
python .\first-smoke-request.py
```

Pass signal: `first-smoke-request\<run-id>-summary.json` and `.md` exist, both enabled routes are `pass`, the extracted output text matches `local llm ok`, and the next action is `first response debrief`.

Hold signal: one route answers but the other route fails, the answer text is not the expected smoke text, or the response shape lacks extractable assistant text. Save the files; do not change prompt, model, runtime, and route at the same time.

## Evidence Row

Copy this row into [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]], [[LLM/Study/Local LLM First Inference Evidence Pack|Local LLM First Inference Evidence Pack]], or [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]:

| Field | Value |
|---|---|
| Run id |  |
| Runtime |  |
| Model id |  |
| Native base URL |  |
| OpenAI-compatible base URL |  |
| Prompt |  |
| Expected text |  |
| Native request |  |
| Native response |  |
| Native output |  |
| Native decision | pass / hold / error / skipped |
| OpenAI-compatible request |  |
| OpenAI-compatible response |  |
| OpenAI-compatible output |  |
| OpenAI-compatible decision | pass / hold / error / skipped |
| Summary JSON |  |
| Summary Markdown |  |
| Status | pass / hold / error |
| Missing layer |  |
| Next action | response debrief / route diagnosis / model-id diagnosis / quality probe |

## Failure Routing

| Observation | Likely owner | Route |
|---|---|---|
| Both routes connection-refuse or time out | server process, listener, firewall, wrong boundary | [[LLM/Study/Local LLM First Runtime Health Snapshot]] or [[LLM/Study/Local LLM Serving Runbook]] |
| Native works and OpenAI-compatible fails | compatibility base URL, model id, auth placeholder, route shape | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]] |
| OpenAI-compatible works and native fails | wrong native base URL or non-Ollama runtime | [[LLM/Study/Local LLM Runtime Stack Anatomy]] |
| Both routes answer but text is not exact | prompt formatting, sampler, chat template, or model instruction following | [[LLM/Study/Local LLM First Response Debrief Card]] before quality claims |
| Response has timing fields but no output text | response extraction mismatch or error-shaped JSON | [[LLM/Study/Local LLM First Response Debrief Card]] |
| Route works but answer quality is doubtful | smoke is route proof only | [[LLM/Study/Local LLM First Quality Probe Suite]] |

## Completion Gate

This smoke runner is complete only when:

- [ ] run folder exists
- [ ] runtime health snapshot exists or is explicitly skipped with reason
- [ ] model id, native base URL, OpenAI-compatible base URL, prompt, expected text, temperature, and max tokens are written
- [ ] native request/response/output files exist or native route is explicitly skipped
- [ ] OpenAI-compatible request/response/output files exist or OpenAI route is explicitly skipped
- [ ] summary JSON, summary Markdown, and `first-smoke-requests.jsonl` exist
- [ ] status is `pass`, `hold`, or `error` with a named missing layer
- [ ] next action names exactly one route: response debrief, route diagnosis, model-id diagnosis, security review, or quality probe

## References

Internal routes:

- [[LLM/Study/Local LLM First Runtime Health Snapshot]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM First Response Debrief Card]]
- [[LLM/Study/Local LLM First Quality Probe Suite]]
- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/Local LLM First Streaming Timing Runner]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Runtime Stack Anatomy]]

External/current sources checked 2026-06-15:

- [Ollama API introduction](https://docs.ollama.com/api/introduction)
- [Ollama generate endpoint](https://docs.ollama.com/api/generate)
- [Ollama chat endpoint](https://docs.ollama.com/api/chat)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
