---
tags: [cs-ds, chunk]
id: chunk-ds-113
source: "[[raw-ds-006]]"
supports: ["[[B-Trees and B-Plus Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Write-ahead logging prevents B-tree corruption on crash

## Context
B-tree page splits are multi-step operations that can be interrupted by crashes.

## Claim
Write-ahead logging writes all changes to a sequential log before applying to tree pages. On crash recovery replays the log restoring the tree to a consistent state.

## Why It Matters
Every database using B-trees (PostgreSQL, MySQL InnoDB, SQLite) requires WAL for crash safety.

## QnA Seeds
- Q: What is write-ahead rule? -> A: Log record must be flushed to disk before the corresponding data page.
- Q: How does recovery work? -> A: Redo committed changes and undo uncommitted ones from the log.
