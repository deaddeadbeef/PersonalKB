---
id: chunk-csa-011
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 5"
topic: "graphs"
claim: "Kahn's topological sort algorithm processes vertices in precedence order by repeatedly removing in-degree-0 vertices in Theta(n+m)"
confidence: verified
supports:
  - "[[DAG and Topological Sort]]"
  - "[[Graph Fundamentals]]"
tags:
  - csa
  - csa/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Graphs — DAG topological sort processes vertices in precedence order in Theta(n+m)

## Context

Kahn's algorithm: maintain a queue of vertices with in-degree 0; repeatedly dequeue a vertex u, append it to the topological order, and for each neighbour v of u, decrement v's in-degree (removing u's dependency); if v's in-degree drops to 0, enqueue it. If all vertices are processed, the output is a valid topological order. If the queue empties before all vertices are processed, a cycle exists. Each vertex and edge is processed once: Θ(n+m).

## Why It Matters

Topological sort underlies many scheduling problems: build system dependency resolution, compiler analysis, course prerequisite ordering, PERT project planning. The linear-time complexity means it scales to large dependency graphs without issue. Cycle detection as a side effect is a useful free diagnostic.

## QnA Seeds

- Q: How does Kahn's algorithm detect a cycle in a directed graph?
- Q: What does it mean for a topological ordering to be valid?
- Q: Why is topological sort only possible on directed acyclic graphs?
