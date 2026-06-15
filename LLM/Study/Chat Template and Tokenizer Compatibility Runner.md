---
tags: [study, llm, inference, local-llm, tokenizer, chat-template, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-15
---

# Chat Template and Tokenizer Compatibility Runner

> **One-line summary** A local chat endpoint is trustworthy only after model package, tokenizer, special-token, chat-template, route, stop, and benchmark/quality evidence agree.

Use this after [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]] and [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]] when a local model responds but you need machine-checkable evidence that the request format is not the hidden failure layer.

This runner does not call the model. It audits evidence you already captured: model metadata, tokenizer/source facts, rendered prompt or non-exposure note, route behavior, tokenizer sanity counts, stop/role-boundary checks, and the benchmark or quality row that used the template.

## What This Proves

| Evidence family | Checks | Why it matters |
|---|---|---|
| Model package | model id, runtime, artifact/tag, model type | separates base/completion behavior from instruct/chat behavior |
| Tokenizer and special tokens | tokenizer source, BOS/EOS, role/tool tokens, context limit | explains token counts, truncation, detokenization, and role markers |
| Chat template | template source, assistant prefix, runtime setting, rendered shape | prevents silent role serialization bugs |
| Route behavior | chat route versus raw/completion route interpretation | separates API success from correct chat behavior |
| Tokenizer sanity set | token counts across English, mixed script, code, JSON, whitespace, and special-looking text | makes local latency and context comparisons fair |
| Stop and role boundary | EOS/stop policy, role-marker leakage, JSON/tool boundary if relevant | catches runaway output and malformed structured responses |
| Benchmark or quality link | downstream run that records template/tokenizer fields | keeps compatibility evidence attached to decisions |

Academic bridge: tokenization and instruction tuning are not side details. A chat model learned a serialized conversation format during post-training. If the runtime sends a different format, the observed failure belongs to request construction, not necessarily to model capability.

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "chat-template-compat-001",
  "run_root": "D:/llm-runs/chat-template-compat",
  "vault_root": "D:/Vaults/PersonalKB",
  "model_id": "llama3.1:8b-instruct-q4_K_M",
  "runtime": "Ollama",
  "route": "http://localhost:11434/v1/chat/completions",
  "runtime_exposes_rendered_prompt": false,
  "rows": [
    {
      "kind": "model_package",
      "status": "pass",
      "proof": "LLM/Study/Local LLM Runtime and Model Compatibility Matrix.md",
      "model_type": "chat",
      "artifact_or_tag": "llama3.1:8b-instruct-q4_K_M"
    },
    {
      "kind": "tokenizer_sanity",
      "status": "pass",
      "proof": "LLM/Study/Chat Template and Tokenizer Compatibility Lab.md",
      "token_counts": [
        {"text_class": "plain_english", "token_count": 5},
        {"text_class": "mixed_script", "token_count": 11},
        {"text_class": "code_identifier", "token_count": 4},
        {"text_class": "json_boundary", "token_count": 6}
      ]
    }
  ]
}
```

`proof` may be an absolute path, a vault-relative path, an Obsidian note path, or an Obsidian link. If the runtime does not expose the rendered prompt, include a `rendered_prompt` row with `runtime_does_not_expose: true`, a non-exposure note, and a behavior-control proof.

## Standard-Library Runner

Save this as `chat_template_tokenizer_compatibility_runner.py` inside the run folder. It uses only Python's standard library.

```python
from __future__ import annotations

import csv
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path
from typing import Any


STATUS_VALUES = {
    "pass": "pass",
    "passed": "pass",
    "complete": "pass",
    "ready": "pass",
    "ok": "pass",
    "hold": "hold",
    "blocked": "hold",
    "gap": "hold",
    "missing": "hold",
    "in-progress": "hold",
    "in progress": "hold",
    "fail": "fail",
    "failed": "fail",
    "error": "fail",
    "unsafe": "fail",
}

STATUS_RANK = {"pass": 0, "hold": 1, "fail": 2}
LINK_OPEN = "[" + "["
LINK_CLOSE = "]" + "]"

DEFAULT_REQUIRED_KINDS = [
    "model_package",
    "tokenizer_special_tokens",
    "chat_template",
    "rendered_prompt",
    "route_behavior",
    "tokenizer_sanity",
    "stop_role_boundary",
    "benchmark_or_quality_link",
]

