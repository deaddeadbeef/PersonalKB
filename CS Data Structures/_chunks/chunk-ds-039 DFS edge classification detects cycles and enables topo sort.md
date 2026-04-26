---
tags: [cs-ds, chunk]
id: chunk-ds-039
source: "[[raw-ds-030]]"
supports: ["[[Adjacency List and Adjacency Matrix]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# DFS edge classification detects cycles and enables topological sort

## Context
DFS traversal classifies edges into tree, back, forward, and cross edges.

## Claim
Back edges in DFS indicate cycles in directed graphs; the absence of back edges means the graph is a DAG, and reverse DFS finish order gives a valid topological sort in O(V+E).

## Why It Matters
Topological sort is essential for dependency resolution, build systems, and course scheduling.

## QnA Seeds
- Q: How does DFS detect cycles? -> A: A back edge (pointing to an ancestor) proves a cycle exists.
- Q: How to get topological order? -> A: Reverse the DFS finish-time order.
