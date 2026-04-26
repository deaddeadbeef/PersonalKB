---
tags: [cs-ds, raw]
source_type: technical_analysis
source_title: "Segment Trees for Range Queries"
authors: [Various]
year: 2020
up: "[[Sources Index]]"
---

# Segment Trees for Range Queries

## Summary

Segment trees store range aggregates in a binary tree. Point update and range query both O(log n). Build O(n). Lazy propagation enables O(log n) range updates. Persistent variants support versioned queries. Widely used in competitive programming and databases.

## Key Claims

1. Range queries answered in O(log n) after O(n) build
2. Point updates propagate in O(log n)
3. Lazy propagation enables O(log n) range updates
4. Persistent segment trees support versioned queries
5. More flexible than Fenwick trees for non-commutative operations

## Atomic Facts

1. Array-based storage: 4n elements for n-element array
2. Build: O(n) bottom-up construction
3. Query: traverse O(log n) nodes combining partial ranges
4. Lazy propagation: defer updates, push down when accessed
5. 2D segment tree: segment tree of segment trees
6. Applications: range min/max/sum, interval scheduling

## Significance

Segment trees are the go-to structure for range query problems, combining flexibility with guaranteed logarithmic performance.

## Chunks Extracted

*Pending*
