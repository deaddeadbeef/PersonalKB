---
tags: [study, llm, papers, research-literacy, local-llm, evidence, routing, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [core, practice, deep-dive]
last-verified: 2026-06-15
---

# LLM Paper-to-Local Proof Router

Use this after [[LLM/Study/LLM Paper Claim Ledger|LLM Paper Claim Ledger]] and [[LLM/Study/LLM Paper Claim Audit Runner|LLM Paper Claim Audit Runner]] when a paper row has a claim, evidence type, limitation, mechanism, source proof, and local implication, but the next local proof is still vague. The paper ledger answers "what did the paper claim?" The audit runner checks whether the row is complete enough to count. This router answers "what would prove whether that claim matters for my local LLM work?" Use [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner|LLM Academic-to-Local Defense Matrix Runner]] after routes and artifacts exist, when the paper basis, mechanism, local prediction, metric, failure owner, and decision need to be defended together.

This is the bridge between academic reading and applied mastery. It keeps a paper from becoming a trivia item by forcing a route to one of the local evidence surfaces: inference lifecycle, context budgeting, quality evaluation, RAG, tools, adaptation, deployment, security, or operations.

## Routing Rule

Do not accept this chain:

```text
paper -> interesting idea -> vague note
```

Accept this chain:

```text
paper -> claim -> evidence -> limitation -> mechanism -> local implication -> proof route -> pass/hold decision
```

## Inputs

Minimum fields for one row:

| Field | Meaning |
|---|---|
| `paper` | Paper title or short label. |
| `claim_type` | `architecture`, `objective`, `scaling`, `systems`, `alignment`, `adaptation`, `retrieval-tools`, `evaluation`, or `inference-systems`. |
| `main_claim` | The claim being retained. |
| `evidence_type` | Benchmark, ablation, scaling curve, human preference, systems measurement, case study, or equivalent. |
| `limitation` | What the paper does not prove. |
| `mechanism` | The mechanism that should map to a local control or failure owner. |
| `local_implication` | Hosting, inference cost, RAG, tools, fine-tuning, quality evaluation, deployment, safety, operations, or similar. |
| `source` or `paper_note` | Vault proof for the paper note or raw capture, audited by [[LLM/Study/LLM Paper Claim Audit Runner|LLM Paper Claim Audit Runner]]. |

Optional fields:

- `confounder` - data, compute, prompt, model size, evaluator, hardware, context, runtime, or workload.
- `follow_up_vault_route` - a preferred Obsidian route if you already know it.
- `expected_route` - a route substring that the runner must include.
- `open_question` - what remains unproven.

## Standard-Library Runner

Save the code block as `llm_paper_to_local_proof_router.py` or extract it directly from this note.

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


REQUIRED_FIELDS = [
    "paper",
    "claim_type",
    "main_claim",
    "evidence_type",
    "limitation",
    "mechanism",
    "local_implication",
]


ROUTE_CATALOG = {
    "architecture": [
        "LLM/Study/Attention Implementation Lab",
        "LLM/Study/LLM Mechanism-to-Inference Bridge Map",
        "LLM/Study/LLM Math and Tensor Shape Primer",
    ],
    "objective": [
        "LLM/Study/LLM Training Pipeline Map",
        "LLM/Study/LLM Metrics and Evaluation Interpretation Guide",
        "LLM/Study/Tiny Decoder-Only Transformer Training Lab",
    ],
    "training": [
        "LLM/Study/LLM Training Pipeline Map",
        "LLM/Study/LLM Paper Claim Ledger",
        "LLM/Study/LLM Metrics and Evaluation Interpretation Guide",
    ],
    "scaling": [
        "LLM/Study/Local LLM Model and Hardware Sizing Guide",
        "LLM/Study/Local LLM Workload to Model Selection Playbook",
        "LLM/Study/LLM Deployment Decision Matrix",
    ],
    "systems": [
        "LLM/Study/LLM Inference Request Lifecycle Runner",
        "LLM/Study/Local LLM Inference Metrics Field Guide",
        "LLM/Study/Local LLM Serving Internals and Scheduler Lab",
    ],
    "inference-systems": [
        "LLM/Study/LLM Inference Request Lifecycle Runner",
        "LLM/Study/Local LLM Context Window and Token Budgeting Runner",
        "LLM/Study/Local LLM Concurrency and Batch Throughput Runner",
    ],
    "alignment": [
        "LLM/Study/Local LLM Quality Evaluation Harness",
        "LLM/Study/Local LLM Security and Privacy Runner",
        "LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide",
    ],
    "adaptation": [
        "LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide",
        "LLM/Study/Local LLM Quality Evaluation Harness",
        "LLM/Study/Local LLM Service Lifecycle and Upgrade Runner",
    ],
    "retrieval-tools": [
        "LLM/Study/Local RAG Minimal Python Harness",
        "LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab",
        "LLM/Study/Local LLM Tool Calling and Structured Output Runner",
    ],
    "evaluation": [
        "LLM/Study/LLM Metrics and Evaluation Interpretation Guide",
        "LLM/Study/Local LLM Quality Evaluation Harness",
        "LLM/Study/Local LLM First Benchmark Row Builder",
    ],
}


