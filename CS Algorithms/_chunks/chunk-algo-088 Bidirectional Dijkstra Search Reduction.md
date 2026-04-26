---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-012]]"
confidence: high
supports:
  - "[[Dijkstra's Algorithm]]"
  - "[[Graph Search Optimization]]"
qna_seeds:
  - "Q: How does bidirectional Dijkstra reduce search space? A: It runs simultaneous searches from source and target, reducing explored area from πd² to πd²/2 in Euclidean graphs by terminating when frontiers meet."
---

# Bidirectional Dijkstra Search Reduction

Bidirectional Dijkstra runs simultaneous searches from source and target, terminating when search frontiers meet. This reduces the search space by approximately half in Euclidean graphs, exploring roughly πd²/2 area instead of πd². For road networks (US: ~24 million vertices, ~58 million edges), A* with landmark-based lower bounds (ALT algorithm) typically expands fewer than 1% of vertices compared to plain Dijkstra.