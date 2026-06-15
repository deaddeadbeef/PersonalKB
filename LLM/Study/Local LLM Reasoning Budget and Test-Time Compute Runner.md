---
tags: [study, llm, reasoning, inference, local-llm, test-time-compute, audit, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-15
---

# Local LLM Reasoning Budget and Test-Time Compute Runner

> **One-line summary** Reasoning mode should become a local inference decision only after saved evidence proves the trigger, parser, effort sweep, latency cost, quality delta, trace policy, and retest trigger.

Use this after [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Lab|Local LLM Reasoning Budget and Test-Time Compute Lab]] has produced raw response, timing, and quality rows. Use it before [[LLM/Study/Local LLM Runtime Comparison Lab|Local LLM Runtime Comparison Lab]], [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]], [[LLM/Study/Local LLM Result Synthesis Runner|Local LLM Result Synthesis Runner]], or [[LLM/Study/LLM Deployment Readiness Audit Runner|LLM Deployment Readiness Audit Runner]] when a keep/tune/reject decision depends on thinking mode, reasoning effort, parser separation, or trace retention.

This runner does not call a model. It audits the evidence you already saved from client runs, benchmark rows, quality rows, parser checks, trace-policy notes, and deployment decisions.

## What This Proves

| Evidence family | Checks | Why it matters |
|---|---|---|
| Capability and trigger | model/runtime, control field, reasoning setting, parser setting | avoids assuming a runtime honored a thinking or effort field |
| Parser separation | reasoning output shape, final-answer field, inline-tag decision | prevents raw reasoning traces from being mistaken for final answer quality |
| Controlled sweep | two or more effort settings with fixed prompt, sampler, route, and output cap | makes quality and latency differences attributable to reasoning budget |
| Cost and quality | TTFT/latency, token or trace length, quality result, quality delta | shows whether more test-time compute is worth the user-visible cost |
| Trace policy | show/hide/log/redact/disable policy plus review for risky sharing | prevents accidental retention or export of private reasoning traces |
| Decision | selected effort, use policy, failure owner, retest trigger | turns the experiment into a reproducible local inference choice |

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "reasoning-budget-2026-06-15",
  "run_root": "D:/llm-runs/reasoning-budget",
  "vault_root": "D:/Vaults/PersonalKB",
  "workload": "private research assistant",
  "model_id": "qwen3:8b",
  "runtime": "Ollama",
  "route": "http://127.0.0.1:11434/v1/chat/completions",
  "prompt_id": "logic-control-001",
  "sampler_contract": "temperature=0, top_p=1, max_output_tokens=512",
  "output_cap": 512,
  "trials": [
    {
      "trial_id": "off",
      "status": "pass",
      "proof": "D:/llm-runs/reasoning-budget/off-response.json",
      "reasoning_setting": "off",
      "control_field": "think",
      "parser_setting": "none",
      "reasoning_output_shape": "disabled",
      "raw_response_artifact": "D:/llm-runs/reasoning-budget/off-response.json",
      "final_answer_artifact": "D:/llm-runs/reasoning-budget/off-output.txt",
      "trace_visibility_policy": "disabled",
      "quality_result": "baseline correct but terse",
      "quality_score": 3,
      "ttft_ms": 300,
      "total_latency_ms": 2400,
      "output_tokens": 96
    },
    {
      "trial_id": "medium",
      "status": "pass",
      "proof": "D:/llm-runs/reasoning-budget/medium-response.json",
      "reasoning_setting": "medium",
      "control_field": "think",
      "parser_setting": "ollama thinking field",
      "reasoning_output_shape": "separate_field",
      "raw_response_artifact": "D:/llm-runs/reasoning-budget/medium-response.json",
      "final_answer_artifact": "D:/llm-runs/reasoning-budget/medium-output.txt",
      "trace_visibility_policy": "hide",
      "quality_result": "improves planning without exposing trace",
      "quality_score": 5,
      "ttft_ms": 500,
      "total_latency_ms": 5200,
      "reasoning_tokens_or_chars": 1400,
      "output_tokens": 132
    }
  ],
  "decision": {
    "selected_effort": "medium",
    "use_policy": "use reasoning only for planning prompts",
    "quality_delta": 2,
    "latency_delta_ms": 2800,
    "token_impact": "adds about 1400 trace chars and 36 final-answer tokens",
    "failure_owner": "quality",
    "retest_trigger": "new model, runtime parser, prompt suite, or privacy boundary"
  }
}
```

`proof`, `raw_response_artifact`, `final_answer_artifact`, `quality_artifact`, `benchmark_artifact`, `parser_artifact`, `trace_policy_artifact`, and `review_artifact` may be absolute paths, vault-relative paths, Obsidian note paths, or Obsidian links.

## Row Contract

| Field | Required when | Meaning |
|---|---|---|
| `trial_id` | always | stable id for one effort setting |
| `status` | always | `pass`, `hold`, or `fail` for the saved trial |
| `proof` | always | primary evidence note or raw response path |
| `model_id`, `runtime`, `route`, `prompt_id` | always, unless inherited from manifest | identifies what was tested |
| `reasoning_setting` | always | off/none/low/medium/high or runtime-specific value |
| `control_field` | always | request field, parser flag, template setting, or UI control |
| `parser_setting` or `reasoning_output_shape` | always | how reasoning was separated, hidden, inline, disabled, or unavailable |
| `raw_response_artifact` | always | exact response or event log |
| `final_answer_artifact` or `final_answer_excerpt` | always | final answer evidence separate from trace evidence |
| `trace_visibility_policy` | always | show, hide, log_locally, redact, disable, or reviewed external share |
| `quality_result`, `quality_score`, or `quality_artifact` | always | workload quality signal for this effort level |
| `ttft_ms`, `total_latency_ms`, or `tokens_per_second` | always | user-visible cost evidence |
| `output_tokens`, `reasoning_tokens_or_chars`, or `trace_length` | recommended | separates reasoning cost from final answer cost |
| `review_artifact` | risky trace sharing or unsafe trace policy | proof that retention/export was reviewed |

The manifest-level `decision` should include `selected_effort`, `use_policy`, `quality_delta`, `latency_delta_ms` or latency rationale, `token_impact`, `failure_owner`, and `retest_trigger`.

## Standard-Library Runner

Save this as `local_llm_reasoning_budget_runner.py` inside the run folder. It uses only Python's standard library.

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
    "ready": "pass",
    "complete": "pass",
    "hold": "hold",
    "partial": "hold",
    "incomplete": "hold",
    "todo": "hold",
    "fail": "fail",
    "failed": "fail",
    "blocked": "fail",
    "reject": "fail",
    "rejected": "fail",
}

USE_DECISIONS = {
    "use",
    "use_reasoning",
    "use reasoning",
    "use_high",
    "use high",
    "use_medium",
    "use medium",
    "enable",
    "enable_reasoning",
    "route_hard_prompts",
    "planning_only",
}

RISKY_TRACE_POLICIES = {
    "share",
    "share_external",
    "external",
    "upload",
    "export",
    "log_unredacted",
    "log unredacted",
    "public",
}


def utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def slug(value: str) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip())
    return text.strip("-") or "reasoning-budget"


def status_value(value: Any) -> str:
    key = str(value or "hold").strip().lower().replace("_", " ")
    return STATUS_VALUES.get(key, "hold")


def text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (list, tuple, set)):
        return ", ".join(text(item) for item in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=True, sort_keys=True)
    return str(value).strip()


def has_text(row: dict[str, Any], *names: str) -> bool:
    return any(text(row.get(name)) for name in names)


def numeric(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    raw = text(value)
    if not raw:
        return None
    match = re.search(r"-?\d+(?:\.\d+)?", raw)
    if not match:
        return None
    try:
        return float(match.group(0))
    except ValueError:
        return None


def bool_value(value: Any, default: bool = False) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "pass", "required"}


def unwrap_link(value: str) -> str:
    raw = text(value)
    if raw.startswith("[" * 2) and raw.endswith("]" * 2):
        raw = raw[2:-2]
    raw = raw.split("|", 1)[0].split("#", 1)[0].strip()
    return raw


def proof_exists(vault_root: Path, value: Any) -> tuple[bool, str]:
    raw = unwrap_link(text(value))
    if not raw:
        return False, ""
    candidates: list[Path] = []
    path = Path(raw).expanduser()
    if path.is_absolute():
        candidates.append(path)
    else:
        candidates.append((vault_root / raw).resolve())
        if not raw.lower().endswith(".md"):
            candidates.append((vault_root / f"{raw}.md").resolve())
    for candidate in candidates:
        if candidate.exists():
            return True, str(candidate)
    return False, str(candidates[0]) if candidates else raw


def finding(level: str, owner: str, message: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "owner": owner,
        "message": message,
        "evidence": evidence,
        "action": action,
    }


def inherited(row: dict[str, Any], manifest: dict[str, Any], key: str) -> str:
    return text(row.get(key) or manifest.get(key))


def trace_policy(row: dict[str, Any], manifest: dict[str, Any]) -> str:
    return text(row.get("trace_visibility_policy") or row.get("trace_policy") or manifest.get("trace_visibility_policy") or manifest.get("trace_policy")).lower().replace("-", "_")


def decision_text(manifest: dict[str, Any]) -> str:
    decision = manifest.get("decision")
    if isinstance(decision, dict):
        return text(decision.get("decision") or decision.get("use_policy") or decision.get("selected_policy"))
    return text(decision)


def decision_map(manifest: dict[str, Any]) -> dict[str, Any]:
    decision = manifest.get("decision")
    return decision if isinstance(decision, dict) else {}


def output_shape(row: dict[str, Any]) -> str:
    return text(row.get("reasoning_output_shape") or row.get("output_shape") or row.get("parser_result")).lower().replace("-", "_")


def evaluate_trial(row: dict[str, Any], manifest: dict[str, Any], vault_root: Path) -> dict[str, Any]:
    trial_id = text(row.get("trial_id") or row.get("id") or row.get("name"))
    status = status_value(row.get("status"))
    proof = text(row.get("proof") or row.get("proof_path") or row.get("evidence"))
    findings: list[dict[str, str]] = []

    if not trial_id:
        findings.append(finding("hold", "trial", "Trial id is missing.", text(row), "Give every effort setting a stable trial_id."))
    if status == "fail":
        findings.append(finding("fail", trial_id or "trial", "Trial is explicitly marked failed.", status, "Resolve or exclude the failed reasoning-budget trial before using the sweep."))
    elif status != "pass":
        findings.append(finding("hold", trial_id or "trial", "Trial is not marked pass.", status, "Set status to pass only after the saved response, timing, parser, and quality rows are reviewed."))

    proof_resolved = ""
    proof_ok = False
    if proof:
        proof_ok, proof_resolved = proof_exists(vault_root, proof)
        if not proof_ok:
            findings.append(finding("hold", trial_id or "trial", "Primary proof path does not resolve.", proof_resolved, "Fix the proof path or create the linked evidence artifact."))
    else:
        findings.append(finding("hold", trial_id or "trial", "Trial has no primary proof link.", trial_id, "Link the raw response, run folder, benchmark row, or evidence note."))

    for key, owner, label, action in [
        ("model_id", "model", "model id", "Record the exact local model id or inherit it at manifest level."),
        ("runtime", "runtime", "runtime", "Record Ollama, LM Studio, llama.cpp, vLLM, SGLang, or the tested runtime."),
        ("route", "route", "route or endpoint", "Record the API route, UI path, or client boundary."),
        ("prompt_id", "prompt", "prompt id", "Record the frozen prompt id used for the effort sweep."),
    ]:
        if not inherited(row, manifest, key):
            findings.append(finding("hold", owner, f"Trial has no {label}.", trial_id, action))

    if not has_text(row, "reasoning_setting", "effort", "thinking_mode"):
        findings.append(finding("hold", "reasoning", "Trial has no reasoning setting or effort value.", trial_id, "Record off, none, low, medium, high, or runtime-specific value."))
    if not has_text(row, "control_field", "trigger", "request_field", "parser_flag", "template_setting"):
        findings.append(finding("hold", "trigger", "Trial has no reasoning control field.", trial_id, "Record the request field, parser flag, template setting, or UI control."))
    if not (has_text(row, "parser_setting", "reasoning_output_shape", "parser_artifact") or output_shape(row) in {"disabled", "unsupported", "hidden"}):
        findings.append(finding("hold", "parser", "Trial has no parser setting or reasoning-output shape.", trial_id, "Record separate field, inline tags, hidden, disabled, unsupported, parser name, or parser artifact."))

    shape = output_shape(row)
    if "inline" in shape and not has_text(row, "inline_tag_decision", "parser_artifact", "failure_owner"):
        findings.append(finding("hold", "parser", "Inline reasoning trace has no parser or final-answer separation decision.", shape, "Record whether inline tags are accepted for learning only, parsed, hidden, or a route failure."))

    if not has_text(row, "raw_response_artifact", "raw_response", "event_log"):
        findings.append(finding("hold", "response", "Trial has no raw response artifact.", trial_id, "Link the exact JSON response, streaming event log, or UI export."))
    if not has_text(row, "final_answer_artifact", "final_answer_excerpt", "final_answer"):
        findings.append(finding("hold", "answer", "Trial has no final-answer artifact or excerpt.", trial_id, "Link or excerpt the final answer separately from any reasoning trace."))
    if not has_text(row, "quality_result", "quality_score", "quality_artifact", "rubric_result"):
        findings.append(finding("hold", "quality", "Trial has no quality result.", trial_id, "Link a rubric row or record the pass/hold/fail quality result."))
    if not (has_text(row, "ttft_ms", "total_latency_ms", "latency_ms", "tokens_per_second") or isinstance(row.get("metrics"), dict)):
        findings.append(finding("hold", "latency", "Trial has no timing metric.", trial_id, "Record TTFT, total latency, tokens/sec, or a linked metrics artifact."))

    policy = trace_policy(row, manifest)
    if not policy:
        findings.append(finding("hold", "trace policy", "Trial has no trace visibility policy.", trial_id, "Record show, hide, log_locally, redact, disable, or reviewed external share."))
    if policy in RISKY_TRACE_POLICIES and not has_text(row, "review_artifact", "trace_policy_artifact", "privacy_review"):
        findings.append(finding("fail", "trace policy", "Risky trace sharing or unredacted logging has no review artifact.", policy, "Do not export or retain reasoning traces without a linked privacy/security review."))

    fail_count = sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        row_status = "fail"
        row_decision = "trial_failed"
    elif hold_count:
        row_status = "hold"
        row_decision = "trial_incomplete"
    else:
        row_status = "pass"
        row_decision = "trial_ready"

    return {
        "trial_id": trial_id,
        "status": row_status,
        "decision": row_decision,
        "declared_status": status,
        "proof": proof,
        "proof_resolved": proof_resolved,
        "proof_exists": proof_ok,
        "model_id": inherited(row, manifest, "model_id"),
        "runtime": inherited(row, manifest, "runtime"),
        "route": inherited(row, manifest, "route"),
        "prompt_id": inherited(row, manifest, "prompt_id"),
        "reasoning_setting": text(row.get("reasoning_setting") or row.get("effort") or row.get("thinking_mode")),
        "control_field": text(row.get("control_field") or row.get("trigger") or row.get("request_field") or row.get("parser_flag") or row.get("template_setting")),
        "reasoning_output_shape": text(row.get("reasoning_output_shape") or row.get("output_shape") or row.get("parser_result")),
        "trace_visibility_policy": policy,
        "quality_score": text(row.get("quality_score") or row.get("score") or ""),
        "quality_result": text(row.get("quality_result") or row.get("rubric_result") or ""),
        "ttft_ms": text(row.get("ttft_ms") or ""),
        "total_latency_ms": text(row.get("total_latency_ms") or row.get("latency_ms") or ""),
        "reasoning_tokens_or_chars": text(row.get("reasoning_tokens_or_chars") or row.get("trace_length") or row.get("reasoning_tokens") or ""),
        "output_tokens": text(row.get("output_tokens") or row.get("final_answer_tokens") or ""),
        "next_action": findings[0]["action"] if findings else "Use this trial in the reasoning-budget decision card.",
        "findings": findings,
    }


def evaluate_manifest(manifest: dict[str, Any], evaluated: list[dict[str, Any]], vault_root: Path) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not has_text(manifest, "workload"):
        findings.append(finding("hold", "workload", "Manifest has no workload.", "(manifest)", "Name the user task or product workflow that reasoning mode is supposed to improve."))
    if not has_text(manifest, "model_id"):
        findings.append(finding("hold", "model", "Manifest has no model id.", "(manifest)", "Record the exact reasoning-capable model id at manifest or trial level."))
    if not has_text(manifest, "runtime"):
        findings.append(finding("hold", "runtime", "Manifest has no runtime.", "(manifest)", "Record the local runtime or UI under test."))
    if not has_text(manifest, "sampler_contract"):
        findings.append(finding("hold", "controls", "Manifest has no sampler contract.", "(manifest)", "Freeze sampler settings so the effort sweep changes only reasoning budget."))
    if not (has_text(manifest, "output_cap", "max_output_tokens") or any(row.get("output_tokens") for row in evaluated)):
        findings.append(finding("hold", "controls", "Manifest has no output cap or token evidence.", "(manifest)", "Record max output tokens or final-answer token counts."))

    settings = {row["reasoning_setting"].strip().lower() for row in evaluated if row["reasoning_setting"].strip()}
    if len(evaluated) < 2 or len(settings) < 2:
        findings.append(finding("hold", "sweep", "Reasoning budget sweep has fewer than two distinct effort settings.", ",".join(sorted(settings)), "Compare off/none/low against at least one higher effort or the closest supported alternatives."))

    prompts = {row["prompt_id"] for row in evaluated if row["prompt_id"]}
    models = {row["model_id"] for row in evaluated if row["model_id"]}
    runtimes = {row["runtime"] for row in evaluated if row["runtime"]}
    routes = {row["route"] for row in evaluated if row["route"]}
    if len(prompts) > 1:
        findings.append(finding("hold", "controlled sweep", "Sweep uses multiple prompt ids.", ", ".join(sorted(prompts)), "Keep the prompt fixed or split this into separate manifests."))
    if len(models) > 1:
        findings.append(finding("hold", "controlled sweep", "Sweep uses multiple model ids.", ", ".join(sorted(models)), "Keep the model fixed or use the runtime comparison route."))
    if len(runtimes) > 1:
        findings.append(finding("hold", "controlled sweep", "Sweep uses multiple runtimes.", ", ".join(sorted(runtimes)), "Keep the runtime fixed or use Local LLM Runtime Comparison Lab."))
    if len(routes) > 1:
        findings.append(finding("hold", "controlled sweep", "Sweep uses multiple routes.", ", ".join(sorted(routes)), "Keep the route fixed or record separate API-contract evidence first."))

    decision = decision_map(manifest)
    decision_raw = decision_text(manifest)
    if not decision:
        findings.append(finding("hold", "decision", "Manifest has no decision card.", "(manifest)", "Add selected_effort, use_policy, quality_delta, latency_delta, token_impact, failure_owner, and retest_trigger."))
    else:
        for key, label, action in [
            ("selected_effort", "selected effort", "Choose off, low, medium, high, or a runtime-specific policy."),
            ("use_policy", "use policy", "State when reasoning is used, reduced, disabled, or rejected."),
            ("quality_delta", "quality delta", "Record measured quality difference versus low/off."),
            ("token_impact", "token impact", "Record reasoning trace length, output tokens, or cost impact."),
            ("retest_trigger", "retest trigger", "Name what invalidates this reasoning-budget decision."),
        ]:
            if not has_text(decision, key):
                findings.append(finding("hold", "decision", f"Decision card has no {label}.", key, action))
        if not (has_text(decision, "latency_delta_ms", "latency_delta", "latency_rationale") or any(row["total_latency_ms"] for row in evaluated)):
            findings.append(finding("hold", "decision", "Decision card has no latency delta or rationale.", "decision", "Record latency cost versus low/off or explain why it is unavailable."))

    normalized_decision = decision_raw.strip().lower().replace("-", "_")
    quality_delta = numeric(decision.get("quality_delta")) if decision else None
    if normalized_decision in USE_DECISIONS and (quality_delta is None or quality_delta <= 0):
        findings.append(finding("hold", "decision", "Decision enables reasoning without a positive quality delta.", text(decision.get("quality_delta") if decision else ""), "Use reasoning only when quality evidence improves enough to justify latency and trace policy."))

    for link_key in ("quality_artifact", "benchmark_artifact", "parser_artifact", "trace_policy_artifact", "review_artifact"):
        value = manifest.get(link_key)
        if value:
            exists, resolved = proof_exists(vault_root, value)
            if not exists:
                findings.append(finding("hold", "manifest proof", f"Manifest {link_key} does not resolve.", resolved, "Fix the manifest-level proof path or create the linked artifact."))

    return findings


def csv_cell(value: Any) -> str:
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=True)
    return text(value)


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "trial_id",
        "status",
        "decision",
        "declared_status",
        "proof",
        "model_id",
        "runtime",
        "route",
        "prompt_id",
        "reasoning_setting",
        "control_field",
        "reasoning_output_shape",
        "trace_visibility_policy",
        "quality_score",
        "quality_result",
        "ttft_ms",
        "total_latency_ms",
        "reasoning_tokens_or_chars",
        "output_tokens",
        "next_action",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: csv_cell(row.get(field)) for field in fields})


def render_markdown(record: dict[str, Any]) -> str:
    lines = [
        f"# Local LLM Reasoning Budget Audit - {record['run_id']}",
        "",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Workload: `{record.get('workload') or ''}`",
        f"- Model: `{record.get('model_id') or ''}`",
        f"- Runtime: `{record.get('runtime') or ''}`",
        f"- Trial count: `{record['trial_count']}`",
        f"- Pass/Hold/Fail: `{record['pass_count']}/{record['hold_count']}/{record['fail_count']}`",
        "",
        "## Manifest Findings",
        "",
    ]
    if record["manifest_findings"]:
        for item in record["manifest_findings"]:
            lines.append(f"- `{item['level']}` {item['message']} Evidence: `{item['evidence']}` Action: {item['action']}")
    else:
        lines.append("- No manifest-level findings.")

    lines.extend([
        "",
        "## Trials",
        "",
        "| Trial | Status | Setting | Shape | Policy | Quality | Latency | Next action |",
        "|---|---|---|---|---|---|---:|---|",
    ])
    for row in record["trials"]:
        latency = row.get("total_latency_ms") or row.get("ttft_ms") or ""
        lines.append(
            f"| {row['trial_id']} | {row['status']} | {row['reasoning_setting']} | {row['reasoning_output_shape']} | {row['trace_visibility_policy']} | {row['quality_result'] or row['quality_score']} | {latency} | {row['next_action']} |"
        )
        for item in row["findings"]:
            lines.append(f"|  | `{item['level']}` |  |  |  | {item['message']} |  | {item['action']} |")
    return "\n".join(lines) + "\n"


def load_manifest() -> tuple[Path, dict[str, Any]]:
    manifest_value = os.environ.get("LOCAL_LLM_REASONING_BUDGET_AUDIT_MANIFEST")
    if not manifest_value:
        raise ValueError("Set LOCAL_LLM_REASONING_BUDGET_AUDIT_MANIFEST to a JSON manifest path.")
    manifest_path = Path(manifest_value).expanduser().resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict):
        raise ValueError("Manifest must be a JSON object.")
    return manifest_path, manifest


def main() -> int:
    manifest_path, manifest = load_manifest()
    base_for_relative = manifest_path.parent
    run_root_value = os.environ.get("LOCAL_LLM_REASONING_BUDGET_AUDIT_RUN_ROOT") or manifest.get("run_root") or base_for_relative
    run_root = Path(str(run_root_value)).expanduser()
    if not run_root.is_absolute():
        run_root = (base_for_relative / run_root).resolve()
    else:
        run_root = run_root.resolve()
    vault_root_value = manifest.get("vault_root") or os.environ.get("LOCAL_LLM_REASONING_BUDGET_AUDIT_VAULT_ROOT") or "."
    vault_root = Path(str(vault_root_value)).expanduser().resolve()
    run_id = text(manifest.get("run_id") or os.environ.get("LOCAL_LLM_REASONING_BUDGET_AUDIT_RUN_ID") or f"{utc_stamp()}-{slug(manifest_path.stem)}")
    output_root_value = manifest.get("output_root") or os.environ.get("LOCAL_LLM_REASONING_BUDGET_AUDIT_OUTPUT_ROOT") or "reasoning-budget-audits"
    output_root = Path(str(output_root_value)).expanduser()
    if not output_root.is_absolute():
        output_root = run_root / output_root
    output_dir = (output_root / run_id).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    trials = manifest.get("trials")
    if not isinstance(trials, list) or not all(isinstance(row, dict) for row in trials):
        raise ValueError("Manifest trials must be a list of objects.")

    evaluated = [evaluate_trial(dict(row), manifest, vault_root) for row in trials]
    manifest_findings = evaluate_manifest(manifest, evaluated, vault_root)

    pass_count = sum(1 for row in evaluated if row["status"] == "pass")
    hold_count = sum(1 for row in evaluated if row["status"] == "hold")
    fail_count = sum(1 for row in evaluated if row["status"] == "fail")
    manifest_fail_count = sum(1 for item in manifest_findings if item["level"] == "fail")
    manifest_hold_count = sum(1 for item in manifest_findings if item["level"] == "hold")

    if fail_count or manifest_fail_count:
        status = "fail"
        decision = "reasoning_budget_failed"
    elif hold_count or manifest_hold_count:
        status = "hold"
        decision = "reasoning_budget_incomplete"
    else:
        status = "pass"
        decision = "reasoning_budget_ready"

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "manifest_path": str(manifest_path),
        "vault_root": str(vault_root),
        "workload": text(manifest.get("workload")),
        "model_id": text(manifest.get("model_id")),
        "runtime": text(manifest.get("runtime")),
        "route": text(manifest.get("route")),
        "prompt_id": text(manifest.get("prompt_id")),
        "trial_count": len(evaluated),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "manifest_findings": manifest_findings,
        "trials": evaluated,
        "outputs": {},
    }

    json_path = output_dir / f"{run_id}-reasoning-budget-audit.json"
    markdown_path = output_dir / f"{run_id}-reasoning-budget-audit.md"
    csv_path = output_dir / f"{run_id}-reasoning-budget-audit.csv"
    jsonl_path = output_root / "reasoning-budget-audits.jsonl"
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
        "trial_count": len(evaluated),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "manifest_findings": len(manifest_findings),
        "output_dir": str(output_dir),
    }, indent=2))
    return 0 if status == "pass" else 1 if status == "hold" else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"status": "error", "decision": "reasoning_budget_error", "error": str(exc)}, indent=2), file=sys.stderr)
        raise SystemExit(2)
```