KIND_HINTS = {
    "model_package": {
        "owner": "model package",
        "pass_signal": "Model id, runtime, model type, and artifact/tag are recorded.",
        "next_route": "LLM/Study/Local LLM Runtime and Model Compatibility Matrix",
    },
    "tokenizer_special_tokens": {
        "owner": "tokenizer",
        "pass_signal": "Tokenizer source, BOS/EOS policy, special tokens, and context limit are recorded.",
        "next_route": "LLM/Study/Chat Template and Tokenizer Compatibility Lab",
    },
    "chat_template": {
        "owner": "chat template",
        "pass_signal": "Template source, assistant prefix, runtime setting, and template shape are recorded.",
        "next_route": "LLM/Study/Chat Template and Tokenizer Compatibility Lab",
    },
    "rendered_prompt": {
        "owner": "rendered prompt",
        "pass_signal": "Rendered role order is checked, or non-exposure is documented with behavior controls.",
        "next_route": "LLM/Study/Chat Template and Tokenizer Compatibility Lab",
    },
    "route_behavior": {
        "owner": "route",
        "pass_signal": "Chat/messages route behavior is interpreted against raw/completion behavior or a skipped-route reason.",
        "next_route": "LLM/Study/Local LLM OpenAI-Compatible API Contract Lab",
    },
    "tokenizer_sanity": {
        "owner": "tokenizer",
        "pass_signal": "At least four tokenizer sanity examples have token counts.",
        "next_route": "LLM/Study/Local LLM Context Window and Token Budgeting Lab",
    },
    "stop_role_boundary": {
        "owner": "stop and role boundary",
        "pass_signal": "Stop/EOS policy, role-marker leakage, and structured-output boundary are checked.",
        "next_route": "LLM/Study/Chat Template and Tokenizer Compatibility Lab",
    },
    "benchmark_or_quality_link": {
        "owner": "decision evidence",
        "pass_signal": "A benchmark or quality row records the template/tokenizer fields used by the run.",
        "next_route": "LLM/Study/Local LLM Inference Benchmark Log",
    },
    "context_budget_link": {
        "owner": "context budget",
        "pass_signal": "Context-budget evidence is linked when history, RAG, or tool schemas are present.",
        "next_route": "LLM/Study/Local LLM Context Window and Token Budgeting Runner",
    },
}


def utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def slug(value: Any) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value or "").strip().lower())
    return text.strip("-") or "chat-template-tokenizer-compatibility"


def norm(value: Any) -> str:
    return str(value or "").strip().lower().replace(" ", "_").replace("-", "_")


def status_value(value: Any) -> str:
    return STATUS_VALUES.get(norm(value).replace("_", "-"), "hold")


def bool_value(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value in (None, ""):
        return default
    text = norm(value)
    if text in {"true", "yes", "y", "1", "ok", "pass", "checked", "present"}:
        return True
    if text in {"false", "no", "n", "0", "fail", "missing", "absent", "leaked"}:
        return False
    return default


def load_manifest() -> tuple[Path, dict[str, Any]]:
    manifest_path = os.environ.get("CHAT_TEMPLATE_COMPAT_MANIFEST")
    if not manifest_path:
        raise ValueError("Set CHAT_TEMPLATE_COMPAT_MANIFEST to a JSON manifest path.")
    path = Path(manifest_path).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"Manifest path does not exist: {path}")
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError("Manifest must be a JSON object.")
    return path, data


def strip_obsidian_link(value: str) -> str:
    text = value.strip()
    if text.startswith(LINK_OPEN) and text.endswith(LINK_CLOSE):
        inner = text[2:-2]
        return inner.split("|", 1)[0].split("#", 1)[0].strip()
    return text


def proof_candidates(vault_root: Path, proof: str) -> list[Path]:
    proof_text = strip_obsidian_link(proof)
    if not proof_text:
        return []
    path = Path(proof_text).expanduser()
    candidates: list[Path] = []
    if path.is_absolute():
        candidates.append(path)
        if path.suffix == "":
            candidates.append(path.with_suffix(".md"))
    else:
        candidates.append(vault_root / path)
        if path.suffix == "":
            candidates.append((vault_root / path).with_suffix(".md"))
    return [candidate.resolve() for candidate in candidates]


