---
id: chunk-csa-013
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 6"
topic: "graphs"
claim: "Bellman-Ford relaxes all edges n-1 times to handle negative weights and detects negative-weight cycles on pass n"
confidence: verified
supports:
  - "[[Bellman-Ford Algorithm]]"
  - "[[Shortest Path Overview]]"
tags:
  - csa
  - csa/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Graphs — Bellman-Ford handles negative weights and detects negative cycles in O(nm)

## Context

Bellman-Ford relaxes every edge (u,v) in n−1 passes. After pass k, d[v] is optimal if the true shortest path uses at most k edges. Any shortest path in a graph with n vertices has at most n−1 edges (otherwise a vertex repeats, implying a cycle). Run a final (nth) pass: if any d[v] still decreases, a negative-weight cycle is reachable from the source. Running time O(nm) — far slower than Dijkstra but handles negative weights and provides cycle detection. Applied to currency arbitrage: represent each currency exchange as an edge in a log-cost graph; a negative-weight cycle signals an arbitrage opportunity.

## Why It Matters

Bellman-Ford completes the coverage of shortest-path problems: it handles what Dijkstra cannot. Its O(nm) complexity is acceptable for moderate graph sizes. The arbitrage application is a compelling real-world example of why negative-weight shortest paths matter practically.

## QnA Seeds

- Q: Why does Bellman-Ford need exactly n-1 relaxation passes?
- Q: How does Bellman-Ford detect a negative-weight cycle?
- Q: How does Bellman-Ford apply to currency arbitrage detection?
