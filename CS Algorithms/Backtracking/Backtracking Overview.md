---
tags: [csa, csa/backtracking]
up: "[[CS Algorithms Index]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Backtracking Overview

> **One-line summary**: Backtracking systematically explores all potential solutions by building candidates incrementally and abandoning ("pruning") a branch as soon as it determines the candidate cannot lead to a valid or optimal solution.

## 🎯 Intuition
**The Core Idea:** Try a choice, recurse; if it fails, undo the choice and try the next option.
**Analogy:** Navigating a maze by walking forward at every fork, and whenever you hit a dead end, you retrace your steps to the last fork and try a different path.
**Why It Matters:** Backtracking is the go-to strategy for constraint-satisfaction problems (CSPs) — puzzles, combinatorial search, and NP-hard problems where exhaustive search is needed but pruning makes it tractable.

---

## ⚙️ Core Mechanics
### General Framework
1. **Choose:** Select a candidate for the current decision point.
2. **Explore:** Recurse to make the next decision.
3. **Unchoose (Backtrack):** If the path doesn't lead to a solution, undo the choice and try the next candidate.

### Pseudocode
```
function Backtrack(state, decisions):
    if state is a complete solution:
        record or return solution
        return
    for each candidate in choices(state, decisions):
        if isValid(state, candidate):
            applyChoice(state, candidate)
            Backtrack(state, remaining_decisions)
            undoChoice(state, candidate)
```

### Complexity

| Case | Time | Space |
|------|------|-------|
| Best | $O(1)$ — pruned early | $O(d)$ — recursion depth d |
| Average | Problem-dependent | $O(d)$ |
| Worst | $O(b^d)$ — full tree | $O(d)$ |

Where b = branching factor and d = depth of the search tree.

### Key Facts
- Backtracking is a refined brute-force: it prunes invalid branches early instead of generating all possibilities and filtering.
- The effectiveness depends entirely on the quality of pruning (constraint propagation, bounding functions).
- Backtracking generates the search tree **implicitly** — it never stores the whole tree in memory.
- Space complexity is $O(d)$, far better than BFS-based exploration ($O(b^d)$).

---

## 🔬 Deep Dive
### Pruning Strategies
1. **Feasibility pruning:** Reject candidates that violate hard constraints immediately (e.g., placing two queens in the same column).
2. **Bounding (Branch and Bound):** Compute an upper/lower bound on the best solution achievable from the current state; prune if it can't beat the best known solution.
3. **Symmetry breaking:** Avoid exploring equivalent configurations (e.g., fixing the first queen's position to eliminate rotational symmetry).
4. **Constraint propagation:** Use arc consistency or forward checking to reduce the domain of future variables.

### Edge Cases and Pitfalls
- **Forgetting to undo state changes** — the classic bug. If you modify a global array in "choose," you must reverse it in "unchoose."
- **Stack overflow on deep recursion** — limit depth or switch to iterative backtracking for very deep search trees.
- **Generating duplicates** — when candidates can be reordered, enforce a canonical ordering to avoid processing the same subset multiple times.
- **Confusing backtracking with DFS** — DFS is a traversal; backtracking is a problem-solving paradigm that uses DFS as its search mechanism plus pruning.

### Comparison with Alternatives
- **Brute Force / Exhaustive Enumeration:** Generates all possibilities without pruning. Backtracking is strictly better due to early termination.
- **Dynamic Programming:** Use when the problem has overlapping sub-problems and optimal substructure. Backtracking has independent paths.
- **Greedy:** Use when a local optimum guarantees global optimum. Backtracking is for when you need to explore multiple branches.
- **Branch and Bound:** A specialization of backtracking for optimization problems, adding bounding functions.

### Real-World Usage
- **Sudoku solvers** — try a number, propagate constraints, backtrack if a conflict arises.
- **SAT solvers (DPLL)** — backtracking with unit propagation and pure literal elimination.
- **Compiler register allocation** — graph coloring via backtracking.
- **Automated theorem provers** — searching proof trees.
- **Crossword puzzle generators** — placing words on a grid with letter-sharing constraints.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What distinguishes backtracking from plain brute-force enumeration?
2. In the backtracking template, why is the "unchoose" step critical?
3. What is the space complexity of backtracking, and why?

### Core Problems
1. **Subsets (LeetCode 78):** Generate all subsets of a set. *Approach:* At each element, choose to include or exclude, recurse, backtrack.
2. **Permutations (LeetCode 46):** Generate all permutations of distinct numbers. *Approach:* Swap-based or used-array backtracking.

### Challenge
- **Sudoku Solver (LeetCode 37):** Solve a 9×9 Sudoku. Implement backtracking with constraint propagation (naked singles, hidden singles). Measure how much pruning reduces the search space compared to plain backtracking.

---

*See also:* [[N-Queens Problem]] · [[Dynamic Programming Overview]] · [[Greedy Algorithms Overview]] | **CS Data Structures:** [[Stacks]] · [[Recursion and Call Stack]]

## References
-> [[Sources Index]]
