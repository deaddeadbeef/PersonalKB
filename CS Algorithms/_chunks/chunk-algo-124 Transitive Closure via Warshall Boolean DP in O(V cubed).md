---
id: chunk-algo-124
type: chunk
source: "[[raw-algo-021]]"
source_loc: "Floyd-Warshall - Key Claims"
topic: "graphs"
claim: "Warshall's algorithm (1962) computes transitive closure—all-pairs reachability—in O(V^3) using the same structure as Floyd-Warshall but replacing (min, +) with (OR, AND) on a Boolean matrix, with bitwise operations giving ~64x practical speedup."
confidence: verified
supports:
  - "[[Floyd-Warshall Algorithm]]"
  - "[[Graph Algorithms]]"
tags:
  - cs-algorithms
  - cs-algorithms/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Transitive Closure via Warshall Boolean DP in O(V cubed)

## Context

The recurrence T^(k)[i][j] = T^(k-1)[i][j] OR (T^(k-1)[i][k] AND T^(k-1)[k][j]) determines reachability using vertices {1,...,k} as intermediates. The Boolean matrix uses bitwise operations, processing 64 entries per machine word. Applications include relational database query optimization and reachability analysis in program verification. Warshall's algorithm predates the shortest-path version and illustrates how changing the algebraic semiring solves different problems with the same structure.

## Why It Matters

Warshall's transitive closure connects graph theory to relational algebra and databases. Its Boolean nature enables significant practical speedups and illustrates the semiring generalization of shortest-path algorithms.

## QnA Seeds

- Q: How does Warshall differ from Floyd-Warshall?
- Q: What practical speedup do bitwise operations provide?
- Q: What is the semiring interpretation of these algorithms?