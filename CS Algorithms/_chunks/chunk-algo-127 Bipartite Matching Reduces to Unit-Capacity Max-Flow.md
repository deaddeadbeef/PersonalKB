---
id: chunk-algo-127
type: chunk
source: "[[raw-algo-022]]"
source_loc: "Network Flow - Key Claims"
topic: "network-flow"
claim: "Maximum bipartite matching reduces to max-flow: super-source to left vertices, right vertices to super-sink, all capacities 1; max-flow value equals maximum matching size, solvable in O(E*sqrt(V)) via Dinic's algorithm."
confidence: verified
supports:
  - "[[Network Flow]]"
  - "[[Bipartite Matching]]"
tags:
  - cs-algorithms
  - cs-algorithms/network-flow
  - chunk
up: "[[CS Algorithms]]"
---
# Bipartite Matching Reduces to Unit-Capacity Max-Flow

## Context

Each unit of flow routes through exactly one left-right edge, and unit capacities ensure each vertex matches at most once. The integrality theorem guarantees integer max-flow. Dinic's achieves O(E*sqrt(V)) on unit-capacity networks, making this the most efficient general bipartite matching approach. The Konig-Egervary theorem further connects maximum matching to minimum vertex cover in bipartite graphs via the min-cut.

## Why It Matters

This reduction demonstrates network flow as a unified modeling framework, linking matching, covering, and scheduling through flow duality.

## QnA Seeds

- Q: How is bipartite matching modeled as max-flow?
- Q: Why do unit capacities ensure one-to-one matching?
- Q: What is bipartite matching complexity via Dinic's?