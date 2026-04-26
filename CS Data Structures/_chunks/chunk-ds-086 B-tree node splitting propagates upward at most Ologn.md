---
tags: [cs-ds, chunk]
id: chunk-ds-086
source: "[[raw-ds-006]]"
supports: ["[[B-Trees and B-Plus Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# B-tree node splitting propagates upward at most O(log n) levels

## Context
Inserting into a full B-tree node requires splitting.

## Claim
When a node overflows it splits into two nodes and promotes the median key to the parent. This may cascade upward but at most O(log_m n) splits occur and the tree grows taller only when the root splits.

## Why It Matters
Splitting is the only way B-trees grow in height ensuring balanced growth from the bottom up.

## QnA Seeds
- Q: When does the tree height increase? -> A: Only when the root splits creating a new root.
- Q: Why promote the median? -> A: Ensures both halves have at least minimum occupancy.
