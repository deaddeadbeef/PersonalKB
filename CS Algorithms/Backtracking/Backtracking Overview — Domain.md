---
tags:
  - csa
  - moc
up: "[[CS Algorithms]]"
---
# Backtracking Overview — Domain

Backtracking is systematic trial-and-error: build a candidate solution incrementally, and as soon as a partial candidate violates the problem constraints, **prune** that branch and backtrack to try another option. It is the general framework for constraint-satisfaction and combinatorial search problems — from puzzles like Sudoku and N-Queens to real-world scheduling and configuration.

---

## Learn in This Order

1. [[Backtracking Overview]] — the paradigm; state-space tree; pruning; contrast with brute force
2. [[N-Queens Problem]] — classic constraint-satisfaction problem; column/diagonal conflict checking

---

## In This Domain

| Page | One-line summary |
|------|-----------------|
| [[Backtracking Overview]] | Paradigm definition; state-space trees; pruning strategies |
| [[N-Queens Problem]] | Place N queens with no mutual attacks; column and diagonal pruning |

---

## Common Distinctions

| Question | Answer |
|----------|--------|
| Backtracking vs brute force? | Brute force generates all candidates then filters; backtracking prunes invalid branches early, dramatically reducing the search space. |
| Backtracking vs DP? | Backtracking explores a decision tree with pruning; DP caches overlapping subproblem results. Backtracking applies when subproblems don't overlap. |
| Backtracking vs branch-and-bound? | Both prune search trees. Branch-and-bound uses a bounding function to prune suboptimal (not just infeasible) branches — it targets optimisation, while backtracking targets feasibility. |

---

## How to Navigate

- **Learning the paradigm?** Start at [[Backtracking Overview]].
- **Want a concrete example?** [[N-Queens Problem]] is the classic demonstration.
- **Ready for optimisation search?** Branch-and-bound extends backtracking — see [[Complexity Theory Overview]] for approximation strategies.

---

## Related Domains

- **[[Graphs Overview]]** — DFS is the traversal strategy underlying backtracking.
- **[[Complexity Theory Overview]]** — many backtracking problems are NP-complete; approximation algorithms provide alternatives.
- **[[Divide and Conquer Overview — Domain]]** — contrasting paradigm: D&C divides into independent subproblems rather than exploring a decision tree.
