---
id: chunk-csa-014
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 6"
topic: "graphs"
claim: "Floyd-Warshall solves all-pairs shortest paths via dynamic programming on intermediate vertex sets in Theta(n cubed)"
confidence: verified
supports:
  - "[[Floyd-Warshall Algorithm]]"
  - "[[Shortest Path Overview]]"
tags:
  - csa
  - csa/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Graphs — Floyd-Warshall solves all-pairs shortest paths in Theta(n cubed)

## Context

Floyd-Warshall defines shortest[u,v,x] = the shortest path from u to v using only vertices {1,…,x} as intermediates. Base case: shortest[u,v,0] = w(u,v) if edge exists, ∞ otherwise (and 0 for u=v). Transition: shortest[u,v,x] = min(shortest[u,v,x−1], shortest[u,x,x−1] + shortest[x,v,x−1]) — either vertex x is not on the optimal path, or it is, in which case we split at x. Fill an n×n×n table; the final layer is the answer. In practice compress to two n×n arrays. Time Θ(n³). Works with negative weights; detects negative-weight cycles if any diagonal entry becomes negative.

## Why It Matters

Floyd-Warshall is the go-to all-pairs algorithm for dense graphs where n is manageable. Its simplicity (three nested loops) makes it easy to implement correctly. The DP formulation is a beautiful example of the "intermediaries" DP pattern: parameterise the subproblem by which vertices are allowed as intermediates.

## QnA Seeds

- Q: What is the recurrence for Floyd-Warshall?
- Q: When is Floyd-Warshall preferable to running Dijkstra from every vertex?
- Q: How does Floyd-Warshall detect negative-weight cycles?
