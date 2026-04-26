---
tags: [cs-ds, chunk]
id: chunk-ds-040
source: "[[raw-ds-030]]"
supports: ["[[Graphs Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Tarjans SCC algorithm finds all strongly connected components in one DFS

## Context
Finding strongly connected components normally seems to require multiple passes.

## Claim
Tarjan's algorithm uses a single DFS pass with a stack and lowlink values to identify all SCCs in O(V+E) time, where a node's lowlink is the smallest discovery time reachable from its subtree.

## Why It Matters
SCCs decompose directed graphs into a DAG of components — fundamental for program analysis and 2-SAT.

## QnA Seeds
- Q: What is lowlink? -> A: Smallest discovery time reachable from the subtree rooted at this node.
- Q: When is an SCC identified? -> A: When a node's lowlink equals its own discovery time — it is the root of an SCC.
