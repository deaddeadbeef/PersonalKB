---
tags: [study, llm, inference, local-llm, ollama, metrics, benchmark, debrief, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM First Response Debrief Runner

> **One-line summary** Turn the first saved local LLM response into debrief JSON, Markdown, and JSONL evidence without sending another inference request.

Use this after [[LLM/Study/Local LLM First Smoke Request Runner|Local LLM First Smoke Request Runner]] creates a smoke summary, or after [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]] saves a native Ollama response. The manual [[LLM/Study/Local LLM First Response Debrief Card|Local LLM First Response Debrief Card]] explains the interpretation. This runner makes the interpretation repeatable.

This is a read-only debrief over local files. It does not call `/api/generate`, `/api/chat`, `/v1/chat/completions`, or any other endpoint. That matters because the debrief should explain the first response, not accidentally create a second response with different cache, load, prompt, or sampler state.

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| Smoke summary path | The debrief is tied to a named first-run artifact. | That the endpoint is still running now. |
| Native response path | The raw local response was preserved. | Quality, safety, or workload fit. |
| Parsed model and text | The saved response has a model id and extractable output. | The exact model bytes without pull/show evidence. |
| Converted timing fields | Load, prefill, and decode timing can be discussed in seconds. | TTFT or stream behavior. |
| Token-rate fields | Prompt and decode denominators can be audited. | A stable benchmark without repeated runs. |
| Mechanism owner | The next action is assigned to cold load, prefill, decode, route, template, metrics, or quality. | Production readiness. |

Academic bridge: a saved native Ollama response exposes the serving phases that map back to the transformer inference path. `prompt_eval_duration` belongs to prompt processing and prefill. `eval_duration` belongs to the autoregressive decode loop. `load_duration` belongs to model residency and cold-start behavior. Those fields are route evidence, not model-quality evidence.

## Inputs

Set only the inputs you need:

| Variable | Default | Meaning |
|---|---|---|
| `LOCAL_LLM_RUN_ROOT` | current directory | Run folder that contains `first-smoke-request`. |
| `LOCAL_LLM_SMOKE_SUMMARY` | newest `first-smoke-request/*-summary.json` | Smoke runner summary to inspect. |
| `LOCAL_LLM_NATIVE_RESPONSE` | path from smoke summary, then native response fallback | Saved native Ollama response or smoke-runner wrapper. |
| `LOCAL_LLM_OPENAI_RESPONSE` | path from smoke summary, then OpenAI response fallback | Optional saved OpenAI-compatible response or wrapper. |
| `LOCAL_LLM_EXPECT_MODEL` | `model` from smoke summary | Expected served model id. |
| `LOCAL_LLM_EXPECT_TEXT` | `expected_text` from smoke summary | Optional exact smoke text. |
| `LOCAL_LLM_ROUTE` | `Ollama native /api/generate` | Human-facing route label. |
| `LOCAL_LLM_BOUNDARY` | `loopback or recorded boundary` | Listener boundary to record. |
| `LOCAL_LLM_NEXT_ACTION` | derived from status | Override the routed next action. |

## Standard-Library Debrief Runner

Save this as `first-response-debrief.py` inside the run folder.

