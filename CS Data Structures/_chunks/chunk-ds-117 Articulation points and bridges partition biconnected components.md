---
tags: [cs-ds, chunk]
id: chunk-ds-117
source: "[[raw-ds-030]]"
supports: ["[[Graphs Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Articulation points and bridges partition biconnected components

## Context
Removing a single vertex or edge can disconnect a graph.

## Claim
Articulation points are vertices whose removal disconnects the graph. Bridges are edges whose removal disconnects it. DFS discovers both in O(V+E) using discovery time and low values enabling biconnected component decomposition.

## Why It Matters
Network reliability analysis: identifying single points of failure in communication networks.

## QnA Seeds
- Q: How to detect articulation point? -> A: Non-root vertex v is articulation if any child has low value >= discovery of v.
- Q: What is a biconnected component? -> A: Maximal subgraph with no articulation points. Two vertex-disjoint paths between any pair.
