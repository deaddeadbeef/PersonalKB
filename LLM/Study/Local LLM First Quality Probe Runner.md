---
tags: [study, llm, evaluation, local-llm, ollama, quality, inference, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM First Quality Probe Runner

> **One-line summary** After endpoint evidence passes, run the first five private quality probes through a local Ollama chat endpoint and save request, response, output, score, CSV, Markdown, and JSONL evidence.

Use this after [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner|Local LLM First Endpoint Evidence Audit Runner]] says the first endpoint run folder is ready. That audit now requires pass-state debrief and template/tokenizer compatibility, so this runner starts from a defensible endpoint instead of probing quality on top of a partial route proof. The manual [[LLM/Study/Local LLM First Quality Probe Suite|Local LLM First Quality Probe Suite]] defines the probe set and scoring intent. This runner turns that suite into repeatable Python evidence.

This runner sends real local inference requests when you run it against an actual endpoint. Do not run it until the model id, endpoint boundary, sampler, evidence folder, and first endpoint evidence audit are fixed. For verification or dry runs, point `LOCAL_LLM_BASE_URL` at a fake local fixture server instead of Ollama.

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| Endpoint audit JSON | The first endpoint passed run-card, preflight, runtime, smoke, debrief, template/tokenizer, and decision gates before quality probing. | That the endpoint remains healthy forever. |
| Five saved request bodies | The prompt suite, sampler, model id, and route are reproducible. | Workload coverage. |
| Five saved response bodies | The local endpoint handled the suite. | That the model is good enough for real use. |
| Output text files | Assistant content can be inspected outside the terminal. | Correctness by itself. |
| Auto checks | Arithmetic, JSON, extraction, refusal, and constraint signals can be triaged quickly. | Final human quality judgment. |
| Results JSON/CSV/Markdown | Probe rows can feed the full quality harness and capstone workbook. | Stable benchmark ranking. |
| JSONL row | This run can join the later benchmark and client logs. | Production observability. |

Academic bridge: this runner separates endpoint proof from quality evidence. The probes map to factuality, constrained generation, context grounding, calibrated refusal, and instruction following. Those are evaluation dimensions, not the same thing as loss, perplexity, latency, or memory.

## Fixed Conditions

Write these before running:

| Field | Value |
|---|---|
| Run folder |  |
| First endpoint evidence audit |  |
| First response debrief |  |
| Runtime | Ollama native `/api/chat` |
| Base URL | `http://127.0.0.1:11434` |
| Model id |  |
| Temperature | `0` |
| Output cap | `256` |
| Route boundary | loopback / exposed / unclear |
| Scorer | script-assisted plus human review |
| Next gate | full quality harness / client harness / troubleshooting |

Do not compare two models or runtimes with this runner unless the prompt set, sampler, max tokens, endpoint route, context, and scoring rules are unchanged.

## Standard-Library Runner

Save this as `first-quality-probe-runner.py` inside the run folder.

