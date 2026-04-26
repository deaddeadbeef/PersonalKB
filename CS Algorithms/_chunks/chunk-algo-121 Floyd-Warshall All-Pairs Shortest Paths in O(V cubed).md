---
id: chunk-algo-121
type: chunk
source: "[[raw-algo-021]]"
source_loc: "Floyd-Warshall - Summary and Key Claims"
topic: "graphs"
claim: "Floyd-Warshall computes all-pairs shortest paths in O(V^3) time and O(V^2) space via DP recurrence D^(k)[i][j] = min(D^(k-1)[i][j], D^(k-1)[i][k] + D^(k-1)[k][j]), optimal for dense adjacency-matrix graphs."
confidence: verified
supports:
  - "[[Floyd-Warshall Algorithm]]"
  - "[[Shortest Path Overview]]"
tags:
  - cs-algorithms
  - cs-algorithms/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Floyd-Warshall All-Pairs Shortest Paths in O(V cubed)

## Context

The algorithm builds matrices D^(0) through D^(V) where D^(k)[i][j] is the shortest i-to-j path using only vertices {1,...,k} as intermediates. Space reduces to O(V^2) by in-place updates since row k and column k are invariant between layers. For sparse graphs, Johnson's O(V^2 log V + VE) outperforms Floyd-Warshall, but for dense graphs the cubic bound is competitive and the algorithm's simplicity (three nested loops, ~5 lines) makes it highly implementable.

## Why It Matters

Floyd-Warshall is the standard all-pairs shortest path algorithm for dense graphs, used in network routing, GIS driving distance computation, and graph analysis tools.

## QnA Seeds

- Q: What is the Floyd-Warshall DP recurrence?
- Q: Why can Floyd-Warshall update in-place with O(V^2) space?
- Q: When does Johnson's algorithm outperform Floyd-Warshall?