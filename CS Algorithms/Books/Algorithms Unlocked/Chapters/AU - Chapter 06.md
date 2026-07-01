---
id: au-ch-06
type: book-chapter
chapter: 6
book: "Algorithms Unlocked"
author: "Thomas H. Cormen"
status: processed
chunk_count: 3
source: "[[Cormen 2013 - Algorithms Unlocked]]"
tags:
  - csa
  - book-chapter
up: "[[CS Algorithms/Books/Algorithms Unlocked/Chapter Index|Chapter Index]]"
confidence: established
freshness: stable
tier-coverage: [core]
---
# AU — Chapter 06: Shortest Paths

## Summary

Chapter 6 extends shortest-path finding from acyclic graphs (Chapter 5) to general directed graphs with cycles. Three landmark algorithms address different problem variants. **Dijkstra's algorithm** solves single-source shortest paths when all edge weights are non-negative: a priority queue repeatedly extracts the vertex with the smallest current distance estimate and relaxes its outgoing edges. Once extracted, a vertex is finalised — non-negative weights ensure no later edge can improve it. Time $O((n+m)$ lg n) with a binary heap. **Bellman-Ford** handles arbitrary weights including negatives by relaxing all m edges in n−1 passes; after pass k, shortest paths using ≤ k edges are correct. A negative-weight cycle is detected if any distance still decreases on pass n. Time $O(nm)$. Bellman-Ford also detects **arbitrage** opportunities in currency exchange (negative-weight cycle in a log-cost graph). **Floyd-Warshall** solves all-pairs shortest paths via a DP on intermediate vertex sets: shortest[u,v,x] = min cost from u to v using only vertices 1..x as intermediates. The $\Theta(n³)$ triple loop fills an n×n table. All three algorithms share the **relaxation** primitive first seen in Chapter 5.

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| Negative-weight cycle | Cycle with total weight < 0; makes shortest path undefined |
| Dijkstra | Greedy; non-negative weights; $O((n+m)$ lg n) with binary heap |
| Bellman-Ford | Relaxes all edges n−1 times; handles negatives; detects negative cycles; $O(nm)$ |
| Floyd-Warshall | All-pairs DP on intermediate vertices; $\Theta(n³)$ |
| Relaxation | If d[u]+w(u,v) < d[v]: update d[v] and predecessor |
| Arbitrage detection | Negative-weight cycle in log-transformed currency exchange graph |

## Chunk Candidates

- [x] [[Graphs - Dijkstra's greedy approach requires non-negative edge weights]]
- [x] [[Graphs - Bellman-Ford handles negative weights and detects negative cycles]]
- [x] [[Graphs - Floyd-Warshall solves all-pairs shortest paths in Theta(n cubed)]]

## Wiki Pages Seeded

- [[Dijkstra's Algorithm]] — full algorithm, complexity, correctness requirement
- [[Bellman-Ford Algorithm]] — procedure, negative-cycle detection, arbitrage
- [[Floyd-Warshall Algorithm]] — DP formulation and $\Theta(n³)$ analysis

## References

See [[CS Algorithms/Sources/Sources Index#Cormen 2013|Cormen 2013]].
