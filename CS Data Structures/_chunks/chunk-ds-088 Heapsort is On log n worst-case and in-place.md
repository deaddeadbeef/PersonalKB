---
tags: [cs-ds, chunk]
id: chunk-ds-088
source: "[[raw-ds-008]]"
supports: ["[[Binary Heaps and Heapsort]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Heapsort is On log n worst-case and in-place but not stable

## Context
Comparison sorts need O(n log n) lower bound. Quicksort is O(n^2) worst-case.

## Claim
Heapsort achieves O(n log n) worst-case using O(1) extra space by building a max-heap in O(n) then repeatedly extracting max. However it is not stable and has poor cache performance.

## Why It Matters
Guaranteed O(n log n) makes heapsort useful as a fallback. Introsort combines quicksort with heapsort fallback.

## QnA Seeds
- Q: Why not stable? -> A: Heap operations can swap equal elements across the array.
- Q: Why poor cache performance? -> A: Heap sift-down jumps to child at 2i making access patterns irregular.
