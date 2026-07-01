---
type: task-state
tags: [task, stock-trading, wiki-build]
up: "[[Welcome]]"
confidence: policy
---
# Stock Trading Wiki Build Task

## Goal

Create a new `Stock Trading` domain so the vault can relearn how stocks work from first principles before any strategy or live-trading work.

## Scope

- Add a reader-facing MOC, learning path, source index, foundations, market mechanics, account mechanics, analysis, risk process, and review drill.
- Use current official SEC/Investor.gov and FINRA sources for market mechanics, settlement, brokerage accounts, margin, due diligence, and investor-risk claims.
- Keep this as education and paper-study infrastructure, not financial advice or trade recommendations.
- Do not ingest raw copyrighted source captures in this pass.

## Acceptance Criteria

- The new topic has a root MOC linked from `Welcome.md`.
- Every new reader-facing article has YAML frontmatter, `up`, `confidence`, and a `## References` section.
- New internal wikilinks resolve under the vault audit tooling.
- `index.md`, audit reports, and `log.md` are regenerated or deliberately left unchanged with a reason.
- The feature branch is committed, pushed, and opened as a PR.

## Validation Plan

- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- Targeted Stock Trading link and metadata check.
- `git diff --check`

## Status

- 2026-07-01: Task created in isolated worktree `codex/stock-trading-wiki`.
- 2026-07-01: Added 13 Stock Trading wiki notes and linked the topic from `Welcome.md`.
- 2026-07-01: Regenerated `index.md` and audit reports; targeted Stock Trading validation passed.
- 2026-07-01: Diff whitespace checks passed after EOF formatting cleanup.
