---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-012]]"
confidence: high
supports:
  - "[[Dijkstra's Algorithm]]"
  - "[[Greedy Algorithms]]"
qna_seeds:
  - "Q: Why does Dijkstra's algorithm require non-negative weights? A: The greedy invariant—the unvisited vertex with smallest tentative distance has its final distance—only holds when edge weights are non-negative."
---

# Dijkstra Greedy Correctness Proof

Dijkstra's algorithm correctly computes shortest paths from a single source to all reachable vertices in graphs with non-negative edge weights, proved by induction on the number of finalized vertices. The key greedy property is that the vertex with the smallest tentative distance among unvisited vertices has its final shortest-path distance. With negative weights, a vertex finalized early may later be reachable via a shorter path, violating this invariant.