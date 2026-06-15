---
tags: [study, llm, inference, local-llm, observability, operations, metrics, logs, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-15
---

# Local LLM Observability and Operations Runner

> **One-line summary** Capture a no-generation operations snapshot for a local LLM service: route reachability, loaded model state, runtime metrics, slots, local resource evidence, redacted log tails, privacy posture, and the next controlled action.

Use this after [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]] defines the manual evidence standard. Use it before accepting a latency, memory, queue, cache, error, or service-state claim as real operations evidence. Use [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner|Local LLM Service Lifecycle and Upgrade Runner]] next when the observation will drive a restart, upgrade, model-cache move, UI update, startup change, or rollback.

This runner does not send a generation request. It calls read-only endpoints such as `/v1/models`, Ollama `/api/ps`, Prometheus-style `/metrics`, and llama.cpp `/slots`, then optionally tails local logs and runs a local GPU snapshot. Use the benchmark, concurrency, prompt-cache, speculative-decoding, quality, or tool runners when the claim needs inference output.

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| `/v1/models` route snapshot | The OpenAI-compatible route is reachable and exposes model ids. | That chat completion works; use the API contract runner. |
| Ollama `/api/ps` snapshot | The Ollama daemon has loaded model state. | That Ollama response timings are acceptable. |
| `/metrics` scrape | Runtime counters for queue, KV/cache, tokens, errors, or resource pressure are visible. | Comparable metric names across vLLM, SGLang, llama.cpp, and proxies. |
| `/slots` scrape | llama.cpp slot/context state is visible when exposed. | Full scheduler behavior under load. |
| `nvidia-smi` or explicit unavailable row | GPU resource evidence was checked locally. | CPU/RAM pressure unless you add a separate observer. |
| Redacted log tails | Recent service errors are attached without leaking obvious secrets. | That all private prompt text is removed; keep raw logs local. |
| JSON/CSV/Markdown/JSONL output | The operations decision can feed the capstone workbook, benchmark log, deployment matrix, and troubleshooting tree. | Long-run service reliability or post-upgrade survival. |

Academic bridge: operations evidence connects serving theory to the live system. Queue depth, active requests, KV/cache pressure, slot state, preemption, error rate, and memory pressure name the mechanism owner before you tune model size, context length, concurrency, cache flags, speculative decoding, or runtime choice.

## Fixed Conditions

Write these before running:

| Field | Value |
|---|---|
| Run folder |  |
| Runtime | Ollama / LM Studio / llama.cpp / vLLM / SGLang / other |
| Startup command or service mode |  |
| OpenAI-compatible base URL |  |
| Native runtime URL |  |
| Expected model id |  |
| Metrics URLs |  |
| Slots URLs |  |
| Log paths tailed |  |
| GPU/resource observer | enabled / unavailable / disabled |
| Privacy boundary | loopback / LAN / shared host / unknown |
| Next gate | API contract / benchmark / concurrency / cache / speculation / troubleshooting / lifecycle |

If the service is exposed beyond loopback, complete [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] before collecting logs.

## Standard-Library Runner

Save this as `observability-operations-runner.py` inside the run folder. It uses only Python's standard library.

