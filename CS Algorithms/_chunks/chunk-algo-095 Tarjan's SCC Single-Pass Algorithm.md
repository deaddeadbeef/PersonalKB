---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-014]]"
confidence: high
supports:
  - "[[Strongly Connected Components]]"
  - "[[DFS]]"
qna_seeds:
  - "Q: How does Tarjan's algorithm find SCCs in one DFS pass? A: It uses a stack and low-link values; vertex u is an SCC root iff low[u] = disc[u], completing in O(V + E) without needing the transpose graph."
---

# Tarjan's SCC Single-Pass Algorithm

Tarjan's algorithm finds all strongly connected components of a directed graph in a single DFS pass using O(V + E) time. It maintains a stack and low-link array: a vertex u is the root of an SCC if and only if low[u] = disc[u] (its low-link value equals its discovery time). Unlike Kosaraju's algorithm, which requires two DFS traversals and construction of the transpose graph G^T, Tarjan's uses only one pass and no additional graph construction.