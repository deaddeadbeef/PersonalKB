---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-012]]"
confidence: high
supports:
  - "[[Dijkstra's Algorithm]]"
  - "[[Fibonacci Heaps]]"
qna_seeds:
  - "Q: What is the exact breakdown of Dijkstra with Fibonacci heap? A: V extract-min operations cost O(V log V) total; E decrease-key operations cost O(E) total at O(1) amortized each; overall O(V log V + E)."
---

# Dijkstra Fibonacci Heap Improvement

With a Fibonacci heap, Dijkstra's total running time is O(V log V + E) because each of the V extract-min operations costs O(log V) amortized and each of the E decrease-key operations costs O(1) amortized. The shortest-path tree produced contains exactly V − 1 edges, and for any vertex v, the tree path from source to v is a shortest path. For sparse graphs where E = O(V), this gives O(V log V).