```python
import json
import os
import time
from pathlib import Path


DURATION_FIELDS = {
    "total_duration": "total_seconds",
    "load_duration": "load_seconds",
    "prompt_eval_duration": "prompt_eval_seconds",
    "eval_duration": "decode_seconds",
}
COUNT_FIELDS = ["prompt_eval_count", "eval_count"]


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def read_json(path):
    if not path:
        return None, "path not set"
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except FileNotFoundError:
        return None, f"missing file: {path}"
    except json.JSONDecodeError as exc:
        return None, f"invalid json: {path}: {exc}"


def latest_file(root, pattern):
    if not root.exists():
        return None
    files = list(root.glob(pattern))
    if not files:
        return None
    return sorted(files, key=lambda item: item.stat().st_mtime, reverse=True)[0]


def resolve_path(value, base):
    if not value:
        return None
    path = Path(str(value)).expanduser()
    if not path.is_absolute():
        path = base / path
    return path.resolve()


def summary_response_path(summary, route_name):
    if not isinstance(summary, dict):
        return None
    block = summary.get(route_name)
    if not isinstance(block, dict):
        return None
    return block.get("response_path")


def unwrap_response(raw):
    if isinstance(raw, dict) and isinstance(raw.get("json"), dict):
        return raw["json"], raw
    if isinstance(raw, dict):
        return raw, {}
    return {}, {}


def nested_text(value):
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        parts = []
        for item in value:
            if isinstance(item, dict):
                parts.append(str(item.get("text") or item.get("content") or ""))
            else:
                parts.append(str(item))
        return " ".join(part for part in parts if part)
    return ""


def normalize_text(value):
    return " ".join(str(value or "").strip().lower().split())


def md_cell(value):
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True)
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def as_number(value):
    if value is None or isinstance(value, bool):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def ns_to_seconds(value):
    number = as_number(value)
    if number is None:
        return None
    return number / 1_000_000_000


def round_optional(value, digits=3):
    if value is None:
        return None
    return round(value, digits)


def tokens_per_second(count, duration_ns):
    count_number = as_number(count)
    seconds = ns_to_seconds(duration_ns)
    if count_number is None or seconds is None or seconds <= 0:
        return None
    return round(count_number / seconds, 2)


def extract_native(body, wrapper):
    message = body.get("message") if isinstance(body.get("message"), dict) else {}
    generated_text = body.get("response")
    if not generated_text:
        generated_text = nested_text(message.get("content"))
    timing_ns = {key: body.get(key) for key in DURATION_FIELDS if key in body}
    counts = {key: body.get(key) for key in COUNT_FIELDS if key in body}
    timing_seconds = {
        label: round_optional(ns_to_seconds(body.get(raw_field)))
        for raw_field, label in DURATION_FIELDS.items()
        if raw_field in body
    }
    return {
        "route_status": wrapper.get("status") or ("pass" if body else "error"),
        "http_status": wrapper.get("http_status"),
        "elapsed_s": wrapper.get("elapsed_s"),
        "model": body.get("model"),
        "done": body.get("done"),
        "done_reason": body.get("done_reason"),
        "text": generated_text or "",
        "text_excerpt": " ".join(str(generated_text or "").split())[:240],
        "timing_ns": timing_ns,
        "timing_seconds": timing_seconds,
        "counts": counts,
        "prompt_tokens_per_second": tokens_per_second(body.get("prompt_eval_count"), body.get("prompt_eval_duration")),
        "decode_tokens_per_second": tokens_per_second(body.get("eval_count"), body.get("eval_duration")),
    }


def extract_openai(body, wrapper):
    choices = body.get("choices") if isinstance(body.get("choices"), list) else []
    first = choices[0] if choices and isinstance(choices[0], dict) else {}
    message = first.get("message") if isinstance(first.get("message"), dict) else {}
    text = nested_text(message.get("content")) or nested_text(first.get("text"))
    return {
        "route_status": wrapper.get("status") or ("pass" if body else "missing"),
        "http_status": wrapper.get("http_status"),
        "elapsed_s": wrapper.get("elapsed_s"),
        "finish_reason": first.get("finish_reason"),
        "text": text,
        "text_excerpt": " ".join(str(text or "").split())[:240],
        "usage": body.get("usage") if isinstance(body.get("usage"), dict) else {},
    }


def dominant_timing(native):
    values = {
        "cold load": as_number(native["timing_ns"].get("load_duration")),
        "prefill": as_number(native["timing_ns"].get("prompt_eval_duration")),
        "decode": as_number(native["timing_ns"].get("eval_duration")),
    }
    values = {name: value for name, value in values.items() if value is not None and value > 0}
    if not values:
        return "missing metrics"
    return max(values, key=values.get)


def choose_mechanism(native, model_match, text_match, openai_expected, openai):
    if native["route_status"] == "error":
        return "route"
    if not native["text"]:
        return "output extraction"
    if model_match is False:
        return "model id"
    if text_match is False:
        return "template or sampler"
    if openai_expected and openai["route_status"] != "pass":
        return "api compatibility"
    timing_owner = dominant_timing(native)
    if timing_owner != "missing metrics":
        return timing_owner
    return "missing metrics"


def default_next_action(status, mechanism):
    if status == "error":
        return "diagnose listener, model id, or route before retry"
    if mechanism == "api compatibility":
        return "run Local LLM OpenAI-Compatible API Contract Lab"
    if mechanism == "model id":
        return "rerun Local LLM First Model Pull Gate and smoke request with the intended model id"
    if mechanism == "output extraction":
        return "diagnose prompt, stop condition, response shape, and chat template"
    if mechanism == "missing metrics":
        return "use Local LLM Client Harness Lab or Inference Metrics Field Guide before benchmark claims"
    if mechanism in {"cold load", "prefill", "decode"}:
        return "run Local LLM First Quality Probe Suite before any quality claim"
    return "run Local LLM First Quality Probe Suite"


def write_markdown(path, record):
    lines = [
        f"# First Response Debrief - {record['run_id']}",
        "",
        f"Status: `{record['status']}`",
        "",
        "## What This Proves",
        "",
        f"This run proves {record['route']} answered on {record['boundary']} with {record['native']['model'] or 'an unreported model id'}; it does not yet prove quality, safety, workload fit, RAG behavior, tool use, or deployment readiness.",
        "",
        "## Source Files",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Smoke summary | {md_cell(record['source']['smoke_summary_path'])} |",
        f"| Native response | {md_cell(record['source']['native_response_path'])} |",
        f"| OpenAI-compatible response | {md_cell(record['source']['openai_response_path'])} |",
        f"| Smoke status | {md_cell(record['source']['smoke_status'])} |",
        "",
        "## Native Response",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Model | {md_cell(record['native']['model'])} |",
        f"| Expected model | {md_cell(record['expected_model'])} |",
        f"| Model match | {md_cell(record['model_match'])} |",
        f"| Done | {md_cell(record['native']['done'])} |",
        f"| Done reason | {md_cell(record['native']['done_reason'])} |",
        f"| Expected text match | {md_cell(record['text_match'])} |",
        f"| Response excerpt | {md_cell(record['native']['text_excerpt'])} |",
        "",
        "## Timing",
        "",
        "| Metric | Raw ns | Seconds |",
        "|---|---:|---:|",
    ]
    for raw_field, seconds_field in DURATION_FIELDS.items():
        lines.append(
            f"| {raw_field} | {md_cell(record['native']['timing_ns'].get(raw_field))} | {md_cell(record['native']['timing_seconds'].get(seconds_field))} |"
        )
    lines.extend([
        "",
        "| Rate | Value |",
        "|---|---:|",
        f"| prompt tokens/sec | {md_cell(record['native']['prompt_tokens_per_second'])} |",
        f"| decode tokens/sec | {md_cell(record['native']['decode_tokens_per_second'])} |",
        "",
        "## Mechanism And Next Action",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Mechanism owner | {md_cell(record['mechanism_owner'])} |",
        f"| Quality boundary | {md_cell(record['quality_boundary'])} |",
        f"| Missing layer | {md_cell(', '.join(record['missing_layers']) if record['missing_layers'] else 'none')} |",
        f"| Next action | {md_cell(record['next_action'])} |",
        "",
        "## Benchmark Add-On",
        "",
        "| Field | Value |",
        "|---|---|",
    ])
    for key, value in record["benchmark_add_on"].items():
        lines.append(f"| {key} | {md_cell(value)} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


RUN_ROOT = Path(os.environ.get("LOCAL_LLM_RUN_ROOT", ".")).expanduser().resolve()
summary_path = resolve_path(os.environ.get("LOCAL_LLM_SMOKE_SUMMARY"), RUN_ROOT)
if not summary_path:
    summary_path = latest_file(RUN_ROOT / "first-smoke-request", "*-summary.json")
summary, summary_error = read_json(summary_path)
if summary is None:
    summary = {}

native_path = resolve_path(os.environ.get("LOCAL_LLM_NATIVE_RESPONSE"), RUN_ROOT)
if not native_path:
    native_path = resolve_path(summary_response_path(summary, "native"), RUN_ROOT)
if not native_path:
    native_path = latest_file(RUN_ROOT / "first-smoke-request" / "responses", "*native*response.json")
if not native_path:
    native_path = resolve_path("ollama-native-response.json", RUN_ROOT)

openai_path = resolve_path(os.environ.get("LOCAL_LLM_OPENAI_RESPONSE"), RUN_ROOT)
if not openai_path:
    openai_path = resolve_path(summary_response_path(summary, "openai"), RUN_ROOT)
if not openai_path:
    openai_path = latest_file(RUN_ROOT / "first-smoke-request" / "responses", "*openai*response.json")

native_raw, native_error = read_json(native_path)
openai_raw, openai_error = read_json(openai_path) if openai_path else (None, "path not set")
native_body, native_wrapper = unwrap_response(native_raw)
openai_body, openai_wrapper = unwrap_response(openai_raw)

native = extract_native(native_body, native_wrapper)
openai = extract_openai(openai_body, openai_wrapper)

expected_model = os.environ.get("LOCAL_LLM_EXPECT_MODEL") or summary.get("model") or ""
expected_text = os.environ.get("LOCAL_LLM_EXPECT_TEXT") or summary.get("expected_text") or ""
route = os.environ.get("LOCAL_LLM_ROUTE", "Ollama native /api/generate")
boundary = os.environ.get("LOCAL_LLM_BOUNDARY", "loopback or recorded boundary")

model_match = None
if expected_model:
    model_match = native["model"] == expected_model
text_match = None
if expected_text and native["text"]:
    text_match = normalize_text(native["text"]) == normalize_text(expected_text)

openai_summary = summary.get("openai") if isinstance(summary.get("openai"), dict) else {}
openai_expected = bool(openai_path) or openai_summary.get("decision") not in {None, "", "skipped"}

missing_layers = []
if summary_error:
    missing_layers.append("smoke summary")
if native_error:
    missing_layers.append("native response file")
if native["route_status"] == "error":
    missing_layers.append("native route status")
if not native["text"]:
    missing_layers.append("response text")
if expected_model and model_match is False:
    missing_layers.append("model match")
if expected_text and text_match is False:
    missing_layers.append("expected smoke text")
if native["done"] is False:
    missing_layers.append("done state")
if not native["timing_ns"]:
    missing_layers.append("timing fields")
if not native["counts"]:
    missing_layers.append("token counts")
if openai_expected and openai_error:
    missing_layers.append("openai-compatible response")
elif openai_expected and openai["route_status"] == "error":
    missing_layers.append("openai-compatible route")

if native_error or native["route_status"] == "error":
    status = "error"
elif missing_layers:
    status = "hold"
else:
    status = "pass"

mechanism = choose_mechanism(native, model_match, text_match, openai_expected, openai)
next_action = os.environ.get("LOCAL_LLM_NEXT_ACTION") or default_next_action(status, mechanism)
run_id = summary.get("run_id") or f"{time.strftime('%Y%m%d-%H%M%S')}-first-response"
timestamp = time.strftime("%Y-%m-%dT%H:%M:%S%z")

record = {
    "run_id": run_id,
    "timestamp": timestamp,
    "status": status,
    "route": route,
    "boundary": boundary,
    "expected_model": expected_model,
    "expected_text": expected_text,
    "model_match": model_match,
    "text_match": text_match,
    "source": {
        "smoke_summary_path": str(summary_path) if summary_path else "",
        "smoke_summary_error": summary_error,
        "smoke_status": summary.get("status"),
        "native_response_path": str(native_path) if native_path else "",
        "native_response_error": native_error,
        "openai_response_path": str(openai_path) if openai_path else "",
        "openai_response_error": openai_error,
    },
    "native": native,
    "openai": openai,
    "missing_layers": missing_layers,
    "mechanism_owner": mechanism,
    "quality_boundary": "route-only until Local LLM First Quality Probe Suite is scored",
    "next_action": next_action,
    "benchmark_add_on": {
        "Run id": run_id,
        "Response file": str(native_path) if native_path else "",
        "Runtime and route": route,
        "Model": native["model"],
        "Prompt class": "smoke",
        "Done reason": native["done_reason"],
        "Total seconds": native["timing_seconds"].get("total_seconds"),
        "Load seconds": native["timing_seconds"].get("load_seconds"),
        "Prompt tokens": native["counts"].get("prompt_eval_count"),
        "Prompt eval seconds": native["timing_seconds"].get("prompt_eval_seconds"),
        "Prompt tokens/sec": native["prompt_tokens_per_second"],
        "Output tokens": native["counts"].get("eval_count"),
        "Decode seconds": native["timing_seconds"].get("decode_seconds"),
        "Decode tokens/sec": native["decode_tokens_per_second"],
        "Listener boundary": boundary,
        "Quality status": "route-only",
        "Main mechanism": mechanism,
        "Next controlled action": next_action,
    },
}

out_dir = RUN_ROOT / "first-response-debrief"
json_path = out_dir / f"{run_id}-debrief.json"
markdown_path = out_dir / f"{run_id}-debrief.md"
jsonl_path = out_dir / "response-debriefs.jsonl"
write_json(json_path, record)
write_markdown(markdown_path, record)
jsonl_path.parent.mkdir(parents=True, exist_ok=True)
with jsonl_path.open("a", encoding="utf-8") as handle:
    handle.write(json.dumps(record, ensure_ascii=True) + "\n")

print(json.dumps({
    "status": status,
    "debrief_json": str(json_path),
    "debrief_markdown": str(markdown_path),
    "missing_layers": missing_layers,
    "mechanism_owner": mechanism,
    "next_action": next_action,
}, indent=2))
```

