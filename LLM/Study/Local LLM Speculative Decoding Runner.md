---
tags: [study, llm, inference, local-llm, speculative-decoding, draft-model, latency, throughput, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-15
---

# Local LLM Speculative Decoding Runner

> **One-line summary** Compare a no-spec local endpoint profile against a spec-enabled profile with the same prompts, sampler, and output cap, then save timing, output-rate, accepted-token-signal, quality, and keep/disable evidence.

Use this after [[LLM/Study/Local LLM Speculative Decoding Lab|Local LLM Speculative Decoding Lab]] explains the manual experiment and after [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner|Local LLM OpenAI-Compatible API Contract Runner]] proves both routes. Use it before claiming that a draft model, EAGLE, MTP, n-gram, Medusa-style path, or runtime-specific proposer improves local generation speed.

The runner does not enable speculative decoding by request body. Start the baseline and spec-enabled profiles yourself, then point this runner at each OpenAI-compatible endpoint. This avoids sending runtime-specific speculative fields to endpoints that may reject them.

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| Baseline/spec paired prompt rows | The same prompt suite was run with speculation off and on. | That the spec-enabled server really used drafts unless metrics/logs say so. |
| Streaming TTFT and decode-rate rows | Decode-phase speed can be compared separately from first-token timing. | Production throughput under concurrency. |
| Optional metrics snapshots | Draft, speculative, accepted-token, or rejection counters can support the speed result. | Comparable metric names across runtimes. |
| Output checks | Spec-enabled output stayed non-empty and matched required smoke constraints. | Full workload quality; use the quality harness for that. |
| JSON/CSV/Markdown/JSONL output | The result can feed the benchmark log, deployment matrix, and capstone workbook. | Long-run reliability, memory stability, or restart survival. |

Academic bridge: speculative decoding is a draft-and-verify decode-loop change. A cheap draft path proposes several tokens, and the target model verifies those tokens in fewer target-model steps. It can improve output-token speed when acceptance is high enough. It can regress when the draft path is too large, acceptance is low, memory pressure rises, or batching efficiency falls.

## Fixed Conditions

Write these before running:

| Field | Value |
|---|---|
| Baseline route |  |
| Spec-enabled route |  |
| Main model id |  |
| Draft method | draft model / EAGLE / MTP / n-gram / Medusa / other |
| Draft model or config |  |
| Same tokenizer/vocabulary evidence |  |
| Runtime and version |  |
| Output cap |  |
| Sampler | temperature `0`, fixed output cap |
| Streaming timing | on / off |
| Metrics URLs | baseline / spec / none |
| Peak memory check | manual row / metrics / not captured |
| Next gate | benchmark log / quality harness / concurrency runner / disable speculation |

If the spec-enabled profile is reachable beyond loopback, complete [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] before running the probe.

## Standard-Library Runner

Save this as `speculative-decoding-runner.py` inside the run folder. It uses only Python's standard library.

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


def make_headers(api_key):
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    return headers


