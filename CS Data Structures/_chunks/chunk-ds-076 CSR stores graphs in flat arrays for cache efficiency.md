---
tags: [cs-ds, chunk]
id: chunk-ds-076
source: "[[raw-ds-015]]"
supports: ["[[Adjacency List and Adjacency Matrix]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# CSR format stores graphs in flat arrays for maximum cache efficiency

## Context
Adjacency lists use linked lists or vectors of vectors with poor cache locality.

## Claim
Compressed Sparse Row stores all neighbors in one flat array with an offset array indexing into it. This gives O(1) neighbor-start lookup and sequential memory access for neighbor iteration.

## Why It Matters
Standard format for graph analytics frameworks like GraphBLAS, ligra, and scipy sparse matrices.

## QnA Seeds
- Q: What are the two arrays? -> A: Offsets (one per vertex) and edges (one per edge flat).
- Q: Main limitation? -> A: Static. Adding edges requires rebuilding arrays.
