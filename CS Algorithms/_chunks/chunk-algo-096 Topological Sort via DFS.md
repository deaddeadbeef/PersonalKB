---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-014]]"
confidence: high
supports:
  - "[[Topological Sort]]"
  - "[[DFS]]"
  - "[[DAGs]]"
qna_seeds:
  - "Q: How does DFS produce a topological ordering? A: Output vertices in reverse DFS finish-time order; alternatively, Kahn's algorithm repeatedly removes zero-in-degree vertices. Both run in O(V + E)."
---

# Topological Sort via DFS

Topological sorting of a DAG is achieved by running DFS and outputting vertices in reverse finish-time order, or equivalently by Kahn's algorithm (repeatedly removing vertices with in-degree zero), both in O(V + E) time. The DFS-based approach naturally integrates with cycle detection: if a back edge is found, the graph is not a DAG and no topological ordering exists. This is the foundation for build systems, task scheduling, and DP evaluation order.