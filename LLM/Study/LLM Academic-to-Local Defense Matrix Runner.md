---
tags: [study, llm, papers, local-llm, defense, evidence, audit, capstone, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [core, deep-dive, practice]
last-verified: 2026-06-15
---

# LLM Academic-to-Local Defense Matrix Runner

> **One-line summary** LLM mastery is defensible when each academic claim can predict or explain a local inference artifact, metric, failure owner, and next decision.

Use this after [[LLM/Study/LLM Paper Claim Audit Runner|LLM Paper Claim Audit Runner]] and [[LLM/Study/LLM Paper-to-Local Proof Router|LLM Paper-to-Local Proof Router]] when the paper rows, mechanism bridge, local labs, and capstone workbook need to become one oral/practical defense matrix.

This runner does not replace the paper audit or the local lab runners. It checks the cross-link that those tools cannot prove alone:

```text
paper claim -> mechanism -> local prediction -> artifact -> metric -> failure owner -> decision
```

If a row cannot make that chain explicit, it is not yet strong enough for the final mastery defense.

## What This Proves

| Defense axis | What the row must connect | Why it matters |
|---|---|---|
| Paper basis | Paper, paper cluster, source proof, or claim ledger row | prevents local tuning folklore from replacing academic grounding |
| Mechanism | Tokenization, attention, KV cache, quantization, sampling, RAG, tools, evaluation, or deployment economics | keeps the explanation causal rather than anecdotal |
| Local prediction | What should happen before the run is inspected | separates hypothesis from hindsight |
| Artifact | Saved local evidence, lab output, runner output, benchmark row, or capstone link | makes the claim replayable |
| Metric | Which number or rubric proves the claim, and what it cannot prove | avoids treating any green output as universal quality |
| Failure owner | The layer that owns a miss if the row fails | drives one controlled next action |
| Decision | keep, tune, reject, rerun, deploy, or block | turns learning into an operational choice |

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "llm-defense-matrix-001",
  "run_root": "D:/llm-runs/defense-matrix",
  "vault_root": "D:/Vaults/PersonalKB",
  "rows": [
    {
      "cluster": "architecture-attention",
      "status": "pass",
      "paper_basis": "Attention Is All You Need and FlashAttention",
      "paper_proof": "LLM/Study/LLM Paper Claim Audit Runner.md",
      "mechanism": "Self-attention and IO-aware attention make long prompts a prefill and memory problem.",
      "local_prediction": "Longer rendered prompts should raise TTFT before they strongly affect decode tokens/sec.",
      "local_artifact": "LLM/Study/LLM Inference Request Lifecycle Runner.md",
      "metric_kind": "latency",
      "metric": "TTFT and prompt-token count",
      "controlled_variable": "prompt length",
      "confounder": "cold model load, sampler, route, and output cap",
      "failure_owner": "prompt assembly or prefill",
      "decision": "rerun",
      "defense_answer": "The paper mechanism predicts the local timing pattern; the runner proves whether the measurement isolates that phase.",
      "next_route": "LLM/Study/Local LLM Context Window and Token Budgeting Runner.md"
    }
  ]
}
```

`paper_proof`, `local_artifact`, and `next_route` may be absolute paths, vault-relative paths, Obsidian note paths, or Obsidian links.

The input can also be a JSON list or CSV if you set `LLM_DEFENSE_MATRIX_INPUT` directly.

## Default Defense Clusters

If `expected_clusters` is omitted, the runner expects one passable row for each cluster:

| Cluster | Minimum defense |
|---|---|
| `architecture-attention` | attention, tokenization, position, template, or context mechanism predicts a local request behavior |
| `pretraining-scaling` | data, objective, scale, or training pipeline explains capability, sample efficiency, or failure type |
| `systems-serving` | KV cache, batching, scheduler, quantization, runtime, or hardware explains latency, memory, throughput, or OOM |
| `alignment-posttraining` | SFT, RLHF, DPO, CAI, refusal, instruction following, or safety evaluation explains behavior |
| `adaptation-compression` | LoRA, QLoRA, distillation, quantization, prompt-only, RAG, or no-train choice is justified by measured failure |
| `retrieval-rag` | retrieval, chunking, embedding, reranking, context assembly, citation, or refusal evidence explains a RAG result |
| `tools-agents` | tool schema, policy, execution, structured output, or agent loop is validated outside the model |
| `evaluation-deployment` | benchmark, quality, judge calibration, security, operations, cost, or deployment decision is defensible |

## Standard-Library Runner

Save the code block as `llm_academic_to_local_defense_matrix_runner.py` or extract it directly from this note.

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


DEFAULT_EXPECTED_CLUSTERS = [
    {
        "label": "architecture-attention",
        "aliases": ["attention", "architecture", "tokenization", "context", "template"],
    },
    {
        "label": "pretraining-scaling",
        "aliases": ["pretraining", "scaling", "training", "data", "objective"],
    },
    {
        "label": "systems-serving",
        "aliases": ["systems", "serving", "kv-cache", "scheduler", "runtime", "quantization"],
    },
    {
        "label": "alignment-posttraining",
        "aliases": ["alignment", "posttraining", "post-training", "rlhf", "dpo", "cai"],
    },
    {
        "label": "adaptation-compression",
        "aliases": ["adaptation", "compression", "lora", "qlora", "distillation", "no-train"],
    },
    {
        "label": "retrieval-rag",
        "aliases": ["rag", "retrieval", "embedding", "reranking", "citation"],
    },
    {
        "label": "tools-agents",
        "aliases": ["tools", "agents", "structured-output", "function-calling"],
    },
    {
        "label": "evaluation-deployment",
        "aliases": ["evaluation", "deployment", "benchmark", "quality", "ops", "security"],
    },
]

ALLOWED_STATUS = {"pass", "hold", "fail"}
ALLOWED_DECISIONS = {"keep", "tune", "reject", "rerun", "deploy", "block", "hold"}
ALLOWED_METRIC_KINDS = {
    "loss",
    "perplexity",
    "benchmark",
    "quality",
    "latency",
    "throughput",
    "memory",
    "retrieval",
    "safety",
    "cost",
    "operations",
    "mixed",
}
STATUS_RANK = {"fail": 0, "hold": 1, "pass": 2}


def utc_iso() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def slug(value: str) -> str:
    result = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip()).strip("-")
    return result or "run"


def norm(value: Any) -> str:
    return re.sub(r"[^a-z0-9]+", "-", str(value or "").lower()).strip("-")


def display(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value)


def list_value(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [display(item) for item in value if display(item)]
    if isinstance(value, str):
        return [item.strip() for item in re.split(r"[;,]", value) if item.strip()]
    return [display(value)] if display(value) else []


def bool_value(value: Any, default: bool) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def first_text(row: dict[str, Any], *names: str) -> str:
    for name in names:
        value = row.get(name)
        if display(value):
            return display(value)
    return ""


def has_text(row: dict[str, Any], field: str) -> bool:
    return bool(display(row.get(field)))


def status_value(value: Any) -> str:
    text = norm(value)
    if text in ALLOWED_STATUS:
        return text
    if text in {"passed", "ready", "complete"}:
        return "pass"
    if text in {"blocked", "incomplete", "todo", "not-started"}:
        return "hold"
    if text in {"failed", "error"}:
        return "fail"
    return text


def clean_link(value: str) -> str:
    text = display(value)
    if text.startswith("[" * 2) and text.endswith("]" * 2):
        text = text[2:-2]
    text = text.split("|", 1)[0].split("#", 1)[0].strip()
    return text


def proof_exists(vault_root: Path, value: str) -> tuple[bool, str]:
    target = clean_link(value)
    if not target:
        return False, ""
    path = Path(target)
    candidates: list[Path] = []
    if path.is_absolute():
        candidates.append(path)
    else:
        candidates.append(vault_root / path)
        if not target.endswith(".md"):
            candidates.append(vault_root / f"{target}.md")
    for candidate in candidates:
        if candidate.exists():
            return True, str(candidate)
    return False, str(candidates[0]) if candidates else target


def load_rows_from_path(path: Path) -> list[dict[str, Any]]:
    if path.suffix.lower() == ".csv":
        with path.open("r", newline="", encoding="utf-8-sig") as handle:
            return [dict(row) for row in csv.DictReader(handle)]
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return [dict(row) for row in data]
    if isinstance(data, dict):
        for key in ("rows", "matrix", "defense_rows"):
            value = data.get(key)
            if isinstance(value, list):
                return [dict(row) for row in value]
    raise ValueError(f"Unsupported row input shape: {path}")


def load_manifest() -> tuple[Path, dict[str, Any], list[dict[str, Any]]]:
    manifest_path_value = os.environ.get("LLM_DEFENSE_MATRIX_MANIFEST")
    input_path_value = os.environ.get("LLM_DEFENSE_MATRIX_INPUT")
    if not manifest_path_value and not input_path_value:
        raise ValueError("Set LLM_DEFENSE_MATRIX_MANIFEST or LLM_DEFENSE_MATRIX_INPUT.")

    if manifest_path_value:
        manifest_path = Path(manifest_path_value).expanduser().resolve()
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if not isinstance(manifest, dict):
            raise ValueError("Manifest must be a JSON object.")
        if input_path_value:
            rows = load_rows_from_path(Path(input_path_value).expanduser().resolve())
        else:
            rows_value = manifest.get("rows") or manifest.get("matrix") or manifest.get("defense_rows")
            if rows_value is None:
                input_value = manifest.get("input") or manifest.get("input_path")
                if not input_value:
                    raise ValueError("Manifest must include rows/matrix/defense_rows or set LLM_DEFENSE_MATRIX_INPUT.")
                input_path = Path(str(input_value)).expanduser()
                if not input_path.is_absolute():
                    input_path = manifest_path.parent / input_path
                rows = load_rows_from_path(input_path.resolve())
            else:
                if not isinstance(rows_value, list):
                    raise ValueError("Manifest rows must be a list of objects.")
                rows = [dict(row) for row in rows_value]
        return manifest_path, manifest, rows

    input_path = Path(str(input_path_value)).expanduser().resolve()
    return input_path, {}, load_rows_from_path(input_path)


def expected_from_manifest(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    configured = manifest.get("expected_clusters")
    if not configured:
        return DEFAULT_EXPECTED_CLUSTERS
    expected: list[dict[str, Any]] = []
    for item in configured:
        if isinstance(item, dict):
            label = display(item.get("label") or item.get("cluster") or item.get("name"))
            aliases = list_value(item.get("aliases"))
        else:
            label = display(item)
            aliases = [label]
        if label:
            expected.append({"label": label, "aliases": aliases or [label]})
    return expected or DEFAULT_EXPECTED_CLUSTERS


def canonical_expected_label(cluster: str, expected: list[dict[str, Any]]) -> str:
    cluster_norm = norm(cluster)
    for item in expected:
        aliases = [display(item["label"])] + list_value(item.get("aliases"))
        for alias in aliases:
            alias_norm = norm(alias)
            if alias_norm and (alias_norm == cluster_norm or alias_norm in cluster_norm or cluster_norm in alias_norm):
                return display(item["label"])
    return ""


def finding(level: str, owner: str, text: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "owner": owner,
        "finding": text,
        "evidence": evidence,
        "action": action,
    }


def evaluate_row(row: dict[str, Any], vault_root: Path, manifest: dict[str, Any], expected: list[dict[str, Any]]) -> dict[str, Any]:
    row_id = first_text(row, "id", "row_id") or first_text(row, "cluster") or "unnamed-row"
    cluster = first_text(row, "cluster", "defense_cluster", "axis")
    declared_status = status_value(row.get("status"))
    expected_label = canonical_expected_label(cluster, expected) if cluster else ""
    require_next_route = bool_value(manifest.get("require_next_route"), True)
    require_defense_answer = bool_value(manifest.get("require_defense_answer"), True)
    findings: list[dict[str, str]] = []

    if not cluster:
        findings.append(finding("hold", "cluster", "Defense row has no cluster.", row_id, "Add cluster or defense_cluster."))
    elif not expected_label:
        findings.append(finding("hold", "cluster", "Defense row does not match an expected cluster.", cluster, "Add an alias or document an expected_clusters override."))

    required_fields = [
        "paper_basis",
        "paper_proof",
        "mechanism",
        "local_prediction",
        "local_artifact",
        "metric_kind",
        "metric",
        "controlled_variable",
        "confounder",
        "failure_owner",
        "decision",
    ]
    if require_defense_answer:
        required_fields.append("defense_answer")
    if require_next_route:
        required_fields.append("next_route")

    for field in required_fields:
        if not has_text(row, field):
            findings.append(finding("hold", field, f"Defense row is missing {field}.", row_id, f"Fill {field} before counting this cluster as defended."))

    if declared_status not in ALLOWED_STATUS:
        findings.append(finding("hold", "status", "Defense row status is not recognized.", declared_status, "Use pass, hold, or fail."))

    decision = norm(first_text(row, "decision"))
    if decision and decision not in ALLOWED_DECISIONS:
        findings.append(finding("hold", "decision", "Decision is not one of the accepted defense outcomes.", decision, "Use keep, tune, reject, rerun, deploy, block, or hold."))

    metric_kind = norm(first_text(row, "metric_kind", "metric_family"))
    if metric_kind and metric_kind not in ALLOWED_METRIC_KINDS:
        findings.append(finding("hold", "metric_kind", "Metric kind is not recognized.", metric_kind, "Use loss, perplexity, benchmark, quality, latency, throughput, memory, retrieval, safety, cost, operations, or mixed."))

    path_fields = ["paper_proof", "local_artifact"]
    if require_next_route:
        path_fields.append("next_route")
    resolved_paths: dict[str, str] = {}
    path_exists: dict[str, bool] = {}
    for field in path_fields:
        value = first_text(row, field)
        if not value:
            continue
        exists, resolved = proof_exists(vault_root, value)
        resolved_paths[f"{field}_resolved"] = resolved
        path_exists[f"{field}_exists"] = exists
        if not exists:
            findings.append(finding("hold", field, "Defense proof path does not resolve in the vault.", resolved, "Fix the path or create the missing evidence note."))

    if declared_status == "fail":
        findings.append(finding("fail", "status", "Defense row is explicitly failed.", row_id, "Remediate the row before using it as final defense evidence."))

    fail_count = sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        row_status = "fail"
        row_decision = "defense_row_failed"
    elif hold_count:
        row_status = "hold"
        row_decision = "defense_row_incomplete"
    else:
        row_status = "pass"
        row_decision = "defense_row_ready"

    result = {
        "row_id": row_id,
        "cluster": cluster,
        "expected_label": expected_label,
        "status": row_status,
        "declared_status": declared_status,
        "decision": row_decision,
        "paper_basis": first_text(row, "paper_basis"),
        "mechanism": first_text(row, "mechanism"),
        "local_prediction": first_text(row, "local_prediction"),
        "metric_kind": metric_kind,
        "metric": first_text(row, "metric"),
        "controlled_variable": first_text(row, "controlled_variable"),
        "failure_owner": first_text(row, "failure_owner"),
        "defense_decision": decision,
        "next_action": findings[0]["action"] if findings else "Use this row in the capstone workbook or mastery exam run sheet.",
        "findings": findings,
    }
    result.update(resolved_paths)
    result.update(path_exists)
    return result


def missing_expected_findings(rows: list[dict[str, Any]], expected: list[dict[str, Any]]) -> list[dict[str, str]]:
    covered = {row["expected_label"] for row in rows if row.get("expected_label")}
    findings: list[dict[str, str]] = []
    for item in expected:
        label = display(item["label"])
        if label not in covered:
            findings.append(finding("hold", "coverage", "Expected defense cluster is missing.", label, "Add a complete defense row or override expected_clusters with a documented scope."))
    return findings


def cluster_summary(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    labels = sorted({row["expected_label"] or row["cluster"] or "unspecified" for row in rows})
    summary = []
    for label in labels:
        subset = [row for row in rows if (row["expected_label"] or row["cluster"] or "unspecified") == label]
        summary.append({
            "cluster": label,
            "row_count": len(subset),
            "pass_count": sum(1 for row in subset if row["status"] == "pass"),
            "hold_count": sum(1 for row in subset if row["status"] == "hold"),
            "fail_count": sum(1 for row in subset if row["status"] == "fail"),
        })
    return summary


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "row_id",
        "cluster",
        "expected_label",
        "status",
        "declared_status",
        "decision",
        "paper_basis",
        "mechanism",
        "local_prediction",
        "metric_kind",
        "metric",
        "controlled_variable",
        "failure_owner",
        "defense_decision",
        "paper_proof_resolved",
        "paper_proof_exists",
        "local_artifact_resolved",
        "local_artifact_exists",
        "next_route_resolved",
        "next_route_exists",
        "next_action",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({name: row.get(name, "") for name in fieldnames})


def md_cell(value: Any) -> str:
    return display(value).replace("|", "\\|").replace("\n", " ")


def render_markdown(record: dict[str, Any]) -> str:
    lines = [
        f"# LLM Academic-to-Local Defense Matrix - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Expected clusters: `{record['expected_count']}`",
        f"- Covered expected clusters: `{record['covered_expected_count']}`",
        f"- Next action: {record['next_action']}",
        "",
        "## Defense Rows",
        "",
        "| Cluster | Status | Metric kind | Failure owner | Defense decision | Next action |",
        "|---|---|---|---|---|---|",
    ]
    for row in record["rows"]:
        lines.append("| " + " | ".join([
            md_cell(row["expected_label"] or row["cluster"]),
            md_cell(row["status"]),
            md_cell(row["metric_kind"]),
            md_cell(row["failure_owner"]),
            md_cell(row["defense_decision"]),
            md_cell(row["next_action"]),
        ]) + " |")
    lines.extend(["", "## Cluster Summary", "", "| Cluster | Rows | Pass | Hold | Fail |", "|---|---:|---:|---:|---:|"])
    for row in record["cluster_summary"]:
        lines.append("| " + " | ".join([
            md_cell(row["cluster"]),
            md_cell(row["row_count"]),
            md_cell(row["pass_count"]),
            md_cell(row["hold_count"]),
            md_cell(row["fail_count"]),
        ]) + " |")
    lines.extend(["", "## Findings", ""])
    if record["findings"]:
        for item in record["findings"]:
            lines.append(f"- `{item['level']}` {item['owner']}: {item['finding']} -> {item['action']}")
    else:
        lines.append("- No blocking findings.")
    return "\n".join(lines) + "\n"


def main() -> int:
    manifest_path, manifest, raw_rows = load_manifest()
    vault_root = Path(manifest.get("vault_root") or os.environ.get("LLM_DEFENSE_MATRIX_VAULT_ROOT") or manifest_path.parent).expanduser().resolve()
    run_id = str(manifest.get("run_id") or os.environ.get("LLM_DEFENSE_MATRIX_RUN_ID") or f"{utc_stamp()}-{slug(manifest_path.stem)}")
    run_root_value = os.environ.get("LLM_DEFENSE_MATRIX_RUN_ROOT") or manifest.get("run_root", "llm-defense-matrix-runs")
    run_root = Path(str(run_root_value)).expanduser()
    if not run_root.is_absolute():
        run_root = manifest_path.parent / run_root
    run_dir = run_root / slug(run_id)
    run_dir.mkdir(parents=True, exist_ok=True)

    expected = expected_from_manifest(manifest)
    rows = [evaluate_row(dict(row), vault_root, manifest, expected) for row in raw_rows]
    rows.sort(key=lambda row: (STATUS_RANK.get(row["status"], 3), row["expected_label"] or row["cluster"], row["row_id"]))

    findings = missing_expected_findings(rows, expected)
    findings.extend(item for row in rows for item in row["findings"])
    fail_count = sum(1 for row in rows if row["status"] == "fail") + sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for row in rows if row["status"] == "hold") + sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        status = "fail"
        decision = "defense_matrix_failed"
        next_action = "Fix failed defense rows before using this matrix in the final oral/practical defense."
    elif hold_count:
        status = "hold"
        decision = "defense_matrix_incomplete"
        next_action = "Complete the first missing or held defense row."
    else:
        status = "pass"
        decision = "defense_matrix_ready"
        next_action = "Link the defense matrix output into the capstone workbook and mastery exam run sheet."

    covered = {row["expected_label"] for row in rows if row.get("expected_label")}
    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "next_action": next_action,
        "manifest_path": str(manifest_path),
        "vault_root": str(vault_root),
        "row_count": len(rows),
        "expected_count": len(expected),
        "covered_expected_count": len(covered),
        "pass_count": sum(1 for row in rows if row["status"] == "pass"),
        "hold_count": sum(1 for row in rows if row["status"] == "hold"),
        "fail_count": sum(1 for row in rows if row["status"] == "fail"),
        "cluster_summary": cluster_summary(rows),
        "findings": findings,
        "rows": rows,
        "outputs": {},
    }

    json_path = run_dir / f"{run_id}-defense-matrix.json"
    markdown_path = run_dir / f"{run_id}-defense-matrix.md"
    csv_path = run_dir / f"{run_id}-defense-matrix.csv"
    jsonl_path = run_root / "llm-defense-matrix-runs.jsonl"
    record["outputs"] = {
        "json": str(json_path),
        "markdown": str(markdown_path),
        "csv": str(csv_path),
        "jsonl": str(jsonl_path),
    }

    csv_write(csv_path, rows)
    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=True), encoding="utf-8")
    markdown_path.write_text(render_markdown(record), encoding="utf-8")
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=True) + "\n")

    print(json.dumps({
        "status": status,
        "decision": decision,
        "run_id": run_id,
        "row_count": len(rows),
        "expected_count": len(expected),
        "covered_expected_count": len(covered),
        "pass_count": record["pass_count"],
        "hold_count": record["hold_count"],
        "fail_count": record["fail_count"],
        "finding_count": len(findings),
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
$env:LLM_DEFENSE_MATRIX_MANIFEST = "D:\llm-runs\defense-matrix\defense-matrix-manifest.json"
$env:LLM_DEFENSE_MATRIX_VAULT_ROOT = "D:\Vaults\PersonalKB"
$env:LLM_DEFENSE_MATRIX_RUN_ROOT = "D:\llm-runs\defense-matrix"
python .\llm_academic_to_local_defense_matrix_runner.py
```

