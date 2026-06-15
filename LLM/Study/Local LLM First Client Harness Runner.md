---
tags: [study, llm, inference, local-llm, client, harness, python, openai-compatible, evidence]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM First Client Harness Runner

> **One-line summary** After the local endpoint answers, run this first reusable client harness so local inference becomes a saved script, request file, response file, output text, and JSONL row instead of a one-off terminal success.

Use this after [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] proves the local `/v1` route and [[LLM/Study/Local LLM First Quality Probe Suite|Local LLM First Quality Probe Suite]] has at least one prompt worth rerunning through a client. The contract lab says which base URL, route, model id, and feature flags are safe. This runner turns that contract into repeatable client-side inference evidence.

Use [[LLM/Study/Local LLM First Streaming Timing Runner|Local LLM First Streaming Timing Runner]] after this when the next narrow question is perceived latency, first content delta, chunk count, and streaming errors. Use [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] when the harness needs retries, multiple prompt suites, tool traces, richer metrics, or integration into a real application. This note is the first small non-streaming pass.

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| Script runs against a local `/v1/chat/completions` endpoint | A normal client can call the local model. | Full OpenAI feature compatibility. |
| Request and response files are saved | The run can be inspected and reproduced. | The prompt is a good workload test. |
| Output text file exists | The client can extract assistant content. | The answer is correct. |
| JSONL row is appended | The run can feed benchmark and quality notes. | Production observability. |
| Error row is logged on failure | The client failure is diagnosable. | The server is fixed. |
| Same prompt id as the probe suite is used | Route, quality, and client evidence can be compared. | Full model selection. |

The useful claim is narrow: "I can run local inference from a reusable client and preserve enough evidence to review it."

## Fixed Conditions

Write these before running:

| Field | Value |
|---|---|
| Run folder |  |
| API contract card |  |
| First quality probe row |  |
| Runtime | Ollama / LM Studio / llama.cpp / vLLM / SGLang / other |
| Base URL | `http://127.0.0.1:11434/v1` for Ollama OpenAI-compatible route |
| Route | `/chat/completions` |
| Model id |  |
| Prompt id | `K-01` / `S-01` / workload prompt id |
| Temperature | `0` |
| Max tokens | `128` for first client proof |
| Auth behavior | placeholder bearer / none / real token / proxy |
| Log policy | redacted excerpt / full local-only output / no private content |

Do not put real hosted API keys in this runner. For Ollama's OpenAI-compatible route, the placeholder key is required by the OpenAI-style client pattern but ignored by Ollama.

## Standard-Library Runner

This version uses only Python's standard library. Save it as `first-client-harness.py` inside the run folder.

```python
import json
import os
import time
import uuid
import urllib.error
import urllib.request
from pathlib import Path

RUN_ROOT = Path(os.environ.get("LOCAL_LLM_RUN_ROOT", ".")).resolve()
BASE_URL = os.environ.get("LOCAL_LLM_BASE_URL", "http://127.0.0.1:11434/v1").rstrip("/")
ROUTE = os.environ.get("LOCAL_LLM_ROUTE", "/chat/completions")
MODEL = os.environ.get("LOCAL_LLM_MODEL", "<served-model-id>")
PROMPT_ID = os.environ.get("LOCAL_LLM_PROMPT_ID", "K-01")
AUTH_TOKEN = os.environ.get("LOCAL_LLM_API_KEY", "local")

HARNESS_DIR = RUN_ROOT / "first-client-harness"
REQUEST_DIR = HARNESS_DIR / "requests"
RESPONSE_DIR = HARNESS_DIR / "responses"
OUTPUT_DIR = HARNESS_DIR / "outputs"
for directory in (REQUEST_DIR, RESPONSE_DIR, OUTPUT_DIR):
    directory.mkdir(parents=True, exist_ok=True)

PROMPTS = {
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
response_path = RESPONSE_DIR / f"{run_id}-{PROMPT_ID}.json"
output_path = OUTPUT_DIR / f"{run_id}-{PROMPT_ID}.txt"
log_path = HARNESS_DIR / "client-runs.jsonl"

payload = {
    "model": MODEL,
    "messages": [
        {"role": "system", "content": case["system"]},
        {"role": "user", "content": case["user"]},
    ],
    "temperature": 0,
    "max_tokens": 128,
    "stream": False,
}

request_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

started_at = time.strftime("%Y-%m-%dT%H:%M:%S%z")
started = time.perf_counter()
status = "pass"
error_class = ""
http_status = ""
finish_reason = None
usage = {}
text = ""

try:
    request = urllib.request.Request(
        BASE_URL + ROUTE,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {AUTH_TOKEN}",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        raw = response.read().decode("utf-8")
    response_path.write_text(raw, encoding="utf-8")
    data = json.loads(raw)
    choice = data["choices"][0]
    text = choice["message"]["content"] or ""
    finish_reason = choice.get("finish_reason")
    usage = data.get("usage") or {}
except urllib.error.HTTPError as exc:
    status = "error"
    error_class = "HTTPError"
    http_status = exc.code
    text = exc.read().decode("utf-8", errors="replace")
    response_path.write_text(text, encoding="utf-8")
except Exception as exc:
    status = "error"
    error_class = type(exc).__name__
    text = str(exc)
    response_path.write_text(json.dumps({"error": text}, indent=2), encoding="utf-8")
finally:
    elapsed_s = time.perf_counter() - started

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
    "stream": False,
    "temperature": payload["temperature"],
    "max_tokens": payload["max_tokens"],
    "request_path": str(request_path),
    "response_path": str(response_path),
    "output_path": str(output_path),
    "latency_s": round(elapsed_s, 3),
    "finish_reason": finish_reason,
    "prompt_tokens": usage.get("prompt_tokens"),
    "output_tokens": usage.get("completion_tokens"),
    "total_tokens": usage.get("total_tokens"),
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
python .\first-client-harness.py
```

