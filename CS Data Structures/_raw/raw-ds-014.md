---
tags: [cs-ds, raw]
source_type: technical_analysis
source_title: "Fenwick Trees"
authors: [Various]
year: 2020
up: "[[Sources Index]]"
---

# Fenwick Trees (Binary Indexed Trees)

## Summary

Fenwick trees compute prefix sums and point updates in O(log n) using bit manipulation. Node i covers range determined by lowest set bit. Query removes lowest bit, update adds lowest bit. O(n) space. Simpler and faster than segment trees for commutative operations. Peter Fenwick, 1994.

## Key Claims

1. O(log n) prefix sum query and point update
2. Bit manipulation determines each node's range
3. Simpler and faster than segment trees in practice
4. Only supports commutative associative operations
5. Range query via prefix(r) - prefix(l-1)

## Atomic Facts

1. Query: while i > 0: sum += tree[i]; i -= i & (-i)
2. Update: while i <= n: tree[i] += delta; i += i & (-i)
3. Space: single array of n+1 elements
4. Fenwick, 1994: A New Data Structure for Cumulative Frequency Tables
5. 2D Fenwick: nested for 2D prefix sums
6. Cannot efficiently support range minimum (non-invertible)

## Significance

Fenwick trees demonstrate how bit-level tricks can yield elegant, efficient solutions with minimal memory overhead.

## Chunks Extracted

*Pending*
