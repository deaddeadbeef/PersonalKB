---
id: chunk-algo-132
type: chunk
source: "[[raw-algo-023]]"
source_loc: "Union-Find - Key Claims"
topic: "graphs"
claim: "Kruskal's MST processes edges by weight, using Union-Find for O(alpha(V)) connectivity tests; total Union-Find cost is O(E*alpha(V)), making overall MST time O(E log E) dominated by edge sorting."
confidence: verified
supports:
  - "[[Union-Find]]"
  - "[[Minimum Spanning Trees]]"
tags:
  - cs-algorithms
  - cs-algorithms/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Kruskal MST Uses Union-Find for O(E alpha V) Checks

## Context

Kruskal iterates sorted edges, adding each if its endpoints are in different components. With V Make-Sets and at most 2E Finds + V-1 Unions, total Union-Find cost is O(E*alpha(V)) ~ O(E) in practice. Edge sorting in O(E log E) = O(E log V) dominates. Without Union-Find, naive component tracking costs O(V) per edge check, giving O(EV) total—far worse for large graphs.

## Why It Matters

Kruskal's is the canonical Union-Find application, illustrating how a near-optimal data structure enables an efficient graph algorithm competitive with Prim's for sparse graphs.

## QnA Seeds

- Q: How does Kruskal use Union-Find?
- Q: What is total Union-Find cost in Kruskal's?
- Q: Why is sorting, not Union-Find, the bottleneck?