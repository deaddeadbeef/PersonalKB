---
tags: [study, llm, inference, local-llm, windows, storage, cache, runner, python, evidence]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-16
---

# Local LLM Model Store Bootstrap Runner

> **One-line summary** This runner turns the model-store decision into a controlled, evidence-producing bootstrap step: plan or create the run folder, model directories, and user cache variables before the first runtime install or model pull.

Use this after [[LLM/Study/Local LLM Model Store Readiness Snapshot|Local LLM Model Store Readiness Snapshot]] and [[LLM/Study/Local LLM First Run Readiness Runner|Local LLM First Run Readiness Runner]] report that storage paths or cache variables are the lowest unproven layer. Use it before [[LLM/Study/Local LLM Windows Runtime Install Gate|Local LLM Windows Runtime Install Gate]], [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]], or [[LLM/Study/Local LLM Windows First-Run Quickstart|Local LLM Windows First-Run Quickstart]].

The default mode is dry run. It does **not** install Ollama or LM Studio, download a model, launch a listener, delete files, or send a prompt. In `--apply` mode it can create the named directories and set user-level environment variables, but only when the manifest contains the confirmation string.

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| Bootstrap plan | Which folders and variables would change before the first model pull. | That a runtime has inherited the variables. |
| Directory action rows | Whether the run folder, model root, Ollama store, Hub cache, and GGUF directory exist or were created. | That the runtime will accept those paths. |
| User environment action rows | Whether `OLLAMA_MODELS`, `HF_HOME`, and `HF_HUB_CACHE` are already correct or were set for future shells. | That the current shell or a running service sees the new values. |
| Disk checks | Whether the target drive appears to have enough free space before creating stores. | Exact final download size, duplicate cache risk, or model fit. |
| Safety checks | Whether the requested paths look like narrow model/run folders rather than drive roots or system directories. | A full security review of endpoint exposure or private data boundaries. |

## Runner Manifest

Use a manifest like this for the planned first local setup:

```json
{
  "run_id": "first-local-llm-model-store-bootstrap",
  "run_root": "C:/Users/fpan1/Documents/local-llm-runs/2026-06-16-model-store-bootstrap",
  "output_root": "C:/Users/fpan1/Documents/local-llm-runs/2026-06-16-model-store-bootstrap",
  "model_root": "D:/Models",
  "ollama_models_path": "D:/Models/ollama",
  "hf_home": "D:/Models/hf",
  "hf_hub_cache": "D:/Models/hf/hub",
  "gguf_dir": "D:/Models/gguf",
  "minimum_free_gb": 20,
  "set_user_env": true,
  "confirm_apply": "create-model-store-and-user-env"
}
```

Dry run first:

```powershell
python .\local_llm_model_store_bootstrap_runner.py .\model-store-bootstrap-manifest.json
```

Apply only after reviewing the dry-run plan:

```powershell
python .\local_llm_model_store_bootstrap_runner.py .\model-store-bootstrap-manifest.json --apply
```

After apply, open a new PowerShell and rerun [[LLM/Study/Local LLM First Run Readiness Runner|Local LLM First Run Readiness Runner]]. The old shell may not inherit user environment changes.

## Standard-Library Runner

Save this as `local_llm_model_store_bootstrap_runner.py` inside the run folder. It uses only Python's standard library.

