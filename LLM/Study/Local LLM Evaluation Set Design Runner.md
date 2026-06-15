---
tags: [study, llm, evaluation, eval-set, benchmark, local-llm, contamination, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-15
---

# Local LLM Evaluation Set Design Runner

> **One-line summary** A quality score is trustworthy only after the prompt suite itself is representative, held out, contamination-aware, rubric-backed, and tied to the workload decision.

Use this before [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] when the prompt suite will decide whether to keep, tune, reject, deploy, or compare a local model/runtime. The quality harness scores outputs; this runner audits whether the evaluation set is good enough to score.

This runner does not call a model. It audits a manifest of prompt-suite design evidence: workload, decision scope, required task classes, private/local examples, held-out split, public benchmark isolation, expected behavior, rubric, pass criteria, contamination risk, and downstream proof links.

## What This Proves

| Evidence family | Checks | Why it matters |
|---|---|---|
| Workload contract | workload, quality bar, decision scope | prevents generic benchmark scores from replacing local acceptance criteria |
| Coverage | required task classes and minimum case count | catches suites that only test easy or convenient prompts |
| Held-out split | held-out count, tune/test separation, refresh plan | prevents prompt tuning against the same cases used for acceptance |
| Contamination control | private/local prompts, public benchmark isolation, source notes | keeps memorized public examples from becoming the pass/fail gate |
| Rubric and expected behavior | expected answer/behavior, pass criteria, failure owner | makes the quality harness auditable instead of vibe-based |
| Boundary-specific fields | schema contract, RAG sources, tool policy, safety boundary | ensures specialized task classes test their real failure modes |
| Downstream route | quality harness, RAG retrieval eval, tool eval, judge calibration | turns prompt-suite gaps into the next proof artifact |

Academic bridge: benchmark contamination and distribution shift are evaluation failures, not just paperwork. A model can score well on public examples while failing the private workload you actually intend to host locally.

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "local-eval-set-001",
  "run_root": "D:/llm-runs/eval-set-design",
  "vault_root": "D:/Vaults/PersonalKB",
  "workload": "private note summarization",
  "quality_bar": "answers preserve cited facts and refuse unsupported claims",
  "decision_scope": "choose local model/runtime for personal notes",
  "required_task_classes": ["known_answer", "schema", "domain_specific"],
  "minimum_cases": 3,
  "minimum_heldout_fraction": 0.33,
  "rows": [
    {
      "prompt_id": "K-01",
      "task_class": "known_answer",
      "status": "pass",
      "split": "heldout",
      "source_type": "private",
      "proof": "LLM/Study/Local LLM Quality Evaluation Harness.md",
      "expected_behavior": "answer the locally verifiable fact with no invented support",
      "pass_criteria": "correct answer and no unsupported claims",
      "rubric": "factuality, instruction following, concision",
      "tuned_against": false,
      "contamination_risk": "low",
      "decision_use": "acceptance"
    }
  ]
}
```

`proof` may be an absolute path, a vault-relative path, an Obsidian note path, or an Obsidian link. For local/private prompts, link only the design row or redacted prompt card if the full prompt contains private data.

## Standard-Library Runner

Save this as `local_llm_eval_set_design_runner.py` inside the run folder. It uses only Python's standard library.

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
}

STATUS_RANK = {"pass": 0, "hold": 1, "fail": 2}
LINK_OPEN = "[" + "["
LINK_CLOSE = "]" + "]"

DEFAULT_REQUIRED_CLASSES = [
    "known_answer",
    "schema",
    "extraction",
    "long_context",
    "rag",
    "multi_turn",
    "tool",
    "constraint_refusal",
    "domain_specific",
]


def utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def slug(value: Any) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value or "").strip().lower())
    return text.strip("-") or "local-llm-eval-set-design"


def norm(value: Any) -> str:
    return str(value or "").strip().lower().replace(" ", "_").replace("-", "_").replace("/", "_")


def status_value(value: Any) -> str:
    return STATUS_VALUES.get(norm(value).replace("_", "-"), "hold")


def bool_value(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value in (None, ""):
        return default
    text = norm(value)
    if text in {"true", "yes", "y", "1", "ok", "pass", "used", "acceptance"}:
        return True
    if text in {"false", "no", "n", "0", "not_used", "learning_only"}:
        return False
    return default


def number_value(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        return float(value)
    if value in (None, ""):
        return None
    try:
        return float(str(value).strip())
    except ValueError:
        return None


def list_value(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            return []
        if stripped.startswith("["):
            try:
                parsed = json.loads(stripped)
                if isinstance(parsed, list):
                    return [str(item).strip() for item in parsed if str(item).strip()]
            except json.JSONDecodeError:
                pass
        return [part.strip() for part in stripped.split(",") if part.strip()]
    return [str(value).strip()] if str(value).strip() else []


def load_manifest() -> tuple[Path, dict[str, Any]]:
    manifest_path = os.environ.get("LOCAL_LLM_EVAL_SET_MANIFEST")
    if not manifest_path:
        raise ValueError("Set LOCAL_LLM_EVAL_SET_MANIFEST to a JSON manifest path.")
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


def route_for_class(task_class: str) -> str:
    task = norm(task_class)
    if task == "rag":
        return "LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab"
    if task == "tool":
        return "LLM/Study/Local LLM Tool Calling and Structured Output Runner"
    if task in {"constraint_refusal", "safety"}:
        return "LLM/Study/Local LLM Security and Privacy Runner"
    if task == "long_context":
        return "LLM/Study/Local LLM Context Window and Token Budgeting Runner"
    return "LLM/Study/Local LLM Quality Evaluation Harness"


def route_for_row(row: dict[str, Any]) -> str:
    route = str(row.get("next_route") or row.get("route") or row.get("proof") or "")
    if route:
        return strip_obsidian_link(route).removesuffix(".md")
    return route_for_class(str(row.get("task_class") or ""))


def source_type(row: dict[str, Any]) -> str:
    return norm(row.get("source_type") or row.get("source") or "")


def split_type(row: dict[str, Any]) -> str:
    return norm(row.get("split") or row.get("set") or "")


def decision_use(row: dict[str, Any]) -> str:
    return norm(row.get("decision_use") or row.get("use") or "")


def evaluate_row(row: dict[str, Any], vault_root: Path) -> dict[str, Any]:
    prompt_id = str(row.get("prompt_id") or row.get("id") or row.get("row_id") or "")
    task_class = norm(row.get("task_class") or row.get("class") or "")
    split = split_type(row)
    source = source_type(row)
    use = decision_use(row)
    declared_status = status_value(row.get("status"))
    proof = str(row.get("proof") or row.get("proof_path") or row.get("evidence_path") or "")
    findings: list[dict[str, str]] = []

    if not prompt_id:
        findings.append(finding("hold", "manifest", "Prompt id is missing.", str(row), "Give every prompt a stable id."))
    if not task_class:
        findings.append(finding("hold", "coverage", "Task class is missing.", prompt_id, "Name the task class: known_answer, schema, extraction, long_context, rag, multi_turn, tool, constraint_refusal, or domain_specific."))
    if not split:
        findings.append(finding("hold", "split", "Evaluation split is missing.", prompt_id, "Set split to smoke, tune, heldout, regression, or learning_only."))
    if not source:
        findings.append(finding("hold", "source", "Source type is missing.", prompt_id, "Set source_type to private, local, synthetic, public, or benchmark."))

    proof_ok = False
    proof_resolved = ""
    if proof:
        proof_ok, proof_resolved = proof_exists(vault_root, proof)
        if not proof_ok:
            findings.append(finding("hold", "proof", "Proof link or path does not resolve in the vault.", proof_resolved, "Fix the proof path or create the linked design evidence."))
    else:
        findings.append(finding("hold", "proof", "Prompt row has no proof link or path.", prompt_id, "Link the prompt design row, quality harness row, or redacted prompt card."))

    if declared_status == "fail":
        findings.append(finding("fail", "review", "Prompt row is explicitly marked fail.", prompt_id, "Repair or remove this prompt before using the suite."))
    elif declared_status != "pass":
        findings.append(finding("hold", "review", "Prompt row is not marked pass.", declared_status, "Mark pass only after expected behavior, rubric, source, and split are complete."))

    if not has_text(row, "expected_behavior", "expected_answer", "gold_answer", "oracle", "minimum_expected_behavior"):
        findings.append(finding("hold", "rubric", "Expected behavior or answer is missing.", prompt_id, "Write the expected behavior, gold answer, oracle check, or minimum acceptable behavior."))
    if not has_text(row, "pass_criteria", "rubric", "threshold"):
        findings.append(finding("hold", "rubric", "Pass criteria or rubric is missing.", prompt_id, "Define what pass, hold, and fail mean for this prompt."))
    if not has_text(row, "failure_mode", "failure_owner", "what_it_tests"):
        findings.append(finding("hold", "coverage", "Failure mode or tested capability is missing.", prompt_id, "Name the failure this prompt is meant to catch."))

    if source in {"public", "benchmark"} and use in {"acceptance", "deployment", "model_selection", "runtime_selection", "keep_reject"}:
        findings.append(finding("hold", "contamination", "Public or benchmark prompt is used as acceptance evidence.", prompt_id, "Use public benchmarks for learning/context and keep private or local prompts for pass/fail decisions."))
    if source in {"public", "benchmark"} and not has_text(row, "contamination_mitigation", "public_use_reason", "learning_only_reason"):
        findings.append(finding("hold", "contamination", "Public or benchmark prompt has no contamination mitigation note.", prompt_id, "State why the prompt is learning-only, refreshed, time-bounded, or otherwise not the acceptance gate."))

    if split == "heldout" and bool_value(row.get("tuned_against"), False):
        findings.append(finding("fail", "leakage", "Held-out prompt was tuned against.", prompt_id, "Move this prompt out of held-out acceptance or create a fresh held-out case."))
    if split in {"heldout", "regression"} and not has_text(row, "refresh_trigger", "version", "created_at", "source_date"):
        findings.append(finding("hold", "maintenance", "Held-out or regression prompt has no refresh/version marker.", prompt_id, "Add a version, created date, source date, or refresh trigger."))

    if task_class == "schema" and not has_text(row, "schema_contract", "json_schema", "format_contract"):
        findings.append(finding("hold", "schema", "Schema prompt has no schema or format contract.", prompt_id, "Attach the JSON schema, table contract, command shape, or parser rule."))
    if task_class == "rag" and not has_text(row, "expected_source", "source_id", "citation_requirement", "retrieval_target"):
        findings.append(finding("hold", "rag", "RAG prompt has no expected source or citation requirement.", prompt_id, "Record expected source ids, citation rule, retrieval target, or unsupported-answer behavior."))
    if task_class == "tool" and not has_text(row, "tool_policy", "expected_tool", "allowed_tool"):
        findings.append(finding("hold", "tool", "Tool prompt has no tool policy or expected tool.", prompt_id, "Record the allowed tool, expected tool, policy, and argument constraints."))
    if task_class in {"constraint_refusal", "safety"} and not has_text(row, "allowed_boundary", "refusal_rule", "policy_boundary"):
        findings.append(finding("hold", "safety", "Constraint/refusal prompt has no boundary rule.", prompt_id, "Record allowed behavior, refusal rule, or policy boundary."))

    fail_count = sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        status = "fail"
        decision = "prompt_design_failed"
    elif hold_count:
        status = "hold"
        decision = "prompt_design_incomplete"
    else:
        status = "pass"
        decision = "prompt_design_ready"

    return {
        "prompt_id": prompt_id,
        "task_class": task_class,
        "split": split,
        "source_type": source,
        "decision_use": use,
        "declared_status": declared_status,
        "status": status,
        "decision": decision,
        "proof": proof,
        "proof_resolved": proof_resolved,
        "proof_exists": proof_ok,
        "next_route": route_for_row(row),
        "next_action": findings[0]["action"] if findings else "Use this prompt in the quality harness without tuning on held-out acceptance rows.",
        "findings": findings,
    }


def suite_findings(rows: list[dict[str, Any]], manifest: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not str(manifest.get("workload") or "").strip():
        findings.append(finding("hold", "workload", "Manifest has no workload.", "manifest", "Name the workload this evaluation set accepts or rejects."))
    if not str(manifest.get("quality_bar") or "").strip():
        findings.append(finding("hold", "quality", "Manifest has no quality bar.", "manifest", "State the quality floor before scoring outputs."))
    if not str(manifest.get("decision_scope") or "").strip():
        findings.append(finding("hold", "decision", "Manifest has no decision scope.", "manifest", "State whether the suite supports smoke, tuning, model selection, deployment, or regression."))

    minimum_cases = int(number_value(manifest.get("minimum_cases")) or 0)
    if minimum_cases and len(rows) < minimum_cases:
        findings.append(finding("hold", "coverage", "Prompt suite has too few rows.", f"{len(rows)}/{minimum_cases}", "Add enough prompt rows before using the suite for the decision."))

    required_classes = [norm(item) for item in list_value(manifest.get("required_task_classes"))] or list(DEFAULT_REQUIRED_CLASSES)
    present = {row["task_class"] for row in rows if row["task_class"]}
    for task_class in required_classes:
        if task_class not in present:
            findings.append(finding("hold", "coverage", "Required task class is missing.", task_class, f"Add a {task_class} prompt row or remove it from required_task_classes with a rationale."))

    heldout = [row for row in rows if row["split"] == "heldout"]
    min_fraction = number_value(manifest.get("minimum_heldout_fraction"))
    if min_fraction is None:
        min_fraction = 0.2
    if rows and (len(heldout) / len(rows)) < min_fraction:
        findings.append(finding("hold", "split", "Held-out fraction is too low.", f"{len(heldout)}/{len(rows)}", "Add held-out prompts that are not used for prompt tuning."))
    if not heldout:
        findings.append(finding("hold", "split", "No held-out acceptance prompts are present.", "manifest", "Add at least one held-out prompt before using the suite as an acceptance gate."))

    private_or_local = [row for row in rows if row["source_type"] in {"private", "local", "synthetic"}]
    if not private_or_local:
        findings.append(finding("hold", "contamination", "No private, local, or synthetic prompts are present.", "manifest", "Use locally written or private prompts for pass/fail decisions."))

    prompt_ids = [row["prompt_id"] for row in rows if row["prompt_id"]]
    duplicates = sorted({item for item in prompt_ids if prompt_ids.count(item) > 1})
    for duplicate in duplicates:
        findings.append(finding("fail", "manifest", "Duplicate prompt id.", duplicate, "Give each prompt row a stable unique id."))

    if not str(manifest.get("refresh_plan") or manifest.get("refresh_trigger") or "").strip():
        findings.append(finding("hold", "maintenance", "Suite has no refresh plan.", "manifest", "State when prompts should be refreshed: model change, corpus change, prompt tuning, or deployment review."))

    return findings


def md_cell(value: Any) -> str:
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True)
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "prompt_id",
        "task_class",
        "split",
        "source_type",
        "decision_use",
        "declared_status",
        "status",
        "decision",
        "proof",
        "proof_resolved",
        "proof_exists",
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
        f"# Local LLM Evaluation Set Design - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Workload: `{record['workload']}`",
        f"- Rows: `{record['prompt_count']}`",
        f"- Held-out rows: `{record['heldout_count']}`",
        f"- Private/local/synthetic rows: `{record['private_or_local_count']}`",
        f"- Pass/Hold/Fail rows: `{record['pass_count']}` / `{record['hold_count']}` / `{record['fail_count']}`",
        "",
        "## Prompt Rows",
        "",
        "| Prompt | Task | Split | Source | Status | Next route |",
        "|---|---|---|---|---|---|",
    ]
    for row in record["rows"]:
        lines.append(
            "| "
            + " | ".join([
                md_cell(row["prompt_id"]),
                md_cell(row["task_class"]),
                md_cell(row["split"]),
                md_cell(row["source_type"]),
                md_cell(row["status"]),
                md_cell(wiki_link(row["next_route"])),
            ])
            + " |"
        )
    lines.extend(["", "## Suite Findings", ""])
    for item in record["suite_findings"]:
        lines.append(f"- `{item['level']}` {item['owner']}: {item['finding']} -> {item['action']}")
    if not record["suite_findings"]:
        lines.append("- Suite-level design checks passed.")
    lines.extend(["", "## Next Actions", ""])
    incomplete = [row for row in record["rows"] if row["status"] != "pass"]
    for row in incomplete:
        lines.append(f"- `{row['prompt_id']}` -> {wiki_link(row['next_route'])}: {row['next_action']}")
    if not incomplete:
        lines.append("- Prompt suite is ready to score in the quality harness.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    manifest_path, manifest = load_manifest()
    vault_root = Path(manifest.get("vault_root") or os.environ.get("LOCAL_LLM_EVAL_SET_VAULT_ROOT") or manifest_path.parent).expanduser().resolve()
    run_id = str(manifest.get("run_id") or os.environ.get("LOCAL_LLM_EVAL_SET_RUN_ID") or f"{utc_stamp()}-{slug(manifest_path.stem)}")
    run_root_value = os.environ.get("LOCAL_LLM_EVAL_SET_RUN_ROOT") or manifest.get("run_root", "local-llm-eval-set-design-runs")
    run_root = Path(str(run_root_value)).expanduser()
    if not run_root.is_absolute():
        run_root = manifest_path.parent / run_root
    run_root = run_root.resolve()
    run_dir = run_root / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    prompt_rows = manifest.get("rows")
    if prompt_rows is None:
        prompt_rows = manifest.get("prompts")
    if not isinstance(prompt_rows, list) or not all(isinstance(row, dict) for row in prompt_rows):
        raise ValueError("Manifest rows/prompts must be a list of objects.")
    if not prompt_rows:
        raise ValueError("Manifest must include at least one prompt row.")

    evaluated = [evaluate_row(dict(row), vault_root) for row in prompt_rows]
    suite = suite_findings(evaluated, manifest)
    evaluated.sort(key=lambda row: (
        STATUS_RANK.get(row["status"], 3),
        row["task_class"],
        row["prompt_id"],
    ))

    pass_count = sum(1 for row in evaluated if row["status"] == "pass")
    hold_count = sum(1 for row in evaluated if row["status"] == "hold")
    fail_count = sum(1 for row in evaluated if row["status"] == "fail")
    suite_fail_count = sum(1 for item in suite if item["level"] == "fail")
    suite_hold_count = sum(1 for item in suite if item["level"] == "hold")
    heldout_count = sum(1 for row in evaluated if row["split"] == "heldout")
    private_or_local_count = sum(1 for row in evaluated if row["source_type"] in {"private", "local", "synthetic"})

    if fail_count or suite_fail_count:
        status = "fail"
        decision = "eval_set_design_failed"
    elif hold_count or suite_hold_count:
        status = "hold"
        decision = "eval_set_design_incomplete"
    else:
        status = "pass"
        decision = "eval_set_ready_for_quality_harness"

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "manifest_path": str(manifest_path),
        "vault_root": str(vault_root),
        "workload": str(manifest.get("workload") or ""),
        "quality_bar": str(manifest.get("quality_bar") or ""),
        "decision_scope": str(manifest.get("decision_scope") or ""),
        "prompt_count": len(evaluated),
        "heldout_count": heldout_count,
        "private_or_local_count": private_or_local_count,
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "suite_findings": suite,
        "rows": evaluated,
        "outputs": {},
    }

    json_path = run_dir / f"{run_id}-eval-set-design.json"
    markdown_path = run_dir / f"{run_id}-eval-set-design.md"
    csv_path = run_dir / f"{run_id}-eval-set-design.csv"
    jsonl_path = run_root / "local-llm-eval-set-design-runs.jsonl"
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
        "prompt_count": len(evaluated),
        "heldout_count": heldout_count,
        "private_or_local_count": private_or_local_count,
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "suite_findings": len(suite),
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
$env:LOCAL_LLM_EVAL_SET_MANIFEST = "D:\llm-runs\eval-set-design\eval-set-manifest.json"
$env:LOCAL_LLM_EVAL_SET_VAULT_ROOT = "D:\Vaults\PersonalKB"
$env:LOCAL_LLM_EVAL_SET_RUN_ROOT = "D:\llm-runs\eval-set-design"
python .\local_llm_eval_set_design_runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/eval_set_ready_for_quality_harness` | the suite has workload, decision scope, coverage, held-out/private prompts, rubric, expected behavior, and leakage controls | run [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| `hold/eval_set_design_incomplete` | coverage, proof links, held-out rows, rubric, public-use notes, or refresh plan are missing | fill prompt-suite design rows before scoring model quality |
| `fail/eval_set_design_failed` | duplicate prompt ids, explicitly failed rows, or held-out rows tuned against are present | repair the suite before using it as an acceptance gate |

## Capstone Row

| Gate | Required artifact | Pass signal |
|---|---|---|
| Evaluation set design | `<run-id>-eval-set-design.json`, `<run-id>-eval-set-design.md`, `<run-id>-eval-set-design.csv`, and one `local-llm-eval-set-design-runs.jsonl` row | workload, quality bar, decision scope, required task classes, held-out/private prompts, contamination controls, expected behavior, rubric, pass criteria, refresh plan, and downstream route are complete before quality scoring |

## Completion Gate

- [ ] workload, quality bar, and decision scope are written before scoring outputs
- [ ] required task classes match the workload and are represented in the suite
- [ ] at least one held-out acceptance prompt is not tuned against
- [ ] public benchmark examples are learning/context only or have a contamination mitigation note
- [ ] each prompt has expected behavior, pass criteria, failure mode, source type, split, and proof link
- [ ] RAG, tool, schema, long-context, and safety prompts include their boundary-specific evidence
- [ ] the suite has a refresh plan after model, corpus, prompt, or workload changes

## References

- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/Study/Local LLM Judge Calibration Runner]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/2020–2021 — The Scaling Era/Contamination and Data Leakage]]
- [[LLM/2018–2019 — Pretrained Language Models/Knowledge and Reasoning Benchmarks]]
- [[LLM/2022 — Alignment and Chat/Human Evaluation and Preference Studies]]
