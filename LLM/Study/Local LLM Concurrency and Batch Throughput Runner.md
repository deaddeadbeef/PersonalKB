---
tags: [study, llm, inference, local-llm, concurrency, batching, throughput, queueing, latency, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-15
---

# Local LLM Concurrency and Batch Throughput Runner

> **One-line summary** Run a controlled local concurrency ladder against an OpenAI-compatible endpoint and save per-request latency, p50/p95, success/error, throughput, and saturation evidence.

Use this after [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab|Local LLM Concurrency and Batch Throughput Lab]] explains the manual method and after [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner|Local LLM OpenAI-Compatible API Contract Runner]] proves the base route. Use it before claiming that a local model can handle shared use, a local queue, multi-client traffic, or offline batch throughput.

This runner sends real local HTTP requests when pointed at an actual endpoint. For verification or dry runs, point `LOCAL_LLM_BASE_URL` at a fake loopback fixture server. Keep the first real run on loopback, use synthetic prompts, and stop before thermal, memory, queue, or timeout behavior becomes unsafe.

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| Fixed prompt and sampler config | The concurrency ladder changed load, not prompt, model, sampler, or output cap. | That the prompt is representative of every workload. |
| Per-request CSV/JSONL rows | Each request has latency, status, error, finish reason, and output-token evidence. | Server-side queue time unless the runtime exposes it. |
| Per-level ladder CSV | C1/C2/C4-style levels have comparable success, p50/p95, throughput, and error rows. | Exact scheduler internals. |
| Optional streaming TTFT | The client can measure first-token timing when the route streams SSE chunks. | TTFT for non-streaming runs. |
| Saturation decision | The first concurrency where latency, errors, or throughput flattening matters is explicit. | A universal capacity limit across prompts, context windows, and models. |
| JSON/Markdown/JSONL output | Concurrency evidence can feed the benchmark log, deployment matrix, and capstone workbook. | Production observability or long-run reliability. |

Academic bridge: concurrency increases active sequences, KV-cache pressure, scheduler contention, and queueing. Continuous batching can raise total throughput, but interactive quality depends on p95 latency and first-token responsiveness. A local server that passes one request can still fail as soon as two users or a small batch arrive.

## Fixed Conditions

Write these before running:

| Field | Value |
|---|---|
| Run folder |  |
| API contract runner result |  |
| Single-request baseline |  |
| Context budget runner result |  |
| Runtime | Ollama / LM Studio / llama.cpp / vLLM / SGLang / other |
| Base URL | `http://127.0.0.1:11434/v1` for an OpenAI-compatible local route |
| Model id |  |
| Concurrency levels | `1,2,4` |
| Requests per level |  |
| Output cap |  |
| Prompt mode | short / mixed |
| Streaming TTFT | on / off |
| Runtime concurrency knobs | `OLLAMA_NUM_PARALLEL`, Max Concurrent Predictions, `--parallel`, `--max-concurrency`, or equivalent |
| Boundary | loopback / LAN / tunnel / remote |
| Next gate | benchmark log / deployment matrix / scheduler lab / troubleshooting |

If the endpoint is exposed beyond loopback, complete [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] before running a load test.

## Standard-Library Runner

Save this as `concurrency-batch-throughput-runner.py` inside the run folder. It uses only Python's standard library.

