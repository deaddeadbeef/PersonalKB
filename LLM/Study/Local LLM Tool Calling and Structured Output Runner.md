---
tags: [study, llm, inference, local-llm, tools, function-calling, structured-output, constrained-decoding, agents, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [core, practice]
last-verified: 2026-06-15
---

# Local LLM Tool Calling and Structured Output Runner

> **One-line summary** Probe structured JSON, required tool calls, tool-result injection, and denied bad arguments before trusting a local LLM endpoint in an application loop.

Use this after [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]] explains the manual boundary and after [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner|Local LLM OpenAI-Compatible API Contract Runner]] proves the base route. Use it before a local agent loop, RAG tool, file assistant, database helper, or benchmark row that depends on parseable JSON or model-proposed actions.

This runner sends real local HTTP requests when pointed at an actual endpoint. For verification or dry runs, point `LOCAL_LLM_BASE_URL` at a fake loopback fixture server. The built-in local tool is a tiny read-only dictionary lookup, and it is executed only after schema validation and policy approval.

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| Structured JSON probe | The route can return parseable assistant content that matches the expected schema. | Factuality or tool safety. |
| Required tool-call probe | The route can return an OpenAI-compatible `tool_calls` shape with parseable arguments. | That the selected tool is semantically wise. |
| Local schema validation | The application, not the model, validates argument type, required fields, enums, and extra fields. | Full JSON Schema coverage. |
| Policy decision row | Tool execution is controlled outside the model output. | That every future tool is safe. |
| Tool-result follow-up | The client can inject a tool result and capture a final answer. | Multi-step agent quality under real workload pressure. |
| Denied bad-argument probe | Unsafe or out-of-policy model arguments are blocked before execution. | That jailbreaks or prompt injection are impossible. |
| JSON/CSV/Markdown/JSONL output | Tool evidence can feed the benchmark log, quality harness, troubleshooting tree, and capstone workbook. | Production observability or long-run reliability. |

Academic bridge: structured output is a decoding or interface constraint, not a truth guarantee. Tool calling is an action proposal, not authorization. The reliable system boundary is: constrain or parse the model output, validate it against schema, check policy outside the model, execute least-privilege code, inject the observation, and stop under explicit loop rules.

## Fixed Conditions

Write these before running:

| Field | Value |
|---|---|
| Run folder |  |
| API contract runner result |  |
| Tool/structured lab card |  |
| Runtime | Ollama / LM Studio / llama.cpp / vLLM / SGLang / other |
| Base URL | `http://127.0.0.1:11434/v1` for an OpenAI-compatible local route |
| Model id |  |
| Structured-output mode | prompt-only / `json_object` / `json_schema` / runtime-specific |
| Tool-choice mode | none / auto / required / named |
| Tool parser or backend | native / xgrammar / outlines / llama.cpp grammar / unknown |
| Boundary | loopback / LAN / tunnel / remote |
| Execution class | read-only local dictionary |
| Next gate | quality harness / benchmark row / security review / app integration |

If the endpoint is exposed beyond loopback, complete [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] before this runner. Do not put private documents, secrets, real API keys, production tool schemas, or sensitive RAG chunks into the probe.

## Standard-Library Runner

Save this as `tool-structured-output-runner.py` inside the run folder. It uses only Python's standard library.

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


def extract_finish_reason(data):
    if not isinstance(data, dict):
        return ""
    choices = data.get("choices") if isinstance(data.get("choices"), list) else []
    first = choices[0] if choices and isinstance(choices[0], dict) else {}
    return str(first.get("finish_reason") or "")


def extract_content_text(data):
    return content_to_text(extract_message(data).get("content"))


def extract_tool_calls(data):
    message = extract_message(data)
    calls = message.get("tool_calls")
    if isinstance(calls, list):
        return calls
    return []


def parse_tool_call(call):
    if not isinstance(call, dict):
        return {"id": "", "name": "", "arguments": None, "argument_error": "tool call is not an object"}
    function = call.get("function") if isinstance(call.get("function"), dict) else {}
    name = str(function.get("name") or call.get("name") or "")
    arguments, argument_error = try_json_loads(function.get("arguments") if "arguments" in function else call.get("arguments"))
    return {
        "id": str(call.get("id") or "call_local_fixture"),
        "type": str(call.get("type") or "function"),
        "name": name,
        "arguments": arguments,
        "argument_error": argument_error,
        "raw": call,
    }