def make_body(model, prompt):
    return {
        "model": model,
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
    return {
        "system": "You are a concise local benchmark assistant. Follow the requested format.",
        "prompts": [
            {
                "prompt_id": "SMOKE-EXACT",
                "class": "predictable",
                "prompt": "Reply with exactly: speculative check",
                "must_contain": ["speculative check"],
            },
            {
                "prompt_id": "WORK-SUMMARY",
                "class": "workload",
                "prompt": (
                    "In four short bullets, summarize why speculative decoding can improve local "
                    "LLM decode latency and name one reason it can regress."
                ),
                "must_contain": ["speculative"],
            },
            {
                "prompt_id": "LOW-ACCEPT",
                "class": "low_acceptance",
                "prompt": (
                    "Write one unusual sentence using the words latency, draft, verifier, and local. "
                    "Use a surprising metaphor but keep it technical."
                ),
                "must_contain": ["latency", "draft"],
            },
        ],
    }


def build_prompts(manifest):
    prompts = manifest.get("prompts") if isinstance(manifest.get("prompts"), list) else []
    clean = []
    for index, item in enumerate(prompts, start=1):
        if not isinstance(item, dict):
            continue
        prompt = str(item.get("prompt") or "").strip()
        if not prompt:
            continue
        must_contain = item.get("must_contain") if isinstance(item.get("must_contain"), list) else []
        clean.append(
            {
                "prompt_id": str(item.get("prompt_id") or f"PROMPT-{index:02d}"),
                "class": str(item.get("class") or "workload"),
                "prompt": prompt,
                "must_contain": [str(value).lower() for value in must_contain],
            }
        )
    if not clean:
        raise ValueError("manifest requires at least one prompt")
    return clean


def fetch_metrics(url, label):
    if not url:
        return {"label": label, "enabled": False}
    request = urllib.request.Request(url, method="GET")
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            text = response.read().decode("utf-8", errors="replace")
        elapsed_ms = round((time.perf_counter() - started) * 1000, 3)
        keywords = ("spec", "draft", "accept", "reject", "verify", "eagle", "mtp", "ngram", "medusa")
        relevant = [line for line in text.splitlines() if any(word in line.lower() for word in keywords)]
        return {
            "label": label,
            "enabled": True,
            "status": "ok",
            "elapsed_ms": elapsed_ms,
            "bytes": len(text.encode("utf-8")),
            "relevant_line_count": len(relevant),
            "relevant_lines": relevant[:80],
        }
    except Exception as exc:
        return {
            "label": label,
            "enabled": True,
            "status": "error",
            "error": f"{type(exc).__name__}: {exc}",
        }


def has_acceptance_signal(metrics):
    if not metrics or not metrics.get("enabled") or metrics.get("status") != "ok":
        return False
    text = "\n".join(metrics.get("relevant_lines") or []).lower()
    return ("accept" in text and ("draft" in text or "spec" in text)) or "accepted" in text


def run_case(profile, prompt_item, repeat_index):
    body = make_body(profile["model"], prompt_item["prompt"])
    case_id = f"{profile['name']}-{prompt_item['prompt_id']}-r{repeat_index}"
    request_path = OUT_DIR / f"{RUN_ID}-{case_id}-request.json"
    response_path = OUT_DIR / f"{RUN_ID}-{case_id}-response.json"
    output_path = OUT_DIR / f"{RUN_ID}-{case_id}-output.txt"
    request_record = {
        "case_id": case_id,
        "profile": profile["name"],
        "profile_kind": profile["kind"],
        "prompt_id": prompt_item["prompt_id"],
        "prompt_class": prompt_item["class"],
        "model": profile["model"],
        "base_url": profile["base_url"],
        "stream": STREAM,
        "max_tokens": MAX_TOKENS,
        "prompt_chars": len(prompt_item["prompt"]),
        "prompt_digest": digest_text(prompt_item["prompt"]),
    }
    if SAVE_PROMPTS:
        request_record["prompt"] = prompt_item["prompt"]
        request_record["body"] = body
    write_json(request_path, request_record)

    request = urllib.request.Request(
        join_url(profile["base_url"], "/chat/completions"),
        data=json.dumps(body).encode("utf-8"),
        headers=make_headers(profile["api_key"]),
        method="POST",
    )
    started = time.perf_counter()
    first_event_ms = None
    first_content_ms = None
    finish_reason = ""
    final_data = {}
    content_parts = []
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
    usage = usage_counts(final_data)
    completion_units = usage["completion_tokens"]
    unit_source = "completion_tokens"
    if completion_units is None:
        completion_units = max(1, len(text.split()))
        unit_source = "estimated_words"
    decode_ms = None
    decode_units_per_second = None
    if first_content_ms is not None:
        decode_ms = max(1.0, total_latency_ms - first_content_ms)
    else:
        decode_ms = max(1.0, total_latency_ms)
    decode_units_per_second = round(float(completion_units) / (decode_ms / 1000.0), 3)
    lower_text = text.lower()
    missing_terms = [term for term in prompt_item["must_contain"] if term not in lower_text]
    quality_status = "pass" if text.strip() and not missing_terms else "hold"

    output_path.write_text(text + "\n", encoding="utf-8")
    write_json(response_path, final_data if final_data else {"status": status, "error": error})

    return {
        "case_id": case_id,
        "profile": profile["name"],
        "profile_kind": profile["kind"],
        "prompt_id": prompt_item["prompt_id"],
        "prompt_class": prompt_item["class"],
        "repeat_index": repeat_index,
        "status": status,
        "error": error,
        "total_latency_ms": total_latency_ms,
        "first_event_ms": first_event_ms,
        "ttft_ms": first_content_ms,
        "decode_ms": round(decode_ms, 3) if decode_ms is not None else None,
        "decode_units_per_second": decode_units_per_second,
        "decode_unit_source": unit_source,
        "prompt_tokens": usage["prompt_tokens"],
        "completion_tokens": usage["completion_tokens"],
        "total_tokens": usage["total_tokens"],
        "finish_reason": finish_reason,
        "quality_status": quality_status,
        "missing_terms": missing_terms,
        "output_chars": len(text),
        "output_digest": digest_text(text),
        "output_preview": text[:140].replace("\n", " "),
        "prompt_chars": len(prompt_item["prompt"]),
        "prompt_digest": digest_text(prompt_item["prompt"]),
        "request_path": str(request_path),
        "response_path": str(response_path),
        "output_path": str(output_path),
    }


def mean(values):
    values = [float(value) for value in values if value is not None]
    if not values:
        return None
    return round(sum(values) / len(values), 3)


def summarize_prompt(rows, prompt_id):
    base = [row for row in rows if row["prompt_id"] == prompt_id and row["profile_kind"] == "baseline" and row["status"] == "ok"]
    spec = [row for row in rows if row["prompt_id"] == prompt_id and row["profile_kind"] == "spec" and row["status"] == "ok"]
    base_rate = mean([row["decode_units_per_second"] for row in base])
    spec_rate = mean([row["decode_units_per_second"] for row in spec])
    base_ttft = mean([row["ttft_ms"] for row in base])
    spec_ttft = mean([row["ttft_ms"] for row in spec])
    speedup = round(spec_rate / base_rate, 3) if base_rate and spec_rate else None
    return {
        "prompt_id": prompt_id,
        "baseline_decode_units_per_second": base_rate,
        "spec_decode_units_per_second": spec_rate,
        "decode_speedup": speedup,
        "baseline_ttft_ms": base_ttft,
        "spec_ttft_ms": spec_ttft,
        "quality_ok": all(row["quality_status"] == "pass" for row in base + spec) if base and spec else False,
    }


def classify(rows, summaries, metrics_before, metrics_after):
    errors = [row for row in rows if row["status"] != "ok"]
    quality_holds = [row for row in rows if row["quality_status"] != "pass"]
    speedups = [item["decode_speedup"] for item in summaries if item["decode_speedup"] is not None]
    average_speedup = mean(speedups)
    acceptance_signal = any(has_acceptance_signal(metrics) for metrics in metrics_before + metrics_after)

    if errors:
        return {
            "status": "error",
            "decision": "route_or_response_error",
            "reason": "At least one baseline or spec request failed.",
            "average_decode_speedup": average_speedup,
            "acceptance_signal": acceptance_signal,
            "next_route": "OpenAI-compatible API contract runner or troubleshooting decision tree.",
        }
    if quality_holds:
        return {
            "status": "hold",
            "decision": "quality_not_equivalent",
            "reason": "At least one output was empty or missed required smoke terms.",
            "average_decode_speedup": average_speedup,
            "acceptance_signal": acceptance_signal,
            "next_route": "Run quality harness or inspect prompt/template differences before enabling speculation.",
        }
    if average_speedup is None:
        return {
            "status": "hold",
            "decision": "inconclusive",
            "reason": "Decode-rate comparison could not be computed.",
            "average_decode_speedup": average_speedup,
            "acceptance_signal": acceptance_signal,
            "next_route": "Enable usage fields, streaming timing, or longer outputs.",
        }
    if average_speedup >= MIN_SPEEDUP and acceptance_signal:
        return {
            "status": "pass",
            "decision": "speculation_useful_with_acceptance_signal",
            "reason": "Spec profile improved decode output rate and metrics/logs include a draft or accepted-token signal.",
            "average_decode_speedup": average_speedup,
            "acceptance_signal": acceptance_signal,
            "next_route": "Record in benchmark log, then test memory and selected concurrency.",
        }
    if average_speedup >= MIN_SPEEDUP:
        return {
            "status": "hold",
            "decision": "speedup_observed_acceptance_unproven",
            "reason": "Spec profile improved decode output rate, but no accepted-token or draft metric was captured.",
            "average_decode_speedup": average_speedup,
            "acceptance_signal": acceptance_signal,
            "next_route": "Capture runtime metrics/logs before claiming speculative decoding is the cause.",
        }
    return {
        "status": "pass",
        "decision": "speculation_not_useful",
        "reason": "Spec profile did not beat the baseline decode-rate threshold.",
        "average_decode_speedup": average_speedup,
        "acceptance_signal": acceptance_signal,
        "next_route": "Keep speculation disabled for this workload or test a different draft method/model.",
    }


def write_csv(path, rows):
    fields = [
        "case_id",
        "profile",
        "profile_kind",
        "prompt_id",
        "prompt_class",
        "repeat_index",
        "status",
        "total_latency_ms",
        "ttft_ms",
        "decode_ms",
        "decode_units_per_second",
        "decode_unit_source",
        "prompt_tokens",
        "completion_tokens",
        "quality_status",
        "missing_terms",
        "finish_reason",
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
    lines = [
        f"# Speculative Decoding Runner - {RUN_ID}",
        "",
        "## Decision",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Status | `{decision['status']}` |",
        f"| Decision | `{decision['decision']}` |",
        f"| Reason | {md_cell(decision['reason'])} |",
        f"| Average decode speedup | {md_cell(decision['average_decode_speedup'])} |",
        f"| Acceptance signal captured | `{decision['acceptance_signal']}` |",
        f"| Next route | {md_cell(decision['next_route'])} |",
        "",
        "## Prompt Summary",
        "",
        "| Prompt | Baseline units/s | Spec units/s | Speedup | Baseline TTFT | Spec TTFT | Quality OK |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in result["prompt_summaries"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    md_cell(row["prompt_id"]),
                    md_cell(row["baseline_decode_units_per_second"]),
                    md_cell(row["spec_decode_units_per_second"]),
                    md_cell(row["decode_speedup"]),
                    md_cell(row["baseline_ttft_ms"]),
                    md_cell(row["spec_ttft_ms"]),
                    md_cell(row["quality_ok"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Request Rows",
            "",
            "| Profile | Prompt | Status | Total ms | TTFT ms | Decode units/s | Quality | Error |",
            "|---|---|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in result["requests"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    md_cell(row["profile"]),
                    md_cell(row["prompt_id"]),
                    md_cell(row["status"]),
                    md_cell(row["total_latency_ms"]),
                    md_cell(row["ttft_ms"]),
                    md_cell(row["decode_units_per_second"]),
                    md_cell(row["quality_status"]),
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
            f"- Baseline metrics before/after: `{result['metrics_before'][0].get('status', 'disabled')}` / `{result['metrics_after'][0].get('status', 'disabled')}`",
            f"- Spec metrics before/after: `{result['metrics_before'][1].get('status', 'disabled')}` / `{result['metrics_after'][1].get('status', 'disabled')}`",
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
SPEC_BASE_URL = os.environ.get("LOCAL_LLM_SPEC_BASE_URL", "").strip() or BASE_URL
SPEC_MODEL = os.environ.get("LOCAL_LLM_SPEC_MODEL", "").strip() or MODEL
API_KEY = os.environ.get("LOCAL_LLM_API_KEY", "").strip()
SPEC_API_KEY = os.environ.get("LOCAL_LLM_SPEC_API_KEY", "").strip() or API_KEY
RUN_ROOT = Path(os.environ.get("LOCAL_LLM_RUN_ROOT", ".")).expanduser().resolve()
STREAM = env_bool("LOCAL_LLM_STREAM", True)
SAVE_PROMPTS = env_bool("LOCAL_LLM_SAVE_PROMPTS", False)
MAX_TOKENS = as_int(os.environ.get("LOCAL_LLM_MAX_TOKENS"), 128)
REPEATS = max(1, as_int(os.environ.get("LOCAL_LLM_REPEATS"), 1))
TIMEOUT_SECONDS = as_int(os.environ.get("LOCAL_LLM_TIMEOUT_SECONDS"), 120)
MIN_SPEEDUP = as_float(os.environ.get("LOCAL_LLM_MIN_SPEC_SPEEDUP"), 1.10)
MANIFEST_PATH = os.environ.get("LOCAL_LLM_SPEC_PROMPT_MANIFEST", "").strip()
BASE_METRICS_URL = os.environ.get("LOCAL_LLM_METRICS_URL", "").strip()
SPEC_METRICS_URL = os.environ.get("LOCAL_LLM_SPEC_METRICS_URL", "").strip()
BASE_LABEL = os.environ.get("LOCAL_LLM_BASELINE_LABEL", "baseline-no-spec").strip()
SPEC_LABEL = os.environ.get("LOCAL_LLM_SPEC_LABEL", "spec-enabled").strip()
RUN_ID = time.strftime("%Y%m%d-%H%M%S-speculative")
OUT_DIR = RUN_ROOT / "speculative-decoding-runner"

if not BASE_URL or not MODEL:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    sample = {
        "LOCAL_LLM_BASE_URL": "http://127.0.0.1:8000/v1",
        "LOCAL_LLM_MODEL": "main-model-id",
        "LOCAL_LLM_SPEC_BASE_URL": "http://127.0.0.1:8001/v1",
        "LOCAL_LLM_SPEC_MODEL": "main-model-id",
        "LOCAL_LLM_STREAM": "1",
        "LOCAL_LLM_MAX_TOKENS": "128",
        "LOCAL_LLM_METRICS_URL": "optional baseline metrics URL",
        "LOCAL_LLM_SPEC_METRICS_URL": "optional spec metrics URL",
    }
    write_json(OUT_DIR / "speculative-decoding-runner-env-template.json", sample)
    print(json.dumps({"status": "error", "template": str(OUT_DIR / "speculative-decoding-runner-env-template.json")}, indent=2))
    raise SystemExit(0)

manifest = load_manifest(MANIFEST_PATH) if MANIFEST_PATH else default_manifest()
SYSTEM_PROMPT = str(manifest.get("system") or "You are a concise local benchmark assistant.")
prompts = build_prompts(manifest)
profiles = [
    {"name": BASE_LABEL, "kind": "baseline", "base_url": BASE_URL, "model": MODEL, "api_key": API_KEY, "metrics_url": BASE_METRICS_URL},
    {"name": SPEC_LABEL, "kind": "spec", "base_url": SPEC_BASE_URL, "model": SPEC_MODEL, "api_key": SPEC_API_KEY, "metrics_url": SPEC_METRICS_URL},
]

metrics_before = [fetch_metrics(profile["metrics_url"], f"{profile['name']}-before") for profile in profiles]
rows = []
for profile in profiles:
    for repeat_index in range(1, REPEATS + 1):
        for prompt_item in prompts:
            row = run_case(profile, prompt_item, repeat_index)
            rows.append(row)
            append_jsonl(OUT_DIR / f"{RUN_ID}-speculative-requests.jsonl", row)
metrics_after = [fetch_metrics(profile["metrics_url"], f"{profile['name']}-after") for profile in profiles]
prompt_summaries = [summarize_prompt(rows, prompt["prompt_id"]) for prompt in prompts]
decision = classify(rows, prompt_summaries, metrics_before, metrics_after)

result = {
    "run_id": RUN_ID,
    "created_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
    "baseline": {"base_url": BASE_URL, "model": MODEL, "label": BASE_LABEL},
    "spec": {"base_url": SPEC_BASE_URL, "model": SPEC_MODEL, "label": SPEC_LABEL},
    "stream": STREAM,
    "max_tokens": MAX_TOKENS,
    "repeats": REPEATS,
    "manifest_path": MANIFEST_PATH,
    "prompt_text_saved": SAVE_PROMPTS,
    "min_speedup": MIN_SPEEDUP,
    "metrics_before": metrics_before,
    "metrics_after": metrics_after,
    "prompt_summaries": prompt_summaries,
    "decision": decision,
    "requests": rows,
    "external_docs_checked": [
        "https://docs.vllm.ai/en/latest/features/speculative_decoding/",
        "https://sgl-project.github.io/advanced_features/speculative_decoding.html",
        "https://github.com/ggml-org/llama.cpp/blob/master/docs/speculative.md",
        "https://lmstudio.ai/docs/app/advanced/speculative-decoding",
        "https://lmstudio.ai/docs/python/llm-prediction/speculative-decoding",
        "https://arxiv.org/abs/2211.17192",
    ],
}

results_json = OUT_DIR / f"{RUN_ID}-speculative-results.json"
results_md = OUT_DIR / f"{RUN_ID}-speculative-results.md"
requests_csv = OUT_DIR / f"{RUN_ID}-speculative-requests.csv"
runs_jsonl = OUT_DIR / "speculative-decoding-runs.jsonl"
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
            "requests_jsonl": str(OUT_DIR / f"{RUN_ID}-speculative-requests.jsonl"),
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
| `LOCAL_LLM_BASE_URL` | yes | Baseline OpenAI-compatible base URL. |
| `LOCAL_LLM_MODEL` | yes | Baseline model id. |
| `LOCAL_LLM_SPEC_BASE_URL` | no | Spec-enabled base URL. Defaults to baseline URL for same-server profile tests. |
| `LOCAL_LLM_SPEC_MODEL` | no | Spec-enabled served model id. Defaults to baseline model id. |
| `LOCAL_LLM_API_KEY` / `LOCAL_LLM_SPEC_API_KEY` | no | Local placeholder or proxy token. |
| `LOCAL_LLM_STREAM` | no | Set `1` to measure TTFT from SSE chunks. Defaults to `1`. |
| `LOCAL_LLM_MAX_TOKENS` | no | Output cap. Defaults to `128`. |
| `LOCAL_LLM_REPEATS` | no | Repeats per prompt per profile. Defaults to `1`. |
| `LOCAL_LLM_METRICS_URL` | no | Baseline metrics endpoint. |
| `LOCAL_LLM_SPEC_METRICS_URL` | no | Spec-enabled metrics endpoint. |
| `LOCAL_LLM_SPEC_PROMPT_MANIFEST` | no | Optional prompt suite JSON. |
| `LOCAL_LLM_MIN_SPEC_SPEEDUP` | no | Minimum average decode-rate ratio for a speedup. Defaults to `1.10`. |
| `LOCAL_LLM_SAVE_PROMPTS` | no | Set `1` to save prompt text. Defaults to `0`; prompt hashes are still saved. |

## PowerShell Run

```powershell
$RunRoot = Join-Path $HOME ("Documents\local-llm-runs\" + (Get-Date -Format "yyyy-MM-dd-HHmm") + "-speculative")
New-Item -ItemType Directory -Force -Path $RunRoot | Out-Null

$env:LOCAL_LLM_RUN_ROOT = $RunRoot
$env:LOCAL_LLM_BASE_URL = "http://127.0.0.1:8000/v1"
$env:LOCAL_LLM_MODEL = "main-model-id"
$env:LOCAL_LLM_SPEC_BASE_URL = "http://127.0.0.1:8001/v1"
$env:LOCAL_LLM_SPEC_MODEL = "main-model-id"
$env:LOCAL_LLM_STREAM = "1"
$env:LOCAL_LLM_MAX_TOKENS = "128"
python .\speculative-decoding-runner.py
```

With metrics:

```powershell
$env:LOCAL_LLM_METRICS_URL = "http://127.0.0.1:8000/metrics"
$env:LOCAL_LLM_SPEC_METRICS_URL = "http://127.0.0.1:8001/metrics"
python .\speculative-decoding-runner.py
```

## Optional Prompt Manifest

```json
{
  "system": "Answer briefly.",
  "prompts": [
    {
      "prompt_id": "SMOKE-EXACT",
      "class": "predictable",
      "prompt": "Reply with exactly: speculative check",
      "must_contain": ["speculative check"]
    },
    {
      "prompt_id": "WORK-01",
      "class": "workload",
      "prompt": "Summarize the local task in four bullets.",
      "must_contain": ["local"]
    }
  ]
}
```

## Status Interpretation

| Status | Decision | Meaning | Next route |
|---|---|---|---|
| `pass` | `speculation_useful_with_acceptance_signal` | Spec profile improves decode output rate and metrics/logs contain a draft or accepted-token signal. | Record in [[LLM/Study/Local LLM Inference Benchmark Log]], then test memory and concurrency. |
| `hold` | `speedup_observed_acceptance_unproven` | Spec profile is faster, but no accepted-token or draft metric was captured. | Add runtime metrics/log evidence before claiming speculative decoding is the cause. |
| `pass` | `speculation_not_useful` | The spec profile did not beat the decode-speed threshold. | Keep speculation disabled or try another draft method/model. |
| `hold` | `quality_not_equivalent` | Output checks failed. | Run [[LLM/Study/Local LLM Quality Evaluation Harness]] or inspect prompt/template differences. |
| `hold` | `inconclusive` | Decode-rate comparison could not be computed. | Enable streaming, usage fields, longer outputs, or repeated runs. |
| `error` | `route_or_response_error` | A baseline/spec request failed. | Run [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]] or [[LLM/Study/Local LLM Troubleshooting Decision Tree]]. |

## Completion Gate

The runner output is usable when:

- [ ] baseline and spec-enabled profiles both completed the same prompt suite
- [ ] output cap, sampler, model id, and prompt hashes are recorded
- [ ] decode-rate and TTFT fields are present or the missing metric is named
- [ ] accepted-token, draft, speculative, or equivalent metrics/logs are attached when available
- [ ] quality checks are pass or have a named owner
- [ ] the decision is not based only on a faster second warm request
- [ ] the next route says keep, disable, add metrics, run quality harness, or test concurrency

## External Docs Checked

- [vLLM speculative decoding](https://docs.vllm.ai/en/latest/features/speculative_decoding/)
- [SGLang speculative decoding](https://sgl-project.github.io/advanced_features/speculative_decoding.html)
- [llama.cpp speculative decoding](https://github.com/ggml-org/llama.cpp/blob/master/docs/speculative.md)
- [LM Studio speculative decoding](https://lmstudio.ai/docs/app/advanced/speculative-decoding)
- [LM Studio Python SDK speculative decoding](https://lmstudio.ai/docs/python/llm-prediction/speculative-decoding)
- [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192)

## References

- [[LLM/Study/Local LLM Speculative Decoding Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]]
- [[LLM/Study/Decoding and Sampling Controls Runner]]
- [[LLM/Study/Local LLM First Streaming Timing Runner]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner]]
- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/2024–2025 — Frontier and Efficiency/Speculative Decoding]]