```python
import csv
import json
import math
import os
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
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


def as_int(value, default):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def as_float(value, default):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def parse_int_list(value, default):
    if not value:
        return default
    levels = []
    for part in str(value).split(","):
        number = as_int(part.strip(), 0)
        if number > 0:
            levels.append(number)
    return levels or default


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


def try_json_loads(value):
    if isinstance(value, (dict, list)):
        return value, ""
    if value is None:
        return None, "empty value"
    text = str(value).strip()
    if not text:
        return None, "empty value"
    try:
        return json.loads(text), ""
    except json.JSONDecodeError as exc:
        return None, f"json decode error: {exc}"


def extract_message(data):
    if not isinstance(data, dict):
        return {}
    choices = data.get("choices") if isinstance(data.get("choices"), list) else []
    first = choices[0] if choices and isinstance(choices[0], dict) else {}
    message = first.get("message") if isinstance(first.get("message"), dict) else {}
    return message


def extract_content_text(data):
    return content_to_text(extract_message(data).get("content"))


def extract_finish_reason(data):
    if not isinstance(data, dict):
        return ""
    choices = data.get("choices") if isinstance(data.get("choices"), list) else []
    first = choices[0] if choices and isinstance(choices[0], dict) else {}
    return str(first.get("finish_reason") or "")


def extract_completion_tokens(data, text):
    if isinstance(data, dict) and isinstance(data.get("usage"), dict):
        value = data["usage"].get("completion_tokens")
        if isinstance(value, int):
            return value, "usage.completion_tokens"
    return max(1, math.ceil(len(str(text or "")) / 4)), "char_estimate"


def percentile(values, pct):
    ordered = sorted(float(v) for v in values if v is not None)
    if not ordered:
        return None
    if len(ordered) == 1:
        return round(ordered[0], 2)
    rank = (len(ordered) - 1) * pct
    lower = math.floor(rank)
    upper = math.ceil(rank)
    if lower == upper:
        return round(ordered[int(rank)], 2)
    fraction = rank - lower
    return round(ordered[lower] * (1 - fraction) + ordered[upper] * fraction, 2)


def prompt_for(index, prompt_mode):
    if prompt_mode == "mixed" and index % 5 == 0:
        details = " ".join([
            "This is a longer synthetic prompt used to stress prefill and queueing.",
            "Summarize the constraints, keep the answer short, and include the request id.",
            "No private data is present; this is a local concurrency benchmark fixture.",
        ])
        return f"Request {index}: {details}"
    return f"Request {index}: reply with 'concurrency ok {index}' and one short sentence."


def make_body(prompt, request_id):
    return {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a concise local benchmark assistant. Keep answers short."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0,
        "stream": STREAM,
        "max_tokens": MAX_TOKENS,
    }


def parse_sse(raw_line):
    line = raw_line.decode("utf-8", errors="replace").strip()
    if not line or line.startswith(":"):
        return None, False
    if not line.startswith("data:"):
        return None, False
    data = line[5:].strip()
    if data == "[DONE]":
        return None, True
    parsed, error = try_json_loads(data)
    if error:
        return {"parse_error": error, "raw": data}, False
    return parsed, False


def stream_delta_text(data):
    if not isinstance(data, dict):
        return ""
    choices = data.get("choices") if isinstance(data.get("choices"), list) else []
    first = choices[0] if choices and isinstance(choices[0], dict) else {}
    delta = first.get("delta") if isinstance(first.get("delta"), dict) else {}
    if "content" in delta:
        return content_to_text(delta.get("content"))
    message = first.get("message") if isinstance(first.get("message"), dict) else {}
    if "content" in message:
        return content_to_text(message.get("content"))
    return ""


def run_request(level, sequence_index):
    request_id = f"c{level}-r{sequence_index}"
    prompt = prompt_for(sequence_index, PROMPT_MODE)
    body = make_body(prompt, request_id)
    payload = json.dumps(body).encode("utf-8")
    request = urllib.request.Request(
        CHAT_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    if API_KEY:
        request.add_header("Authorization", f"Bearer {API_KEY}")

    started = time.perf_counter()
    ttft_ms = None
    text = ""
    finish_reason = ""
    completion_tokens = 0
    token_source = ""
    http_status = 0
    error = ""
    parse_error = ""
    ok = False

    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            http_status = response.status
            if STREAM:
                chunks = []
                for raw_line in response:
                    data, done = parse_sse(raw_line)
                    if done:
                        break
                    if data is None:
                        continue
                    delta = stream_delta_text(data)
                    if delta and ttft_ms is None:
                        ttft_ms = round((time.perf_counter() - started) * 1000, 2)
                    if delta:
                        chunks.append(delta)
                    if isinstance(data, dict):
                        finish_reason = extract_finish_reason(data) or finish_reason
                text = "".join(chunks)
                completion_tokens, token_source = extract_completion_tokens({}, text)
                ok = 200 <= response.status < 300 and bool(text)
            else:
                raw = response.read().decode("utf-8", errors="replace")
                data, parse_error = try_json_loads(raw)
                text = extract_content_text(data)
                finish_reason = extract_finish_reason(data)
                completion_tokens, token_source = extract_completion_tokens(data, text)
                ok = 200 <= response.status < 300 and not parse_error and bool(text)
    except urllib.error.HTTPError as exc:
        http_status = exc.code
        raw = exc.read().decode("utf-8", errors="replace")
        data, parse_error = try_json_loads(raw)
        error = str(exc)
        text = extract_content_text(data) if isinstance(data, dict) else raw[:500]
    except (urllib.error.URLError, TimeoutError) as exc:
        error = str(exc)
    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"

    total_ms = round((time.perf_counter() - started) * 1000, 2)
    return {
        "level": level,
        "request_id": request_id,
        "sequence_index": sequence_index,
        "prompt_mode": PROMPT_MODE,
        "prompt_chars": len(prompt),
        "stream": STREAM,
        "ok": ok,
        "http_status": http_status,
        "ttft_ms": ttft_ms,
        "total_ms": total_ms,
        "completion_tokens": completion_tokens,
        "token_source": token_source,
        "finish_reason": finish_reason,
        "error": error,
        "parse_error": parse_error,
        "output_excerpt": text[:300],
    }


def summarize_level(level, rows, elapsed_s):
    successes = [row for row in rows if row["ok"]]
    errors = [row for row in rows if not row["ok"]]
    total_values = [row["total_ms"] for row in successes]
    ttft_values = [row["ttft_ms"] for row in successes if row.get("ttft_ms") is not None]
    output_tokens = sum(row["completion_tokens"] for row in successes)
    return {
        "level": level,
        "requests": len(rows),
        "successes": len(successes),
        "errors": len(errors),
        "elapsed_s": round(elapsed_s, 3),
        "request_throughput_per_s": round(len(successes) / elapsed_s, 3) if elapsed_s > 0 else 0,
        "output_tokens_per_s": round(output_tokens / elapsed_s, 3) if elapsed_s > 0 else 0,
        "p50_total_ms": percentile(total_values, 0.50),
        "p95_total_ms": percentile(total_values, 0.95),
        "p50_ttft_ms": percentile(ttft_values, 0.50),
        "p95_ttft_ms": percentile(ttft_values, 0.95),
        "error_examples": sorted({row["error"] or row["parse_error"] or f"HTTP {row['http_status']}" for row in errors if row})[:3],
    }


RUN_ROOT = Path(os.environ.get("LOCAL_LLM_RUN_ROOT", ".")).expanduser().resolve()
BASE_URL = os.environ.get("LOCAL_LLM_BASE_URL", "").strip().rstrip("/")
MODEL = os.environ.get("LOCAL_LLM_MODEL", "").strip()
API_KEY = os.environ.get("LOCAL_LLM_API_KEY", "").strip()
TIMEOUT_SECONDS = as_float(os.environ.get("LOCAL_LLM_TIMEOUT_SECONDS"), 60.0)
MAX_TOKENS = as_int(os.environ.get("LOCAL_LLM_MAX_TOKENS"), 96)
REQUESTS_PER_LEVEL = as_int(os.environ.get("LOCAL_LLM_REQUESTS_PER_LEVEL"), 6)
CONCURRENCY_LEVELS = parse_int_list(os.environ.get("LOCAL_LLM_CONCURRENCY_LEVELS"), [1, 2, 4])
PROMPT_MODE = os.environ.get("LOCAL_LLM_PROMPT_MODE", "short").strip().lower()
STREAM = env_bool("LOCAL_LLM_STREAM", False)
TARGET_P95_TOTAL_MS = as_float(os.environ.get("LOCAL_LLM_TARGET_P95_TOTAL_MS"), 0.0)
RUN_ID = time.strftime("%Y%m%d-%H%M%S-concurrency")
OUT_DIR = RUN_ROOT / "concurrency-batch-throughput-runner"
CHAT_URL = join_url(BASE_URL, "/chat/completions") if BASE_URL else ""

summary = {
    "run_id": RUN_ID,
    "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
    "base_url": BASE_URL,
    "model": MODEL,
    "stream": STREAM,
    "prompt_mode": PROMPT_MODE,
    "max_tokens": MAX_TOKENS,
    "requests_per_level": REQUESTS_PER_LEVEL,
    "concurrency_levels": CONCURRENCY_LEVELS,
    "status": "hold",
    "output_dir": str(OUT_DIR),
    "ladder": [],
    "notes": [],
}

if not BASE_URL or not MODEL:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    sample = {
        "LOCAL_LLM_RUN_ROOT": str(RUN_ROOT),
        "LOCAL_LLM_BASE_URL": "http://127.0.0.1:11434/v1",
        "LOCAL_LLM_MODEL": "your-local-model-id",
        "LOCAL_LLM_CONCURRENCY_LEVELS": "1,2,4",
        "LOCAL_LLM_REQUESTS_PER_LEVEL": "6",
        "LOCAL_LLM_MAX_TOKENS": "96",
        "LOCAL_LLM_STREAM": "0",
    }
    write_json(OUT_DIR / "concurrency-batch-throughput-runner-env-template.json", sample)
    summary["status"] = "error"
    summary["next_action"] = "Set LOCAL_LLM_BASE_URL and LOCAL_LLM_MODEL, or point them at a fake loopback fixture server."
    write_json(OUT_DIR / f"{RUN_ID}-concurrency-results.json", summary)
    print(json.dumps({"status": summary["status"], "template": str(OUT_DIR / "concurrency-batch-throughput-runner-env-template.json")}, indent=2))
    raise SystemExit(0)

all_rows = []
for level in CONCURRENCY_LEVELS:
    started_level = time.perf_counter()
    level_rows = []
    with ThreadPoolExecutor(max_workers=level) as executor:
        futures = [executor.submit(run_request, level, index + 1) for index in range(REQUESTS_PER_LEVEL)]
        for future in as_completed(futures):
            row = future.result()
            level_rows.append(row)
            all_rows.append(row)
    elapsed_s = time.perf_counter() - started_level
    level_rows.sort(key=lambda item: item["sequence_index"])
    summary["ladder"].append(summarize_level(level, level_rows, elapsed_s))

first_failure = next((row for row in summary["ladder"] if row["errors"] > 0), None)
if first_failure:
    summary["status"] = "hold"
    summary["saturation_level"] = first_failure["level"]
    summary["next_action"] = "Investigate errors, overload, timeouts, or queue limits before raising concurrency."
else:
    over_target = None
    if TARGET_P95_TOTAL_MS > 0:
        over_target = next((row for row in summary["ladder"] if (row["p95_total_ms"] or 0) > TARGET_P95_TOTAL_MS), None)
    if over_target:
        summary["status"] = "hold"
        summary["saturation_level"] = over_target["level"]
        summary["next_action"] = "P95 total latency crossed the target; choose a lower concurrency or adjust runtime queue/backpressure."
    else:
        summary["status"] = "pass"
        summary["saturation_level"] = ""
        summary["next_action"] = "Use the highest passing level only if p95 latency, memory headroom, and quality are acceptable for the workload."

if not STREAM:
    summary["notes"].append("TTFT is blank because LOCAL_LLM_STREAM=0. Use streaming mode when first-token latency matters.")

summary_json_path = OUT_DIR / f"{RUN_ID}-concurrency-results.json"
summary_md_path = OUT_DIR / f"{RUN_ID}-concurrency-results.md"
ladder_csv_path = OUT_DIR / f"{RUN_ID}-concurrency-ladder.csv"
requests_csv_path = OUT_DIR / f"{RUN_ID}-concurrency-requests.csv"
requests_jsonl_path = OUT_DIR / f"{RUN_ID}-concurrency-requests.jsonl"
runs_jsonl_path = OUT_DIR / "concurrency-batch-throughput-runs.jsonl"

write_json(summary_json_path, summary)

with ladder_csv_path.open("w", newline="", encoding="utf-8") as handle:
    fieldnames = [
        "level",
        "requests",
        "successes",
        "errors",
        "elapsed_s",
        "request_throughput_per_s",
        "output_tokens_per_s",
        "p50_total_ms",
        "p95_total_ms",
        "p50_ttft_ms",
        "p95_ttft_ms",
        "error_examples",
    ]
    writer = csv.DictWriter(handle, fieldnames=fieldnames)
    writer.writeheader()
    for row in summary["ladder"]:
        clean = dict(row)
        clean["error_examples"] = json.dumps(clean["error_examples"], ensure_ascii=True)
        writer.writerow(clean)

with requests_csv_path.open("w", newline="", encoding="utf-8") as handle:
    fieldnames = [
        "level",
        "request_id",
        "sequence_index",
        "prompt_mode",
        "prompt_chars",
        "stream",
        "ok",
        "http_status",
        "ttft_ms",
        "total_ms",
        "completion_tokens",
        "token_source",
        "finish_reason",
        "error",
        "parse_error",
        "output_excerpt",
    ]
    writer = csv.DictWriter(handle, fieldnames=fieldnames)
    writer.writeheader()
    for row in sorted(all_rows, key=lambda item: (item["level"], item["sequence_index"])):
        writer.writerow(row)
        append_jsonl(requests_jsonl_path, row)

md_lines = [
    f"# Concurrency and Batch Throughput Run - {RUN_ID}",
    "",
    f"- Status: `{summary['status']}`",
    f"- Model: `{MODEL}`",
    f"- Base URL: `{BASE_URL}`",
    f"- Stream: `{STREAM}`",
    f"- Prompt mode: `{PROMPT_MODE}`",
    f"- Requests per level: `{REQUESTS_PER_LEVEL}`",
    f"- Levels: `{', '.join(str(item) for item in CONCURRENCY_LEVELS)}`",
    f"- Next action: {summary['next_action']}",
    "",
    "| Level | Success | Errors | Req/s | Output tok/s | p50 total ms | p95 total ms | p50 TTFT ms | p95 TTFT ms |",
    "|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
]
for row in summary["ladder"]:
    md_lines.append(
        f"| {md_cell(row['level'])} | {md_cell(row['successes'])}/{md_cell(row['requests'])} | "
        f"{md_cell(row['errors'])} | {md_cell(row['request_throughput_per_s'])} | "
        f"{md_cell(row['output_tokens_per_s'])} | {md_cell(row['p50_total_ms'])} | "
        f"{md_cell(row['p95_total_ms'])} | {md_cell(row['p50_ttft_ms'])} | {md_cell(row['p95_ttft_ms'])} |"
    )
if summary["notes"]:
    md_lines.extend(["", "## Notes", ""])
    md_lines.extend(f"- {note}" for note in summary["notes"])
write_text(summary_md_path, "\n".join(md_lines))

append_jsonl(runs_jsonl_path, summary)

print(json.dumps({
    "status": summary["status"],
    "run_id": RUN_ID,
    "results_json": str(summary_json_path),
    "results_md": str(summary_md_path),
    "ladder_csv": str(ladder_csv_path),
    "requests_csv": str(requests_csv_path),
    "requests_jsonl": str(requests_jsonl_path),
    "runs_jsonl": str(runs_jsonl_path),
}, indent=2, ensure_ascii=True))
```

