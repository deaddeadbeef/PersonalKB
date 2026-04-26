---
id: chunk-csa-159
type: chunk
source: "[[Halim 2013 - Segment Trees]]"
source_loc: "Fenwick Tree"
topic: "data-structures"
claim: "Fenwick tree (BIT) supports point update and prefix query in O(log n) using O(n) space with simpler code than segment trees, but limited to invertible operations"
confidence: verified
supports:
  - "[[Fenwick Tree]]"
  - "[[Range Query Data Structures]]"
tags:
  - csa
  - csa/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Data Structures — Fenwick tree O(log n) prefix sums with minimal overhead

## Context

A Fenwick tree (Binary Indexed Tree) uses the binary representation of indices to efficiently compute prefix sums. Update at index i affects positions i, i + LSB(i), i + LSB(i) + LSB(...), where LSB(i) = i & (-i). It requires only O(n) space and supports O(log n) point updates and prefix queries with significantly less code and memory overhead than a segment tree. However, Fenwick trees are limited to operations with inverses (like addition, where range [l, r] = prefix(r) - prefix(l-1)) and cannot natively support arbitrary range queries or non-invertible aggregates like min/max.

## Why It Matters

Fenwick trees are the practical choice when only prefix-sum operations are needed, offering better constants and simpler implementation than segment trees for this common use case.

## QnA Seeds

- Q: How does the LSB (least significant bit) trick enable Fenwick tree operations?
- Q: Why can't Fenwick trees natively support range minimum queries?
- Q: When should you choose a Fenwick tree over a segment tree?