def proof_exists(vault_root: Path, proof: str) -> tuple[bool, str]:
    if not proof.strip():
        return False, ""
    candidates = proof_candidates(vault_root, proof)
    for candidate in candidates:
        if candidate.exists():
            return True, str(candidate)
    return False, str(candidates[0]) if candidates else proof


def wiki_link(route: str) -> str:
    return LINK_OPEN + route + LINK_CLOSE


def list_value(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, dict):
        return [value]
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            return []
        if stripped.startswith("["):
            try:
                parsed = json.loads(stripped)
                return parsed if isinstance(parsed, list) else []
            except json.JSONDecodeError:
                return []
        return [part.strip() for part in stripped.split(",") if part.strip()]
    return [value]


def has_text(row: dict[str, Any], *names: str) -> bool:
    return any(str(row.get(name) or "").strip() for name in names)


def finding(level: str, owner: str, text: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "owner": owner,
        "finding": text,
        "evidence": evidence,
        "action": action,
    }


def route_for_row(row: dict[str, Any], kind: str) -> str:
    route = str(row.get("next_route") or row.get("route") or row.get("proof") or "")
    if route:
        return strip_obsidian_link(route).removesuffix(".md")
    return KIND_HINTS.get(kind, {}).get("next_route", "LLM/Study/Chat Template and Tokenizer Compatibility Lab")


def count_token_rows(row: dict[str, Any]) -> int:
    token_counts = row.get("token_counts")
    if isinstance(token_counts, str):
        try:
            token_counts = json.loads(token_counts)
        except json.JSONDecodeError:
            token_counts = []
    count = 0
    for item in list_value(token_counts):
        if isinstance(item, dict) and has_text(item, "text_class", "example") and str(item.get("token_count") or "").strip():
            count += 1
    return count


