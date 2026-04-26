---
tags: [cs-algorithms, raw]
source_type: textbook-chapter
source_title: "Topological Sort: Ordering Directed Acyclic Graphs"
authors: [Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein]
year: 2022
---

## Summary

Topological sorting produces a linear ordering of the vertices of a directed acyclic graph (DAG) such that for every directed edge (u, v), vertex u appears before v in the ordering. This ordering exists if and only if the graph is a DAG—any directed cycle makes topological ordering impossible. Two standard algorithms compute topological sorts in O(V + E) time. Kahn's algorithm (BFS-based) maintains an indegree count for each vertex and a queue of vertices with indegree 0. Repeatedly dequeue a vertex, output it, and decrement the indegree of all its neighbors; any neighbor reaching indegree 0 is enqueued. If the total number of output vertices is less than V, the graph contains a cycle. The DFS-based algorithm runs a full depth-first search, appending each vertex to a list upon completion (post-order), then reverses the list. The reversed post-order is a valid topological sort because a vertex is completed only after all vertices reachable from it are completed. Topological sort is fundamental to dependency resolution: build systems (Make, Gradle) use it to determine compilation order; package managers (npm, pip) use it to resolve installation dependencies; course prerequisite systems use it to plan valid course sequences; and job schedulers use it to order tasks respecting precedence constraints. The longest path in a DAG (critical path), computable in O(V + E) using topological order, determines the minimum project completion time in scheduling. Multiple valid topological orderings typically exist; if the ordering must be unique, it implies a Hamiltonian path in the DAG. Lexicographically smallest topological sort can be computed by replacing the queue in Kahn's algorithm with a min-priority queue.

## Key Claims

1. Topological sort produces a valid linear ordering of a DAG in O(V + E) time; such an ordering exists if and only if the graph has no directed cycles.
2. Kahn's algorithm processes vertices in BFS order by indegree, doubling as a cycle detector: if fewer than V vertices are output, the graph contains a cycle.
3. DFS-based topological sort outputs vertices in reverse post-order, which is correct because every vertex finishes after all of its descendants in the DFS tree.
4. The longest path in a DAG (critical path) is computable in O(V + E) by relaxing edges in topological order—unlike general graphs where longest path is NP-hard.
5. Multiple valid topological orderings exist for most DAGs; uniqueness occurs only when the DAG has a Hamiltonian path (total order on vertices).

## Atomic Facts

1. Kahn's algorithm initializes a queue with all vertices having indegree 0, then iteratively processes each vertex by reducing its neighbors' indegrees and enqueueing those reaching 0.
2. DFS-based topological sort appends vertex v to the output list when DFS(v) finishes (all descendants explored); the final list is reversed to obtain the topological order.
3. Both algorithms run in O(V + E): Kahn's processes each vertex once and each edge once during indegree decrement; DFS visits each vertex and edge once.
4. In build systems like Make, topological sort ensures that a source file is compiled before any file that depends on it, minimizing recompilation.
5. The lexicographically smallest topological sort replaces Kahn's FIFO queue with a min-heap, producing the alphabetically/numerically earliest valid ordering in O((V + E) log V).
6. Dynamic topological sort algorithms maintain a topological order under edge insertions, detecting cycles incrementally without recomputing from scratch.

## Significance

Topological sort is one of the most practically ubiquitous graph algorithms, underpinning dependency management in software engineering, task scheduling in project management, and data flow analysis in compilers. Its simplicity (both algorithms are straightforward to implement) and efficiency (linear time) make it a foundational tool. The connection between topological sort and DAG shortest/longest paths enables critical path analysis in project scheduling (PERT/CPM), a technique used across engineering and management disciplines. Understanding topological sort is essential for reasoning about partial orders, causality in distributed systems (Lamport clocks), and instruction scheduling in compilers.

## Chunks Extracted

chunk-algo-185 through chunk-algo-188
