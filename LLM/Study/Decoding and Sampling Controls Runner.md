---
tags: [study, llm, inference, local-llm, decoding, sampling, controls, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [core, practice]
last-verified: 2026-06-15
---

# Decoding and Sampling Controls Runner

> **One-line summary** Run a repeatable local sampler-control probe for baseline decoding, temperature, seed repeatability, stop strings, and output caps before comparing local LLM quality or speed.

Use this after [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]] explains the mechanisms and after [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner|Local LLM OpenAI-Compatible API Contract Runner]] or [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] proves the `/v1/chat/completions` route. Use the result before [[LLM/Study/Local LLM First Benchmark Row Builder|Local LLM First Benchmark Row Builder]], [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]], and [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] whenever two runs must be compared fairly.

This runner sends real local inference requests when pointed at an actual endpoint. Do not run it until the base URL, model id, boundary, and evidence folder are fixed. For verification or dry runs, point `LOCAL_LLM_BASE_URL` at a fake loopback fixture server.

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| Saved baseline request and response | The route can run a low-temperature, capped decoding baseline. | Workload quality. |
| Temperature probe | The request records the control that changes the logits-to-token distribution. | That one sample captures the full distribution. |
| Seed repeatability probe | The endpoint can or cannot reproduce the same output under a fixed seed. | Determinism across runtime upgrades or GPU kernels. |
| Stop-string probe | The endpoint can or cannot enforce a requested generation boundary. | Correct chat-template EOS behavior. |
| Output-cap probe | The endpoint records max-token behavior and finish reason when available. | A full context-budget proof. |
| JSON/CSV/Markdown/JSONL output | Sampler settings can be joined with benchmark, quality, and capstone evidence. | Production observability. |

Academic bridge: temperature rescales logits, filters such as top-p change the candidate set, penalties alter logits before sampling, seed controls the sampler RNG only when the runtime honors it, and stop rules terminate the decode loop after detokenization. This runner makes those mechanisms visible as local endpoint evidence.

## Fixed Conditions

Write these before running:

| Field | Value |
|---|---|
| Run folder |  |
| API contract runner result |  |
| Runtime | Ollama / LM Studio / llama.cpp / vLLM / SGLang / other |
| Base URL | `http://127.0.0.1:11434/v1` for Ollama compatibility mode |
| Model id |  |
| Boundary | loopback / LAN / tunnel / remote |
| Baseline temperature | `0` |
| Baseline top-p | `1` |
| Seed probe | on / off |
| Stop probe | on / off |
| Cap probe | on / off |
| Next gate | benchmark row / quality harness / prompt diagnosis / contract diagnosis |

If the endpoint is exposed beyond loopback, complete [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] first.

## Standard-Library Runner

Save this as `decoding-sampling-controls-runner.py` inside the run folder. It uses only Python's standard library.