## Environment Variables

| Variable | Required | Meaning |
|---|---:|---|
| `LOCAL_LLM_RUN_ROOT` | no | Evidence root. Defaults to the current directory. |
| `LOCAL_LLM_BASE_URL` | yes | OpenAI-compatible base URL such as `http://127.0.0.1:11434/v1`. |
| `LOCAL_LLM_MODEL` | yes | Served model id. |
| `LOCAL_LLM_API_KEY` | no | Local placeholder token or proxy token. The runner records only whether a token was configured. |
| `LOCAL_LLM_CONCURRENCY_LEVELS` | no | Comma list such as `1,2,4`. Defaults to `1,2,4`. |
| `LOCAL_LLM_REQUESTS_PER_LEVEL` | no | Requests submitted for each level. Defaults to `6`. |
| `LOCAL_LLM_MAX_TOKENS` | no | Output cap. Defaults to `96`. |
| `LOCAL_LLM_STREAM` | no | Set `1` to request SSE streaming and measure TTFT. Defaults to `0`. |
| `LOCAL_LLM_PROMPT_MODE` | no | `short` or `mixed`. Mixed inserts periodic longer synthetic prompts. |
| `LOCAL_LLM_TARGET_P95_TOTAL_MS` | no | Optional latency target that turns a high-p95 level into `hold`. |
| `LOCAL_LLM_TIMEOUT_SECONDS` | no | Per-request timeout. Defaults to `60`. |

