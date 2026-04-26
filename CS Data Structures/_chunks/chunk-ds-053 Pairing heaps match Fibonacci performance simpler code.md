---
tags: [cs-ds, chunk]
id: chunk-ds-053
source: "[[raw-ds-038]]"
supports: ["[[Heaps and Priority Queues Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Pairing heaps match Fibonacci heap performance with simpler code

## Context
Fibonacci heaps are theoretically optimal but complex to implement.

## Claim
Pairing heaps are multi-way trees with O(1) insert and O(log n) amortized extract-min, matching Fibonacci heaps empirically while using dramatically simpler code — conjectured O(1) decrease-key.

## Why It Matters
The practical choice when decrease-key performance matters — much simpler than Fibonacci heaps.

## QnA Seeds
- Q: How does pairing heap insert work? -> A: Create singleton and link with root — O(1).
- Q: How does delete-min work? -> A: Remove root, pair children left-to-right, then merge right-to-left.
