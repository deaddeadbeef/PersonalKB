---
tags: [study, llm, inference, local-llm, kv-cache, prompt-cache, prefix-caching, latency, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-15
---

# Local LLM Prompt Cache and KV Reuse Runner

> **One-line summary** Run a repeated-prefix A/B probe against a local OpenAI-compatible endpoint and save the timing, cache-signal, control, and decision evidence needed before claiming prompt-cache or KV-reuse benefit.

Use this after [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Local LLM Prompt Cache and KV Reuse Lab]] explains the manual experiment and after [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner|Local LLM OpenAI-Compatible API Contract Runner]] proves the route. Use it before claiming that repeated system prompts, few-shot examples, long documents, RAG context, tool protocols, or chat history reduce prefill, TTFT, or repeated-request latency.

This runner sends real local HTTP requests when pointed at an actual endpoint. For verification or dry runs, point `LOCAL_LLM_BASE_URL` at a fake loopback fixture server. Default prompts are synthetic and prompt text is not saved unless `LOCAL_LLM_SAVE_PROMPTS=1`.

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| Shared-prefix A1/A2/A3 rows | Later requests with identical leading tokens can be compared to the first request. | That the runtime exposed a direct cache-hit counter. |
| Changed-prefix and unique-first controls | A speedup is not just a warm loaded model or shorter prompt. | Exact token identity unless tokenizer evidence is also saved. |
| Streaming TTFT or prompt-eval timing | The prefill-facing part of latency changed. | Long-output throughput, unless output cap is also held fixed. |
| Optional `/metrics` snapshot | vLLM/SGLang/llama.cpp cache counters can support the timing result. | That every runtime exposes comparable metric names. |
| JSON/CSV/Markdown/JSONL output | The cache decision can feed the benchmark log, deployment matrix, and capstone workbook. | Production reliability across restarts, concurrency, eviction, or private workloads. |

Academic bridge: prompt caching extends the ordinary per-request KV cache across requests. It helps when many requests share the same token prefix, because the server can reuse already-computed attention states for the prefix and only prefill the changed suffix. It is not response caching, semantic caching, or fine-tuning. It should not change the intended answer; it should change prefill work and first-token latency.

## Fixed Conditions

Write these before running:

| Field | Value |
|---|---|
| Run folder |  |
| API contract runner result |  |
| Context budget runner result |  |
| Runtime | Ollama / LM Studio / llama.cpp / vLLM / SGLang / other |
| Base URL | `http://127.0.0.1:11434/v1` or another OpenAI-compatible local route |
| Model id |  |
| Streaming TTFT | on / off |
| Metrics URL | optional, such as `http://127.0.0.1:8000/metrics` |
| Shared prefix source | system / examples / document / history / RAG / tool protocol |
| Output cap |  |
| Sampler settings | temperature `0`, fixed output cap |
| Cache feature flag | enabled / disabled / unknown |
| Cache privacy boundary | local only / shared service / multi-tenant / unknown |
| Next gate | benchmark log / deployment matrix / scheduler lab / troubleshooting |

If the endpoint is exposed beyond loopback, complete [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] before running the probe.

## Standard-Library Runner

Save this as `prompt-cache-kv-reuse-runner.py` inside the run folder. It uses only Python's standard library.

