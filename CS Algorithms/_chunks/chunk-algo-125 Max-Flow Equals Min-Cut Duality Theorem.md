---
id: chunk-algo-125
type: chunk
source: "[[raw-algo-022]]"
source_loc: "Network Flow - Key Claims"
topic: "network-flow"
claim: "The max-flow min-cut theorem (Ford-Fulkerson, 1956) states that maximum s-t flow value equals minimum s-t cut capacity, providing an optimality certificate and fundamental duality in combinatorial optimization."
confidence: verified
supports:
  - "[[Network Flow]]"
  - "[[Max-Flow Min-Cut]]"
tags:
  - cs-algorithms
  - cs-algorithms/network-flow
  - chunk
up: "[[CS Algorithms]]"
---
# Max-Flow Equals Min-Cut Duality Theorem

## Context

A cut (S,T) partitions vertices with s in S, t in T; capacity = sum of edge capacities from S to T. Three equivalent conditions: (1) f is max flow, (2) residual graph has no s-t augmenting path, (3) |f| equals some cut capacity. The proof uses flow conservation: any flow is bounded by any cut capacity (weak duality), and Ford-Fulkerson termination gives equality (strong duality). The integrality theorem guarantees integer max-flow for integer capacities.

## Why It Matters

Max-flow min-cut is one of the most important duality results in combinatorial optimization, underpinning network design, bipartite matching, and minimum-cost flow.

## QnA Seeds

- Q: What does the max-flow min-cut theorem state?
- Q: What three conditions are equivalent for maximum flow?
- Q: Why does the integrality theorem matter?