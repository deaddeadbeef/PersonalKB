---
tags: [cs-ds, chunk]
id: chunk-ds-054
source: "[[raw-ds-038]]"
supports: ["[[Binary Heaps and Heapsort]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Leftist heaps enable Ologn merge via right-spine bias

## Context
Binary heaps cannot merge efficiently — requires O(n) rebuild.

## Claim
Leftist heaps bias toward the left: the right spine has length at most O(log n), and merge follows only right spines, giving O(log n) merge, insert, and delete-min.

## Why It Matters
First mergeable heap — conceptual stepping stone to binomial and Fibonacci heaps.

## QnA Seeds
- Q: What is the s-value? -> A: Length of the shortest path from a node to a null descendant.
- Q: Why bias right spine? -> A: Guarantees merge traverses at most O(log n) nodes.
