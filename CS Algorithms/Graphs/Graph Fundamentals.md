---
tags:
  - csa
  - csa/graphs
confidence: verified
up: "[[Graphs Overview]]"
tier-coverage: [intuition, core, deep-dive, practice]
---
# Graph Fundamentals

> **Core vocabulary and representations for all graph algorithms — vertices, edges, adjacency structures, and DAGs.**

## 🎯 Intuition
**The Core Idea:** Graphs model pairwise relationships; the representation you choose (list vs matrix) determines the efficiency of every algorithm built on top.
**Analogy:** Graph fundamentals are the vocabulary of maps — vertices are cities, edges are roads, and before you can navigate, you need the map legend.
**Why It Matters:** Every shortest-path, flow, and connectivity algorithm assumes you know these definitions. Choosing adjacency list vs matrix affects both space and time complexity.

---

## ⚙️ Core Mechanics
### Graph Representations

**Adjacency List** — For each vertex u, store a list of its neighbours (and weights). Space: $\Theta(n + m)$ where n = |V|, m = |E|. Efficient for sparse graphs (m ≪ n²). Preferred representation in *Algorithms Unlocked*.

**Adjacency Matrix** — n×n matrix where entry (u,v) = 1 (or weight) if edge (u,v) exists. Space: $\Theta(n²)$. Efficient for dense graphs; constant-time edge lookup; used by Floyd-Warshall.

### Basic Definitions

**Figure:** Directed vs Undirected graph

```mermaid
graph LR
    subgraph "Directed"
        A1((A)) -->|""| B1((B))
        B1 -->|""| C1((C))
        A1 -->|""| C1
    end
    subgraph "Undirected"
        A2((A)) ---|""| B2((B))
        B2 ---|""| C2((C))
        A2 ---|""| C2
    end
```


| Term | Definition |
|------|------------|
| **Graph** G = (V, E) | Set of **vertices** V and **edges** E |
| **Directed graph** | Edges are ordered pairs (u, v) — direction matters |
| **Undirected graph** | Edges are unordered pairs {u, v} |
| **Weighted graph** | Each edge has a numeric weight w(u, v) |
| **Adjacent** | v is adjacent to u if edge (u, v) exists |
| **Degree** | Number of edges incident to a vertex |
| **In-degree** | Number of incoming edges (directed graphs) |
| **Out-degree** | Number of outgoing edges (directed graphs) |
| **Path** | Sequence of vertices v₀, v₁, …, vₖ where (vᵢ, vᵢ₊₁) is an edge |
| **Cycle** | Path where v₀ = vₖ |
| **DAG** | Directed Acyclic Graph — directed graph with no directed cycles |

### Pseudocode
N/A — this is a vocabulary page; see individual algorithm pages for pseudocode.

### Complexity

| Representation | Space | Edge Lookup | Iterate Neighbours |
|----------------|-------|-------------|-------------------|
| Adjacency List | $\Theta(n + m)$ | $O(degree)$ | $O(degree)$ |
| Adjacency Matrix | $\Theta(n²)$ | $O(1)$ | $O(n)$ |

### Key Facts
- Graph algorithm running times use both n = |V| and m = |E|
- For sparse graphs m = $O(n)$; for dense graphs m = $O(n²)$
- Adjacency list is preferred for most algorithms; adjacency matrix suits dense graphs and Floyd-Warshall
- A DAG can always be topologically sorted
- These definitions are prerequisites for [[DAG and Topological Sort]], [[Dijkstra's Algorithm]], [[Bellman-Ford Algorithm]], and [[Floyd-Warshall Algorithm]]

---

## 🔬 Deep Dive
### DAG Properties
A directed graph with no directed cycles. Key property: vertices can be linearly ordered (topological sort) such that all edges go from earlier to later in the order.

**Natural examples**: dependency graphs (build systems, course prerequisites), PERT project networks, computational DAGs in compilers.

### Sparse vs Dense Trade-offs
Graph algorithm running times are typically expressed in terms of both n = |V| (vertices) and m = |E| (edges). For sparse graphs m = $O(n)$; for dense graphs m = $O(n²)$. This distinction matters when comparing Dijkstra ($O((n+m)$ lg n)) vs Floyd-Warshall ($\Theta(n³)$).

### Edge Cases and Pitfalls
- Forgetting to handle disconnected components (unreachable vertices)
- Confusing directed vs undirected edge counts (undirected edge appears in both adjacency lists)
- Self-loops: an edge (v, v) — some algorithms assume no self-loops
- Multigraphs: multiple edges between the same pair of vertices — standard representations may need adaptation

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Given a graph with 6 vertices and 8 edges, is it sparse or dense? What representation would you choose?
2. Can an undirected graph be a DAG? Why or why not?

### Core Problems
1. **Representation conversion**: Given an adjacency matrix, convert it to an adjacency list. What is the time complexity?
2. **Degree computation**: Given an adjacency list for a directed graph, compute the in-degree and out-degree of every vertex in $O(n + m)$.
3. **Cycle detection**: Given a directed graph as an adjacency list, determine whether it contains a cycle.

### Challenge
Given a directed graph, determine the minimum number of edges to remove to make it a DAG.

---

*See also:* [[Dynamic Programming]], [[Asymptotic Notation]], [[NP Completeness]], [[DAG and Topological Sort]], [[Dijkstra's Algorithm]], [[Bellman-Ford Algorithm]], [[Floyd-Warshall Algorithm]], [[CS Data Structures]]

## Supporting Chunks

### Supporting Chunks

- [[Graphs - Graph representation uses adjacency lists for sparse graphs and adjacency matrices for dense graphs]]
- [[Graphs - DAG topological sort processes vertices in precedence order in Theta(n+m)]]

## References

See [[CS Algorithms/Sources/Sources Index#Cormen 2013|Sources Index]]. Chapter 5. See [[DAG and Topological Sort]] for the first algorithm built on this vocabulary.
