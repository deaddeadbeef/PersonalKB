---
tags: [cs-ds, chunk]
id: chunk-ds-047
source: "[[raw-ds-034]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Piece tables avoid copying by indexing into original plus add buffer

## Context
Text editors need efficient insert/delete on large documents.

## Claim
A piece table maintains a table of pieces pointing into an original buffer (read-only) and an append-only add buffer, making inserts O(1) for the data copy and O(log n) for table management.

## Why It Matters
VS Code uses piece tables — extremely efficient for editing workflows with undo/redo support.

## QnA Seeds
- Q: What are the two buffers? -> A: Original (immutable source) and add (append-only for new text).
- Q: How does delete work? -> A: Split the piece containing the deletion range into two pieces excluding the deleted text.
