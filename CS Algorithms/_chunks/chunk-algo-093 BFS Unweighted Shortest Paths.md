---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-014]]"
confidence: high
supports:
  - "[[BFS]]"
  - "[[Graph Traversal]]"
  - "[[Shortest Paths]]"
qna_seeds:
  - "Q: Why does BFS compute shortest paths in unweighted graphs? A: BFS explores vertices level by level, discovering all vertices at distance d before any at distance d+1, in O(V + E) time."
---

# BFS Unweighted Shortest Paths

BFS computes the shortest path (minimum number of edges) from a source vertex to all reachable vertices in an unweighted graph in O(V + E) time. It explores vertices level by level using a queue, discovering all vertices at distance d before any vertex at distance d + 1. The BFS tree has the property that every non-tree edge connects vertices whose levels differ by at most 1, and uses O(V) space.