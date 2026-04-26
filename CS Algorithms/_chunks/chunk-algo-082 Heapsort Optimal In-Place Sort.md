---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-011]]"
confidence: high
supports:
  - "[[Heapsort]]"
  - "[[Comparison Sort Bounds]]"
qna_seeds:
  - "Q: Why is heapsort unique among comparison sorts? A: It is the only comparison sort that is simultaneously O(n log n) worst-case and in-place O(1) auxiliary space, though it is not stable."
---

# Heapsort Optimal In-Place Sort

Heapsort achieves O(n log n) worst-case time and O(1) auxiliary space, making it the only comparison sort that is simultaneously asymptotically optimal in time and in-place. It makes at most 2n log₂ n + O(n) comparisons, about 39% more than the theoretical minimum of n log₂ n − 1.44n. The tradeoff is that heapsort is not stable and has poor cache locality compared to quicksort.