def evaluate_kind_requirements(row: dict[str, Any], kind: str, manifest: dict[str, Any]) -> list[dict[str, str]]:
    owner = KIND_HINTS.get(kind, {}).get("owner", kind)
    findings: list[dict[str, str]] = []

    if kind == "model_package":
        if not has_text(row, "model_id") and not has_text(manifest, "model_id"):
            findings.append(finding("hold", owner, "Model id is missing.", kind, "Record the exact served model id or tag."))
        if not has_text(row, "runtime") and not has_text(manifest, "runtime"):
            findings.append(finding("hold", owner, "Runtime is missing.", kind, "Record Ollama, llama.cpp, vLLM, SGLang, LM Studio, or the exact runtime."))
        if not has_text(row, "model_type", "model_class"):
            findings.append(finding("hold", owner, "Model type is missing.", kind, "Classify the model as base, instruct, chat, code, tool, or embedding oriented."))
        if not has_text(row, "artifact_or_tag", "model_file", "package", "revision"):
            findings.append(finding("hold", owner, "Artifact, tag, or revision is missing.", kind, "Record the local tag, GGUF, Hugging Face revision, or package identity."))

    elif kind == "tokenizer_special_tokens":
        if not has_text(row, "tokenizer_source", "tokenizer_file", "tokenizer_config"):
            findings.append(finding("hold", owner, "Tokenizer source is missing.", kind, "Record tokenizer source from config, GGUF metadata, runtime info, or model card."))
        if not has_text(row, "bos_token", "eos_token", "special_tokens", "role_tokens"):
            findings.append(finding("hold", owner, "BOS/EOS or special-token evidence is missing.", kind, "Record BOS, EOS, role markers, tool markers, or an explicit not-exposed note."))
        if not has_text(row, "context_limit", "context_window", "n_ctx") and not has_text(manifest, "context_limit"):
            findings.append(finding("hold", owner, "Context limit is missing.", kind, "Record the context limit used by this endpoint."))

    elif kind == "chat_template":
        if not has_text(row, "chat_template_source", "template_source", "template_hash", "template_excerpt"):
            findings.append(finding("hold", owner, "Chat-template source is missing.", kind, "Record template source, template hash, rendered shape, or runtime template setting."))
        if not has_text(row, "assistant_prefix", "assistant_generation_marker", "template_shape", "template_excerpt"):
            findings.append(finding("hold", owner, "Assistant-generation marker or template shape is missing.", kind, "Record how the assistant turn begins."))
        if not has_text(row, "runtime_template_setting", "adapter_behavior", "template_applied_by"):
            findings.append(finding("hold", owner, "Runtime template setting is missing.", kind, "State whether the runtime applies the template or expects a pre-rendered prompt."))

    elif kind == "rendered_prompt":
        runtime_exposes = bool_value(row.get("runtime_exposes_rendered_prompt"), bool_value(manifest.get("runtime_exposes_rendered_prompt"), True))
        runtime_does_not_expose = bool_value(row.get("runtime_does_not_expose"), False) or not runtime_exposes
        if runtime_does_not_expose:
            if not has_text(row, "non_exposure_note", "not_exposed_reason"):
                findings.append(finding("hold", owner, "Runtime non-exposure note is missing.", kind, "Explain that the runtime does not expose the rendered prompt and how you controlled for it."))
            if not has_text(row, "behavior_control_proof", "route_behavior_proof", "proof"):
                findings.append(finding("hold", owner, "Rendered-prompt fallback proof is missing.", kind, "Link a route behavior or quality row that controls for template failure."))
        else:
            if not has_text(row, "rendered_prompt_excerpt", "role_order", "template_shape"):
                findings.append(finding("hold", owner, "Rendered prompt shape is missing.", kind, "Record a redacted rendered-prompt excerpt or role-order shape."))
            if not bool_value(row.get("role_order_checked"), False):
                findings.append(finding("hold", owner, "Role order was not checked.", kind, "Check system, user, assistant, and tool role boundaries."))
            if row.get("bos_eos_duplicated") is not None and bool_value(row.get("bos_eos_duplicated"), False):
                findings.append(finding("fail", owner, "BOS/EOS tokens appear duplicated.", kind, "Fix duplicate special tokens before using this endpoint for quality decisions."))

    elif kind == "route_behavior":
        if not has_text(row, "chat_route_result", "messages_route_result", "chat_output"):
            findings.append(finding("hold", owner, "Chat/messages route result is missing.", kind, "Record the intended chat route output or response shape."))
        if not has_text(row, "raw_route_result", "completion_route_result", "raw_route_skipped_reason"):
            findings.append(finding("hold", owner, "Raw/completion route control or skipped reason is missing.", kind, "Compare against a raw route when safe, or explain why it was skipped."))
        if not has_text(row, "interpretation", "decision", "finding"):
            findings.append(finding("hold", owner, "Route behavior interpretation is missing.", kind, "State whether behavior proves the chat template is being applied correctly."))

    elif kind == "tokenizer_sanity":
        minimum = int(manifest.get("minimum_tokenizer_examples") or 4)
        count = count_token_rows(row)
        if count < minimum:
            findings.append(finding("hold", owner, "Tokenizer sanity set has too few counted examples.", f"{count}/{minimum}", "Record token counts for English, mixed script, code, JSON, whitespace, or special-token-looking text."))

    elif kind == "stop_role_boundary":
        if not has_text(row, "stop_policy", "eos_policy", "stop_strings"):
            findings.append(finding("hold", owner, "Stop/EOS policy is missing.", kind, "Record EOS token, stop strings, max output tokens, or parser boundary."))
        if row.get("role_marker_leak") is None:
            findings.append(finding("hold", owner, "Role-marker leakage check is missing.", kind, "Record whether output leaked user, assistant, system, or special-token markers."))
        elif bool_value(row.get("role_marker_leak"), False):
            findings.append(finding("fail", owner, "Output leaked role or special-token markers.", kind, "Fix template, stop policy, or route before accepting quality evidence."))
        if not has_text(row, "stop_test_result", "multi_turn_result", "json_boundary_result", "tool_boundary_result"):
            findings.append(finding("hold", owner, "Stop or role-boundary test result is missing.", kind, "Run a stop sentinel, multi-turn role-order, JSON-only, or tool-boundary test."))

    elif kind == "benchmark_or_quality_link":
        if not has_text(row, "benchmark_proof", "quality_proof", "proof"):
            findings.append(finding("hold", owner, "Benchmark or quality proof is missing.", kind, "Link the benchmark or quality row that records template/tokenizer fields."))
        if not has_text(row, "template_fields_recorded", "recorded_fields", "decision"):
            findings.append(finding("hold", owner, "Template/tokenizer fields were not recorded downstream.", kind, "Record model type, tokenizer source, template source, rendered check, stop policy, and token counts in the downstream row."))

    elif kind == "context_budget_link":
        context_sensitive = bool_value(row.get("context_sensitive"), bool_value(manifest.get("context_sensitive"), False))
        if context_sensitive and not has_text(row, "context_budget_proof", "proof"):
            findings.append(finding("hold", owner, "Context-sensitive prompt has no context-budget proof.", kind, "Run the context-window/token-budgeting runner before long, RAG, tool, or multi-turn inference."))

    else:
        findings.append(finding("hold", owner, "Evidence kind is not recognized.", kind, "Use a known chat-template compatibility kind or add a waiver reason."))

    return findings


