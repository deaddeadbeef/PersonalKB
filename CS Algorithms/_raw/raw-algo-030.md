---
tags: [cs-algorithms, raw]
source_type: textbook-chapter
source_title: "Segment Trees and Range Query Data Structures"
authors: [Steven Halim, Felix Halim]
year: 2013
---

## Summary

A segment tree is a binary tree data structure that enables efficient range queries and point updates on an array of n elements. Each leaf stores an array element, and each internal node stores an aggregate (sum, minimum, maximum, GCD, etc.) of its children's values. The tree has height O(log n) and 2n−1 nodes, supporting both point updates and range queries in O(log n) time. For a range query [l, r], the algorithm decomposes the range into O(log n) disjoint segments corresponding to tree nodes, combining their stored values. Point updates propagate changes from a leaf up to the root, updating O(log n) ancestors. Lazy propagation extends segment trees to support range updates in O(log n) time: instead of updating every element in a range individually, a "lazy" tag is stored at a node indicating a pending update to its entire subtree. The tag is propagated to children only when those children are accessed, amortizing the update cost. Common operations enhanced by lazy propagation include range addition, range assignment, and range flip. Segment trees handle any associative operation as the aggregate function, making them extremely versatile. The Fenwick tree (Binary Indexed Tree, BIT) is a simpler alternative for prefix sums: it uses O(n) space, supports point update and prefix query in O(log n), and requires less code and memory than a segment tree. However, BITs are limited to operations with inverses (like addition) and do not natively support arbitrary range queries or range updates, making segment trees the more general choice.

## Key Claims

1. Segment trees support point update and range query for any associative aggregate function in O(log n) time, with O(n) space.
2. Lazy propagation enables O(log n) range updates by deferring modifications to subtrees until they are queried, avoiding O(n) per-update cost.
3. Range decomposition in a segment tree splits [l, r] into O(log n) disjoint node ranges, each representing a contiguous subarray—this is the key insight enabling efficient queries.
4. Fenwick trees are simpler and faster in practice for prefix-sum problems but lack the generality of segment trees for arbitrary range operations and non-invertible aggregates.
5. Persistent segment trees enable querying historical versions by sharing structure between versions, using O(log n) additional nodes per update.

## Atomic Facts

1. A segment tree on n elements uses an array of size 4n (for 1-indexed implementation) or 2n (for iterative implementation), stored as a complete binary tree.
2. The build operation runs in O(n) by constructing the tree bottom-up; each internal node computes its value from its two children.
3. Lazy propagation requires a separate lazy array; before accessing a node's children, any pending lazy value is pushed down and the node's lazy tag is cleared.
4. Fenwick trees exploit the binary representation of indices: update at index i affects positions i, i + LSB(i), i + LSB(i) + LSB(i + LSB(i)), etc., where LSB(i) = i & (−i).
5. Merge sort trees store the full sorted subarray at each node, enabling order-statistic queries on ranges in O(log² n) time with O(n log n) space.
6. 2D segment trees (segment tree of segment trees) extend range queries to rectangular regions in O(log² n) time, useful in computational geometry and image processing.

## Significance

Segment trees are one of the most versatile data structures in competitive programming and practical algorithm design. They provide a unified framework for range queries across dozens of aggregate functions, from simple sums to complex operations like range GCD or range mode. Lazy propagation makes them suitable for problems requiring both queries and updates on ranges, common in database systems, real-time analytics, and interval scheduling. Fenwick trees serve as the lightweight alternative when only prefix operations are needed. Together, these structures form the backbone of efficient range query processing and appear in implementations of interval trees, orthogonal range searching, and offline query algorithms.

## Chunks Extracted

chunk-algo-157 through chunk-algo-160
