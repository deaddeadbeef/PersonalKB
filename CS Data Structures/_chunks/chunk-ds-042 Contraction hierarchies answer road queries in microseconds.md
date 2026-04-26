---
tags: [cs-ds, chunk]
id: chunk-ds-042
source: "[[raw-ds-031]]"
supports: ["[[Graphs Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Contraction hierarchies answer road network queries in microseconds

## Context
Dijkstra on full road networks is too slow for real-time routing.

## Claim
Contraction hierarchies preprocess the graph by contracting less important nodes, creating shortcut edges. Queries then run bidirectional Dijkstra on the augmented graph in O(log V) effective time.

## Why It Matters
Powers Google Maps, OSRM, and all modern routing engines — million-node graphs queried in microseconds.

## QnA Seeds
- Q: What is node contraction? -> A: Remove a node and add shortcut edges to preserve shortest paths between its neighbors.
- Q: Why bidirectional? -> A: Search from source and target simultaneously, meet at a high-importance node.
