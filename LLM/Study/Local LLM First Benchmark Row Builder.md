---
tags: [study, llm, inference, local-llm, benchmark, latency, metrics, client, harness, evidence]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM First Benchmark Row Builder

> **One-line summary** After the first client and streaming runs exist, use this builder to turn raw JSONL evidence into one benchmark row with timing, token, quality, missing-layer, and next-action fields.

Use this after [[LLM/Study/Local LLM First Client Harness Runner|Local LLM First Client Harness Runner]] and [[LLM/Study/Local LLM First Streaming Timing Runner|Local LLM First Streaming Timing Runner]] produce run logs. Use [[LLM/Study/Decoding and Sampling Controls Runner|Decoding and Sampling Controls Runner]] first when sampler settings, seed behavior, stop strings, or output caps are not yet fixed. Use [[LLM/Study/Local LLM Context Window and Token Budgeting Runner|Local LLM Context Window and Token Budgeting Runner]] first when prompt, history, RAG chunks, tool schemas, or output reserve may explain TTFT, truncation, or memory. Use it before copying anything into [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] or [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]. After the row exists, use [[LLM/Study/Local LLM Benchmark Evidence Audit Runner|Local LLM Benchmark Evidence Audit Runner]] before that row supports comparison, tuning, result synthesis, or deployment.

The point is not to make a full benchmark suite. The point is to prevent a first local inference run from becoming scattered files that no longer answer: "what exactly ran, how fast did it feel, what token counts are known, what is missing, and what is the next controlled action?"

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| Client JSONL row | A reusable client call was attempted and logged. | A fair runtime comparison. |
| Streaming JSONL row | First event, TTFT, chunk count, final text, and stream errors were captured. | Quality or throughput under load. |
| Native Ollama response, optional | Runtime-native token and duration fields are available for that response. | That OpenAI-compatible and native routes are identical. |
| Generated benchmark JSON | The evidence can be parsed by another script. | The source data is complete. |
| Generated benchmark Markdown | The row can be copied into the benchmark log or capstone. | The model is good enough. |
| Missing-layer list | The next action is explicit instead of guessed. | The missing layer is fixed. |

The useful claim is narrow: "I can summarize one local run into a benchmark row without hiding missing token, native timing, quality, hardware, or security evidence."

## Required Inputs

| Input | Default path | Required |
|---|---|---|
| Non-streaming client log | `first-client-harness/client-runs.jsonl` | At least one client or streaming row is required. |
| Streaming timing log | `first-streaming-timing/streaming-runs.jsonl` | Required when the workload streams. |
| Native Ollama response JSON | `LOCAL_LLM_NATIVE_RESPONSE` | Optional; useful for load, prompt eval, and decode metrics. |
| Hardware boundary | `LOCAL_LLM_HARDWARE_BOUNDARY` | Required for a credible benchmark row. |
| Model artifact or quantization | `LOCAL_LLM_MODEL_ARTIFACT`, `LOCAL_LLM_QUANTIZATION` | Required before comparing models. |
| Cold/warm state | `LOCAL_LLM_COLD_OR_WARM` | Required before comparing latency. |
| Quality decision | `LOCAL_LLM_QUALITY_DECISION` | Required as `pass`, `hold`, or `fail` before calling a fast result useful. |
| Next action | `LOCAL_LLM_NEXT_ACTION` | Required before moving to another variable. |

If the model has not run yet, this note is still useful: it tells you which files the earlier runners need to produce before a benchmark row can be trusted.

## Standard-Library Builder

Save this as `first-benchmark-row.py` inside the run folder after the first client or streaming run.

