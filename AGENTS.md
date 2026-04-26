# PersonalKB Agent Schema

This vault follows an LLM-maintained wiki pattern. Raw sources are preserved as evidence, wiki notes are the compiled working layer, and agent operations must leave a clear audit trail.

## Roles

- Human: curates sources, chooses priorities, reviews important claims, and decides which domains should be refreshed.
- Agent: maintains structure, links, indexes, summaries, references, and lint reports.
- Obsidian: serves as the reading and navigation frontend.
- Git: records every meaningful maintenance pass.

## Layer Model

| Layer | Location | Rule |
| --- | --- | --- |
| Raw sources | `*/_raw/` | Read-only unless explicitly ingesting a new source. Do not rewrite existing raw captures during refinement. |
| Chunks | `*/_chunks/` | Atomic evidence notes. Prefer linking existing chunks before inventing new claims. |
| Wiki | Domain folders outside underscore directories | The LLM-maintained article layer. This is where refinement work happens. |
| Queries | `*/_queries/` | Reusable Q&A and coverage maps. Update only when the operation directly affects them. |
| Operations | `_ops/` | Scripts, reports, and maintenance artifacts. |
| Navigation | `index.md`, `log.md`, domain MOCs | Keep these current enough for agents and humans to orient quickly. |

## Global Rules

1. Preserve source provenance. Any non-obvious factual claim in a wiki note should be backed by an existing chunk, raw source, source index entry, or a clearly marked external source.
2. Do not copy long copyrighted text into wiki notes. Summarize, paraphrase, and use only short fair-use excerpts when necessary.
3. Do not silently update time-sensitive claims from memory. For current domains such as LLM and SpaceX, use web verification and cite the source in the note or maintenance log.
4. Do not rewrite a whole article just to change style. Prefer targeted edits that improve correctness, navigation, evidence, or learning value.
5. Maintain YAML frontmatter. Keep `tags`, `up`, `confidence`, and `tier-coverage` when present.
6. Use Obsidian links for internal navigation. Prefer the shortest unambiguous `[[Page Name]]` link, or a path-qualified link when duplicate names exist.
7. Every substantive wiki article should have a references section. Use the domain source index when no more specific source is available.
8. Every maintenance pass should append to `log.md` with date, operation, scope, changed files, and verification command.
9. Keep generated reports in `_ops/reports/`. Do not mix operational reports into topic folders.
10. Commit after coherent checkpoints, not after every tiny mechanical edit.

## Confidence Values

Use this taxonomy consistently:

- `verified`: supported by source material in the vault or a checked current source.
- `plausible`: reasonable synthesis or extrapolation, but not directly proven by a source.
- `fictional`: in-universe or fictional material.
- `policy`: recommendation, process, or strategy rather than factual claim.
- `uncertain`: known gap, conflict, or low-confidence claim.

## Operations

### Ingest

Use when new source material is added.

1. Read the new raw source.
2. Extract atomic chunk candidates where useful.
3. Update or create relevant wiki pages.
4. Update domain MOCs, `index.md`, and `log.md`.
5. Flag contradictions instead of smoothing them over.

### Query

Use when answering a question against the vault.

1. Read `index.md` first.
2. Search domain MOCs and relevant pages.
3. Read chunks/raw sources only as needed for evidence.
4. Answer with links to supporting notes.
5. If the answer is durable, file it back as a wiki note or query note and log it.

### Lint

Use for health checks.

Check for empty notes, stubs, missing frontmatter, missing references, unresolved links, orphan pages, placeholder text, stale claims, and weak source coverage. Write machine-readable reports to `_ops/reports/`.

### Refine

Use for existing wiki notes.

1. Scope the pass to one domain or a small list of files.
2. Read the relevant MOC, article, supporting chunks, and source index.
3. Fix structure and links before prose.
4. Add evidence links and references where the source material exists.
5. Leave factual gaps as explicit gaps when evidence is missing.
6. Run the audit tool after the pass.

## Protected Paths

Do not modify these unless the task explicitly asks for it:

- `.git/`
- `.obsidian/`
- `*/_raw/`
- `*/_chunks/`
- `*/_templates/`
- media files such as `.mp3`, `.jpg`, `.png`

## Pilot Scope

The first auto-refinement pilot is `CS Data Structures`. It is the safest domain because most claims are stable textbook facts and the folder already has raw/chunk evidence. The pilot should touch no more than 10 wiki notes before review.