```python
import csv
import json
import os
import platform
import re
import shutil
import socket
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path


SECRET_PATTERNS = [
    re.compile(r"(?i)(authorization:\s*bearer\s+)[A-Za-z0-9._\-+/=]+"),
    re.compile(r"(?i)(api[_-]?key['\"\s:=]+)[A-Za-z0-9._\-+/=]+"),
    re.compile(r"(?i)(token['\"\s:=]+)[A-Za-z0-9._\-+/=]+"),
    re.compile(r"(?i)(password['\"\s:=]+)\S+"),
]

METRIC_KEYWORDS = (
    "request",
    "waiting",
    "running",
    "queue",
    "latency",
    "ttft",
    "time_to_first",
    "token",
    "throughput",
    "kv",
    "cache",
    "prefix",
    "gpu",
    "memory",
    "preempt",
    "error",
    "fail",
    "slot",
)


def env_bool(name, default):
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() not in {"0", "false", "no", "off"}


def as_int(value, default):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def append_jsonl(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(data, ensure_ascii=True) + "\n")


def md_cell(value):
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True)
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def split_urls(value):
    if not value:
        return []
    return [item.strip() for item in value.replace(";", ",").split(",") if item.strip()]


def split_log_paths(value):
    if not value:
        return []
    return [item.strip().strip('"') for item in value.split(";") if item.strip()]


def join_url(base_url, route):
    return f"{base_url.rstrip('/')}/{route.lstrip('/')}"


def auth_headers():
    headers = {"Accept": "application/json, text/plain, */*"}
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"
    return headers


def redact(text):
    redacted = text
    for pattern in SECRET_PATTERNS:
        redacted = pattern.sub(r"\1<redacted>", redacted)
    return redacted


def body_to_json(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def fetch_source(source_id, source_type, url, expect_json=False, operation_signal=False):
    started = time.perf_counter()
    record = {
        "source_id": source_id,
        "source_type": source_type,
        "url": url,
        "status": "error",
        "ok": False,
        "operation_signal": operation_signal,
        "elapsed_ms": None,
        "bytes": 0,
        "result_path": "",
        "note": "",
    }
    request = urllib.request.Request(url, headers=auth_headers(), method="GET")
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            raw = response.read()
            status_code = getattr(response, "status", 200)
        elapsed_ms = round((time.perf_counter() - started) * 1000, 3)
        text = raw.decode("utf-8", errors="replace")
        parsed = body_to_json(text)
        extension = "json" if parsed is not None else "txt"
        result_path = OUT_DIR / f"{RUN_ID}-{source_id}.{extension}"
        if parsed is not None:
            write_json(result_path, parsed)
        else:
            write_text(result_path, text)
        record.update(
            {
                "status": str(status_code),
                "ok": 200 <= int(status_code) < 400 and (parsed is not None or not expect_json),
                "elapsed_ms": elapsed_ms,
                "bytes": len(raw),
                "result_path": str(result_path),
                "note": "json" if parsed is not None else "text",
                "parsed": parsed,
                "text": text if parsed is None else "",
            }
        )
    except urllib.error.HTTPError as exc:
        raw = exc.read()
        text = raw.decode("utf-8", errors="replace")
        result_path = OUT_DIR / f"{RUN_ID}-{source_id}-error.txt"
        write_text(result_path, text)
        record.update(
            {
                "status": f"HTTP {exc.code}",
                "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
                "bytes": len(raw),
                "result_path": str(result_path),
                "note": text[:200].replace("\n", " "),
            }
        )
    except Exception as exc:
        record.update(
            {
                "status": "error",
                "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
                "note": f"{type(exc).__name__}: {exc}",
            }
        )
    return record


def relevant_metric_lines(text):
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        lowered = stripped.lower()
        if any(keyword in lowered for keyword in METRIC_KEYWORDS):
            lines.append(stripped)
    return lines[:120]


def summarize_metrics(record):
    if not record.get("ok"):
        return record
    text = record.get("text")
    if not text and record.get("result_path"):
        text = Path(record["result_path"]).read_text(encoding="utf-8", errors="replace")
    lines = relevant_metric_lines(text or "")
    summary_path = OUT_DIR / f"{RUN_ID}-{record['source_id']}-relevant-lines.txt"
    write_text(summary_path, "\n".join(lines) + ("\n" if lines else ""))
    record["relevant_line_count"] = len(lines)
    record["relevant_lines_path"] = str(summary_path)
    record["note"] = f"{len(lines)} relevant metric lines"
    return record


def collect_log_tail(source_id, log_path):
    path = Path(log_path).expanduser()
    record = {
        "source_id": source_id,
        "source_type": "log_tail",
        "url": "",
        "path": str(path),
        "status": "missing",
        "ok": False,
        "operation_signal": True,
        "elapsed_ms": None,
        "bytes": 0,
        "result_path": "",
        "note": "",
    }
    started = time.perf_counter()
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()[-LOG_TAIL_LINES:]
        redacted = "\n".join(redact(line) for line in lines) + ("\n" if lines else "")
        result_path = OUT_DIR / f"{RUN_ID}-{source_id}.log"
        write_text(result_path, redacted)
        record.update(
            {
                "status": "ok",
                "ok": True,
                "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
                "bytes": len(redacted.encode("utf-8")),
                "result_path": str(result_path),
                "note": f"last {len(lines)} lines, redacted obvious secrets",
            }
        )
    except Exception as exc:
        record.update(
            {
                "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
                "note": f"{type(exc).__name__}: {exc}",
            }
        )
    return record


def collect_platform_snapshot():
    data = {
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
        "python": platform.python_version(),
        "processor": platform.processor(),
        "machine": platform.machine(),
        "cpu_count": os.cpu_count(),
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    path = OUT_DIR / f"{RUN_ID}-host-platform.json"
    write_json(path, data)
    return {
        "source_id": "host_platform",
        "source_type": "host_platform",
        "url": "",
        "status": "ok",
        "ok": True,
        "operation_signal": False,
        "elapsed_ms": 0,
        "bytes": path.stat().st_size,
        "result_path": str(path),
        "note": "host identity only; not enough for pass by itself",
        "parsed": data,
    }


def collect_nvidia_smi():
    exe = shutil.which("nvidia-smi")
    record = {
        "source_id": "nvidia_smi",
        "source_type": "resource_nvidia_smi",
        "url": "",
        "status": "unavailable",
        "ok": False,
        "operation_signal": True,
        "elapsed_ms": None,
        "bytes": 0,
        "result_path": "",
        "note": "nvidia-smi not found",
    }
    if not exe:
        return record
    command = [
        exe,
        "--query-gpu=timestamp,name,driver_version,utilization.gpu,utilization.memory,memory.total,memory.used,memory.free,power.draw,temperature.gpu",
        "--format=csv",
    ]
    started = time.perf_counter()
    try:
        completed = subprocess.run(command, capture_output=True, text=True, timeout=COMMAND_TIMEOUT_SECONDS, check=False)
        text = redact(completed.stdout + completed.stderr)
        result_path = OUT_DIR / f"{RUN_ID}-nvidia-smi.csv"
        write_text(result_path, text)
        record.update(
            {
                "status": f"exit {completed.returncode}",
                "ok": completed.returncode == 0,
                "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
                "bytes": len(text.encode("utf-8")),
                "result_path": str(result_path),
                "note": "GPU snapshot" if completed.returncode == 0 else text[:200].replace("\n", " "),
            }
        )
    except Exception as exc:
        record.update(
            {
                "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
                "note": f"{type(exc).__name__}: {exc}",
            }
        )
    return record


def openai_model_ids(parsed):
    ids = []
    if isinstance(parsed, dict):
        data = parsed.get("data")
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and item.get("id"):
                    ids.append(str(item["id"]))
    return ids


def ollama_model_ids(parsed):
    ids = []
    if isinstance(parsed, dict):
        models = parsed.get("models")
        if isinstance(models, list):
            for item in models:
                if isinstance(item, dict):
                    for key in ("name", "model", "id"):
                        if item.get(key):
                            ids.append(str(item[key]))
    return ids


def classify(sources, model_ids):
    route = next((item for item in sources if item["source_id"] == "openai_models"), None)
    route_ok = bool(route and route.get("ok"))
    operation_sources = [
        item for item in sources
        if item.get("operation_signal") and item.get("ok") and item.get("source_type") != "host_platform"
    ]
    expected_present = None
    if EXPECTED_MODEL:
        expected_present = EXPECTED_MODEL in model_ids
        if not expected_present:
            return {
                "status": "hold",
                "decision": "expected_model_missing",
                "reason": f"Expected model `{EXPECTED_MODEL}` was not visible in route or loaded-model snapshots.",
                "next_route": "Check model id, load state, runtime route, or first runtime health snapshot.",
                "route_ok": route_ok,
                "operation_source_count": len(operation_sources),
                "expected_model_present": False,
            }
    if route_ok and operation_sources:
        return {
            "status": "pass",
            "decision": "operational_snapshot_ready",
            "reason": "The model route is reachable and at least one operations signal was saved.",
            "next_route": "Use the specific runner for the next claim: API contract, benchmark, concurrency, cache, speculation, quality, lifecycle, or troubleshooting.",
            "route_ok": True,
            "operation_source_count": len(operation_sources),
            "expected_model_present": expected_present,
        }
    if route_ok:
        return {
            "status": "hold",
            "decision": "route_only_observability_gap",
            "reason": "The model route is reachable, but no metrics, slots, loaded-model, resource, or log operation signal succeeded.",
            "next_route": "Enable metrics/log capture or add the runtime-native state endpoint before accepting operations claims.",
            "route_ok": True,
            "operation_source_count": 0,
            "expected_model_present": expected_present,
        }
    if operation_sources:
        return {
            "status": "hold",
            "decision": "model_route_unreachable_ops_visible",
            "reason": "Operations sources responded, but the OpenAI-compatible model route did not.",
            "next_route": "Run the API contract runner or troubleshoot base URL, route, and model serving boundary.",
            "route_ok": False,
            "operation_source_count": len(operation_sources),
            "expected_model_present": expected_present,
        }
    return {
        "status": "error",
        "decision": "no_observable_service",
        "reason": "The model route failed and no operations source succeeded.",
        "next_route": "Return to runtime health snapshot, serving runbook, or troubleshooting decision tree.",
        "route_ok": False,
        "operation_source_count": 0,
        "expected_model_present": expected_present,
    }


def write_sources_csv(path, sources):
    fields = [
        "source_id",
        "source_type",
        "status",
        "ok",
        "operation_signal",
        "elapsed_ms",
        "bytes",
        "url",
        "path",
        "result_path",
        "note",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for source in sources:
            writer.writerow(source)


def write_markdown(path, result):
    decision = result["decision"]
    lines = [
        f"# Observability and Operations Runner - {RUN_ID}",
        "",
        "## Decision",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Status | `{decision['status']}` |",
        f"| Decision | `{decision['decision']}` |",
        f"| Reason | {md_cell(decision['reason'])} |",
        f"| Route OK | `{decision['route_ok']}` |",
        f"| Operation sources | `{decision['operation_source_count']}` |",
        f"| Expected model present | `{decision.get('expected_model_present')}` |",
        f"| Next route | {md_cell(decision['next_route'])} |",
        "",
        "## Model Visibility",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Expected model | `{EXPECTED_MODEL or ''}` |",
        f"| Visible model ids | {md_cell(result['model_ids'])} |",
        "",
        "## Sources",
        "",
        "| Source | Type | OK | Status | Operation signal | Result | Note |",
        "|---|---|---:|---|---:|---|---|",
    ]
    for source in result["sources"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    md_cell(source["source_id"]),
                    md_cell(source["source_type"]),
                    md_cell(source["ok"]),
                    md_cell(source["status"]),
                    md_cell(source["operation_signal"]),
                    md_cell(source.get("result_path", "")),
                    md_cell(source.get("note", "")),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Privacy",
            "",
            f"- Log paths tailed: `{len(result['log_paths'])}`",
            f"- Log tail lines per file: `{LOG_TAIL_LINES}`",
            "- Log tails are redacted for obvious bearer tokens, API keys, tokens, and passwords, but raw service logs can still contain private prompt text.",
            "- Keep this evidence local unless you intentionally scrub and export it.",
            "",
            "## Output Files",
            "",
            f"- Results JSON: `{result['results_json']}`",
            f"- Sources CSV: `{result['sources_csv']}`",
            f"- Sources JSONL: `{result['sources_jsonl']}`",
            f"- Runs JSONL: `{result['runs_jsonl']}`",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


BASE_URL = os.environ.get("LOCAL_LLM_BASE_URL", "").strip()
API_KEY = os.environ.get("LOCAL_LLM_API_KEY", "").strip()
EXPECTED_MODEL = os.environ.get("LOCAL_LLM_EXPECTED_MODEL", "").strip()
OLLAMA_API_URL = os.environ.get("LOCAL_LLM_OLLAMA_API_URL", "").strip()
METRICS_URLS = split_urls(os.environ.get("LOCAL_LLM_METRICS_URLS", ""))
SLOTS_URLS = split_urls(os.environ.get("LOCAL_LLM_SLOTS_URLS", ""))
LOG_PATHS = split_log_paths(os.environ.get("LOCAL_LLM_LOG_PATHS", ""))
LOG_TAIL_LINES = max(1, as_int(os.environ.get("LOCAL_LLM_LOG_TAIL_LINES"), 80))
TIMEOUT_SECONDS = max(1, as_int(os.environ.get("LOCAL_LLM_TIMEOUT_SECONDS"), 10))
COMMAND_TIMEOUT_SECONDS = max(1, as_int(os.environ.get("LOCAL_LLM_COMMAND_TIMEOUT_SECONDS"), 10))
ENABLE_RESOURCE_COMMANDS = env_bool("LOCAL_LLM_RESOURCE_COMMANDS", True)
RUN_ROOT = Path(os.environ.get("LOCAL_LLM_RUN_ROOT", ".")).expanduser().resolve()
RUN_ID = time.strftime("%Y%m%d-%H%M%S-operations")
OUT_DIR = RUN_ROOT / "observability-operations-runner"

OUT_DIR.mkdir(parents=True, exist_ok=True)

if not BASE_URL:
    sample = {
        "LOCAL_LLM_RUN_ROOT": str(RUN_ROOT),
        "LOCAL_LLM_BASE_URL": "http://127.0.0.1:11434/v1",
        "LOCAL_LLM_EXPECTED_MODEL": "your-local-model-id",
        "LOCAL_LLM_OLLAMA_API_URL": "http://127.0.0.1:11434/api",
        "LOCAL_LLM_METRICS_URLS": "http://127.0.0.1:8000/metrics",
        "LOCAL_LLM_SLOTS_URLS": "http://127.0.0.1:8080/slots",
        "LOCAL_LLM_LOG_PATHS": "C:\\path\\to\\server.log;C:\\path\\to\\another.log",
        "LOCAL_LLM_RESOURCE_COMMANDS": "1",
    }
    template = OUT_DIR / "observability-operations-runner-env-template.json"
    write_json(template, sample)
    print(json.dumps({"status": "error", "decision": "missing_base_url", "template": str(template)}, indent=2))
    raise SystemExit(0)

sources = []
sources.append(collect_platform_snapshot())
sources.append(fetch_source("openai_models", "openai_models", join_url(BASE_URL, "/models"), expect_json=True, operation_signal=False))

if OLLAMA_API_URL:
    sources.append(fetch_source("ollama_ps", "ollama_ps", join_url(OLLAMA_API_URL, "/ps"), expect_json=True, operation_signal=True))

for index, url in enumerate(METRICS_URLS, start=1):
    sources.append(summarize_metrics(fetch_source(f"metrics_{index}", "metrics", url, expect_json=False, operation_signal=True)))

for index, url in enumerate(SLOTS_URLS, start=1):
    sources.append(fetch_source(f"slots_{index}", "slots", url, expect_json=True, operation_signal=True))

for index, path in enumerate(LOG_PATHS, start=1):
    sources.append(collect_log_tail(f"log_tail_{index}", path))

if ENABLE_RESOURCE_COMMANDS:
    sources.append(collect_nvidia_smi())

model_ids = []
for source in sources:
    if source["source_type"] == "openai_models":
        model_ids.extend(openai_model_ids(source.get("parsed")))
    if source["source_type"] == "ollama_ps":
        model_ids.extend(ollama_model_ids(source.get("parsed")))
model_ids = sorted(set(model_ids))

sources_csv = OUT_DIR / f"{RUN_ID}-operations-sources.csv"
sources_jsonl = OUT_DIR / f"{RUN_ID}-operations-sources.jsonl"
runs_jsonl = OUT_DIR / "observability-operations-runs.jsonl"
results_json = OUT_DIR / f"{RUN_ID}-operations-results.json"
results_md = OUT_DIR / f"{RUN_ID}-operations-results.md"

for source in sources:
    compact = dict(source)
    compact.pop("parsed", None)
    compact.pop("text", None)
    append_jsonl(sources_jsonl, compact)

decision = classify(sources, model_ids)
result = {
    "run_id": RUN_ID,
    "created_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
    "base_url": BASE_URL,
    "expected_model": EXPECTED_MODEL,
    "model_ids": model_ids,
    "metrics_urls": METRICS_URLS,
    "slots_urls": SLOTS_URLS,
    "log_paths": LOG_PATHS,
    "resource_commands_enabled": ENABLE_RESOURCE_COMMANDS,
    "decision": decision,
    "sources": [{key: value for key, value in source.items() if key not in {"parsed", "text"}} for source in sources],
    "results_json": str(results_json),
    "results_md": str(results_md),
    "sources_csv": str(sources_csv),
    "sources_jsonl": str(sources_jsonl),
    "runs_jsonl": str(runs_jsonl),
    "external_docs_checked": [
        "https://docs.ollama.com/api/introduction",
        "https://docs.ollama.com/api/ps",
        "https://docs.ollama.com/api/usage",
        "https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md",
        "https://docs.vllm.ai/en/stable/design/metrics/",
        "https://docs.sglang.ai/references/production_metrics.html",
        "https://sgl-project.github.io/advanced_features/observability.html",
    ],
}

write_sources_csv(sources_csv, result["sources"])
write_json(results_json, result)
write_markdown(results_md, result)
append_jsonl(
    runs_jsonl,
    {
        "run_id": RUN_ID,
        "status": decision["status"],
        "decision": decision["decision"],
        "results_json": str(results_json),
        "results_md": str(results_md),
        "sources_csv": str(sources_csv),
    },
)

print(
    json.dumps(
        {
            "status": decision["status"],
            "decision": decision["decision"],
            "run_id": RUN_ID,
            "results_json": str(results_json),
            "results_md": str(results_md),
            "sources_csv": str(sources_csv),
            "sources_jsonl": str(sources_jsonl),
            "runs_jsonl": str(runs_jsonl),
        },
        indent=2,
    )
)
```