```python
import csv
import json
import os
import re
import time
import urllib.error
import urllib.request
from pathlib import Path


RUN_ROOT = Path(os.environ.get("LOCAL_LLM_RUN_ROOT", ".")).expanduser().resolve()
BASE_URL = os.environ.get("LOCAL_LLM_BASE_URL", "http://127.0.0.1:11434").rstrip("/")
ROUTE = os.environ.get("LOCAL_LLM_ROUTE", "/api/chat")
MODEL = os.environ.get("LOCAL_LLM_MODEL", "<served-model-id>")
BOUNDARY = os.environ.get("LOCAL_LLM_BOUNDARY", "loopback or recorded boundary")
TEMPERATURE = float(os.environ.get("LOCAL_LLM_TEMPERATURE", "0"))
MAX_TOKENS = int(os.environ.get("LOCAL_LLM_MAX_TOKENS", "256"))
TIMEOUT_S = float(os.environ.get("LOCAL_LLM_TIMEOUT_S", "90"))
EXTRACTION_MODEL_TEXT = os.environ.get("LOCAL_LLM_EXTRACT_MODEL_TEXT", "qwen3.5:4b")
ENDPOINT_AUDIT_JSON = os.environ.get("LOCAL_LLM_ENDPOINT_AUDIT_JSON")

SUITE_DIR = RUN_ROOT / "first-quality-probe-runner"
REQUEST_DIR = SUITE_DIR / "requests"
RESPONSE_DIR = SUITE_DIR / "responses"
OUTPUT_DIR = SUITE_DIR / "outputs"
for directory in (REQUEST_DIR, RESPONSE_DIR, OUTPUT_DIR):
    directory.mkdir(parents=True, exist_ok=True)


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def md_cell(value):
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True)
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def normalize(value):
    return " ".join(str(value or "").strip().lower().split())


def bool_env(name, default):
    value = os.environ.get(name)
    if value is None:
        return default
    return normalize(value) not in {"0", "false", "no", "off", "skip", "skipped"}


def resolve_path(value, base):
    if not value:
        return None
    path = Path(str(value)).expanduser()
    if not path.is_absolute():
        path = base / path
    return path.resolve()


def latest_file(root, pattern):
    if not root.exists():
        return None
    files = [path for path in root.glob(pattern) if path.is_file()]
    if not files:
        return None
    return sorted(files, key=lambda item: item.stat().st_mtime, reverse=True)[0]


def read_json(path):
    if not path:
        return None, "path not set"
    try:
        return json.loads(path.read_text(encoding="utf-8-sig")), None
    except FileNotFoundError:
        return None, f"missing file: {path}"
    except json.JSONDecodeError as exc:
        return None, f"invalid json: {path}: {exc}"


def endpoint_audit_path():
    path = resolve_path(ENDPOINT_AUDIT_JSON, RUN_ROOT)
    if path:
        return path
    for pattern in [
        "first-endpoint-evidence-audit/*/*first-endpoint-evidence-audit.json",
        "first-endpoint-evidence-audit/*first-endpoint-evidence-audit.json",
        "*/*first-endpoint-evidence-audit.json",
        "*first-endpoint-evidence-audit.json",
    ]:
        path = latest_file(RUN_ROOT, pattern)
        if path:
            return path
    return None


def endpoint_audit_status(path):
    data, error = read_json(path)
    if error:
        return {
            "path": str(path) if path else "",
            "status": "hold",
            "decision": "endpoint_audit_missing",
            "gate_count": 0,
            "pass_count": 0,
            "hold_count": 0,
            "fail_count": 0,
            "missing_layer": "first endpoint evidence audit",
            "block_reason": error,
        }
    if not isinstance(data, dict):
        return {
            "path": str(path),
            "status": "hold",
            "decision": "endpoint_audit_unreadable",
            "gate_count": 0,
            "pass_count": 0,
            "hold_count": 0,
            "fail_count": 0,
            "missing_layer": "first endpoint evidence audit",
            "block_reason": "endpoint audit JSON is not an object",
        }
    status = normalize(data.get("status"))
    decision = str(data.get("decision") or "")
    return {
        "path": str(path),
        "status": status,
        "decision": decision,
        "gate_count": data.get("gate_count"),
        "pass_count": data.get("pass_count"),
        "hold_count": data.get("hold_count"),
        "fail_count": data.get("fail_count"),
        "missing_layer": "" if status == "pass" else "first endpoint evidence audit",
        "block_reason": "" if status == "pass" else f"endpoint audit status is {status or 'missing'}",
    }


def response_text(data):
    message = data.get("message") if isinstance(data.get("message"), dict) else {}
    content = message.get("content", "")
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict):
                parts.append(str(item.get("text") or item.get("content") or ""))
            else:
                parts.append(str(item))
        return " ".join(part for part in parts if part)
    return str(content or data.get("response") or "")


def word_count(text):
    return len(re.findall(r"[A-Za-z0-9']+", text))


def bullet_lines(text):
    return [line.strip() for line in str(text).splitlines() if line.strip().startswith(("-", "*"))]


def ns_to_seconds(value):
    if value is None or isinstance(value, bool):
        return None
    try:
        return round(float(value) / 1_000_000_000, 3)
    except (TypeError, ValueError):
        return None


def post_json(url, body):
    payload = json.dumps(body).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=payload,
        headers={"Accept": "application/json", "Content-Type": "application/json"},
        method="POST",
    )
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_S) as response:
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
                "raw_excerpt": " ".join(raw.split())[:500],
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
            "raw_excerpt": " ".join(raw.split())[:500],
        }
    except Exception as exc:
        elapsed_s = time.perf_counter() - started
        return {
            "status": "error",
            "elapsed_s": round(elapsed_s, 3),
            "error_class": type(exc).__name__,
            "error": str(exc),
        }


def check_known_answer(text):
    normalized = normalize(text)
    return "answer=410" in normalized


def check_structured_json(text):
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        return False, "invalid json"
    if not isinstance(parsed, dict):
        return False, "json parsed but top-level value is not an object"
    tokens = parsed.get("tokens")
    seconds = parsed.get("seconds")
    rate = parsed.get("tokens_per_second")
    try:
        numeric_rate = float(rate)
    except (TypeError, ValueError):
        return False, "json parsed but tokens_per_second is not numeric"
    if tokens == 128 and seconds == 4 and numeric_rate == 32.0:
        return True, "valid json and expected rate"
    return False, "json parsed but expected values differ"


def check_extraction(text):
    normalized = normalize(text)
    has_supplied = all(value.lower() in normalized for value in ["127.0.0.1", EXTRACTION_MODEL_TEXT.lower(), "D:\\LLM-Runs\\first".lower()])
    invented_gpu = "gpu" in normalized or "rtx" in normalized or "cuda" in normalized
    return has_supplied and not invented_gpu


def check_grounded_refusal(text):
    return normalize(text) == "not enough evidence"


def check_constraint(text):
    lines = bullet_lines(text)
    if len(lines) != 2:
        return False
    return all(word_count(line.lstrip("-* ").strip()) == 5 for line in lines)


RESULT_FIELDNAMES = [
    "run_id",
    "timestamp",
    "prompt_id",
    "task_class",
    "model",
    "base_url",
    "route",
    "boundary",
    "temperature",
    "max_tokens",
    "request_path",
    "response_path",
    "output_path",
    "route_status",
    "http_status",
    "elapsed_s",
    "total_seconds",
    "prompt_eval_count",
    "eval_count",
    "done",
    "done_reason",
    "expected_signal",
    "auto_decision",
    "auto_note",
    "human_score",
    "human_decision",
    "failure_owner",
    "response_excerpt",
]


CASES = [
    {
        "id": "K-01",
        "task_class": "known-answer arithmetic",
        "system": "Answer the user exactly. Keep reasoning to one short sentence.",
        "user": "Compute 17 * 23 + 19. Return exactly: answer=<number>; reason=<one short sentence>.",
        "format": None,
        "expected_signal": "answer=410",
        "check": check_known_answer,
    },
    {
        "id": "S-01",
        "task_class": "structured output",
        "system": "Return only valid JSON. Do not wrap it in markdown.",
        "user": "A local model produced 128 output tokens in 4 seconds. Return JSON with keys \"tokens\", \"seconds\", \"tokens_per_second\", and \"caveat\".",
        "format": "json",
        "expected_signal": "valid JSON; tokens_per_second=32",
        "check": check_structured_json,
    },
    {
        "id": "X-01",
        "task_class": "extraction",
        "system": "Use only the provided text. Do not add facts.",
        "user": f"Text: \"The local server is bound to 127.0.0.1, the selected model is {EXTRACTION_MODEL_TEXT}, and the run folder is D:\\LLM-Runs\\first.\" Extract server, model, and run_folder as a three-row markdown table. Do not add facts.",
        "format": None,
        "expected_signal": "only supplied server, model, and run_folder",
        "check": check_extraction,
    },
    {
        "id": "G-01",
        "task_class": "grounded refusal",
        "system": "Use only the supplied text. If the answer is absent, follow the requested refusal string exactly.",
        "user": f"Using only this text: \"The model tag is {EXTRACTION_MODEL_TEXT}.\" What GPU is being used? If the answer is not present, say exactly: not enough evidence.",
        "format": None,
        "expected_signal": "not enough evidence",
        "check": check_grounded_refusal,
    },
    {
        "id": "C-01",
        "task_class": "constraint following",
        "system": "Follow the format constraints exactly.",
        "user": "Give two bullet points. Each bullet must have exactly five words. Topic: why route proof is not quality proof.",
        "format": None,
        "expected_signal": "two bullets, five words each",
        "check": check_constraint,
    },
]

run_id = f"{time.strftime('%Y%m%d-%H%M%S')}-first-quality-probe"
timestamp = time.strftime("%Y-%m-%dT%H:%M:%S%z")
url = f"{BASE_URL}{ROUTE if ROUTE.startswith('/') else '/' + ROUTE}"
require_endpoint_audit = bool_env("LOCAL_LLM_REQUIRE_ENDPOINT_AUDIT", True)
endpoint_audit = endpoint_audit_status(endpoint_audit_path())
if not require_endpoint_audit:
    endpoint_audit = {
        "path": "",
        "status": "skipped",
        "decision": "endpoint_audit_not_required",
        "gate_count": 0,
        "pass_count": 0,
        "hold_count": 0,
        "fail_count": 0,
        "missing_layer": "",
        "block_reason": "",
    }
endpoint_audit_ready = endpoint_audit["status"] == "pass"

serializable_cases = [{key: value for key, value in case.items() if key != "check"} for case in CASES]
write_json(SUITE_DIR / "quality-probe-cases.json", serializable_cases)

rows = []
if require_endpoint_audit and not endpoint_audit_ready:
    status = "hold"
else:
    status = ""

for case in ([] if status == "hold" else CASES):
    request_body = {
        "model": MODEL,
        "stream": False,
        "messages": [
            {"role": "system", "content": case["system"]},
            {"role": "user", "content": case["user"]},
        ],
        "options": {
            "temperature": TEMPERATURE,
            "num_predict": MAX_TOKENS,
        },
    }
    if case["format"]:
        request_body["format"] = case["format"]

    request_path = REQUEST_DIR / f"{run_id}-{case['id']}-request.json"
    response_path = RESPONSE_DIR / f"{run_id}-{case['id']}-response.json"
    output_path = OUTPUT_DIR / f"{run_id}-{case['id']}-output.txt"

    write_json(request_path, request_body)
    result = post_json(url, request_body)
    write_json(response_path, result)

    body = result.get("json") if isinstance(result.get("json"), dict) else {}
    text = response_text(body) if result["status"] == "pass" else ""
    output_path.write_text(text + "\n", encoding="utf-8")

    if result["status"] != "pass":
        auto_pass = False
        auto_note = result.get("error") or result.get("error_class") or "route error"
    else:
        check_result = case["check"](text)
        if isinstance(check_result, tuple):
            auto_pass, auto_note = check_result
        else:
            auto_pass, auto_note = bool(check_result), ""

    auto_decision = "pass" if auto_pass else ("error" if result["status"] != "pass" else "hold")
    response_excerpt = " ".join(text.split())[:220]
    rows.append({
        "run_id": run_id,
        "timestamp": timestamp,
        "prompt_id": case["id"],
        "task_class": case["task_class"],
        "model": MODEL,
        "base_url": BASE_URL,
        "route": ROUTE,
        "boundary": BOUNDARY,
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS,
        "request_path": str(request_path),
        "response_path": str(response_path),
        "output_path": str(output_path),
        "route_status": result["status"],
        "http_status": result.get("http_status"),
        "elapsed_s": result.get("elapsed_s"),
        "total_seconds": ns_to_seconds(body.get("total_duration")),
        "prompt_eval_count": body.get("prompt_eval_count"),
        "eval_count": body.get("eval_count"),
        "done": body.get("done"),
        "done_reason": body.get("done_reason"),
        "expected_signal": case["expected_signal"],
        "auto_decision": auto_decision,
        "auto_note": auto_note,
        "human_score": "",
        "human_decision": "",
        "failure_owner": "" if auto_decision == "pass" else "model / prompt / sampler / route",
        "response_excerpt": response_excerpt,
    })

if status == "hold":
    pass
elif any(row["route_status"] == "error" for row in rows):
    status = "error"
elif all(row["auto_decision"] == "pass" for row in rows):
    status = "pass"
else:
    status = "hold"

summary = {
    "run_id": run_id,
    "timestamp": timestamp,
    "status": status,
    "model": MODEL,
    "base_url": BASE_URL,
    "route": ROUTE,
    "boundary": BOUNDARY,
    "temperature": TEMPERATURE,
    "max_tokens": MAX_TOKENS,
    "require_endpoint_audit": require_endpoint_audit,
    "endpoint_audit": endpoint_audit,
    "case_count": len(rows),
    "pass_count": sum(1 for row in rows if row["auto_decision"] == "pass"),
    "hold_count": sum(1 for row in rows if row["auto_decision"] == "hold"),
    "error_count": sum(1 for row in rows if row["auto_decision"] == "error"),
    "quality_boundary": "first private probe only; route to full quality harness before workload claims",
    "next_action": {
        "pass": "copy rows into Local LLM Quality Evaluation Harness and rerun a workload prompt through the client harness",
        "hold": "inspect held probes, then tune prompt, sampler, JSON mode, or chat template before rerun",
        "error": "route to Local LLM Troubleshooting Decision Tree before judging model quality",
    }[status] if rows else "complete Local LLM First Endpoint Evidence Audit Runner before quality probing",
    "rows": rows,
}

results_json = SUITE_DIR / f"{run_id}-quality-probe-results.json"
results_csv = SUITE_DIR / f"{run_id}-quality-probe-results.csv"
results_md = SUITE_DIR / f"{run_id}-quality-probe-results.md"
jsonl_path = SUITE_DIR / "quality-probe-runs.jsonl"

write_json(results_json, summary)
with results_csv.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=RESULT_FIELDNAMES)
    writer.writeheader()
    writer.writerows(rows)

md_lines = [
    f"# First Quality Probe - {run_id}",
    "",
    f"Status: `{status}`",
    "",
    "| Prompt | Class | Auto decision | Expected signal | Output | Note |",
    "|---|---|---|---|---|---|",
]
for row in rows:
    md_lines.append(
        f"| {md_cell(row['prompt_id'])} | {md_cell(row['task_class'])} | {md_cell(row['auto_decision'])} | {md_cell(row['expected_signal'])} | {md_cell(row['output_path'])} | {md_cell(row['auto_note'])} |"
    )
md_lines.extend([
    "",
    "## Next Action",
    "",
    summary["next_action"],
    "",
    "## Endpoint Audit",
    "",
    "| Field | Value |",
    "|---|---|",
    f"| Require endpoint audit | {md_cell(require_endpoint_audit)} |",
    f"| Endpoint audit JSON | {md_cell(endpoint_audit['path'])} |",
    f"| Endpoint audit status | {md_cell(endpoint_audit['status'])} |",
    f"| Endpoint audit decision | {md_cell(endpoint_audit['decision'])} |",
    f"| Endpoint audit block reason | {md_cell(endpoint_audit['block_reason'])} |",
])
results_md.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

with jsonl_path.open("a", encoding="utf-8") as handle:
    handle.write(json.dumps(summary, ensure_ascii=True) + "\n")

print(json.dumps({
    "status": status,
    "results_json": str(results_json),
    "results_csv": str(results_csv),
    "results_markdown": str(results_md),
    "pass_count": summary["pass_count"],
    "hold_count": summary["hold_count"],
    "error_count": summary["error_count"],
    "endpoint_audit_status": endpoint_audit["status"],
    "next_action": summary["next_action"],
}, indent=2))
```

