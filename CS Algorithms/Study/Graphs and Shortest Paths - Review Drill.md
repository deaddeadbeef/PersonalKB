---
tags:
  - csa
  - csa/study
  - csa/graphs
up: "[[Algorithms Study Index]]"
confidence: policy
---
# Graphs and Shortest Paths — Review Drill

Active-recall drill covering graph vocabulary, DAG processing, and all major shortest-path algorithms.

**Canon pages:** [[Graph Fundamentals]] · [[DAG and Topological Sort]] · [[Shortest Path Overview]] · [[Dijkstra's Algorithm]] · [[Bellman-Ford Algorithm]] · [[Floyd-Warshall Algorithm]]

---

## How to Use

Answer each question cold. For algorithm-specific questions, try to state both the correctness argument and the complexity before checking the canonical page.

---

## Core Recall

**Graph Vocabulary**

Q: What is the difference between a directed and an undirected graph?
A: In a directed graph (digraph), each edge has a direction (u → v). In an undirected graph, edges are symmetric — (u, v) and (v, u) are the same edge.

Q: Define in-degree and out-degree for a directed graph.
A: In-degree of v: number of edges directed *into* v. Out-degree of v: number of edges directed *out of* v.

Q: When should you use an adjacency list vs an adjacency matrix?
A: Adjacency list: sparse graphs (m ≪ n²) — $O(n + m)$ space, efficient edge iteration. Adjacency matrix: dense graphs or when you need $O(1)$ edge-existence queries — $O(n²)$ space.

Q: What is a DAG?
A: Directed Acyclic Graph — a directed graph with no cycles. DAGs arise naturally in dependency modelling, task scheduling, and dynamic programming state spaces.

---

**Topological Sort**

Q: What is a topological ordering of a DAG?
A: A linear ordering of vertices such that for every directed edge (u → v), u appears before v. Only possible on DAGs (cycles prevent any such ordering).

Q: Describe the Kahn's algorithm (in-degree–based) for topological sort.
A: 1. Compute in-degree of every vertex. 2. Enqueue all vertices with in-degree 0. 3. Repeatedly dequeue a vertex u, output it, and decrement the in-degree of each successor v; if v's in-degree drops to 0, enqueue v. 4. If all vertices are output, the result is a valid topological order; if not, the graph contains a cycle.

Q: What is the PERT critical path, and which algorithm computes it?
A: The critical path is the longest path in a task-duration DAG, determining the minimum project duration. It is computed as a single-source longest-path problem on the DAG using topological-order relaxation (negate edge weights and run shortest-path, or directly propagate a `dist` array in topological order).

---

**Shortest Path Algorithms — Overview**

Q: What is the relaxation operation?
A: For edge (u, v, w): if dist[u] + w < dist[v], set dist[v] = dist[u] + w. Relaxation never makes a distance estimate larger, only smaller.

Q: Summarise the algorithm selection criteria for shortest paths.

| Scenario | Algorithm |
|----------|-----------|
| Single source, non-negative weights | Dijkstra |
| Single source, negative weights (no negative cycle) | Bellman-Ford |
| Single source, DAG (any weights) | DAG relaxation |
| All-pairs, any weights (no negative cycle) | Floyd-Warshall |

Q: What is a negative cycle, and why is it problematic for shortest paths?
A: A cycle whose total edge weight is negative. Traversing it repeatedly decreases path length without bound, so "shortest path" becomes −∞. Both Bellman-Ford and Floyd-Warshall can *detect* negative cycles but cannot return meaningful shortest-path distances when one exists.

---

**Dijkstra's Algorithm**

Q: State Dijkstra's algorithm's correctness invariant (cut invariant).
A: At each step, for every vertex u in the "settled" set S, dist[u] is the true shortest-path distance from the source. The invariant is maintained because: the next vertex added is the unsettled vertex with minimum tentative distance, and because all weights are non-negative, no future path via unsettled vertices can be shorter.

Q: Why does Dijkstra's algorithm require non-negative edge weights?
A: With a negative edge (u → v, w < 0), settling u and not yet considering v could miss a path that goes through some w' before reaching u, then takes the negative edge to v — yielding a shorter path than the one at the time of settling. Non-negative weights guarantee that relaxation can only improve estimates monotonically.

Q: What is Dijkstra's time complexity?
A: With a binary min-heap: $O((n + m)$ lg n). With a Fibonacci heap: $O(m + n \lg n)$. For sparse graphs the binary-heap version is standard.

---

**Bellman-Ford Algorithm**

Q: Describe the Bellman-Ford algorithm.
A: Relax all m edges exactly n−1 times. After i rounds, dist[v] is the shortest path from source using at most i edges. After n−1 rounds, all simple paths have been considered.

Q: How does Bellman-Ford detect negative cycles?
A: After n−1 relaxation rounds, perform one more round. If any dist[v] value decreases, a negative cycle is reachable from the source — a shorter path exists, which is only possible via a negative cycle.

Q: What is Bellman-Ford's time complexity?
A: $O(nm)$ — n−1 passes each relaxing all m edges.

Q: When must you use Bellman-Ford instead of Dijkstra?
A: When edge weights may be negative (and there are no negative cycles in the paths you want). DAGs with negative weights can also be handled more efficiently by topological-order relaxation, but Bellman-Ford works for general graphs.

---

**Floyd-Warshall Algorithm**

Q: What problem does Floyd-Warshall solve?
A: All-Pairs Shortest Paths (APSP) — the shortest path between every pair of vertices in a weighted directed graph.

Q: State Floyd-Warshall's recurrence.
A: Let D_k[i][j] = shortest path from i to j using only vertices {1, …, k} as intermediates.
- D₀[i][j] = w(i,j) if edge exists, 0 if i=j, ∞ otherwise.
- D_k[i][j] = min(D_{k−1}[i][j], D_{k−1}[i][k] + D_{k−1}[k][j]).
After k = n iterations, D_n[i][j] is the true shortest-path distance.

Q: What is Floyd-Warshall's time complexity?
A: $\Theta(n³)$ — three nested loops each over n vertices.

Q: How do you detect negative cycles with Floyd-Warshall?
A: After the algorithm finishes, check the diagonal: if D[i][i] < 0 for any i, vertex i lies on a negative cycle.

---

## Compare and Contrast

**Dijkstra vs Bellman-Ford**

| Property | Dijkstra | Bellman-Ford |
|----------|---------|-------------|
| Negative weights | ❌ — requires non-negative | ✅ |
| Negative cycle detection | ❌ | ✅ |
| Complexity | $O((n+m)$ lg n) | $O(nm)$ |
| Approach | Greedy (cut invariant) | Dynamic programming |
| When to use | Non-negative weights, sparse graph | Negative weights or cycle detection needed |

**SSSP vs APSP**

| | SSSP (single source) | APSP (all pairs) |
|--|---------------------|-----------------|
| Output | Distances from one source | Distances between all pairs |
| Dijkstra | ✅ $O((n+m)$ lg n) per source | ✅ n runs → $O(n(n+m)$ lg n) but expensive |
| Floyd-Warshall | — | ✅ $\Theta(n³)$; simpler for dense graphs |

**DAG vs General Graph Shortest Paths**

| | DAG Relaxation | Dijkstra | Bellman-Ford |
|--|---------------|---------|-------------|
| Graph type | DAG only | Any (non-neg weights) | Any |
| Negative weights | ✅ | ❌ | ✅ |
| Complexity | $\Theta(n + m)$ | $O((n+m)$ lg n) | $O(nm)$ |
| Cycles | N/A — DAGs have none | OK | OK |

---

## Common Mistakes

1. **Using Dijkstra with negative weights** — Dijkstra's cut invariant breaks down with negative edges. A vertex settled with a sub-optimal estimate may never be re-relaxed.

2. **Forgetting the n−1 bound in Bellman-Ford** — the algorithm needs exactly n−1 rounds because the longest simple path has at most n−1 edges. Running fewer rounds may leave some distances not yet optimal.

3. **Floyd-Warshall diagonal check** — after running the algorithm, checking D[i][i] < 0 is the standard negative-cycle test. Forgetting this step means missing negative cycles.

4. **Topological sort applicability** — topological sort and DAG shortest-path algorithms require the graph to be a DAG. Applying them to cyclic graphs produces incorrect results.

5. **PERT critical path direction** — the critical path is the *longest* path, not the shortest. Negate weights if using a shortest-path routine, or use a direct longest-path propagation in topological order.

6. **In-degree 0 only at start** — Kahn's topological sort requires initialising the queue with *all* in-degree-0 vertices, not just one. Missing some leaves gaps in the output.

---

## Links Back

- [[Graph Fundamentals]] — vocabulary, adjacency list vs matrix
- [[DAG and Topological Sort]] — Kahn's algorithm, PERT critical path
- [[Shortest Path Overview]] — algorithm selection, relaxation primitive, negative-weight handling
- [[Dijkstra's Algorithm]] — greedy SSSP for non-negative weights
- [[Bellman-Ford Algorithm]] — DP-based SSSP; negative weights and cycle detection
- [[Floyd-Warshall Algorithm]] — all-pairs DP; $\Theta(n³)$; negative cycle detection

## References
- [[CS Algorithms/Sources/Sources Index|CS Algorithms Sources Index]]