```python
from __future__ import annotations

import csv
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


CONFIRM = "create-model-store-and-user-env"
ENV_TARGETS = {
    "OLLAMA_MODELS": "ollama_models_path",
    "HF_HOME": "hf_home",
    "HF_HUB_CACHE": "hf_hub_cache",
}
PATH_KEYS = ["run_root", "model_root", "ollama_models_path", "hf_home", "hf_hub_cache", "gguf_dir"]
SYSTEM_NAMES = {"windows", "program files", "program files (x86)", "programdata"}


def now_iso() -> str:
    return dt.datetime.now().isoformat(timespec="seconds")


def text(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def as_bool(value: Any, default: bool = False) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def number(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def norm_path(value: str) -> Path:
    return Path(value).expanduser()


def ps_json(script: str, timeout: int = 15) -> tuple[str, Any]:
    exe = shutil.which("powershell") or shutil.which("pwsh")
    if not exe:
        return "skipped:no_powershell", None
    try:
        proc = subprocess.run(
            [exe, "-NoProfile", "-Command", script],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except Exception as exc:
        return f"error:{type(exc).__name__}:{exc}", None
    output = proc.stdout.strip()
    if proc.returncode != 0:
        return f"error:returncode_{proc.returncode}:{proc.stderr.strip()}", None
    if not output:
        return "ok", None
    try:
        return "ok", json.loads(output)
    except json.JSONDecodeError:
        return "error:json_decode", output


def read_user_env() -> dict[str, dict[str, str]]:
    result = {name: {"process": os.environ.get(name, ""), "user": ""} for name in ENV_TARGETS}
    if os.name != "nt":
        return result
    parts = []
    for name in ENV_TARGETS:
        parts.append(f"{name}=[Environment]::GetEnvironmentVariable('{name}','User')")
    status, data = ps_json("[pscustomobject]@{" + ";".join(parts) + "} | ConvertTo-Json -Compress")
    if status == "ok" and isinstance(data, dict):
        for name in ENV_TARGETS:
            result[name]["user"] = text(data.get(name))
    else:
        result["_user_env_status"] = {"process": status, "user": ""}
    return result


def set_user_env(name: str, value: str) -> str:
    escaped_name = name.replace("'", "''")
    escaped_value = value.replace("'", "''")
    script = f"[Environment]::SetEnvironmentVariable('{escaped_name}','{escaped_value}','User')"
    status, _ = ps_json(script)
    return status


def nearest_existing(path: Path) -> Path:
    current = path
    while not current.exists() and current.parent != current:
        current = current.parent
    return current


def disk_for(path: Path) -> dict[str, Any]:
    root = nearest_existing(path)
    try:
        usage = shutil.disk_usage(str(root))
    except Exception as exc:
        return {"path": str(path), "nearest_existing": str(root), "available": False, "error": str(exc)}
    return {
        "path": str(path),
        "nearest_existing": str(root),
        "available": True,
        "free_gb": round(usage.free / (1024**3), 1),
        "total_gb": round(usage.total / (1024**3), 1),
    }


def path_values(manifest: dict[str, Any]) -> dict[str, str]:
    values: dict[str, str] = {}
    for key in PATH_KEYS:
        value = text(manifest.get(key))
        if value:
            values[key] = value
    return values


def path_record(key: str, raw: str) -> dict[str, Any]:
    path = norm_path(raw)
    return {
        "key": key,
        "path": str(path),
        "exists": path.exists(),
        "is_dir": path.is_dir(),
        "anchor": path.anchor,
        "parts": list(path.parts),
    }


def dangerous_path_reason(path: Path) -> str:
    raw = str(path)
    if not raw:
        return "empty path"
    if path.parent == path:
        return "filesystem root"
    if path.anchor and raw.rstrip("\\/").lower() == path.anchor.rstrip("\\/").lower():
        return "drive root"
    try:
        home = Path.home().resolve()
        resolved = path.resolve(strict=False)
        if resolved == home or resolved == home.parent:
            return "home or user root"
    except Exception:
        pass
    parts = [part.lower().strip("\\/") for part in path.parts]
    if len(parts) <= 1:
        return "too broad"
    if any(part in SYSTEM_NAMES for part in parts):
        return "system directory"
    return ""


def build_plan(manifest: dict[str, Any], apply_mode: bool) -> dict[str, Any]:
    values = path_values(manifest)
    paths = [path_record(key, value) for key, value in values.items()]
    env = read_user_env()
    minimum_free_gb = number(manifest.get("minimum_free_gb"), 20)
    set_env = as_bool(manifest.get("set_user_env"), True)

    actions: list[dict[str, Any]] = []
    findings: list[dict[str, str]] = []

    for row in paths:
        path = norm_path(row["path"])
        reason = dangerous_path_reason(path)
        if reason:
            findings.append(
                {
                    "level": "fail",
                    "owner": row["key"],
                    "finding": "Refusing broad or unsafe path.",
                    "evidence": f"{row['path']} ({reason})",
                    "action": "Use a narrow run or model-store directory.",
                }
            )
            continue
        disk = disk_for(path)
        if disk.get("available") and number(disk.get("free_gb")) < minimum_free_gb:
            findings.append(
                {
                    "level": "hold",
                    "owner": "disk",
                    "finding": "Target path is on a drive below the configured free-space threshold.",
                    "evidence": f"{row['path']} free_gb={disk.get('free_gb')}",
                    "action": "Free space, lower the threshold with justification, or choose another drive.",
                }
            )
        if row["exists"] and not row["is_dir"]:
            findings.append(
                {
                    "level": "fail",
                    "owner": row["key"],
                    "finding": "Path exists but is not a directory.",
                    "evidence": row["path"],
                    "action": "Choose a directory path or remove the conflicting file manually.",
                }
            )
        elif not row["exists"]:
            actions.append({"type": "create_dir", "key": row["key"], "path": row["path"], "status": "planned"})
        else:
            actions.append({"type": "create_dir", "key": row["key"], "path": row["path"], "status": "already_exists"})

    if set_env:
        for env_name, manifest_key in ENV_TARGETS.items():
            desired = text(manifest.get(manifest_key))
            if not desired:
                continue
            current = text(env.get(env_name, {}).get("user"))
            if current.lower() == desired.lower():
                actions.append({"type": "set_user_env", "name": env_name, "value": desired, "status": "already_set"})
            elif current:
                actions.append({"type": "set_user_env", "name": env_name, "value": desired, "previous": current, "status": "planned_replace"})
            else:
                actions.append({"type": "set_user_env", "name": env_name, "value": desired, "status": "planned"})

    if apply_mode and text(manifest.get("confirm_apply")) != CONFIRM:
        findings.append(
            {
                "level": "fail",
                "owner": "manifest",
                "finding": "Apply mode requires an explicit confirmation string.",
                "evidence": "confirm_apply missing or different",
                "action": f"Set confirm_apply to {CONFIRM!r} after reviewing the dry-run plan.",
            }
        )

    return {
        "apply_mode": apply_mode,
        "paths": paths,
        "environment_before": env,
        "disk": [disk_for(norm_path(value)) for value in values.values()],
        "actions": actions,
        "findings": findings,
    }


def apply_plan(plan: dict[str, Any]) -> None:
    for action in plan["actions"]:
        if action["status"] in {"already_exists", "already_set"}:
            continue
        if action["type"] == "create_dir":
            try:
                Path(action["path"]).mkdir(parents=True, exist_ok=True)
                action["status"] = "applied"
            except Exception as exc:
                action["status"] = "error"
                action["error"] = f"{type(exc).__name__}:{exc}"
        elif action["type"] == "set_user_env":
            status = set_user_env(action["name"], action["value"])
            action["status"] = "applied" if status == "ok" else "error"
            if status != "ok":
                action["error"] = status


def classify(plan: dict[str, Any]) -> dict[str, Any]:
    findings = list(plan.get("findings", []))
    actions = plan.get("actions", [])
    if any(action.get("status") == "error" for action in actions):
        for action in actions:
            if action.get("status") == "error":
                findings.append(
                    {
                        "level": "fail",
                        "owner": action.get("type", "action"),
                        "finding": "Bootstrap action failed.",
                        "evidence": action.get("error", ""),
                        "action": "Fix the failed action before installing or pulling a model.",
                    }
                )
    if any(item["level"] == "fail" for item in findings):
        status, reason = "fail", "bootstrap_blocked"
    elif any(item["level"] == "hold" for item in findings):
        status, reason = "hold", "bootstrap_incomplete"
    elif not plan.get("apply_mode") and any(action.get("status", "").startswith("planned") for action in actions):
        status, reason = "hold", "bootstrap_pending"
        findings.append(
            {
                "level": "hold",
                "owner": "apply",
                "finding": "Dry run found pending model-store bootstrap actions.",
                "evidence": f"{sum(1 for action in actions if action.get('status', '').startswith('planned'))} planned actions",
                "action": "Review the plan, then rerun with --apply if the paths and env variables are correct.",
            }
        )
    else:
        status, reason = "pass", "bootstrap_ready_for_new_shell_check"
    return {"status": status, "reason": reason, "findings": findings}


def output_paths(manifest: dict[str, Any], result: dict[str, Any]) -> dict[str, Path]:
    root = Path(text(manifest.get("output_root") or manifest.get("run_root") or ".")).expanduser()
    run_id = result["run_id"]
    return {
        "json": root / f"{run_id}-model-store-bootstrap.json",
        "csv": root / f"{run_id}-model-store-bootstrap-actions.csv",
        "md": root / f"{run_id}-model-store-bootstrap.md",
        "jsonl": root / "local-llm-model-store-bootstrap-runs.jsonl",
    }


def md_cell(value: Any) -> str:
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True)
    return text(value).replace("|", "\\|").replace("\n", " ")


def write_outputs(manifest: dict[str, Any], result: dict[str, Any]) -> dict[str, str]:
    paths = output_paths(manifest, result)
    for path in paths.values():
        path.parent.mkdir(parents=True, exist_ok=True)
    paths["json"].write_text(json.dumps(result, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    fields = ["type", "key", "name", "path", "value", "previous", "status", "error"]
    with paths["csv"].open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for action in result["plan"]["actions"]:
            writer.writerow({field: action.get(field, "") for field in fields})
    lines = [
        f"# Local LLM Model Store Bootstrap - {result['run_id']}",
        "",
        f"- Decision: `{result['decision']['status']}` / `{result['decision']['reason']}`",
        f"- Generated: {result['generated_at']}",
        f"- Apply mode: `{str(result['plan']['apply_mode']).lower()}`",
        "",
        "## Actions",
        "",
        "| Type | Target | Value | Status |",
        "|---|---|---|---|",
    ]
    for action in result["plan"]["actions"]:
        target = action.get("path") or action.get("name") or action.get("key")
        value = action.get("value") or action.get("previous") or ""
        lines.append(f"| {md_cell(action.get('type'))} | {md_cell(target)} | {md_cell(value)} | {md_cell(action.get('status'))} |")
    lines.extend(["", "## Findings", "", "| Level | Owner | Finding | Evidence | Action |", "|---|---|---|---|---|"])
    if result["decision"]["findings"]:
        for row in result["decision"]["findings"]:
            lines.append(f"| {md_cell(row['level'])} | {md_cell(row['owner'])} | {md_cell(row['finding'])} | {md_cell(row['evidence'])} | {md_cell(row['action'])} |")
    else:
        lines.append("| pass | bootstrap | No blocking findings. | plan | Open a new shell and rerun readiness evidence. |")
    paths["md"].write_text("\n".join(lines) + "\n", encoding="utf-8")
    with paths["jsonl"].open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(result, ensure_ascii=True) + "\n")
    return {key: str(path) for key, path in paths.items()}


def run(manifest: dict[str, Any], apply_mode: bool) -> dict[str, Any]:
    plan = build_plan(manifest, apply_mode)
    if apply_mode and not any(item["level"] == "fail" for item in plan["findings"]):
        apply_plan(plan)
        plan["environment_after"] = read_user_env()
        plan["paths_after"] = [path_record(row["key"], row["path"]) for row in plan["paths"]]
    decision = classify(plan)
    result = {
        "run_id": text(manifest.get("run_id")) or "local-llm-model-store-bootstrap",
        "generated_at": now_iso(),
        "manifest": manifest,
        "plan": plan,
        "decision": decision,
    }
    result["outputs"] = write_outputs(manifest, result)
    return result


def run_self_tests() -> None:
    base = {
        "run_id": "test",
        "run_root": "C:/Users/fpan1/Documents/local-llm-runs/test",
        "output_root": "C:/Users/fpan1/Documents/local-llm-runs/test",
        "model_root": "D:/Models",
        "ollama_models_path": "D:/Models/ollama",
        "hf_home": "D:/Models/hf",
        "hf_hub_cache": "D:/Models/hf/hub",
        "gguf_dir": "D:/Models/gguf",
        "minimum_free_gb": 1,
        "set_user_env": True,
    }
    cases = []
    plan = {
        "apply_mode": False,
        "actions": [{"type": "create_dir", "path": "D:/Models", "status": "planned"}],
        "findings": [],
    }
    cases.append(("dry run pending", plan, "hold"))
    cases.append(("dangerous root", {"apply_mode": False, "actions": [], "findings": [{"level": "fail", "owner": "model_root", "finding": "bad", "evidence": "D:/", "action": "fix"}]}, "fail"))
    cases.append(("already ready", {"apply_mode": False, "actions": [{"type": "create_dir", "path": "D:/Models", "status": "already_exists"}], "findings": []}, "pass"))
    blocked_apply = build_plan({**base, "model_root": "D:/"}, apply_mode=True)
    cases.append(("apply unsafe", blocked_apply, "fail"))
    failures = []
    for name, case_plan, expected in cases:
        got = classify(case_plan)["status"]
        if got != expected:
            failures.append({"case": name, "expected": expected, "got": got})
    if failures:
        print(json.dumps({"self_test": "fail", "failures": failures}, indent=2))
        raise SystemExit(1)
    print(json.dumps({"self_test": "pass", "cases": len(cases)}, indent=2))


def load_manifest(argv: list[str]) -> dict[str, Any]:
    manifest_path = os.environ.get("LOCAL_LLM_MODEL_STORE_BOOTSTRAP_MANIFEST")
    positional = [arg for arg in argv[1:] if not arg.startswith("-")]
    if not manifest_path and positional:
        manifest_path = positional[0]
    if not manifest_path:
        raise SystemExit("Set LOCAL_LLM_MODEL_STORE_BOOTSTRAP_MANIFEST or pass a manifest JSON path.")
    with Path(manifest_path).open("r", encoding="utf-8") as handle:
        manifest = json.load(handle)
    if not isinstance(manifest, dict):
        raise SystemExit("Manifest root must be a JSON object.")
    return manifest


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        run_self_tests()
        return 0
    manifest = load_manifest(argv)
    result = run(manifest, apply_mode="--apply" in argv)
    print(json.dumps(result, indent=2, ensure_ascii=True))
    status = result["decision"]["status"]
    return 0 if status == "pass" else 2 if status == "hold" else 3


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
```

