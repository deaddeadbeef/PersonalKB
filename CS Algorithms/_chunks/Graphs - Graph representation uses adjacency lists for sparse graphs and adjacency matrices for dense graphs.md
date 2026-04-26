---
id: chunk-csa-035
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 5"
topic: "graphs"
claim: "Graphs are represented either as adjacency lists (space Θ(n+m), preferred for sparse graphs) or adjacency matrices (space Θ(n²), used for dense graphs and constant-time edge lookup)"
confidence: verified
supports:
  - "[[Graph Fundamentals]]"
tags:
  - csa
  - csa/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Graphs — Graph representation uses adjacency lists for sparse graphs and adjacency matrices for dense graphs

## Context

Cormen introduces graph representation in Chapter 5 using a dependency graph (putting on goalie equipment in order) as the motivating example. A directed graph G = (V, E) has n = |V| vertices and m = |E| directed edges. Two standard representations are described:

**Adjacency list**: for each vertex u, maintain a list of its out-neighbours. Total space Θ(n + m). Efficient for sparse graphs (m << n²); iteration over a vertex's edges is direct. This is the preferred representation in *Algorithms Unlocked* and underpins topological sort, DAG shortest paths, and PERT.

**Adjacency matrix**: an n × n array where entry (u, v) = 1 (or weight w(u, v)) if edge (u, v) exists, 0 otherwise. Space Θ(n²). Supports constant-time edge lookup; the all-pairs structure suits Floyd-Warshall. Wasteful for sparse graphs.

**In-degree** of a vertex is the count of incoming edges — Kahn's topological sort algorithm identifies source vertices (in-degree 0) to determine the processing order.

## Why It Matters

The representation choice affects how efficiently algorithms traverse edges. With adjacency lists, iterating over all neighbours of a vertex takes time proportional to its actual degree; summed across all vertices, total traversal cost is Θ(m). With an adjacency matrix, finding a vertex's neighbours requires scanning an entire row — Θ(n) per vertex regardless of how many real edges exist, giving Θ(n²) total traversal cost.

For sparse graphs (m ≪ n²) this difference is significant: algorithms such as topological sort, Dijkstra, and Bellman-Ford perform their inner edge-visit steps more efficiently with adjacency lists because only real edges are visited. Floyd-Warshall's all-pairs DP, by contrast, naturally fits the matrix structure. Choosing the representation that matches the graph density and algorithm access pattern is a principled engineering decision.

## QnA Seeds

- Q: What is the space complexity of an adjacency list vs an adjacency matrix for a graph with n vertices and m edges?
- Q: Why does Floyd-Warshall naturally use an adjacency matrix representation?
- Q: What is the in-degree of a vertex and how is it used in topological sort?
