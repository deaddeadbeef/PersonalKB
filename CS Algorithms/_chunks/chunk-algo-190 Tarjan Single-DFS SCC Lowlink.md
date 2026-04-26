---
id: chunk-csa-190
type: chunk
source: "[[Cormen 2022 - Strongly Connected Components]]"
source_loc: "Tarjan Algorithm"
topic: "graphs"
claim: "Tarjan's algorithm finds all SCCs in a single DFS pass using lowlink values and an explicit stack, identifying SCC roots when lowlink equals discovery time"
confidence: verified
supports:
  - "[[SCC]]"
  - "[[Tarjan Algorithm]]"
tags:
  - csa
  - csa/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Graphs — Tarjan's single-DFS SCC algorithm using lowlink values

## Context

Tarjan's algorithm uses a single DFS with a stack and lowlink values. The lowlink of vertex v is the smallest discovery time reachable from v through tree edges and at most one back/cross edge to an ancestor still on the stack. Vertices are pushed onto the stack when discovered. When a vertex's lowlink equals its own discovery time, it is the root of an SCC—all vertices on the stack above it (inclusive) are popped and form that SCC. Tarjan's is generally preferred in practice due to its single-pass nature and avoidance of graph transposition.

## Why It Matters

Tarjan's algorithm is the most efficient and commonly implemented SCC algorithm, requiring only one DFS pass and no graph transposition.

## QnA Seeds

- Q: What does a vertex's lowlink value represent in Tarjan's algorithm?
- Q: How does Tarjan's algorithm identify the root of an SCC?
- Q: Why is Tarjan's algorithm preferred over Kosaraju's in practice?