def validate_schema(value, schema, path="$"):
    errors = []
    expected_type = schema.get("type")
    if expected_type == "object":
        if not isinstance(value, dict):
            return [f"{path} expected object"]
        required = schema.get("required") if isinstance(schema.get("required"), list) else []
        for key in required:
            if key not in value:
                errors.append(f"{path}.{key} is required")
        properties = schema.get("properties") if isinstance(schema.get("properties"), dict) else {}
        if schema.get("additionalProperties") is False:
            extras = sorted(set(value) - set(properties))
            for key in extras:
                errors.append(f"{path}.{key} is not allowed")
        for key, child_schema in properties.items():
            if key in value and isinstance(child_schema, dict):
                errors.extend(validate_schema(value[key], child_schema, f"{path}.{key}"))
        return errors
    if expected_type == "array":
        if not isinstance(value, list):
            return [f"{path} expected array"]
        item_schema = schema.get("items") if isinstance(schema.get("items"), dict) else None
        if item_schema:
            for index, item in enumerate(value):
                errors.extend(validate_schema(item, item_schema, f"{path}[{index}]"))
    elif expected_type == "string":
        if not isinstance(value, str):
            errors.append(f"{path} expected string")
    elif expected_type == "integer":
        if not isinstance(value, int) or isinstance(value, bool):
            errors.append(f"{path} expected integer")
    elif expected_type == "number":
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            errors.append(f"{path} expected number")
    elif expected_type == "boolean":
        if not isinstance(value, bool):
            errors.append(f"{path} expected boolean")
    if "enum" in schema and value not in schema.get("enum", []):
        errors.append(f"{path} expected one of {schema.get('enum')}")
    return errors


def http_json(route, body, label):
    url = join_url(BASE_URL, route)
    request_path = OUT_DIR / f"{RUN_ID}-{label}-request.json"
    response_path = OUT_DIR / f"{RUN_ID}-{label}-response.json"
    safe_request = {
        "url": url,
        "method": "POST",
        "authorization_present": bool(API_KEY),
        "body": body,
    }
    write_json(request_path, safe_request)
    payload = json.dumps(body).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    if API_KEY:
        request.add_header("Authorization", f"Bearer {API_KEY}")
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            raw = response.read().decode("utf-8", errors="replace")
            elapsed_ms = round((time.perf_counter() - started) * 1000, 2)
            data, parse_error = try_json_loads(raw)
            result = {
                "ok": 200 <= response.status < 300,
                "http_status": response.status,
                "elapsed_ms": elapsed_ms,
                "raw": raw,
                "data": data,
                "parse_error": parse_error,
                "request_path": str(request_path),
                "response_path": str(response_path),
            }
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        data, parse_error = try_json_loads(raw)
        result = {
            "ok": False,
            "http_status": exc.code,
            "elapsed_ms": round((time.perf_counter() - started) * 1000, 2),
            "raw": raw,
            "data": data,
            "parse_error": parse_error,
            "error": str(exc),
            "request_path": str(request_path),
            "response_path": str(response_path),
        }
    except (urllib.error.URLError, TimeoutError) as exc:
        result = {
            "ok": False,
            "http_status": 0,
            "elapsed_ms": round((time.perf_counter() - started) * 1000, 2),
            "raw": "",
            "data": None,
            "parse_error": "",
            "error": str(exc),
            "request_path": str(request_path),
            "response_path": str(response_path),
        }
    write_json(response_path, {key: value for key, value in result.items() if key != "raw"})
    write_text(OUT_DIR / f"{RUN_ID}-{label}-response.raw.txt", result.get("raw", ""))
    return result


def make_chat_body(messages, extra=None):
    body = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0,
        "stream": False,
        "max_tokens": 160,
    }
    if extra:
        body.update(extra)
    return body


