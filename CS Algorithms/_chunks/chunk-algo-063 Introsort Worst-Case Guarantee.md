---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-006]]"
confidence: high
supports:
  - "[[Quicksort]]"
  - "[[Heapsort]]"
  - "[[Hybrid Sorting]]"
qna_seeds:
  - "Q: How does introsort guarantee O(n log n) worst case? A: It switches from quicksort to heapsort after O(log n) recursion depth, retaining quicksort's practical speed while guaranteeing O(n log n) worst case."
---

# Introsort Worst-Case Guarantee

Introsort (used in C++ std::sort) switches from quicksort to heapsort after O(log n) recursion depth, guaranteeing O(n log n) worst-case time while retaining quicksort's practical speed on average inputs. This hybrid approach eliminates quicksort's O(n²) worst case without sacrificing its superior cache locality and low constant factors on typical inputs.