PowerShell run from the evidence folder:

```powershell
$env:LOCAL_LLM_RUN_ROOT = "<paste-run-folder-path>"
$env:LOCAL_LLM_SMOKE_SUMMARY = "<optional-first-smoke-summary-json>"
$env:LOCAL_LLM_EXPECT_MODEL = "<model-tag-from-pull-gate>"
$env:LOCAL_LLM_BOUNDARY = "loopback"
python .\first-response-debrief.py
```

Pass signal: `first-response-debrief\<run-id>-debrief.json`, `.md`, and `response-debriefs.jsonl` exist; status is `pass`; model, response text, timing conversions, token rates, mechanism owner, quality boundary, and next action are populated.

Hold signal: the JSON files exist, but the response text, expected model, exact smoke text, timing fields, token counts, or OpenAI-compatible response is missing. Keep the output. A hold row is useful because it names the missing layer.

Error signal: the native response file is missing, unparsable, or saved as an error-shaped route result. Route to [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]] or [[LLM/Study/Local LLM First Runtime Health Snapshot|Local LLM First Runtime Health Snapshot]] before retrying.

## Evidence Row

Copy this row into [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]], [[LLM/Study/Local LLM First Inference Evidence Pack|Local LLM First Inference Evidence Pack]], or [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]:

