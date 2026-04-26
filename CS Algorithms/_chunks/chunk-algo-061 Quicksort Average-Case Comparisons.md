---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-006]]"
confidence: high
supports:
  - "[[Quicksort]]"
  - "[[Comparison Sort Bounds]]"
qna_seeds:
  - "Q: How many comparisons does quicksort make on average? A: Approximately 2n ln n ≈ 1.39n log₂ n, only 39% more than the information-theoretic lower bound of n log₂ n."
---

# Quicksort Average-Case Comparisons

Quicksort's average-case running time is O(n log n) with a small constant factor. The average number of comparisons is approximately 2n ln n ≈ 1.39n log₂ n, which is only 39% more than the information-theoretic lower bound of n log₂ n. This makes quicksort one of the fastest general-purpose comparison sorts in practice despite its O(n²) worst case.