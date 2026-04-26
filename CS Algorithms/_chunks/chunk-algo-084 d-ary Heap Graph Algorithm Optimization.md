---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-011]]"
confidence: high
supports:
  - "[[Binary Heaps]]"
  - "[[Priority Queues]]"
  - "[[Dijkstra's Algorithm]]"
qna_seeds:
  - "Q: How does a d-ary heap optimize Dijkstra? A: With d = E/V children per node, decrease-key costs O(log_d n) and extract-min costs O(d log_d n), giving O(E log_{E/V} V) total for Dijkstra."
---

# d-ary Heap Graph Algorithm Optimization

A d-ary heap with d children per node reduces tree height to log_d n, optimizing decrease-key to O(log_d n) at the cost of O(d log_d n) for extract-min. Setting d = E/V optimizes Dijkstra's algorithm to O(E log_{E/V} V), which is superior to binary heap Dijkstra for dense graphs. This provides a practical middle ground between binary heaps and Fibonacci heaps without the latter's implementation complexity.