```python
import csv
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


def response_error_text(result):
    data = result.get("json") if isinstance(result, dict) else None
    if isinstance(data, dict):
        error = data.get("error")
        if isinstance(error, dict):
            return str(error.get("message") or error.get("type") or error)
        if error:
            return str(error)
    return str(result.get("error") or result.get("error_class") or result.get("raw_excerpt") or "")


def post_json(url, body, timeout_s, headers):
    payload = json.dumps(body).encode("utf-8")
    request_headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    request_headers.update(headers)
    request = urllib.request.Request(url, data=payload, headers=request_headers, method="POST")
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
            "status": "error",
            "elapsed_s": round(elapsed_s, 3),
            "error_class": type(exc).__name__,
            "error": str(exc),
        }


def build_body(prompt, *, temperature, top_p, max_tokens, seed=None, stop=None):
    body = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Follow the requested output exactly."},
            {"role": "user", "content": prompt},
        ],
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": max_tokens,
        "stream": False,
    }
    if seed is not None:
        body["seed"] = seed
    if stop:
        body["stop"] = stop
    return body


def run_probe(probe_id, label, body, check):
    request_path = REQUEST_DIR / f"{run_id}-{probe_id}-request.json"
    response_path = RESPONSE_DIR / f"{run_id}-{probe_id}-response.json"
    output_path = OUTPUT_DIR / f"{run_id}-{probe_id}-output.txt"

    write_json(request_path, body)
    result = post_json(CHAT_URL, body, TIMEOUT_S, HEADERS)
    write_json(response_path, result)

    data = result.get("json") if isinstance(result.get("json"), dict) else {}
    text = extract_chat_text(data)
    finish_reason = extract_finish_reason(data)
    write_text(output_path, text)

    if result["status"] != "pass":
        decision = "error"
        note = response_error_text(result)
    else:
        decision, note = check(text, finish_reason, data)

    row = {
        "probe_id": probe_id,
        "label": label,
        "decision": decision,
        "note": note,
        "request_path": str(request_path),
        "response_path": str(response_path),
        "output_path": str(output_path),
        "http_status": result.get("http_status"),
        "elapsed_s": result.get("elapsed_s"),
        "temperature": body.get("temperature"),
        "top_p": body.get("top_p"),
        "seed": body.get("seed"),
        "stop": body.get("stop"),
        "max_tokens": body.get("max_tokens"),
        "finish_reason": finish_reason,
        "output_text": text,
        "output_excerpt": " ".join(text.split())[:220],
        "usage": data.get("usage") if isinstance(data.get("usage"), dict) else {},
        "error": response_error_text(result) if decision == "error" else "",
    }
    return row


def check_baseline(text, finish_reason, data):
    if normalize_text(text) == normalize_text(BASELINE_EXPECTED):
        return "pass", "baseline exact output matched"
    if text.strip():
        return "hold", "baseline route worked but output did not match the fixed prompt"
    return "hold", "baseline route returned no assistant text"


def check_temperature(text, finish_reason, data):
    if text.strip():
        return "pass", "temperature probe output captured"
    return "hold", "temperature probe returned no assistant text"


def check_stop(text, finish_reason, data):
    normalized = normalize_text(text)
    if not text.strip():
        return "hold", "stop probe returned no assistant text"
    if normalize_text(STOP_STRING) in normalized:
        return "hold", "stop string appeared in the output"
    if finish_reason == "stop":
        return "pass", "stop string absent and finish_reason=stop"
    return "pass", "stop string absent; finish_reason not reported as stop"


def check_cap(text, finish_reason, data):
    if not text.strip():
        return "hold", "cap probe returned no assistant text"
    if finish_reason == "length":
        return "pass", "finish_reason=length captured"
    return "pass", "output cap request captured; runtime did not report length"


def write_csv(path, rows):
    fields = [
        "probe_id",
        "label",
        "decision",
        "note",
        "temperature",
        "top_p",
        "seed",
        "stop",
        "max_tokens",
        "finish_reason",
        "http_status",
        "elapsed_s",
        "output_excerpt",
        "request_path",
        "response_path",
        "output_path",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def write_markdown(path, record):
    lines = [
        f"# Decoding Controls - {record['run_id']}",
        "",
        f"Status: `{record['status']}`",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Runtime | {md_cell(record['runtime'])} |",
        f"| Base URL | {md_cell(record['base_url'])} |",
        f"| Model | {md_cell(record['model'])} |",
        f"| Boundary | {md_cell(record['boundary'])} |",
        f"| Baseline expected | {md_cell(record['baseline_expected'])} |",
        f"| Missing layers | {md_cell(', '.join(record['missing_layers']))} |",
        f"| Next action | {md_cell(record['next_action'])} |",
        "",
        "## Probe Summary",
        "",
        "| Probe | Decision | Controls | Finish | Note |",
        "|---|---|---|---|---|",
    ]
    for row in record["rows"]:
        controls = {
            "temperature": row.get("temperature"),
            "top_p": row.get("top_p"),
            "seed": row.get("seed"),
            "stop": row.get("stop"),
            "max_tokens": row.get("max_tokens"),
        }
        lines.append(
            f"| {md_cell(row['label'])} | {md_cell(row['decision'])} | "
            f"{md_cell(controls)} | {md_cell(row.get('finish_reason'))} | {md_cell(row.get('note'))} |"
        )
    lines.extend([
        "",
        "## Outputs",
        "",
    ])
    for row in record["rows"]:
        lines.extend([
            f"### {row['label']}",
            "",
            "```text",
            row.get("output_text", ""),
            "```",
            "",
        ])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


