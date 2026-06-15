---
tags: [study, llm, evaluation, judge, calibration, local-llm, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-15
---

# Local LLM Judge Calibration Runner

> **One-line summary** LLM-as-judge evidence is usable only after human rubric rows, AB/BA order checks, agreement, bias signals, and failure routes are visible.

Use this after [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide|LLM Metrics and Evaluation Interpretation Guide]] and [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] when an LLM judge is being used to screen local model outputs, compare two local runtimes, score RAG answers, or triage tool/agent results.

This runner does not call a judge model. It audits comparison rows you already collected from human review and judge review. It is intentionally boring: manifest in, JSON/CSV/Markdown/JSONL out.

## What This Proves

| Evidence family | Checks | Why it matters |
|---|---|---|
| Human rubric anchor | prompt id, task class, human winner or decision, proof link | keeps judge scores subordinate to human acceptance criteria |
| AB and BA order control | judge verdict when A is first and when B is first | exposes position bias before a judge is trusted |
| Agreement | judge canonical verdict versus human verdict | separates useful triage from misleading automation |
| Bias signals | position flip, longer-answer preference, missing rationale inspection | catches common judge failure modes |
| Next route | quality harness, metric interpretation, RAG evaluation, tool evaluation, or human review | turns judge failure into a controlled next action |

