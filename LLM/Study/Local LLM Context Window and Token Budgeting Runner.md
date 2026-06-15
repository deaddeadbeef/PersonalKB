---
tags: [study, llm, inference, local-llm, tokenization, context-window, budgeting, rag, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [core, practice]
last-verified: 2026-06-15
---

# Local LLM Context Window and Token Budgeting Runner

> **One-line summary** Turn a prompt, history, RAG chunks, tool schemas, output reserve, safety margin, and runtime context limit into a repeatable context-budget evidence packet before running local inference.

Use this after [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]] explains the manual method and after [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]] identifies the served tokenizer or template boundary. Use the result before long-context calls, RAG packing, tool-heavy prompts, benchmark comparisons, and [[LLM/Study/Local LLM First Benchmark Row Builder|Local LLM First Benchmark Row Builder]] rows.

This runner does not contact an LLM endpoint. It reads a local manifest, counts exact token fields when you provide them, estimates missing token counts with a conservative local heuristic, and records which parts are exact versus estimated. Treat an estimated `pass` as a planning gate; exact production proof still needs the served tokenizer or runtime usage fields.

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| Saved manifest | The prompt components, priorities, output reserve, and context limit are explicit. | That the model saw exactly this rendered sequence. |
| Component token rows | System, user, history, RAG, tool schema, and metadata costs are visible. | Exact tokenizer behavior unless counts are supplied from the served tokenizer. |
| Fit decision | Prompt plus reserved output plus margin fits, holds, or exceeds the configured limit. | That quality is good or retrieval is relevant. |
| Drop plan | The first removable context layers are named. | That dropping them is semantically safe. |
| JSON/CSV/Markdown/JSONL output | Budget evidence can feed benchmark, RAG, tool, and capstone notes. | Runtime memory telemetry or KV-cache measurement. |

Academic bridge: a context window is a sequence budget over token IDs, not words or characters. Longer prompts increase prefill work and KV-cache memory. RAG chunks, tool schemas, and chat history compete with reserved output tokens, so a request can fail by starving the answer even if it stays below the nominal context limit.

## Manifest Shape

Save this as `context-budget-manifest.json` in the run folder. Exact token counts are preferred; text-only components are estimated.

```json
{
  "runtime": "ollama",
  "model": "example-model",
  "tokenizer": "served tokenizer or unknown",
  "context_limit_tokens": 8192,
  "reserved_output_tokens": 512,
  "safety_margin_tokens": 512,
  "token_count_method": "served tokenizer / runtime usage / estimate",
  "components": [
    {
      "name": "system prompt",
      "kind": "system",
      "text": "You are a concise local assistant.",
      "priority": 100,
      "required": true
    },
    {
      "name": "current user task",
      "kind": "user",
      "text": "Answer the question using the supplied evidence.",
      "priority": 100,
      "required": true
    },
    {
      "name": "retrieved chunk 1",
      "kind": "retrieved_context",
      "text": "Evidence chunk text goes here.",
      "priority": 60,
      "required": false,
      "source": "doc-1"
    }
  ]
}
```

Optional fields:

| Field | Meaning |
|---|---|
| `exact_tokens` | Token count from the served tokenizer, `apply_chat_template(..., tokenize=True)`, runtime usage, or another trusted source. |
| `rendered_text` | Use this instead of `text` when the component has already passed through a chat template or serializer. |
| `shared_prefix` | Set `true` when a component may be reused by prompt cache or prefix cache. |
| `drop_group` | Label components that should be removed together. |
| `source` | Local note, retrieval id, tool name, or benchmark source. |

## Standard-Library Runner

Save this as `context-window-budget-runner.py` beside the manifest. It uses only Python's standard library.

