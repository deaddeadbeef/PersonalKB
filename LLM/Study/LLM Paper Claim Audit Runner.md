---
tags: [study, llm, papers, research-literacy, claims, evidence, audit, local-llm, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [core, deep-dive, practice]
last-verified: 2026-06-15
---

# LLM Paper Claim Audit Runner

> **One-line summary** Academic LLM mastery is defensible only when each core paper has a claim, evidence type, limitation, mechanism, source proof, local implication, and follow-up proof route.

Use this after [[LLM/Study/LLM Paper Claim Ledger|LLM Paper Claim Ledger]] and before [[LLM/Study/LLM Paper Oral Defense Runner|LLM Paper Oral Defense Runner]] or [[LLM/Study/LLM Paper-to-Local Proof Router|LLM Paper-to-Local Proof Router]] supports a capstone claim. The ledger teaches what to record. The oral-defense runner proves closed-book answer readiness. The paper-to-local router chooses proof routes. This runner checks whether the paper claim set is complete enough to count as academic evidence.

This runner does not fetch papers, summarize PDFs, or decide whether a claim is true. It audits the rows you already wrote from paper notes, raw captures, or a capstone CSV/JSON manifest.

## What This Proves

| Gate | Evidence checked | Why it matters |
|---|---|---|
| Fast-path coverage | every required paper label is represented | prevents skipping a core paper while claiming field mastery |
| Claim anatomy | claim type, main claim, evidence type, limitation, mechanism, and local implication | separates paper literacy from vibes or historical trivia |
| Source proof | raw note, source note, or paper note path resolves in the vault | keeps academic claims traceable |
| Local bridge | follow-up proof route resolves in the vault | turns paper reading into local inference, RAG, tools, evaluation, adaptation, or deployment evidence |
| Confounder discipline | optional baseline/confounder fields when required by the manifest | prevents overclaiming from benchmark, scale, hardware, or evaluator effects |

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "fast-path-paper-audit-001",
  "run_root": "D:/llm-runs/paper-claim-audit",
  "vault_root": "D:/Vaults/PersonalKB",
  "require_follow_up_routes": true,
  "rows": [
    {
      "paper": "Attention Is All You Need",
      "claim_type": "architecture",
      "main_claim": "Self-attention can replace recurrence/convolution for strong sequence modeling.",
      "evidence_type": "machine translation quality and parallel training comparison",
      "limitation": "Original evidence is seq2seq translation, not chat assistant behavior.",
      "mechanism": "scaled dot-product attention, multi-head projections, positional encoding",
      "source": "LLM/_raw/raw-llm-001 Attention Is All You Need.md",
      "local_implication": "Local inference cost depends on attention, context length, prefill, and KV cache.",
      "follow_up_route": "LLM/Study/Attention Implementation Lab"
    }
  ]
}
```

The input can also be a JSON list or CSV if you set `LLM_PAPER_CLAIM_AUDIT_INPUT` directly.

## Required Fields

| Field family | Accepted keys |
|---|---|
| Paper | `paper`, `title`, `short_label` |
| Claim type | `claim_type`, `type`, `category` |
| Main claim | `main_claim`, `claim`, `retained_claim` |
| Evidence type | `evidence_type`, `evidence`, `evidence_summary` |
| Limitation | `limitation`, `key_limitation`, `does_not_prove` |
| Mechanism | `mechanism`, `mechanism_anchor`, `main_mechanism` |
| Source proof | `source`, `paper_note`, `raw_note`, `reference`, `proof` |
| Local implication | `local_implication`, `local_consequence`, `deployment_implication` |
| Follow-up route | `follow_up_route`, `follow_up_vault_route`, `proof_route`, `local_proof_route` |

## Standard-Library Runner

Save this as `llm_paper_claim_audit_runner.py` inside the run folder. It uses only Python's standard library.

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


LINK_OPEN = "[" + "["
LINK_CLOSE = "]" + "]"

DEFAULT_EXPECTED_PAPERS = [
    {"label": "Attention Is All You Need", "aliases": ["attention is all you need", "transformer"]},
    {"label": "BERT", "aliases": ["bert", "bidirectional transformers"]},
    {"label": "GPT-1", "aliases": ["gpt-1", "generative pre-training"]},
    {"label": "GPT-2", "aliases": ["gpt-2", "unsupervised multitask learners"]},
    {"label": "GPT-3", "aliases": ["gpt-3", "few-shot learners"]},
    {"label": "Scaling Laws", "aliases": ["scaling laws", "neural language models"]},
    {"label": "Chinchilla", "aliases": ["chinchilla", "compute-optimal"]},
    {"label": "Megatron-LM", "aliases": ["megatron", "model parallelism"]},
    {"label": "FlashAttention", "aliases": ["flashattention", "io-aware"]},
    {"label": "LLaMA", "aliases": ["llama", "open foundation"]},
    {"label": "T5", "aliases": ["t5", "text-to-text"]},
    {"label": "InstructGPT", "aliases": ["instructgpt", "human feedback"]},
    {"label": "Constitutional AI", "aliases": ["constitutional ai", "harmlessness"]},
    {"label": "DPO", "aliases": ["dpo", "direct preference optimization"]},
    {"label": "LoRA", "aliases": ["lora", "low-rank adaptation"]},
    {"label": "QLoRA", "aliases": ["qlora", "quantized llm"]},
    {"label": "Chain-of-Thought", "aliases": ["chain-of-thought", "chain of thought", "cot"]},
    {"label": "RAG", "aliases": ["rag", "retrieval-augmented generation", "retrieval augmented generation"]},
    {"label": "ReAct", "aliases": ["react", "reasoning and acting"]},
    {"label": "HELM", "aliases": ["helm", "holistic evaluation"]},
]

FIELD_GROUPS = {
    "paper": ("paper", "title", "short_label"),
    "claim_type": ("claim_type", "type", "category"),
    "main_claim": ("main_claim", "claim", "retained_claim"),
    "evidence_type": ("evidence_type", "evidence", "evidence_summary"),
    "limitation": ("limitation", "key_limitation", "does_not_prove"),
    "mechanism": ("mechanism", "mechanism_anchor", "main_mechanism"),
    "source": ("source", "paper_note", "raw_note", "reference", "proof"),
    "local_implication": ("local_implication", "local_consequence", "deployment_implication"),
    "follow_up_route": ("follow_up_route", "follow_up_vault_route", "proof_route", "local_proof_route"),
    "confounder": ("confounder", "confounder_to_control", "baseline_confounder"),
    "baseline": ("baseline", "strongest_baseline", "comparison"),
}

ALLOWED_CLAIM_TYPES = {
    "architecture",
    "objective",
    "pretraining",
    "scaling",
    "systems",
    "inference-systems",
    "alignment",
    "adaptation",
    "retrieval-tools",
    "evaluation",
}

STATUS_VALUES = {
    "pass": "pass",
    "passed": "pass",
    "ready": "pass",
    "complete": "pass",
    "hold": "hold",
    "pending": "hold",
    "missing": "hold",
    "incomplete": "hold",
    "fail": "fail",
    "failed": "fail",
    "rejected": "fail",
}

STATUS_RANK = {"pass": 0, "hold": 1, "fail": 2}


def utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def slug(value: Any) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value or "").strip().lower())
    return text.strip("-") or "llm-paper-claim-audit"


def norm(value: Any) -> str:
    return str(value or "").strip().lower().replace("_", "-")


def display(value: Any) -> str:
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=True)
    return str(value if value is not None else "")


def list_value(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, tuple):
        return [str(item).strip() for item in value if str(item).strip()]
    text = str(value).strip()
    if not text:
        return []
    if text.startswith("["):
        try:
            parsed = json.loads(text)
            if isinstance(parsed, list):
                return [str(item).strip() for item in parsed if str(item).strip()]
        except json.JSONDecodeError:
            pass
    return [item.strip() for item in re.split(r"[,;|]", text) if item.strip()]


def bool_value(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value in (None, ""):
        return default
    text = str(value).strip().lower()
    if text in {"1", "true", "yes", "y", "required"}:
        return True
    if text in {"0", "false", "no", "n", "optional", "waived"}:
        return False
    return default


def status_value(value: Any) -> str:
    return STATUS_VALUES.get(norm(value), "hold")


def first_text(row: dict[str, Any], field: str) -> str:
    for name in FIELD_GROUPS[field]:
        value = row.get(name)
        if str(value or "").strip():
            return str(value).strip()
    return ""


def has_text(row: dict[str, Any], field: str) -> bool:
    return bool(first_text(row, field))


def proof_candidates(vault_root: Path, proof: str) -> list[Path]:
    text = proof.strip()
    if not text:
        return []
    if text.startswith(LINK_OPEN) and text.endswith(LINK_CLOSE):
        text = text[2:-2].split("|", 1)[0].split("#", 1)[0]
    text = text.replace("/", os.sep)
    path = Path(text).expanduser()
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
    candidates = proof_candidates(vault_root, proof)
    for candidate in candidates:
        if candidate.exists():
            return True, str(candidate)
    return False, str(candidates[0]) if candidates else proof


def load_rows_from_path(path: Path) -> list[dict[str, Any]]:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return [dict(row) for row in csv.DictReader(handle)]
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if isinstance(data, list):
        return [row for row in data if isinstance(row, dict)]
    if isinstance(data, dict):
        for key in ("rows", "papers", "claims"):
            if isinstance(data.get(key), list):
                return [row for row in data[key] if isinstance(row, dict)]
        return [data]
    raise ValueError("Input must be a JSON object, JSON list, or CSV with headers.")


def load_manifest() -> tuple[Path, dict[str, Any], list[dict[str, Any]]]:
    manifest_path = os.environ.get("LLM_PAPER_CLAIM_AUDIT_MANIFEST")
    input_path = os.environ.get("LLM_PAPER_CLAIM_AUDIT_INPUT")
    if not manifest_path and not input_path:
        raise ValueError("Set LLM_PAPER_CLAIM_AUDIT_MANIFEST or LLM_PAPER_CLAIM_AUDIT_INPUT.")
    if manifest_path:
        path = Path(manifest_path).expanduser().resolve()
        if not path.exists():
            raise FileNotFoundError(path)
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        if not isinstance(data, dict):
            raise ValueError("Manifest must be a JSON object.")
        if input_path:
            rows = load_rows_from_path(Path(input_path).expanduser().resolve())
        else:
            rows = []
            for key in ("rows", "papers", "claims"):
                if isinstance(data.get(key), list):
                    rows = [row for row in data[key] if isinstance(row, dict)]
                    break
            if not rows:
                raise ValueError("Manifest must include rows/papers/claims or set LLM_PAPER_CLAIM_AUDIT_INPUT.")
        return path, data, rows
    path = Path(str(input_path)).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(path)
    return path, {}, load_rows_from_path(path)


def expected_from_manifest(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    configured = manifest.get("expected_papers")
    if not configured:
        return DEFAULT_EXPECTED_PAPERS
    expected = []
    for item in configured:
        if isinstance(item, dict):
            label = str(item.get("label") or item.get("paper") or item.get("title") or "").strip()
            aliases = list_value(item.get("aliases"))
        else:
            label = str(item).strip()
            aliases = [label]
        if label:
            expected.append({"label": label, "aliases": aliases or [label]})
    return expected or DEFAULT_EXPECTED_PAPERS


def canonical_expected_label(paper: str, expected: list[dict[str, Any]]) -> str:
    paper_norm = norm(paper)
    for item in expected:
        aliases = [str(item["label"])] + list_value(item.get("aliases"))
        for alias in aliases:
            alias_norm = norm(alias)
            if alias_norm and (alias_norm == paper_norm or alias_norm in paper_norm or paper_norm in alias_norm):
                return str(item["label"])
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
    paper = first_text(row, "paper")
    row_id = str(row.get("id") or row.get("row_id") or paper or "")
    declared_status = status_value(row.get("status"))
    require_routes = bool_value(manifest.get("require_follow_up_routes"), True)
    require_confounders = bool_value(manifest.get("require_confounders"), False)
    require_baselines = bool_value(manifest.get("require_baselines"), False)
    findings: list[dict[str, str]] = []

    if not paper:
        findings.append(finding("hold", "paper", "Row has no paper title or label.", display(row), "Add paper, title, or short_label."))

    expected_label = canonical_expected_label(paper, expected) if paper else ""

    required_fields = ["claim_type", "main_claim", "evidence_type", "limitation", "mechanism", "source", "local_implication"]
    if require_routes:
        required_fields.append("follow_up_route")
    if require_confounders:
        required_fields.append("confounder")
    if require_baselines:
        required_fields.append("baseline")

    for field in required_fields:
        if not has_text(row, field):
            findings.append(finding("hold", field, f"Paper row is missing {field}.", paper or row_id, f"Fill {field} before counting this paper as academic proof."))

    claim_type = norm(first_text(row, "claim_type"))
    if claim_type and claim_type not in ALLOWED_CLAIM_TYPES:
        findings.append(finding("hold", "claim_type", "Claim type is not recognized.", claim_type, "Use architecture, objective, pretraining, scaling, systems, inference-systems, alignment, adaptation, retrieval-tools, or evaluation."))

    source = first_text(row, "source")
    source_exists = False
    source_resolved = ""
    if source:
        source_exists, source_resolved = proof_exists(vault_root, source)
        if not source_exists:
            findings.append(finding("hold", "source", "Source proof path does not resolve in the vault.", source_resolved, "Fix the raw/source/paper note path."))

    route = first_text(row, "follow_up_route")
    route_exists = False
    route_resolved = ""
    if route:
        route_exists, route_resolved = proof_exists(vault_root, route)
        if not route_exists:
            findings.append(finding("hold", "follow_up_route", "Follow-up proof route does not resolve in the vault.", route_resolved, "Fix the local proof route or create the note."))

    if declared_status == "fail":
        findings.append(finding("fail", "status", "Paper row is explicitly failed.", paper or row_id, "Reread the paper or remove the row from proof claims."))
    elif declared_status not in {"pass", "hold"}:
        findings.append(finding("hold", "status", "Paper row status is not recognized.", declared_status, "Use pass, hold, or fail."))

    fail_count = sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        status = "fail"
        decision = "paper_row_failed"
    elif hold_count:
        status = "hold"
        decision = "paper_row_incomplete"
    else:
        status = "pass"
        decision = "paper_row_ready"

    return {
        "row_id": row_id,
        "paper": paper,
        "expected_label": expected_label,
        "claim_type": claim_type,
        "status": status,
        "declared_status": declared_status,
        "decision": decision,
        "source": source,
        "source_resolved": source_resolved,
        "source_exists": source_exists,
        "follow_up_route": route,
        "follow_up_route_resolved": route_resolved,
        "follow_up_route_exists": route_exists,
        "next_action": findings[0]["action"] if findings else "Use this row in the paper-to-local proof router or capstone workbook.",
        "findings": findings,
    }


def missing_expected_findings(rows: list[dict[str, Any]], expected: list[dict[str, Any]]) -> list[dict[str, str]]:
    covered = {row["expected_label"] for row in rows if row.get("expected_label")}
    findings = []
    for item in expected:
        label = str(item["label"])
        if label not in covered:
            findings.append(finding("hold", "coverage", "Expected fast-path paper is missing.", label, "Add a complete paper claim row or override expected_papers with a documented scope."))
    return findings


def group_summary(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups = sorted({row["claim_type"] or "unspecified" for row in rows})
    summary = []
    for group in groups:
        subset = [row for row in rows if (row["claim_type"] or "unspecified") == group]
        summary.append({
            "claim_type": group,
            "row_count": len(subset),
            "pass_count": sum(1 for row in subset if row["status"] == "pass"),
            "hold_count": sum(1 for row in subset if row["status"] == "hold"),
            "fail_count": sum(1 for row in subset if row["status"] == "fail"),
        })
    return summary


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "row_id",
        "paper",
        "expected_label",
        "claim_type",
        "status",
        "declared_status",
        "decision",
        "source",
        "source_resolved",
        "source_exists",
        "follow_up_route",
        "follow_up_route_resolved",
        "follow_up_route_exists",
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
        f"# LLM Paper Claim Audit - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Expected papers: `{record['expected_count']}`",
        f"- Covered expected papers: `{record['covered_expected_count']}`",
        f"- Next action: {record['next_action']}",
        "",
        "## Paper Rows",
        "",
        "| Paper | Expected label | Claim type | Status | Next action |",
        "|---|---|---|---|---|",
    ]
    for row in record["rows"]:
        lines.append("| " + " | ".join([
            md_cell(row["paper"]),
            md_cell(row["expected_label"]),
            md_cell(row["claim_type"]),
            md_cell(row["status"]),
            md_cell(row["next_action"]),
        ]) + " |")
    lines.extend(["", "## Claim-Type Summary", "", "| Claim type | Rows | Pass | Hold | Fail |", "|---|---:|---:|---:|---:|"])
    for row in record["claim_type_summary"]:
        lines.append("| " + " | ".join([
            md_cell(row["claim_type"]),
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
    vault_root = Path(manifest.get("vault_root") or os.environ.get("LLM_PAPER_CLAIM_AUDIT_VAULT_ROOT") or manifest_path.parent).expanduser().resolve()
    run_id = str(manifest.get("run_id") or os.environ.get("LLM_PAPER_CLAIM_AUDIT_RUN_ID") or f"{utc_stamp()}-{slug(manifest_path.stem)}")
    run_root_value = os.environ.get("LLM_PAPER_CLAIM_AUDIT_RUN_ROOT") or manifest.get("run_root", "llm-paper-claim-audit-runs")
    run_root = Path(run_root_value).expanduser()
    if not run_root.is_absolute():
        run_root = manifest_path.parent / run_root
    run_dir = run_root / slug(run_id)
    run_dir.mkdir(parents=True, exist_ok=True)

    expected = expected_from_manifest(manifest)
    rows = [evaluate_row(dict(row), vault_root, manifest, expected) for row in raw_rows]
    rows.sort(key=lambda row: (STATUS_RANK.get(row["status"], 3), row["expected_label"] or row["paper"], row["row_id"]))

    findings = missing_expected_findings(rows, expected)
    findings.extend(item for row in rows for item in row["findings"])

    fail_count = sum(1 for row in rows if row["status"] == "fail") + sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for row in rows if row["status"] == "hold") + sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        status = "fail"
        decision = "paper_claim_audit_failed"
        next_action = "Fix failed paper rows before using the academic proof bundle."
    elif hold_count:
        status = "hold"
        decision = "paper_claim_audit_incomplete"
        next_action = "Complete the first missing or held paper claim row."
    else:
        status = "pass"
        decision = "paper_claim_audit_ready"
        next_action = "Run the paper-to-local proof router for the current capstone claim set."

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
        "claim_type_summary": group_summary(rows),
        "findings": findings,
        "rows": rows,
        "outputs": {},
    }

    json_path = run_dir / f"{run_id}-paper-claim-audit.json"
    markdown_path = run_dir / f"{run_id}-paper-claim-audit.md"
    csv_path = run_dir / f"{run_id}-paper-claim-audit.csv"
    jsonl_path = run_root / "llm-paper-claim-audit-runs.jsonl"
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
$env:LLM_PAPER_CLAIM_AUDIT_MANIFEST = "D:\llm-runs\paper-claim-audit\paper-claim-audit-manifest.json"
$env:LLM_PAPER_CLAIM_AUDIT_VAULT_ROOT = "D:\Vaults\PersonalKB"
$env:LLM_PAPER_CLAIM_AUDIT_RUN_ROOT = "D:\llm-runs\paper-claim-audit"
python .\llm_paper_claim_audit_runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/paper_claim_audit_ready` | all expected papers have complete claim anatomy, source proof, local implication, and follow-up route | run [[LLM/Study/LLM Paper-to-Local Proof Router|LLM Paper-to-Local Proof Router]] for the capstone claim set |
| `hold/paper_claim_audit_incomplete` | a paper is missing, a field is blank, a proof path does not resolve, or a route is missing | fill the first missing paper claim row |
| `fail/paper_claim_audit_failed` | a row is explicitly failed or rejected | reread the paper or remove the row from proof claims |

## Capstone Row

| Evidence | Output |
|---|---|
| Paper claim audit runner | `<run-id>-paper-claim-audit.json`, `<run-id>-paper-claim-audit.md`, `<run-id>-paper-claim-audit.csv`, and one `llm-paper-claim-audit-runs.jsonl` row |

## Completion Gate

- [ ] every expected fast-path paper is represented
- [ ] every row has claim type, main claim, evidence type, limitation, mechanism, source proof, and local implication
- [ ] every source proof link resolves in the vault
- [ ] every required follow-up proof route resolves in the vault
- [ ] output JSON, Markdown, CSV, and JSONL artifacts are saved
- [ ] outputs are linked from [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]

## References

- [[LLM/Study/LLM Paper Reading Protocol]]
- [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]]
- [[LLM/Study/LLM Paper Claim Ledger]]
- [[LLM/Study/LLM Paper Oral Defense Runner]]
- [[LLM/Study/LLM Paper-to-Local Proof Router]]
- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mastery Evidence Audit Runner]]
- [[LLM/Study/Local LLM End-to-End Mental Model]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