```python
import json
import os
import time
from pathlib import Path


def env_path(name, default=None):
    value = os.environ.get(name)
    if value:
        return Path(value).expanduser().resolve()
    return default


def load_last_jsonl(path):
    if path is None:
        return None, "not_configured"
    if not path.exists():
        return None, "missing"
    last = None
    valid_count = 0
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            text = line.strip()
            if not text:
                continue
            try:
                last = json.loads(text)
                valid_count += 1
            except json.JSONDecodeError:
                continue
    if last is None:
        return None, "empty"
    return last, f"loaded:{valid_count}"


def load_json(path):
    if path is None:
        return None, "not_configured"
    if not path.exists():
        return None, "missing"
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list) and data:
        data = data[-1]
    return data, "loaded"


def first_value(*values):
    for value in values:
        if value not in (None, ""):
            return value
    return None


def as_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def ns_to_s(value):
    number = as_float(value)
    if number is None:
        return None
    return number / 1_000_000_000


def rate(count, seconds):
    count_f = as_float(count)
    seconds_f = as_float(seconds)
    if count_f is None or seconds_f is None or seconds_f <= 0:
        return None
    return count_f / seconds_f


def rounded(value, digits=3):
    number = as_float(value)
    if number is None:
        return None
    return round(number, digits)


def cell(value):
    if value in (None, ""):
        return ""
    return str(value).replace("|", "\\|")


def safe_name(value):
    text = str(value or "benchmark-row")
    return "".join(char if char.isalnum() or char in ("-", "_") else "-" for char in text)


RUN_ROOT = Path(os.environ.get("LOCAL_LLM_RUN_ROOT", ".")).resolve()
CLIENT_LOG = env_path("LOCAL_LLM_CLIENT_LOG", RUN_ROOT / "first-client-harness" / "client-runs.jsonl")
STREAM_LOG = env_path("LOCAL_LLM_STREAM_LOG", RUN_ROOT / "first-streaming-timing" / "streaming-runs.jsonl")
NATIVE_RESPONSE = env_path("LOCAL_LLM_NATIVE_RESPONSE")

OUTPUT_DIR = RUN_ROOT / "first-benchmark-row"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

client_row, client_status = load_last_jsonl(CLIENT_LOG)
stream_row, stream_status = load_last_jsonl(STREAM_LOG)
native_row, native_status = load_json(NATIVE_RESPONSE)

source = stream_row or client_row or {}
native_usage = native_row or {}
timestamp = time.strftime("%Y-%m-%dT%H:%M:%S%z")

prompt_tokens = first_value(
    source.get("prompt_tokens"),
    (client_row or {}).get("prompt_tokens"),
    native_usage.get("prompt_eval_count"),
)
output_tokens = first_value(
    source.get("output_tokens"),
    (client_row or {}).get("output_tokens"),
    native_usage.get("eval_count"),
)
total_latency_s = first_value(
    source.get("total_latency_s"),
    source.get("latency_s"),
    (client_row or {}).get("latency_s"),
    ns_to_s(native_usage.get("total_duration")),
)
ttft_s = first_value((stream_row or {}).get("ttft_s"), os.environ.get("LOCAL_LLM_TTFT_S"))
first_event_s = first_value((stream_row or {}).get("first_event_s"), os.environ.get("LOCAL_LLM_FIRST_EVENT_S"))

native_eval_s = ns_to_s(native_usage.get("eval_duration"))
native_prompt_s = ns_to_s(native_usage.get("prompt_eval_duration"))
native_total_s = ns_to_s(native_usage.get("total_duration"))
native_load_s = ns_to_s(native_usage.get("load_duration"))

client_output_tps = rate(output_tokens, total_latency_s)
native_eval_tps = rate(native_usage.get("eval_count"), native_eval_s)
native_prompt_tps = rate(native_usage.get("prompt_eval_count"), native_prompt_s)

quality_decision = os.environ.get("LOCAL_LLM_QUALITY_DECISION", "")
quality_status = quality_decision.strip().lower()
next_action = os.environ.get("LOCAL_LLM_NEXT_ACTION", "")

missing_layers = []
optional_gaps = []
if client_row is None:
    missing_layers.append("non-streaming client row")
if stream_row is None:
    missing_layers.append("streaming timing row")
if native_row is None:
    optional_gaps.append("native runtime timing row")
if prompt_tokens in (None, "") or output_tokens in (None, ""):
    missing_layers.append("token counts")
if not os.environ.get("LOCAL_LLM_HARDWARE_BOUNDARY"):
    missing_layers.append("hardware boundary")
if not quality_decision or quality_status == "pending":
    missing_layers.append("quality decision")
if not next_action:
    missing_layers.append("next controlled action")

status = "pass" if (client_row or stream_row) and not missing_layers else "hold"
if not (client_row or stream_row):
    status = "error"
    missing_layers.insert(0, "client or streaming source row")

run_id = first_value(
    source.get("run_id"),
    (client_row or {}).get("run_id"),
    (native_row or {}).get("created_at"),
    f"benchmark-{time.strftime('%Y%m%d-%H%M%S')}",
)

record = {
    "run_id": run_id,
    "timestamp": timestamp,
    "status": status,
    "source_status": {
        "client_log": client_status,
        "stream_log": stream_status,
        "native_response": native_status,
    },
    "runtime": first_value(source.get("runtime"), os.environ.get("LOCAL_LLM_RUNTIME")),
    "route": first_value(source.get("route"), os.environ.get("LOCAL_LLM_ROUTE")),
    "model_id": first_value(source.get("model_id"), native_usage.get("model"), os.environ.get("LOCAL_LLM_MODEL")),
    "model_artifact": os.environ.get("LOCAL_LLM_MODEL_ARTIFACT", ""),
    "quantization": os.environ.get("LOCAL_LLM_QUANTIZATION", ""),
    "hardware_boundary": os.environ.get("LOCAL_LLM_HARDWARE_BOUNDARY", ""),
    "cold_or_warm": os.environ.get("LOCAL_LLM_COLD_OR_WARM", ""),
    "prompt_id": first_value(source.get("prompt_id"), (client_row or {}).get("prompt_id")),
    "prompt_class": first_value(source.get("prompt_class"), (client_row or {}).get("prompt_class")),
    "stream": bool(stream_row),
    "prompt_tokens": prompt_tokens,
    "output_tokens": output_tokens,
    "first_event_s": rounded(first_event_s),
    "ttft_s": rounded(ttft_s),
    "total_latency_s": rounded(total_latency_s),
    "client_output_tokens_per_s": rounded(client_output_tps),
    "native_load_s": rounded(native_load_s),
    "native_prompt_eval_s": rounded(native_prompt_s),
    "native_eval_s": rounded(native_eval_s),
    "native_total_s": rounded(native_total_s),
    "native_prompt_tokens_per_s": rounded(native_prompt_tps),
    "native_eval_tokens_per_s": rounded(native_eval_tps),
    "peak_memory": os.environ.get("LOCAL_LLM_PEAK_MEMORY", ""),
    "quality_decision": quality_decision,
    "failed_or_missing_layer": ", ".join(missing_layers),
    "optional_gap": ", ".join(optional_gaps),
    "next_controlled_action": next_action,
    "client_log": str(CLIENT_LOG),
    "stream_log": str(STREAM_LOG),
    "native_response": str(NATIVE_RESPONSE) if NATIVE_RESPONSE else "",
}

safe_run_id = safe_name(run_id)
json_path = OUTPUT_DIR / f"{safe_run_id}-benchmark-row.json"
md_path = OUTPUT_DIR / f"{safe_run_id}-benchmark-row.md"
log_path = OUTPUT_DIR / "benchmark-rows.jsonl"

json_path.write_text(json.dumps(record, indent=2, ensure_ascii=True), encoding="utf-8")

table_fields = [
    ("Run id", record["run_id"]),
    ("Runtime and route", f"{cell(record['runtime'])} {cell(record['route'])}".strip()),
    ("Model id and artifact", f"{cell(record['model_id'])} {cell(record['model_artifact'])}".strip()),
    ("Quantization and offload", record["quantization"]),
    ("Hardware boundary", record["hardware_boundary"]),
    ("Cold or warm", record["cold_or_warm"]),
    ("Workload and prompt id", f"{cell(record['prompt_class'])} {cell(record['prompt_id'])}".strip()),
    ("Prompt tokens", record["prompt_tokens"]),
    ("Output tokens", record["output_tokens"]),
    ("First event seconds", record["first_event_s"]),
    ("TTFT seconds", record["ttft_s"]),
    ("Total latency seconds", record["total_latency_s"]),
    ("Client output tokens/sec", record["client_output_tokens_per_s"]),
    ("Native eval tokens/sec", record["native_eval_tokens_per_s"]),
    ("Peak RAM/VRAM", record["peak_memory"]),
    ("Quality pass/hold/fail", record["quality_decision"]),
    ("Failed or missing layer", record["failed_or_missing_layer"]),
    ("Optional gap", record["optional_gap"]),
    ("Next controlled action", record["next_controlled_action"]),
]

copy_headers = [
    "Run id",
    "Runtime",
    "Model",
    "Prompt id",
    "Stream",
    "Prompt tokens",
    "Output tokens",
    "TTFT",
    "Tokens/sec",
    "Total latency",
    "Quality decision",
    "Next action",
]
copy_values = [
    record["run_id"],
    record["runtime"],
    record["model_id"],
    record["prompt_id"],
    record["stream"],
    record["prompt_tokens"],
    record["output_tokens"],
    record["ttft_s"],
    first_value(record["native_eval_tokens_per_s"], record["client_output_tokens_per_s"]),
    record["total_latency_s"],
    record["quality_decision"],
    record["next_controlled_action"],
]

lines = [
    f"# First Benchmark Row - {record['run_id']}",
    "",
    f"Status: `{record['status']}`",
    "",
    "## Field Row",
    "",
    "| Field | Value |",
    "|---|---|",
]
for key, value in table_fields:
    lines.append(f"| {cell(key)} | {cell(value)} |")

lines.extend([
    "",
    "## Copy Row",
    "",
    "| " + " | ".join(copy_headers) + " |",
    "| " + " | ".join(["---"] * len(copy_headers)) + " |",
    "| " + " | ".join(cell(value) for value in copy_values) + " |",
    "",
    "## Source Files",
    "",
    f"- Client log: `{cell(record['client_log'])}` ({client_status})",
    f"- Streaming log: `{cell(record['stream_log'])}` ({stream_status})",
    f"- Native response: `{cell(record['native_response'])}` ({native_status})",
])

md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

with log_path.open("a", encoding="utf-8") as handle:
    handle.write(json.dumps(record, ensure_ascii=True) + "\n")

print(json.dumps({"status": status, "json_path": str(json_path), "markdown_path": str(md_path)}, indent=2))
```

