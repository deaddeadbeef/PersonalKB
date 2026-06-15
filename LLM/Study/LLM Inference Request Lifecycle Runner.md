---
tags: [study, llm, inference, local-llm, lifecycle, request, metrics, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [core, practice]
last-verified: 2026-06-16
---

# LLM Inference Request Lifecycle Runner

Use this after [[LLM/Study/LLM Inference Request Lifecycle Lab|LLM Inference Request Lifecycle Lab]] when a saved local request and response should become repeatable evidence. The lab teaches the phases. This runner checks one concrete request against those phases and writes JSON, Markdown, CSV, and JSONL artifacts.

Current dated proof: [[LLM/Study/Local LLM Request Lifecycle Proof - 2026-06-16|Local LLM Request Lifecycle Proof - 2026-06-16]] records a native Ollama `pass/lifecycle_trace_ready` row and an OpenAI-compatible `hold/lifecycle_trace_partial` contrast row for the first local endpoint.

Use it with files from [[LLM/Study/Local LLM First Smoke Request Runner|Local LLM First Smoke Request Runner]], [[LLM/Study/Local LLM First Client Harness Runner|Local LLM First Client Harness Runner]], [[LLM/Study/Local LLM First Streaming Timing Runner|Local LLM First Streaming Timing Runner]], [[LLM/Study/Decoding and Sampling Controls Runner|Decoding and Sampling Controls Runner]], or any local client that preserves request and response JSON.

This is a read-only runner. It does not call `/api/generate`, `/api/chat`, `/v1/chat/completions`, or any local endpoint. It only reads local files and explains what the captured request already proves.

## What This Proves

| Phase | Evidence this runner looks for | Why it matters |
| --- | --- | --- |
| Client request | request file, model, route, sampler, stream flag | proves what the client actually asked for |
| Prompt assembly | messages, prompt, input text, rendered length | separates prompt construction from model behavior |
| Tokenization | prompt token count from response or budget file | turns vague "long prompt" claims into token evidence |
| Prefill | prompt eval duration, TTFT proxy, prompt tokens | names the input-side cost before generation starts |
| Decode loop | output text, output tokens, eval duration, streaming events | separates token production from prompt processing |
| Stop condition | finish reason, done reason, stop signal, stream end | proves why generation stopped |
| Detokenization and parse | returned text, expected text, optional JSON parse | catches format and parser failures after generation |
| Application handling | generated result packet and next owner | turns the request into an operational next step |

## Inputs

Minimum inputs:

- `LOCAL_LLM_REQUEST_PATH` - saved request JSON.
- `LOCAL_LLM_RESPONSE_PATH` - saved response JSON or raw text response.
- `LOCAL_LLM_RUN_ROOT` - output folder for lifecycle artifacts.

Optional inputs:

- `LOCAL_LLM_LIFECYCLE_MANIFEST` - JSON manifest that can hold all paths and expectations.
- `LOCAL_LLM_STREAM_EVENTS_PATH` - JSONL stream event log.
- `LOCAL_LLM_CONTEXT_BUDGET_PATH` - JSON output from [[LLM/Study/Local LLM Context Window and Token Budgeting Runner|Local LLM Context Window and Token Budgeting Runner]] or equivalent.
- `LOCAL_LLM_EXPECT_MODEL` - expected response model id.
- `LOCAL_LLM_EXPECT_JSON` - `true` when the returned text must parse as JSON.
- `LOCAL_LLM_EXPECT_TEXT` - expected substring or exact text.
- `LOCAL_LLM_TEXT_MATCH_MODE` - `contains`, `exact`, or `regex`.

Example manifest:

```json
{
  "run_id": "20260615T120000Z-llama32-smoke",
  "route": "ollama_native",
  "runtime": "ollama",
  "request_path": "ollama-native-request.json",
  "response_path": "ollama-native-response.json",
  "stream_events_path": "stream-events.jsonl",
  "context_budget_path": "context-budget.json",
  "expected_model": "llama3.2:3b",
  "expect_json": false,
  "expect_text": "local llm ok",
  "text_match_mode": "contains"
}
```

## Standard-Library Runner

Save the code block as `llm_request_lifecycle_runner.py` or extract it directly from this note.

```python
from __future__ import annotations

import csv
import datetime as dt
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any


def utc_stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def as_bool(value: Any, default: bool = False) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    if text in {"1", "true", "yes", "y", "on"}:
        return True
    if text in {"0", "false", "no", "n", "off"}:
        return False
    return default


def as_float(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def ns_to_seconds(value: Any) -> float | None:
    numeric = as_float(value)
    if numeric is None:
        return None
    return numeric / 1_000_000_000


def pick(mapping: dict[str, Any], *keys: str) -> Any:
    for key in keys:
        if key in mapping and mapping[key] not in (None, ""):
            return mapping[key]
    return None


def env_or_manifest(env_name: str, manifest: dict[str, Any], key: str, default: Any = None) -> Any:
    if os.environ.get(env_name) not in (None, ""):
        return os.environ[env_name]
    return manifest.get(key, default)


def resolve_path(value: Any, base_dir: Path) -> Path | None:
    if value in (None, ""):
        return None
    path = Path(str(value)).expanduser()
    if not path.is_absolute():
        path = base_dir / path
    return path.resolve()


def load_json_file(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def load_json_or_raw(path: Path) -> tuple[Any, str]:
    raw = path.read_text(encoding="utf-8-sig")
    try:
        return json.loads(raw), raw
    except json.JSONDecodeError:
        return {"_raw_text": raw}, raw


def sha256_short(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()[:16]


def text_from_content(content: Any) -> str:
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            text = text_from_content(item)
            if text:
                parts.append(text)
        return "\n".join(parts)
    if isinstance(content, dict):
        for key in ("text", "content", "value", "output_text"):
            if key in content:
                text = text_from_content(content[key])
                if text:
                    return text
        if content.get("type") == "text" and "data" in content:
            return text_from_content(content["data"])
        return ""
    return str(content)


def extract_request(request_obj: Any) -> dict[str, Any]:
    if not isinstance(request_obj, dict):
        return {
            "model": None,
            "route": "unknown",
            "messages_count": 0,
            "prompt_text": "",
            "prompt_chars": 0,
            "sampler": {},
            "stream": False,
            "request_shape": type(request_obj).__name__,
        }

    messages = request_obj.get("messages")
    prompt_parts: list[str] = []
    roles: list[str] = []
    if isinstance(messages, list):
        for message in messages:
            if isinstance(message, dict):
                role = str(message.get("role", "unknown"))
                text = text_from_content(message.get("content"))
            else:
                role = "unknown"
                text = text_from_content(message)
            roles.append(role)
            if text:
                prompt_parts.append(f"{role}: {text}")

    for key in ("prompt", "input", "instruction", "query"):
        if key in request_obj and request_obj[key] not in (None, ""):
            text = text_from_content(request_obj[key])
            if text:
                prompt_parts.append(text)

    prompt_text = "\n".join(part for part in prompt_parts if part)
    sampler_keys = [
        "temperature",
        "top_p",
        "top_k",
        "min_p",
        "typical_p",
        "max_tokens",
        "num_predict",
        "n_predict",
        "repeat_penalty",
        "presence_penalty",
        "frequency_penalty",
        "seed",
        "stop",
        "format",
        "response_format",
    ]
    sampler = {key: request_obj[key] for key in sampler_keys if key in request_obj}
    options = request_obj.get("options")
    if isinstance(options, dict):
        for key in sampler_keys:
            if key in options and key not in sampler:
                sampler[key] = options[key]
    if "think" in request_obj:
        sampler["think"] = request_obj["think"]

    route = "openai_compatible" if "messages" in request_obj else "native_or_raw"
    return {
        "model": request_obj.get("model"),
        "route": route,
        "messages_count": len(messages) if isinstance(messages, list) else 0,
        "roles": roles,
        "prompt_text": prompt_text,
        "prompt_chars": len(prompt_text),
        "sampler": sampler,
        "stream": as_bool(request_obj.get("stream"), False),
        "request_shape": "object",
    }


def extract_response_text_from_output(output: Any) -> str:
    if not isinstance(output, list):
        return ""
    parts: list[str] = []
    for item in output:
        if isinstance(item, dict):
            if "content" in item:
                parts.append(text_from_content(item["content"]))
            elif "text" in item:
                parts.append(text_from_content(item["text"]))
        else:
            parts.append(text_from_content(item))
    return "\n".join(part for part in parts if part)


def extract_response(response_obj: Any) -> dict[str, Any]:
    if not isinstance(response_obj, dict):
        text = text_from_content(response_obj)
        return {
            "route": "raw",
            "model": None,
            "output_text": text,
            "output_chars": len(text),
            "finish_reason": None,
            "done": None,
            "prompt_tokens": None,
            "output_tokens": None,
            "total_tokens": None,
            "load_s": None,
            "prefill_s": None,
            "decode_s": None,
            "total_s": None,
            "elapsed_s": None,
        }

    route = "unknown"
    output_text = ""
    finish_reason = pick(response_obj, "finish_reason", "done_reason", "stop_reason")

    choices = response_obj.get("choices")
    if isinstance(choices, list) and choices:
        route = "openai_compatible"
        first = choices[0] if isinstance(choices[0], dict) else {}
        message = first.get("message") if isinstance(first.get("message"), dict) else {}
        delta = first.get("delta") if isinstance(first.get("delta"), dict) else {}
        output_text = (
            text_from_content(message.get("content"))
            or text_from_content(delta.get("content"))
            or text_from_content(first.get("text"))
        )
        finish_reason = finish_reason or first.get("finish_reason")
    elif "response" in response_obj:
        route = "ollama_native"
        output_text = text_from_content(response_obj.get("response"))
    elif isinstance(response_obj.get("message"), dict):
        route = "ollama_chat"
        output_text = text_from_content(response_obj["message"].get("content"))
    elif "output_text" in response_obj:
        route = "responses_api"
        output_text = text_from_content(response_obj.get("output_text"))
    elif "output" in response_obj:
        route = "responses_api"
        output_text = extract_response_text_from_output(response_obj.get("output"))
    elif "_raw_text" in response_obj:
        route = "raw"
        output_text = text_from_content(response_obj.get("_raw_text"))
    else:
        output_text = text_from_content(pick(response_obj, "content", "text", "answer"))

    usage = response_obj.get("usage") if isinstance(response_obj.get("usage"), dict) else {}
    prompt_tokens = pick(usage, "prompt_tokens", "input_tokens")
    output_tokens = pick(usage, "completion_tokens", "output_tokens")
    total_tokens = pick(usage, "total_tokens")
    prompt_tokens = prompt_tokens if prompt_tokens is not None else pick(response_obj, "prompt_eval_count", "prompt_tokens", "input_tokens")
    output_tokens = output_tokens if output_tokens is not None else pick(response_obj, "eval_count", "completion_tokens", "output_tokens")
    total_tokens = total_tokens if total_tokens is not None else pick(response_obj, "total_tokens")

    prompt_tokens_f = as_float(prompt_tokens)
    output_tokens_f = as_float(output_tokens)
    total_tokens_f = as_float(total_tokens)
    if total_tokens_f is None and prompt_tokens_f is not None and output_tokens_f is not None:
        total_tokens_f = prompt_tokens_f + output_tokens_f

    prefill_s = ns_to_seconds(response_obj.get("prompt_eval_duration"))
    decode_s = ns_to_seconds(response_obj.get("eval_duration"))
    total_s = ns_to_seconds(response_obj.get("total_duration"))
    load_s = ns_to_seconds(response_obj.get("load_duration"))
    elapsed_s = as_float(pick(response_obj, "elapsed_s", "elapsed_seconds", "duration_s", "wall_seconds"))

    prompt_tps = None
    if prompt_tokens_f is not None and prefill_s and prefill_s > 0:
        prompt_tps = prompt_tokens_f / prefill_s
    decode_tps = None
    if output_tokens_f is not None and decode_s and decode_s > 0:
        decode_tps = output_tokens_f / decode_s

    return {
        "route": route,
        "model": response_obj.get("model") or response_obj.get("model_id"),
        "output_text": output_text,
        "output_chars": len(output_text),
        "finish_reason": finish_reason,
        "done": response_obj.get("done"),
        "prompt_tokens": prompt_tokens_f,
        "output_tokens": output_tokens_f,
        "total_tokens": total_tokens_f,
        "load_s": load_s,
        "prefill_s": prefill_s,
        "decode_s": decode_s,
        "total_s": total_s,
        "elapsed_s": elapsed_s,
        "prompt_tokens_per_s": prompt_tps,
        "decode_tokens_per_s": decode_tps,
    }


def stream_event_text(event: Any) -> str:
    if not isinstance(event, dict):
        return text_from_content(event)
    choices = event.get("choices")
    if isinstance(choices, list) and choices:
        first = choices[0] if isinstance(choices[0], dict) else {}
        delta = first.get("delta") if isinstance(first.get("delta"), dict) else {}
        message = first.get("message") if isinstance(first.get("message"), dict) else {}
        return (
            text_from_content(delta.get("content"))
            or text_from_content(message.get("content"))
            or text_from_content(first.get("text"))
        )
    return text_from_content(pick(event, "response", "content", "text", "token", "output_text"))


def parse_stream_events(path: Path | None) -> dict[str, Any]:
    if path is None:
        return {
            "path": None,
            "event_count": 0,
            "content_event_count": 0,
            "first_content": "",
            "final_text_excerpt": "",
            "done_seen": False,
        }
    content_events: list[str] = []
    event_count = 0
    done_seen = False
    first_event_shape = ""
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        raw = line.strip()
        if not raw:
            continue
        if raw.startswith("data:"):
            raw = raw[5:].strip()
        if raw == "[DONE]":
            event_count += 1
            done_seen = True
            continue
        try:
            event = json.loads(raw)
        except json.JSONDecodeError:
            event = {"_raw_text": raw}
        event_count += 1
        if not first_event_shape:
            first_event_shape = type(event).__name__
        text = stream_event_text(event)
        if text:
            content_events.append(text)
        if isinstance(event, dict) and (event.get("done") is True or event.get("finish_reason")):
            done_seen = True
    final_text = "".join(content_events)
    return {
        "path": str(path),
        "event_count": event_count,
        "content_event_count": len(content_events),
        "first_content": content_events[0] if content_events else "",
        "final_text_excerpt": final_text[:500],
        "done_seen": done_seen,
        "first_event_shape": first_event_shape,
    }


def parse_context_budget(path: Path | None) -> dict[str, Any]:
    if path is None:
        return {"path": None}
    data = load_json_file(path)
    if not isinstance(data, dict):
        return {"path": str(path), "shape": type(data).__name__}
    return {
        "path": str(path),
        "context_window": pick(data, "context_window", "context_limit", "model_context_window"),
        "prompt_tokens": pick(data, "prompt_tokens", "total_prompt_tokens", "input_tokens"),
        "output_reserve_tokens": pick(data, "output_reserve_tokens", "max_output_tokens", "reserved_output_tokens"),
        "margin_tokens": pick(data, "margin_tokens", "remaining_tokens", "headroom_tokens"),
        "fits": data.get("fits"),
        "component_count": len(data.get("components", [])) if isinstance(data.get("components"), list) else None,
    }


def expectation_match(output_text: str, expected_text: str, mode: str) -> bool:
    if not expected_text:
        return True
    if mode == "exact":
        return output_text.strip() == expected_text.strip()
    if mode == "regex":
        return re.search(expected_text, output_text, flags=re.MULTILINE) is not None
    return expected_text in output_text


def json_parse_status(output_text: str, expect_json: bool) -> tuple[bool | None, str]:
    if not expect_json:
        return None, "not requested"
    try:
        json.loads(output_text)
        return True, "returned text parses as JSON"
    except json.JSONDecodeError as exc:
        return False, f"returned text is not valid JSON: {exc}"


def compact(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.4f}"
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value)


def phase_row(phase: str, owner: str, status: str, question: str, evidence: str, next_action: str) -> dict[str, str]:
    return {
        "phase": phase,
        "owner": owner,
        "status": status,
        "question": question,
        "evidence": evidence,
        "next_action": next_action,
    }


def finding(level: str, owner: str, finding_text: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "owner": owner,
        "finding": finding_text,
        "evidence": evidence,
        "action": action,
    }


def csv_write(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: compact(row.get(field)) for field in fields})


def md_cell(value: Any) -> str:
    text = compact(value).replace("\n", "<br>")
    return text.replace("|", "\\|")


def render_markdown(record: dict[str, Any]) -> str:
    lines = [
        f"# LLM Request Lifecycle - {record['run_id']}",
        "",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Created: `{record['created_at']}`",
        f"- Route: `{record['route']}`",
        f"- Runtime: `{record.get('runtime') or ''}`",
        f"- Request: `{record['input_files']['request_path']}`",
        f"- Response: `{record['input_files']['response_path']}`",
        "",
        "## Phase Rows",
        "",
        "| Phase | Owner | Status | Evidence | Next action |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in record["phase_rows"]:
        lines.append(
            f"| {md_cell(row['phase'])} | {md_cell(row['owner'])} | {md_cell(row['status'])} | {md_cell(row['evidence'])} | {md_cell(row['next_action'])} |"
        )
    lines.extend(["", "## Findings", "", "| Level | Owner | Finding | Evidence | Action |", "| --- | --- | --- | --- | --- |"])
    for row in record["findings"]:
        lines.append(
            f"| {md_cell(row['level'])} | {md_cell(row['owner'])} | {md_cell(row['finding'])} | {md_cell(row['evidence'])} | {md_cell(row['action'])} |"
        )
    lines.extend(["", "## Output Excerpt", "", "```text", record["response"]["output_text"][:1500], "```", ""])
    return "\n".join(lines)


def build_phase_rows(
    request_info: dict[str, Any],
    response_info: dict[str, Any],
    stream_info: dict[str, Any],
    context_info: dict[str, Any],
    expected_model: str,
    expect_json: bool,
    expected_text: str,
    text_match_mode: str,
    findings: list[dict[str, str]],
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    model_label = request_info.get("model") or response_info.get("model") or expected_model
    prompt_tokens = response_info.get("prompt_tokens") or as_float(context_info.get("prompt_tokens"))
    output_tokens = response_info.get("output_tokens")

    if expected_model and response_info.get("model") and response_info["model"] != expected_model:
        findings.append(
            finding(
                "hold",
                "route",
                "Response model id differs from expectation.",
                f"expected={expected_model}; actual={response_info['model']}",
                "Confirm the server route, model alias, or manifest expectation before using this as final evidence.",
            )
        )

    client_ok = bool(model_label and request_info.get("prompt_chars", 0) > 0)
    rows.append(
        phase_row(
            "client request",
            "client",
            "pass" if client_ok else "hold",
            "Did the client preserve the model, prompt, route, and sampler?",
            f"model={model_label or 'missing'}; route={request_info.get('route')}; stream={request_info.get('stream')}; sampler={compact(request_info.get('sampler'))}",
            "Capture the exact request JSON before rerunning the endpoint." if not client_ok else "Use this request as the frozen input for comparisons.",
        )
    )

    prompt_ok = request_info.get("prompt_chars", 0) > 0
    rows.append(
        phase_row(
            "prompt assembly",
            "prompt/template",
            "pass" if prompt_ok else "hold",
            "Can the rendered prompt or message list be inspected?",
            f"messages={request_info.get('messages_count')}; roles={compact(request_info.get('roles'))}; prompt_chars={request_info.get('prompt_chars')}",
            "Save the rendered chat template or prompt string." if not prompt_ok else "Compare this prompt against tokenizer and template expectations.",
        )
    )

    token_ok = prompt_tokens is not None
    rows.append(
        phase_row(
            "tokenization",
            "tokenizer/context",
            "pass" if token_ok else "hold",
            "Do we have token evidence for the prompt?",
            f"prompt_tokens={compact(prompt_tokens)}; context_window={compact(context_info.get('context_window'))}; margin_tokens={compact(context_info.get('margin_tokens'))}",
            "Run the context budgeting runner or save runtime token counts." if not token_ok else "Use prompt tokens to explain TTFT and context pressure.",
        )
    )

    prefill_ok = response_info.get("prefill_s") is not None
    rows.append(
        phase_row(
            "prefill",
            "runtime",
            "pass" if prefill_ok else "hold",
            "Can input-side compute be separated from decode?",
            f"prefill_s={compact(response_info.get('prefill_s'))}; prompt_tokens_per_s={compact(response_info.get('prompt_tokens_per_s'))}; load_s={compact(response_info.get('load_s'))}",
            "Capture prompt_eval_duration, TTFT, or trace timing." if not prefill_ok else "Use prefill timing to diagnose long prompts, cache misses, and cold loads.",
        )
    )

    decode_ok = bool(response_info.get("output_text")) and (
        output_tokens is not None or response_info.get("decode_s") is not None or stream_info.get("content_event_count", 0) > 0
    )
    rows.append(
        phase_row(
            "decode loop",
            "runtime/sampler",
            "pass" if decode_ok else "hold",
            "Can token production be separated from request setup?",
            f"output_tokens={compact(output_tokens)}; decode_s={compact(response_info.get('decode_s'))}; decode_tokens_per_s={compact(response_info.get('decode_tokens_per_s'))}; stream_events={stream_info.get('event_count')}",
            "Save eval_count/eval_duration or streaming event logs." if not decode_ok else "Compare decode speed against sampler, quantization, and hardware settings.",
        )
    )

    stop_ok = bool(response_info.get("finish_reason") or response_info.get("done") is True or stream_info.get("done_seen"))
    rows.append(
        phase_row(
            "stop condition",
            "runtime/protocol",
            "pass" if stop_ok else "hold",
            "Do we know why generation stopped?",
            f"finish_reason={compact(response_info.get('finish_reason'))}; done={compact(response_info.get('done'))}; stream_done={compact(stream_info.get('done_seen'))}",
            "Capture finish_reason, done_reason, stop sequence, or stream end marker." if not stop_ok else "Use the stop reason before blaming model quality.",
        )
    )

    json_ok, json_note = json_parse_status(response_info.get("output_text", ""), expect_json)
    text_ok = expectation_match(response_info.get("output_text", ""), expected_text, text_match_mode)
    parse_ok = bool(response_info.get("output_text")) and (json_ok is not False) and text_ok
    if json_ok is False:
        findings.append(finding("hold", "parser", "Expected JSON did not parse.", json_note, "Fix prompt/schema constraints or parser expectations."))
    if expected_text and not text_ok:
        findings.append(
            finding(
                "hold",
                "application",
                "Returned text did not match expectation.",
                f"mode={text_match_mode}; expected={expected_text}",
                "Inspect the prompt, sampler, model id, and parsing boundary.",
            )
        )
    rows.append(
        phase_row(
            "detokenization and parse",
            "parser/application",
            "pass" if parse_ok else "hold",
            "Can the returned tokens be consumed by the application?",
            f"output_chars={response_info.get('output_chars')}; expect_json={expect_json}; json_status={json_note}; expected_text_match={text_ok}",
            "Capture the raw returned text and parser error." if not parse_ok else "Use this output for the application or quality probe layer.",
        )
    )

    prior_holds = [row for row in rows if row["status"] != "pass"]
    rows.append(
        phase_row(
            "application handling",
            "operator",
            "pass" if not prior_holds and not any(item["level"] == "hold" for item in findings) else "hold",
            "Is there a clear next owner after this request?",
            f"phase_holds={len(prior_holds)}; findings={len(findings)}",
            "Move to benchmark, quality probe, or capstone row." if not prior_holds else f"Fix or rerun: {prior_holds[0]['phase']}",
        )
    )
    return rows


def main() -> int:
    manifest_path_value = os.environ.get("LOCAL_LLM_LIFECYCLE_MANIFEST")
    manifest_path = Path(manifest_path_value).expanduser().resolve() if manifest_path_value else None
    manifest: dict[str, Any] = {}
    manifest_dir = Path.cwd()
    if manifest_path is not None:
        manifest = load_json_file(manifest_path)
        if not isinstance(manifest, dict):
            raise ValueError("Lifecycle manifest must be a JSON object.")
        manifest_dir = manifest_path.parent

    run_id = str(env_or_manifest("LOCAL_LLM_RUN_ID", manifest, "run_id", utc_stamp()))
    run_root_value = env_or_manifest("LOCAL_LLM_RUN_ROOT", manifest, "run_root", manifest.get("output_dir", "request-lifecycle-runs"))
    run_root = resolve_path(run_root_value, manifest_dir) or (Path.cwd() / "request-lifecycle-runs")
    run_dir = run_root / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    request_path = resolve_path(env_or_manifest("LOCAL_LLM_REQUEST_PATH", manifest, "request_path"), manifest_dir)
    response_path = resolve_path(env_or_manifest("LOCAL_LLM_RESPONSE_PATH", manifest, "response_path"), manifest_dir)
    stream_path = resolve_path(env_or_manifest("LOCAL_LLM_STREAM_EVENTS_PATH", manifest, "stream_events_path"), manifest_dir)
    context_path = resolve_path(env_or_manifest("LOCAL_LLM_CONTEXT_BUDGET_PATH", manifest, "context_budget_path"), manifest_dir)

    findings: list[dict[str, str]] = []
    missing = []
    if request_path is None:
        missing.append("request_path")
    if response_path is None:
        missing.append("response_path")
    if missing:
        error_record = {
            "run_id": run_id,
            "created_at": utc_iso(),
            "status": "error",
            "decision": "invalid_lifecycle_inputs",
            "missing": missing,
        }
        (run_dir / f"{run_id}-lifecycle-results.json").write_text(json.dumps(error_record, indent=2), encoding="utf-8")
        print(json.dumps(error_record, indent=2))
        return 2

    assert request_path is not None
    assert response_path is not None
    if not request_path.exists():
        raise FileNotFoundError(f"Request path does not exist: {request_path}")
    if not response_path.exists():
        raise FileNotFoundError(f"Response path does not exist: {response_path}")

    request_obj = load_json_file(request_path)
    response_obj, _response_raw = load_json_or_raw(response_path)
    request_info = extract_request(request_obj)
    response_info = extract_response(response_obj)

    if stream_path is not None and not stream_path.exists():
        findings.append(finding("hold", "client", "Stream event path was provided but does not exist.", str(stream_path), "Fix the path or remove the stream expectation."))
        stream_info = {
            "path": str(stream_path),
            "event_count": 0,
            "content_event_count": 0,
            "first_content": "",
            "final_text_excerpt": "",
            "done_seen": False,
            "missing": True,
        }
    else:
        stream_info = parse_stream_events(stream_path)

    if context_path is not None and not context_path.exists():
        findings.append(finding("hold", "context", "Context budget path was provided but does not exist.", str(context_path), "Fix the path or remove the budget expectation."))
        context_info = {"path": str(context_path), "missing": True}
    else:
        context_info = parse_context_budget(context_path)

    expected_model = str(env_or_manifest("LOCAL_LLM_EXPECT_MODEL", manifest, "expected_model", "") or "")
    expect_json = as_bool(env_or_manifest("LOCAL_LLM_EXPECT_JSON", manifest, "expect_json", False), False)
    expected_text = str(env_or_manifest("LOCAL_LLM_EXPECT_TEXT", manifest, "expect_text", "") or "")
    text_match_mode = str(env_or_manifest("LOCAL_LLM_TEXT_MATCH_MODE", manifest, "text_match_mode", "contains") or "contains").lower()
    runtime = str(env_or_manifest("LOCAL_LLM_RUNTIME", manifest, "runtime", "") or "")
    route = str(env_or_manifest("LOCAL_LLM_ROUTE", manifest, "route", response_info.get("route") or request_info.get("route") or "unknown") or "unknown")

    phase_rows = build_phase_rows(
        request_info,
        response_info,
        stream_info,
        context_info,
        expected_model,
        expect_json,
        expected_text,
        text_match_mode,
        findings,
    )

    if any(row["status"] == "error" for row in phase_rows) or any(item["level"] == "error" for item in findings):
        status = "error"
        decision = "invalid_lifecycle_inputs"
    elif any(row["status"] == "hold" for row in phase_rows) or any(item["level"] == "hold" for item in findings):
        status = "hold"
        decision = "lifecycle_trace_partial"
    else:
        status = "pass"
        decision = "lifecycle_trace_ready"

    record: dict[str, Any] = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "runtime": runtime,
        "route": route,
        "input_files": {
            "manifest_path": str(manifest_path) if manifest_path else "",
            "request_path": str(request_path),
            "request_sha256_16": sha256_short(request_path),
            "response_path": str(response_path),
            "response_sha256_16": sha256_short(response_path),
            "stream_events_path": str(stream_path) if stream_path else "",
            "context_budget_path": str(context_path) if context_path else "",
        },
        "request": request_info,
        "response": response_info,
        "stream": stream_info,
        "context_budget": context_info,
        "phase_rows": phase_rows,
        "findings": findings,
        "outputs": {},
    }

    json_path = run_dir / f"{run_id}-lifecycle-results.json"
    markdown_path = run_dir / f"{run_id}-lifecycle-results.md"
    phases_csv_path = run_dir / f"{run_id}-lifecycle-phases.csv"
    findings_csv_path = run_dir / f"{run_id}-lifecycle-findings.csv"
    jsonl_path = run_root / "request-lifecycle-runs.jsonl"

    record["outputs"] = {
        "json": str(json_path),
        "markdown": str(markdown_path),
        "phases_csv": str(phases_csv_path),
        "findings_csv": str(findings_csv_path),
        "jsonl": str(jsonl_path),
    }

    csv_write(phases_csv_path, phase_rows, ["phase", "owner", "status", "question", "evidence", "next_action"])
    csv_write(findings_csv_path, findings, ["level", "owner", "finding", "evidence", "action"])
    markdown_path.write_text(render_markdown(record), encoding="utf-8")
    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(
        json.dumps(
            {
                "status": status,
                "decision": decision,
                "run_id": run_id,
                "output_dir": str(run_dir),
                "phase_count": len(phase_rows),
                "finding_count": len(findings),
            },
            indent=2,
        )
    )
    return 0 if status == "pass" else 1 if status == "hold" else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"status": "error", "decision": "runner_exception", "error": str(exc)}, indent=2), file=sys.stderr)
        raise
```

## PowerShell Run

```powershell
$env:LOCAL_LLM_LIFECYCLE_MANIFEST = "D:\llm-runs\first-smoke\lifecycle-manifest.json"
$env:LOCAL_LLM_RUN_ROOT = "D:\llm-runs\request-lifecycle"
python .\llm_request_lifecycle_runner.py
```

Without a manifest:

```powershell
$env:LOCAL_LLM_REQUEST_PATH = "D:\llm-runs\first-smoke\ollama-native-request.json"
$env:LOCAL_LLM_RESPONSE_PATH = "D:\llm-runs\first-smoke\ollama-native-response.json"
$env:LOCAL_LLM_RUN_ROOT = "D:\llm-runs\request-lifecycle"
$env:LOCAL_LLM_EXPECT_TEXT = "local llm ok"
python .\llm_request_lifecycle_runner.py
```

## Reading The Result

| Runner status | Meaning | Next action |
| --- | --- | --- |
| `pass/lifecycle_trace_ready` | the request has enough evidence for all eight lifecycle phases | copy the Markdown or CSV row into the benchmark or capstone workbook |
| `hold/lifecycle_trace_partial` | the request answered, but one or more phases lack evidence | rerun the endpoint with missing metrics, stream events, token counts, or parser proof |
| `error/invalid_lifecycle_inputs` | the runner could not read the required files or manifest | fix paths and file shape before drawing conclusions |

For Ollama native responses, `prompt_eval_count`, `prompt_eval_duration`, `eval_count`, and `eval_duration` usually give the strongest prefill/decode split. For OpenAI-compatible responses, `usage.prompt_tokens`, `usage.completion_tokens`, `finish_reason`, and any client-side timing are the minimum evidence.

## Fixture Verification

Use a tiny fixture before trusting the runner in a new folder:

```json
{
  "model": "fixture-model",
  "messages": [
    {"role": "system", "content": "Return only JSON."},
    {"role": "user", "content": "Return {\"answer\": 42}."}
  ],
  "temperature": 0,
  "max_tokens": 32,
  "stream": false
}
```

Expected response shape:

```json
{
  "model": "fixture-model",
  "response": "{\"answer\": 42}",
  "done": true,
  "done_reason": "stop",
  "total_duration": 900000000,
  "load_duration": 100000000,
  "prompt_eval_count": 12,
  "prompt_eval_duration": 200000000,
  "eval_count": 5,
  "eval_duration": 400000000
}
```

Pass signal: stdout says `pass`, decision is `lifecycle_trace_ready`, there are eight phase rows, prompt/decode tokens per second are present, and JSON parse status is true.

## Capstone Row

| Evidence | Output |
| --- | --- |
| Request lifecycle runner | `<run-id>-lifecycle-results.json`, `<run-id>-lifecycle-results.md`, `<run-id>-lifecycle-phases.csv`, `<run-id>-lifecycle-findings.csv`, and one `request-lifecycle-runs.jsonl` row |

## References

- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Local LLM End-to-End Mental Model]]
- [[LLM/Study/Local LLM First Smoke Request Runner]]
- [[LLM/Study/Local LLM First Response Debrief Runner]]
- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/Local LLM First Streaming Timing Runner]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]]
- [[LLM/Study/Decoding and Sampling Controls Runner]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
