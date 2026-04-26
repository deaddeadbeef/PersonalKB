---
id: chunk-csa-153
type: chunk
source: "[[de Berg 2008 - Computational Geometry]]"
source_loc: "Convex Hull"
topic: "geometry"
claim: "Graham scan computes the 2D convex hull in O(n log n) which is optimal since convex hull reduces to sorting via the parabola reduction"
confidence: verified
supports:
  - "[[Convex Hull]]"
  - "[[Computational Geometry]]"
tags:
  - csa
  - csa/geometry
  - chunk
up: "[[CS Algorithms]]"
---
# Geometry — Graham scan computes 2D convex hull in optimal O(n log n)

## Context

Graham scan sorts points by polar angle relative to the bottom-most point, then processes them in order while maintaining the convex hull invariant using a stack. Points causing left turns are pushed; right turns trigger pops removing non-hull points. The O(n log n) bound is dominated by sorting and is optimal: the lower bound follows from a reduction from sorting—given n numbers, create points (x_i, x_i^2) on a parabola whose convex hull reveals the sorted order. Jarvis march is an output-sensitive alternative at O(nh) where h is the hull size.

## Why It Matters

Convex hull is the foundational problem in computational geometry, and Graham scan's optimality proof via reduction from sorting demonstrates the technique of proving lower bounds through reductions.

## QnA Seeds

- Q: How does Graham scan maintain the convex hull invariant using a stack?
- Q: Why is O(n log n) optimal for convex hull computation?
- Q: When is Jarvis march preferable to Graham scan?