KEYWORD_ROUTES = [
    (r"\b(attention|q/k/v|tensor|head|mask)\b", "LLM/Study/Attention Implementation Lab"),
    (r"\b(token|tokenizer|template|special token|role marker)\b", "LLM/Study/Chat Template and Tokenizer Compatibility Lab"),
    (r"\b(prefill|decode|ttft|tpot|latency|tokens/sec|stream)\b", "LLM/Study/LLM Inference Request Lifecycle Runner"),
    (r"\b(context|long prompt|window|rag context|history)\b", "LLM/Study/Local LLM Context Window and Token Budgeting Runner"),
    (r"\b(kv cache|pagedattention|batch|queue|throughput|concurrency|scheduler)\b", "LLM/Study/Local LLM Serving Internals and Scheduler Lab"),
    (r"\b(prompt cache|prefix|cache reuse)\b", "LLM/Study/Local LLM Prompt Cache and KV Reuse Runner"),
    (r"\b(speculative|draft|verify)\b", "LLM/Study/Local LLM Speculative Decoding Runner"),
    (r"\b(quant|offload|vram|memory|gguf|nf4|gptq|awq)\b", "LLM/Study/Local LLM Quantization and GPU Offload Lab"),
    (r"\b(lora|qlora|adapter|fine[- ]?tun|dpo|sft)\b", "LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide"),
    (r"\b(rlhf|preference|refusal|safety|alignment|policy)\b", "LLM/Study/Local LLM Quality Evaluation Harness"),
    (r"\b(rag|retrieval|citation|chunk|embedding|rerank)\b", "LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab"),
    (r"\b(tool|function|agent|react|schema|action)\b", "LLM/Study/Local LLM Tool Calling and Structured Output Runner"),
    (r"\b(benchmark|metric|evaluation|rubric|calibration|held[- ]?out)\b", "LLM/Study/LLM Metrics and Evaluation Interpretation Guide"),
    (r"\b(deploy|privacy|cost|hybrid|hosted|local)\b", "LLM/Study/LLM Deployment Decision Matrix"),
]


CONFUNDER_ROUTES = {
    "data": "LLM/Study/LLM Paper Claim Ledger",
    "compute": "LLM/Study/Local LLM Model and Hardware Sizing Guide",
    "prompt": "LLM/Study/Decoding and Sampling Controls Runner",
    "model size": "LLM/Study/Local LLM Workload to Model Selection Playbook",
    "evaluator": "LLM/Study/LLM Metrics and Evaluation Interpretation Guide",
    "hardware": "LLM/Study/Local LLM Environment Preflight Lab",
    "context": "LLM/Study/Local LLM Context Window and Token Budgeting Runner",
    "runtime": "LLM/Study/Local LLM Runtime and Model Compatibility Matrix",
    "workload": "LLM/Study/Local LLM Quality Evaluation Harness",
}


def utc_stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def slug(value: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return text[:80] or "paper-proof"


def normalize_key(value: str) -> str:
    return value.strip().lower().replace("_", "-").replace(" ", "-")


def compact(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value)


def wiki_link(route: str) -> str:
    if not route:
        return ""
    return "[" + "[" + route + "]" + "]"


def as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    text = str(value).strip()
    if not text:
        return []
    if ";" in text:
        return [item.strip() for item in text.split(";") if item.strip()]
    if "|" in text:
        return [item.strip() for item in text.split("|") if item.strip()]
    return [text]


def load_rows(path: Path) -> list[dict[str, Any]]:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return [dict(row) for row in csv.DictReader(handle)]
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if isinstance(data, list):
        return [row for row in data if isinstance(row, dict)]
    if isinstance(data, dict):
        if isinstance(data.get("papers"), list):
            return [row for row in data["papers"] if isinstance(row, dict)]
        if isinstance(data.get("rows"), list):
            return [row for row in data["rows"] if isinstance(row, dict)]
        return [data]
    raise ValueError("Input must be a JSON object, JSON list, or CSV with headers.")


def load_input() -> tuple[Path, list[dict[str, Any]]]:
    input_path = os.environ.get("LLM_PAPER_PROOF_INPUT") or os.environ.get("LLM_PAPER_CLAIMS_PATH")
    if not input_path:
        manifest_path = os.environ.get("LLM_PAPER_PROOF_MANIFEST")
        if not manifest_path:
            raise ValueError("Set LLM_PAPER_PROOF_INPUT, LLM_PAPER_CLAIMS_PATH, or LLM_PAPER_PROOF_MANIFEST.")
        input_path = manifest_path
    path = Path(input_path).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"Input path does not exist: {path}")
    return path, load_rows(path)


