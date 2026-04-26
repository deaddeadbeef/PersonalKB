---
tags:
  - csa
  - query
up: "[[CS Algorithms/_queries/QnA System Roadmap|QnA System Roadmap]]"
---
# QnA — Chapter Coverage

## Purpose

Track which chapters of *Algorithms Unlocked* have been processed into chapter notes, their processing status, and how many chunks have been extracted. Use this to find coverage gaps and prioritise remaining work.

## Dataview Query (Optional)

> [!info] Requires the Dataview plugin. If not installed, use the manual search below.

**All chapter notes with status and chunk count:**

```dataview
TABLE chapter, status, chunk_count, book
FROM "CS Algorithms/Books/Algorithms Unlocked/Chapters"
WHERE type = "book-chapter"
SORT chapter ASC
```

**Unprocessed chapters only:**

```dataview
TABLE chapter, book
FROM "CS Algorithms/Books/Algorithms Unlocked/Chapters"
WHERE type = "book-chapter" AND status = "unprocessed"
SORT chapter ASC
```

**Chapters needing more chunks (chunk_count < 3):**

```dataview
TABLE chapter, chunk_count
FROM "CS Algorithms/Books/Algorithms Unlocked/Chapters"
WHERE type = "book-chapter" AND chunk_count < 3
SORT chunk_count ASC
```

## Manual Search Fallback

Use Obsidian's built-in search (`Ctrl+Shift+F`):

**All chapter notes:**
```
path:"CS Algorithms/Books/Algorithms Unlocked/Chapters" tag:#book-chapter
```

**Find unprocessed chapters:**
```
path:"CS Algorithms/Books/Algorithms Unlocked/Chapters" status: unprocessed
```

## Current Coverage

As of initial build:

| Chapter | Status | Chunk Count |
|---------|--------|-------------|
| 01 — What Are Algorithms | processed | 3 |
| 02 — Describe and Evaluate | processed | 5 |
| 03 — Sorting and Searching | processed | 5 |
| 04 — Lower Bound, Counting, Radix | processed | 3 |
| 05 — Directed Acyclic Graphs | processed | 4 |
| 06 — Shortest Paths | processed | 3 |
| 07 — String Algorithms | processed | 4 |
| 08 — Cryptography | processed | 5 |
| 09 — Data Compression | processed | 3 |
| 10 — Hard Problems | processed | 3 |

**Total**: 10/10 chapters processed, 37 unique chunk notes extracted (38 chapter-to-chunk references; the Asymptotic Notation chunk is cited in both Chapter 01 and Chapter 02).

## Notes

- Chapter notes live in `CS Algorithms/Books/Algorithms Unlocked/Chapters/` named `AU - Chapter NN.md`.
- The [[Chapter Index]] is the browsable MOC; this query note provides systematic coverage tracking.
- Update the Current Coverage table manually if Dataview is not installed, or let the Dataview query replace it once the plugin is available.
