---
id: chunk-csa-041
type: chunk
source: "[[Erickson 2019 - Algorithms]]"
source_loc: "Chapter 12 — NP-Hardness"
topic: "complexity"
claim: "To prove a new problem NP-hard, exhibit a polynomial-time reduction from a known NP-hard problem to it; the direction of reduction is from known-hard to unknown"
confidence: verified
supports:
  - "[[NP Completeness]]"
  - "[[P vs NP]]"
tags:
  - csa
  - csa/complexity
  - chunk
up: "[[CS Algorithms]]"
---
# Complexity — NP-hardness is established by polynomial reduction from a known NP-hard problem

## Context

The standard technique for proving that a new problem B is NP-hard is to show that a known NP-hard problem A **reduces** to B in polynomial time (written A ≤ₚ B). The reduction transforms any instance of A into an equivalent instance of B — a YES instance of A maps to a YES instance of B, and a NO instance maps to a NO instance — in time polynomial in the input size.

**Why the direction matters**: A ≤ₚ B means "A is no harder than B." If A is hard and A ≤ₚ B, then B must be at least as hard as A. The chain works: if we could solve B in polynomial time, we could also solve A (run the reduction, then run B's algorithm) — but A has no polynomial algorithm, so B cannot either.

**Common starting points for reductions:**
- **3-SAT** (Cook-Levin; the canonical first NP-complete problem)
- **Independent Set**, **Vertex Cover**, **Clique** — once one is proven NP-hard, the others follow by simple reductions
- **Hamiltonian Cycle** → **TSP**

**Reduction checklist**:
1. The transformation from A-instance to B-instance is computable in polynomial time.
2. A-instance is YES ⟺ B-instance is YES.
3. The starting problem A is already known to be NP-hard.

## Why It Matters

Reduction-based proofs are the primary tool for classifying new computational problems as NP-hard. Once a problem is classified NP-hard, the research agenda shifts: pursue approximation algorithms, exploit special structure (fixed-parameter tractability), or use heuristics — do not invest in finding a polynomial-time exact algorithm. The ability to construct and verify reductions is therefore a core skill in algorithm design and complexity theory.

## QnA Seeds

- Q: Why does the reduction go from the known NP-hard problem to the new problem, not the other way around?
- Q: What two conditions must a polynomial-time reduction from A to B satisfy?
- Q: If A ≤ₚ B and A is NP-hard, what does this tell us about B?
- Q: Why is 3-SAT a common starting point for NP-hardness proofs?
