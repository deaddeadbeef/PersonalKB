---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-013]]"
confidence: high
supports:
  - "[[Bellman-Ford Algorithm]]"
  - "[[Dijkstra's Algorithm]]"
  - "[[All-Pairs Shortest Paths]]"
qna_seeds:
  - "Q: How does Johnson's algorithm combine Bellman-Ford and Dijkstra? A: One Bellman-Ford run in O(VE) computes reweighting potentials; then V Dijkstra runs give O(V² log V + VE) total for all pairs."
---

# Johnson's All-Pairs Shortest Paths

Johnson's algorithm solves all-pairs shortest paths in O(V² log V + VE) by combining Bellman-Ford and Dijkstra. A single Bellman-Ford run in O(VE) computes a potential function h(v) that reweights all edges to be non-negative (w'(u,v) = w(u,v) + h(u) − h(v) ≥ 0). Then V instances of Dijkstra with the reweighted graph compute all-pairs distances. This is faster than Floyd-Warshall's O(V³) for sparse graphs.