```python
import csv
import json
import math
import os
import re
import time
from pathlib import Path


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


def as_int(value, default=0):
    if value is None or value == "":
        return default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def as_bool(value, default=False):
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "on"}


def text_for_component(component):
    if component.get("rendered_text") is not None:
        return str(component.get("rendered_text") or "")
    if component.get("text") is not None:
        return str(component.get("text") or "")
    if component.get("json") is not None:
        return json.dumps(component.get("json"), ensure_ascii=True, sort_keys=True)
    return ""


def estimate_tokens(text):
    value = str(text or "")
    if not value:
        return 0
    cjk_chars = len(re.findall(r"[\u3040-\u30ff\u3400-\u9fff\uf900-\ufaff]", value))
    ascii_runs = re.findall(r"[A-Za-z0-9_./:=-]+", value)
    ascii_token_estimate = sum(max(1, math.ceil(len(run) / 4)) for run in ascii_runs)
    punctuation = len(re.findall(r"[^\w\s\u3040-\u30ff\u3400-\u9fff\uf900-\ufaff]", value))
    whitespace_lines = value.count("\n")
    return max(1, cjk_chars + ascii_token_estimate + math.ceil(punctuation / 4) + whitespace_lines)


def component_row(component, index):
    text = text_for_component(component)
    exact_tokens = component.get("exact_tokens")
    if exact_tokens is not None:
        tokens = as_int(exact_tokens)
        count_status = "exact"
        count_source = str(component.get("token_source") or "manifest exact_tokens")
    else:
        tokens = estimate_tokens(text)
        count_status = "estimate"
        count_source = "local heuristic"

    priority = as_int(component.get("priority"), 50)
    required = as_bool(component.get("required"), False)
    row = {
        "index": index,
        "name": str(component.get("name") or f"component {index}"),
        "kind": str(component.get("kind") or "unknown"),
        "source": str(component.get("source") or ""),
        "required": required,
        "priority": priority,
        "drop_group": str(component.get("drop_group") or ""),
        "shared_prefix": as_bool(component.get("shared_prefix"), False),
        "tokens": tokens,
        "count_status": count_status,
        "count_source": count_source,
        "chars": len(text),
        "text_excerpt": " ".join(text.split())[:180],
    }
    return row


def drop_candidates(rows):
    candidates = [row for row in rows if not row["required"]]
    return sorted(candidates, key=lambda row: (row["priority"], -row["tokens"], row["index"]))


def build_drop_plan(rows, over_by):
    remaining = max(0, over_by)
    plan = []
    freed = 0
    for row in drop_candidates(rows):
        if remaining <= 0:
            break
        freed += row["tokens"]
        remaining = max(0, over_by - freed)
        plan.append({
            "name": row["name"],
            "kind": row["kind"],
            "tokens": row["tokens"],
            "priority": row["priority"],
            "drop_group": row["drop_group"],
            "remaining_over_by_after_drop": remaining,
        })
    return plan


def write_csv(path, rows):
    fields = [
        "index",
        "name",
        "kind",
        "source",
        "required",
        "priority",
        "drop_group",
        "shared_prefix",
        "tokens",
        "count_status",
        "count_source",
        "chars",
        "text_excerpt",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def write_markdown(path, record):
    lines = [
        f"# Context Budget - {record['run_id']}",
        "",
        f"Status: `{record['status']}`",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Runtime | {md_cell(record['runtime'])} |",
        f"| Model | {md_cell(record['model'])} |",
        f"| Tokenizer | {md_cell(record['tokenizer'])} |",
        f"| Count method | {md_cell(record['token_count_method'])} |",
        f"| Context limit | {md_cell(record['context_limit_tokens'])} |",
        f"| Input tokens | {md_cell(record['input_tokens'])} |",
        f"| Reserved output | {md_cell(record['reserved_output_tokens'])} |",
        f"| Safety margin | {md_cell(record['safety_margin_tokens'])} |",
        f"| Total planned | {md_cell(record['total_planned_tokens'])} |",
        f"| Remaining tokens | {md_cell(record['remaining_tokens'])} |",
        f"| Estimated rows | {md_cell(record['estimated_component_count'])} |",
        f"| Exact rows | {md_cell(record['exact_component_count'])} |",
        f"| Next action | {md_cell(record['next_action'])} |",
        "",
        "## Components",
        "",
        "| Component | Kind | Tokens | Count | Required | Priority | Source |",
        "|---|---|---:|---|---|---:|---|",
    ]
    for row in record["components"]:
        lines.append(
            f"| {md_cell(row['name'])} | {md_cell(row['kind'])} | {row['tokens']} | "
            f"{md_cell(row['count_status'])} | {md_cell(row['required'])} | {row['priority']} | {md_cell(row['source'])} |"
        )
    lines.extend(["", "## Drop Plan", ""])
    if record["drop_plan"]:
        lines.extend(["| Drop | Kind | Frees tokens | Remaining over by |", "|---|---|---:|---:|"])
        for item in record["drop_plan"]:
            lines.append(
                f"| {md_cell(item['name'])} | {md_cell(item['kind'])} | {item['tokens']} | "
                f"{item['remaining_over_by_after_drop']} |"
            )
    else:
        lines.append("No drop plan required for the current budget.")
    lines.extend(["", "## Notes", ""])
    for note in record["notes"]:
        lines.append(f"- {note}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


RUN_ROOT = Path(os.environ.get("LOCAL_LLM_RUN_ROOT", ".")).expanduser().resolve()
MANIFEST_PATH = Path(os.environ.get("LOCAL_LLM_CONTEXT_MANIFEST", RUN_ROOT / "context-budget-manifest.json")).expanduser().resolve()

OUT_DIR = RUN_ROOT / "context-window-budget-runner"
OUT_DIR.mkdir(parents=True, exist_ok=True)

if not MANIFEST_PATH.exists():
    sample = {
        "runtime": "ollama",
        "model": "<served-model-id>",
        "tokenizer": "served tokenizer or unknown",
        "context_limit_tokens": 8192,
        "reserved_output_tokens": 512,
        "safety_margin_tokens": 512,
        "token_count_method": "estimate",
        "components": [
            {
                "name": "system prompt",
                "kind": "system",
                "text": "You are a concise local assistant.",
                "priority": 100,
                "required": True,
            },
            {
                "name": "current user task",
                "kind": "user",
                "text": "Answer using only the supplied context.",
                "priority": 100,
                "required": True,
            },
        ],
    }
    write_json(MANIFEST_PATH, sample)
    print(json.dumps({
        "status": "template_written",
        "manifest": str(MANIFEST_PATH),
        "next_action": "fill the manifest and rerun",
    }, indent=2, ensure_ascii=True))
    raise SystemExit(0)

manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
components = manifest.get("components") if isinstance(manifest.get("components"), list) else []

run_id = f"{time.strftime('%Y%m%d-%H%M%S')}-context-budget"
timestamp = time.strftime("%Y-%m-%dT%H:%M:%S%z")
rows = [component_row(component, index + 1) for index, component in enumerate(components)]

context_limit = as_int(manifest.get("context_limit_tokens"))
reserved_output = as_int(manifest.get("reserved_output_tokens"))
safety_margin = as_int(manifest.get("safety_margin_tokens"))
if safety_margin == 0 and manifest.get("safety_margin_fraction") is not None:
    try:
        safety_margin = math.ceil(context_limit * float(manifest["safety_margin_fraction"]))
    except (TypeError, ValueError):
        safety_margin = 0

input_tokens = sum(row["tokens"] for row in rows)
total_planned = input_tokens + reserved_output + safety_margin
remaining = context_limit - total_planned
over_by = max(0, -remaining)
exact_count = len([row for row in rows if row["count_status"] == "exact"])
estimated_count = len(rows) - exact_count

notes = []
if estimated_count:
    notes.append("Some component counts are estimates; exact tokenizer or runtime counts are still needed before production use.")
if context_limit <= 0:
    notes.append("Context limit is missing or zero.")
if reserved_output <= 0:
    notes.append("Reserved output tokens are missing or zero; the answer may be starved.")
if not components:
    notes.append("No components were supplied in the manifest.")

drop_plan = build_drop_plan(rows, over_by)
if context_limit <= 0 or not components:
    status = "error"
    next_action = "fill context limit and prompt components before running inference"
elif over_by > 0:
    status = "hold"
    next_action = "drop or summarize low-priority context before running inference"
elif estimated_count:
    status = "hold"
    next_action = "replace estimated counts with served-tokenizer counts before final comparison"
else:
    status = "pass"
    next_action = "use this budget in benchmark, RAG, tool, or client-harness evidence"

record = {
    "run_id": run_id,
    "timestamp": timestamp,
    "status": status,
    "runtime": str(manifest.get("runtime") or ""),
    "model": str(manifest.get("model") or ""),
    "tokenizer": str(manifest.get("tokenizer") or ""),
    "token_count_method": str(manifest.get("token_count_method") or ""),
    "manifest_path": str(MANIFEST_PATH),
    "context_limit_tokens": context_limit,
    "input_tokens": input_tokens,
    "reserved_output_tokens": reserved_output,
    "safety_margin_tokens": safety_margin,
    "total_planned_tokens": total_planned,
    "remaining_tokens": remaining,
    "over_by_tokens": over_by,
    "exact_component_count": exact_count,
    "estimated_component_count": estimated_count,
    "components": rows,
    "drop_plan": drop_plan,
    "notes": notes,
    "next_action": next_action,
}

summary_json_path = OUT_DIR / f"{run_id}-context-budget-results.json"
summary_md_path = OUT_DIR / f"{run_id}-context-budget-results.md"
summary_csv_path = OUT_DIR / f"{run_id}-context-budget-components.csv"
jsonl_path = OUT_DIR / "context-budget-runs.jsonl"
normalized_manifest_path = OUT_DIR / f"{run_id}-normalized-manifest.json"

write_json(summary_json_path, record)
write_markdown(summary_md_path, record)
write_csv(summary_csv_path, rows)
write_json(normalized_manifest_path, manifest)
append_jsonl(jsonl_path, record)

print(json.dumps({
    "status": status,
    "run_id": run_id,
    "results_json": str(summary_json_path),
    "results_md": str(summary_md_path),
    "components_csv": str(summary_csv_path),
    "jsonl": str(jsonl_path),
    "normalized_manifest": str(normalized_manifest_path),
    "remaining_tokens": remaining,
    "over_by_tokens": over_by,
    "estimated_component_count": estimated_count,
    "next_action": next_action,
}, indent=2, ensure_ascii=True))
```