| Field | Value |
|---|---|
| Run id |  |
| Smoke summary |  |
| Native response file |  |
| OpenAI-compatible response file |  |
| Debrief JSON |  |
| Debrief Markdown |  |
| Status | pass / hold / error |
| Model match | true / false / not checked |
| Text match | true / false / not checked |
| Timing fields | present / missing |
| Prompt tokens/sec |  |
| Decode tokens/sec |  |
| Mechanism owner | cold load / prefill / decode / route / template or sampler / api compatibility / missing metrics |
| Quality boundary | route-only until quality probe suite |
| Next controlled action |  |

## Mechanism Routing

| Observation | Owner | Next route |
|---|---|---|
| `load_duration` dominates | Cold load or model residency | [[LLM/Study/Local LLM Observability and Operations Runbook]] |
| `prompt_eval_duration` dominates | Prefill, prompt length, rendered context, tokenizer/template | [[LLM/Study/LLM Inference Request Lifecycle Lab]] and [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]] |
| `eval_duration` dominates | Decode loop, model size, memory bandwidth, quantization, offload | [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]] |
| Native route works but OpenAI-compatible response is missing | API compatibility layer | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]] |
| Text is missing or does not match the smoke target | Response extraction, prompt, sampler, stop, or chat template | [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]] |
| Timing fields are missing | Runtime route limitation or wrapper choice | [[LLM/Study/Local LLM Client Harness Lab]] and [[LLM/Study/Local LLM Inference Metrics Field Guide]] |
| Route works but quality is unknown | Evaluation, not serving | [[LLM/Study/Local LLM First Quality Probe Suite]] |

## Completion Gate

This runner is complete only when:

- [ ] the source smoke summary or native response path is recorded
- [ ] the debrief JSON exists
- [ ] the debrief Markdown exists
- [ ] `response-debriefs.jsonl` has the run row
- [ ] nanosecond timing fields are converted or marked missing
- [ ] token rates are calculated or marked missing
- [ ] one mechanism owner is named
- [ ] one next action is named
- [ ] route-only evidence is not treated as quality proof

## References

Internal routes:

- [[LLM/Study/Local LLM First Smoke Request Runner]]
- [[LLM/Study/Local LLM First Response Debrief Card]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM First Quality Probe Suite]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]

External/current sources checked 2026-06-15:

- [Ollama generate endpoint](https://docs.ollama.com/api/generate)
- [Ollama chat endpoint](https://docs.ollama.com/api/chat)
- [Ollama usage metrics](https://docs.ollama.com/api/usage)