```python
import csv
import hashlib
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


def join_url(base_url, route):
    return f"{base_url.rstrip('/')}/{route.lstrip('/')}"


def digest_text(value):
    return hashlib.sha256(str(value or "").encode("utf-8")).hexdigest()[:16]


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


def first_choice(data):
    if not isinstance(data, dict):
        return {}
    choices = data.get("choices") if isinstance(data.get("choices"), list) else []
    return choices[0] if choices and isinstance(choices[0], dict) else {}


def extract_content_text(data):
    choice = first_choice(data)
    message = choice.get("message") if isinstance(choice.get("message"), dict) else {}
    return content_to_text(message.get("content"))


def extract_stream_content(data):
    choice = first_choice(data)
    delta = choice.get("delta") if isinstance(choice.get("delta"), dict) else {}
    message = choice.get("message") if isinstance(choice.get("message"), dict) else {}
    return content_to_text(delta.get("content") or message.get("content"))


def extract_finish_reason(data):
    return str(first_choice(data).get("finish_reason") or "")


def usage_counts(data):
    usage = data.get("usage") if isinstance(data, dict) and isinstance(data.get("usage"), dict) else {}
    return {
        "prompt_tokens": usage.get("prompt_tokens"),
        "completion_tokens": usage.get("completion_tokens"),
        "total_tokens": usage.get("total_tokens"),
    }


def ns_to_ms(value):
    try:
        return round(float(value) / 1_000_000, 3)
    except (TypeError, ValueError):
        return None


def response_timing_fields(data):
    if not isinstance(data, dict):
        return {}
    return {
        "load_duration_ms": ns_to_ms(data.get("load_duration")),
        "prompt_eval_duration_ms": ns_to_ms(data.get("prompt_eval_duration")),
        "eval_duration_ms": ns_to_ms(data.get("eval_duration")),
        "total_duration_ms": ns_to_ms(data.get("total_duration")),
        "prompt_eval_count": data.get("prompt_eval_count"),
        "eval_count": data.get("eval_count"),
    }


def parse_sse_line(raw_line):
    line = raw_line.decode("utf-8", errors="replace").strip()
    if not line or line.startswith(":"):
        return None
    if not line.startswith("data:"):
        return None
    payload = line[5:].strip()
    if payload == "[DONE]":
        return "[DONE]"
    try:
        return json.loads(payload)
    except json.JSONDecodeError:
        return {"_malformed_sse": payload}


def make_headers():
    headers = {"Content-Type": "application/json"}
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"
    return headers


def make_body(prompt):
    return {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0,
        "stream": STREAM,
        "max_tokens": MAX_TOKENS,
    }


def load_manifest(path):
    if not path:
        return None
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("manifest must be a JSON object")
    return data


def default_manifest():
    shared_paragraph = (
        "CACHE_PROBE_SHARED_PREFIX_V1. This synthetic document explains that prefill computes "
        "key and value states for the prompt before decoding begins. Prompt caching can reuse "
        "those states when a later request starts with the same rendered tokens. The shared "
        "section intentionally stays first so the changed question appears only after the stable "
        "prefix. The document mentions local inference, KV cache pressure, time to first token, "
        "and repeated RAG context. "
    )
    changed_paragraph = (
        "CACHE_PROBE_CHANGED_PREFIX_V1. This synthetic control discusses local model serving with "
        "a different opening sequence and different token order. It is similar in length, but it "
        "should not match the shared-prefix cache entry. The control mentions local inference, KV "
        "cache pressure, time to first token, and repeated RAG context in a changed arrangement. "
    )
    shared_prefix = "\n".join([shared_paragraph for _ in range(8)])
    changed_prefix = "\n".join([changed_paragraph for _ in range(8)])
    return {
        "system": "You are a concise local benchmark assistant. Answer in one short sentence.",
        "shared_prefix": shared_prefix,
        "changed_prefix": changed_prefix,
        "suffixes": [
            "Question A: name the phase prompt caching is meant to reduce.",
            "Question B: name the measurement that best captures first-token responsiveness.",
            "Question C: name the control that separates warm-model behavior from prefix reuse.",
        ],
    }


def build_cases(manifest):
    shared = str(manifest.get("shared_prefix") or "").strip()
    changed = str(manifest.get("changed_prefix") or "").strip()
    suffixes = manifest.get("suffixes") if isinstance(manifest.get("suffixes"), list) else []
    suffixes = [str(item).strip() for item in suffixes if str(item).strip()]
    if not shared or not changed or len(suffixes) < 3:
        raise ValueError("manifest requires shared_prefix, changed_prefix, and at least three suffixes")

    return [
        {
            "case_id": "warm_short",
            "phase": "warm_model",
            "prefix_id": "short",
            "expected_cache": "none",
            "prompt": "Warmup only: answer with the words prompt cache probe.",
        },
        {
            "case_id": "shared_a1",
            "phase": "shared_prefix",
            "prefix_id": "shared-v1",
            "expected_cache": "cold_or_miss",
            "prompt": f"{shared}\n\n{suffixes[0]}",
        },
        {
            "case_id": "shared_a2",
            "phase": "shared_prefix",
            "prefix_id": "shared-v1",
            "expected_cache": "expected_hit",
            "prompt": f"{shared}\n\n{suffixes[1]}",
        },
        {
            "case_id": "shared_a3",
            "phase": "shared_prefix",
            "prefix_id": "shared-v1",
            "expected_cache": "expected_hit",
            "prompt": f"{shared}\n\n{suffixes[2]}",
        },
        {
            "case_id": "changed_b1",
            "phase": "changed_prefix_control",
            "prefix_id": "changed-v1",
            "expected_cache": "expected_miss",
            "prompt": f"{changed}\n\n{suffixes[1]}",
        },
        {
            "case_id": "unique_first_u1",
            "phase": "unique_first_control",
            "prefix_id": "shared-v1-late",
            "expected_cache": "expected_miss",
            "prompt": f"{suffixes[1]}\n\n{shared}",
        },
    ]


def fetch_metrics(label):
    if not METRICS_URL:
        return {"label": label, "enabled": False}
    request = urllib.request.Request(METRICS_URL, method="GET")
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            text = response.read().decode("utf-8", errors="replace")
        elapsed_ms = round((time.perf_counter() - started) * 1000, 3)
        keywords = ("prefix", "cache", "kv", "prompt")
        relevant = [line for line in text.splitlines() if any(word in line.lower() for word in keywords)]
        return {
            "label": label,
            "enabled": True,
            "status": "ok",
            "elapsed_ms": elapsed_ms,
            "bytes": len(text.encode("utf-8")),
            "relevant_line_count": len(relevant),
            "relevant_lines": relevant[:60],
        }
    except Exception as exc:
        return {
            "label": label,
            "enabled": True,
            "status": "error",
            "error": f"{type(exc).__name__}: {exc}",
        }


def run_case(case):
    body = make_body(case["prompt"])
    request_path = OUT_DIR / f"{RUN_ID}-{case['case_id']}-request.json"
    response_path = OUT_DIR / f"{RUN_ID}-{case['case_id']}-response.json"
    output_path = OUT_DIR / f"{RUN_ID}-{case['case_id']}-output.txt"

    request_record = {
        "case_id": case["case_id"],
        "phase": case["phase"],
        "prefix_id": case["prefix_id"],
        "expected_cache": case["expected_cache"],
        "model": MODEL,
        "stream": STREAM,
        "max_tokens": MAX_TOKENS,
        "prompt_chars": len(case["prompt"]),
        "prompt_digest": digest_text(case["prompt"]),
    }
    if SAVE_PROMPTS:
        request_record["prompt"] = case["prompt"]
        request_record["body"] = body
    write_json(request_path, request_record)

    payload = json.dumps(body).encode("utf-8")
    request = urllib.request.Request(CHAT_URL, data=payload, headers=make_headers(), method="POST")
    started = time.perf_counter()
    first_event_ms = None
    first_content_ms = None
    finish_reason = ""
    content_parts = []
    final_data = {}
    status = "ok"
    error = ""

    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            if STREAM:
                for raw_line in response:
                    event = parse_sse_line(raw_line)
                    if event is None:
                        continue
                    now_ms = round((time.perf_counter() - started) * 1000, 3)
                    if first_event_ms is None:
                        first_event_ms = now_ms
                    if event == "[DONE]":
                        break
                    if event.get("_malformed_sse"):
                        status = "error"
                        error = f"malformed SSE: {event['_malformed_sse'][:120]}"
                        continue
                    final_data = event
                    delta_text = extract_stream_content(event)
                    if delta_text:
                        if first_content_ms is None:
                            first_content_ms = now_ms
                        content_parts.append(delta_text)
                    finish_reason = extract_finish_reason(event) or finish_reason
            else:
                final_data = json.loads(response.read().decode("utf-8"))
                content_parts.append(extract_content_text(final_data))
                finish_reason = extract_finish_reason(final_data)
    except urllib.error.HTTPError as exc:
        status = "error"
        error_body = exc.read().decode("utf-8", errors="replace")
        error = f"HTTP {exc.code}: {error_body[:500]}"
    except Exception as exc:
        status = "error"
        error = f"{type(exc).__name__}: {exc}"

    total_latency_ms = round((time.perf_counter() - started) * 1000, 3)
    text = "".join(content_parts)
    timing = response_timing_fields(final_data)
    usage = usage_counts(final_data)
    output_path.write_text(text + "\n", encoding="utf-8")
    response_payload = final_data if final_data else {"status": status, "error": error}
    write_json(response_path, response_payload)

    return {
        "case_id": case["case_id"],
        "phase": case["phase"],
        "prefix_id": case["prefix_id"],
        "expected_cache": case["expected_cache"],
        "status": status,
        "error": error,
        "prompt_chars": len(case["prompt"]),
        "prompt_digest": digest_text(case["prompt"]),
        "total_latency_ms": total_latency_ms,
        "first_event_ms": first_event_ms,
        "ttft_ms": first_content_ms,
        "finish_reason": finish_reason,
        "prompt_tokens": usage["prompt_tokens"],
        "completion_tokens": usage["completion_tokens"],
        "total_tokens": usage["total_tokens"],
        "output_chars": len(text),
        "output_digest": digest_text(text),
        "output_preview": text[:120].replace("\n", " "),
        "load_duration_ms": timing.get("load_duration_ms"),
        "prompt_eval_duration_ms": timing.get("prompt_eval_duration_ms"),
        "eval_duration_ms": timing.get("eval_duration_ms"),
        "response_total_duration_ms": timing.get("total_duration_ms"),
        "prompt_eval_count": timing.get("prompt_eval_count"),
        "eval_count": timing.get("eval_count"),
        "request_path": str(request_path),
        "response_path": str(response_path),
        "output_path": str(output_path),
    }


def mean(values):
    values = [float(value) for value in values if value is not None]
    if not values:
        return None
    return round(sum(values) / len(values), 3)


def pick_metric(rows):
    if any(row.get("ttft_ms") is not None for row in rows):
        return "ttft_ms", "direct"
    if any(row.get("prompt_eval_duration_ms") is not None for row in rows):
        return "prompt_eval_duration_ms", "direct"
    return "total_latency_ms", "indirect"


def classify(rows):
    ok_rows = [row for row in rows if row["status"] == "ok"]
    error_rows = [row for row in rows if row["status"] != "ok"]
    metric_name, evidence_strength = pick_metric(ok_rows)

    by_case = {row["case_id"]: row for row in ok_rows}
    shared_first = by_case.get("shared_a1", {}).get(metric_name)
    shared_hits = [
        row.get(metric_name)
        for row in ok_rows
        if row["case_id"] in {"shared_a2", "shared_a3"}
    ]
    controls = [
        row.get(metric_name)
        for row in ok_rows
        if row["case_id"] in {"changed_b1", "unique_first_u1"}
    ]
    hit_mean = mean(shared_hits)
    control_mean = mean(controls)
    first_ratio = round(hit_mean / shared_first, 3) if hit_mean and shared_first else None
    control_ratio = round(hit_mean / control_mean, 3) if hit_mean and control_mean else None

    if error_rows:
        decision = "error"
        status = "error"
        next_route = "OpenAI-compatible API contract runner or troubleshooting decision tree"
        reason = "At least one request failed."
    elif evidence_strength != "direct":
        decision = "inconclusive"
        status = "hold"
        next_route = "Enable streaming TTFT or collect runtime prompt/prefix-cache metrics."
        reason = "Only total latency is available; total latency can hide prefill and decode effects."
    elif hit_mean is None or control_mean is None or shared_first is None:
        decision = "inconclusive"
        status = "hold"
        next_route = "Re-run with all shared-prefix and changed-prefix control rows."
        reason = "Required comparison rows are missing."
    elif hit_mean + MIN_METRIC_DELTA_MS < control_mean and control_ratio is not None and control_ratio <= MIN_METRIC_RATIO:
        decision = "cache_likely"
        status = "pass"
        next_route = "Record cache decision in benchmark log and deployment matrix."
        reason = "Expected-hit rows are faster than changed-prefix controls on a prefill-facing metric."
    elif hit_mean + MIN_METRIC_DELTA_MS < shared_first and first_ratio is not None and first_ratio <= MIN_METRIC_RATIO:
        decision = "warm_or_cache_signal"
        status = "hold"
        next_route = "Add changed-prefix metrics or runtime cache counters before claiming prompt-cache benefit."
        reason = "Expected-hit rows beat the first shared-prefix row, but controls do not prove the cause."
    else:
        decision = "cache_not_proven"
        status = "pass"
        next_route = "Treat prompt caching as unproven for this runtime/workload; inspect flags, prompt layout, and metrics."
        reason = "The expected-hit rows did not beat changed-prefix controls enough to support a cache benefit."

    return {
        "status": status,
        "decision": decision,
        "reason": reason,
        "metric_name": metric_name,
        "evidence_strength": evidence_strength,
        "shared_first": shared_first,
        "shared_hit_mean": hit_mean,
        "control_mean": control_mean,
        "hit_vs_first_ratio": first_ratio,
        "hit_vs_control_ratio": control_ratio,
        "threshold_delta_ms": MIN_METRIC_DELTA_MS,
        "threshold_ratio": MIN_METRIC_RATIO,
        "next_route": next_route,
        "errors": [row for row in rows if row["status"] != "ok"],
    }


def write_csv(path, rows):
    fields = [
        "case_id",
        "phase",
        "prefix_id",
        "expected_cache",
        "status",
        "total_latency_ms",
        "ttft_ms",
        "prompt_eval_duration_ms",
        "prompt_tokens",
        "completion_tokens",
        "finish_reason",
        "prompt_chars",
        "prompt_digest",
        "output_digest",
        "error",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def write_markdown(path, result):
    decision = result["decision"]
    rows = result["requests"]
    lines = [
        f"# Prompt Cache and KV Reuse Runner - {RUN_ID}",
        "",
        "## Decision",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Status | `{decision['status']}` |",
        f"| Decision | `{decision['decision']}` |",
        f"| Reason | {md_cell(decision['reason'])} |",
        f"| Metric | `{decision['metric_name']}` ({decision['evidence_strength']}) |",
        f"| Shared hit mean | {md_cell(decision['shared_hit_mean'])} |",
        f"| Control mean | {md_cell(decision['control_mean'])} |",
        f"| Hit/control ratio | {md_cell(decision['hit_vs_control_ratio'])} |",
        f"| Next route | {md_cell(decision['next_route'])} |",
        "",
        "## Request Rows",
        "",
        "| Case | Expected | Status | Total ms | TTFT ms | Prompt eval ms | Prompt tokens | Output tokens | Error |",
        "|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    md_cell(row["case_id"]),
                    md_cell(row["expected_cache"]),
                    md_cell(row["status"]),
                    md_cell(row["total_latency_ms"]),
                    md_cell(row["ttft_ms"]),
                    md_cell(row["prompt_eval_duration_ms"]),
                    md_cell(row["prompt_tokens"]),
                    md_cell(row["completion_tokens"]),
                    md_cell(row["error"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Metrics",
            "",
            f"- Before metrics: `{result['metrics_before'].get('status', 'disabled')}`",
            f"- After metrics: `{result['metrics_after'].get('status', 'disabled')}`",
            "",
            "## Privacy",
            "",
            f"- Prompt text saved: `{SAVE_PROMPTS}`",
            "- Prompt hashes and character counts are saved by default.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


BASE_URL = os.environ.get("LOCAL_LLM_BASE_URL", "").strip()
MODEL = os.environ.get("LOCAL_LLM_MODEL", "").strip()
API_KEY = os.environ.get("LOCAL_LLM_API_KEY", "").strip()
RUN_ROOT = Path(os.environ.get("LOCAL_LLM_RUN_ROOT", ".")).expanduser().resolve()
MAX_TOKENS = as_int(os.environ.get("LOCAL_LLM_MAX_TOKENS"), 64)
STREAM = env_bool("LOCAL_LLM_STREAM", True)
SAVE_PROMPTS = env_bool("LOCAL_LLM_SAVE_PROMPTS", False)
TIMEOUT_SECONDS = as_int(os.environ.get("LOCAL_LLM_TIMEOUT_SECONDS"), 90)
MANIFEST_PATH = os.environ.get("LOCAL_LLM_PROMPT_CACHE_MANIFEST", "").strip()
METRICS_URL = os.environ.get("LOCAL_LLM_METRICS_URL", "").strip()
MIN_METRIC_DELTA_MS = as_float(os.environ.get("LOCAL_LLM_MIN_METRIC_DELTA_MS"), 25.0)
MIN_METRIC_RATIO = as_float(os.environ.get("LOCAL_LLM_MIN_METRIC_RATIO"), 0.85)
RUN_ID = time.strftime("%Y%m%d-%H%M%S-prompt-cache")
OUT_DIR = RUN_ROOT / "prompt-cache-kv-reuse-runner"
CHAT_URL = join_url(BASE_URL, "/chat/completions") if BASE_URL else ""

summary = {
    "run_id": RUN_ID,
    "status": "error",
    "base_url": BASE_URL,
    "model": MODEL,
    "stream": STREAM,
    "metrics_enabled": bool(METRICS_URL),
    "prompt_text_saved": SAVE_PROMPTS,
}

if not BASE_URL or not MODEL:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    sample = {
        "LOCAL_LLM_BASE_URL": "http://127.0.0.1:11434/v1",
        "LOCAL_LLM_MODEL": "your-local-model-id",
        "LOCAL_LLM_STREAM": "1",
        "LOCAL_LLM_MAX_TOKENS": "64",
        "LOCAL_LLM_METRICS_URL": "optional http://127.0.0.1:8000/metrics",
        "LOCAL_LLM_PROMPT_CACHE_MANIFEST": "optional path to manifest JSON",
        "LOCAL_LLM_SAVE_PROMPTS": "0",
    }
    write_json(OUT_DIR / "prompt-cache-kv-reuse-runner-env-template.json", sample)
    summary["missing"] = [name for name, value in {"LOCAL_LLM_BASE_URL": BASE_URL, "LOCAL_LLM_MODEL": MODEL}.items() if not value]
    print(json.dumps({"status": "error", "template": str(OUT_DIR / "prompt-cache-kv-reuse-runner-env-template.json")}, indent=2))
    raise SystemExit(0)

manifest = load_manifest(MANIFEST_PATH) if MANIFEST_PATH else default_manifest()
SYSTEM_PROMPT = str(manifest.get("system") or "You are a concise local benchmark assistant.")
cases = build_cases(manifest)
metrics_before = fetch_metrics("before")
rows = []

for case in cases:
    row = run_case(case)
    rows.append(row)
    append_jsonl(OUT_DIR / f"{RUN_ID}-prompt-cache-requests.jsonl", row)

metrics_after = fetch_metrics("after")
decision = classify(rows)

result = {
    "run_id": RUN_ID,
    "created_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
    "base_url": BASE_URL,
    "model": MODEL,
    "stream": STREAM,
    "max_tokens": MAX_TOKENS,
    "manifest_path": MANIFEST_PATH,
    "prompt_text_saved": SAVE_PROMPTS,
    "metrics_before": metrics_before,
    "metrics_after": metrics_after,
    "decision": decision,
    "requests": rows,
    "external_docs_checked": [
        "https://docs.vllm.ai/en/stable/design/prefix_caching/",
        "https://docs.vllm.ai/en/stable/design/metrics/",
        "https://docs.ollama.com/api/generate",
        "https://docs.sglang.io/docs/advanced_features/server_arguments",
        "https://docs.sglang.io/docs/advanced_features/hicache_design",
        "https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md",
        "https://arxiv.org/abs/2311.04934",
    ],
}

results_json = OUT_DIR / f"{RUN_ID}-prompt-cache-results.json"
results_md = OUT_DIR / f"{RUN_ID}-prompt-cache-results.md"
requests_csv = OUT_DIR / f"{RUN_ID}-prompt-cache-requests.csv"
runs_jsonl = OUT_DIR / "prompt-cache-kv-reuse-runs.jsonl"

write_json(results_json, result)
write_csv(requests_csv, rows)
write_markdown(results_md, result)
append_jsonl(runs_jsonl, {"run_id": RUN_ID, "status": decision["status"], "decision": decision["decision"], "results_json": str(results_json)})

print(
    json.dumps(
        {
            "status": decision["status"],
            "decision": decision["decision"],
            "run_id": RUN_ID,
            "results_json": str(results_json),
            "results_md": str(results_md),
            "requests_csv": str(requests_csv),
            "requests_jsonl": str(OUT_DIR / f"{RUN_ID}-prompt-cache-requests.jsonl"),
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
| `LOCAL_LLM_BASE_URL` | yes | OpenAI-compatible base URL such as `http://127.0.0.1:11434/v1`. |
| `LOCAL_LLM_MODEL` | yes | Served model id. |
| `LOCAL_LLM_API_KEY` | no | Local placeholder token or proxy token. |
| `LOCAL_LLM_STREAM` | no | Set `1` to measure TTFT from SSE chunks. Defaults to `1`. |
| `LOCAL_LLM_MAX_TOKENS` | no | Output cap. Defaults to `64`. |
| `LOCAL_LLM_METRICS_URL` | no | Optional runtime metrics endpoint. Saves cache/prefix/KV/prompt lines. |
| `LOCAL_LLM_PROMPT_CACHE_MANIFEST` | no | Optional JSON manifest with `shared_prefix`, `changed_prefix`, `suffixes`, and optional `system`. |
| `LOCAL_LLM_SAVE_PROMPTS` | no | Set `1` to save prompt text. Defaults to `0`; prompt hashes and lengths are still saved. |
| `LOCAL_LLM_MIN_METRIC_DELTA_MS` | no | Minimum expected-hit improvement over controls. Defaults to `25`. |
| `LOCAL_LLM_MIN_METRIC_RATIO` | no | Expected-hit/control ratio threshold. Defaults to `0.85`. |