## Runtime Knobs

| Variable | Required | Meaning |
|---|---:|---|
| `LOCAL_LLM_RUN_ROOT` | no | Evidence root. Defaults to the current directory. |
| `LOCAL_LLM_BASE_URL` | yes | OpenAI-compatible base URL, such as `http://127.0.0.1:11434/v1`. |
| `LOCAL_LLM_EXPECTED_MODEL` | no | Model id that should appear in `/v1/models` or loaded-model state. |
| `LOCAL_LLM_API_KEY` | no | Local placeholder or proxy token for the OpenAI-compatible route. |
| `LOCAL_LLM_OLLAMA_API_URL` | no | Ollama native API base, such as `http://127.0.0.1:11434/api`; captures `/ps`. |
| `LOCAL_LLM_METRICS_URLS` | no | Comma- or semicolon-separated metrics endpoints for vLLM, SGLang, llama.cpp, or a proxy. |
| `LOCAL_LLM_SLOTS_URLS` | no | Comma- or semicolon-separated slots endpoints, usually llama.cpp `/slots`. |
| `LOCAL_LLM_LOG_PATHS` | no | Semicolon-separated local log files to tail and redact. |
| `LOCAL_LLM_LOG_TAIL_LINES` | no | Lines to keep from each log. Defaults to `80`. |
| `LOCAL_LLM_RESOURCE_COMMANDS` | no | Set `0` to skip local resource commands. Defaults to `1`. |
| `LOCAL_LLM_TIMEOUT_SECONDS` | no | HTTP timeout. Defaults to `10`. |
| `LOCAL_LLM_COMMAND_TIMEOUT_SECONDS` | no | Local command timeout. Defaults to `10`. |

