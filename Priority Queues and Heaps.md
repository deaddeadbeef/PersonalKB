---
tags: [cs-ds, heaps]
up: "[[CS Data Structures/Heaps and Priority Queues/Heaps and Priority Queues Overview|Heaps and Priority Queues Overview]]"
confidence: verified
freshness: stable
---

# Priority Queues and Heaps

This note is the navigation entry for the heap and priority queue cluster. Use it to choose the right heap family before drilling into implementation details.

## Selection Guide

- Use [[CS Data Structures/Heaps and Priority Queues/Binary Heaps|Binary Heaps]] as the default: they are simple, array-backed, cache-friendly, and give $O(\log n)$ insert, extract-min, and decrease-key.
- Use [[CS Data Structures/Heaps and Priority Queues/Binomial Heaps|Binomial Heaps]] when merging priority queues is a first-class operation rather than an occasional rebuild.
- Study [[CS Data Structures/Heaps and Priority Queues/Fibonacci Heaps|Fibonacci Heaps]] for amortized analysis and graph-algorithm bounds, especially the theoretical value of $O(1)$ amortized decrease-key.
- Consider [[CS Data Structures/Heaps and Priority Queues/Heap Applications and d-ary Heaps|d-ary heaps]] when the workload is cache-sensitive or decrease-key-heavy; higher branching reduces height but makes sift-down compare more children.

## Cluster Map

- [[CS Data Structures/Heaps and Priority Queues/Heaps and Priority Queues Overview|Heaps and Priority Queues Overview]] — overview of the cluster and its trade-offs
- [[CS Data Structures/Heaps and Priority Queues/Priority Queue ADT|Priority Queue ADT]] — defines the core priority queue operations
- [[CS Data Structures/Heaps and Priority Queues/Binary Heaps|Binary Heaps]] — default array-backed heap implementation
- [[CS Data Structures/Heaps and Priority Queues/Binomial Heaps|Binomial Heaps]] — mergeable heap variant
- [[CS Data Structures/Heaps and Priority Queues/Fibonacci Heaps|Fibonacci Heaps]] — amortized heap variant with fast decrease-key
- [[CS Data Structures/Heaps and Priority Queues/Heap Applications and d-ary Heaps|Heap Applications and d-ary Heaps]] — branching-factor trade-offs and common uses

## Study Order

1. Start with [[CS Data Structures/Heaps and Priority Queues/Priority Queue ADT|Priority Queue ADT]] to separate the interface from implementations.
2. Learn [[CS Data Structures/Heaps and Priority Queues/Binary Heaps|Binary Heaps]] next; most heap reasoning depends on the implicit array layout and bottom-up build-heap.
3. Compare mergeable and amortized variants with [[CS Data Structures/Heaps and Priority Queues/Binomial Heaps|Binomial Heaps]] and [[CS Data Structures/Heaps and Priority Queues/Fibonacci Heaps|Fibonacci Heaps]].
4. Finish with [[CS Data Structures/Heaps and Priority Queues/Heap Applications and d-ary Heaps|Heap Applications and d-ary Heaps]] for applied patterns such as k-way merge, top-k selection, median maintenance, and Dijkstra tuning.

## Supporting Evidence

- [[CS Data Structures/_chunks/chunk-ds-067 Binary heap array layout has implicit parent-child|Binary heap array layout has implicit parent-child links]]
- [[CS Data Structures/_chunks/chunk-ds-068 Build-heap runs in On not Onlogn via bottom-up sift-down|Bottom-up build-heap is O(n)]]
- [[CS Data Structures/_chunks/chunk-ds-037 Binomial heaps support Ologn merge|Binomial heaps support O(log n) merge]]
- [[CS Data Structures/_chunks/chunk-ds-036 Fibonacci heaps achieve O1 amortized decrease-key|Fibonacci heaps achieve O(1) amortized decrease-key]]
- [[CS Data Structures/_chunks/chunk-ds-154 Fibonacci heaps rarely used despite optimal theory|Fibonacci heaps illustrate the theory/practice gap]]

## References

→ [[CS Data Structures/Sources/Sources Index|Sources Index]]
