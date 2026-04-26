---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-015]]"
confidence: high
supports:
  - "[[Prim's Algorithm]]"
  - "[[Fibonacci Heaps]]"
  - "[[Minimum Spanning Trees]]"
qna_seeds:
  - "Q: What is Prim's best time complexity? A: O(E + V log V) with a Fibonacci heap, since each of E decrease-key operations costs O(1) amortized and each of V extract-min operations costs O(log V)."
---

# Prim's Algorithm Fibonacci Heap Bound

Prim's algorithm with a Fibonacci heap runs in O(E + V log V) for connected graphs, since each of at most E decrease-key operations costs O(1) amortized and each of V extract-min operations costs O(log V). With a binary heap it runs in O(E log V). For dense graphs (E = Θ(V²)), an array-based O(V²) implementation is optimal, outperforming both Kruskal's O(V² log V) and heap-based Prim's.