Pass signal: `first-client-harness\client-runs.jsonl`, request JSON, response JSON, and output text exist. A failure still passes the harness-logging check if the JSONL row names the error class and response path.

## Optional OpenAI SDK Adapter

Use this only after the Python `openai` package is intentionally installed in the environment. It should produce the same evidence fields as the standard-library runner.

```python
import json
import os
import time
import uuid
from pathlib import Path

from openai import OpenAI

RUN_ROOT = Path(os.environ.get("LOCAL_LLM_RUN_ROOT", ".")).resolve()
BASE_URL = os.environ.get("LOCAL_LLM_BASE_URL", "http://127.0.0.1:11434/v1")
MODEL = os.environ.get("LOCAL_LLM_MODEL", "<served-model-id>")
PROMPT_ID = os.environ.get("LOCAL_LLM_PROMPT_ID", "K-01")
API_KEY = os.environ.get("LOCAL_LLM_API_KEY", "ollama")

HARNESS_DIR = RUN_ROOT / "first-client-harness-sdk"
HARNESS_DIR.mkdir(parents=True, exist_ok=True)
log_path = HARNESS_DIR / "client-runs.jsonl"
run_id = f"{time.strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:8]}"

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

started = time.perf_counter()
completion = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "Answer the user exactly."},
        {"role": "user", "content": "Reply with exactly: local llm ok"},
    ],
    temperature=0,
    max_tokens=32,
)
elapsed_s = time.perf_counter() - started

text = completion.choices[0].message.content or ""
record = {
    "run_id": run_id,
    "runtime": "local-openai-sdk",
    "base_url": BASE_URL,
    "route": "/chat/completions",
    "model_id": MODEL,
    "prompt_id": PROMPT_ID,
    "latency_s": round(elapsed_s, 3),
    "finish_reason": completion.choices[0].finish_reason,
    "prompt_tokens": completion.usage.prompt_tokens if completion.usage else None,
    "output_tokens": completion.usage.completion_tokens if completion.usage else None,
    "status": "pass",
    "response_excerpt": " ".join(text.split())[:200],
}

with log_path.open("a", encoding="utf-8") as handle:
    handle.write(json.dumps(record, ensure_ascii=True) + "\n")

print(json.dumps(record, indent=2, ensure_ascii=True))
```

The SDK path is convenient, but the standard-library path is the proof floor. If the SDK fails and the standard-library path succeeds, route the mismatch to [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] before blaming the model.

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
| Response path |  |
| Output path |  |
| JSONL row |  |
| Latency seconds |  |
| Prompt tokens |  |
| Output tokens |  |
| Finish reason |  |
| Status/error |  |
| Next route | streaming timing / benchmark row builder / quality harness / API contract / troubleshooting |

## Failure Routing

| Symptom | Likely owner | Route |
|---|---|---|
| Connection refused | server process, port, or loopback binding | [[LLM/Study/Local LLM Serving Runbook]] |
| 404 or wrong route | base URL or `/v1` contract | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]] |
| model not found | served model id mismatch | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]] |
| HTTP success but empty text | response parser, template, stop rule, or model behavior | [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]] |
| output is wrong but route works | quality, prompt, sampler, or model capability | [[LLM/Study/Local LLM First Quality Probe Suite]] or [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| latency is high | cold load, prefill, decode, or memory pressure | [[LLM/Study/Local LLM Inference Metrics Field Guide]] |
| JSONL row leaks private text | logging policy | [[LLM/Study/Local LLM Security and Privacy Runbook]] |

## Completion Gate

This first client runner is complete only when:

- [ ] API contract card supplies base URL, route, model id, and auth behavior
- [ ] one script path is recorded
- [ ] one non-streaming local inference call is attempted
- [ ] request, response, output, and JSONL evidence paths exist
- [ ] success or failure is recorded as structured data
- [ ] one benchmark or quality row consumes the JSONL fields, or a blocker route is named
- [ ] private prompts and outputs are logged according to the security decision

## References

Internal routes:

- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM First Streaming Timing Runner]]
- [[LLM/Study/Local LLM First Benchmark Row Builder]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM First Quality Probe Suite]]
- [[LLM/Study/Local LLM Command Cookbook]]
- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]

External/current sources checked 2026-06-15:

- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
- [Ollama chat endpoint](https://docs.ollama.com/api/chat)
- [Ollama usage metrics](https://docs.ollama.com/api/usage)
- [OpenAI Python library reference](https://developers.openai.com/api/reference/python/)
- [OpenAI SDKs and CLI](https://developers.openai.com/api/docs/libraries)
- [OpenAI Python repository](https://github.com/openai/openai-python)