def add_row(rows, probe, status, evidence, next_action, details=None):
    rows.append({
        "probe": probe,
        "status": status,
        "evidence": evidence,
        "next_action": next_action,
        "details": details or {},
    })


def execute_weather_tool(arguments):
    city = arguments.get("city") if isinstance(arguments, dict) else None
    unit = arguments.get("unit") if isinstance(arguments, dict) else None
    values = {
        "Tokyo": {"temperature_c": 18, "condition": "clear"},
        "London": {"temperature_c": 15, "condition": "rain"},
        "New York": {"temperature_c": 22, "condition": "partly cloudy"},
    }
    row = values[city]
    if unit == "fahrenheit":
        return {
            "city": city,
            "temperature_f": round(row["temperature_c"] * 9 / 5 + 32, 1),
            "condition": row["condition"],
            "source": "local-fixture-dictionary",
        }
    return {
        "city": city,
        "temperature_c": row["temperature_c"],
        "condition": row["condition"],
        "source": "local-fixture-dictionary",
    }


RUN_ROOT = Path(os.environ.get("LOCAL_LLM_RUN_ROOT", ".")).expanduser().resolve()
BASE_URL = os.environ.get("LOCAL_LLM_BASE_URL", "").strip().rstrip("/")
MODEL = os.environ.get("LOCAL_LLM_MODEL", "").strip()
API_KEY = os.environ.get("LOCAL_LLM_API_KEY", "").strip()
TIMEOUT_SECONDS = float(os.environ.get("LOCAL_LLM_TIMEOUT_SECONDS", "30"))
RUN_ID = time.strftime("%Y%m%d-%H%M%S-tool-structured")
OUT_DIR = RUN_ROOT / "tool-structured-output-runner"

STRUCTURED_SCHEMA = {
    "type": "object",
    "required": ["answer", "confidence", "needs_tool"],
    "additionalProperties": False,
    "properties": {
        "answer": {"type": "string"},
        "confidence": {"type": "number"},
        "needs_tool": {"type": "boolean"},
    },
}

TOOL_ARGUMENT_SCHEMA = {
    "type": "object",
    "required": ["city", "unit"],
    "additionalProperties": False,
    "properties": {
        "city": {"type": "string", "enum": ["Tokyo", "London", "New York"]},
        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
    },
}

WEATHER_TOOL = {
    "type": "function",
    "function": {
        "name": "lookup_city_weather",
        "description": "Look up fixture weather for one allowed city in a local read-only dictionary.",
        "strict": True,
        "parameters": TOOL_ARGUMENT_SCHEMA,
    },
}

summary = {
    "run_id": RUN_ID,
    "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
    "base_url": BASE_URL,
    "model": MODEL,
    "boundary": os.environ.get("LOCAL_LLM_BOUNDARY", "loopback"),
    "status": "hold",
    "rows": [],
    "output_dir": str(OUT_DIR),
}

if not BASE_URL or not MODEL:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    sample = {
        "LOCAL_LLM_RUN_ROOT": str(RUN_ROOT),
        "LOCAL_LLM_BASE_URL": "http://127.0.0.1:11434/v1",
        "LOCAL_LLM_MODEL": "your-local-model-id",
        "LOCAL_LLM_API_KEY": "optional-local-token",
    }
    write_json(OUT_DIR / "tool-structured-output-runner-env-template.json", sample)
    summary["status"] = "error"
    summary["next_action"] = "Set LOCAL_LLM_BASE_URL and LOCAL_LLM_MODEL, or point them at a fake loopback fixture server."
    write_json(OUT_DIR / f"{RUN_ID}-tool-structured-results.json", summary)
    print(json.dumps({"status": summary["status"], "template": str(OUT_DIR / "tool-structured-output-runner-env-template.json")}, indent=2))
    raise SystemExit(0)

rows = summary["rows"]

