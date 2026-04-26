---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-007]]"
confidence: high
supports:
  - "[[Mergesort]]"
  - "[[Timsort]]"
  - "[[Adaptive Sorting]]"
qna_seeds:
  - "Q: How does Timsort achieve O(n) on partially sorted data? A: Timsort uses natural mergesort identifying pre-sorted runs, with insertion sort for small runs (≤ 64 elements) and galloping merge mode."
---

# Timsort Natural Mergesort Optimization

Timsort (used in Python and Java for objects) exploits existing order by identifying pre-sorted runs in the input, achieving O(n) best-case time on partially sorted data. It uses insertion sort for small runs (≤ 64 elements) and a galloping merge mode for efficiently merging runs of different lengths. This natural mergesort approach underpins the adaptive sorting behavior in both Python's sorted() and Java's Arrays.sort() for objects.