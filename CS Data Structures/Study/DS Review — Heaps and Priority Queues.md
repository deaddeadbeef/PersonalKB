---
tags: [cs-ds, study, drill]
up: "[[CS Data Structures Study Index]]"
---

# DS Review — Heaps and Priority Queues

## Quick-Fire Questions

1. How is a binary heap stored in an array? What are the parent/child formulas?
2. Why is build-heap $O(n)$ not $O(n \log n)$?
3. What is the key advantage of binomial heaps over binary heaps?
4. Why are Fibonacci heaps rarely used in practice despite optimal bounds?
5. When would a d-ary heap outperform a binary heap?

## Compare and Contrast

| Heap Type | Insert | Extract-Min | Decrease-Key | Merge |
|-----------|--------|-------------|-------------|-------|
| Binary | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ |
| Binomial | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ |
| Fibonacci | $O(1)$* | $O(\log n)$* | $O(1)$* | $O(1)$* |
| d-ary | $O(log_d n)$ | $O(d log_d n)$ | $O(log_d n)$ | $O(n)$ |

*Amortized