Academic bridge: [[LLM/2023 — Open Models and Agents/LLM-as-Judge|LLM-as-Judge]] and preference evaluation are not ground truth. They are measurement systems with bias. A judge must be calibrated against human review just as a classifier must be calibrated against labels.

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "judge-calibration-001",
  "run_root": "D:/llm-runs/judge-calibration",
  "vault_root": "D:/Vaults/PersonalKB",
  "agreement_threshold": 0.7,
  "comparisons": [
    {
      "id": "q001",
      "prompt_id": "D-01",
      "task_class": "domain-specific",
      "status": "pass",
      "proof": "LLM/Study/Local LLM Quality Evaluation Harness.md",
      "human_winner": "A",
      "judge_ab_presented_winner": "A",
      "judge_ba_presented_winner": "B",
      "output_a_tokens": 180,
      "output_b_tokens": 260,
      "rationale_inspected": true,
      "next_route": "LLM/Study/Local LLM Quality Evaluation Harness"
    }
  ]
}
```

`judge_ab_presented_winner` is the winner label when the judge prompt showed original output A first and original output B second. `judge_ba_presented_winner` is the winner label when the judge prompt showed original output B first and original output A second. The runner converts both back to the original A/B labels before comparing them.

Use `human_winner: "tie"` when the human reviewer says neither output clearly wins. If no judge was used, this runner is not the right proof artifact; keep the quality row in [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] instead.

## Standard-Library Runner

Save this as `local_llm_judge_calibration_runner.py` inside the run folder. It uses only Python's standard library.

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
    "hold": "hold",
    "blocked": "hold",
    "gap": "hold",
    "missing": "hold",
    "in-progress": "hold",
    "in progress": "hold",
    "fail": "fail",
    "failed": "fail",
    "rejected": "fail",
    "unsafe": "fail",
    "error": "fail",
}

STATUS_RANK = {"pass": 0, "hold": 1, "fail": 2}
WIN_VALUES = {
    "a": "A",
    "output_a": "A",
    "answer_a": "A",
    "left": "A",
    "first": "A",
    "b": "B",
    "output_b": "B",
    "answer_b": "B",
    "right": "B",
    "second": "B",
    "tie": "tie",
    "draw": "tie",
    "equal": "tie",
    "no_preference": "tie",
}
LINK_OPEN = "[" + "["
LINK_CLOSE = "]" + "]"


def utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def slug(value: Any) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value or "").strip().lower())
    return text.strip("-") or "local-llm-judge-calibration"


def norm(value: Any) -> str:
    return str(value or "").strip().lower().replace(" ", "_").replace("-", "_")


def status_value(value: Any) -> str:
    return STATUS_VALUES.get(norm(value).replace("_", "-"), "hold")


def win_value(value: Any) -> str:
    return WIN_VALUES.get(norm(value), "")


def bool_value(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value in (None, ""):
        return default
    text = norm(value)
    if text in {"true", "yes", "y", "1", "inspected", "reviewed"}:
        return True
    if text in {"false", "no", "n", "0", "missing", "not_reviewed"}:
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


def load_manifest() -> tuple[Path, dict[str, Any]]:
    manifest_path = os.environ.get("LOCAL_LLM_JUDGE_CALIBRATION_MANIFEST")
    if not manifest_path:
        raise ValueError("Set LOCAL_LLM_JUDGE_CALIBRATION_MANIFEST to a JSON manifest path.")
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


def route_for_row(row: dict[str, Any]) -> str:
    route = str(row.get("next_route") or row.get("route") or row.get("proof") or "")
    if route:
        return strip_obsidian_link(route).removesuffix(".md")
    task_class = norm(row.get("task_class"))
    if "rag" in task_class or "citation" in task_class:
        return "LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab"
    if "tool" in task_class or "agent" in task_class:
        return "LLM/Study/Local LLM Tool Calling and Structured Output Runner"
    return "LLM/Study/Local LLM Quality Evaluation Harness"


def presented_to_canonical(winner: str, order: str) -> str:
    value = win_value(winner)
    if value in {"", "tie"}:
        return value
    if order == "ab":
        return value
    if order == "ba":
        return "B" if value == "A" else "A"
    return ""


def finding(level: str, owner: str, text: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "owner": owner,
        "finding": text,
        "evidence": evidence,
        "action": action,
    }


def longer_output(row: dict[str, Any]) -> str:
    a_tokens = number_value(row.get("output_a_tokens"))
    b_tokens = number_value(row.get("output_b_tokens"))
    if a_tokens is None or b_tokens is None:
        return ""
    if abs(a_tokens - b_tokens) < max(20.0, 0.15 * max(a_tokens, b_tokens)):
        return "similar"
    return "A" if a_tokens > b_tokens else "B"


def evaluate_row(row: dict[str, Any], vault_root: Path) -> dict[str, Any]:
    row_id = str(row.get("row_id") or row.get("id") or row.get("prompt_id") or "")
    prompt_id = str(row.get("prompt_id") or "")
    task_class = str(row.get("task_class") or "")
    declared_status = status_value(row.get("status"))
    proof = str(row.get("proof") or row.get("proof_path") or row.get("evidence_path") or "")
    human_winner = win_value(row.get("human_winner") or row.get("human_decision"))
    judge_ab = presented_to_canonical(str(row.get("judge_ab_presented_winner") or row.get("judge_ab_winner") or ""), "ab")
    judge_ba = presented_to_canonical(str(row.get("judge_ba_presented_winner") or row.get("judge_ba_winner") or ""), "ba")
    rationale_inspected = bool_value(row.get("rationale_inspected"), False)
    findings: list[dict[str, str]] = []

    if not row_id:
        findings.append(finding("hold", "manifest", "Comparison row id is missing.", str(row), "Give every comparison a stable id."))
    if not prompt_id:
        findings.append(finding("hold", "prompt", "Prompt id is missing.", row_id, "Attach the comparison to a prompt-suite item."))
    if not task_class:
        findings.append(finding("hold", "prompt", "Task class is missing.", row_id, "Name the task class: known answer, schema, RAG, tool, coding, extraction, or domain-specific."))

    exists = False
    proof_resolved = ""
    if proof:
        exists, proof_resolved = proof_exists(vault_root, proof)
        if not exists:
            findings.append(finding("hold", "proof", "Proof link or path does not resolve in the vault.", proof_resolved, "Fix the proof path or create the linked quality evidence."))
    else:
        findings.append(finding("hold", "proof", "Comparison has no proof link or path.", row_id, "Link the human rubric row, judge prompt transcript, or quality harness row."))

    if declared_status == "fail":
        findings.append(finding("fail", "review", "Comparison row is explicitly marked fail.", row_id, "Resolve the failed human or judge review before using this comparison."))
    elif declared_status != "pass":
        findings.append(finding("hold", "review", "Comparison row is not marked pass.", declared_status, "Mark pass only after the human and judge evidence is complete."))

    if not human_winner:
        findings.append(finding("hold", "human review", "Human winner or tie is missing.", row_id, "Add human_winner as A, B, or tie."))
    if not judge_ab:
        findings.append(finding("hold", "judge review", "AB judge verdict is missing or invalid.", row_id, "Add judge_ab_presented_winner as A, B, or tie."))
    if not judge_ba:
        findings.append(finding("hold", "judge review", "BA judge verdict is missing or invalid.", row_id, "Add judge_ba_presented_winner from the reversed-order prompt."))
    if not rationale_inspected:
        findings.append(finding("hold", "judge review", "Judge rationale was not inspected.", row_id, "Read the rationale for rubric leakage, unsupported claims, or verbosity bias."))

    order_consistent = bool(judge_ab and judge_ba and judge_ab == judge_ba)
    human_agree = bool(order_consistent and human_winner and judge_ab == human_winner)
    if judge_ab and judge_ba and not order_consistent:
        findings.append(finding("hold", "position bias", "AB and BA judge verdicts choose different original outputs.", f"AB={judge_ab}; BA={judge_ba}", "Treat this prompt as order-sensitive and do not use the judge verdict as ground truth."))
    elif order_consistent and human_winner and judge_ab != human_winner:
        findings.append(finding("fail", "calibration", "Judge verdict disagrees with human review in both orders.", f"human={human_winner}; judge={judge_ab}", "Keep this task class under human review or rewrite the judge rubric and rerun calibration."))

    longer = longer_output(row)
    verbosity_flag = ""
    if longer in {"A", "B"} and order_consistent and judge_ab == longer and human_winner != longer:
        verbosity_flag = "judge_prefers_longer_output"
        findings.append(finding("hold", "verbosity bias", "Judge appears to prefer the longer output against human review.", f"longer={longer}; human={human_winner}; judge={judge_ab}", "Inspect whether the judge rewarded verbosity rather than correctness."))

    fail_count = sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        status = "fail"
        decision = "judge_not_calibrated"
    elif hold_count:
        status = "hold"
        decision = "calibration_incomplete"
    else:
        status = "pass"
        decision = "judge_matches_human"

    return {
        "row_id": row_id,
        "prompt_id": prompt_id,
        "task_class": task_class,
        "declared_status": declared_status,
        "status": status,
        "decision": decision,
        "proof": proof,
        "proof_resolved": proof_resolved,
        "proof_exists": exists,
        "human_winner": human_winner,
        "judge_ab_original_winner": judge_ab,
        "judge_ba_original_winner": judge_ba,
        "order_consistent": order_consistent,
        "human_agreement": human_agree,
        "rationale_inspected": rationale_inspected,
        "longer_output": longer,
        "verbosity_flag": verbosity_flag,
        "next_route": route_for_row(row),
        "next_action": findings[0]["action"] if findings else "Use the judge only as supporting evidence beside the human rubric row.",
        "findings": findings,
    }


def md_cell(value: Any) -> str:
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True)
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "row_id",
        "prompt_id",
        "task_class",
        "declared_status",
        "status",
        "decision",
        "proof",
        "proof_resolved",
        "proof_exists",
        "human_winner",
        "judge_ab_original_winner",
        "judge_ba_original_winner",
        "order_consistent",
        "human_agreement",
        "rationale_inspected",
        "longer_output",
        "verbosity_flag",
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
        f"# Local LLM Judge Calibration - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Comparisons: `{record['comparison_count']}`",
        f"- Pass/Hold/Fail: `{record['pass_count']}` / `{record['hold_count']}` / `{record['fail_count']}`",
        f"- Human agreement rate: `{record['human_agreement_rate']}`",
        f"- Order-sensitive rows: `{record['order_sensitive_count']}`",
        f"- Verbosity flags: `{record['verbosity_flag_count']}`",
        "",
        "## Comparison Rows",
        "",
        "| Row | Prompt | Task | Status | Human | Judge AB | Judge BA | Agreement | Next route |",
        "|---|---|---|---|---|---|---|---:|---|",
    ]
    for row in record["comparisons"]:
        lines.append(
            "| "
            + " | ".join([
                md_cell(row["row_id"]),
                md_cell(row["prompt_id"]),
                md_cell(row["task_class"]),
                md_cell(row["status"]),
                md_cell(row["human_winner"]),
                md_cell(row["judge_ab_original_winner"]),
                md_cell(row["judge_ba_original_winner"]),
                md_cell(row["human_agreement"]),
                md_cell(wiki_link(row["next_route"])),
            ])
            + " |"
        )
    lines.extend(["", "## Next Actions", ""])
    incomplete = [row for row in record["comparisons"] if row["status"] != "pass"]
    for row in incomplete:
        lines.append(f"- `{row['row_id']}` -> {wiki_link(row['next_route'])}: {row['next_action']}")
    if not incomplete:
        lines.append("- Judge calibration is good enough to use as supporting evidence for this prompt set.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    manifest_path, manifest = load_manifest()
    vault_root = Path(manifest.get("vault_root") or os.environ.get("LOCAL_LLM_JUDGE_CALIBRATION_VAULT_ROOT") or manifest_path.parent).expanduser().resolve()
    run_id = str(manifest.get("run_id") or os.environ.get("LOCAL_LLM_JUDGE_CALIBRATION_RUN_ID") or f"{utc_stamp()}-{slug(manifest_path.stem)}")
    run_root_value = os.environ.get("LOCAL_LLM_JUDGE_CALIBRATION_RUN_ROOT") or manifest.get("run_root", "local-llm-judge-calibration-runs")
    run_root = Path(str(run_root_value)).expanduser()
    if not run_root.is_absolute():
        run_root = manifest_path.parent / run_root
    run_root = run_root.resolve()
    run_dir = run_root / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    comparisons = manifest.get("comparisons")
    if comparisons is None:
        comparisons = manifest.get("rows")
    if not isinstance(comparisons, list) or not all(isinstance(row, dict) for row in comparisons):
        raise ValueError("Manifest comparisons must be a list of objects.")
    if not comparisons:
        raise ValueError("Manifest must include at least one comparison row.")

    evaluated = [evaluate_row(dict(row), vault_root) for row in comparisons]
    evaluated.sort(key=lambda row: (
        STATUS_RANK.get(row["status"], 3),
        row["prompt_id"],
        row["row_id"],
    ))

    pass_count = sum(1 for row in evaluated if row["status"] == "pass")
    hold_count = sum(1 for row in evaluated if row["status"] == "hold")
    fail_count = sum(1 for row in evaluated if row["status"] == "fail")
    order_sensitive_count = sum(1 for row in evaluated if row["judge_ab_original_winner"] and row["judge_ba_original_winner"] and not row["order_consistent"])
    verbosity_flag_count = sum(1 for row in evaluated if row["verbosity_flag"])
    comparable_count = sum(1 for row in evaluated if row["order_consistent"] and row["human_winner"])
    agreement_count = sum(1 for row in evaluated if row["human_agreement"])
    agreement_rate = (agreement_count / comparable_count) if comparable_count else 0.0
    threshold = number_value(manifest.get("agreement_threshold"))
    if threshold is None:
        threshold = 0.7

    if fail_count:
        status = "fail"
        decision = "judge_calibration_failed"
    elif hold_count or agreement_rate < threshold:
        status = "hold"
        decision = "judge_calibration_incomplete"
    else:
        status = "pass"
        decision = "judge_calibrated_for_supporting_use"

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "manifest_path": str(manifest_path),
        "vault_root": str(vault_root),
        "agreement_threshold": threshold,
        "comparison_count": len(evaluated),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "human_agreement_count": agreement_count,
        "human_agreement_rate": round(agreement_rate, 4),
        "order_sensitive_count": order_sensitive_count,
        "verbosity_flag_count": verbosity_flag_count,
        "comparisons": evaluated,
        "outputs": {},
    }

    json_path = run_dir / f"{run_id}-judge-calibration.json"
    markdown_path = run_dir / f"{run_id}-judge-calibration.md"
    csv_path = run_dir / f"{run_id}-judge-calibration.csv"
    jsonl_path = run_root / "local-llm-judge-calibration-runs.jsonl"
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
        "comparison_count": len(evaluated),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "human_agreement_rate": round(agreement_rate, 4),
        "order_sensitive_count": order_sensitive_count,
        "verbosity_flag_count": verbosity_flag_count,
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
$env:LOCAL_LLM_JUDGE_CALIBRATION_MANIFEST = "D:\llm-runs\judge-calibration\judge-calibration-manifest.json"
$env:LOCAL_LLM_JUDGE_CALIBRATION_VAULT_ROOT = "D:\Vaults\PersonalKB"
$env:LOCAL_LLM_JUDGE_CALIBRATION_RUN_ROOT = "D:\llm-runs\judge-calibration"
python .\local_llm_judge_calibration_runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/judge_calibrated_for_supporting_use` | AB and BA verdicts are order-stable, match human review above the threshold, proof links resolve, and rationales were inspected | use judge scores only as supporting evidence in the quality harness |
| `hold/judge_calibration_incomplete` | evidence is missing, order-sensitive, rationale was not inspected, or agreement is below threshold without explicit failure | rerun human review, AB/BA judge prompts, or the quality harness |
| `fail/judge_calibration_failed` | judge consistently disagrees with human review or a comparison row is explicitly failed | do not use the judge for this task class until the rubric/prompt is repaired and recalibrated |

