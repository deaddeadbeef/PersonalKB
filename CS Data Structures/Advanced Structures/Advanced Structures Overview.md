---
tags:
  - cs-ds
  - hub
up: "[[CS Data Structures]]"
---

# Advanced Structures Overview

Some problems demand more than a sorted map or a priority queue. Range-sum queries over a mutable array, nearest-neighbour search in high-dimensional space, and tracking connected components under a stream of union operations each call for a specialised structure. This hub gathers data structures that go beyond the introductory canon — structures that appear in competitive programming, computational geometry, databases, and systems research.

## Skip Lists and Union-Find

A **skip list** layers multiple sorted linked lists with probabilistic express lanes, achieving expected $O(\log n)$ search, insert, and delete with a remarkably simple implementation — no rotations, no recolouring. It serves as a practical alternative to balanced BSTs in concurrent settings where fine-grained locking is easier on a list than on a tree. **Disjoint sets (union-find)** maintain a partition of elements into groups, supporting near-$O(1)$ amortised union and find through path compression and union by rank. Union-find is indispensable in Kruskal's MST algorithm, image segmentation, and network connectivity.

## Range Query Structures

**Segment trees** answer arbitrary range queries — sum, minimum, GCD — over an array in $O(\log n)$ time and support point or range updates with lazy propagation. **Fenwick trees (binary indexed trees)** offer a more space-efficient solution for prefix-sum and point-update workloads, using clever bit manipulation to navigate an implicit tree stored in a flat array. **Interval trees** and **range trees** extend the concept to overlapping intervals and multi-dimensional orthogonal queries, powering calendar scheduling and computational geometry algorithms.

## Spatial Data Structures

When data lives in two or more dimensions, **k-d trees** recursively partition space along alternating axes, enabling efficient nearest-neighbour and range searches that underpin geographic information systems, ray tracing, and machine-learning classifiers such as k-NN.

## Caching and Eviction Structures

**LRU (Least Recently Used)** and **LFU (Least Frequently Used)** caches combine hash tables with doubly linked lists or frequency-indexed bucket lists to achieve $O(1)$ eviction and lookup — essential building blocks in CPU caches, web proxies, and database buffer pools.

## Memory-Hierarchy and Systems Structures

Some structures are designed not for a specific query type but for a specific hardware reality. **Cache-oblivious structures** achieve optimal cache performance without knowing cache-line sizes, delivering portable efficiency across hardware. **External memory structures** (such as B-tree variants and buffer trees) minimise disk I/O by batching reads and writes in blocks. **Concurrent data structures** use fine-grained locking, lock-free algorithms, or transactional memory to support safe parallel access. **Persistent and immutable structures** preserve all prior versions efficiently through path-copying or fat nodes — invaluable in functional programming, version control, and undo systems.

## Pages in This Hub

- [[Skip Lists]]
- [[Disjoint Sets and Union-Find]]
- [[Segment Trees]]
- [[Fenwick Trees]]
- [[Interval Trees and Range Trees]]
- [[k-d Trees and Spatial Data Structures]]
- [[LRU and LFU Caches]]
- [[Cache-Oblivious Structures]]
- [[External Memory Structures]]
- [[Concurrent Data Structures]]
- [[Persistent and Immutable Structures]]

## Related Hubs

- [[Trees Overview]] — foundational tree concepts extended here
- [[Foundational Concepts Overview]] — amortised and worst-case analysis for advanced structures
- [[Graphs Overview]] — union-find and spatial structures applied in graph algorithms
- [[Heaps and Priority Queues Overview]] — priority-based structures complementing range-query tools