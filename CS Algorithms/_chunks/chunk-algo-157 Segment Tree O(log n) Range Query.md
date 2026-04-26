---
id: chunk-csa-157
type: chunk
source: "[[Halim 2013 - Segment Trees]]"
source_loc: "Basic Segment Tree"
topic: "data-structures"
claim: "A segment tree supports point update and range query for any associative aggregate in O(log n) time with O(n) space"
confidence: verified
supports:
  - "[[Segment Tree]]"
  - "[[Range Query Data Structures]]"
tags:
  - csa
  - csa/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Data Structures — Segment tree O(log n) point update and range query

## Context

A segment tree is a binary tree where each leaf stores an array element and each internal node stores an aggregate (sum, min, max, GCD, etc.) of its children's values. The tree has height O(log n) and uses O(n) space (array of size 4n for 1-indexed, 2n for iterative). Range query [l, r] decomposes the range into O(log n) disjoint segments corresponding to tree nodes. Point updates propagate from leaf to root, updating O(log n) ancestors. The build operation runs in O(n) bottom-up. Any associative operation works as the aggregate function.

## Why It Matters

Segment trees are one of the most versatile data structures in competitive programming and practical systems, providing a unified framework for dozens of range query operations.

## QnA Seeds

- Q: Why does range decomposition in a segment tree produce at most O(log n) segments?
- Q: What property must the aggregate function satisfy for a segment tree to be correct?
- Q: What is the space usage of a segment tree for an array of n elements?
