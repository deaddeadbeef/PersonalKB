---
tags: [cs-ds, chunk]
id: chunk-ds-038
source: "[[raw-ds-030]]"
supports: ["[[Adjacency List and Adjacency Matrix]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# BFS finds shortest unweighted paths by exploring level by level

## Context
Finding shortest paths in unweighted graphs is a fundamental problem.

## Claim
BFS explores vertices in order of distance from the source, guaranteeing that the first time a vertex is reached it is via a shortest path, using O(V+E) time and O(V) space.

## Why It Matters
Foundation for network analysis, social graph distance, puzzle solving, and web crawling.

## QnA Seeds
- Q: Why does BFS find shortest paths? -> A: It explores all vertices at distance d before any at distance d+1.
- Q: What data structure does BFS use? -> A: A queue (FIFO).
