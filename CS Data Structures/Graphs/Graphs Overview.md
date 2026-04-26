---
tags:
  - cs-ds
  - hub
up: "[[CS Data Structures]]"
---

# Graphs Overview

Graphs model pairwise relationships — friendships in a social network, roads between cities, dependencies in a build system. A graph is simply a set of **vertices** connected by **edges**, yet this minimal definition supports an astonishing variety of real-world problems. Before any graph algorithm can run, the graph must be stored in memory, and the choice of representation profoundly affects both time and space performance. This hub focuses on how graphs are represented and characterised, laying the groundwork for algorithm-oriented study.

## Core Representations

The two classic representations are the **adjacency list** and the **adjacency matrix**. An adjacency list stores, for each vertex, a collection of its neighbours — typically a dynamic array or linked list. It uses $O(V + E)$ space and excels when the graph is sparse. An adjacency matrix uses a V × V array of booleans (or weights), offering $O(1)$ edge lookup at the cost of $O(V²)$ space. Dense graphs or algorithms that repeatedly query edge existence (e.g., Floyd-Warshall) favour the matrix; most other workloads favour the list.

## Directed, Weighted, and Special Graphs

Edges may carry direction (**directed graphs / digraphs**), numerical weights (**weighted graphs**), or both. These attributes influence representation details — a directed edge appears only once in an adjacency list, while an undirected edge appears twice. Understanding fundamental **graph properties and terminology** — degree, connectivity, bipartiteness, planarity, DAGs — is essential for selecting the right algorithm later.

## Implicit and Compressed Representations

Not every graph is materialised in memory. Game-state spaces, procedural maps, and web crawls generate neighbours on the fly via **implicit representations**. At the other extreme, massive static graphs (web graphs, social networks) use **compressed representations** like CSR (Compressed Sparse Row) to slash memory while retaining fast traversal.

## Pages in This Hub

- [[Graph Representations Overview]]
- [[Adjacency List and Adjacency Matrix]]
- [[Weighted and Directed Graphs]]
- [[Graph Properties and Terminology]]
- [[Implicit and Compressed Graph Representations]]

## Related Hubs

- [[Foundational Concepts Overview]] — complexity analysis for graph algorithms
- [[Trees Overview]] — trees as connected acyclic graphs
- [[Hash-Based Structures Overview]] — hash maps for adjacency-list storage
- [[Advanced Structures Overview]] — disjoint sets and spatial structures used in graph problems