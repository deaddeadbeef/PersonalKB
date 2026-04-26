---
id: chunk-csa-186
type: chunk
source: "[[Cormen 2022 - Topological Sort]]"
source_loc: "Kahn Algorithm"
topic: "graphs"
claim: "Kahn's algorithm processes vertices by indegree using a queue, doubling as a cycle detector when fewer than V vertices are output"
confidence: verified
supports:
  - "[[Topological Sort]]"
  - "[[Kahn Algorithm]]"
tags:
  - csa
  - csa/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Graphs — Kahn's BFS topological sort with built-in cycle detection

## Context

Kahn's algorithm initializes a queue with all vertices having indegree 0. It repeatedly dequeues a vertex, outputs it, and decrements the indegree of all its neighbors; any neighbor reaching indegree 0 is enqueued. If the total output count is less than V, the graph contains a cycle (remaining vertices are all part of cycles with nonzero indegree). For lexicographically smallest ordering, replace the FIFO queue with a min-heap, producing the earliest valid ordering in O((V + E) log V).

## Why It Matters

Kahn's algorithm elegantly combines topological sorting with cycle detection in a single pass, and is the more intuitive of the two standard approaches for practical implementation.

## QnA Seeds

- Q: How does Kahn's algorithm detect cycles in a directed graph?
- Q: What modification produces the lexicographically smallest topological sort?
- Q: What is the time complexity of Kahn's algorithm?
