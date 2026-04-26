---
tags: [cs-algorithms, raw]
source_type: textbook-chapter
source_title: "Approximation Algorithms for NP-Hard Problems"
authors: [Vijay V. Vazirani]
year: 2003
---

## Summary

When facing NP-hard optimization problems where exact solutions require superpolynomial time, approximation algorithms provide provably near-optimal solutions in polynomial time. The approximation ratio ρ(n) of an algorithm measures how far its solution can be from optimal: for a minimization problem, the algorithm's cost C satisfies C ≤ ρ(n)·C*, where C* is the optimal cost. Vertex cover admits a simple 2-approximation: repeatedly pick any uncovered edge, add both endpoints to the cover. This runs in O(V + E) and guarantees the cover is at most twice the minimum. The Traveling Salesman Problem with triangle inequality has a 3/2-approximation due to Christofides (1976): compute MST, find minimum-weight perfect matching on odd-degree vertices, combine into Eulerian circuit, and shortcut. The set cover problem has an O(log n)-approximation via the greedy algorithm (always pick the set covering the most uncovered elements), and this ratio is essentially tight unless P = NP. A Polynomial-Time Approximation Scheme (PTAS) achieves a (1+ε)-approximation for any fixed ε > 0, with running time polynomial in n but potentially exponential in 1/ε. A Fully Polynomial-Time Approximation Scheme (FPTAS) is polynomial in both n and 1/ε. The knapsack problem has an FPTAS with time O(n²/ε), while the general TSP (without triangle inequality) cannot be approximated within any constant factor unless P = NP.

## Key Claims

1. Approximation algorithms provide polynomial-time solutions with provable guarantees on solution quality, offering a practical alternative to exact exponential algorithms for NP-hard problems.
2. Vertex cover has a simple 2-approximation, and achieving a ratio better than 2 − ε remains a major open problem (related to the Unique Games Conjecture).
3. Christofides' 3/2-approximation for metric TSP was the best known for 45 years until a slight improvement by Karlin, Klein, and Oveis Gharan in 2021.
4. The greedy algorithm for set cover achieves O(log n) approximation ratio, which is tight: no polynomial-time algorithm can achieve o(log n) unless P = NP.
5. The distinction between PTAS and FPTAS is practically significant: a PTAS may have impractical running time for small ε, while an FPTAS guarantees efficiency for any desired accuracy.

## Atomic Facts

1. The 2-approximation for vertex cover works because each selected edge contributes at most 2 vertices to the cover, and the optimal solution must include at least one endpoint of every selected edge.
2. Christofides' algorithm combines MST (cost ≤ OPT) with minimum perfect matching on odd-degree vertices (cost ≤ OPT/2) to get a tour of cost ≤ 3/2·OPT.
3. The greedy set cover algorithm achieves an H(n) approximation ratio where H(n) = 1 + 1/2 + ... + 1/n ≈ ln(n) is the harmonic number.
4. The knapsack FPTAS works by scaling and rounding item values to reduce the state space, then applying exact dynamic programming on the reduced instance.
5. General TSP (without metric) has no constant-factor approximation unless P = NP, proved by a gap-preserving reduction from Hamiltonian cycle.
6. LP relaxation and rounding is a powerful technique for approximation: solve the linear programming relaxation, then round fractional values to obtain integer solutions with bounded quality loss.

## Significance

Approximation algorithms bridge the gap between theoretical intractability and practical problem-solving. They provide rigorous performance guarantees that heuristics lack, while remaining computationally feasible unlike exact methods. The field has driven deep connections between computational complexity and optimization: inapproximability results (via PCP theorem and Unique Games Conjecture) establish that certain approximation ratios cannot be improved, while algorithm design techniques (LP rounding, semidefinite programming, primal-dual methods) continue to push achievable ratios closer to these limits. In practice, approximation algorithms are used in network design, facility location, scheduling, and resource allocation.

## Chunks Extracted

chunk-algo-149 through chunk-algo-152
