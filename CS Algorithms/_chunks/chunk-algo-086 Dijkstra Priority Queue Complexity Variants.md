---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-012]]"
confidence: high
supports:
  - "[[Dijkstra's Algorithm]]"
  - "[[Priority Queues]]"
qna_seeds:
  - "Q: How does priority queue choice affect Dijkstra's complexity? A: Array: O(V²+E); binary heap: O((V+E) log V); Fibonacci heap: O(V log V + E). Array is optimal for dense graphs with E = Θ(V²)."
---

# Dijkstra Priority Queue Complexity Variants

Dijkstra's algorithm complexity depends on the priority queue: O(V² + E) with a simple array, O((V + E) log V) with a binary heap (V extract-mins at O(log V) plus E decrease-keys at O(log V)), and O(V log V + E) with a Fibonacci heap. For dense graphs where E = Θ(V²), the array-based O(V²) implementation is optimal and outperforms heap-based versions due to lower constant factors.