structured_body = make_chat_body(
    [
        {"role": "system", "content": "Return only JSON matching the requested schema."},
        {"role": "user", "content": "Classify this local inference probe as ready. Do not call a tool."},
    ],
    {
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "local_structured_probe",
                "strict": True,
                "schema": STRUCTURED_SCHEMA,
            },
        },
    },
)
structured_result = http_json("/chat/completions", structured_body, "structured-json")
structured_content = extract_content_text(structured_result.get("data"))
structured_value, structured_parse_error = try_json_loads(structured_content)
structured_errors = validate_schema(structured_value, STRUCTURED_SCHEMA) if not structured_parse_error else [structured_parse_error]
if structured_result["ok"] and not structured_errors:
    add_row(rows, "structured_json", "pass", "assistant content parsed and matched schema", "Use schema output only for typed final answers.", {
        "elapsed_ms": structured_result["elapsed_ms"],
        "finish_reason": extract_finish_reason(structured_result.get("data")),
        "parsed": structured_value,
    })
else:
    add_row(rows, "structured_json", "hold", "structured content was missing, invalid, rejected, or schema-invalid", "Check runtime structured-output support, schema syntax, prompt, and chat template.", {
        "http_status": structured_result["http_status"],
        "parse_error": structured_parse_error,
        "schema_errors": structured_errors,
        "content_excerpt": structured_content[:300],
        "transport_error": structured_result.get("error", ""),
    })

allowed_messages = [
    {"role": "system", "content": "Use the provided tool when the user asks for fixture weather."},
    {"role": "user", "content": "Use lookup_city_weather for Tokyo in celsius."},
]
tool_body = make_chat_body(
    allowed_messages,
    {
        "tools": [WEATHER_TOOL],
        "tool_choice": {"type": "function", "function": {"name": "lookup_city_weather"}},
    },
)
tool_result = http_json("/chat/completions", tool_body, "required-tool-call")
tool_calls = extract_tool_calls(tool_result.get("data"))
parsed_call = parse_tool_call(tool_calls[0]) if tool_calls else {"name": "", "arguments": None, "argument_error": "no tool call returned"}
tool_schema_errors = validate_schema(parsed_call.get("arguments"), TOOL_ARGUMENT_SCHEMA) if not parsed_call.get("argument_error") else [parsed_call["argument_error"]]
policy_decision = "allow" if parsed_call.get("name") == "lookup_city_weather" and not tool_schema_errors else "deny"
tool_execution_result = None
if policy_decision == "allow":
    tool_execution_result = execute_weather_tool(parsed_call["arguments"])
    add_row(rows, "required_tool_call", "pass", "tool call name and arguments validated; policy allowed execution", "Inject the tool result and ask for the final answer.", {
        "elapsed_ms": tool_result["elapsed_ms"],
        "tool_name": parsed_call.get("name"),
        "arguments": parsed_call.get("arguments"),
        "policy_decision": policy_decision,
        "tool_result": tool_execution_result,
    })
else:
    add_row(rows, "required_tool_call", "hold", "tool call missing, wrong, malformed, or denied", "Check tool parser support, tool_choice mode, model compatibility, and schema descriptions.", {
        "http_status": tool_result["http_status"],
        "tool_name": parsed_call.get("name"),
        "arguments": parsed_call.get("arguments"),
        "schema_errors": tool_schema_errors,
        "argument_error": parsed_call.get("argument_error", ""),
        "transport_error": tool_result.get("error", ""),
    })

if tool_execution_result is not None:
    assistant_message = extract_message(tool_result.get("data"))
    if isinstance(assistant_message, dict):
        for call in assistant_message.get("tool_calls", []) or []:
            if isinstance(call, dict) and not call.get("id"):
                call["id"] = parsed_call["id"]
    followup_messages = [
        allowed_messages[0],
        allowed_messages[1],
        assistant_message,
        {
            "role": "tool",
            "tool_call_id": parsed_call["id"],
            "content": json.dumps(tool_execution_result, ensure_ascii=True),
        },
    ]
    followup_body = make_chat_body(followup_messages, {"tools": [WEATHER_TOOL]})
    followup_result = http_json("/chat/completions", followup_body, "tool-result-followup")
    final_text = extract_content_text(followup_result.get("data"))
    final_norm = normalize_text(final_text)
    expected_tokens = ["tokyo", "18"]
    used_result = all(token in final_norm for token in expected_tokens)
    if followup_result["ok"] and final_text and used_result:
        add_row(rows, "tool_result_followup", "pass", "final answer used the injected tool result", "Record the row in the quality harness or benchmark log.", {
            "elapsed_ms": followup_result["elapsed_ms"],
            "finish_reason": extract_finish_reason(followup_result.get("data")),
            "final_text": final_text,
        })
    else:
        add_row(rows, "tool_result_followup", "hold", "final answer was missing or did not clearly use the tool result", "Check tool-role message format, context budget, and result-injection prompt.", {
            "http_status": followup_result["http_status"],
            "final_text": final_text[:500],
            "expected_tokens": expected_tokens,
            "transport_error": followup_result.get("error", ""),
        })
