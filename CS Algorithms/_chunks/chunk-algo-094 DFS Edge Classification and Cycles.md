---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-014]]"
confidence: high
supports:
  - "[[DFS]]"
  - "[[Cycle Detection]]"
  - "[[Graph Traversal]]"
qna_seeds:
  - "Q: How does DFS detect cycles in directed graphs? A: DFS classifies edges into tree, back, forward, and cross edges; a back edge exists if and only if the directed graph contains a cycle."
---

# DFS Edge Classification and Cycles

DFS classifies edges into four types: tree edges (to unvisited vertices), back edges (to ancestors), forward edges (to descendants via non-tree paths), and cross edges (between unrelated subtrees). The presence of a back edge is equivalent to the existence of a cycle in a directed graph. DFS runs in O(V + E) time but may require O(V) stack frames for recursion, necessitating an iterative implementation for graphs with V > 10⁶.