---
tags: [cs-ds, study, drill]
up: "[[CS Data Structures Study Index]]"
confidence: verified
freshness: stable
---

# DS Review — Heaps and Priority Queues

Use this drill after reading [[Heaps and Priority Queues Overview]], [[Priority Queue ADT]], [[Binary Heaps]], [[Binomial Heaps]], [[Fibonacci Heaps]], and [[Heap Applications and d-ary Heaps]]. The goal is to choose the right priority-queue representation from the operation mix and connect each operation bound to the structural trick that makes it possible.

## Quick-Fire Questions

1. How is a binary heap stored in an array? What are the parent/child formulas?
2. Why is build-heap $O(n)$ not $O(n \log n)$?
3. What is the key advantage of binomial heaps over binary heaps?
4. Why are Fibonacci heaps rarely used in practice despite optimal bounds?
5. When would a d-ary heap outperform a binary heap?

## Answer Key

1. A [[Binary Heaps|binary heap]] is an implicit complete binary tree in an array. In the common 1-indexed layout, `parent(i) = floor(i/2)`, `left(i) = 2i`, and `right(i) = 2i + 1`; the 0-indexed layout shifts these to `parent(i) = floor((i - 1)/2)`, `left(i) = 2i + 1`, and `right(i) = 2i + 2`.
2. Bottom-up build-heap is $O(n)$ because most nodes are near the leaves and can sift down only a short distance. Summing "nodes at height h times h work" gives a convergent geometric series rather than *n* independent $O(\log n)$ insertions.
3. [[Binomial Heaps|Binomial heaps]] are mergeable: they combine forests of binomial trees in $O(\log n)$ by linking same-order trees, while merging two binary heaps generally requires rebuilding or heapifying at $O(n)$.
4. [[Fibonacci Heaps|Fibonacci heaps]] are important theoretically because insert and decrease-key are $O(1)$ amortized, but their pointer-heavy structure, poor locality, and implementation complexity usually lose to simpler binary or d-ary heaps in practical systems.
5. A [[Heap Applications and d-ary Heaps|d-ary heap]] can win when the workload performs many decrease-key operations relative to extract-min, because larger *d* lowers height to $\log_d n$. The trade-off is that extract-min compares up to *d* children per level, so large *d* only works for the right operation mix.

## Compare and Contrast

| Heap Type | Insert | Extract-Min | Decrease-Key | Merge |
|-----------|--------|-------------|-------------|-------|
| Binary | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ |
| Binomial | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ |
| Fibonacci | $O(1)$* | $O(\log n)$* | $O(1)$* | $O(1)$* |
| d-ary | $O(\log_d n)$ | $O(d \log_d n)$ | $O(\log_d n)$ | $O(n)$ |

*Amortized.

## Decision Prompts

- Default to a [[Binary Heaps|binary heap]] for ordinary priority queues: it is compact, cache-friendly, and simple.
- Prefer [[Binomial Heaps|binomial heaps]] when the operation profile includes frequent heap merges.
- Reach for [[Fibonacci Heaps|Fibonacci heaps]] mainly to understand theoretical graph-algorithm bounds or amortized analysis; use caution for production implementations.
- Consider [[Heap Applications and d-ary Heaps|d-ary heaps]] when decrease-key dominates and the best branching factor can be tuned empirically.

## Supporting Evidence

- [[CS Data Structures/_chunks/chunk-ds-067 Binary heap array layout has implicit parent-child|Binary heap array layout has implicit parent-child links]]
- [[CS Data Structures/_chunks/chunk-ds-068 Build-heap runs in On not Onlogn via bottom-up sift-down|Bottom-up build-heap is O(n)]]
- [[CS Data Structures/_chunks/chunk-ds-037 Binomial heaps support Ologn merge|Binomial heaps support O(log n) merge]]
- [[CS Data Structures/_chunks/chunk-ds-036 Fibonacci heaps achieve O1 amortized decrease-key|Fibonacci heaps achieve O(1) amortized decrease-key]]
- [[CS Data Structures/_chunks/chunk-ds-154 Fibonacci heaps rarely used despite optimal theory|Fibonacci heaps illustrate the theory/practice gap]]

## References

→ [[CS Data Structures/Sources/Sources Index|Sources Index]]
→ [[Heaps and Priority Queues Overview]]
→ [[Binary Heaps]]
→ [[Priority Queue ADT]]
→ [[Binomial Heaps]]
→ [[Fibonacci Heaps]]
→ [[Heap Applications and d-ary Heaps]]