def evaluate_row(row: dict[str, Any], vault_root: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    kind = norm(row.get("kind") or row.get("evidence_kind"))
    row_id = str(row.get("row_id") or row.get("id") or kind or "row")
    required = bool_value(row.get("required"), kind in DEFAULT_REQUIRED_KINDS)
    critical = bool_value(row.get("critical"), kind in {"model_package", "tokenizer_special_tokens", "chat_template", "rendered_prompt", "stop_role_boundary"})
    declared_status = status_value(row.get("status"))
    proof = str(row.get("proof") or row.get("proof_path") or row.get("evidence_path") or "")
    findings: list[dict[str, str]] = []

    if not kind:
        findings.append(finding("hold", "manifest", "Evidence row kind is missing.", row_id, "Set kind to a required chat-template compatibility kind."))

    proof_resolved = ""
    proof_ok = False
    if proof:
        proof_ok, proof_resolved = proof_exists(vault_root, proof)
        if not proof_ok and required:
            findings.append(finding("hold", "proof", "Proof link or path does not resolve in the vault.", proof_resolved, "Fix the proof path or create the linked evidence."))
    elif required and not has_text(row, "waiver_reason"):
        findings.append(finding("hold", "proof", "Required evidence row has no proof link or path.", row_id, "Link the compatibility lab, API contract, benchmark, quality, or context-budget evidence."))

    if not required:
        if not has_text(row, "waiver_reason"):
            findings.append(finding("hold", "waiver", "Optional or skipped row has no waiver reason.", row_id, "Explain why this row is out of scope."))
    elif declared_status == "fail":
        findings.append(finding("fail", KIND_HINTS.get(kind, {}).get("owner", kind), "Evidence row is explicitly marked fail.", row_id, "Resolve this failed compatibility evidence before accepting the endpoint."))
    elif declared_status != "pass":
        findings.append(finding("hold", KIND_HINTS.get(kind, {}).get("owner", kind), "Evidence row is not marked pass.", declared_status, "Mark pass only after the evidence is complete."))

    if required:
        findings.extend(evaluate_kind_requirements(row, kind, manifest))

    fail_count = sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        status = "fail"
        decision = "compatibility_failed"
    elif hold_count:
        status = "hold"
        decision = "compatibility_incomplete"
    else:
        status = "pass"
        decision = "compatibility_evidence_ready"

    return {
        "row_id": row_id,
        "kind": kind,
        "required": required,
        "critical": critical,
        "declared_status": declared_status,
        "status": status,
        "decision": decision,
        "proof": proof,
        "proof_resolved": proof_resolved,
        "proof_exists": proof_ok,
        "owner": KIND_HINTS.get(kind, {}).get("owner", kind),
        "pass_signal": KIND_HINTS.get(kind, {}).get("pass_signal", ""),
        "next_route": route_for_row(row, kind),
        "next_action": findings[0]["action"] if findings else "Use this compatibility evidence before benchmark, quality, or deployment decisions.",
        "findings": findings,
    }


def missing_kind_row(kind: str) -> dict[str, Any]:
    return {
        "row_id": f"missing-{kind}",
        "kind": kind,
        "required": True,
        "critical": kind in {"model_package", "tokenizer_special_tokens", "chat_template", "rendered_prompt", "stop_role_boundary"},
        "declared_status": "missing",
        "status": "hold",
        "decision": "compatibility_incomplete",
        "proof": "",
        "proof_resolved": "",
        "proof_exists": False,
        "owner": KIND_HINTS.get(kind, {}).get("owner", kind),
        "pass_signal": KIND_HINTS.get(kind, {}).get("pass_signal", ""),
        "next_route": KIND_HINTS.get(kind, {}).get("next_route", "LLM/Study/Chat Template and Tokenizer Compatibility Lab"),
        "next_action": "Add this required evidence row to the manifest.",
        "findings": [finding("hold", KIND_HINTS.get(kind, {}).get("owner", kind), "Required evidence kind is missing.", kind, "Add this required evidence row to the manifest.")],
    }


def md_cell(value: Any) -> str:
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True)
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "row_id",
        "kind",
        "required",
        "critical",
        "declared_status",
        "status",
        "decision",
        "proof",
        "proof_resolved",
        "proof_exists",
        "owner",
        "pass_signal",
        "next_route",
        "next_action",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({name: row.get(name, "") for name in fieldnames})


