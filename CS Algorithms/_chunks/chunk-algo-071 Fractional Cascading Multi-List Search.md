---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-008]]"
confidence: high
supports:
  - "[[Binary Search]]"
  - "[[Fractional Cascading]]"
  - "[[Computational Geometry]]"
qna_seeds:
  - "Q: How does fractional cascading speed up searching across multiple sorted lists? A: It reduces binary search across k sorted lists from O(k log n) to O(log n + k) total time by threading pointers between lists."
---

# Fractional Cascading Multi-List Search

Fractional cascading allows binary search across k sorted lists sharing elements in O(log n + k) total time instead of the naive O(k log n). It works by threading forwarding pointers between adjacent lists so that a single binary search in the first list propagates results to subsequent lists in O(1) each. This technique has applications in computational geometry range trees and multi-level data structures.