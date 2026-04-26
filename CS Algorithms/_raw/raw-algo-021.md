---
tags: [cs-algorithms, raw]
source_type: textbook-chapter
source_title: "Floyd-Warshall All-Pairs Shortest Paths"
authors: [Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein]
year: 2022
---

## Summary

The Floyd-Warshall algorithm solves the all-pairs shortest path problem: given a weighted directed graph with V vertices, compute the shortest path between every pair of vertices. The algorithm runs in O(V³) time and O(V²) space, using a dynamic programming approach that systematically considers intermediate vertices. Unlike Dijkstra's algorithm (which handles single-source shortest paths), Floyd-Warshall processes all pairs simultaneously and correctly handles negative edge weights, provided no negative-weight cycles exist. The algorithm builds a sequence of matrices D⁽⁰⁾, D⁽¹⁾, …, D⁽ⁿ⁾ where D⁽ᵏ⁾[i][j] represents the shortest path from i to j using only vertices {1, 2, …, k} as intermediates. The recurrence is D⁽ᵏ⁾[i][j] = min(D⁽ᵏ⁻¹⁾[i][j], D⁽ᵏ⁻¹⁾[i][k] + D⁽ᵏ⁻¹⁾[k][j]). Negative-weight cycles can be detected by checking whether any diagonal entry D[i][i] becomes negative. Beyond shortest paths, the same framework computes the transitive closure of a graph—determining reachability between all vertex pairs—by replacing (min, +) with (OR, AND) operations. Path reconstruction uses a predecessor matrix Π updated alongside the distance matrix.

## Key Claims

1. Floyd-Warshall computes all-pairs shortest paths in O(V³) time using dynamic programming on the set of intermediate vertices, which is optimal for dense graphs represented as adjacency matrices.
2. The algorithm correctly handles negative edge weights (unlike Dijkstra) and detects negative-weight cycles by inspecting diagonal entries of the distance matrix.
3. The DP recurrence considers whether the shortest path from i to j benefits from routing through vertex k, building solutions from smaller vertex subsets to the full graph.
4. Transitive closure—determining whether a path exists between every pair of vertices—is computed using the same algorithmic structure with Boolean operations replacing arithmetic.
5. For sparse graphs, running Dijkstra from each vertex (O(V·E log V)) or Johnson's algorithm (O(V² log V + VE)) outperforms Floyd-Warshall, but for dense graphs the cubic bound is competitive.

## Atomic Facts

1. The space complexity can be reduced to O(V²) by updating the distance matrix in-place, since D⁽ᵏ⁾[i][k] = D⁽ᵏ⁻¹⁾[i][k] and D⁽ᵏ⁾[k][j] = D⁽ᵏ⁻¹⁾[k][j].
2. The algorithm uses three nested loops (k, i, j), where the outermost loop iterates over intermediate vertices—the loop order is critical for correctness.
3. Path reconstruction requires maintaining a predecessor matrix Π where Π[i][j] stores the last intermediate vertex on the shortest path from i to j.
4. A negative-weight cycle exists if and only if some D[i][i] < 0 after the algorithm completes.
5. The transitive closure variant (Warshall's algorithm, 1962) predates the shortest-path version and uses bitwise OR/AND instead of min/addition.
6. Floyd-Warshall is easily parallelizable: for a fixed k, all (i, j) entries can be computed independently, enabling GPU acceleration for large graphs.

## Significance

Floyd-Warshall remains the standard algorithm for all-pairs shortest paths on dense graphs and a foundational example of dynamic programming in graph theory. Its simplicity (triple nested loop, ~5 lines of core code) makes it highly teachable and implementable. The algorithm is used in network routing protocols, geographic information systems for computing driving distances between all city pairs, and as a subroutine in graph analysis tools. The transitive closure application connects it to relational database query optimization and reachability analysis in program verification.

## Chunks Extracted

*Pending*
