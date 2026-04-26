---
tags: [cs-ds, raw]
id: raw-ds-030
source: "Various (graph algorithm literature)"
up: "[[CS Data Structures]]"
---

# Graph Traversal — BFS and DFS Structures

## Key Ideas
- BFS uses queue: explore level by level, finds shortest unweighted paths
- DFS uses stack (or recursion): explore depth-first, useful for cycle detection and topological sort
- BFS tree: edges form shortest-path tree from source
- DFS tree: classifies edges as tree, back, forward, cross edges
- Back edges indicate cycles in directed graphs
- Topological sort: reverse DFS finish order — O(V+E)
- Connected components (undirected): BFS/DFS from each unvisited vertex
- Strongly connected components (directed): Tarjan's or Kosaraju's algorithm — O(V+E)
- Tarjan's SCC: single DFS pass with lowlink values and stack
- Kosaraju's SCC: two DFS passes (forward then reverse graph)
- Articulation points and bridges: DFS with discovery/low values
- Biconnected components: partition edges by articulation points
- BFS on implicit graphs: used in puzzle solving, game trees, shortest path in unweighted

## Space Complexity
- Both BFS and DFS: O(V) auxiliary space
- BFS queue can grow to O(V) — problematic for wide graphs
- DFS stack depth up to O(V) — problematic for deep graphs (stack overflow risk)
