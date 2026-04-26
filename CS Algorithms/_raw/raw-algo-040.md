---
tags: [cs-algorithms, raw]
source_type: textbook-chapter
source_title: "Linear Programming: Simplex, Interior Point, and Duality"
authors: [Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein]
year: 2022
---

## Summary

Linear programming (LP) optimizes a linear objective function subject to linear inequality and equality constraints. The feasible region—the set of all points satisfying the constraints—forms a convex polytope, and the optimal solution (if it exists) occurs at a vertex of this polytope. The simplex method, developed by George Dantzig in 1947, traverses vertices of the polytope by pivoting along edges, improving the objective at each step. Despite exponential worst-case complexity (the Klee-Minty cube requires 2^n pivots on an n-dimensional problem), simplex is extremely fast in practice, typically requiring O(m + n) pivots for m constraints and n variables. Bland's rule and the lexicographic method prevent cycling (infinite loops among degenerate vertices). Interior point methods, introduced by Karmarkar in 1984, traverse the interior of the feasible region rather than its boundary, achieving polynomial worst-case time O(n^3.5 L) where L is the input bit length. Modern LP solvers (CPLEX, Gurobi, COIN-OR) implement both simplex and barrier (interior point) methods, automatically selecting based on problem structure. LP duality is a profound theoretical result: every LP (the primal) has a corresponding dual LP, and strong duality guarantees that if both are feasible, their optimal values are equal. The dual provides certificates of optimality (a feasible dual solution proves a lower bound on the primal minimum) and has economic interpretations (shadow prices). LP relaxation—relaxing integer constraints to linear ones—provides bounds for integer programming, underpinning branch-and-bound and cutting-plane methods. Applications pervade operations research: airline crew scheduling, supply chain optimization, portfolio optimization, network flow (which can be formulated as LP), and resource allocation problems. The ellipsoid method (Khachiyan, 1979) provided the first polynomial-time algorithm for LP but is impractical; it is theoretically important for proving that LP is in P.

## Key Claims

1. The simplex method finds optimal LP solutions by traversing polytope vertices, with exponential worst-case but excellent practical performance (typically polynomial in m + n pivots).
2. Interior point methods achieve polynomial worst-case complexity O(n^3.5 L) and are competitive with or superior to simplex for large, sparse problems.
3. LP duality (strong duality theorem) guarantees that primal and dual optimal values are equal, providing optimality certificates and sensitivity analysis through dual variables.
4. LP relaxation of integer programs provides bounds used by branch-and-bound solvers; the tightness of these bounds determines solver efficiency.
5. Linear programming is in P (proven by the ellipsoid method, practically solved by simplex and interior point), making it the cornerstone of polynomial-time optimization.

## Atomic Facts

1. An LP in standard form is: minimize c^T x subject to Ax ≤ b, x ≥ 0, where x ∈ R^n, A ∈ R^(m×n), b ∈ R^m, c ∈ R^n.
2. The simplex method maintains a basis (set of m basic variables) defining a vertex; each pivot swaps one basic variable with one non-basic variable, moving to an adjacent vertex.
3. Bland's rule (choose the smallest-index entering and leaving variables) prevents cycling in degenerate LPs where multiple pivots produce the same objective value.
4. The dual of min c^T x s.t. Ax ≥ b, x ≥ 0 is max b^T y s.t. A^T y ≤ c, y ≥ 0; weak duality always holds (dual ≤ primal), strong duality holds at optimality.
5. Interior point methods follow a central path through the interior of the feasible region, using Newton's method on a barrier function that penalizes approaching constraint boundaries.
6. Network flow problems (max flow, min-cost flow, assignment) are special cases of LP with totally unimodular constraint matrices, guaranteeing integer optimal solutions to LP relaxations.

## Significance

Linear programming is the most widely used optimization framework in industry and science. The simplex method, despite its age, remains one of the most impactful algorithms ever devised, solving millions of decision variables in modern supply chain, logistics, and financial optimization systems. LP duality connects optimization to economics (shadow prices, marginal costs) and provides the theoretical foundation for convex optimization, game theory (minimax theorem), and algorithmic mechanism design. LP relaxation is the primary tool for tackling NP-hard integer programs, making LP the bridge between tractable and intractable optimization. Understanding LP is essential for operations research, machine learning (SVMs are LP/QP), and any domain involving constrained optimization.

## Chunks Extracted

chunk-algo-197 through chunk-algo-200
