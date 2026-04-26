---
tags: [cs-ds, chunk]
id: chunk-ds-155
source: "[[raw-ds-032]]"
supports: ["[[Graphs Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# MST uniqueness is guaranteed when all edge weights are distinct

## Context
A graph may have multiple minimum spanning trees.

## Claim
If all edge weights are distinct then the MST is unique. This follows from the cut property: for each cut there is exactly one lightest edge so every MST must include the same edges.

## Why It Matters
Simplifies correctness proofs and ensures Kruskal and Prim produce identical results on the same graph.

## QnA Seeds
- Q: What if weights are not distinct? -> A: Multiple valid MSTs may exist with the same total weight but different edge sets.
- Q: Does tie-breaking matter? -> A: Yes. Consistent tie-breaking can force unique MST even with duplicate weights.
