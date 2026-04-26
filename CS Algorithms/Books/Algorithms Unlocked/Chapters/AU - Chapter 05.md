---
id: au-ch-05
type: book-chapter
chapter: 5
book: "Algorithms Unlocked"
author: "Thomas H. Cormen"
status: processed
chunk_count: 4
source: "[[Cormen 2013 - Algorithms Unlocked]]"
tags:
  - csa
  - book-chapter
up: "[[Chapter Index]]"
---
# AU — Chapter 05: Directed Acyclic Graphs

## Summary

Cormen introduces graphs through a vivid concrete example: putting on hockey goalie equipment in dependency order. The diagram of items with "must go on before" arrows is exactly a **directed acyclic graph (DAG)** — directed edges with no cycles. The chapter establishes graph vocabulary (vertices, edges, adjacency lists, in-degree) and then presents **topological sort** via Kahn's algorithm: repeatedly remove any vertex with no incoming edges and append it to the output. This processes each vertex and edge once, running in $\Theta(n+m)$. If no in-degree-0 vertex exists before all vertices are removed, a cycle is detected. The chapter then applies DAGs to **PERT charts**: tasks are vertices, durations are edge weights, and the **critical path** (longest path) determines the minimum project duration, computed in $\Theta(n+m)$ via a topological-order DP pass. Finally, it shows that single-source shortest paths in a DAG can be computed in $\Theta(n+m)$ even with negative edge weights — relax edges in topological order; no back edges exist so each vertex is finalized before its successors are processed.

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| DAG | Directed graph with no directed cycles |
| Adjacency list | Per-vertex list of neighbours; space-efficient representation |
| In-degree | Number of incoming edges to a vertex |
| Topological sort | Linear ordering of vertices consistent with all directed edges |
| Kahn's algorithm | Repeatedly remove in-degree-0 vertices; $\Theta(n+m)$ |
| PERT / critical path | Longest path in task-duration DAG; project minimum duration |
| Relaxation | If d[u]+w(u,v) < d[v]: update d[v] and predecessor |
| DAG shortest paths | Relax in topological order; $\Theta(n+m)$; handles negative weights |

## Chunk Candidates

- [x] [[Graphs - Graph representation uses adjacency lists for sparse graphs and adjacency matrices for dense graphs]]
- [x] [[Graphs - DAG topological sort processes vertices in precedence order in Theta(n+m)]]
- [x] [[Graphs - PERT critical path is the longest path in a task-duration DAG]]
- [x] [[Graphs - DAG shortest paths use topological-order relaxation handling negative weights]]

## Wiki Pages Seeded

- [[Graph Fundamentals]] — vocabulary and adjacency list
- [[DAG and Topological Sort]] — Kahn's algorithm, PERT

## References

See [[CS Algorithms/Sources/Sources Index#Cormen 2013|Cormen 2013]].
