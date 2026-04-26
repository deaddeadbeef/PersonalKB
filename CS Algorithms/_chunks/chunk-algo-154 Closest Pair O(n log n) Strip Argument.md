---
id: chunk-csa-154
type: chunk
source: "[[de Berg 2008 - Computational Geometry]]"
source_loc: "Closest Pair"
topic: "geometry"
claim: "Closest pair of points is solvable in O(n log n) by divide and conquer where the strip near the dividing line requires at most 7 comparisons per point"
confidence: verified
supports:
  - "[[Closest Pair Problem]]"
  - "[[Computational Geometry]]"
tags:
  - csa
  - csa/geometry
  - chunk
up: "[[CS Algorithms]]"
---
# Geometry — Closest pair in O(n log n) with at most 7 strip comparisons per point

## Context

The closest pair algorithm splits points by x-coordinate, recursively finds the closest pair in each half, then examines points within distance delta of the dividing line (where delta is the smaller recursive result). The key geometric insight: the strip of width 2*delta is partitioned into delta-by-delta boxes, each containing at most one point, limiting per-point comparisons to at most 7 neighbors. This yields recurrence T(n) = 2T(n/2) + O(n), solving to O(n log n) total.

## Why It Matters

The closest pair algorithm is a canonical example of geometric divide-and-conquer where the combine step's efficiency depends on a geometric packing argument, a technique that appears throughout computational geometry.

## QnA Seeds

- Q: Why are at most 7 comparisons needed per point in the closest-pair strip?
- Q: What is the recurrence for the closest-pair divide-and-conquer algorithm?
- Q: How does the delta-by-delta box packing argument limit comparisons?
