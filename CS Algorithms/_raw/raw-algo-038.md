---
tags: [cs-algorithms, raw]
source_type: textbook-chapter
source_title: "Strongly Connected Components in Directed Graphs"
authors: [Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein]
year: 2022
---

## Summary

A strongly connected component (SCC) of a directed graph is a maximal set of vertices such that every vertex is reachable from every other vertex in the set. Decomposing a directed graph into its SCCs reveals the graph's macroscopic structure: the condensation graph—formed by contracting each SCC into a single supernode—is always a DAG, enabling topological sort on the component level. Two classic algorithms compute SCCs in O(V + E) time. Kosaraju's algorithm performs two passes of DFS: first on the original graph to compute finish times, then on the transposed graph (all edges reversed) processing vertices in decreasing finish order. Each DFS tree in the second pass identifies one SCC. The correctness relies on the property that in the condensation DAG, the SCC with the latest finish time in the first DFS is a source component. Tarjan's algorithm uses a single DFS with a stack and a "lowlink" value for each vertex. The lowlink of a vertex v is the smallest discovery time reachable from v through the DFS subtree and at most one back edge. When a vertex's lowlink equals its own discovery time, it is the root of an SCC, and all vertices on the stack above it (inclusive) form that SCC. Tarjan's algorithm is generally preferred in practice due to its single-pass nature and avoidance of graph transposition. Applications of SCC decomposition include: 2-SAT solving (each variable and its negation are vertices; an SCC containing both x and ¬x indicates unsatisfiability), analyzing social network structures (communities where everyone can reach everyone), compiler optimization (identifying strongly connected regions in call graphs), and model checking in formal verification.

## Key Claims

1. Both Kosaraju's and Tarjan's algorithms compute all SCCs in O(V + E) time, which is optimal since every vertex and edge must be examined.
2. Kosaraju's algorithm exploits the fact that the transpose graph has the same SCCs as the original, and processing in reverse finish order ensures each second-pass DFS tree corresponds to exactly one SCC.
3. Tarjan's algorithm uses a single DFS with a lowlink array and an explicit stack, identifying SCC roots as vertices whose lowlink equals their discovery time.
4. The condensation graph (DAG of SCCs) enables reasoning about the directed graph at a higher level, supporting topological ordering of components and reachability analysis.
5. 2-SAT is solvable in O(V + E) using SCC decomposition on the implication graph: a satisfying assignment exists if and only if no variable and its negation belong to the same SCC.

## Atomic Facts

1. Kosaraju's first DFS computes finish times; the second DFS processes the transposed graph in decreasing finish order, with each DFS tree in the second pass being one SCC.
2. The transposed graph G^T has the same SCCs as G because if u and v are mutually reachable in G, they remain mutually reachable in G^T.
3. Tarjan's lowlink[v] = min(disc[v], disc[w]) where w is any vertex reachable from v via tree edges and at most one back/cross edge to an ancestor still on the stack.
4. In Tarjan's algorithm, vertices are pushed onto the stack when discovered and popped when their SCC is identified (when lowlink[v] == disc[v]).
5. The condensation graph has at most V vertices and at most E edges, and it is a DAG: if two SCCs had a cycle between them, they would be merged into a single SCC.
6. In 2-SAT, the implication graph has 2n vertices (one for each literal); the clause (a ∨ b) is modeled as edges ¬a → b and ¬b → a.

## Significance

SCC decomposition is a fundamental tool in graph theory and its applications. It provides the structural decomposition of directed graphs that topological sort provides for DAGs, enabling analysis of cyclic graphs by reducing them to their acyclic component structure. In compiler optimization, SCCs in the call graph identify mutually recursive function groups. In formal verification, SCCs in state-transition graphs identify recurrent behaviors. The 2-SAT application demonstrates an elegant polynomial-time algorithm for a restricted satisfiability problem, contrasting with the NP-completeness of general SAT. Understanding SCCs is essential for analyzing directed networks in social media, web link structures (the "bow-tie" structure of the web), and biological interaction networks.

## Chunks Extracted

chunk-algo-189 through chunk-algo-192