## PowerShell Run

```powershell
$RunRoot = Join-Path $HOME ("Documents\local-llm-runs\" + (Get-Date -Format "yyyy-MM-dd-HHmm") + "-ops")
New-Item -ItemType Directory -Force -Path $RunRoot | Out-Null

$env:LOCAL_LLM_RUN_ROOT = $RunRoot
$env:LOCAL_LLM_BASE_URL = "http://127.0.0.1:11434/v1"
$env:LOCAL_LLM_EXPECTED_MODEL = "qwen3"
$env:LOCAL_LLM_OLLAMA_API_URL = "http://127.0.0.1:11434/api"
$env:LOCAL_LLM_METRICS_URLS = ""
$env:LOCAL_LLM_SLOTS_URLS = ""
$env:LOCAL_LLM_RESOURCE_COMMANDS = "1"
python .\observability-operations-runner.py
```

For vLLM or SGLang:

```powershell
$env:LOCAL_LLM_BASE_URL = "http://127.0.0.1:8000/v1"
$env:LOCAL_LLM_EXPECTED_MODEL = "served-model-id"
$env:LOCAL_LLM_METRICS_URLS = "http://127.0.0.1:8000/metrics"
python .\observability-operations-runner.py
```

For llama.cpp:

```powershell
$env:LOCAL_LLM_BASE_URL = "http://127.0.0.1:8080/v1"
$env:LOCAL_LLM_EXPECTED_MODEL = "local-model-id"
$env:LOCAL_LLM_METRICS_URLS = "http://127.0.0.1:8080/metrics"
$env:LOCAL_LLM_SLOTS_URLS = "http://127.0.0.1:8080/slots"
python .\observability-operations-runner.py
```

