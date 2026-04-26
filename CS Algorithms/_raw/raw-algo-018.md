---
tags: [cs-algorithms, raw]
source_type: textbook
source_title: "NP-Completeness: Computational Intractability"
authors: "Stephen Cook, Richard Karp, Michael Garey, David S. Johnson"
year: 1971
---

# NP-Completeness Theory

## Summary
NP-completeness theory classifies computational problems by their inherent difficulty, establishing that a large class of important optimization and decision problems are unlikely to have polynomial-time algorithms. The class P contains problems solvable in polynomial time, NP contains problems whose solutions are verifiable in polynomial time, and NP-complete problems are the hardest problems in NP—if any one of them has a polynomial-time algorithm, then all of NP does (P = NP). The Cook-Levin theorem (1971) proved that Boolean satisfiability (SAT) is NP-complete, and Karp's 21 reductions established NP-completeness for a wide range of combinatorial problems.

## Key Claims
- A problem L is NP-complete if (1) L ∈ NP (solutions are verifiable in polynomial time) and (2) every problem in NP is polynomial-time reducible to L; this means NP-complete problems are at least as hard as every problem in NP
- The Cook-Levin theorem proves SAT is NP-complete by showing that any nondeterministic Turing machine computation of polynomial length can be encoded as a Boolean formula of polynomial size that is satisfiable if and only if the machine accepts
- Polynomial-time reductions (Karp reductions) transform instances of one problem into instances of another in polynomial time; if A ≤_p B and B ∈ P, then A ∈ P; contrapositively, if A is NP-hard and A ≤_p B, then B is NP-hard
- The P vs NP question asks whether every problem whose solution can be verified quickly can also be solved quickly; it is one of the seven Millennium Prize Problems with a $1 million reward, and remains open since 1971
- NP-completeness does not mean a problem is unsolvable—it means no known polynomial-time algorithm exists; practical approaches include approximation algorithms, parameterized algorithms, heuristics, and exploiting special structure

## Atomic Facts
1. Karp's 1972 paper demonstrated 21 NP-complete problems via polynomial reductions from SAT, including Clique, Vertex Cover, Hamiltonian Cycle, Graph Coloring, Subset Sum, and Integer Linear Programming
2. 3-SAT (satisfiability with at most 3 literals per clause) is NP-complete, but 2-SAT is in P, solvable in O(V + E) via strongly connected components on the implication graph—a sharp complexity boundary at clause size 3
3. The Vertex Cover problem asks for the minimum set of vertices covering all edges; it is NP-complete, but has a simple 2-approximation algorithm (take both endpoints of any maximal matching) and a fixed-parameter tractable algorithm running in O(2^k · n) for cover size k
4. The Traveling Salesman Problem (TSP) on n cities has n!/2n distinct tours; the Held-Karp DP algorithm solves it exactly in O(n² · 2ⁿ) time and O(n · 2ⁿ) space, which for n = 25 is about 838 million states
5. Unless P = NP, no NP-complete problem can be solved in polynomial time; the exponential time hypothesis (ETH) further conjectures that 3-SAT cannot be solved in 2^{o(n)} time, implying specific lower bounds for many problems
6. There are over 3,000 known NP-complete problems catalogued in Garey and Johnson's 1979 reference "Computers and Intractability," spanning graph theory, logic, scheduling, number theory, and network design

## Significance
NP-completeness theory is one of the most important intellectual achievements in computer science, providing a rigorous framework for understanding computational intractability. When a problem is proved NP-complete, it shifts the focus from seeking exact polynomial algorithms to designing approximation algorithms, heuristics, and special-case solutions. This theory guides billions of dollars of engineering decisions: the security of RSA and other cryptographic systems relies on the assumed hardness of problems believed to be outside P. Understanding NP-completeness is essential for any computer scientist, as it answers the fundamental question of when to stop searching for efficient exact algorithms and start designing practical alternatives.

## Chunks Extracted
*Pending*
