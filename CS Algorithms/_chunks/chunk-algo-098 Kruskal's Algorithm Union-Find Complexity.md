---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-015]]"
confidence: high
supports:
  - "[[Kruskal's Algorithm]]"
  - "[[Union-Find]]"
qna_seeds:
  - "Q: What dominates Kruskal's algorithm running time? A: Sorting edges in O(E log E); union-find operations contribute only O(E · α(V)) ≈ O(E), where α is the inverse Ackermann function (≤ 4 for V < 10^80)."
---

# Kruskal's Algorithm Union-Find Complexity

Kruskal's algorithm runs in O(E log E) time, dominated by sorting edges. The union-find operations with union by rank and path compression contribute O(E · α(V)) ≈ O(E) time, where α is the inverse Ackermann function—effectively O(1) per operation for all practical input sizes (α(V) ≤ 4 for V < 10^{80}). The algorithm greedily adds the cheapest edge that doesn't create a cycle.