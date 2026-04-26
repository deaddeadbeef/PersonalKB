---
tags: [cs-ds, chunk]
id: chunk-ds-108
source: "[[raw-ds-038]]"
supports: ["[[Heaps and Priority Queues Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Brodal queue achieves O1 insert and decrease-key worst-case

## Context
Fibonacci heaps achieve O(1) amortized. Can we get worst-case?

## Claim
Brodal queue achieves O(1) worst-case insert, find-min, decrease-key, and meld with O(log n) worst-case delete-min. This is theoretically optimal matching the information-theoretic lower bounds.

## Why It Matters
Theoretical breakthrough proving optimal priority queue bounds are achievable. Too complex for practical use.

## QnA Seeds
- Q: Is it practical? -> A: No. The constant factors and implementation complexity are prohibitive.
- Q: What bounds are optimal? -> A: O(1) for everything except delete-min which requires O(log n).
