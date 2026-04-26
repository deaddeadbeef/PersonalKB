---
tags: [cs-ds, chunk]
id: chunk-ds-073
source: "[[raw-ds-012]]"
supports: ["[[Disjoint Sets and Union-Find]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Union by rank keeps Union-Find trees shallow at Ologn height

## Context
Naive union can create tall trees making Find O(n).

## Claim
Union by rank always attaches the shorter tree under the taller one keeping tree height at most O(log n). Combined with path compression this drops to O(alpha(n)).

## Why It Matters
Without rank, path compression alone only gives O(log n) amortized. Both optimizations are needed.

## QnA Seeds
- Q: What is rank? -> A: Upper bound on tree height maintained during unions.
- Q: Why not union by size? -> A: Both work but rank is simpler since it only increases on equal-rank merges.
