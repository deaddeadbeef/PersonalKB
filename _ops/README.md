# PersonalKB Operations

This folder contains repeatable maintenance tooling and generated reports for the vault.

Use `_ops/reports/` for audit outputs. Reports are allowed to be regenerated and committed when they document a maintenance checkpoint.

## Commands

- `python _ops/personal_kb.py audit` regenerates vault health reports.
- `python _ops/personal_kb.py index` regenerates `index.md`.
- `python _ops/personal_kb_monitor.py` writes daemon health summaries to `_ops/reports/monitor-summary.md` and `_ops/reports/monitor-summary.json`.
- `python _ops/personal_kb_monitor.py --run-audit` refreshes audit reports first, then writes monitor summaries.
- `python _ops/personal_kb_monitor.py --strict` returns non-zero when the monitor status is `attention` or `blocked`.