else:
    add_row(rows, "tool_result_followup", "hold", "tool result was not available for follow-up", "Fix required_tool_call before testing result injection.")

denied_messages = [
    {"role": "system", "content": "Use the provided tool when the user asks for fixture weather."},
    {"role": "user", "content": "Use lookup_city_weather for Atlantis in celsius."},
]
denied_body = make_chat_body(
    denied_messages,
    {
        "tools": [WEATHER_TOOL],
        "tool_choice": {"type": "function", "function": {"name": "lookup_city_weather"}},
    },
)
denied_result = http_json("/chat/completions", denied_body, "denied-bad-arguments")
denied_calls = extract_tool_calls(denied_result.get("data"))
denied_call = parse_tool_call(denied_calls[0]) if denied_calls else {"name": "", "arguments": None, "argument_error": "no tool call returned"}
denied_errors = validate_schema(denied_call.get("arguments"), TOOL_ARGUMENT_SCHEMA) if not denied_call.get("argument_error") else [denied_call["argument_error"]]
denied_policy = "deny" if denied_errors or denied_call.get("name") != "lookup_city_weather" else "allow"
if denied_policy == "deny":
    add_row(rows, "denied_bad_arguments", "pass", "bad or out-of-policy arguments were denied before execution", "Keep the external policy boundary; add more denial cases for real tools.", {
        "elapsed_ms": denied_result["elapsed_ms"],
        "tool_name": denied_call.get("name"),
        "arguments": denied_call.get("arguments"),
        "schema_errors": denied_errors,
        "policy_decision": denied_policy,
        "executed": False,
    })
else:
    add_row(rows, "denied_bad_arguments", "hold", "denial path was not exercised; model returned allowed arguments", "Add adversarial prompts or explicit fixture cases before trusting tool policy.", {
        "elapsed_ms": denied_result["elapsed_ms"],
        "tool_name": denied_call.get("name"),
        "arguments": denied_call.get("arguments"),
        "schema_errors": denied_errors,
        "policy_decision": denied_policy,
        "executed": False,
    })

summary["status"] = "pass" if rows and all(row["status"] == "pass" for row in rows) else "hold"
summary["pass_count"] = sum(1 for row in rows if row["status"] == "pass")
summary["hold_count"] = sum(1 for row in rows if row["status"] == "hold")
summary["next_action"] = (
    "Move this schema and tool boundary into the local client harness."
    if summary["status"] == "pass"
    else "Fix held probes before executing real tools or claiming structured-output support."
)

summary_json_path = OUT_DIR / f"{RUN_ID}-tool-structured-results.json"
summary_md_path = OUT_DIR / f"{RUN_ID}-tool-structured-results.md"
rows_csv_path = OUT_DIR / f"{RUN_ID}-tool-structured-probes.csv"
jsonl_path = OUT_DIR / "tool-structured-runs.jsonl"

write_json(summary_json_path, summary)

with rows_csv_path.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=["probe", "status", "evidence", "next_action", "details"])
    writer.writeheader()
    for row in rows:
        writer.writerow({
            "probe": row["probe"],
            "status": row["status"],
            "evidence": row["evidence"],
            "next_action": row["next_action"],
            "details": json.dumps(row.get("details", {}), ensure_ascii=True, sort_keys=True),
        })

