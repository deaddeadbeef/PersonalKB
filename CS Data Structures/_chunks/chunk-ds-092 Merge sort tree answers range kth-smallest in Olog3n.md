---
tags: [cs-ds, chunk]
id: chunk-ds-092
source: "[[raw-ds-013]]"
supports: ["[[Segment Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Merge sort tree answers static range kth-smallest in Olog3n

## Context
Finding the kth smallest in an arbitrary range is harder than range sum.

## Claim
A merge sort tree stores sorted sublists at each segment tree node. Range kth-smallest is answered by binary search on answer combined with counting elements less than candidate in O(log^3 n).

## Why It Matters
Alternative to persistent segment trees with wavelet trees. Simpler to implement for offline queries.

## QnA Seeds
- Q: What is stored at each node? -> A: Sorted array of all elements in that segment.
- Q: Can it handle updates? -> A: Not efficiently. Best for static arrays.
