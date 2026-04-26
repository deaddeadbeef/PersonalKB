---
tags: [cs-algorithms, raw]
source_type: textbook
source_title: "Graph Traversal: Breadth-First Search and Depth-First Search"
authors: "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein"
year: 2009
---

# BFS and DFS Graph Traversal

## Summary
Breadth-first search (BFS) and depth-first search (DFS) are the two fundamental graph traversal algorithms, each running in O(V + E) time and forming the basis for a vast range of graph algorithms. BFS explores vertices level by level using a queue, computing shortest paths in unweighted graphs. DFS explores as deep as possible before backtracking using a stack (or recursion), enabling the discovery of structural properties such as cycles, topological orderings, and connected components. Together, they are the building blocks upon which nearly all graph algorithms are constructed.

## Key Claims
- BFS computes the shortest path (minimum number of edges) from a source vertex to all reachable vertices in an unweighted graph, producing a BFS tree of shortest-path distances in O(V + E) time
- DFS classifies edges into tree edges, back edges, forward edges, and cross edges; the presence of a back edge is equivalent to the existence of a cycle in a directed graph
- Topological sorting of a DAG is achieved by running DFS and outputting vertices in reverse finish time order, or equivalently by repeatedly removing vertices with in-degree zero (Kahn's algorithm), both in O(V + E)
- Tarjan's algorithm finds all strongly connected components (SCCs) of a directed graph in a single DFS pass using O(V + E) time and a stack-based low-link value computation
- Kosaraju's algorithm also finds SCCs in O(V + E) by running DFS twice: first on the original graph to compute finish times, then on the transposed graph in reverse finish-time order

## Atomic Facts
1. BFS uses O(V) space for the queue and visited array; for a graph with V = 10⁶ vertices stored as an adjacency list, the total memory for BFS is approximately 8 MB (two arrays of V integers plus the queue)
2. In an unweighted graph, BFS discovers vertices at distance d from the source before any vertex at distance d + 1; the BFS tree has the property that every non-tree edge connects vertices whose levels differ by at most 1
3. DFS on a graph with V = 10⁶ using recursion requires O(V) stack frames; for deep graphs this may cause stack overflow, necessitating an iterative implementation with an explicit stack
4. Tarjan's SCC algorithm maintains a stack and a low-link array; a vertex u is the root of an SCC if and only if its low-link value equals its DFS discovery time, i.e., low[u] = disc[u]
5. Kosaraju's algorithm requires two full DFS traversals and the construction of the transpose graph G^T (reversing all edges), using O(V + E) additional space for G^T; Tarjan's algorithm avoids this by using only one pass
6. BFS is the basis for Hopcroft-Karp bipartite matching, which achieves O(E√V) by finding maximal sets of vertex-disjoint augmenting paths via BFS layering, improving on the O(VE) Hungarian augmenting-path method

## Significance
BFS and DFS are the workhorses of graph algorithms—virtually every graph problem either reduces to or begins with one of these traversals. BFS underpins unweighted shortest paths, bipartite checking (a graph is bipartite if and only if BFS produces no odd-length cycles), and level-based network flow algorithms (Dinic's algorithm uses BFS for blocking flow layers). DFS is the foundation of topological sorting (critical for build systems, task scheduling, and DP on DAGs), cycle detection, articulation point and bridge finding (in O(V + E)), and strongly connected component decomposition. Mastering BFS and DFS is prerequisite to understanding Dijkstra, Bellman-Ford, network flow, and 2-SAT algorithms.

## Chunks Extracted
*Pending*
