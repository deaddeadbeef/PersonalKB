---
tags:
  - phm
  - system
  - qna
up: "[[Project Hail Mary]]"
---
# QnA System Roadmap

This note outlines the phased plan for building a question-and-answer retrieval system on top of the [[Project Hail Mary]] knowledge base.

---

## Design Principles

- **Human-readable first.** Every raw note, chunk, and query should be useful as a standalone Obsidian note, even with zero plugins installed.
- **Structured enough for automation.** YAML frontmatter fields (`type`, `topic`, `claim`, `confidence`, `supports`) enable future machine-readable queries.
- **Progressive enhancement.** Each phase adds capability without breaking the previous one.

---

## Phase 1 — Manual Search with Chunk Metadata (Current)

**Status:** Active

What exists now:
- `_raw/` notes capture source material with structured frontmatter and chunk-candidate checklists.
- `_chunks/` notes isolate single claims with `claim`, `confidence`, `topic`, and `supports` fields plus QnA seed questions.
- `_queries/` notes provide pre-built search patterns using Obsidian's native search.

**How to use it:**
1. Open Obsidian search (`Ctrl+Shift+F`).
2. Use path and tag filters: `path:"Project Hail Mary/_chunks" tag:#propulsion`
3. Browse the `claim` field in YAML to find specific facts.
4. Follow `supports` links to reach the relevant wiki notes.
5. Use the query notes in `_queries/` for common lookup patterns.

---

## Phase 1.5 — Novel Ingestion Pipeline (Next)

**Status:** Scaffolded — awaiting source file

The novel itself is the foundational source for this entire KB but has not yet been ingested at chapter level. A legal-ingestion scaffold is in place:

- **Raw registration:** [[Weir 2021 - Project Hail Mary Novel]] tracks the source file status.
- **Chapter Index:** [[Chapter Index]] provides a MOC with unresolved links for all 30 chapters + epilogue.
- **Template:** [[Chapter Summary Template]] enforces original summaries, short fair-use quotes, and science annotations per chapter.
- **Processing guide:** [[Novel Ingestion Guide]] documents the full workflow, compliance rules, and format-specific extraction steps.
- **Coverage query:** [[QnA - Novel Chapter Coverage]] tracks ingestion progress.

Chapter summaries and novel-derived chunks will feed into the same retrieval pipeline as existing `_raw/` → `_chunks/` evidence. Once chapters are processed, their chunks appear in all existing query notes automatically.

**Blocker:** No legally owned DRM-free digital copy has been located yet. The external staging folder (`D:\Sources\ProjectHailMary\`) is ready.

---

## Phase 2 — Dataview Structured Queries (Next)

**Status:** Planned — requires the [Dataview](https://github.com/blacksmithgu/obsidian-dataview) plugin.

What this adds:
- Live, auto-updating tables and lists generated from chunk frontmatter.
- Filter by topic, confidence level, source, or any combination.
- Cross-reference which raw materials have been fully chunked vs. which still need processing.

**Prerequisite:** Install the Dataview community plugin. No vault restructuring needed — the current frontmatter schema is already Dataview-compatible.

The query notes in `_queries/` already contain example Dataview blocks that will activate once the plugin is installed.

---

## Phase 3 — Semantic Search and RAG (Future)

**Status:** Aspirational

Options to explore:
- **Smart Connections plugin** — uses local embeddings to find semantically similar notes. Low setup cost.
- **Obsidian Copilot / local LLM** — chat interface that can answer questions using vault content as context.
- **External RAG pipeline** — export chunks (using frontmatter as structured metadata) into a vector database, query with a local LLM.

The chunk structure is designed to support this: each chunk's `claim` field is a complete standalone sentence suitable for embedding, and the `source` / `supports` fields provide provenance for any generated answer.

**No action needed now.** The current schema will work as input for any of these approaches without restructuring.

---

## Chunk Schema Reference

For template details see [[Chunk Template]].

| Field | Purpose | Example |
|---|---|---|
| `id` | Unique identifier | `chunk-prop-001` |
| `type` | Always `chunk` | `chunk` |
| `source` | Link to raw note | `[[Bailer-Jones 2025 - Physics of Interstellar Travel]]` |
| `source_loc` | Where in the source | `"Section 3.2"` |
| `topic` | Primary topic tag | `Propulsion` |
| `claim` | Standalone sentence | `"Photon rockets require ~300 MW per newton."` |
| `confidence` | Assessment level | `verified` / `plausible` / `fictional` / `policy` / `uncertain` |
| `supports` | Wiki notes this evidences | `["[[The Hail Mary Drive]]"]` |

---

## Related

- [[QnA - All Chunks by Topic]]
- [[QnA - Unprocessed Raw Materials]]
- [[QnA - Fact Check Lookup]]
- [[QnA - Chunk Coverage Map]]
- [[QnA - Novel Chapter Coverage]]
