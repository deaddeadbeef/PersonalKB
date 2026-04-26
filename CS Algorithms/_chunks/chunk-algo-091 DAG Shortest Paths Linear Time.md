---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-013]]"
confidence: high
supports:
  - "[[Shortest Paths]]"
  - "[[Topological Sort]]"
  - "[[Dynamic Programming]]"
qna_seeds:
  - "Q: What is the fastest shortest-path algorithm for DAGs? A: Process vertices in topological order, relaxing outgoing edges for each—O(V + E) time, one pass through all edges."
---

# DAG Shortest Paths Linear Time

For directed acyclic graphs (DAGs), shortest paths from a single source can be computed in O(V + E) time by processing vertices in topological order and relaxing all outgoing edges for each vertex. This requires exactly one pass through all edges, using O(V) space. This technique is fundamental because any dynamic programming recurrence can be viewed as a shortest or longest path problem in the DAG of subproblems.