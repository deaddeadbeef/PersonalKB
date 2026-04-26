---
id: chunk-csa-189
type: chunk
source: "[[Cormen 2022 - Strongly Connected Components]]"
source_loc: "Kosaraju Algorithm"
topic: "graphs"
claim: "Kosaraju's algorithm finds all SCCs in O(V+E) using two DFS passes: first on the original graph for finish times, then on the transposed graph in reverse finish order"
confidence: verified
supports:
  - "[[SCC]]"
  - "[[Kosaraju Algorithm]]"
tags:
  - csa
  - csa/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Graphs — Kosaraju's two-pass DFS for SCCs in O(V+E)

## Context

Kosaraju's algorithm: (1) run DFS on the original graph, recording finish times, (2) transpose the graph (reverse all edges), (3) run DFS on the transposed graph processing vertices in decreasing finish order—each DFS tree in the second pass is one SCC. Correctness relies on the fact that the SCC with the latest finish time in the first DFS is a source component in the condensation DAG. The transposed graph has the same SCCs as the original because mutual reachability is preserved when edges are reversed.

## Why It Matters

Kosaraju's algorithm is conceptually clear and demonstrates the deep relationship between DFS finishing times and the structure of strongly connected components.

## QnA Seeds

- Q: Why does the transposed graph have the same SCCs as the original?
- Q: Why must the second DFS process vertices in decreasing finish order?
- Q: What is the overall time complexity of Kosaraju's algorithm?
