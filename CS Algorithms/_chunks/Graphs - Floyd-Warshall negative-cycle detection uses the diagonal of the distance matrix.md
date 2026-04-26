---
id: chunk-csa-048
type: chunk
source: "[[Erickson 2019 - Algorithms]]"
source_loc: "Chapter 9 — All-Pairs Shortest Paths"
topic: "graphs"
claim: "Floyd-Warshall detects negative-weight cycles by checking the diagonal of the final distance matrix: D[v][v] < 0 after the algorithm completes means vertex v lies on a negative cycle"
confidence: verified
supports:
  - "[[Floyd-Warshall Algorithm]]"
  - "[[Shortest Path Overview]]"
tags:
  - csa
  - csa/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Graphs — Floyd-Warshall negative-cycle detection uses the diagonal of the distance matrix

## Context

Floyd-Warshall computes D[u][v] = shortest-path distance from u to v using only vertices 1..n as intermediates. In the absence of negative cycles, D[v][v] = 0 for all v (a path of zero edges from v to itself has cost 0, and no cheaper path exists when there are no negative cycles).

**Negative-cycle detection**: After the algorithm completes, check all diagonal entries. If D[v][v] < 0 for some v, then the algorithm found a path from v to v with negative total weight — i.e., v lies on a negative-weight cycle. This check costs O(n) additional time after the Θ(n³) main computation.

**What negative cycles mean for shortest paths**: If vertex v lies on a negative cycle, then any vertex reachable from v (and from which v is also reachable) has no well-defined shortest-path distance — we can make the path arbitrarily short by going around the cycle repeatedly. Floyd-Warshall's main loop may produce meaningless values in D[u][w] for such vertices.

**Contrast with Bellman-Ford detection**: Bellman-Ford detects negative cycles during single-source computation by performing one additional relaxation pass — if any distance improves on pass n, a negative cycle exists. Floyd-Warshall's diagonal test is the all-pairs analogue: compact and O(n) to check.

## Why It Matters

Negative-cycle detection is a required correctness step when using Floyd-Warshall in practice. A graph with a negative cycle often arises in financial modelling (arbitrage detection: can a sequence of currency exchanges produce a profit?). The diagonal test turns Floyd-Warshall into a dual-purpose algorithm — shortest paths *and* negative-cycle detection — with no additional asymptotic cost.

## QnA Seeds

- Q: How does Floyd-Warshall detect negative-weight cycles?
- Q: What does D[v][v] < 0 mean after Floyd-Warshall completes?
- Q: Why are shortest-path distances undefined for vertices on or reachable from a negative cycle?
- Q: What is an application where negative-cycle detection is directly useful?
