---
id: chunk-algo-122
type: chunk
source: "[[raw-algo-021]]"
source_loc: "Floyd-Warshall - Atomic Facts"
topic: "graphs"
claim: "Floyd-Warshall handles negative edge weights and detects negative-weight cycles: D[i][i] < 0 after completion indicates a negative-cost path from vertex i to itself, checkable in O(V) by inspecting the diagonal."
confidence: verified
supports:
  - "[[Floyd-Warshall Algorithm]]"
  - "[[Shortest Path Overview]]"
tags:
  - cs-algorithms
  - cs-algorithms/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Floyd-Warshall Detects Negative Cycles via Diagonal

## Context

Diagonal entries D[i][i] are initialized to 0. After processing all intermediate vertices, D[i][i] < 0 means a negative-weight cycle through i exists. Any vertex j on such a cycle also has D[j][j] < 0. This detection is a free byproduct of the algorithm, requiring only O(V) additional inspection. Unlike Dijkstra (which requires non-negative weights), Floyd-Warshall naturally handles arbitrary edge weights.

## Why It Matters

Negative-weight cycle detection is critical for financial arbitrage detection, game theory equilibrium analysis, and validating shortest-path solutions. Floyd-Warshall provides this as a free byproduct.

## QnA Seeds

- Q: How does Floyd-Warshall detect negative-weight cycles?
- Q: Why does D[i][i] < 0 indicate a negative cycle?
- Q: What advantage does Floyd-Warshall have over Dijkstra for negative weights?