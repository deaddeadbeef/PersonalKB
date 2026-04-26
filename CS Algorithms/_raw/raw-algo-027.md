---
tags: [cs-algorithms, raw]
source_type: textbook-chapter
source_title: "Backtracking and Branch-and-Bound Algorithms"
authors: [Steven S. Skiena]
year: 2020
---

## Summary

Backtracking is a systematic method for exploring all possible configurations of a search space by incrementally building candidates and abandoning (pruning) a candidate as soon as it violates problem constraints. The algorithm constructs a solution vector one component at a time, using a recursive tree structure where each node represents a partial solution. At each node, if the partial solution cannot lead to a valid complete solution, the subtree is pruned—avoiding the exponential cost of exhaustive enumeration. The N-queens problem illustrates backtracking elegantly: queens are placed row by row, and any placement that conflicts with existing queens triggers immediate backtracking. Other classic applications include subset sum, graph coloring, Sudoku solving, and generating permutations and combinations. Branch-and-bound extends backtracking for optimization problems by maintaining a bound on the best achievable solution in each subtree. If the bound for a subtree is worse than the best complete solution found so far, the subtree is pruned. For minimization problems, a lower bound is computed for each node; for maximization, an upper bound. The Traveling Salesman Problem (TSP) and integer linear programming are canonical branch-and-bound applications. The method uses a priority queue to explore the most promising nodes first (best-first search), contrasting with backtracking's depth-first approach. While worst-case complexity remains exponential, effective bounding functions and heuristic ordering can reduce the explored search space by orders of magnitude in practice.

## Key Claims

1. Backtracking systematically prunes the search space by abandoning partial solutions that cannot lead to valid or optimal complete solutions, dramatically reducing exploration compared to brute force.
2. The effectiveness of backtracking depends critically on early pruning: the sooner infeasible branches are identified, the larger the subtrees that can be skipped.
3. Branch-and-bound augments backtracking with optimization bounds, enabling pruning of subtrees whose best possible outcome cannot improve on the current best known solution.
4. Constraint propagation techniques (like forward checking in CSPs) strengthen pruning by proactively reducing the domain of future variables based on current assignments.
5. Despite exponential worst-case complexity, well-designed backtracking with good heuristics (variable ordering, value ordering) solves many practical instances efficiently.

## Atomic Facts

1. The N-queens problem places n non-attacking queens on an n×n board; backtracking explores at most n! placements but prunes most, solving n=20 in milliseconds.
2. In graph coloring, backtracking assigns colors to vertices one by one, backtracking when no valid color exists for the current vertex given the current partial coloring.
3. Branch-and-bound for TSP uses a lower bound computed from minimum spanning tree cost or linear programming relaxation of the integer formulation.
4. Best-first branch-and-bound uses a priority queue ordered by bound values, expanding the most promising node first rather than following depth-first order.
5. The branching strategy determines how subproblems are created: for 0-1 variables, branching fixes a variable to 0 or 1; for TSP, branching includes or excludes a specific edge.
6. Branch-and-bound is the primary method in commercial integer programming solvers (CPLEX, Gurobi), combined with cutting planes and sophisticated bounding.

## Significance

Backtracking and branch-and-bound are fundamental algorithmic paradigms for solving constraint satisfaction and combinatorial optimization problems. They provide the theoretical foundation for SAT solvers, constraint programming systems, and integer programming solvers that drive applications in logistics, scheduling, circuit design, and artificial intelligence. The pruning philosophy—avoid unnecessary work by detecting failure early—extends beyond these specific techniques to influence algorithm design broadly. Modern SAT solvers (DPLL, CDCL) are sophisticated backtracking algorithms enhanced with clause learning, unit propagation, and restart strategies, capable of solving instances with millions of variables.

## Chunks Extracted

chunk-algo-145 through chunk-algo-148
