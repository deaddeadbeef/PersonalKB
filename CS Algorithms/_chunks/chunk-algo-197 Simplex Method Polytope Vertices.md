---
id: chunk-csa-197
type: chunk
source: "[[Cormen 2022 - Linear Programming]]"
source_loc: "Simplex Method"
topic: "optimization"
claim: "The simplex method finds optimal LP solutions by traversing polytope vertices with exponential worst case but typically polynomial practical performance in O(m+n) pivots"
confidence: verified
supports:
  - "[[Linear Programming]]"
  - "[[Simplex Method]]"
tags:
  - csa
  - csa/optimization
  - chunk
up: "[[CS Algorithms]]"
---
# Optimization — Simplex traverses polytope vertices with practical polynomial performance

## Context

The simplex method (Dantzig, 1947) maintains a basis defining a polytope vertex and pivots along edges to adjacent vertices, improving the objective at each step. Each pivot swaps one basic variable with one non-basic variable. Despite the Klee-Minty cube requiring 2^n pivots (exponential worst case), simplex typically needs O(m + n) pivots for m constraints and n variables. Bland's rule prevents cycling on degenerate vertices. The LP feasible region is a convex polytope and the optimum occurs at a vertex, justifying the vertex-traversal approach.

## Why It Matters

The simplex method remains one of the most impactful algorithms ever devised, solving problems with millions of variables in modern supply chain, logistics, and financial optimization.

## QnA Seeds

- Q: Why does the simplex method examine only vertices of the polytope?
- Q: What is the Klee-Minty cube and what does it demonstrate?
- Q: What does Bland's rule prevent in the simplex method?
