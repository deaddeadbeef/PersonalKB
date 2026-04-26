---
id: chunk-csa-155
type: chunk
source: "[[de Berg 2008 - Computational Geometry]]"
source_loc: "Line Segment Intersection"
topic: "geometry"
claim: "Bentley-Ottmann sweep-line finds all k intersections among n segments in O((n+k) log n) using an event queue and status structure"
confidence: verified
supports:
  - "[[Sweep Line Algorithm]]"
  - "[[Computational Geometry]]"
tags:
  - csa
  - csa/geometry
  - chunk
up: "[[CS Algorithms]]"
---
# Geometry — Bentley-Ottmann sweep-line for segment intersections in O((n+k) log n)

## Context

The Bentley-Ottmann algorithm sweeps a vertical line left to right, processing events (segment endpoints and intersections) from an event queue while maintaining a status structure of active segments ordered by their y-coordinate at the sweep line. Only adjacent segments in the status structure can produce new intersection events. This reduces the 2D intersection problem to a sequence of 1D operations, achieving O((n + k) log n) time where k is the number of intersections—a major improvement over O(n^2) brute force.

## Why It Matters

The sweep-line paradigm introduced in computational geometry reduces 2D problems to 1D and has influenced algorithm design across many domains including GIS, VLSI design, and computational biology.

## QnA Seeds

- Q: How does the sweep-line paradigm reduce 2D problems to 1D?
- Q: Why can only adjacent segments in the status structure produce new intersections?
- Q: What data structures does Bentley-Ottmann use and what are their roles?
