---
id: chunk-csa-012
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 6"
topic: "graphs"
claim: "Dijkstra's greedy extraction requires non-negative edge weights — a negative edge could improve a finalised vertex"
confidence: verified
supports:
  - "[[Dijkstra's Algorithm]]"
  - "[[Bellman-Ford Algorithm]]"
  - "[[Shortest Path Overview]]"
tags:
  - csa
  - csa/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Graphs — Dijkstra's greedy approach requires non-negative edge weights

## Context

Dijkstra's algorithm maintains a min-priority queue of vertices keyed by their current shortest-path estimate d[v]. When a vertex u is extracted (its estimate is minimal), the algorithm declares d[u] finalised — no future relaxation can improve it. This is correct *only if all edge weights are non-negative*. A negative edge (u,v) with weight −5 could mean that even after u is extracted, some path through a later vertex w → u → v might give a shorter path to v than the one already recorded. With negative weights, use [[Bellman-Ford Algorithm]] instead.

## Why It Matters

The non-negative weight requirement is the single most common pitfall when applying Dijkstra's algorithm. It explains why Bellman-Ford exists as a separate algorithm. Understanding *why* the requirement holds (the greedy-extract step's invariant) is more useful than memorising the constraint.

## QnA Seeds

- Q: Why does Dijkstra's algorithm fail with negative edge weights?
- Q: What is the invariant maintained when Dijkstra extracts a vertex from the priority queue?
- Q: Which algorithm should you use when edge weights can be negative?