## Result Decisions

| Status and decision | Meaning | Next route |
|---|---|---|
| `pass/defense_matrix_ready` | every expected cluster has a complete paper-to-local defense row with resolving proof links | link the output in [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]] and the exam attempt |
| `hold/defense_matrix_incomplete` | a cluster is missing, a proof path does not resolve, or a row lacks metric, confounder, owner, or defense answer | fill the missing row or route through [[LLM/Study/LLM Paper-to-Local Proof Router|LLM Paper-to-Local Proof Router]] |
| `fail/defense_matrix_failed` | a row is explicitly failed | remediate the underlying academic claim or local artifact before final defense |

## Defense Row Template

| Field | Value |
|---|---|
| `cluster` |  |
| `status` | pass / hold / fail |
| `paper_basis` |  |
| `paper_proof` |  |
| `mechanism` |  |
| `local_prediction` |  |
| `local_artifact` |  |
| `metric_kind` | loss / perplexity / benchmark / quality / latency / throughput / memory / retrieval / safety / cost / operations / mixed |
| `metric` |  |
| `controlled_variable` |  |
| `confounder` |  |
| `failure_owner` |  |
| `decision` | keep / tune / reject / rerun / deploy / block / hold |
| `defense_answer` |  |
| `next_route` |  |

## Oral Defense Prompts

