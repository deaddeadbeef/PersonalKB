---
tags: [cs-ds, chunk]
id: chunk-ds-018
source: "[[raw-ds-014]]"
supports: ["[[Fenwick Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Fenwick trees use bit manipulation for O(log n) prefix sums

## Context
Prefix sums with point updates need specialized structures.

## Claim
Fenwick trees achieve O(log n) queries and updates using bit manipulation: query removes lowest set bit, update adds it, traversing an implicit tree over the array.

## Why It Matters
Simpler and faster in practice than segment trees for commutative operations like sum and XOR.

## QnA Seeds
- Q: How does lowest set bit determine structure? -> A: Node i covers a range of length equal to its lowest set bit.
- Q: Main limitation? -> A: Only supports commutative associative operations -- min/max are difficult.
