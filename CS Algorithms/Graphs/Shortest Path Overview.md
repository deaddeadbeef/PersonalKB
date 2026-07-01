---
tags:
  - csa
  - csa/graphs
confidence: verified
freshness: stable
up: '[[CS Algorithms/Graphs/Graphs Overview|Graphs Overview]]'
tier-coverage: [intuition, core, deep-dive, practice]
---
# Shortest Path Overview

> **One-line summary**: Shortest-path algorithms find minimum-weight paths in weighted graphs, varying by single-source vs all-pairs, weight constraints, and graph structure.

## 🎯 Intuition
**The Core Idea:** Find the cheapest route between vertices in a weighted graph, just like GPS finds the fastest driving route.
**Analogy:** GPS routing — your navigation app explores possible roads, always extending the cheapest partial route first (Dijkstra), or checking all roads repeatedly for toll-road discounts that could make a longer path cheaper (Bellman-Ford).
**Why It Matters:** Shortest-path algorithms power network routing (OSPF), GPS navigation, logistics optimisation, and any system that needs to minimise cost across a graph.

---

## ⚙️ Core Mechanics
### How It Works / Formal Definition
A **shortest path** from vertex s to vertex t in a weighted graph is a path whose total edge weight is minimised. All main SSSP algorithms use a shared **relaxation** primitive:

```
RELAX(u, v, w):
  if d[u] + w(u,v) < d[v]:
    d[v] = d[u] + w(u,v)
    pred[v] = u
```

The algorithms differ in the order they apply relaxation:
- **Dijkstra**: relax in order of current shortest distance (greedy)
- **Bellman-Ford**: relax all edges n𢄡 times (brute force)
- **DAG**: relax in topological order (one pass suffices)

### Key Properties

| Property | Detail |
|----------|--------|
| **Optimal substructure** | Any subpath of a shortest path is itself a shortest path |
| **No-cycle property** | Shortest paths in graphs without negative cycles contain no cycles |
| **Predecessor subgraph** | Shortest-path predecessors form a tree rooted at the source |

### Key Facts
- **Problem variants**: single-source (SSSP), single-pair, all-pairs (APSP), single-destination (reverse edges + SSSP)
- **Negative edges**: Dijkstra fails; Bellman-Ford and Floyd-Warshall handle them
- **Negative cycles**: make shortest paths undefined — both Bellman-Ford and Floyd-Warshall detect them

### Algorithm Selection Guide

| Algorithm | Weights | Negative cycles? | Time | Best for |
|-----------|---------|-----------------|------|---------|
| [[Dijkstra's Algorithm]] | Non-negative only | Cannot handle | $O((n+m)$ lg n) | Sparse graphs, GPS routing, OSPF |
| [[Bellman-Ford Algorithm]] | Any (including negative) | Detects | $O(nm)$ | Negative weights; checks negative cycles |
| DAG Shortest Paths | Any (DAG only) | N/A (no cycles in DAG) | $\Theta(n+m)$ | Precedence-constrained scheduling |
| [[Floyd-Warshall Algorithm]] | Any | Detects (via diagonal) | $\Theta(n³)$ | All-pairs; dense graphs; moderate n |
| Dijkstra × n | Non-negative | Cannot handle | $O(n(n+m)$ lg n) | All-pairs on sparse non-negative graphs |

---

## 🔬 Deep Dive
### Proofs / Formal Arguments
**Optimal substructure proof**: If subpath p′ of shortest path p were not shortest, replacing p′ with a shorter alternative would reduce total weight of p — contradicting p being shortest. □

**Relaxation correctness**: After sufficient relaxations, d[v] = δ(s,v) for all reachable v. Dijkstra achieves this in $O((n+m)$ lg n) via a greedy cut invariant; Bellman-Ford in $O(nm)$ by brute-force iteration; DAG relaxation in $\Theta(n+m)$ via topological order.

### Edge Cases and Pitfalls
- **Dijkstra with negative edges**: a negative edge can shorten a path to an already-finalised vertex, violating the greedy invariant
- **Disconnected vertices**: d[v] remains ∞ if v is unreachable from s
- **Negative-weight cycles**: traversing the cycle repeatedly yields arbitrarily negative cost — shortest path is undefined
- **Floyd-Warshall cycle detection**: D[v][v] < 0 after completion ⟹ v lies on a negative cycle

### Real-World Implications
- **Network routing (OSPF)**: uses Dijkstra with link-state costs
- **GPS / map navigation**: Dijkstra or A* on road graphs
- **Currency arbitrage detection**: Bellman-Ford on log-transformed exchange rates detects negative cycles (profitable arbitrage loops)
- **Project scheduling**: DAG shortest/longest paths for critical path analysis

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why does Dijkstra fail on graphs with negative edge weights? Give a two-vertex counterexample.
2. What does it mean for a graph to have a negative-weight cycle? Why does this make shortest paths undefined?
3. In what order does DAG shortest-paths apply relaxation, and why is one pass sufficient?

### Core Problems
1. Given a weighted directed graph with some negative edges but no negative cycles, which algorithm would you choose for single-source shortest paths? Justify the time complexity.
2. Prove that the relaxation operation maintains the invariant d[v] ≥ δ(s,v) throughout Dijkstra's algorithm.

### Challenge
1. Design an algorithm to find shortest paths from a single source in a graph where exactly one edge has a negative weight (no negative cycles). Can you beat $O(nm)$?

---

*See also:* [[Dijkstra's Algorithm]], [[Bellman-Ford Algorithm]], [[Floyd-Warshall Algorithm]], [[DAG and Topological Sort]], [[CS Algorithms/Graphs/Graphs Overview|Graphs Overview]]

## Supporting Chunks

- [[Graphs - Dijkstra's greedy approach requires non-negative edge weights]]
- [[Graphs - Dijkstra's algorithm maintains a cut invariant that guarantees correctness on non-negative graphs]]
- [[Graphs - Bellman-Ford handles negative weights and detects negative cycles]]
- [[Graphs - DAG shortest paths use topological-order relaxation handling negative weights]]
- [[Graphs - Floyd-Warshall solves all-pairs shortest paths in Theta(n cubed)]]
- [[Graphs - Floyd-Warshall negative-cycle detection uses the diagonal of the distance matrix]]

## References

See [[CS Algorithms/Sources/Sources Index#Cormen 2013|Cormen 2013]], Chapter 6. See [[CS Algorithms/Sources/Sources Index#Erickson 2019|Erickson 2019]], Chapter 8𠄹. See [[Dijkstra's Algorithm]], [[Bellman-Ford Algorithm]], [[Floyd-Warshall Algorithm]], and [[DAG and Topological Sort]] for individual algorithm pages.
