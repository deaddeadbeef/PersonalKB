---
tags: [cs-ds, chunk]
id: chunk-ds-158
source: "[[raw-ds-039]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# SSTables are immutable sorted files enabling efficient merge

## Context
LSM trees need to combine overlapping data from multiple writes.

## Claim
SSTables (Sorted String Tables) are immutable files of sorted key-value pairs. Their sorted and immutable nature enables O(n+m) merge of two tables via merge-sort-like scan. Index blocks allow binary search within an SSTable.

## Why It Matters
The on-disk building block of LSM trees. Immutability simplifies concurrency and crash recovery.

## QnA Seeds
- Q: Why immutable? -> A: No in-place updates simplifies concurrent reads and crash consistency.
- Q: How is lookup done? -> A: Binary search on index block to find data block then scan within block.
