---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-007]]"
confidence: high
supports:
  - "[[Mergesort]]"
  - "[[Comparison Sort Bounds]]"
qna_seeds:
  - "Q: What is mergesort's exact worst-case comparison count? A: n⌈log₂ n⌉ − 2^⌈log₂ n⌉ + 1; for n = 1,000,000 this is approximately 19,931,569 comparisons."
---

# Mergesort Worst-Case Optimal Comparisons

Mergesort guarantees O(n log n) comparisons in the worst case, matching the Ω(n log n) lower bound for comparison-based sorting. The exact worst-case number of comparisons is n⌈log₂ n⌉ − 2^⌈log₂ n⌉ + 1, which for n = 1,000,000 is approximately 19,931,569 comparisons. The merge subroutine combines two sorted sequences of total length n in exactly n − 1 comparisons in the worst case.