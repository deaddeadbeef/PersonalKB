---
tags:
  - cs-ds
  - hub
up: "[[CS Data Structures]]"
confidence: verified
freshness: stable
---

# Heaps and Priority Queues Overview

A priority queue lets you repeatedly extract the minimum (or maximum) element efficiently — a requirement at the heart of Dijkstra's algorithm, event-driven simulation, OS scheduling, and streaming median computation. The **heap** is the classic structure that fulfils this contract. This hub surveys heap variants from the elementary binary heap to the theoretically optimal Fibonacci heap, highlighting the trade-offs between simplicity, constant factors, and amortised bounds.

## Binary Heaps and the Priority Queue ADT

The **priority queue ADT** specifies insert and extract-min (or max) as its core operations, with decrease-key as a common extension. A **binary heap** implements this ADT in an array with no pointers: the parent of index *i* lives at ⌊i/2⌋, giving $O(\log n)$ insert and extract-min with superb cache locality. Building a heap from an unsorted array takes only $O(n)$ via the bottom-up *heapify* procedure — a result that often surprises newcomers.

## Mergeable and Amortised Heaps

When workloads require merging two priority queues, binary heaps fall short at $O(n)$. **Binomial heaps** solve this with a forest of binomial trees, supporting $O(\log n)$ merge, insert, and extract-min. **Fibonacci heaps** push further: $O(1)$ amortised insert and decrease-key make them theoretically ideal for graph algorithms like Prim's and Dijkstra's, though their pointer-heavy structure and large constants limit practical adoption. Understanding the potential-method analysis behind Fibonacci heaps is an excellent exercise in amortised reasoning.

## Generalised and Applied Heaps

**d-ary heaps** generalise the binary heap by giving each node *d* children, reducing tree height at the cost of costlier sift-down comparisons — a worthwhile trade-off when decrease-key dominates. Beyond stand-alone use, heaps power heapsort, efficient median maintenance with two heaps, and priority-based scheduling in real-time systems.

## Pages in This Hub

- [[Binary Heaps]]
- [[Priority Queue ADT]]
- [[Binomial Heaps]]
- [[Fibonacci Heaps]]
- [[Heap Applications and d-ary Heaps]]

## Related Hubs

- [[Foundational Concepts Overview]] — amortised analysis central to Fibonacci and binomial heaps
- [[Trees Overview]] — heaps as a specialised form of complete binary tree
- [[Linear Structures Overview]] — array representation underlying binary heaps
- [[CS Data Structures/Graphs/Graphs Overview|Graphs Overview]] — shortest-path algorithms that depend on efficient decrease-key

## References

→ [[CS Data Structures/Sources/Sources Index|Sources Index]]
