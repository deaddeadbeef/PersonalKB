---
id: chunk-csa-185
type: chunk
source: "[[Cormen 2022 - Topological Sort]]"
source_loc: "Definition and Existence"
topic: "graphs"
claim: "Topological sort produces a linear ordering of DAG vertices in O(V+E) time; such an ordering exists if and only if the graph has no directed cycles"
confidence: verified
supports:
  - "[[Topological Sort]]"
  - "[[DAG]]"
tags:
  - csa
  - csa/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Graphs — Topological sort orders DAG vertices in O(V+E)

## Context

Topological sorting produces a linear ordering of directed acyclic graph (DAG) vertices such that for every edge (u, v), u appears before v. This exists if and only if the graph is a DAG—any directed cycle makes topological ordering impossible. Two O(V + E) algorithms exist: Kahn's (BFS-based with indegree tracking) and DFS-based (reverse post-order). Multiple valid orderings typically exist; uniqueness implies a Hamiltonian path. Applications span build systems, package managers, course prerequisites, and job schedulers.

## Why It Matters

Topological sort is one of the most practically ubiquitous graph algorithms, underpinning dependency resolution in nearly every software build system and package manager.

## QnA Seeds

- Q: Under what condition does a topological ordering exist for a directed graph?
- Q: What are the two standard algorithms for topological sort?
- Q: When is the topological ordering of a DAG unique?