def unique_routes(routes: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for route in routes:
        clean = route.strip()
        if not clean:
            continue
        key = clean.lower()
        if key in seen:
            continue
        seen.add(key)
        result.append(clean)
    return result


def route_row(row: dict[str, Any]) -> dict[str, Any]:
    paper = str(row.get("paper", "")).strip()
    claim_type = normalize_key(str(row.get("claim_type", "")))
    main_claim = str(row.get("main_claim", "") or row.get("claim", "")).strip()
    evidence_type = str(row.get("evidence_type", "") or row.get("evidence", "")).strip()
    limitation = str(row.get("limitation", "") or row.get("key_limitation", "")).strip()
    mechanism = str(row.get("mechanism", "") or row.get("main_mechanism", "")).strip()
    local_implication = str(row.get("local_implication", "") or row.get("deployment_implication", "")).strip()
    confounders = as_list(row.get("confounder") or row.get("confounders"))
    preferred_routes = as_list(row.get("follow_up_vault_route") or row.get("proof_route") or row.get("vault_route"))
    expected_routes = as_list(row.get("expected_route"))
    open_question = str(row.get("open_question", "")).strip()

    normalized = {
        "paper": paper,
        "claim_type": claim_type,
        "main_claim": main_claim,
        "evidence_type": evidence_type,
        "limitation": limitation,
        "mechanism": mechanism,
        "local_implication": local_implication,
        "confounders": confounders,
        "preferred_routes": preferred_routes,
        "expected_routes": expected_routes,
        "open_question": open_question,
    }

    missing: list[str] = []
    for field in REQUIRED_FIELDS:
        if field == "main_claim":
            value = main_claim
        elif field == "evidence_type":
            value = evidence_type
        elif field == "local_implication":
            value = local_implication
        else:
            value = normalized.get(field)
        if not value:
            missing.append(field)

    candidate_routes: list[str] = []
    candidate_routes.extend(preferred_routes)
    candidate_routes.extend(ROUTE_CATALOG.get(claim_type, []))

    combined_text = " ".join([main_claim, evidence_type, limitation, mechanism, local_implication, open_question]).lower()
    for pattern, route in KEYWORD_ROUTES:
        if re.search(pattern, combined_text):
            candidate_routes.append(route)

    for confounder in confounders:
        route = CONFUNDER_ROUTES.get(confounder.strip().lower())
        if route:
            candidate_routes.append(route)

    candidate_routes = unique_routes(candidate_routes)
    primary_route = candidate_routes[0] if candidate_routes else ""

    expected_missing: list[str] = []
    for expected in expected_routes:
        expected_lower = expected.lower()
        if not any(expected_lower in route.lower() for route in candidate_routes):
            expected_missing.append(expected)

    if missing:
        status = "hold"
        decision = "missing_claim_fields"
        next_action = f"Fill missing fields: {', '.join(missing)}"
    elif expected_missing:
        status = "hold"
        decision = "expected_route_not_found"
        next_action = f"Check route expectation: {', '.join(expected_missing)}"
    elif not primary_route:
        status = "hold"
        decision = "no_local_proof_route"
        next_action = "Add follow_up_vault_route or clarify local_implication."
    else:
        status = "pass"
        decision = "paper_claim_route_ready"
        next_action = f"Create or link proof artifact in {wiki_link(primary_route)}."

    proof_question = build_proof_question(normalized, primary_route)
    return {
        **normalized,
        "status": status,
        "decision": decision,
        "missing_fields": missing,
        "expected_routes_missing": expected_missing,
        "primary_route": primary_route,
        "candidate_routes": candidate_routes,
        "proof_question": proof_question,
        "next_action": next_action,
    }


def build_proof_question(row: dict[str, Any], primary_route: str) -> str:
    paper = row["paper"] or "this paper"
    mechanism = row["mechanism"] or "the claimed mechanism"
    local_implication = row["local_implication"] or "the local implication"
    if not primary_route:
        return f"What local evidence would test whether {paper}'s {mechanism} claim affects {local_implication}?"
    return f"Using {wiki_link(primary_route)}, what evidence would test whether {paper}'s {mechanism} claim affects {local_implication}?"


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "paper",
        "claim_type",
        "status",
        "decision",
        "primary_route",
        "main_claim",
        "evidence_type",
        "limitation",
        "mechanism",
        "local_implication",
        "confounders",
        "proof_question",
        "next_action",
        "candidate_routes",
        "missing_fields",
        "expected_routes_missing",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: compact(row.get(field)) for field in fields})