PowerShell run for the first Ollama quality pass:

```powershell
$env:LOCAL_LLM_RUN_ROOT = "<paste-run-folder-path>"
$env:LOCAL_LLM_ENDPOINT_AUDIT_JSON = "<first-endpoint-evidence-audit-json>"
$env:LOCAL_LLM_REQUIRE_ENDPOINT_AUDIT = "true"
$env:LOCAL_LLM_MODEL = "<model-tag-from-pull-gate>"
$env:LOCAL_LLM_BASE_URL = "http://127.0.0.1:11434"
$env:LOCAL_LLM_ROUTE = "/api/chat"
$env:LOCAL_LLM_BOUNDARY = "loopback"
$env:LOCAL_LLM_TEMPERATURE = "0"
$env:LOCAL_LLM_MAX_TOKENS = "256"
python .\first-quality-probe-runner.py
```

Pass signal: `first-quality-probe-runner\<run-id>-quality-probe-results.json`, `.csv`, `.md`, `quality-probe-cases.json`, `quality-probe-runs.jsonl`, five request files, five response files, and five output files exist. `status` is `pass` only when the endpoint audit is `pass` and all five script-assisted checks pass.

Hold signal: the endpoint evidence audit is missing or not `pass`, or the endpoint answers but one or more probe checks fail. Keep the artifacts. A hold is a useful diagnosis, not wasted work.

