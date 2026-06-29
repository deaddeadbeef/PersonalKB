---
type: ops-report
tags: [llm-wiki, second-brain, strategy, audit]
up: "[[log]]"
confidence: verified
---
# LLM Wiki and Second Brain Strategy

Generated: 2026-06-29

## Summary

Karpathy's LLM Wiki pattern is not "chat with a folder" and not ordinary RAG. It is a compiled knowledge system: raw sources stay as evidence, an LLM maintains a persistent interlinked Markdown wiki, and the human steers source choice, questions, emphasis, and review.

Second Brain practice adds the user-facing purpose: the system should help you find, connect, and use knowledge for live projects and long-running areas of responsibility. For this vault, that means PersonalKB should not become a static encyclopedia. It should become a maintained working memory for learning, operations, research, and decisions.

## What Karpathy Means By LLM Wiki

Karpathy's core distinction is accumulation. In normal RAG, the model retrieves chunks and reconstructs an answer each time. In the LLM Wiki pattern, the agent reads sources, extracts stable claims, updates wiki pages, links concepts, flags contradictions, refreshes indexes, and logs the pass. The output is a persistent artifact that compounds.

The architecture has three useful layers:

| Layer | Meaning | PersonalKB fit |
| --- | --- | --- |
| Raw sources | Immutable source of truth | Domain `_raw/` folders already match this. |
| Wiki | LLM-maintained Markdown synthesis | Domain folders outside underscore directories already match this. |
| Schema | Agent instructions and workflows | `AGENTS.md`, `_ops/`, `index.md`, and `log.md` already match this. |

Operationally, Karpathy names three loops:

| Loop | Role in this vault |
| --- | --- |
| Ingest | Add a source, extract evidence, update relevant wiki pages, index, and log. |
| Query | Answer from the wiki, then file durable answers back when they improve the knowledge base. |
| Lint | Find broken links, missing references, stale claims, weak coverage, orphan pages, and contradictions. |

## What Second Brain Adds

The Second Brain idea is broader than an LLM-maintained wiki. Forte's framing is about reducing information friction so saved material can support work and life outcomes. PARA is the common organizing lens: projects, areas, resources, and archives. The most relevant principle for this vault is not that every folder must be reorganized into PARA. It is that information should be organized by actionability.

For PersonalKB, the practical merge is:

- Use the LLM Wiki pattern for evidence, compilation, cross-linking, and audit trails.
- Use Second Brain practice to decide what gets maintained first: active projects, durable areas, high-value resources, then archives.
- Keep Obsidian as the reading and navigation frontend.
- Keep Git as the audit and rollback layer.

## Current Vault Fit

This vault is already much closer to Karpathy's pattern than a blank setup:

- Root `AGENTS.md` already defines roles, layer model, operations, confidence values, protected paths, and logging.
- `index.md` is generated and content-oriented, matching the "read index first" query route.
- `log.md` is chronological and parseable.
- `_ops/personal_kb.py` already supports `audit`, `index`, and `init-log`.
- The LLM domain already has a large source index, raw sources, chunks, study pages, and local LLM proof artifacts.
- `PersonalKB Wiki Quality Dashboard.md` already separates reader-facing quality from raw/chunk/template noise.

The main gap is not architecture. The main gap is operating discipline at scale:

- Reader-facing broken links still interrupt navigation.
- Many high-value wiki pages still need references and confidence metadata.
- LLM pages still contain placeholder source-coverage text.
- There is no explicit "error book" or contradiction ledger for claims that need later repair.
- Current-source domains need a repeatable source-recheck path before claims are refreshed.

## Recommended Direction

### Phase 1: Stabilize Navigation And Provenance

Run small, reviewable maintenance passes that make the existing wiki trustworthy before adding large new domains.

Acceptance target:

- Reader-facing broken links trend down each pass.
- Top LLM placeholder hits are removed or converted into explicit evidence gaps.
- High-traffic pages have `confidence`, `up`, and `## References`.
- Every pass updates `log.md` and runs `_ops/personal_kb.py audit`.

### Phase 2: Make LLM The Flagship Compounding Domain

Use the LLM folder as the first mature second-brain domain because it already has raw/chunk evidence, current-source needs, local proof artifacts, and active learning workflows.

Next useful slice:

1. Select up to 10 high-traffic LLM pages from the book spine, study index, and quality dashboard.
2. For each page, remove visible placeholder text, add references from `LLM/Sources/Sources Index.md`, and mark unresolved source gaps explicitly.
3. Update the relevant MOC or study index only when navigation changes.
4. Run audit and compare reader-facing counts.

### Phase 3: Add A Query-To-Wiki Habit

When a question produces a durable synthesis, file it back as one of:

- A wiki article, when it is a stable concept or reference page.
- A `_queries/` note, when it is a reusable question, comparison, or coverage map.
- An `_ops/reports/` note, when it is a maintenance decision, audit, or operating plan.

This prevents good answers from disappearing into chat history.

### Phase 4: Add A Contradiction And Staleness Ledger

Add a lightweight report or query note for:

- claim
- page
- source backing
- conflict or staleness trigger
- recommended repair
- last checked date

This is the missing piece that turns "wiki maintenance" into reliable long-term memory.

### Phase 5: Add Better Search Only After The Index Strains

Do not add embedding infrastructure yet. The generated index and `rg` are still enough for current operation. Reconsider a local Markdown search tool when query work repeatedly fails because the index is too large or too shallow.

## Operating Rules Going Forward

- Keep raw sources immutable unless the task is explicitly ingesting new material.
- Prefer one coherent domain pass at a time.
- Make the agent cite vault evidence before changing factual wiki claims.
- Use current web checks for LLM, SpaceX, and other fast-moving domains.
- File durable query answers back into the vault.
- Treat audit deltas as the scoreboard for maintenance quality.
- Commit coherent checkpoints, not tiny mechanical edits.

## Immediate Next Action

Run a narrow LLM cleanup pass:

Scope:

- Up to 10 LLM reader-facing pages.
- Start from the top placeholder hits in `PersonalKB Wiki Quality Dashboard.md`.
- Do not ingest new LLM sources in that pass unless a claim requires current verification.

Verifier:

- `python _ops\personal_kb.py audit`
- `git diff --check`
- Manual review of changed pages for frontmatter, references, internal links, and explicit gaps.

Expected result:

- Fewer reader-facing placeholder hits.
- No increase in reader-facing broken links.
- Clearer provenance on the edited LLM pages.

## Sources Checked

- [Karpathy, "LLM Wiki" gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [Forte Labs, "The PARA Method"](https://fortelabs.com/blog/para/)
- [Building a Second Brain](https://www.buildingasecondbrain.com/)

## References

- [[AGENTS]]
- [[index|PersonalKB Index]]
- [[log|PersonalKB Maintenance Log]]
- [[PersonalKB Wiki Quality Dashboard]]
- [[LLM/LLM]]
- [[LLM/Sources/Sources Index]]