## Fixture Verification

Use this fake loopback server to verify the runner without contacting a real model endpoint.

```python
import json
import os
import subprocess
import sys
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class FixtureHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return

    def send_json(self, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_text(self, payload):
        body = payload.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/v1/models":
            self.send_json({"object": "list", "data": [{"id": "fixture-model", "object": "model"}]})
            return
        if self.path == "/api/ps":
            self.send_json({"models": [{"name": "fixture-model", "model": "fixture-model", "size_vram": 123456789}]})
            return
        if self.path == "/metrics":
            self.send_text(
                "\n".join(
                    [
                        "vllm:num_requests_running 1",
                        "vllm:num_requests_waiting 0",
                        "vllm:gpu_cache_usage_perc 0.42",
                        "sglang:num_running_reqs 1",
                        "llamacpp:tokens_predicted_total 42",
                    ]
                )
                + "\n"
            )
            return
        if self.path == "/slots":
            self.send_json([{"id": 0, "is_processing": False, "n_ctx": 4096}])
            return
        self.send_response(404)
        self.end_headers()


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: python fixture-test.py observability-operations-runner.py")
    runner = Path(sys.argv[1]).resolve()
    if not runner.exists():
        raise SystemExit(f"runner not found: {runner}")

    server = ThreadingHTTPServer(("127.0.0.1", 0), FixtureHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_address[1]}"

    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        log_path = root / "fixture-server.log"
        log_path.write_text("INFO loaded fixture-model\nAuthorization: Bearer secret-token\n", encoding="utf-8")
        env = os.environ.copy()
        env.update(
            {
                "LOCAL_LLM_RUN_ROOT": str(root),
                "LOCAL_LLM_BASE_URL": f"{base}/v1",
                "LOCAL_LLM_EXPECTED_MODEL": "fixture-model",
                "LOCAL_LLM_OLLAMA_API_URL": f"{base}/api",
                "LOCAL_LLM_METRICS_URLS": f"{base}/metrics",
                "LOCAL_LLM_SLOTS_URLS": f"{base}/slots",
                "LOCAL_LLM_LOG_PATHS": str(log_path),
                "LOCAL_LLM_RESOURCE_COMMANDS": "0",
                "LOCAL_LLM_TIMEOUT_SECONDS": "5",
            }
        )
        completed = subprocess.run([sys.executable, str(runner)], text=True, capture_output=True, env=env, check=True)
        summary = json.loads(completed.stdout)
        results = json.loads(Path(summary["results_json"]).read_text(encoding="utf-8"))
        assert summary["status"] == "pass", summary
        assert summary["decision"] == "operational_snapshot_ready", summary
        assert "fixture-model" in results["model_ids"], results["model_ids"]
        assert any(source["source_type"] == "metrics" and source["ok"] for source in results["sources"])
        assert any(source["source_type"] == "slots" and source["ok"] for source in results["sources"])
        assert any(source["source_type"] == "ollama_ps" and source["ok"] for source in results["sources"])
        assert Path(summary["sources_csv"]).exists()
        assert Path(summary["sources_jsonl"]).exists()
        assert Path(summary["results_md"]).exists()
    server.shutdown()
    print("fixture pass")


if __name__ == "__main__":
    main()
```

