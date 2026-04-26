---
tags: [cs-ds, chunk]
id: chunk-ds-009
source: "[[raw-ds-006]]"
supports: ["[[B-Trees and B-Plus Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# B-trees minimize disk IO by matching node size to disk pages

## Context
Disk access is 100000x slower than memory access.

## Claim
B-trees size each node to match a disk page (4-16 KB), so reading one node requires one disk IO. High branching factor (100-1000) keeps height to 3-4 levels for billions of records.

## Why It Matters
This makes B-trees the dominant index structure for databases and file systems.

## QnA Seeds
- Q: Why high branching factors? -> A: Each node read costs one disk IO regardless of size, so wider nodes mean fewer levels.
- Q: Why B+ over plain B-trees? -> A: Data only in leaves with linked list enables efficient range queries.
