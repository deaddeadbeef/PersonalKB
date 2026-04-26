---
id: chunk-csa-187
type: chunk
source: "[[Cormen 2022 - Topological Sort]]"
source_loc: "DFS-based"
topic: "graphs"
claim: "DFS-based topological sort outputs vertices in reverse post-order, correct because every vertex finishes after all descendants in the DFS tree"
confidence: verified
supports:
  - "[[Topological Sort]]"
  - "[[DFS]]"
tags:
  - csa
  - csa/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Graphs — DFS topological sort uses reverse post-order finishing times

## Context

The DFS-based algorithm runs a full depth-first search, appending each vertex to a list upon completion (post-order), then reverses the list. The reversed post-order is a valid topological sort because a vertex is completed only after all vertices reachable from it are completed—so if edge (u, v) exists, u finishes after v and appears earlier in the reversed list. Both Kahn's and DFS approaches run in O(V + E), each processing every vertex and edge exactly once.

## Why It Matters

DFS-based topological sort connects naturally to other DFS applications (SCCs, cycle detection) and is often preferred when DFS is already being used for other analysis on the same graph.

## QnA Seeds

- Q: Why does reverse post-order from DFS produce a valid topological sort?
- Q: How does DFS topological sort handle disconnected DAGs?
- Q: What is the relationship between DFS finishing times and topological order?
