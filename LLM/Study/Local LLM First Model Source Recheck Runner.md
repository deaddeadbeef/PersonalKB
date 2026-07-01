---
tags: [study, llm, inference, local-llm, ollama, model-selection, provenance, first-run, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice]
last-verified: 2026-06-16
---

# Local LLM First Model Source Recheck Runner

> **One-line summary** Recheck the current model registry pages for the first local model candidates before trusting a command plan, pull gate, or endpoint run sheet.

Use this after [[LLM/Study/Local LLM First Model Candidate Ladder|Local LLM First Model Candidate Ladder]] picks a baseline, fallback, and stretch class, and before [[LLM/Study/Local LLM First Run Command Plan Runner|Local LLM First Run Command Plan Runner]] or [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]] freezes the first pull. The runner fetches the source pages, checks expected snippets such as tag, digest, size, context, modality, architecture, parameter count, and quantization, then writes JSON, Markdown, CSV, and JSONL evidence.

This runner does not install Ollama, pull a model, inspect local blobs, or send inference requests. It answers only: "Do the current source pages still match the candidate facts we are about to use?"

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| Source URL fetch | The model page or tag page is reachable now. | The local runtime can pull from it. |
| Required snippets | The expected tag, digest, size, context, modality, and quantization claims are still visible. | The local blob checksum after pull. |
| Candidate status | Baseline, fallback, text-only control, and stretch candidates are pass, hold, or fail before download. | That the model is high quality for the workload. |
| JSONL handoff | Later pull/endpoint artifacts can cite the exact source check run. | That a later page update did not happen. |

Academic bridge: model selection is a custody problem before it is a performance problem. If the selected artifact changes under the same tag, local benchmark or quality results become hard to interpret.

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "first-model-source-recheck-001",
  "run_root": "D:/llm-runs/2026-06-16-first-local-inference",
  "source_checked_at": "2026-06-16",
  "candidates": [
    {
      "candidate_id": "baseline-qwen35-4b",
      "slot": "route-proof baseline",
      "model_id": "qwen3.5:4b",
      "source_url": "https://ollama.com/library/qwen3.5:4b",
      "required": true,
      "expected_snippets": [
        "ollama run qwen3.5:4b",
        "2a654d98e6fb",
        "3.4GB",
        "parameters 4.66B",
        "quantization Q4_K_M",
        "Apache License Version 2.0"
      ],
      "next_route": "LLM/Study/Local LLM First Run Command Plan Runner"
    }
  ]
}
```

Recommended first-run candidates for this machine. The 2026-06-16 applied run used `qwen3.5:2b-q4_K_M` because that required smaller fallback passed the live source check, while optional 4B/control snippets needed refresh before use:

```json
[
  {
    "candidate_id": "baseline-qwen35-4b",
    "slot": "optional larger baseline to refresh",
    "model_id": "qwen3.5:4b",
    "source_url": "https://ollama.com/library/qwen3.5:4b",
    "required": false,
    "expected_snippets": ["2a654d98e6fb", "3.4GB", "parameters 4.66B", "quantization Q4_K_M"]
  },
  {
    "candidate_id": "small-fallback-qwen35-2b-q4",
    "slot": "emergency smaller fallback",
    "model_id": "qwen3.5:2b-q4_K_M",
    "source_url": "https://ollama.com/library/qwen3.5/tags",
    "required": true,
    "expected_snippets": ["qwen3.5:2b-q4_K_M", "124a03c34777", "1.9GB", "256K", "Text, Image"]
  },
  {
    "candidate_id": "text-control-qwen3-4b-instruct",
    "slot": "text-only instruct control",
    "model_id": "qwen3:4b-instruct",
    "source_url": "https://ollama.com/library/qwen3:4b-instruct",
    "required": false,
    "expected_snippets": ["0edcdef34593", "2.5GB", "parameters 4.02B", "quantization Q4_K_M"]
  },
  {
    "candidate_id": "stretch-qwen35-9b",
    "slot": "practical stretch",
    "model_id": "qwen3.5:9b",
    "source_url": "https://ollama.com/library/qwen3.5/tags",
    "required": false,
    "expected_snippets": ["qwen3.5:9b", "6488c96fa5fa", "6.6GB", "256K", "Text, Image"]
  }
]
```

## Standard-Library Runner

Save this as `first-model-source-recheck.py` in the run folder. It uses only Python's standard library.

```python
from __future__ import annotations