## Status Interpretation

| Status | Decision | Meaning | Next route |
|---|---|---|---|
| `pass` | `operational_snapshot_ready` | `/v1/models` is reachable and at least one operations signal was saved. | Use the specific runner for the next claim. |
| `hold` | `expected_model_missing` | The expected model id was not visible in route or loaded-model state. | Check model id, load state, or runtime route. |
| `hold` | `route_only_observability_gap` | Route works, but metrics, slots, logs, loaded-model state, or resource evidence is missing. | Enable metrics/logs or add native runtime state before accepting ops claims. |
| `hold` | `model_route_unreachable_ops_visible` | Metrics/logs/state responded, but `/v1/models` did not. | Run the API contract runner or route troubleshooting. |
| `error` | `no_observable_service` | Route and all operation sources failed. | Return to runtime health snapshot, serving runbook, or troubleshooting tree. |

## Completion Gate

The runner output is usable when:

- [ ] `/v1/models` succeeded or the route failure has a named owner.
- [ ] expected model visibility is pass or explicitly marked missing.
- [ ] at least one runtime-native signal is saved: Ollama `/api/ps`, metrics, slots, local GPU snapshot, or redacted log tail.
- [ ] raw metrics or slots are saved with source URL and timestamped output path.
- [ ] log tails are either omitted intentionally or stored locally with obvious secrets redacted.
- [ ] the next route says API contract, benchmark, concurrency, cache, speculation, quality, lifecycle, troubleshooting, or deployment decision.

## External Docs Checked

- [Ollama API introduction](https://docs.ollama.com/api/introduction)
- [Ollama list running models](https://docs.ollama.com/api/ps)
- [Ollama usage metrics fields](https://docs.ollama.com/api/usage)
- [llama.cpp server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- [vLLM metrics](https://docs.vllm.ai/en/stable/design/metrics/)
- [SGLang production metrics](https://docs.sglang.ai/references/production_metrics.html)
- [SGLang observability](https://sgl-project.github.io/advanced_features/observability.html)

## References

- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM First Runtime Health Snapshot]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner]]
- [[LLM/Study/Local LLM Speculative Decoding Runner]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