PowerShell example:

```powershell
$env:LOCAL_LLM_RUN_ROOT = "D:\LLM-runs\concurrency-001"
$env:LOCAL_LLM_BASE_URL = "http://127.0.0.1:11434/v1"
$env:LOCAL_LLM_MODEL = "qwen3"
$env:LOCAL_LLM_CONCURRENCY_LEVELS = "1,2,4"
$env:LOCAL_LLM_REQUESTS_PER_LEVEL = "8"
$env:LOCAL_LLM_STREAM = "1"
python .\concurrency-batch-throughput-runner.py
```

## Result Interpretation

| Runner status | Meaning | Next move |
|---|---|---|
| `pass` | All submitted requests returned usable text and optional latency target was not crossed. | Compare the ladder with memory, quality, and runtime logs before choosing the deployment setting. |
| `hold` | A level had errors, overload, timeout, parse failure, or crossed the optional p95 latency target. | Treat the first held level as saturation or a diagnostic boundary. |
| `error` | Required configuration was missing. | Set base URL and model id, or run against a fake fixture server. |

Interpret `pass` narrowly. It means the client-side ladder completed, not that production capacity is solved. You still need peak RAM/VRAM, runtime logs, quality under load, and backpressure policy before deployment.

## Runtime Knobs To Record Beside This Runner