## PowerShell Run

```powershell
$RunRoot = Join-Path $HOME ("Documents\local-llm-runs\" + (Get-Date -Format "yyyy-MM-dd-HHmm") + "-prompt-cache")
New-Item -ItemType Directory -Force -Path $RunRoot | Out-Null

$env:LOCAL_LLM_RUN_ROOT = $RunRoot
$env:LOCAL_LLM_BASE_URL = "http://127.0.0.1:11434/v1"
$env:LOCAL_LLM_MODEL = "qwen3"
$env:LOCAL_LLM_STREAM = "1"
$env:LOCAL_LLM_MAX_TOKENS = "64"
python .\prompt-cache-kv-reuse-runner.py
```

If the runtime exposes metrics:

```powershell
$env:LOCAL_LLM_METRICS_URL = "http://127.0.0.1:8000/metrics"
python .\prompt-cache-kv-reuse-runner.py
```

## Optional Manifest

Use a manifest when the synthetic default prompt is not representative.

```json
{
  "system": "Answer briefly.",
  "shared_prefix": "Stable system prompt, examples, tool protocol, or document goes first.",
  "changed_prefix": "Similar length control text with a different opening token sequence.",
  "suffixes": [
    "Question A",
    "Question B",
    "Question C"
  ]
}
```

