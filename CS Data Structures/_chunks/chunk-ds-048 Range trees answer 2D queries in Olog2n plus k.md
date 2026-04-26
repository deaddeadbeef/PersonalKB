---
tags: [cs-ds, chunk]
id: chunk-ds-048
source: "[[raw-ds-035]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Range trees answer 2D orthogonal queries in Olog2n plus k

## Context
2D range queries: find all points with x in [x1,x2] and y in [y1,y2].

## Claim
A range tree stores points in a primary BST on x; each node has a secondary BST on y for its subtree. This gives O(log^2 n + k) query time with O(n log n) space.

## Why It Matters
Foundational structure for computational geometry and spatial database indexing.

## QnA Seeds
- Q: Why two levels of trees? -> A: Primary filters x-range, secondary filters y-range within those.
- Q: How does fractional cascading help? -> A: Eliminates one log factor, reducing query to O(log n + k).
