---
id: chunk-csa-199
type: chunk
source: "[[Cormen 2022 - Linear Programming]]"
source_loc: "LP Duality"
topic: "optimization"
claim: "LP strong duality guarantees that primal and dual optimal values are equal, providing optimality certificates and sensitivity analysis through dual variables (shadow prices)"
confidence: verified
supports:
  - "[[Linear Programming]]"
  - "[[LP Duality]]"
tags:
  - csa
  - csa/optimization
  - chunk
up: "[[CS Algorithms]]"
---
# Optimization — LP strong duality equates primal and dual optima

## Context

Every LP (primal) has a corresponding dual LP. Weak duality always holds: the dual objective bounds the primal. Strong duality guarantees that if both are feasible, their optimal values are equal. The dual of min c^T x s.t. Ax >= b, x >= 0 is max b^T y s.t. A^T y <= c, y >= 0. Dual variables (shadow prices) represent the marginal value of relaxing each constraint, providing sensitivity analysis. A feasible dual solution proves a lower bound on the primal minimum, serving as an optimality certificate.

## Why It Matters

LP duality is a cornerstone of optimization theory, connecting to economics (shadow prices), game theory (minimax), and providing the theoretical foundation for branch-and-bound bounds.

## QnA Seeds

- Q: What is the relationship between weak and strong LP duality?
- Q: What do dual variables (shadow prices) represent economically?
- Q: How does a feasible dual solution certify primal optimality?