This runner cannot prove that a model is good. It proves whether the judging setup is trustworthy enough to support a human quality decision.

## Capstone Row

| Gate | Required artifact | Pass signal |
|---|---|---|
| Judge calibration | `<run-id>-judge-calibration.json`, `<run-id>-judge-calibration.md`, `<run-id>-judge-calibration.csv`, and one `local-llm-judge-calibration-runs.jsonl` row | human review, AB and BA judge rows, proof links, rationale inspection, agreement rate, and bias signals are captured before LLM judge output is used as evidence |

## Completion Gate

- [ ] each comparison has a prompt id, task class, human winner, AB judge verdict, BA judge verdict, proof link, and inspected rationale
- [ ] AB and BA verdicts are converted back to original output labels before comparison
- [ ] order-sensitive rows are not accepted as ground truth
- [ ] judge disagreement with human review blocks judge use for that task class
- [ ] outputs are linked from [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]] when LLM-as-judge evidence is used

## References

- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab]]
- [[LLM/Study/Local RAG Evidence Runner]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/2023 — Open Models and Agents/LLM-as-Judge]]
- [[LLM/2022 — Alignment and Chat/Human Evaluation and Preference Studies]]
- [[LLM/_chunks/chunk-llm-237 MT-Bench Multi-Turn LLM Evaluation]]
- [[LLM/_chunks/chunk-llm-238 Chatbot Arena Elo Rating System]]
- [[LLM/_chunks/chunk-llm-239 LLM Judge Agreement Rates and Biases]]
- [[LLM/_chunks/chunk-llm-240 MT-Bench Chatbot Arena Evaluation Paradigms]]
