---
id: chunk-algo-126
type: chunk
source: "[[raw-algo-022]]"
source_loc: "Network Flow - Key Claims"
topic: "network-flow"
claim: "Edmonds-Karp uses BFS for shortest augmenting paths, guaranteeing O(VE^2) time independent of capacities; it performs at most O(VE) augmentations because BFS path lengths are non-decreasing and distances from s increase monotonically."
confidence: verified
supports:
  - "[[Network Flow]]"
  - "[[Edmonds-Karp Algorithm]]"
tags:
  - cs-algorithms
  - cs-algorithms/network-flow
  - chunk
up: "[[CS Algorithms]]"
---
# Edmonds-Karp Guarantees O(VE squared) via BFS

## Context

Basic Ford-Fulkerson with DFS runs in O(E*|f*|) which can be pseudo-polynomial. Edmonds-Karp fixes this by augmenting along shortest paths via BFS. After each augmentation, at least one edge becomes saturated, and the s-to-vertex distances can only increase. This limits augmentations to O(VE), each costing O(E) for BFS, giving O(VE^2). For dense graphs (E~V^2), this is O(V^5), motivating Dinic's O(V^2*E).

## Why It Matters

Edmonds-Karp shows how BFS instead of DFS transforms a pseudo-polynomial algorithm into a strongly polynomial one. The monotone distance argument recurs throughout flow algorithm analysis.

## QnA Seeds

- Q: How does Edmonds-Karp improve over Ford-Fulkerson?
- Q: Why at most O(VE) augmentations in Edmonds-Karp?
- Q: Why can basic Ford-Fulkerson be pseudo-polynomial?