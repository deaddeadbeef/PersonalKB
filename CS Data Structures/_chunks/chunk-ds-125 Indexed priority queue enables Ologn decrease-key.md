---
tags: [cs-ds, chunk]
id: chunk-ds-125
source: "[[raw-ds-008]]"
supports: ["[[Binary Heaps and Heapsort]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Indexed priority queue enables O(log n) decrease-key by position tracking

## Context
Standard binary heap has no way to find an element by key efficiently.

## Claim
An indexed priority queue maintains a position array mapping keys to heap indices. This enables O(log n) decrease-key and O(log n) delete by key making it suitable for Dijkstra and Prim algorithms.

## Why It Matters
The practical priority queue for graph algorithms where decrease-key is frequent.

## QnA Seeds
- Q: What extra structure is needed? -> A: Array mapping key to heap position and reverse mapping position to key.
- Q: Why not just use Fibonacci heap? -> A: Indexed binary heap is simpler and faster in practice due to cache effects.