Use these after the runner passes or to fill held rows:

1. Which paper claim predicts the local result, and what would falsify that claim?
2. Which mechanism owns the observed behavior?
3. Which metric proves the claim, and which metric would be misleading?
4. Which confounder did you control before making the decision?
5. If this row fails, which local layer owns the next action?
6. Why is the decision keep, tune, reject, rerun, deploy, block, or hold?

## Completion Gate

This defense matrix is complete when:

- [ ] all expected clusters have at least one row
- [ ] each row links paper proof and local artifact proof
- [ ] each row states a pre-run prediction, metric, confounder, and failure owner
- [ ] each row has an oral defense answer short enough to say aloud
- [ ] the runner output is linked from the capstone workbook or exam attempt

## References

- [[LLM/Study/LLM Paper Claim Audit Runner]]
- [[LLM/Study/LLM Paper-to-Local Proof Router]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/Local LLM End-to-End Mental Model]]
- [[LLM/Study/LLM Inference Request Lifecycle Runner]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/Local LLM Result Synthesis Runner]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mastery Evidence Audit Runner]]
- [[chunk-llm-049 FlashAttention Exact Attention with Tiling]]
- [[chunk-llm-093 RAG Combines Parametric and Retrieval]]
- [[chunk-llm-117 PagedAttention Eliminates KV Fragmentation]]
- [[chunk-llm-221 Speculative Decoding Draft-Verify Algorithm]]
