---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-007]]"
confidence: high
supports:
  - "[[Mergesort]]"
  - "[[Sorting Stability]]"
qna_seeds:
  - "Q: Why is mergesort preferred for sorting objects? A: Mergesort is stable—equal elements retain their original relative order—which is critical for multi-key sorting and database applications."
---

# Mergesort Stability Guarantee

Mergesort is a stable sorting algorithm: equal elements retain their original relative order throughout the sort. This property is critical for multi-key sorting and database applications. The merge operation requires O(n) auxiliary space; in-place merge algorithms exist but degrade to O(n log² n) time or have large constant factors, making them impractical.