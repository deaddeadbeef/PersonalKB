---
tags:
  - csa
  - moc
up: "[[CS Algorithms]]"
---
# Greedy Overview

Greedy algorithms make the locally optimal choice at each step, hoping to find a global optimum. When a problem exhibits the **greedy-choice property** (a locally optimal choice is part of some globally optimal solution) and **optimal substructure** (an optimal solution contains optimal solutions to subproblems), the greedy approach yields correct and efficient results — often in $O(n \log n)$ or better.

---

## Learn in This Order

1. [[Greedy Algorithms Overview]] — the greedy paradigm; greedy-choice property; when greedy works and when it doesn't
2. [[Activity Selection Problem]] — classic interval scheduling; proof of greedy correctness
3. [[Fractional Knapsack]] — greedy by value-to-weight ratio; contrast with 0/1 knapsack (which requires DP)

---

## In This Domain

| Page | One-line summary |
|------|-----------------|
| [[Greedy Algorithms Overview]] | Paradigm definition; greedy-choice property; correctness proofs |
| [[Activity Selection Problem]] | Select maximum non-overlapping intervals; $O(n \log n)$ |
| [[Fractional Knapsack]] | Maximise value with fractional items; greedy by density |

---

## Common Distinctions

| Question | Answer |
|----------|--------|
| Greedy vs DP? | Greedy commits to one choice per step and never reconsiders; DP explores all subproblem combinations. Greedy is faster when it works, but not all problems have the greedy-choice property. |
| Fractional vs 0/1 knapsack? | Fractional allows breaking items — greedy by value/weight ratio works. 0/1 requires whole items — needs DP. |
| How to prove greedy correctness? | Exchange argument or greedy-stays-ahead: show that swapping any non-greedy choice for the greedy choice doesn't worsen the solution. |

---

## How to Navigate

- **New to greedy?** Start at [[Greedy Algorithms Overview]] for the paradigm and proof techniques.
- **Want a concrete example?** [[Activity Selection Problem]] is the canonical greedy proof.
- **Confused about greedy vs DP?** Compare [[Fractional Knapsack]] (greedy) with the 0/1 variant (DP).

---

## Related Domains

- **[[Graphs Overview]]** — Dijkstra's, Kruskal's, and Prim's are greedy graph algorithms.
- **[[Foundations and Analysis Overview]]** — dynamic programming handles problems where greedy fails.
- **[[Complexity Theory Overview]]** — greedy approximation algorithms for NP-hard problems.