## Decision Meanings

| Decision | Meaning | Next route |
|---|---|---|
| `pass/bootstrap_ready_for_new_shell_check` | There are no blocked paths and all requested actions are either already true or were applied. | Open a new PowerShell, rerun [[LLM/Study/Local LLM First Run Readiness Runner]], then continue to [[LLM/Study/Local LLM Windows Runtime Install Gate]]. |
| `hold/bootstrap_pending` | Dry run found planned directory or environment changes. | Review the plan, then rerun with `--apply` if the paths are correct. |
| `hold/bootstrap_incomplete` | A disk or precondition hold remains. | Fix the named storage issue before runtime install or model pull. |
| `fail/bootstrap_blocked` | A requested path or apply condition is unsafe, too broad, conflicting, or failed. | Stop and fix the manifest or machine state before changing anything. |

## Completion Gate

This bootstrap step is complete when:

- [ ] a dated manifest exists
- [ ] dry-run JSON, CSV, Markdown, and JSONL outputs exist
- [ ] any `--apply` run used the confirmation string
- [ ] the run folder and model-store directories exist, or the plan says why they should not
- [ ] `OLLAMA_MODELS`, `HF_HOME`, and `HF_HUB_CACHE` are either intentionally unset or set to the selected model store paths
- [ ] a new PowerShell verifies the user environment
- [ ] [[LLM/Study/Local LLM First Run Readiness Runner|Local LLM First Run Readiness Runner]] is rerun after bootstrap

## References

Internal routes:

- [[LLM/Study/Local LLM Windows Model Store and Cache Plan]]
- [[LLM/Study/Local LLM Model Store Readiness Snapshot]]
- [[LLM/Study/Local LLM First Run Readiness Runner]]
- [[LLM/Study/Local LLM Windows Runtime Install Gate]]
- [[LLM/Study/Local LLM First Model Pull Gate]]
- [[LLM/Study/Local LLM Windows First-Run Quickstart]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
