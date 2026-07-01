---
tags:
  - cs-ds
  - hub
up: "[[CS Data Structures]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, navigation]
---

# Graphs Overview

> **One-line summary**: Graphs model pairwise relationships, and the data-structure choice determines whether traversal, edge queries, updates, and storage scale well.

## Core Idea

Graphs model pairwise relationships: friendships in a social network, roads between cities, prerequisites in a build system, or states connected by legal moves. A graph is a set of **vertices** connected by **edges**, but the useful implementation question is more specific: how will the program store neighbors, test edge existence, attach direction or weights, and avoid materializing impossible-to-store state spaces?

The default representation for sparse traversal-heavy graphs is the **adjacency list**, which stores only realized edges and uses $O(V + E)$ space. An **adjacency matrix** uses $O(V^2)$ space but gives $O(1)$ edge-existence queries, making it attractive for dense graphs or algorithms that repeatedly ask whether an edge exists. **Edge lists**, **CSR/CSC**, and **implicit neighbor generators** cover edge-centric, cache-sensitive, and state-space workloads.

## Representation Decision Guide

| If the graph workload mostly needs... | Start with... | Why |
| --- | --- | --- |
| BFS, DFS, Dijkstra, topological sort, or sparse traversal | [[Adjacency List and Adjacency Matrix|Adjacency list]] | Neighbor iteration costs $O(\deg(v))$ and storage is $O(V + E)$. |
| Constant-time edge queries or dense all-pairs algorithms | [[Adjacency List and Adjacency Matrix|Adjacency matrix]] | Edge lookup is $O(1)$, trading speed for $O(V^2)$ space. |
| Sorting or streaming edges, such as Kruskal-style processing | [[Graph Representations Overview|Edge list]] | A flat edge array is compact and easy to sort, but poor for repeated neighbor lookup. |
| One-way links, costs, capacities, or dependencies | [[Weighted and Directed Graphs]] | Direction and weights change valid algorithms and storage details. |
| Huge static graphs or generated state spaces | [[Implicit and Compressed Graph Representations]] | CSR/CSC compress explicit graphs; implicit graphs compute neighbors on demand. |

## Terminology First

Before choosing algorithms, pin down the graph's structural promises: directed vs undirected, weighted vs unweighted, connected vs disconnected, cyclic vs acyclic, simple graph vs multigraph, and sparse vs dense. These properties determine whether a graph can be treated as a tree, topologically sorted as a DAG, searched by BFS/DFS, or decomposed into strongly connected components.

## Pages in This Hub

- [[Graph Representations Overview]] - broad map of adjacency lists, matrices, edge lists, and hybrids.
- [[Adjacency List and Adjacency Matrix]] - detailed operations and complexity trade-offs for the two workhorse structures.
- [[Weighted and Directed Graphs]] - direction, weights, DAGs, SCCs, and shortest-path implications.
- [[Graph Properties and Terminology]] - vocabulary for degree, paths, cycles, connectivity, bipartiteness, planarity, and trees.
- [[Implicit and Compressed Graph Representations]] - generated neighbors, CSR/CSC, graph databases, and web-scale compression.

## Related Hubs

- [[Foundational Concepts Overview]] - asymptotic analysis and memory/cache trade-offs used throughout graph implementations.
- [[Trees Overview]] - trees as connected acyclic graphs, plus tree-specific traversal and balancing structures.
- [[Hash-Based Structures Overview]] - hash maps and hash sets as adjacency-list backends for fast membership tests.
- [[Advanced Structures Overview]] - disjoint sets, spatial structures, and external-memory structures used in graph problems.

## Supporting Chunks

- [[CS Data Structures/_chunks/chunk-ds-019 Adjacency lists dominate for sparse graphs|Adjacency lists dominate for sparse graphs]]
- [[CS Data Structures/_chunks/chunk-ds-094 Adjacency matrix enables O1 edge queries but wastes space|Adjacency matrices enable O(1) edge queries but waste space]]
- [[CS Data Structures/_chunks/chunk-ds-127 Edge list is simplest graph representation|Edge lists are the simplest graph representation]]
- [[CS Data Structures/_chunks/chunk-ds-076 CSR stores graphs in flat arrays for cache efficiency|CSR stores graphs in flat arrays for cache efficiency]]
- [[CS Data Structures/_chunks/chunk-ds-040 Tarjans SCC finds all strongly connected components in one DFS|Tarjan's SCC finds strongly connected components in one DFS]]
- [[CS Data Structures/_chunks/chunk-ds-157 Kosarajus SCC uses two DFS on forward and reverse graph|Kosaraju's SCC uses forward and reverse graph passes]]

## References

-> [[CS Data Structures/Sources/Sources Index|Sources Index]]