## PowerShell Execution

Create a manifest, then run:

```powershell
$env:LOCAL_LLM_RUN_ROOT = "D:\LLM-Runs\context-budget-$(Get-Date -Format yyyyMMdd-HHmmss)"
$env:LOCAL_LLM_CONTEXT_MANIFEST = "$env:LOCAL_LLM_RUN_ROOT\context-budget-manifest.json"
python .\context-window-budget-runner.py
```

If the manifest does not exist, the runner writes a template and exits with `template_written`. Fill exact counts when possible:

- use the served tokenizer or `apply_chat_template(..., tokenize=True)` for chat-template-aware counts
- use runtime `usage` fields or native timing fields when a probe has already run
- mark heuristic estimates as planning evidence, not final tokenizer proof

## Result Interpretation

| Runner status | Meaning | Next route |
|---|---|---|
| `pass` | Every component had exact counts and prompt plus output reserve plus margin fits. | [[LLM/Study/Local LLM First Benchmark Row Builder]] or [[LLM/Study/Local RAG Minimal Python Harness]] |
| `hold` | The request fits only with estimates, or it exceeds the limit and needs a drop plan. | [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]] |
| `error` | Context limit or prompt components are missing. | Fill the manifest before endpoint use. |
| `template_written` | A starter manifest was created. | Edit the manifest and rerun. |

