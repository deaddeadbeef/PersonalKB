---
tags: [cs-ds, chunk]
id: chunk-ds-036
source: "[[raw-ds-029]]"
supports: ["[[Fibonacci Heaps]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Fibonacci heaps achieve O1 amortized decrease-key via lazy cuts

## Context
Binary heaps require O(log n) for decrease-key due to sift-up.

## Claim
Fibonacci heaps achieve O(1) amortized decrease-key by cutting the decreased node from its parent and adding it to the root list, deferring cleanup to extract-min via cascading cuts.

## Why It Matters
This O(1) decrease-key is why Fibonacci heaps give optimal Dijkstra complexity O(V log V + E).

## QnA Seeds
- Q: Why O(1) decrease-key? -> A: Cut node to root list in O(1); cascading cuts amortize to O(1).
- Q: Why is extract-min still O(log n)? -> A: Consolidation merges trees to maintain at most O(log n) roots.
