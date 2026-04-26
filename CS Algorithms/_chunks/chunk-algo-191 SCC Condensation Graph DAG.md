---
id: chunk-csa-191
type: chunk
source: "[[Cormen 2022 - Strongly Connected Components]]"
source_loc: "Condensation Graph"
topic: "graphs"
claim: "The condensation graph formed by contracting each SCC into a supernode is always a DAG, enabling topological reasoning about the directed graph's macroscopic structure"
confidence: verified
supports:
  - "[[SCC]]"
  - "[[Condensation Graph]]"
tags:
  - csa
  - csa/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Graphs — SCC condensation graph is always a DAG

## Context

The condensation graph contracts each SCC into a single supernode, with edges between supernodes corresponding to edges between their SCCs in the original graph. This is always a DAG: if two SCCs had a cycle between them, they would be merged into a single SCC by definition. The condensation has at most V vertices and at most E edges. It enables topological sorting on the component level, supporting reachability analysis and structural decomposition of cyclic directed graphs.

## Why It Matters

The condensation graph is the key conceptual tool for understanding directed graph structure—it reduces any directed graph to its acyclic skeleton of strongly connected components.

## QnA Seeds

- Q: Why is the condensation graph always a DAG?
- Q: What can you do with the condensation graph that you can't with the original?
- Q: What are the size bounds of a condensation graph?