An estimated `hold` is often enough before drafting a prompt. It is not enough before comparing models, diagnosing TTFT, or claiming a RAG/tool prompt fits.

## Completion Gate

This runner pass is complete when you have:

- [ ] a saved `context-budget-results.json`
- [ ] a saved `context-budget-results.md`
- [ ] a saved `context-budget-components.csv`
- [ ] one appended `context-budget-runs.jsonl` row
- [ ] a manifest listing system, user, history, RAG, tool/schema, reserve, margin, and context limit where relevant
- [ ] exact token counts for production or an explicit estimate-only hold
- [ ] a drop plan when the request does not fit
- [ ] a next route to benchmark row builder, RAG harness, tool lab, prompt-cache lab, or troubleshooting

## References

Internal routes:

- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/LLM Math and Tensor Shape Primer]]
- [[LLM/Study/Local LLM First Benchmark Row Builder]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab]]
- [[LLM/Study/Local RAG Assistant Lab]]
- [[LLM/Study/Local RAG Minimal Python Harness]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]

External/current docs checked 2026-06-15:

- [Ollama context length](https://docs.ollama.com/context-length)
- [Hugging Face chat templates](https://huggingface.co/docs/transformers/en/chat_templating)
- [vLLM engine arguments](https://docs.vllm.ai/en/stable/configuration/engine_args/)
