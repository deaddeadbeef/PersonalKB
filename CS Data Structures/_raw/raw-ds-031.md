---
tags: [cs-ds, raw]
id: raw-ds-031
source: "Various (shortest path literature)"
up: "[[CS Data Structures]]"
---

# Shortest Path Data Structures

## Key Ideas
- Dijkstra's algorithm: greedy, non-negative weights, O((V+E) log V) with binary heap
- Priority queue is the key data structure — determines Dijkstra's complexity
- Binary heap: O(log V) decrease-key → O((V+E) log V) total
- Fibonacci heap: O(1) amortized decrease-key → O(V log V + E) total
- Indexed priority queue: binary heap with position array for O(log V) decrease-key
- Bellman-Ford: handles negative weights, O(VE), detects negative cycles
- SPFA (Shortest Path Faster Algorithm): queue-based Bellman-Ford optimization
- Floyd-Warshall: all-pairs shortest paths, O(V^3), DP on adjacency matrix
- Johnson's algorithm: all-pairs via reweighting + V rounds of Dijkstra — O(V^2 log V + VE)
- A* search: Dijkstra + heuristic, optimal with admissible heuristic
- Bidirectional Dijkstra: search from both ends, meets in middle — ~2x speedup in practice
- Contraction hierarchies: preprocess graph for O(log V) queries on road networks

## Data Structure Impact
- Choice of priority queue implementation directly determines shortest path runtime
- For sparse graphs (E ~ V): binary heap is optimal
- For dense graphs (E ~ V^2): Fibonacci heap theoretically better but rarely wins in practice
