---
tags:
  - csa
  - moc
up: "[[CS Algorithms]]"
confidence: established
freshness: stable
tier-coverage: [intuition, core]
---
# Graphs Overview

Graph algorithms model relationships between entities. This domain covers graph vocabulary, ordering via topological sort, and the family of shortest-path algorithms — from single-source to all-pairs, from non-negative to general weights.

---

## Learn in This Order

1. [[Graph Fundamentals]] — vocabulary (vertices, edges, adjacency lists, DAG, in-degree)
2. [[BFS and DFS]] — breadth-first and depth-first traversal; connected components; cycle detection
3. [[DAG and Topological Sort]] — ordering vertices by dependency; PERT critical-path analysis
4. [[Shortest Path Overview]] — algorithm selection guide; SSSP vs APSP; the relaxation primitive
5. ↳ [[Dijkstra's Algorithm]] — greedy; non-negative weights only; $O((n+m)$ lg n)
6. ↳ [[Bellman-Ford Algorithm]] — DP; handles negative weights; detects negative cycles; $O(nm)$
7. ↳ [[Floyd-Warshall Algorithm]] — DP; all-pairs; $\Theta(n³)$; negative-cycle detection via diagonal
8. [[Minimum Spanning Trees]] — MST concept; cut property; when to use Kruskal's vs Prim's
9. ↳ [[Kruskal's Algorithm]] — greedy; sort edges; union-find; $O(m \lg m)$
10. ↳ [[Prim's Algorithm]] — greedy; grow from a vertex; priority queue; $O((n+m)$ lg n)
11. [[Network Flow — Ford-Fulkerson]] — max-flow/min-cut; augmenting paths; residual graphs

---

## In This Domain

| Page | One-line summary |
|------|-----------------|
| [[Graph Fundamentals]] | Core vocabulary; adjacency list vs matrix; DAG definition |
| [[BFS and DFS]] | Traversal strategies; connected components; cycle detection |
| [[DAG and Topological Sort]] | Kahn's algorithm; precedence order; PERT critical path |
| [[Shortest Path Overview]] | Algorithm selection; relaxation; problem variant taxonomy |
| [[Dijkstra's Algorithm]] | Greedy SSSP; cut invariant; requires non-negative weights |
| [[Bellman-Ford Algorithm]] | DP SSSP; handles negative weights; detects negative cycles |
| [[Floyd-Warshall Algorithm]] | DP APSP; $\Theta(n³)$; negative-cycle check via diagonal |
| [[Minimum Spanning Trees]] | MST concept; cut property; algorithm selection |
| [[Kruskal's Algorithm]] | Greedy MST via sorted edges and union-find |
| [[Prim's Algorithm]] | Greedy MST growing from a single vertex |
| [[Network Flow — Ford-Fulkerson]] | Max-flow/min-cut theorem; augmenting paths |

> **Navigating shortest paths:** [[Shortest Path Overview]] is the decision hub — it tells you which algorithm to use and why. Dijkstra, Bellman-Ford, and Floyd-Warshall are the implementations behind that decision.
> **Navigating MST:** [[Minimum Spanning Trees]] is the decision hub for spanning tree problems — it routes you to Kruskal's or Prim's based on graph density and structure.

---

## Common Distinctions

| Question | Answer |
|----------|--------|
| BFS vs DFS? | BFS explores by distance (shortest unweighted path); DFS explores deeply (cycle detection, topological sort). |
| SSSP vs APSP? | Single-source (one start vertex) vs all-pairs (every pair). Use Dijkstra/Bellman-Ford for SSSP; Floyd-Warshall or repeated Dijkstra for APSP. |
| Dijkstra vs Bellman-Ford? | Dijkstra is faster ($O((n+m)$ lg n)) but requires non-negative edge weights. Bellman-Ford handles negatives at $O(nm)$ cost. |
| When to use Floyd-Warshall? | Dense graphs where you need all pairs; also detects negative cycles. |
| Topological sort vs BFS/DFS? | Topo sort is defined only on DAGs; it processes vertices in dependency order, not distance order. |
| Kruskal's vs Prim's? | Kruskal's sorts all edges globally (good for sparse graphs); Prim's grows from one vertex via priority queue (good for dense graphs). |
| When to use network flow? | Bipartite matching, maximum bandwidth, minimum cut — whenever capacity constraints govern throughput. |

---

## How to Navigate

- **New to graphs?** Start at [[Graph Fundamentals]] — every other page assumes this vocabulary.
- **Need to traverse or explore?** [[BFS and DFS]] covers the two fundamental traversal strategies.
- **Choosing a shortest-path algorithm?** Go to [[Shortest Path Overview]] first; it routes you to the right algorithm.
- **Scheduling or dependency problems?** [[DAG and Topological Sort]] covers PERT and task ordering.
- **Need a minimum spanning tree?** Start at [[Minimum Spanning Trees]] to choose between Kruskal's and Prim's.
- **Capacity or flow problems?** [[Network Flow — Ford-Fulkerson]] covers max-flow/min-cut.

---

## Related Domains

- **[[Foundations and Analysis Overview]]** — Bellman-Ford and Floyd-Warshall are DP algorithms; the Master Theorem analysis for graph recursions lives there.
- **[[Greedy Overview]]** — Dijkstra's, Kruskal's, and Prim's are greedy algorithms; the greedy domain explores the paradigm.
- **[[Complexity Theory Overview]]** — graph problems (TSP, clique) are canonical NP-complete benchmarks; Network Flow bridges combinatorial optimization and complexity.

## References

- [[CS Algorithms/Sources/Sources Index]]
- [[CS Algorithms/CS Algorithms Book Reading Spine]]
