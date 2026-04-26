---
id: chunk-csa-188
type: chunk
source: "[[Cormen 2022 - Topological Sort]]"
source_loc: "Critical Path"
topic: "graphs"
claim: "The longest path in a DAG (critical path) is computable in O(V+E) by relaxing edges in topological order, unlike general graphs where longest path is NP-hard"
confidence: verified
supports:
  - "[[Critical Path]]"
  - "[[DAG Shortest Path]]"
tags:
  - csa
  - csa/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Graphs — DAG longest path (critical path) in O(V+E) via topological relaxation

## Context

In a DAG, the longest path from a source to all other vertices can be computed in O(V + E) by negating edge weights and running single-source shortest path in topological order, or equivalently by relaxing edges with max instead of min. This is the critical path in project scheduling (PERT/CPM), representing the minimum project completion time. In general graphs, longest path is NP-hard, but DAG structure enables the polynomial solution because topological order ensures each vertex is processed after all its predecessors.

## Why It Matters

Critical path analysis is fundamental to project management (PERT/CPM) and instruction scheduling in compilers, and demonstrates how DAG structure makes otherwise intractable problems efficient.

## QnA Seeds

- Q: Why is longest path in a DAG polynomial but NP-hard in general graphs?
- Q: How is the critical path used in project scheduling?
- Q: How do you compute longest path using topological order?
