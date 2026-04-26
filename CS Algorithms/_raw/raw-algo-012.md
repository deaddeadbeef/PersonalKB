---
tags: [cs-algorithms, raw]
source_type: journal_paper
source_title: "A Note on Two Problems in Connexion with Graphs"
authors: "Edsger W. Dijkstra"
year: 1959
---

# Dijkstra's Shortest Path Algorithm

## Summary
Dijkstra's algorithm solves the single-source shortest path problem for graphs with non-negative edge weights by greedily expanding the nearest unvisited vertex. It maintains a priority queue of tentative distances and relaxes edges as vertices are finalized, guaranteeing that each vertex's distance is optimal when extracted. The algorithm's time complexity depends on the priority queue implementation: O(V² + E) with a simple array, O((V + E) log V) with a binary heap, and O(V log V + E) with a Fibonacci heap.

## Key Claims
- Dijkstra's algorithm correctly computes shortest paths from a single source to all reachable vertices in a graph with non-negative edge weights, proved by induction on the number of finalized vertices
- The greedy correctness relies on the key property: if all edge weights are non-negative, then the vertex with the smallest tentative distance among unvisited vertices has its final shortest-path distance
- With a binary min-heap, the algorithm performs V extract-min operations (O(V log V) total) and at most E decrease-key operations (O(E log V) total), for O((V + E) log V) overall
- For dense graphs (E = Θ(V²)), the array-based O(V²) implementation is optimal and outperforms heap-based versions due to lower constant factors
- Dijkstra's algorithm fails on graphs with negative edge weights because a vertex finalized early may later be reachable via a shorter path through a negative-weight edge, violating the greedy invariant

## Atomic Facts
1. Dijkstra's 1959 paper was only 2.5 pages long and also presented what is now known as Prim's algorithm for minimum spanning trees; the paper has over 20,000 citations
2. With a Fibonacci heap, the total running time is O(V log V + E) because each of the V extract-min operations costs O(log V) amortized and each of the E decrease-key operations costs O(1) amortized
3. For road networks (V ≈ 24 million for the US, E ≈ 58 million), A* search with landmark-based lower bounds (ALT algorithm) typically expands fewer than 1% of vertices compared to plain Dijkstra
4. Bidirectional Dijkstra runs simultaneous searches from source and target, terminating when search frontiers meet; this reduces the search space by approximately half in Euclidean graphs, exploring roughly πd²/2 area instead of πd²
5. The shortest-path tree produced by Dijkstra contains exactly V − 1 edges (for V reachable vertices), and for any vertex v, the path from source to v in this tree is a shortest path
6. On graphs with integer weights in range [0, C], Dijkstra with a bucket queue (dial's algorithm) runs in O(E + VC) time; for small C this is O(V + E), which is linear

## Significance
Dijkstra's algorithm is the cornerstone of network routing (OSPF protocol), GPS navigation, and countless optimization problems. Its elegant greedy structure makes it a standard introduction to greedy algorithms and priority-queue-based graph algorithms. The algorithm's limitations (no negative weights) motivate Bellman-Ford, while its practical optimizations (A*, bidirectional, contraction hierarchies) enable real-time routing on continental-scale road networks with millions of vertices. The interplay between Dijkstra's algorithm and priority queue data structures (binary heap, Fibonacci heap, bucket queue) illustrates how data structure choice directly determines algorithmic efficiency.

## Chunks Extracted
*Pending*