RUN_ROOT = Path(os.environ.get("LOCAL_LLM_RUN_ROOT", ".")).expanduser().resolve()
RUNTIME = os.environ.get("LOCAL_LLM_RUNTIME", "openai-compatible-local")
BASE_URL = os.environ.get("LOCAL_LLM_BASE_URL", "http://127.0.0.1:11434/v1").rstrip("/")
MODEL = os.environ.get("LOCAL_LLM_MODEL", "<served-model-id>")
API_KEY = os.environ.get("LOCAL_LLM_API_KEY", "local")
BOUNDARY = os.environ.get("LOCAL_LLM_BOUNDARY", "loopback or recorded boundary")
TIMEOUT_S = float(os.environ.get("LOCAL_LLM_TIMEOUT_S", "60"))
BASELINE_EXPECTED = os.environ.get("LOCAL_LLM_BASELINE_EXPECTED", "sampler baseline ok")
BASELINE_TOP_P = float(os.environ.get("LOCAL_LLM_BASELINE_TOP_P", "1"))
BASELINE_MAX_TOKENS = int(os.environ.get("LOCAL_LLM_BASELINE_MAX_TOKENS", "32"))
WARM_TEMPERATURE = float(os.environ.get("LOCAL_LLM_WARM_TEMPERATURE", "0.8"))
WARM_TOP_P = float(os.environ.get("LOCAL_LLM_WARM_TOP_P", "0.95"))
SEED_VALUE = int(os.environ.get("LOCAL_LLM_SEED", "42"))
RUN_SEED = env_bool("LOCAL_LLM_RUN_SEED", True)
RUN_STOP = env_bool("LOCAL_LLM_RUN_STOP", True)
RUN_CAP = env_bool("LOCAL_LLM_RUN_CAP", True)
STOP_STRING = os.environ.get("LOCAL_LLM_STOP_STRING", "END")
CAP_MAX_TOKENS = int(os.environ.get("LOCAL_LLM_CAP_MAX_TOKENS", "4"))

OUT_DIR = RUN_ROOT / "decoding-sampling-controls-runner"
REQUEST_DIR = OUT_DIR / "requests"
RESPONSE_DIR = OUT_DIR / "responses"
OUTPUT_DIR = OUT_DIR / "outputs"
for directory in (REQUEST_DIR, RESPONSE_DIR, OUTPUT_DIR):
    directory.mkdir(parents=True, exist_ok=True)

run_id = f"{time.strftime('%Y%m%d-%H%M%S')}-decoding-controls"
timestamp = time.strftime("%Y-%m-%dT%H:%M:%S%z")
HEADERS = {"Authorization": f"Bearer {API_KEY}"}
CHAT_URL = join_url(BASE_URL, "/chat/completions")

rows = []

baseline_prompt = f"Reply with exactly: {BASELINE_EXPECTED}"
rows.append(run_probe(
    "baseline",
    "Baseline low-temperature decode",
    build_body(baseline_prompt, temperature=0, top_p=BASELINE_TOP_P, max_tokens=BASELINE_MAX_TOKENS),
    check_baseline,
))

temperature_prompt = "Return one short sentence naming two colors. Do not explain."
rows.append(run_probe(
    "temperature",
    "Temperature probe",
    build_body(temperature_prompt, temperature=WARM_TEMPERATURE, top_p=WARM_TOP_P, max_tokens=BASELINE_MAX_TOKENS),
    check_temperature,
))

if RUN_SEED:
    seed_prompt = "Seed repeatability probe. Return a short phrase."
    seed_body = build_body(seed_prompt, temperature=WARM_TEMPERATURE, top_p=WARM_TOP_P, max_tokens=BASELINE_MAX_TOKENS, seed=SEED_VALUE)
    first_seed = run_probe("seed-a", "Seed repeatability A", seed_body, check_temperature)
    second_seed = run_probe("seed-b", "Seed repeatability B", seed_body, check_temperature)
    if first_seed["decision"] == "pass" and second_seed["decision"] == "pass":
        if normalize_text(first_seed["output_text"]) == normalize_text(second_seed["output_text"]):
            first_seed["note"] = "seeded run A matched run B"
            second_seed["note"] = "seeded run B matched run A"
        else:
            first_seed["decision"] = "hold"
            second_seed["decision"] = "hold"
            first_seed["note"] = "same seed produced different output from run B"
            second_seed["note"] = "same seed produced different output from run A"
    rows.extend([first_seed, second_seed])

if RUN_STOP:
    stop_prompt = f'Return the text "alpha {STOP_STRING} beta".'
    rows.append(run_probe(
        "stop",
        "Stop-string boundary",
        build_body(stop_prompt, temperature=0, top_p=BASELINE_TOP_P, max_tokens=BASELINE_MAX_TOKENS, stop=[STOP_STRING]),
        check_stop,
    ))

if RUN_CAP:
    cap_prompt = "Count from one to ten as lowercase English words separated by spaces."
    rows.append(run_probe(
        "cap",
        "Output-cap boundary",
        build_body(cap_prompt, temperature=0, top_p=BASELINE_TOP_P, max_tokens=CAP_MAX_TOKENS),
        check_cap,
    ))

missing_layers = []
for row in rows:
    if row["decision"] == "error":
        missing_layers.append(f"{row['probe_id']} route error")
    elif row["decision"] == "hold":
        missing_layers.append(f"{row['probe_id']} control needs review")

