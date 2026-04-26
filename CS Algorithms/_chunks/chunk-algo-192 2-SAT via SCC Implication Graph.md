---
id: chunk-csa-192
type: chunk
source: "[[Cormen 2022 - Strongly Connected Components]]"
source_loc: "2-SAT Application"
topic: "graphs"
claim: "2-SAT is solvable in O(V+E) via SCC decomposition on the implication graph: satisfiable iff no variable and its negation share an SCC"
confidence: verified
supports:
  - "[[SCC]]"
  - "[[2-SAT]]"
tags:
  - csa
  - csa/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Graphs — 2-SAT solvable in O(V+E) via SCC on implication graph

## Context

In 2-SAT, the implication graph has 2n vertices (one per literal). Each clause (a or b) is modeled as edges (not-a -> b) and (not-b -> a). A satisfying assignment exists if and only if no variable x and its negation not-x belong to the same SCC. If they do, x implies not-x and not-x implies x, creating a contradiction. The solution is found by processing SCCs in reverse topological order of the condensation, assigning truth values to ensure consistency. This runs in O(V + E) total.

## Why It Matters

2-SAT via SCC is an elegant polynomial-time algorithm for a restricted satisfiability problem, contrasting sharply with the NP-completeness of 3-SAT and general SAT.

## QnA Seeds

- Q: How is a 2-SAT clause modeled as edges in the implication graph?
- Q: What SCC condition indicates a 2-SAT formula is unsatisfiable?
- Q: How does 2-SAT complexity contrast with 3-SAT?
