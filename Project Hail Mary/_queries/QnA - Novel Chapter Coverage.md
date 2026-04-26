---
tags:
  - phm
  - query
  - novel
up: "[[QnA System Roadmap]]"
---
# QnA — Novel Chapter Coverage

## Purpose

Track which chapters of *Project Hail Mary* have been processed into chapter notes, what timeline each belongs to, and how many chunks have been extracted. Use this to find gaps in coverage and prioritize remaining work.

## Dataview Query (Optional)

> [!info] Requires the Dataview plugin. If not installed, use the manual search below.

**All chapter notes with status and source mode:**

```dataview
TABLE chapter, timeline, status, source_mode, chunk_count
FROM "Project Hail Mary/Novel"
WHERE type = "novel-chapter"
SORT chapter ASC
```

**Secondary-mode chapters (bootstrap layer, direct quotes pending):**

```dataview
TABLE chapter, timeline, quotes_pending
FROM "Project Hail Mary/Novel"
WHERE type = "novel-chapter" AND source_mode = "secondary"
SORT chapter ASC
```

**Unprocessed chapters only:**

```dataview
TABLE chapter, timeline, source_mode
FROM "Project Hail Mary/Novel"
WHERE type = "novel-chapter" AND status = "unprocessed"
SORT chapter ASC
```

**Chapters by timeline:**

```dataview
TABLE chapter, status, source_mode, chunk_count
FROM "Project Hail Mary/Novel"
WHERE type = "novel-chapter" AND timeline = "present"
SORT chapter ASC
```

## Manual Search Fallback

Use Obsidian's built-in search (`Ctrl+Shift+F`):

**All chapter notes:**
```
path:"Project Hail Mary/Novel" tag:#chapter
```

**Find unprocessed chapters:**
```
path:"Project Hail Mary/Novel" status: unprocessed
```

**Find secondary-mode chapters:**
```
path:"Project Hail Mary/Novel" source_mode: secondary
```

**Find chapters with quotes pending:**
```
path:"Project Hail Mary/Novel" quotes_pending: true
```

**Find chapters by timeline:**
```
path:"Project Hail Mary/Novel" timeline: flashback
```

**Check chunk counts:**
```
path:"Project Hail Mary/Novel" chunk_count
```

## Status Values

| Status | Meaning |
|---|---|
| `unprocessed` | Chapter note created but not yet summarized |
| `secondary-only` | Bootstrapped from public secondary sources; no primary-source verification yet; `quotes_pending: true` |
| `processed` | Summary complete (at current source mode) |
| `fully-chunked` | All chunk candidates extracted into `_chunks/` |

## Source Mode Values

| `source_mode` | Meaning |
|---|---|
| `secondary` | Note built from public secondary summaries; no legally owned copy used; direct quotes blocked |
| `primary` | Note built from a legally owned copy of the novel; direct quotes permitted (fair use, max 3 per chapter) |

> **Note:** `secondary-only` is a **`status`** value (see Status Values table above), not a `source_mode` value. Do not set `source_mode: secondary-only` — the correct field value is `source_mode: secondary`. Use `status: secondary-only` when a chapter note has never had any primary-source verification.

> Notes created during the hybrid bootstrap (secondary mode) have `quotes_pending: true`. This field should be cleared only after primary-mode verification replaces the placeholder.

## Source Mode Guidance

The chapter layer can be populated in two distinct modes:

**Primary mode (current state):** Chapter notes have been verified against a legally owned copy of the novel. Summaries are primary-source synthesis, direct quotes are included under fair use (1–2 sentences, max 3 per chapter), `source_mode` is `primary`, and `quotes_pending` is cleared. See [[Novel Ingestion Guide]] for the full workflow.

**Secondary mode (original bootstrap):** Chapter notes were initially created using public/legal secondary sources (plot summaries, Wikipedia, book-review sites). This mode was the scaffolding layer during initial vault construction. Most chapter notes have since been upgraded to primary mode. See [[PHM Chapter Summaries - Secondary Sources Registry]] for the registered secondary sources that informed the bootstrap layer.

## Notes

- Chapter notes live in `Project Hail Mary/Novel/` with filenames like `PHM Novel - Chapter 01.md`.
- The [[Chapter Index]] is the browsable MOC; this query note is for systematic coverage checks.
- Bootstrap-layer notes (secondary mode) were intentional scaffolding that has since been upgraded to primary mode for all chapters.