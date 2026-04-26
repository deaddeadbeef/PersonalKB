---
tags:
  - phm
  - query
up: "[[QnA System Roadmap]]"
---
# QnA — Unprocessed Raw Materials

## Purpose

Find raw-material notes that have not yet been fully chunked, so you know what still needs processing.

## Dataview Query (Optional)

> [!info] Requires the Dataview plugin. If not installed, use the manual search below.

```dataview
TABLE title, status, chunk_count
FROM "Project Hail Mary/_raw"
WHERE status != "fully-chunked"
SORT status ASC
```

## Manual Search Fallback

Use Obsidian's built-in search (`Ctrl+Shift+F`):

**All raw notes:**
```
path:"Project Hail Mary/_raw"
```

**Find unprocessed or partially processed:**
```
path:"Project Hail Mary/_raw" status: unprocessed
```
```
path:"Project Hail Mary/_raw" status: partial
```

## Status Values

| Status | Meaning |
|---|---|
| `unprocessed` | No chunks extracted yet |
| `partial` | Some chunk candidates extracted, others remain |
| `fully-chunked` | All identified chunk candidates have been extracted |

## Notes

- Check the `## Chunk Candidates` section in each raw note for unchecked items — those are candidates not yet extracted.
