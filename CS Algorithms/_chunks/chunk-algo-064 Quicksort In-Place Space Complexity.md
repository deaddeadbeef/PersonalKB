---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-006]]"
confidence: high
supports:
  - "[[Quicksort]]"
  - "[[Space Complexity]]"
qna_seeds:
  - "Q: How much auxiliary space does quicksort use? A: O(log n) average-case stack space for recursion, compared to mergesort's O(n) extra space. It is in-place but not stable."
---

# Quicksort In-Place Space Complexity

Quicksort is an in-place algorithm requiring only O(log n) auxiliary stack space on average, compared to mergesort's O(n) extra space. Hoare's original partition scheme uses two converging pointers and performs approximately n/2 swaps per partition call. Despite being unstable (equal elements may be reordered), quicksort typically outperforms mergesort on arrays due to better cache locality.