def render_markdown(record: dict[str, Any]) -> str:
    lines = [
        f"# Chat Template and Tokenizer Compatibility - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Model: `{record['model_id']}`",
        f"- Runtime: `{record['runtime']}`",
        f"- Route: `{record['route']}`",
        f"- Rows: `{record['row_count']}`",
        f"- Critical gaps: `{record['critical_gap_count']}`",
        "",
        "## Evidence Rows",
        "",
        "| Row | Kind | Status | Critical | Owner | Next route |",
        "|---|---|---|---:|---|---|",
    ]
    for row in record["rows"]:
        lines.append(
            "| "
            + " | ".join([
                md_cell(row["row_id"]),
                md_cell(row["kind"]),
                md_cell(row["status"]),
                md_cell(row["critical"]),
                md_cell(row["owner"]),
                md_cell(wiki_link(row["next_route"])),
            ])
            + " |"
        )
    lines.extend(["", "## Next Actions", ""])
    incomplete = [row for row in record["rows"] if row["status"] != "pass"]
    for row in incomplete:
        lines.append(f"- `{row['row_id']}` -> {wiki_link(row['next_route'])}: {row['next_action']}")
    if not incomplete:
        lines.append("- Template/tokenizer compatibility evidence is ready to support benchmark, quality, and deployment decisions.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    manifest_path, manifest = load_manifest()
    vault_root = Path(manifest.get("vault_root") or os.environ.get("CHAT_TEMPLATE_COMPAT_VAULT_ROOT") or manifest_path.parent).expanduser().resolve()
    run_id = str(manifest.get("run_id") or os.environ.get("CHAT_TEMPLATE_COMPAT_RUN_ID") or f"{utc_stamp()}-{slug(manifest_path.stem)}")
    run_root_value = os.environ.get("CHAT_TEMPLATE_COMPAT_RUN_ROOT") or manifest.get("run_root", "chat-template-tokenizer-compatibility-runs")
    run_root = Path(str(run_root_value)).expanduser()
    if not run_root.is_absolute():
        run_root = manifest_path.parent / run_root
    run_root = run_root.resolve()
    run_dir = run_root / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    rows = manifest.get("rows")
    if rows is None:
        rows = manifest.get("evidence_rows")
    if not isinstance(rows, list) or not all(isinstance(row, dict) for row in rows):
        raise ValueError("Manifest rows must be a list of objects.")

    required_kinds = list_value(manifest.get("required_kinds")) or list(DEFAULT_REQUIRED_KINDS)
    if bool_value(manifest.get("context_sensitive"), False) and "context_budget_link" not in required_kinds:
        required_kinds.append("context_budget_link")

    evaluated = [evaluate_row(dict(row), vault_root, manifest) for row in rows]
    present_kinds = {row["kind"] for row in evaluated}
    for kind in required_kinds:
        normalized = norm(kind)
        if normalized not in present_kinds:
            evaluated.append(missing_kind_row(normalized))

    evaluated.sort(key=lambda row: (
        STATUS_RANK.get(row["status"], 3),
        0 if row["critical"] else 1,
        row["kind"],
        row["row_id"],
    ))

    pass_count = sum(1 for row in evaluated if row["status"] == "pass")
    hold_count = sum(1 for row in evaluated if row["status"] == "hold")
    fail_count = sum(1 for row in evaluated if row["status"] == "fail")
    critical_gap_count = sum(1 for row in evaluated if row["critical"] and row["status"] != "pass")

    if fail_count:
        status = "fail"
        decision = "chat_template_compatibility_failed"
    elif hold_count or critical_gap_count:
        status = "hold"
        decision = "chat_template_compatibility_incomplete"
    else:
        status = "pass"
        decision = "chat_template_compatibility_ready"

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "manifest_path": str(manifest_path),
        "vault_root": str(vault_root),
        "model_id": str(manifest.get("model_id") or ""),
        "runtime": str(manifest.get("runtime") or ""),
        "route": str(manifest.get("route") or ""),
        "row_count": len(evaluated),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "critical_gap_count": critical_gap_count,
        "rows": evaluated,
        "outputs": {},
    }

    json_path = run_dir / f"{run_id}-chat-template-compatibility.json"
    markdown_path = run_dir / f"{run_id}-chat-template-compatibility.md"
    csv_path = run_dir / f"{run_id}-chat-template-compatibility.csv"
    jsonl_path = run_root / "chat-template-tokenizer-compatibility-runs.jsonl"
    record["outputs"] = {
        "json": str(json_path),
        "markdown": str(markdown_path),
        "csv": str(csv_path),
        "jsonl": str(jsonl_path),
    }

    csv_write(csv_path, evaluated)
    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=True), encoding="utf-8")
    markdown_path.write_text(render_markdown(record), encoding="utf-8")
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=True) + "\n")

    print(json.dumps({
        "status": status,
        "decision": decision,
        "run_id": run_id,
        "row_count": len(evaluated),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "critical_gap_count": critical_gap_count,
        "output_dir": str(run_dir),
    }, indent=2))
    return 0 if status == "pass" else 1 if status == "hold" else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"status": "error", "decision": "runner_exception", "error": str(exc)}, indent=2), file=sys.stderr)
        raise SystemExit(3)
