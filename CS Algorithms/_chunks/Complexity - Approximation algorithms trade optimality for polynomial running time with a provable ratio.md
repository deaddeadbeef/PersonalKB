---
id: chunk-csa-032
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 10"
topic: "complexity"
claim: "Approximation algorithms produce solutions in polynomial time that are guaranteed to be within a factor α of the optimal — a principled alternative when exact NP-complete solutions are intractable"
confidence: verified
supports:
  - "[[NP Completeness]]"
  - "[[Approximation Algorithms]]"
tags:
  - csa
  - csa/complexity
  - chunk
up: "[[CS Algorithms]]"
---
# Complexity — Approximation algorithms trade optimality for polynomial running time with a provable ratio

## Context

For an NP-complete minimisation problem, an **α-approximation algorithm** runs in polynomial time and produces a solution of cost at most α · OPT, where OPT is the true optimal cost and α ≥ 1. For maximisation, the guarantee is at least (1/α) · OPT (or equivalently OPT/α), so α ≥ 1 with smaller being better.

The approximation ratio α is a worst-case guarantee — the algorithm may do better in practice, but α is the ceiling on how bad it can get. Proving the ratio requires bounding the algorithm's output relative to OPT, often without knowing OPT explicitly (instead bounding OPT by a relaxation or structural argument).

**Canonical example** (vertex cover): the greedy 2-approximation repeatedly picks any uncovered edge and adds both endpoints to the cover. The result is at most twice the minimum vertex cover size. Proof: the chosen edges form a matching; any cover must include at least one endpoint of each matching edge; the algorithm picks both.

## Why It Matters

For practitioners facing NP-complete problems, approximation algorithms offer a middle ground between exact exponential solvers (infeasible for large n) and heuristics (no quality guarantee). Having a provable ratio tells you the worst-case quality gap and lets you reason about whether the solution is good enough for the application.

## QnA Seeds

- Q: What does it mean for an algorithm to be an α-approximation algorithm?
- Q: How do you prove an approximation ratio without knowing the optimal value OPT?
- Q: Describe the 2-approximation for vertex cover and explain why the ratio is tight.
