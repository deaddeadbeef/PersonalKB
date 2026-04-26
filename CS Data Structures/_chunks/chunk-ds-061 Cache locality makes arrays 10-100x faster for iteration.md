---
tags: [cs-ds, chunk]
id: chunk-ds-061
source: "[[raw-ds-001]]"
supports: ["[[Arrays and Dynamic Arrays]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Cache locality makes arrays 10-100x faster than linked lists for iteration

## Context
Both arrays and linked lists support O(n) iteration.

## Claim
Array elements occupy contiguous memory enabling hardware prefetching and cache line reuse. Linked list nodes are scattered causing cache misses on nearly every access making arrays 10-100x faster for sequential traversal.

## Why It Matters
Big-O notation hides constant factors. Cache effects dominate real-world performance for iteration-heavy workloads.

## QnA Seeds
- Q: Why are arrays faster to iterate? -> A: Contiguous memory means each cache line holds multiple elements.
- Q: When are linked lists still worth it? -> A: When frequent mid-list insertion/deletion outweighs traversal cost.