Keep private corpora local. The runner saves prompt hashes by default, but the endpoint still receives the actual prompt.

## Status Interpretation

| Status | Decision | Meaning | Next route |
|---|---|---|---|
| `pass` | `cache_likely` | Expected-hit rows beat changed-prefix controls on TTFT or prompt-eval timing. | Record in [[LLM/Study/Local LLM Inference Benchmark Log]] and [[LLM/Study/LLM Deployment Decision Matrix]]. |
| `pass` | `cache_not_proven` | Required rows ran, but repeated-prefix benefit did not appear. | Treat cache benefit as unproven; inspect runtime flags, prompt layout, metrics, or cache eviction. |
| `hold` | `warm_or_cache_signal` | Later shared-prefix rows improved, but controls do not prove why. | Add runtime cache counters or repeat with changed-prefix controls. |
| `hold` | `inconclusive` | Only total latency exists, or required rows are missing. | Enable streaming or collect runtime prompt/cache metrics. |
| `error` | `error` | A route, HTTP, response, or fixture failure occurred. | Run [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]] or [[LLM/Study/Local LLM Troubleshooting Decision Tree]]. |

## Completion Gate

The runner output is usable when:

- [ ] all six cases have `status=ok`, or each failed case has a named route owner
- [ ] the metric used for the decision is TTFT, prompt-eval duration, or explicitly labeled as indirect total latency
- [ ] shared-prefix rows and changed-prefix controls are both present
- [ ] prompt hashes, prompt lengths, output cap, model id, and stream setting are recorded
- [ ] runtime metrics are attached when available
- [ ] the result says `cache_likely`, `cache_not_proven`, `warm_or_cache_signal`, or `inconclusive`, not just "faster second run"
- [ ] private prompt text is either omitted or intentionally saved inside the local evidence folder

## External Docs Checked

- [vLLM Automatic Prefix Caching](https://docs.vllm.ai/en/stable/design/prefix_caching/)
- [vLLM Metrics](https://docs.vllm.ai/en/stable/design/metrics/)
- [Ollama generate API](https://docs.ollama.com/api/generate)
- [SGLang server arguments](https://docs.sglang.io/docs/advanced_features/server_arguments)
- [SGLang HiCache design](https://docs.sglang.io/docs/advanced_features/hicache_design)
- [SGLang FAQ on determinism](https://docs.sglang.io/docs/references/faq)
- [llama.cpp server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- [Prompt Cache: Modular Attention Reuse for Low-Latency Inference](https://arxiv.org/abs/2311.04934)

## References

- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
