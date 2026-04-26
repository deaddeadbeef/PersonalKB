---
tags: [cs-ds, chunk]
id: chunk-ds-049
source: "[[raw-ds-035]]"
supports: ["[[k-d Trees and Spatial Data]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# K-d trees partition space by alternating dimensions for On space

## Context
Multi-dimensional search in O(n) space is desirable for spatial data.

## Claim
K-d trees alternate splitting dimensions at each level, using only O(n) space, with O(sqrt(n) + k) expected query time in 2D — worse than range trees but with far less space.

## Why It Matters
Default structure for nearest-neighbor search in moderate dimensions (2D-20D).

## QnA Seeds
- Q: How are dimensions alternated? -> A: Level 0 splits on x, level 1 on y, level 2 on z, cycling.
- Q: Why O(sqrt n) query in 2D? -> A: Each split eliminates about half the space, but worst case crosses many partitions.
