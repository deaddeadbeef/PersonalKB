---
tags: [cs-ds, chunk]
id: chunk-ds-075
source: "[[raw-ds-014]]"
supports: ["[[Fenwick Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# 2D Fenwick tree answers rectangle sum queries in Olog2n

## Context
1D Fenwick trees handle prefix sums on arrays.

## Claim
Extending Fenwick trees to 2D gives O(log^2 n) point update and rectangle sum query by nesting the bit manipulation technique across both dimensions.

## Why It Matters
Efficient for 2D cumulative frequency tables in competitive programming and image processing.

## QnA Seeds
- Q: How does 2D extension work? -> A: Outer loop on row index using lowbit, inner loop on column index using lowbit.
- Q: Space complexity? -> A: O(n * m) for an n x m grid.
