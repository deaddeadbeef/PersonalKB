---
tags: [cs-ds, chunk]
id: chunk-ds-127
source: "[[raw-ds-015]]"
supports: ["[[Adjacency List and Adjacency Matrix]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Edge list is the simplest graph representation at O(E) space

## Context
Not all algorithms need fast neighbor lookups.

## Claim
An edge list stores graph as array of (u,v,weight) tuples. Space is O(E). Iterating all edges is O(E). Finding neighbors of a vertex is O(E) which is slow but sufficient for Kruskal and Bellman-Ford.

## Why It Matters
Simplest representation. Input format for many graph problems. Optimal for edge-centric algorithms.

## QnA Seeds
- Q: When is edge list sufficient? -> A: Algorithms that iterate all edges like Kruskal and Bellman-Ford.
- Q: How to convert to adjacency list? -> A: Sort by source vertex then build offset array. O(E log E) or O(V+E) with counting sort.