import csv
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


def utc_iso() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def slug(value: Any) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value or "").strip()).strip("-")
    return text or "run"


def display(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def bool_value(value: Any, default: bool = False) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def list_value(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [display(item) for item in value if display(item)]
    if isinstance(value, str):
        return [item.strip() for item in re.split(r"[;\n]", value) if item.strip()]
    return [display(value)] if display(value) else []


def normalize_page(value: str) -> str:
    return re.sub(r"\s+", " ", value or "")


def load_manifest() -> tuple[Path, dict[str, Any]]:
    manifest_value = os.environ.get("LOCAL_LLM_FIRST_MODEL_SOURCE_RECHECK_MANIFEST") or (
        sys.argv[1] if len(sys.argv) > 1 else ""
    )
    if not manifest_value:
        raise ValueError("Set LOCAL_LLM_FIRST_MODEL_SOURCE_RECHECK_MANIFEST or pass a manifest path.")
    path = Path(manifest_value).expanduser().resolve()
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict):
        raise ValueError("Manifest must be a JSON object.")
    return path, manifest


def wiki_link(route: str) -> str:
    clean = display(route)
    if not clean:
        return ""
    label = clean.split("/")[-1]
    open_link = "[" * 2
    close_link = "]" * 2
    return open_link + clean + "|" + label + close_link


def finding(level: str, owner: str, text: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "owner": owner,
        "finding": text,
        "evidence": evidence,
        "action": action,
    }


def fetch_source(url: str, timeout_s: float) -> dict[str, Any]:
    request = urllib.request.Request(url, headers={"User-Agent": "PersonalKB-source-recheck/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout_s) as response:
            raw = response.read()
            text = raw.decode("utf-8", errors="replace")
            return {
                "status": "pass",
                "http_status": getattr(response, "status", None),
                "bytes": len(raw),
                "text_excerpt": normalize_page(text)[:500],
                "page_text": normalize_page(text),
            }
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return {
            "status": "error",
            "http_status": exc.code,
            "error_class": "HTTPError",
            "error": str(exc),
            "text_excerpt": normalize_page(body)[:500],
            "page_text": normalize_page(body),
        }
    except Exception as exc:
        return {
            "status": "error",
            "error_class": type(exc).__name__,
            "error": str(exc),
            "text_excerpt": "",
            "page_text": "",
        }


def check_snippets(page_text: str, snippets: list[str]) -> tuple[list[str], list[str]]:
    present: list[str] = []
    missing: list[str] = []
    page_lower = page_text.lower()
    for snippet in snippets:
        if snippet.lower() in page_lower:
            present.append(snippet)
        else:
            missing.append(snippet)
    return present, missing


def evaluate_candidate(candidate: dict[str, Any], manifest: dict[str, Any]) -> dict[str, Any]:
    candidate_id = display(candidate.get("candidate_id") or candidate.get("model_id") or "candidate")
    model_id = display(candidate.get("model_id"))
    source_url = display(candidate.get("source_url"))
    expected_snippets = list_value(candidate.get("expected_snippets"))
    required = bool_value(candidate.get("required"), True)
    source_checked_at = display(candidate.get("source_checked_at") or manifest.get("source_checked_at"))
    timeout_s = float(candidate.get("timeout_s") or manifest.get("timeout_s") or 15)
    next_route = display(candidate.get("next_route") or "LLM/Study/Local LLM First Model Pull Gate")
    findings: list[dict[str, str]] = []

    if not model_id:
        findings.append(finding("hold", "candidate", "Model id is missing.", candidate_id, "Fill the candidate model id before source recheck."))
    if not source_url:
        findings.append(finding("hold", "source", "Source URL is missing.", candidate_id, "Link the model page or tags page before source recheck."))
    if not source_checked_at:
        findings.append(finding("hold", "source", "Source check date is missing.", candidate_id, "Set source_checked_at to the current check date."))
    if not expected_snippets:
        findings.append(finding("hold", "source", "No expected source snippets were supplied.", candidate_id, "Add tag, digest, size, context, modality, license, or quantization snippets."))

    fetch = {"status": "skipped", "page_text": ""}
    present: list[str] = []
    missing: list[str] = []
    if source_url:
        fetch = fetch_source(source_url, timeout_s)
        if fetch["status"] != "pass":
            findings.append(
                finding(
                    "hold",
                    "source",
                    "Source page could not be fetched.",
                    f"{source_url}: {fetch.get('error_class', '')} {fetch.get('error', '')}".strip(),
                    "Retry with network access or mark the source check partial before pulling.",
                )
            )
        else:
            present, missing = check_snippets(fetch.get("page_text", ""), expected_snippets)
            if missing:
                findings.append(
                    finding(
                        "fail",
                        "source",
                        "Fetched source page is missing expected snippets.",
                        "; ".join(missing),
                        "Hold the pull, refresh candidate facts, or choose a source-checked fallback.",
                    )
                )

    if any(item["level"] == "fail" for item in findings):
        status = "fail"
        decision = "candidate_source_contradicted"
    elif any(item["level"] == "hold" for item in findings):
        status = "hold"
        decision = "candidate_source_incomplete"
    else:
        status = "pass"
        decision = "candidate_source_rechecked"

    return {
        "candidate_id": candidate_id,
        "slot": display(candidate.get("slot")),
        "model_id": model_id,
        "required": required,
        "source_url": source_url,
        "source_checked_at": source_checked_at,
        "status": status,
        "decision": decision,
        "expected_snippet_count": len(expected_snippets),
        "present_snippets": present,
        "missing_snippets": missing,
        "fetch_status": fetch.get("status"),
        "http_status": fetch.get("http_status"),
        "bytes": fetch.get("bytes", 0),
        "text_excerpt": fetch.get("text_excerpt", ""),
        "next_route": next_route,
        "findings": findings,
    }


def md_cell(value: Any) -> str:
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True, sort_keys=True)
    return display(value).replace("|", "\\|").replace("\n", " ")


def render_markdown(record: dict[str, Any]) -> str:
    lines = [
        f"# Local LLM First Model Source Recheck - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Source checked at: `{record['source_checked_at']}`",
        f"- Candidate count: `{record['candidate_count']}`",
        f"- Next route: {wiki_link(record['next_route'])}",
        "",
        "## Candidates",
        "",
        "| Candidate | Required | Model | Status | Decision | Missing snippets | Next route |",
        "|---|---:|---|---|---|---|---|",
    ]
    for row in record["candidates"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    md_cell(row["candidate_id"]),
                    md_cell(row["required"]),
                    md_cell(row["model_id"]),
                    md_cell(row["status"]),
                    md_cell(row["decision"]),
                    md_cell(row["missing_snippets"]),
                    md_cell(wiki_link(row["next_route"])),
                ]
            )
            + " |"
        )
    lines.extend(["", "## Findings", ""])
    if record["findings"]:
        for item in record["findings"]:
            lines.append(f"- `{item['level']}` `{item['candidate_id']}` `{item['owner']}`: {item['finding']} -> {item['action']}")
    else:
        lines.append("- All required candidate source checks passed.")
    return "\n".join(lines) + "\n"