PowerShell run:

```powershell
$env:LOCAL_LLM_RUN_ROOT = "<paste-run-folder-path>"
$env:LOCAL_LLM_HARDWARE_BOUNDARY = "Windows native / RTX 3080 Ti / loopback"
$env:LOCAL_LLM_MODEL_ARTIFACT = "<model tag or file>"
$env:LOCAL_LLM_QUANTIZATION = "<quantization or runtime tag>"
$env:LOCAL_LLM_COLD_OR_WARM = "cold / warm"
$env:LOCAL_LLM_QUALITY_DECISION = "pass / hold / fail"
$env:LOCAL_LLM_NEXT_ACTION = "<one controlled next action>"
python .\first-benchmark-row.py
```

If you also saved an Ollama native response JSON:

```powershell
$env:LOCAL_LLM_NATIVE_RESPONSE = "<path-to-native-response.json>"
python .\first-benchmark-row.py
```

Pass signal: the script writes `first-benchmark-row\benchmark-rows.jsonl`, one benchmark JSON file, and one benchmark Markdown file. A `hold` row is acceptable for the first run if it names exactly what is missing.

## How To Interpret The Row

| If the row says | Meaning | Next route |
|---|---|---|
| `status=pass` | Enough timing, token, hardware, quality, and next-action fields exist for a first benchmark row. | Copy to [[LLM/Study/Local LLM Inference Benchmark Log]] or capstone evidence. |
| `status=hold` with missing token counts | The endpoint ran, but token-normalized speed is incomplete. | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]] or native runtime response. |
| `status=hold` with missing streaming row | Total latency exists, but perceived latency is not proven. | [[LLM/Study/Local LLM First Streaming Timing Runner]] |
| `status=hold` with missing quality decision | The model may be fast, but usefulness is unproven. | [[LLM/Study/Local LLM First Quality Probe Suite]], [[LLM/Study/Local LLM First Quality Probe Runner]], or [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| `status=error` | No client or streaming source row was found. | [[LLM/Study/Local LLM First Client Harness Runner]] |

Do not compare two runs unless both rows name prompt id, route, model artifact, sampler/output cap, hardware boundary, cold/warm state, and quality decision.

## Completion Gate

This first benchmark-row builder is complete only when:

- [ ] one client or streaming JSONL row exists
- [ ] the builder script path is recorded
- [ ] benchmark JSON, benchmark Markdown, and benchmark JSONL files are created
- [ ] token counts are present or explicitly missing
- [ ] TTFT is present when the workload streams, or streaming is marked unsupported/not required
- [ ] native runtime timing is present or explicitly missing
- [ ] hardware boundary, model artifact, quantization/offload, cold/warm state, quality decision, and next action are filled
- [ ] the row is copied to [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] or linked from [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]

## References

Internal routes:

- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/Local LLM First Streaming Timing Runner]]
- [[LLM/Study/Decoding and Sampling Controls Runner]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/Local LLM Benchmark Evidence Audit Runner]]
- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM Command Cookbook]]
- [[LLM/Study/Local LLM First Quality Probe Suite]]
- [[LLM/Study/Local LLM First Quality Probe Runner]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]

External/current sources checked 2026-06-15:

- [Ollama usage metrics](https://docs.ollama.com/api/usage)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
- [Ollama streaming](https://docs.ollama.com/capabilities/streaming)
- [OpenAI streaming responses guide](https://developers.openai.com/api/docs/guides/streaming-responses)