```

## PowerShell Run

```powershell
$env:CHAT_TEMPLATE_COMPAT_MANIFEST = "D:\llm-runs\chat-template-compat\chat-template-compat-manifest.json"
$env:CHAT_TEMPLATE_COMPAT_VAULT_ROOT = "D:\Vaults\PersonalKB"
$env:CHAT_TEMPLATE_COMPAT_RUN_ROOT = "D:\llm-runs\chat-template-compat"
python .\chat_template_tokenizer_compatibility_runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/chat_template_compatibility_ready` | model package, tokenizer, special-token, template, route, stop, and downstream decision evidence are complete | use this compatibility packet before benchmark, quality, or deployment decisions |
| `hold/chat_template_compatibility_incomplete` | required evidence is missing, proof links do not resolve, token counts are too thin, or rendered-prompt fallback is weak | fill the compatibility lab row, API contract row, benchmark row, or context-budget row |
| `fail/chat_template_compatibility_failed` | explicit failure, duplicated BOS/EOS, role-marker leakage, or stop/template boundary failure is present | fix request formatting, template selection, route, or stop policy before judging model quality |

## Capstone Row

| Gate | Required artifact | Pass signal |
|---|---|---|
| Chat template and tokenizer compatibility | `<run-id>-chat-template-compatibility.json`, `<run-id>-chat-template-compatibility.md`, `<run-id>-chat-template-compatibility.csv`, and one `chat-template-tokenizer-compatibility-runs.jsonl` row | model package, tokenizer, special tokens, chat template, rendered prompt or non-exposure control, route behavior, tokenizer sanity counts, stop/role boundary, and downstream benchmark or quality evidence are linked |

## Completion Gate

- [ ] model id, runtime, model type, artifact/tag, tokenizer source, special tokens, context limit, and stop policy are recorded
- [ ] chat template source and assistant-generation marker are recorded
- [ ] rendered prompt shape is checked, or runtime non-exposure is documented with behavior controls
- [ ] chat/messages route behavior is interpreted against a raw route or skipped-route reason
- [ ] tokenizer sanity set has at least four counted examples
- [ ] role-marker leakage and stop/EOS behavior are checked
- [ ] benchmark or quality evidence records template/tokenizer fields
- [ ] context-budget proof is linked when history, RAG, tool schemas, or long prompts are involved

## References

- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Pre-2017 — Before Transformers/Tokenization]]
- [[LLM/2022 — Alignment and Chat/Instruction Tuning]]
- [[LLM/2022 — Alignment and Chat/System Prompts and Role Conditioning]]
- [[LLM/2023 — Open Models and Agents/Structured Output and Constrained Generation]]
