---
id: chunk-csa-148
type: chunk
source: "[[Skiena 2020 - Backtracking and Branch-and-Bound]]"
source_loc: "Best-First Search"
topic: "backtracking"
claim: "Best-first branch-and-bound uses a priority queue ordered by bound values, expanding the most promising node first rather than following depth-first order"
confidence: verified
supports:
  - "[[Branch and Bound]]"
  - "[[Search Strategies]]"
tags:
  - csa
  - csa/backtracking
  - chunk
up: "[[CS Algorithms]]"
---
# Branch-and-Bound — Best-first search expands most promising node via priority queue

## Context

While basic backtracking uses depth-first exploration, best-first branch-and-bound uses a priority queue to expand the node with the tightest (most promising) bound first. For TSP, the lower bound is computed from minimum spanning tree cost or LP relaxation. This strategy focuses computational effort on the most likely paths to the optimum, potentially finding good solutions faster and enabling more effective pruning. Despite exponential worst-case complexity, well-designed heuristic ordering combined with best-first search solves many practical instances efficiently.

## Why It Matters

Best-first search is how modern solvers like CPLEX and Gurobi actually explore the branch-and-bound tree, making it essential for understanding practical optimization.

## QnA Seeds

- Q: How does best-first differ from depth-first branch-and-bound?
- Q: What data structure implements best-first branch-and-bound?
- Q: How is the lower bound for TSP branch-and-bound typically computed?
