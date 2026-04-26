---
tags: [cs-ds, chunk]
id: chunk-ds-154
source: "[[raw-ds-017]]"
supports: ["[[Fibonacci Heaps]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Fibonacci heaps are rarely used in practice despite optimal theory

## Context
Fibonacci heaps have the best asymptotic bounds for priority queues.

## Claim
Despite optimal O(1) amortized insert and decrease-key, Fibonacci heaps are rarely used because: (1) high constant factors from pointer-rich node structure, (2) poor cache performance from non-contiguous memory, (3) implementation complexity with 5+ pointer fields per node.

## Why It Matters
Classic example of theory vs practice gap. Binary heaps and pairing heaps are almost always faster.

## QnA Seeds
- Q: Why poor cache performance? -> A: Nodes scattered in memory with 5+ pointers each causing cache misses on every operation.
- Q: What do practical systems use? -> A: Binary heap or pairing heap. d-ary heaps for Dijkstra.
