---
tags: [cs-ds, raw]
id: raw-ds-032
source: "Various (MST literature)"
up: "[[CS Data Structures]]"
---

# Minimum Spanning Tree Structures

## Key Ideas
- MST: subset of edges connecting all vertices with minimum total weight
- Kruskal's: sort edges, greedily add if no cycle — Union-Find is key structure
- Kruskal's complexity: O(E log E) for sort + O(E alpha(V)) for Union-Find ≈ O(E log V)
- Prim's: grow tree from seed, always add cheapest crossing edge — priority queue is key
- Prim's with binary heap: O((V+E) log V)
- Prim's with Fibonacci heap: O(E + V log V)
- Cut property: lightest edge crossing any cut must be in MST
- Cycle property: heaviest edge in any cycle cannot be in MST
- Boruvka's algorithm: parallel-friendly, each component finds cheapest outgoing edge
- MST uniqueness: unique if all edge weights are distinct
- Bottleneck spanning tree: MST minimizes the maximum edge weight
- Dynamic MST: maintain MST under edge insertions/deletions — O(sqrt(V)) amortized per update
- Randomized linear-time MST: Karger-Klein-Tarjan algorithm — O(V+E) expected

## Practical Notes
- Kruskal's + Union-Find is the standard implementation choice for most cases
- Prim's preferred for dense graphs where E >> V