if any(row["decision"] == "error" for row in rows):
    status = "error"
    next_action = "route to API contract or troubleshooting before sampler comparison"
elif missing_layers:
    status = "hold"
    next_action = "review sampler controls before benchmark or quality comparison"
else:
    status = "pass"
    next_action = "feed sampler settings into benchmark row builder or quality harness"

record = {
    "run_id": run_id,
    "timestamp": timestamp,
    "status": status,
    "runtime": RUNTIME,
    "base_url": BASE_URL,
    "model": MODEL,
    "boundary": BOUNDARY,
    "baseline_expected": BASELINE_EXPECTED,
    "run_seed": RUN_SEED,
    "run_stop": RUN_STOP,
    "run_cap": RUN_CAP,
    "missing_layers": missing_layers,
    "next_action": next_action,
    "rows": rows,
}

summary_json_path = OUT_DIR / f"{run_id}-controls-results.json"
summary_md_path = OUT_DIR / f"{run_id}-controls-results.md"
summary_csv_path = OUT_DIR / f"{run_id}-controls-results.csv"
jsonl_path = OUT_DIR / "decoding-control-runs.jsonl"
write_json(summary_json_path, record)
write_markdown(summary_md_path, record)
write_csv(summary_csv_path, rows)
append_jsonl(jsonl_path, record)

print(json.dumps({
    "status": status,
    "run_id": run_id,
    "results_json": str(summary_json_path),
    "results_md": str(summary_md_path),
    "results_csv": str(summary_csv_path),
    "jsonl": str(jsonl_path),
    "missing_layers": missing_layers,
    "next_action": next_action,
}, indent=2, ensure_ascii=True))
```

## PowerShell Execution

Use a disposable evidence folder first:

```powershell
$env:LOCAL_LLM_RUN_ROOT = "D:\LLM-Runs\decoding-$(Get-Date -Format yyyyMMdd-HHmmss)"
$env:LOCAL_LLM_BASE_URL = "http://127.0.0.1:11434/v1"
$env:LOCAL_LLM_MODEL = "<served-model-id>"
$env:LOCAL_LLM_API_KEY = "local"
$env:LOCAL_LLM_BOUNDARY = "loopback"
$env:LOCAL_LLM_RUN_SEED = "1"
$env:LOCAL_LLM_RUN_STOP = "1"
$env:LOCAL_LLM_RUN_CAP = "1"
python .\decoding-sampling-controls-runner.py
```

If a runtime does not support seed or stop fields, turn off only that probe and record the reason:

```powershell
$env:LOCAL_LLM_RUN_SEED = "0"
$env:LOCAL_LLM_RUN_STOP = "0"
```

Do not compare model quality after changing prompt, sampler, output cap, context, and runtime at the same time. Change one layer, save one row, and write the decision.

## Result Interpretation

| Runner status | Meaning | Next route |
|---|---|---|
| `pass` | Baseline, temperature capture, enabled seed probe, enabled stop probe, and enabled cap probe produced usable evidence. | [[LLM/Study/Local LLM First Benchmark Row Builder]] |
| `hold` | Requests reached the endpoint, but at least one control behaved unexpectedly or needs human review. | [[LLM/Study/Decoding and Sampling Controls Lab]] |
| `error` | At least one required request failed at the route or response-shape layer. | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]] or [[LLM/Study/Local LLM Troubleshooting Decision Tree]] |

Treat a seed mismatch as important, not surprising. Some local stacks do not guarantee byte-identical output across backends, kernels, quantization modes, or runtime versions even when a `seed` field is accepted.

Treat a stop-string leak as a boundary bug. It can break extraction, JSON, tool loops, and code generation even when the response looks semantically correct.

## Completion Gate

This runner pass is complete when you have:

- [ ] a saved `controls-results.json`
- [ ] a saved `controls-results.md`
- [ ] a saved `controls-results.csv`
- [ ] one appended `decoding-control-runs.jsonl` row
- [ ] a baseline low-temperature request and response
- [ ] a temperature probe row
- [ ] a seed repeatability decision or explicit skipped reason
- [ ] a stop-string decision or explicit skipped reason
- [ ] an output-cap decision or explicit skipped reason
- [ ] a next action routed to benchmark row builder, quality harness, contract diagnosis, or troubleshooting

## References

Internal routes:

- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]]
- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/Local LLM First Benchmark Row Builder]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]

External/current docs checked 2026-06-15:

- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
- [Ollama Modelfile reference](https://docs.ollama.com/modelfile)
- [OpenAI chat completions API reference](https://platform.openai.com/docs/api-reference/chat/create)
- [Hugging Face generation parameters](https://huggingface.co/docs/transformers/en/main_classes/text_generation)
