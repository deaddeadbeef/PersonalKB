---
tags: [cs-ds, chunk]
id: chunk-ds-157
source: "[[raw-ds-030]]"
supports: ["[[Graphs Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Kosarajus SCC uses two DFS passes on forward and reverse graph

## Context
Alternative to Tarjan's for finding strongly connected components.

## Claim
Kosaraju's algorithm: (1) DFS on original graph recording finish times, (2) DFS on reverse graph in decreasing finish time order. Each DFS tree in step 2 is an SCC. Both passes are O(V+E).

## Why It Matters
Conceptually simpler than Tarjan's. Clearly separates the discovery and component extraction phases.

## QnA Seeds
- Q: Why reverse graph? -> A: Reversing edges preserves SCCs but changes which vertices are reachable from where.
- Q: Why process in reverse finish order? -> A: Ensures each DFS in step 2 stays within one SCC.
