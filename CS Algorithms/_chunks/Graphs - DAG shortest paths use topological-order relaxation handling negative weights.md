---
id: chunk-csa-027
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 5"
topic: "graphs"
claim: "Single-source shortest paths in a DAG can be computed in Θ(n+m) by relaxing edges in topological order, and correctly handles negative edge weights because DAGs contain no cycles"
confidence: verified
supports:
  - "[[DAG and Topological Sort]]"
  - "[[Shortest Path Overview]]"
tags:
  - csa
  - csa/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Graphs — DAG shortest paths use topological-order relaxation handling negative weights

## Context

For a directed acyclic graph with arbitrary (including negative) edge weights, single-source shortest paths are computed as follows: (1) compute a topological ordering of the vertices; (2) initialise dist[s] = 0, dist[v] = ∞ for all other v; (3) process vertices in topological order — for each vertex u, relax all outgoing edges: if dist[u] + w(u,v) < dist[v], update dist[v]. Because the graph is acyclic, when u is processed, all vertices that can reach u have already been processed, so dist[u] is already finalised. There are no back edges, so negative weights cannot create negative-weight cycles. Total time: Θ(n+m) — one pass over all vertices and edges.

## Why It Matters

This algorithm shows that the no-negative-weights restriction of Dijkstra's algorithm is not a fundamental limitation of shortest-path algorithms, but a consequence of using a greedy approach. In a DAG, topological order provides a natural processing sequence that eliminates the need for a priority queue entirely. The Θ(n+m) time is faster than both Dijkstra O((n+m) lg n) and Bellman-Ford O(nm). Recognising when your graph is a DAG is therefore a significant optimisation opportunity.

## QnA Seeds

- Q: Why can DAG shortest paths handle negative edge weights when Dijkstra's algorithm cannot?
- Q: Why is no priority queue needed for DAG shortest paths?
- Q: What is the time complexity advantage of DAG shortest paths over Dijkstra and Bellman-Ford?