| Runtime | Knobs or evidence to copy next to the runner output |
|---|---|
| Ollama | `OLLAMA_NUM_PARALLEL`, `OLLAMA_MAX_QUEUE`, `OLLAMA_MAX_LOADED_MODELS`, `OLLAMA_CONTEXT_LENGTH`, `OLLAMA_KV_CACHE_TYPE`, `ollama ps`, and any 503 overload rows. |
| LM Studio | Max Concurrent Predictions, llama.cpp runtime version, model TTL, context length, GPU offload, and OpenAI-compatible route proof. |
| llama.cpp server | Startup command with `--parallel`, `/slots`, metrics endpoint if enabled, context size, prompt cache setting, and overload behavior. |
| vLLM | `benchmark_serving` settings such as `--request-rate`, `--max-concurrency`, burstiness, prompt lengths, output lengths, prefix cache, and `/metrics` when enabled. |
| SGLang | `bench_serving` settings, `--max-concurrency`, prompt/output lengths, RadixAttention/cache settings, server launch config, and profiling output when needed. |

## Completion Gate

This runner is complete when you have:

- [ ] a saved `concurrency-results.json`
- [ ] a saved `concurrency-results.md`
- [ ] a saved `concurrency-ladder.csv`
- [ ] a saved `concurrency-requests.csv`
- [ ] a saved `concurrency-requests.jsonl`
- [ ] appended `concurrency-batch-throughput-runs.jsonl`
- [ ] C1 plus at least one higher level, or a named blocker
- [ ] success/error counts, p50/p95 total latency, throughput, and optional TTFT if streaming
- [ ] a note for peak RAM/VRAM or the reason it was unavailable
- [ ] a handoff to [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Local LLM Serving Internals and Scheduler Lab]], [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]], or [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]]

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]]
- [[LLM/Study/Local LLM First Streaming Timing Runner]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]

Current external docs checked 2026-06-15:

- [Ollama FAQ concurrency settings](https://docs.ollama.com/faq)
- [LM Studio parallel requests](https://lmstudio.ai/docs/app/advanced/parallel-requests)
- [vLLM benchmark CLI](https://docs.vllm.ai/en/latest/benchmarking/cli/)
- [SGLang benchmarking and profiling](https://sgl-project.github.io/developer_guide/benchmark_and_profiling.html)
- [llama.cpp HTTP server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
