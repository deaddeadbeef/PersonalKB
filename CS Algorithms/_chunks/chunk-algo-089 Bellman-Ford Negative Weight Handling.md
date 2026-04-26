---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-013]]"
confidence: high
supports:
  - "[[Bellman-Ford Algorithm]]"
  - "[[Shortest Paths]]"
qna_seeds:
  - "Q: How does Bellman-Ford handle negative edge weights? A: It performs V−1 rounds of relaxing all E edges in O(VE) time; after k rounds, it has found all shortest paths using at most k edges."
---

# Bellman-Ford Negative Weight Handling

The Bellman-Ford algorithm computes single-source shortest paths in O(VE) time and correctly handles negative-weight edges (unlike Dijkstra). It performs V − 1 rounds of edge relaxation: after k rounds, all shortest paths consisting of at most k edges are finalized. Since any shortest path without negative cycles has at most V − 1 edges, V − 1 rounds suffice. For V = 10,000 and E = 100,000, this is approximately 999 million relaxation operations.