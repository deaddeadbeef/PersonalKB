---
id: chunk-csa-147
type: chunk
source: "[[Skiena 2020 - Backtracking and Branch-and-Bound]]"
source_loc: "Branch-and-Bound"
topic: "backtracking"
claim: "Branch-and-bound extends backtracking for optimization by maintaining bounds, pruning subtrees whose best possible outcome cannot improve on the current best solution"
confidence: verified
supports:
  - "[[Branch and Bound]]"
  - "[[Combinatorial Optimization]]"
tags:
  - csa
  - csa/backtracking
  - chunk
up: "[[CS Algorithms]]"
---
# Branch-and-Bound — Optimization bounds prune unpromising subtrees

## Context

Branch-and-bound augments backtracking with optimization bounds: for minimization problems a lower bound is computed for each node, and for maximization an upper bound. If the bound for a subtree is worse than the best complete solution found so far, the subtree is pruned entirely. The branching strategy determines how subproblems are created—for 0-1 variables, branching fixes a variable to 0 or 1; for TSP, branching includes or excludes a specific edge. Effective bounding functions (from LP relaxation, MST, etc.) can reduce the explored space by orders of magnitude.

## Why It Matters

Branch-and-bound is the primary method in commercial integer programming solvers (CPLEX, Gurobi) and provides the framework for solving real-world combinatorial optimization problems.

## QnA Seeds

- Q: How does branch-and-bound differ from basic backtracking?
- Q: What role does the bounding function play in branch-and-bound efficiency?
- Q: How does branching work for 0-1 integer programming vs TSP?
