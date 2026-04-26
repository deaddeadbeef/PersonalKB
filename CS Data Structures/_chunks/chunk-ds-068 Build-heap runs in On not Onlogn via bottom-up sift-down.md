---
tags: [cs-ds, chunk]
id: chunk-ds-068
source: "[[raw-ds-008]]"
supports: ["[[Binary Heaps and Heapsort]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Build-heap runs in On not Onlogn via bottom-up sift-down

## Context
Inserting n elements one by one into a heap costs O(n log n).

## Claim
Bottom-up heap construction calls sift-down from the last internal node to the root. Most nodes are near the leaves with short sift distances giving O(n) total by geometric series argument.

## Why It Matters
Makes heapsort and priority queue initialization optimal. The O(n) build is non-obvious and frequently tested.

## QnA Seeds
- Q: Why O(n) not O(n log n)? -> A: Half the nodes are leaves with 0 sift and only 1 root with log n sift.
- Q: Does build order matter? -> A: Must go bottom-up. Top-down insert is O(n log n).
