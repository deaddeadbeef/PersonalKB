---
tags:
  - csa
  - moc
up: '[[CS Algorithms]]'
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Complexity Theory Overview

> **One-line summary**: The study of what computers fundamentally can and cannot compute efficiently — covering P vs NP, NP-completeness, undecidability, and approximation algorithms.

## 🎯 Intuition
**The Core Idea:** Not all problems are created equal — some are easy, some are hard, and some are impossible.
**Analogy:** A difficulty rating system for computational problems — P problems are "green circle" (easy), NP-complete problems are "double black diamond" (hard but doable with enough time), and undecidable problems are "closed trails" (no one can ever complete them).
**Why It Matters:** Complexity theory tells you when to optimise your algorithm, when to settle for an approximation, and when to stop trying entirely — saving you from chasing impossible solutions.

---

## ⚙️ Core Mechanics
### How It Works / Formal Definition

Complexity theory classifies decision problems by the computational resources (time, space) needed to solve them. The central hierarchy:

```
P  ⊆  NP  ⊆  PSPACE  ⊆  EXPTIME
```

### Key Properties

| Class | Definition | Example |
|-------|-----------|---------|
| **P** | Solvable in polynomial time | Sorting, shortest path |
| **NP** | Verifiable in polynomial time | 3-SAT, Hamiltonian Cycle |
| **NP-complete** | Hardest problems in NP (NP ∩ NP-hard) | 3-SAT, TSP, Vertex Cover |
| **NP-hard** | At least as hard as any NP problem | Halting Problem (also undecidable) |
| **Undecidable** | No algorithm exists | Halting Problem |

### Key Facts

**Common Distinctions:**

| Question | Answer |
|----------|--------|
| NP-hard vs NP-complete? | NP-hard = at least as hard as any NP problem (may not be in NP). NP-complete = NP-hard *and* in NP. |
| Undecidable vs intractable? | Undecidable = no algorithm exists. Intractable = algorithm exists but no known polynomial-time one. |
| Approximation vs heuristic? | Approximation has *proved* worst-case bounds. Heuristics do not. |
| P ⊆ NP — why? | Every problem solvable in polynomial time can be verified in polynomial time (trivially, by re-solving). |

---

## 🔬 Deep Dive
### Learn in This Order

1. [[P vs NP]] — definitions of P, NP, and co-NP; the central open question; implications if P = NP
2. [[NP Completeness]] — NP-hard vs NP-complete; Cook-Levin theorem; polynomial reductions
3. [[Halting Problem]] — Turing’s diagonalisation; undecidability; Rice’s Theorem
4. [[Approximation Algorithms]] — α-approximation; vertex-cover 2-approx; load-balancing; hardness of approximation

### In This Domain

| Page | One-line summary |
|------|-----------------|
| [[P vs NP]] | The central complexity question; class definitions; implications |
| [[NP Completeness]] | Reductions; Cook-Levin; NP-hard vs NP-complete distinction |
| [[Halting Problem]] | Undecidability; diagonalisation; limits of all computation |
| [[Approximation Algorithms]] | Polynomial-time algorithms with bounded sub-optimality |

### How to Navigate

- **First time here?** Start at [[P vs NP]] for the foundational definitions, then [[NP Completeness]] for the reduction technique.
- **Proving a problem is hard?** [[NP Completeness]] covers the reduction template.
- **Need to solve an NP-hard problem in practice?** [[Approximation Algorithms]] gives the theory of bounded-quality poly-time algorithms.
- **Limits of computation beyond NP?** [[Halting Problem]] covers undecidability and Rice’s Theorem.

### Edge Cases and Pitfalls
- **NP ≠ "non-polynomial"**: a pervasive misconception
- **Complexity classes are about worst-case**: a problem in NP might be easy on most inputs
- **Reductions go the "wrong" way intuitively**: to show Q is hard, reduce a known hard problem *to* Q

### Real-World Implications
- **Cryptography** ([[Cryptography Overview]]): RSA security rests on the conjectured hardness of factoring — directly tied to complexity theory
- **Graph algorithms** ([[Graphs Overview]]): TSP, clique, and graph colouring are canonical NP-complete problems
- **Foundations** ([[Foundations and Analysis Overview]]): Asymptotic notation and polynomial time are prerequisites

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Place these in the complexity hierarchy: sorting, 3-SAT, Halting Problem. Which is in P? NP-complete? Undecidable?
2. Is every NP-hard problem NP-complete? Give an example of one that is not.
3. A friend says "NP means the problem takes non-polynomial time." Correct them.

### Core Problems
1. Given a new problem Q, outline the steps to prove it NP-complete. What two things must you show?
2. Explain why the existence of an approximation algorithm for Vertex Cover does not imply P = NP.

### Challenge
1. Explain the significance of Ladner’s Theorem: if P ≠ NP, then there exist problems in NP that are neither in P nor NP-complete ("NP-intermediate"). Give a candidate natural problem.

---

*See also:* [[CS Algorithms]], [[Cryptography Overview]], [[Graphs Overview]], [[Foundations and Analysis Overview]]

## Supporting Chunks

*(This MOC page has no individual supporting chunks — see child pages.)*

## Related Domains

- **[[Cryptography Overview]]** — RSA security rests on the *conjectured* hardness of factoring (an NP-intermediate problem). Many cryptographic hardness assumptions link directly to complexity theory.
- **[[Graphs Overview]]** — Traveling Salesman, clique, and graph coloring are canonical NP-complete problems.
- **[[Foundations and Analysis Overview]]** — Asymptotic notation and the notion of polynomial time are prerequisites.