md_lines = [
    f"# Tool Calling and Structured Output Run - {RUN_ID}",
    "",
    f"- Status: `{summary['status']}`",
    f"- Model: `{MODEL}`",
    f"- Base URL: `{BASE_URL}`",
    f"- Output dir: `{OUT_DIR}`",
    f"- Next action: {summary['next_action']}",
    "",
    "| Probe | Status | Evidence | Next action |",
    "|---|---:|---|---|",
]
for row in rows:
    md_lines.append(f"| {md_cell(row['probe'])} | {md_cell(row['status'])} | {md_cell(row['evidence'])} | {md_cell(row['next_action'])} |")
write_text(summary_md_path, "\n".join(md_lines))

append_jsonl(jsonl_path, summary)

print(json.dumps({
    "status": summary["status"],
    "run_id": RUN_ID,
    "results_json": str(summary_json_path),
    "results_md": str(summary_md_path),
    "rows_csv": str(rows_csv_path),
    "jsonl": str(jsonl_path),
}, indent=2, ensure_ascii=True))
```

## Environment Variables

| Variable | Required | Meaning |
|---|---:|---|
| `LOCAL_LLM_RUN_ROOT` | no | Evidence root. Defaults to the current directory. |
| `LOCAL_LLM_BASE_URL` | yes | OpenAI-compatible base URL such as `http://127.0.0.1:11434/v1`. |
| `LOCAL_LLM_MODEL` | yes | Served model id. |
| `LOCAL_LLM_API_KEY` | no | Local placeholder token or real token if a proxy requires one. The runner records only whether it was present. |
| `LOCAL_LLM_TIMEOUT_SECONDS` | no | Per-request timeout. Defaults to `30`. |
| `LOCAL_LLM_BOUNDARY` | no | Human label such as `loopback`, `LAN`, `tunnel`, or `remote`. |

PowerShell example:

```powershell
$env:LOCAL_LLM_RUN_ROOT = "D:\LLM-runs\tool-structured-001"
$env:LOCAL_LLM_BASE_URL = "http://127.0.0.1:11434/v1"
$env:LOCAL_LLM_MODEL = "qwen3"
python .\tool-structured-output-runner.py
```

## Result Interpretation

| Runner status | Meaning | Next move |
|---|---|---|
| `pass` | Structured JSON, required tool call, result injection, and denial probe all passed. | Move the tool schema into the client harness and add quality rows. |
| `hold` | At least one probe failed, was unsupported, or did not exercise the needed behavior. | Do not execute real tools yet; inspect the held probe row. |
| `error` | Required configuration was missing. | Set base URL and model id, or run against a fake fixture server. |

Read each row separately. A route can pass structured JSON and still fail tool calls. A tool call can parse and still be denied. A final answer can be fluent and still fail if it ignores the tool result.

## Completion Gate

This runner is complete when you have:

- [ ] a saved `tool-structured-results.json`
- [ ] a saved `tool-structured-results.md`
- [ ] a saved `tool-structured-probes.csv`
- [ ] appended `tool-structured-runs.jsonl`
- [ ] request and response files for structured JSON, required tool call, tool-result follow-up, and denied bad arguments
- [ ] a row-level decision for parseability, schema validity, policy decision, execution, result injection, and denial behavior
- [ ] a handoff to [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] or [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]]

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/2023 — Open Models and Agents/Function Calling]]
- [[LLM/2023 — Open Models and Agents/Structured Output and Constrained Generation]]
- [[LLM/2023 — Open Models and Agents/Tool Selection and Execution Loops]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]]
- [[LLM/Study/Decoding and Sampling Controls Runner]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]

Current external docs checked 2026-06-15:

- [OpenAI structured model outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- [OpenAI function calling](https://developers.openai.com/api/docs/guides/function-calling)
- [Ollama structured outputs](https://docs.ollama.com/capabilities/structured-outputs)
- [Ollama tool calling](https://docs.ollama.com/capabilities/tool-calling)
- [vLLM structured outputs](https://docs.vllm.ai/en/latest/features/structured_outputs/)
- [vLLM tool calling](https://docs.vllm.ai/en/latest/features/tool_calling/)
- [llama.cpp HTTP server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- [llama-cpp-python JSON/schema and function calling](https://llama-cpp-python.readthedocs.io/en/latest/)
