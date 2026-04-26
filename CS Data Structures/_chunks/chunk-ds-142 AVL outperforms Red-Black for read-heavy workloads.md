---
tags: [cs-ds, chunk]
id: chunk-ds-142
source: "[[raw-ds-005]]"
supports: ["[[AVL Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# AVL trees outperform Red-Black for read-heavy workloads

## Context
Both AVL and Red-Black provide O(log n) guarantees.

## Claim
AVL trees have stricter balance (height at most 1.44 log n vs 2 log n for RB) resulting in shorter average search paths. For read-heavy workloads with few mutations AVL trees provide measurably faster lookups.

## Why It Matters
Informs the choice between AVL and RB trees based on workload characteristics.

## QnA Seeds
- Q: How much shorter are AVL paths? -> A: About 30 percent shorter on average versus Red-Black trees.
- Q: Why not always use AVL then? -> A: More rotations per insertion and deletion. RB wins for write-heavy workloads.
