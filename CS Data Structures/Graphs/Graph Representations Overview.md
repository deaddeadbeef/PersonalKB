---
tags: [cs-ds, graphs]
up: "[[Graphs Overview]]"
confidence: verified
created: 2025-07-14
---

**Graph representations are the data-structure layer that determines the time and space cost of every graph algorithm you run.**

## Core Idea

A graph $G = (V, E)$ can be stored in memory in three canonical ways: an **adjacency list**, an **adjacency matrix**, or an **edge list**. Each representation encodes exactly the same mathematical object but exposes different performance trade-offs for insertion, deletion, edge queries, and neighbor iteration. Choosing the right one is the first design decision in any graph-processing pipeline.

The **adjacency list** stores, for each vertex, a collection of its neighbors. It uses $O(V + E)$ space and is the default choice for sparse graphs—which covers most real-world networks (social graphs, road networks, the web). The **adjacency matrix** uses a $V \times V$ boolean (or weight) matrix, consuming $O(V^2)$ space but providing $O(1)$ edge-existence queries. It shines when the graph is dense or when matrix operations (e.g., transitive closure via matrix multiplication) are needed. The **edge list** is simply a flat sequence of $(u, v)$ pairs; it is the most compact for edge-centric algorithms like Kruskal's MST and is trivially sortable and streamable.

In practice, density is the deciding factor. A graph with $|E| \ll |V|^2$ is sparse; here the adjacency list wastes no space on absent edges. When $|E|$ approaches $|V|^2$, the matrix representation becomes competitive and can leverage cache-friendly row scans. Edge lists are rarely the primary runtime structure but serve well as input/output formats and in external-memory or streaming settings.

## Key Facts

- **Adjacency list** — array of variable-length lists; $O(V + E)$ space; neighbor iteration in $O(\deg(v))$.
- **Adjacency matrix** — $V \times V$ array; $O(V^2)$ space; edge query in $O(1)$.
- **Edge list** — flat array of $(u, v)$ pairs; $O(E)$ space; no fast per-vertex access without indexing.
- Sparse threshold: when $|E| < |V|^2 / \log |V|$, adjacency list is generally preferred.
- Adjacency matrices support matrix multiplication for path counting and transitive closure.
- Most textbook algorithms (BFS, DFS, Dijkstra) assume adjacency-list input.
- Hybrid representations (e.g., hash-map adjacency sets) trade constant factors for $O(1)$ average edge query plus efficient iteration.

## Operations and Complexity

| Operation            | Adjacency List       | Adjacency Matrix | Edge List       |
|----------------------|----------------------|-------------------|-----------------|
| Space                | $O(V + E)$          | $O(V^2)$         | $O(E)$         |
| Add edge             | $O(1)$              | $O(1)$           | $O(1)$ amortized|
| Remove edge          | $O(\deg(v))$        | $O(1)$           | $O(E)$         |
| Edge query           | $O(\deg(v))$        | $O(1)$           | $O(E)$         |
| Iterate neighbors    | $O(\deg(v))$        | $O(V)$           | $O(E)$         |
| Iterate all edges    | $O(V + E)$          | $O(V^2)$         | $O(E)$         |

## Why It Matters

The representation you choose propagates into every algorithm's constant factor and asymptotic bound. Using an adjacency matrix for a million-node sparse graph wastes terabytes of memory; using an edge list for repeated neighbor lookups turns linear scans into a bottleneck. Understanding these trade-offs is foundational to algorithm engineering.

## See Also

- [[Adjacency List and Adjacency Matrix]]
- [[Implicit and Compressed Graph Representations]]
- [[Graph Properties and Terminology]]
- [[Weighted and Directed Graphs]]

## Supporting Chunks

- [[CS Data Structures/_chunks/chunk-ds-019 Adjacency lists dominate for sparse graphs|Adjacency lists dominate for sparse graphs]]
- [[CS Data Structures/_chunks/chunk-ds-094 Adjacency matrix enables O1 edge queries but wastes space|Adjacency matrices enable O(1) edge queries but waste space]]
- [[CS Data Structures/_chunks/chunk-ds-127 Edge list is simplest graph representation|Edge lists are the simplest graph representation]]
- [[CS Data Structures/_chunks/chunk-ds-076 CSR stores graphs in flat arrays for cache efficiency|CSR stores graphs in flat arrays for cache efficiency]]

## References

→ [[CS Data Structures/Sources/Sources Index|Sources Index]]
