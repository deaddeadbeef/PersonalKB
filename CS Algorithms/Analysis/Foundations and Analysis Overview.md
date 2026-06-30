---
tags:
  - csa
  - moc
up: "[[CS Algorithms]]"
confidence: verified
---
# Foundations and Analysis Overview

The analytical toolkit every algorithm chapter draws on. Master this domain first — asymptotic reasoning, loop-invariant proofs, and recurrence solving appear in every other topic in the knowledge base.

---

## Learn in This Order

1. [[Algorithm Definition]] — what an algorithm is; correctness spectrum; exact vs approximate
2. [[Asymptotic Notation]] — Θ, O, Ω; why constants are dropped; growth-rate comparisons
3. [[Loop Invariant]] — three-part correctness proof: initialization, maintenance, termination
4. [[Recurrence Relations]] — expressing divide-and-conquer running time as T(n) = aT(n/b) + f(n)
5. [[Master Theorem]] — three-case recipe for solving common recurrences; watershed exponent
6. [[Dynamic Programming]] — overlapping subproblems; bottom-up tabulation; optimal substructure
7. [[Comparison Sort Lower Bound]] — decision-tree argument for the $\Omega(n \lg n)$ sorting floor

---

## In This Domain

| Page | One-line summary |
|------|-----------------|
| [[Algorithm Definition]] | Formal definition; correctness spectrum; approximation algorithms |
| [[Asymptotic Notation]] | Θ, O, Ω; intuition; common growth rates |
| [[Loop Invariant]] | Initialization/maintenance/termination proof template |
| [[Recurrence Relations]] | Recurrence notation; unrolling; merge sort and binary search cases |
| [[Master Theorem]] | Three-case theorem; watershed; quick-reference card |
| [[Dynamic Programming]] | Optimal substructure; memoization vs tabulation; key examples |
| [[Comparison Sort Lower Bound]] | Decision-tree model; $\Omega(n \lg n)$ lower bound; lg(n!) exact bound |

---

## Common Distinctions

| Question | Answer |
|----------|--------|
| O vs Θ vs Ω? | O = upper bound, Ω = lower bound, Θ = tight (both). Θ is the most informative; O is used when only the worst case is known. |
| Loop invariant vs induction? | Loop invariants *are* induction — initialization = base case, maintenance = inductive step, termination = conclusion. |
| Memoization vs tabulation? | Memoization = top-down with cache; tabulation = bottom-up filling a table. Both achieve the same asymptotic complexity. |
| When does Master Theorem not apply? | When f(n) is not polynomially comparable to $n^{log_b a}$, or when a < 1 or b ≤ 1. Use Akra-Bazzi or unrolling instead. |

---

## How to Navigate

- **Learning algorithm analysis for the first time?** Follow the order above.
- **Need a proof technique for a specific algorithm?** Start at [[Loop Invariant]] for iterative algorithms or [[Recurrence Relations]] for recursive ones.
- **Analyzing time complexity?** [[Asymptotic Notation]] + [[Master Theorem]] cover most cases.
- **Dynamic programming problems?** [[Dynamic Programming]] → then see [[LCS - Longest Common Subsequence]] and [[Edit Distance]] in the Strings domain.

---

## Related Domains

- **[[Sorting Overview]]** — sorting algorithms are the primary worked examples for loop invariants, recurrences, and the $\Omega(n \lg n)$ lower bound.
- **[[Strings Overview]]** — LCS and Edit Distance are the canonical DP examples that extend the Dynamic Programming page.
- **[[Graphs Overview]]** — Bellman-Ford and Floyd-Warshall apply DP to graph shortest paths.
- **[[Complexity Theory Overview]]** — builds on asymptotic reasoning to distinguish tractable from intractable problems.

## References
- [[CS Algorithms/Sources/Sources Index|CS Algorithms Sources Index]]
