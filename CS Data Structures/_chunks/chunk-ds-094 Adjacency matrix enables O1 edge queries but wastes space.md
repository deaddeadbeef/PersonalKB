---
tags: [cs-ds, chunk]
id: chunk-ds-094
source: "[[raw-ds-015]]"
supports: ["[[Adjacency List and Adjacency Matrix]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Adjacency matrix enables O1 edge queries but wastes O(V^2) space

## Context
Edge existence queries are fundamental for graph algorithms.

## Claim
An adjacency matrix stores a V times V boolean array where M[i][j] = 1 means edge i to j. Edge queries are O(1) but space is O(V^2) regardless of edge count making it impractical for sparse graphs.

## Why It Matters
Optimal for dense graphs and matrix-based algorithms like Floyd-Warshall which inherently operate on the full matrix.

## QnA Seeds
- Q: When is adjacency matrix preferred? -> A: Dense graphs or when O(1) edge queries are critical.
- Q: Space for sparse graph with 1M vertices? -> A: 10^12 bits = 125 GB. Clearly impractical.
