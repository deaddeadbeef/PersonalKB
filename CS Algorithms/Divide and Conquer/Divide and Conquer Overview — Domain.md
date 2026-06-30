---
tags:
  - csa
  - moc
up: "[[CS Algorithms]]"
confidence: verified
---
# Divide and Conquer Overview — Domain

Divide and conquer breaks a problem into smaller subproblems of the same type, solves each recursively, and combines the results. It is the engine behind many of the most efficient algorithms in computer science — merge sort, quicksort, Strassen's matrix multiplication, and the FFT. Understanding when and how to apply the paradigm, and how to analyse the resulting recurrences, is fundamental algorithmic literacy.

---

## Learn in This Order

1. [[Divide and Conquer Overview]] — the paradigm; divide/conquer/combine pattern; when D&C applies
2. [[Master Theorem Applications]] — solving recurrences that arise from D&C algorithms; case analysis

---

## In This Domain

| Page | One-line summary |
|------|-----------------|
| [[Divide and Conquer Overview]] | Paradigm definition; recursive decomposition; canonical examples |
| [[Master Theorem Applications]] | Applying the Master Theorem to classify D&C recurrence complexity |

---

## Common Distinctions

| Question | Answer |
|----------|--------|
| D&C vs DP? | D&C subproblems are independent (no overlap); DP subproblems overlap and require memoisation. Merge sort is D&C; Fibonacci is DP. |
| When does the Master Theorem apply? | When the recurrence has the form T(n) = aT(n/b) + f(n) — i.e., a subproblems of size n/b with combine cost f(n). |
| D&C vs decrease-and-conquer? | D&C splits into multiple subproblems (merge sort splits in two); decrease-and-conquer reduces to one subproblem (binary search). |

---

## How to Navigate

- **Learning the paradigm?** Start at [[Divide and Conquer Overview]].
- **Analysing a D&C recurrence?** Go to [[Master Theorem Applications]].
- **Already know D&C?** See specific D&C algorithms in [[Sorting Overview]] (merge sort, quicksort).

---

## Related Domains

- **[[Foundations and Analysis Overview]]** — recurrence relations and the Master Theorem itself.
- **[[Sorting Overview]]** — merge sort and quicksort are canonical D&C algorithms.
- **[[Greedy Overview]]** — contrasting paradigm: greedy makes one choice per step rather than recursing.

## References
- [[CS Algorithms/Sources/Sources Index|CS Algorithms Sources Index]]
