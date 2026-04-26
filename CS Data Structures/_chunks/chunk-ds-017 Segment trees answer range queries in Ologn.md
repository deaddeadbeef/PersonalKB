---
tags: [cs-ds, chunk]
id: chunk-ds-017
source: "[[raw-ds-013]]"
supports: ["[[Segment Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Segment trees answer range queries in Ologn with lazy propagation

## Context
Range queries on mutable arrays naively take O(n).

## Claim
Segment trees store range aggregates in a binary tree, answering range queries and supporting point updates in O(log n), with lazy propagation extending to O(log n) range updates.

## Why It Matters
Most versatile structure for range query problems in competitive programming and databases.

## QnA Seeds
- Q: How does lazy propagation work? -> A: Mark nodes pending; push computation down only when needed.
- Q: Segment tree vs Fenwick? -> A: Segment for non-commutative or range updates; Fenwick for simpler prefix sums.
