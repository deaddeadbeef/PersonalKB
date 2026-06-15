---
tags: [study, llm, rag, local-llm, inference, evaluation, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local RAG Evidence Runner

> **One-line summary** A local RAG assistant is not proven by one good answer; it is proven by artifact evidence for corpus custody, chunk integrity, retrieval hits, selected context, cited answers, unsupported-question refusal, latency, and failure diagnosis.

Use this after [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]] when the experiment folder should become repeatable JSON, Markdown, CSV, and JSONL evidence. The harness explains how to build the local RAG loop. This runner checks whether the saved artifacts prove that loop.

Use [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab|Local RAG Retrieval Evaluation and Reranking Lab]] before this runner when top-k, reranking, hybrid retrieval, or citation audit evidence is still being designed. Use [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] after this runner when answer quality needs a broader task-specific rubric.

This runner does not call a model, embed text, build an index, or scrape current model pages. It validates artifacts already produced by a local run. That keeps the proof portable across Ollama, llama.cpp, vLLM, SGLang, Chroma, FAISS, Qdrant, flat cosine search, or a custom harness.

## What This Proves

| Gate | Evidence checked | Why it matters |
|---|---|---|
| Corpus custody | source ids, titles, paths, allowed-for-RAG flag, digests | proves what the assistant was allowed to know |
| Chunk integrity | chunk ids, source ids, sections, text, citations | makes retrieval and citations auditable |
| Configuration | embedding model, index, generator, endpoint, top-k, context budget | keeps local inference claims reproducible |
| Retrieval | expected sources, retrieved chunks, selected context, hit status | separates retrieval miss from generation failure |
| Generation | saved answer, citations, refusal, support, faithfulness | catches fluent but unsupported local answers |
| Operations | retrieval latency, answer latency, failure mode | connects RAG quality to local serving constraints |
| Next route | pass, hold, fail, owner, and action | chooses the next controlled lab instead of guessing |

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "rag-proof-001",
  "run_root": "D:/llm-runs/rag-proof",
  "experiment_root": "D:/llm-runs/rag-proof",
  "corpus_manifest": "corpus_manifest.jsonl",
  "chunks": "chunks.jsonl",
  "rag_config": "rag_config.json",
  "queries": "queries.jsonl",
  "retrieval_runs": "retrieval_runs.jsonl",
  "answer_runs": "answer_runs.jsonl"
}
```

The paths may be absolute or relative to `experiment_root`.

Expected JSONL row shapes:

```json
{"source_id":"rag-001","title":"RAG Evaluation","path_or_url":"LLM/.../RAG Evaluation.md","allowed_for_rag":true,"updated_at":"2026-06-15","sha256":"..."}
{"chunk_id":"rag-001#s1-c1","source_id":"rag-001","section":"Failure Modes","ordinal":1,"text":"...","citation":"[rag-001:s1:c1]"}
{"query_id":"q001","query":"What are the main RAG failure modes?","expected_source_ids":["rag-001"],"query_type":"supported"}
{"query_id":"q001","retrieved_chunk_ids":["rag-001#s1-c1"],"selected_context_ids":["rag-001#s1-c1"],"sufficient_context":true,"retrieval_latency_ms":42}
{"query_id":"q001","answer_text":"... [rag-001:s1:c1]","citations":["[rag-001:s1:c1]"],"answer_supported":true,"citation_valid":true,"faithfulness_pass":true,"total_latency_ms":920,"failure_mode":""}
```

For unsupported questions, `expected_source_ids` should be an empty list and the answer row should set `refusal: true`.

## Standard-Library Runner

Save the code block as `local_rag_evidence_runner.py` or extract it directly from this note.

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


REQUIRED_SOURCE = ["source_id", "title", "path_or_url", "allowed_for_rag", "sha256"]
REQUIRED_CHUNK = ["chunk_id", "source_id", "section", "text", "citation"]
REQUIRED_CONFIG = [
    "embedding_model",
    "index_type",
    "generator_model",
    "runtime_base_url",
    "top_k",
    "context_budget_tokens",
    "citation_style",
]
REQUIRED_QUERY = ["query_id", "query", "expected_source_ids"]

STATUS_RANK = {"pass": 0, "hold": 1, "fail": 2}


def utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def slug(value: Any) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value or "").strip().lower())
    return text.strip("-") or "rag-evidence"


def norm(value: Any) -> str:
    return str(value or "").strip().lower()


def first_present(mapping: dict[str, Any], *keys: str) -> Any:
    for key in keys:
        if key in mapping and mapping[key] not in (None, ""):
            return mapping[key]
    return None


def bool_value(value: Any) -> bool | None:
    if isinstance(value, bool):
        return value
    if value in (None, ""):
        return None
    text = norm(value).replace("_", "-").replace(" ", "-")
    if text in {"true", "yes", "y", "1", "pass", "passed", "supported", "valid"}:
        return True
    if text in {"false", "no", "n", "0", "fail", "failed", "unsupported", "invalid"}:
        return False
    return None


def number_value(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def list_value(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, tuple):
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


def missing_fields(mapping: dict[str, Any], fields: list[str]) -> list[str]:
    return [field for field in fields if mapping.get(field) in (None, "", [])]


def resolve_path(root: Path, value: Any) -> Path:
    path = Path(str(value)).expanduser()
    if not path.is_absolute():
        path = root / path
    return path.resolve()


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError(f"Expected JSON object: {path}")
    return data


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), start=1):
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"Expected JSON object at {path}:{line_number}")
        rows.append(value)
    return rows


def load_manifest() -> tuple[Path, dict[str, Any]]:
    manifest_path = os.environ.get("LOCAL_RAG_EVIDENCE_MANIFEST")
    if not manifest_path:
        raise ValueError("Set LOCAL_RAG_EVIDENCE_MANIFEST to a JSON manifest path.")
    path = Path(manifest_path).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"Manifest path does not exist: {path}")
    return path, load_json(path)


def finding(level: str, owner: str, text: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "owner": owner,
        "finding": text,
        "evidence": evidence,
        "action": action,
    }


def route_for_owner(owner: str) -> str:
    if owner == "corpus":
        return "LLM/Study/Local RAG Minimal Python Harness"
    if owner == "retrieval":
        return "LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab"
    if owner == "context":
        return "LLM/Study/Local LLM Context Window and Token Budgeting Lab"
    if owner == "generation":
        return "LLM/Study/Local RAG Minimal Python Harness"
    if owner == "quality":
        return "LLM/Study/Local LLM Quality Evaluation Harness"
    if owner == "benchmark":
        return "LLM/Study/Local LLM Inference Benchmark Log"
    if owner == "security":
        return "LLM/Study/Local LLM Security and Privacy Runbook"
    return "LLM/Study/Local RAG Assistant Lab"


def wiki_link(route: str) -> str:
    return "[" + "[" + route + "]" + "]"


def classify(findings: list[dict[str, str]]) -> tuple[str, str, str, str]:
    fail_count = sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        status = "fail"
        decision = "rag_evidence_failed"
    elif hold_count:
        status = "hold"
        decision = "rag_evidence_incomplete"
    else:
        status = "pass"
        decision = "rag_evidence_ready"
    first = findings[0] if findings else None
    next_route = route_for_owner(first["owner"]) if first else route_for_owner("assistant")
    next_action = first["action"] if first else "Promote this run into the capstone evidence ledger."
    return status, decision, next_route, next_action


def source_ids_for_chunks(chunk_ids: list[str], chunks_by_id: dict[str, dict[str, Any]]) -> set[str]:
    source_ids: set[str] = set()
    for chunk_id in chunk_ids:
        chunk = chunks_by_id.get(chunk_id)
        if chunk:
            source_ids.add(str(chunk.get("source_id", "")))
    return {source_id for source_id in source_ids if source_id}


def citation_ids_for_chunks(chunk_ids: list[str], chunks_by_id: dict[str, dict[str, Any]]) -> set[str]:
    citations: set[str] = set()
    for chunk_id in chunk_ids:
        chunk = chunks_by_id.get(chunk_id)
        if chunk:
            citations.add(str(chunk.get("citation", "")))
            citations.add(str(chunk.get("chunk_id", "")))
    return {citation for citation in citations if citation}


def evaluate_query(
    query: dict[str, Any],
    retrieval: dict[str, Any] | None,
    answer: dict[str, Any] | None,
    chunks_by_id: dict[str, dict[str, Any]],
    citation_required: bool,
) -> dict[str, Any]:
    findings: list[dict[str, str]] = []
    query_id = str(query.get("query_id", ""))
    query_missing = [field for field in REQUIRED_QUERY if field not in query or query.get(field) in (None, "")]
    if query_missing:
        findings.append(finding(
            "hold",
            "retrieval",
            "Query row is incomplete.",
            ", ".join(query_missing),
            "Fill the query set before accepting retrieval or answer quality.",
        ))

    expected_sources = list_value(query.get("expected_source_ids"))
    is_supported = len(expected_sources) > 0
    query_type = str(query.get("query_type") or ("supported" if is_supported else "unsupported"))

    if retrieval is None:
        findings.append(finding(
            "hold",
            "retrieval",
            "Retrieval evidence is missing for this query.",
            query_id,
            "Run retrieval and save retrieved_chunk_ids plus selected_context_ids.",
        ))
        retrieval = {}

    retrieved_chunk_ids = list_value(first_present(retrieval, "retrieved_chunk_ids", "retrieved_ids", "top_k_chunk_ids"))
    selected_context_ids = list_value(first_present(retrieval, "selected_context_ids", "context_chunk_ids", "final_context_ids"))
    unknown_retrieved = [chunk_id for chunk_id in retrieved_chunk_ids if chunk_id not in chunks_by_id]
    unknown_selected = [chunk_id for chunk_id in selected_context_ids if chunk_id not in chunks_by_id]
    if unknown_retrieved or unknown_selected:
        findings.append(finding(
            "fail",
            "corpus",
            "Retrieval references chunk ids not present in chunks.jsonl.",
            ", ".join(unknown_retrieved + unknown_selected),
            "Rebuild chunks, index, and retrieval evidence from the same corpus version.",
        ))

    retrieved_sources = source_ids_for_chunks(retrieved_chunk_ids, chunks_by_id)
    selected_sources = source_ids_for_chunks(selected_context_ids, chunks_by_id)
    expected_set = set(expected_sources)
    retrieved_hit = bool(expected_set & retrieved_sources) if is_supported else False
    selected_hit = bool(expected_set & selected_sources) if is_supported else False

    if is_supported and not retrieved_hit:
        findings.append(finding(
            "fail",
            "retrieval",
            "Expected source was not retrieved.",
            "expected=" + ",".join(expected_sources) + "; retrieved_sources=" + ",".join(sorted(retrieved_sources)),
            "Fix corpus, chunking, embedding, query rewrite, metadata filter, hybrid search, or top-k before judging the generator.",
        ))
    elif is_supported and not selected_hit:
        findings.append(finding(
            "fail",
            "context",
            "Expected source was retrieved but not selected for final context.",
            "expected=" + ",".join(expected_sources) + "; selected_sources=" + ",".join(sorted(selected_sources)),
            "Fix reranking, dedupe, context packing, or context budget before generation.",
        ))

    sufficient_context = bool_value(first_present(retrieval, "sufficient_context", "context_sufficient"))
    if is_supported and sufficient_context is False:
        findings.append(finding(
            "fail",
            "context",
            "Retrieval run marked context as insufficient for a supported query.",
            query_id,
            "Do not generate an accepted answer until context selection is sufficient.",
        ))
    if not is_supported and sufficient_context is True:
        findings.append(finding(
            "fail",
            "retrieval",
            "Unsupported query was marked as having sufficient context.",
            query_id,
            "Strengthen the retrieval sufficiency rule and refusal boundary.",
        ))

    retrieval_latency = number_value(first_present(retrieval, "retrieval_latency_ms", "latency_ms"))
    if retrieval_latency is None:
        findings.append(finding(
            "hold",
            "benchmark",
            "Retrieval latency is missing.",
            query_id,
            "Record embedding, search, filter, and reranking latency before accepting local usability.",
        ))

    if answer is None:
        findings.append(finding(
            "hold",
            "generation",
            "Answer evidence is missing for this query.",
            query_id,
            "Save answer text, citations, support decision, and latency.",
        ))
        answer = {}

    answer_text = str(answer.get("answer_text", ""))
    citations = list_value(first_present(answer, "citations", "citation_ids"))
    answer_supported = bool_value(first_present(answer, "answer_supported", "supported"))
    citation_valid = bool_value(first_present(answer, "citation_valid", "citations_valid"))
    faithfulness_pass = bool_value(first_present(answer, "faithfulness_pass", "faithful"))
    refusal = bool_value(first_present(answer, "refusal", "refused", "not_enough_evidence"))
    total_latency = number_value(first_present(answer, "total_latency_ms", "latency_ms"))

    selected_citations = citation_ids_for_chunks(selected_context_ids, chunks_by_id)
    unknown_citations = [citation for citation in citations if citation not in selected_citations]
    if citation_required and is_supported and not citations:
        findings.append(finding(
            "fail",
            "quality",
            "Supported answer has no citations.",
            query_id,
            "Generate with pre-assigned citation labels and save cited answer evidence.",
        ))
    if unknown_citations:
        findings.append(finding(
            "fail",
            "quality",
            "Answer cites chunks or labels that were not selected as context.",
            ", ".join(unknown_citations),
            "Validate citations against selected context before accepting the answer.",
        ))

    if is_supported:
        if not answer_text.strip():
            findings.append(finding(
                "hold",
                "generation",
                "Supported query has no saved answer text.",
                query_id,
                "Save the generated answer text or rerun generation.",
            ))
        if answer_supported is not True:
            findings.append(finding(
                "fail" if answer_supported is False else "hold",
                "quality",
                "Answer support is not proven.",
                str(answer_supported),
                "Mark whether the answer is supported by selected context.",
            ))
        if citation_valid is not True:
            findings.append(finding(
                "fail" if citation_valid is False else "hold",
                "quality",
                "Citation validity is not proven.",
                str(citation_valid),
                "Audit citations claim by claim against selected chunks.",
            ))
        if faithfulness_pass is not True:
            findings.append(finding(
                "fail" if faithfulness_pass is False else "hold",
                "quality",
                "Faithfulness is not proven.",
                str(faithfulness_pass),
                "Check whether every substantive claim is supported by context.",
            ))
    else:
        if refusal is not True:
            findings.append(finding(
                "fail" if refusal is False else "hold",
                "quality",
                "Unsupported query refusal is not proven.",
                str(refusal),
                "Ask an unsupported question and verify that the assistant refuses or says not enough evidence.",
            ))
        if citations:
            findings.append(finding(
                "fail",
                "quality",
                "Unsupported answer contains citations.",
                ", ".join(citations),
                "Unsupported queries should not cite weak or irrelevant chunks as evidence.",
            ))

    if total_latency is None:
        findings.append(finding(
            "hold",
            "benchmark",
            "Answer latency is missing.",
            query_id,
            "Record end-to-end RAG latency before accepting local usability.",
        ))

    failure_mode = str(first_present(answer, "failure_mode") or first_present(retrieval, "failure_mode") or query.get("failure_mode") or "")
    if any(item["level"] == "fail" for item in findings) and not failure_mode:
        findings.append(finding(
            "hold",
            "quality",
            "Failure mode is missing for a failed query.",
            query_id,
            "Name the failed layer before changing model, retriever, chunking, prompt, or runtime.",
        ))

    status, decision, next_route, next_action = classify(findings)
    return {
        "query_id": query_id,
        "query_type": query_type,
        "query": str(query.get("query", "")),
        "expected_source_ids": expected_sources,
        "retrieved_chunk_ids": retrieved_chunk_ids,
        "selected_context_ids": selected_context_ids,
        "retrieved_expected_source": retrieved_hit,
        "selected_expected_source": selected_hit,
        "answer_supported": answer_supported,
        "citation_valid": citation_valid,
        "faithfulness_pass": faithfulness_pass,
        "refusal": refusal,
        "retrieval_latency_ms": retrieval_latency,
        "total_latency_ms": total_latency,
        "failure_mode": failure_mode,
        "status": status,
        "decision": decision,
        "next_route": next_route,
        "next_action": next_action,
        "findings": findings,
    }


def csv_cell(value: Any) -> str:
    if isinstance(value, list):
        return ";".join(str(item) for item in value)
    if value is None:
        return ""
    return str(value)


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "query_id",
        "query_type",
        "status",
        "decision",
        "expected_source_ids",
        "retrieved_chunk_ids",
        "selected_context_ids",
        "retrieved_expected_source",
        "selected_expected_source",
        "answer_supported",
        "citation_valid",
        "faithfulness_pass",
        "refusal",
        "retrieval_latency_ms",
        "total_latency_ms",
        "failure_mode",
        "next_route",
        "next_action",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: csv_cell(row.get(field)) for field in fields})


def md_cell(value: Any) -> str:
    return csv_cell(value).replace("|", "\\|").replace("\n", " ")


def render_markdown(record: dict[str, Any]) -> str:
    lines = [
        f"# Local RAG Evidence Run - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Experiment root: `{record['experiment_root']}`",
        f"- Corpus sources: `{record['source_count']}`",
        f"- Chunks: `{record['chunk_count']}`",
        f"- Queries: `{record['query_count']}`",
        f"- Pass/Hold/Fail: `{record['pass_count']}` / `{record['hold_count']}` / `{record['fail_count']}`",
        "",
        "## Findings",
        "",
    ]
    if record["artifact_findings"]:
        for item in record["artifact_findings"]:
            lines.append(f"- `{item['level']}` `{item['owner']}` {item['finding']} Evidence: {item['evidence']} Action: {item['action']}")
    else:
        lines.append("- No artifact-level findings.")
    lines.extend([
        "",
        "## Query Results",
        "",
        "| Query | Type | Status | Retrieved expected? | Selected expected? | Answer supported? | Citations valid? | Refusal? | Failure mode | Next route |",
        "|---|---|---|---:|---:|---:|---:|---:|---|---|",
    ])
    for row in record["queries"]:
        lines.append(
            "| "
            + " | ".join([
                md_cell(row["query_id"]),
                md_cell(row["query_type"]),
                md_cell(row["status"]),
                md_cell(row["retrieved_expected_source"]),
                md_cell(row["selected_expected_source"]),
                md_cell(row["answer_supported"]),
                md_cell(row["citation_valid"]),
                md_cell(row["refusal"]),
                md_cell(row["failure_mode"]),
                md_cell(wiki_link(row["next_route"])),
            ])
            + " |"
        )
    lines.extend([
        "",
        "## Next Actions",
        "",
    ])
    for row in record["queries"]:
        if row["status"] != "pass":
            lines.append(f"- `{row['query_id']}` -> {wiki_link(row['next_route'])}: {row['next_action']}")
    if all(row["status"] == "pass" for row in record["queries"]) and not record["artifact_findings"]:
        lines.append("- Promote this evidence packet into the capstone workbook.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    manifest_path, manifest = load_manifest()
    experiment_root = resolve_path(manifest_path.parent, manifest.get("experiment_root", manifest_path.parent))
    run_id = str(manifest.get("run_id") or os.environ.get("LOCAL_RAG_EVIDENCE_RUN_ID") or f"{utc_stamp()}-{slug(experiment_root.name)}")
    run_root_value = os.environ.get("LOCAL_RAG_EVIDENCE_RUN_ROOT") or manifest.get("run_root", "rag-evidence-runs")
    run_root = resolve_path(experiment_root, run_root_value)
    run_dir = run_root / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    required_manifest = ["corpus_manifest", "chunks", "rag_config", "queries", "retrieval_runs", "answer_runs"]
    manifest_missing = missing_fields(manifest, required_manifest)
    if manifest_missing:
        raise ValueError("Manifest missing required paths: " + ", ".join(manifest_missing))

    corpus_path = resolve_path(experiment_root, manifest["corpus_manifest"])
    chunks_path = resolve_path(experiment_root, manifest["chunks"])
    config_path = resolve_path(experiment_root, manifest["rag_config"])
    queries_path = resolve_path(experiment_root, manifest["queries"])
    retrieval_path = resolve_path(experiment_root, manifest["retrieval_runs"])
    answer_path = resolve_path(experiment_root, manifest["answer_runs"])

    for path in [corpus_path, chunks_path, config_path, queries_path, retrieval_path, answer_path]:
        if not path.exists():
            raise FileNotFoundError(f"Required artifact path does not exist: {path}")

    corpus = load_jsonl(corpus_path)
    chunks = load_jsonl(chunks_path)
    config = load_json(config_path)
    queries = load_jsonl(queries_path)
    retrieval_rows = load_jsonl(retrieval_path)
    answer_rows = load_jsonl(answer_path)

    artifact_findings: list[dict[str, str]] = []
    config_missing = missing_fields(config, REQUIRED_CONFIG)
    if config_missing:
        artifact_findings.append(finding(
            "hold",
            "context",
            "RAG config is incomplete.",
            ", ".join(config_missing),
            "Record embedding, index, generator, endpoint, top-k, context budget, and citation style.",
        ))

    sources_by_id: dict[str, dict[str, Any]] = {}
    for row in corpus:
        missing = missing_fields(row, REQUIRED_SOURCE)
        source_id = str(row.get("source_id", ""))
        if source_id:
            sources_by_id[source_id] = row
        if missing:
            artifact_findings.append(finding(
                "hold",
                "corpus",
                "Corpus manifest row is incomplete.",
                source_id or "(missing source_id)",
                "Missing fields: " + ", ".join(missing),
            ))
        if bool_value(row.get("allowed_for_rag")) is not True:
            artifact_findings.append(finding(
                "fail",
                "security",
                "Corpus source is not explicitly allowed for RAG.",
                source_id or "(missing source_id)",
                "Remove the source or set a deliberate allowed_for_rag boundary before indexing.",
            ))

    chunks_by_id: dict[str, dict[str, Any]] = {}
    for row in chunks:
        missing = missing_fields(row, REQUIRED_CHUNK)
        chunk_id = str(row.get("chunk_id", ""))
        if chunk_id:
            chunks_by_id[chunk_id] = row
        if missing:
            artifact_findings.append(finding(
                "hold",
                "corpus",
                "Chunk row is incomplete.",
                chunk_id or "(missing chunk_id)",
                "Missing fields: " + ", ".join(missing),
            ))
        source_id = str(row.get("source_id", ""))
        if source_id and source_id not in sources_by_id:
            artifact_findings.append(finding(
                "fail",
                "corpus",
                "Chunk source_id is not present in corpus_manifest.jsonl.",
                f"{chunk_id} -> {source_id}",
                "Rebuild chunks from the same corpus manifest.",
            ))

    retrieval_by_query = {str(row.get("query_id", "")): row for row in retrieval_rows if row.get("query_id")}
    answer_by_query = {str(row.get("query_id", "")): row for row in answer_rows if row.get("query_id")}
    citation_required = norm(config.get("citation_style")) not in {"", "none", "not required", "not-required"}

    supported_count = sum(1 for row in queries if list_value(row.get("expected_source_ids")))
    unsupported_count = len(queries) - supported_count
    if supported_count == 0:
        artifact_findings.append(finding(
            "hold",
            "retrieval",
            "Query set has no supported query.",
            str(queries_path),
            "Add at least one known-answer question with expected_source_ids.",
        ))
    if unsupported_count == 0:
        artifact_findings.append(finding(
            "hold",
            "quality",
            "Query set has no unsupported refusal test.",
            str(queries_path),
            "Add at least one question with no expected sources and a required refusal.",
        ))

    evaluated = [
        evaluate_query(
            query,
            retrieval_by_query.get(str(query.get("query_id", ""))),
            answer_by_query.get(str(query.get("query_id", ""))),
            chunks_by_id,
            citation_required,
        )
        for query in queries
    ]
    evaluated.sort(key=lambda row: (STATUS_RANK.get(row["status"], 3), row["query_id"]))

    if not any(row.get("failure_mode") for row in evaluated):
        artifact_findings.append(finding(
            "hold",
            "quality",
            "Run has no diagnosed failure row.",
            run_id,
            "Record at least one retrieval, context, generation, citation, or benchmark failure mode for the capstone.",
        ))

    artifact_status, artifact_decision, artifact_next_route, artifact_next_action = classify(artifact_findings)
    pass_count = sum(1 for row in evaluated if row["status"] == "pass")
    hold_count = sum(1 for row in evaluated if row["status"] == "hold")
    fail_count = sum(1 for row in evaluated if row["status"] == "fail")
    if artifact_status == "fail" or fail_count:
        status = "fail"
        decision = "rag_evidence_failed"
    elif artifact_status == "hold" or hold_count:
        status = "hold"
        decision = "rag_evidence_incomplete"
    else:
        status = "pass"
        decision = "rag_evidence_ready"

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "manifest_path": str(manifest_path),
        "experiment_root": str(experiment_root),
        "source_count": len(corpus),
        "chunk_count": len(chunks),
        "query_count": len(queries),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "artifact_status": artifact_status,
        "artifact_decision": artifact_decision,
        "artifact_next_route": artifact_next_route,
        "artifact_next_action": artifact_next_action,
        "artifact_findings": artifact_findings,
        "queries": evaluated,
        "outputs": {},
    }

    json_path = run_dir / f"{run_id}-rag-evidence.json"
    markdown_path = run_dir / f"{run_id}-rag-evidence.md"
    csv_path = run_dir / f"{run_id}-rag-evidence.csv"
    jsonl_path = run_root / "rag-evidence-runs.jsonl"
    record["outputs"] = {
        "json": str(json_path),
        "markdown": str(markdown_path),
        "csv": str(csv_path),
        "jsonl": str(jsonl_path),
    }

    csv_write(csv_path, evaluated)
    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    markdown_path.write_text(render_markdown(record), encoding="utf-8")
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(json.dumps({
        "status": status,
        "decision": decision,
        "run_id": run_id,
        "source_count": len(corpus),
        "chunk_count": len(chunks),
        "query_count": len(queries),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "output_dir": str(run_dir),
    }, indent=2))
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
$env:LOCAL_RAG_EVIDENCE_MANIFEST = "D:\llm-runs\rag-proof\rag-evidence-manifest.json"
$env:LOCAL_RAG_EVIDENCE_RUN_ROOT = "D:\llm-runs\rag-proof"
python .\local_rag_evidence_runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/rag_evidence_ready` | corpus, chunks, config, supported query, unsupported refusal, citations, support, faithfulness, latency, and failure diagnosis are all present | promote to [[LLM/Study/LLM Mastery Capstone Workbook]] |
| `hold/rag_evidence_incomplete` | no hard contradiction, but a required artifact, latency, support, citation, refusal, or failure-diagnosis field is missing | follow each query's `next_route` |
| `fail/rag_evidence_failed` | a hard gate failed: source not allowed, chunk mismatch, expected source missing, context omitted evidence, citation invalid, hallucination, or refusal failure | fix the named layer before changing model size |

A `fail` result can be useful if it names the layer and first controlled change. A failed RAG row is better evidence than a vague complaint that the local model is weak.

## Capstone Row

| Evidence | Output |
|---|---|
| RAG evidence runner | `<run-id>-rag-evidence.json`, `<run-id>-rag-evidence.md`, `<run-id>-rag-evidence.csv`, and one `rag-evidence-runs.jsonl` row |

## Completion Gate

This runner is complete when:

- [ ] the manifest points to corpus, chunks, config, query, retrieval, and answer artifacts
- [ ] at least one supported query retrieves and selects the expected source
- [ ] at least one unsupported query proves refusal behavior
- [ ] every accepted supported answer has citations that point to selected chunks
- [ ] support, citation validity, faithfulness, retrieval latency, and answer latency are recorded
- [ ] at least one failure mode row exists for diagnostic learning
- [ ] the output JSON, Markdown, CSV, and JSONL artifacts are saved

## References

- [[LLM/Study/Local RAG Assistant Lab]]
- [[LLM/Study/Local RAG Minimal Python Harness]]
- [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab]]
- [[LLM/Study/Local Embedding and Reranker Hosting Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes]]