## PowerShell Run

```powershell
$env:LOCAL_LLM_REASONING_BUDGET_AUDIT_MANIFEST = "D:\llm-runs\reasoning-budget\reasoning-budget-manifest.json"
$env:LOCAL_LLM_REASONING_BUDGET_AUDIT_VAULT_ROOT = "D:\Vaults\PersonalKB"
python .\local_llm_reasoning_budget_runner.py
```

## Reading The Result

| Status and decision | Meaning | Next action |
|---|---|---|
| `pass/reasoning_budget_ready` | the effort sweep has controlled settings, parser/trace evidence, quality and latency deltas, trace policy, and a decision | link the output in [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]], [[LLM/Study/Local LLM Result Synthesis Runner|Local LLM Result Synthesis Runner]], and [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]] |
| `hold/reasoning_budget_incomplete` | one or more rows or decision fields are missing, unresolved, or not marked pass | complete the first missing response, parser, benchmark, quality, or trace-policy artifact |
| `fail/reasoning_budget_failed` | a trial is failed or trace sharing/logging is unsafe without review | quarantine the trace, change policy, fix parser separation, or reject reasoning mode for the workload |

## Completion Gate

This runner is complete for one reasoning-budget pass when:

- [ ] at least two effort settings are audited
- [ ] prompt, model, runtime, route, sampler, and output cap are fixed or the difference is explicitly routed elsewhere
- [ ] raw response and final-answer evidence are linked for every trial
- [ ] reasoning output shape and parser setting are documented
- [ ] timing, token or trace length, and quality evidence exist
- [ ] trace visibility and retention policy is written
- [ ] decision card names selected effort, use policy, quality delta, latency delta, token impact, failure owner, and retest trigger

## References

- [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Lab]]
- [[LLM/2026 — Reasoning and Agents/Reasoning Models and Test-Time Compute]]
- [[LLM/2026 — Reasoning and Agents/DeepSeek R1 and Open Reasoning]]
- [[LLM/Study/LLM Inference Request Lifecycle Runner]]
- [[LLM/Study/Decoding and Sampling Controls Runner]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Result Synthesis Runner]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/Study/LLM Deployment Readiness Audit Runner]]
