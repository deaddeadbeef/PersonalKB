---
tags: [cs-ds, chunk]
id: chunk-ds-019
source: "[[raw-ds-015]]"
supports: ["[[Adjacency List and Adjacency Matrix]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Adjacency lists dominate for sparse graphs with O(V+E) space

## Context
Most real-world graphs are sparse (E much less than V squared).

## Claim
Adjacency lists use O(V+E) space and iterate neighbors in O(deg(v)), making them optimal for sparse graphs which constitute the vast majority of real-world graphs.

## Why It Matters
The choice between list and matrix is one of the most impactful decisions in graph algorithm implementation.

## QnA Seeds
- Q: When to use adjacency matrix? -> A: Dense graphs or when O(1) edge existence queries are critical.
- Q: What is CSR? -> A: Compressed Sparse Row -- flat arrays for cache-efficient static graph storage.