Error signal: at least one request cannot reach the route, returns an HTTP error, or saves an error-shaped result. Route to [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]] before changing the prompt suite.

## Result Interpretation

| Probe | Auto check | Human check |
|---|---|---|
| K-01 | Contains `answer=410`. | Reason is short and not misleading. |
| S-01 | Response content parses as JSON and has `tokens_per_second = 32`. | JSON is usable without repair and the caveat is reasonable. |
| X-01 | Contains only the supplied server/model/run-folder facts and no invented GPU/CUDA fact. | Table shape is readable and every value came from the prompt. |
| G-01 | Response is exactly `not enough evidence`. | It does not smuggle an unsupported guess. |
| C-01 | Exactly two bullet lines with five counted words each. | The bullets actually explain the route-proof boundary. |

Use the auto checks to triage. Use human review for the final first-quality decision.

## Evidence Row

Copy this row into [[LLM/Study/Local LLM First Quality Probe Suite|Local LLM First Quality Probe Suite]], [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]], or [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]:

| Field | Value |
|---|---|
| Run id |  |
| Endpoint audit JSON |  |
| Endpoint audit status | pass / hold / fail / missing |
| Model id |  |
| Base URL and route |  |
| Boundary | loopback / exposed / unclear |
| Cases file |  |
| Results JSON |  |
| Results CSV |  |
| Results Markdown |  |
| JSONL log |  |
| Pass / hold / error counts |  |
| Human review status | not reviewed / reviewed |
| Decision | pass / hold / fail |
| Next action | full quality harness / client harness / prompt rerun / troubleshooting |

## Completion Gate

This runner is complete only when:

- [ ] fixed conditions are written before the run
- [ ] first endpoint evidence audit is linked and has `status == pass`
- [ ] model id matches model-pull evidence
- [ ] first response debrief is linked
- [ ] all five request files exist
- [ ] all five response files exist
- [ ] all five output files exist
- [ ] results JSON, CSV, Markdown, cases JSON, and JSONL exist
- [ ] held or failed probes have one named failure owner
- [ ] human review has either scored the rows or explicitly deferred scoring
- [ ] the result is not promoted beyond a first quality signal without the full harness

## References

Internal routes:

- [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner]]
- [[LLM/Study/Local LLM First Response Debrief Runner]]
- [[LLM/Study/Local LLM First Response Debrief Card]]
- [[LLM/Study/Local LLM First Quality Probe Suite]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]

External/current sources checked 2026-06-15:

- [Ollama chat endpoint](https://docs.ollama.com/api/chat)
- [Ollama structured outputs](https://docs.ollama.com/capabilities/structured-outputs)
- [OpenAI evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [OpenAI evals guide](https://developers.openai.com/api/docs/guides/evals)