def write_csv(path: Path, candidates: list[dict[str, Any]]) -> None:
    fieldnames = [
        "candidate_id",
        "slot",
        "model_id",
        "required",
        "source_url",
        "source_checked_at",
        "status",
        "decision",
        "expected_snippet_count",
        "missing_snippets",
        "next_route",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in candidates:
            writer.writerow({field: md_cell(row.get(field, "")) for field in fieldnames})


def main() -> int:
    manifest_path, manifest = load_manifest()
    candidates_raw = manifest.get("candidates")
    if not isinstance(candidates_raw, list) or not candidates_raw:
        raise ValueError("Manifest must include a non-empty candidates list.")
    candidates = [evaluate_candidate(row, manifest) for row in candidates_raw if isinstance(row, dict)]
    findings = [
        {"candidate_id": row["candidate_id"], **finding_row}
        for row in candidates
        for finding_row in row["findings"]
    ]
    required_rows = [row for row in candidates if row["required"]]
    required_fail_count = sum(1 for row in required_rows if row["status"] == "fail")
    required_hold_count = sum(1 for row in required_rows if row["status"] == "hold")
    if required_fail_count:
        status = "fail"
        decision = "first_model_source_contradicted"
        next_route = "LLM/Study/Local LLM First Model Candidate Ladder"
    elif required_hold_count:
        status = "hold"
        decision = "first_model_source_incomplete"
        next_route = "LLM/Study/Local LLM First Model Candidate Ladder"
    else:
        status = "pass"
        decision = "first_model_source_rechecked"
        next_route = display(manifest.get("next_route") or "LLM/Study/Local LLM First Run Command Plan Runner")

    run_id = display(manifest.get("run_id") or f"{utc_stamp()}-{slug(manifest_path.stem)}")
    run_root_value = display(manifest.get("run_root") or os.environ.get("LOCAL_LLM_FIRST_MODEL_SOURCE_RECHECK_RUN_ROOT") or "first-model-source-recheck-runs")
    run_root = Path(run_root_value).expanduser()
    if not run_root.is_absolute():
        run_root = manifest_path.parent / run_root
    output_root = run_root / "first-model-source-recheck"
    output_dir = output_root / slug(run_id)
    output_dir.mkdir(parents=True, exist_ok=True)

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "manifest_path": str(manifest_path),
        "source_checked_at": display(manifest.get("source_checked_at")),
        "status": status,
        "decision": decision,
        "next_route": next_route,
        "candidate_count": len(candidates),
        "required_candidate_count": len(required_rows),
        "required_fail_count": required_fail_count,
        "required_hold_count": required_hold_count,
        "finding_count": len(findings),
        "findings": findings,
        "candidates": candidates,
        "outputs": {},
    }

    json_path = output_dir / f"{slug(run_id)}-model-source-recheck.json"
    markdown_path = output_dir / f"{slug(run_id)}-model-source-recheck.md"
    csv_path = output_dir / f"{slug(run_id)}-model-source-recheck.csv"
    jsonl_path = output_root / "model-source-rechecks.jsonl"
    record["outputs"] = {
        "json": str(json_path),
        "markdown": str(markdown_path),
        "csv": str(csv_path),
        "jsonl": str(jsonl_path),
    }
    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(record), encoding="utf-8")
    write_csv(csv_path, candidates)
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=True) + "\n")

    print(
        json.dumps(
            {
                "status": status,
                "decision": decision,
                "run_id": run_id,
                "candidate_count": len(candidates),
                "required_fail_count": required_fail_count,
                "required_hold_count": required_hold_count,
                "output_dir": str(output_dir),
                "next_route": next_route,
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
        raise SystemExit(3)
```

## PowerShell Run

```powershell
$RunRoot = "D:\llm-runs\2026-06-16-first-local-inference"
$Manifest = Join-Path $RunRoot "first-model-source-recheck-manifest.json"
New-Item -ItemType Directory -Force -Path $RunRoot | Out-Null

@{
  run_id = "first-model-source-recheck-001"
  run_root = $RunRoot
  source_checked_at = "2026-06-16"
  next_route = "LLM/Study/Local LLM First Run Command Plan Runner"
  candidates = @(
    @{
      candidate_id = "baseline-qwen35-4b"
      slot = "optional larger baseline to refresh"
      model_id = "qwen3.5:4b"
      source_url = "https://ollama.com/library/qwen3.5:4b"
      required = $false
      expected_snippets = @("ollama run qwen3.5:4b", "2a654d98e6fb", "3.4GB", "parameters 4.66B", "quantization Q4_K_M")
      next_route = "LLM/Study/Local LLM First Run Command Plan Runner"
    },
    @{
      candidate_id = "small-fallback-qwen35-2b-q4"
      slot = "emergency smaller fallback"
      model_id = "qwen3.5:2b-q4_K_M"
      source_url = "https://ollama.com/library/qwen3.5/tags"
      required = $true
      expected_snippets = @("qwen3.5:2b-q4_K_M", "124a03c34777", "1.9GB", "256K", "Text, Image")
      next_route = "LLM/Study/Local LLM First Run Command Plan Runner"
    },
    @{
      candidate_id = "text-control-qwen3-4b-instruct"
      slot = "text-only instruct control"
      model_id = "qwen3:4b-instruct"
      source_url = "https://ollama.com/library/qwen3:4b-instruct"
      required = $false
      expected_snippets = @("ollama run qwen3:4b-instruct", "0edcdef34593", "2.5GB", "parameters 4.02B", "quantization Q4_K_M")
      next_route = "LLM/Study/Local LLM First Run Command Plan Runner"
    }
  )
} | ConvertTo-Json -Depth 10 | Set-Content $Manifest -Encoding utf8

$env:LOCAL_LLM_FIRST_MODEL_SOURCE_RECHECK_MANIFEST = $Manifest
python .\first-model-source-recheck.py
```

Pass signal: `pass/first_model_source_rechecked`, with JSON, Markdown, CSV, and JSONL outputs linked from the first-run folder before `ollama pull`.

## Result Decisions

| Status / decision | Meaning | Next route |
|---|---|---|
| `pass/first_model_source_rechecked` | All required candidate pages fetched and contained the expected snippets. | [[LLM/Study/Local LLM First Run Command Plan Runner]] |
| `hold/first_model_source_incomplete` | A required source page could not be fetched, the check date is missing, or expected snippets are not declared. | [[LLM/Study/Local LLM First Model Candidate Ladder]] |
| `fail/first_model_source_contradicted` | A fetched required source page is missing an expected tag, digest, size, context, modality, or quantization snippet. | Refresh the candidate ladder before any pull |

## Copy Row

| Field | Value |
|---|---|
| Source recheck status | pass / hold / fail |
| Source recheck output |  |
| Baseline model id |  |
| Baseline source URL |  |
| Baseline digest/size/context |  |
| Fallback model id |  |
| Text-only control id |  |
| Missing snippet |  |
| Next route |  |

## Completion Gate

This source recheck counts only when:

- [ ] every required candidate has `model_id`, `source_url`, `source_checked_at`, and `expected_snippets`
- [ ] baseline and fallback candidates both pass or the hold row names the replacement policy
- [ ] the source recheck JSON is linked from the command plan, pull gate, or endpoint run sheet
- [ ] no model pull starts from a source page that failed or changed unexpectedly
- [ ] later `ollama show` or `/api/show` evidence confirms the pulled local artifact, because source-page proof alone is not local custody proof

## References

Internal routes:

- [[LLM/Study/Local LLM First Model Candidate Ladder]]
- [[LLM/Study/Local LLM First Run Command Plan Runner]]
- [[LLM/Study/Local LLM First Model Pull Gate]]
- [[LLM/Study/Local LLM First Model Pull Runner]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Runtime Compatibility Runner]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]

External/current sources checked 2026-06-16:

- [Ollama qwen3.5 tags](https://ollama.com/library/qwen3.5/tags)
- [Ollama qwen3.5:4b model page](https://ollama.com/library/qwen3.5:4b)
- [Ollama qwen3.5:2b model page](https://ollama.com/library/qwen3.5:2b)
- [Ollama qwen3:4b-instruct model page](https://ollama.com/library/qwen3:4b-instruct)
- [Ollama qwen3 tags](https://ollama.com/library/qwen3/tags)