def md_cell(value: Any) -> str:
    return compact(value).replace("\n", "<br>").replace("|", "\\|")


def render_markdown(record: dict[str, Any]) -> str:
    lines = [
        f"# Paper-to-Local Proof Routes - {record['run_id']}",
        "",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Created: `{record['created_at']}`",
        f"- Input: `{record['input_path']}`",
        "",
        "## Routes",
        "",
        "| Paper | Claim type | Status | Primary route | Proof question | Next action |",
        "|---|---|---|---|---|---|",
    ]
    for row in record["rows"]:
        lines.append(
            f"| {md_cell(row['paper'])} | {md_cell(row['claim_type'])} | {md_cell(row['status'])} | {md_cell(wiki_link(row['primary_route']))} | {md_cell(row['proof_question'])} | {md_cell(row['next_action'])} |"
        )

    holds = [row for row in record["rows"] if row["status"] != "pass"]
    if holds:
        lines.extend(["", "## Holds", "", "| Paper | Decision | Missing | Expected route misses |", "|---|---|---|---|"])
        for row in holds:
            lines.append(
                f"| {md_cell(row['paper'])} | {md_cell(row['decision'])} | {md_cell(row['missing_fields'])} | {md_cell(row['expected_routes_missing'])} |"
            )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    input_path, input_rows = load_input()
    run_id = os.environ.get("LLM_PAPER_PROOF_RUN_ID") or f"{utc_stamp()}-{slug(input_path.stem)}"
    run_root = Path(os.environ.get("LLM_PAPER_PROOF_RUN_ROOT", "paper-to-local-proof-runs")).expanduser().resolve()
    run_dir = run_root / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    routed_rows = [route_row(row) for row in input_rows]
    pass_count = sum(1 for row in routed_rows if row["status"] == "pass")
    hold_count = len(routed_rows) - pass_count
    status = "pass" if routed_rows and hold_count == 0 else "hold"
    decision = "all_paper_claim_routes_ready" if status == "pass" else "paper_claim_routes_need_work"

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "input_path": str(input_path),
        "row_count": len(routed_rows),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "rows": routed_rows,
        "outputs": {},
    }

    json_path = run_dir / f"{run_id}-paper-proof-routes.json"
    markdown_path = run_dir / f"{run_id}-paper-proof-routes.md"
    csv_path = run_dir / f"{run_id}-paper-proof-routes.csv"
    jsonl_path = run_root / "paper-to-local-proof-runs.jsonl"
    record["outputs"] = {
        "json": str(json_path),
        "markdown": str(markdown_path),
        "csv": str(csv_path),
        "jsonl": str(jsonl_path),
    }

    csv_write(csv_path, routed_rows)
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
                "row_count": len(routed_rows),
                "pass_count": pass_count,
                "hold_count": hold_count,
                "output_dir": str(run_dir),
            },
            indent=2,
        )
    )
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"status": "error", "decision": "runner_exception", "error": str(exc)}, indent=2), file=sys.stderr)
        raise
```

## PowerShell Run

```powershell
$env:LLM_PAPER_PROOF_INPUT = "D:\llm-reading\paper-claim-rows.json"
$env:LLM_PAPER_PROOF_RUN_ROOT = "D:\llm-reading\paper-proof-routes"
python .\llm_paper_to_local_proof_router.py
```

## Example Input

```json
{
  "papers": [
    {
      "paper": "FlashAttention",
      "claim_type": "inference-systems",
      "main_claim": "IO-aware exact attention reduces memory traffic and improves attention speed.",
      "evidence_type": "systems measurement and kernel benchmark",
      "limitation": "Benefit depends on hardware, sequence length, and runtime integration.",
      "mechanism": "tiled attention and SRAM/HBM traffic",
      "local_implication": "long-context prefill latency and local serving throughput",
      "confounder": "hardware;context",
      "expected_route": "Inference Request Lifecycle"
    }
  ]
}
```

Pass signal: the runner writes JSON, Markdown, CSV, and JSONL; each row has `status=pass`, `decision=paper_claim_route_ready`, a primary route, and a proof question that can be copied into the capstone workbook.

Hold signal: missing fields, missing expected routes, or no local proof route. A hold is useful: it means the paper claim is not yet actionable.

## Capstone Row

| Evidence | Output |
|---|---|
| Paper-to-local proof router | `<run-id>-paper-proof-routes.json`, `<run-id>-paper-proof-routes.md`, `<run-id>-paper-proof-routes.csv`, and one `paper-to-local-proof-runs.jsonl` row |

## References

- [[LLM/Study/LLM Paper Reading Protocol]]
- [[LLM/Study/LLM Paper Claim Ledger]]
- [[LLM/Study/LLM Paper Claim Audit Runner]]
- [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner]]
- [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/LLM Inference Request Lifecycle Runner]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]]
- [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
