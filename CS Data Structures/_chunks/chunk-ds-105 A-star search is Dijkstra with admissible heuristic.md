---
tags: [cs-ds, chunk]
id: chunk-ds-105
source: "[[raw-ds-031]]"
supports: ["[[Graphs Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# A-star search is Dijkstra with an admissible heuristic

## Context
Dijkstra explores all directions equally which is wasteful with a known target.

## Claim
A-star adds a heuristic h(v) estimating distance to target using priority f(v) = g(v) + h(v). If h is admissible (never overestimates) A-star finds optimal paths while exploring far fewer nodes than Dijkstra.

## Why It Matters
Standard pathfinding algorithm in games, robotics, and navigation systems.

## QnA Seeds
- Q: What makes a heuristic admissible? -> A: It never overestimates the true distance to the goal.
- Q: Common heuristics? -> A: Euclidean distance, Manhattan distance for grids.
