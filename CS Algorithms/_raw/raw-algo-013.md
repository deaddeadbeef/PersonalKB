---
tags: [cs-algorithms, raw]
source_type: textbook
source_title: "Shortest Paths with Negative Weights: Bellman-Ford Algorithm"
authors: "Richard Bellman, Lester Ford Jr."
year: 1958
---

# Bellman-Ford and Negative Weights

## Summary
The Bellman-Ford algorithm computes single-source shortest paths in O(VE) time and, unlike Dijkstra's algorithm, correctly handles graphs with negative-weight edges. It works by performing V − 1 rounds of edge relaxation, after which all shortest-path distances are finalized. A crucial additional capability is negative-cycle detection: if any distance decreases during a Vth relaxation round, the graph contains a negative-weight cycle reachable from the source. This makes Bellman-Ford essential for currency arbitrage detection, network flow algorithms, and any domain where negative weights arise naturally.

## Key Claims
- Bellman-Ford correctly computes shortest paths from a single source in O(VE) time for graphs with negative-weight edges but no negative-weight cycles reachable from the source
- After k rounds of relaxation, the algorithm has found all shortest paths consisting of at most k edges; since any shortest path has at most V − 1 edges (assuming no negative cycles), V − 1 rounds suffice
- Negative-cycle detection is performed by running one additional (Vth) round: if any distance value decreases, a negative cycle exists and shortest paths are undefined for affected vertices
- The Shortest Path Faster Algorithm (SPFA) optimizes Bellman-Ford using a queue of recently updated vertices, achieving O(E) expected time on random graphs but retaining O(VE) worst case
- For DAGs (directed acyclic graphs), shortest paths can be computed in O(V + E) by processing vertices in topological order, since each vertex is visited exactly once

## Atomic Facts
1. Bellman-Ford performs exactly (V − 1) × E relaxation operations in the standard implementation, totaling O(VE); for a graph with V = 10,000 and E = 100,000, this is approximately 999,000,000 operations
2. The algorithm can be optimized to terminate early if no distance update occurs during a complete round; in practice this reduces the average number of rounds, but worst case remains V − 1 rounds
3. SPFA maintains a FIFO queue of vertices whose distances have decreased; each vertex enters the queue at most V − 1 times in the worst case, giving the same O(VE) bound but with significantly better practical performance
4. DAG shortest paths via topological order require exactly one pass through all edges: for each vertex u in topological order, relax all outgoing edges (u, v), yielding O(V + E) time and O(V) space
5. In the context of network flow, Bellman-Ford is used to find augmenting paths in the residual graph with minimum cost (successive shortest paths algorithm for min-cost max-flow), where negative edges represent backward flow
6. Johnson's algorithm for all-pairs shortest paths uses one Bellman-Ford run in O(VE) to compute a potential function h(v) that reweights all edges to be non-negative, then runs V instances of Dijkstra for O(V² log V + VE) total

## Significance
Bellman-Ford fills the critical gap left by Dijkstra's non-negative weight requirement, providing a general-purpose shortest-path algorithm for any weighted graph. Its negative-cycle detection capability has direct applications in financial arbitrage (detecting profitable currency exchange loops), distributed routing (distance-vector protocols like RIP use a distributed form of Bellman-Ford), and network optimization. The DAG shortest-path specialization is a cornerstone of dynamic programming, as any DP recurrence can be viewed as a shortest/longest path problem in the DAG of subproblems. Johnson's algorithm elegantly combines Bellman-Ford and Dijkstra to achieve the best known time for all-pairs shortest paths in sparse graphs.

## Chunks Extracted
*Pending*
