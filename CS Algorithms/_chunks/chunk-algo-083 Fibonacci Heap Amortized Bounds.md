---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-011]]"
confidence: high
supports:
  - "[[Fibonacci Heaps]]"
  - "[[Priority Queues]]"
  - "[[Dijkstra's Algorithm]]"
qna_seeds:
  - "Q: How do Fibonacci heaps improve Dijkstra's algorithm? A: Decrease-key costs O(1) amortized (vs O(log n) in binary heaps), reducing Dijkstra from O((V + E) log V) to O(V log V + E)."
---

# Fibonacci Heap Amortized Bounds

Fibonacci heaps support decrease-key in O(1) amortized time and extract-min in O(log n) amortized time, using lazy consolidation with potential function Φ = t + 2m (t = trees, m = marked nodes). This reduces Dijkstra's algorithm from O((V + E) log V) with a binary heap to O(V log V + E). Despite theoretical superiority, Fibonacci heaps are rarely used in practice due to large constant factors and complex implementation.