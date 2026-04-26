---
tags:
  - csa
  - csa/study
  - csa/complexity
up: "[[Algorithms Study Index]]"
---
# Complexity Theory — Review Drill

Active-recall drill covering computational complexity classes, undecidability, NP-completeness, and approximation algorithms.

**Canon pages:** [[P vs NP]] · [[NP Completeness]] · [[Halting Problem]] · [[Approximation Algorithms]]

---

## How to Use

Complexity concepts require precise language. For each question, aim to state both the definition and the significance before checking the canonical page.

---

## Core Recall

**P vs NP**

Q: Define the complexity class P.
A: P is the set of decision problems solvable by a deterministic Turing machine in polynomial time — i.e., there exists an algorithm running in $O(nᵏ)$ for some constant k. These are the problems considered "efficiently solvable."

Q: Define the complexity class NP.
A: NP is the set of decision problems where a proposed solution (certificate) can be *verified* in polynomial time. Equivalently, NP is the set of problems solvable by a non-deterministic Turing machine in polynomial time.

Q: State the P vs NP question precisely.
A: Is P = NP? That is, does the ability to verify a solution in polynomial time imply the ability to *find* a solution in polynomial time? It is one of the Millennium Prize Problems — unsolved and widely believed to be P ≠ NP.

Q: What would it mean if P = NP?
A: Every problem whose solution can be quickly verified could also be quickly solved. This would revolutionise cryptography (public-key encryption relies on problems believed outside P), optimisation, and AI — many currently hard problems would become tractable.

---

**NP-Completeness**

Q: Define NP-hard.
A: A problem X is NP-hard if every problem in NP can be reduced to X in polynomial time. NP-hard problems are at least as hard as the hardest problems in NP. They may not be in NP themselves (e.g., the Halting Problem is NP-hard but undecidable).

Q: Define NP-complete.
A: A problem X is NP-complete if: (1) X ∈ NP (solutions can be verified in polynomial time), and (2) X is NP-hard (every NP problem reduces to X in polynomial time). NP-complete problems are the hardest problems in NP.

Q: What is a polynomial reduction, and why is it the right notion of reduction for NP?
A: A polynomial reduction from problem A to problem B is a polynomial-time algorithm that transforms instances of A into instances of B, such that the answer is preserved (yes → yes, no → no). Polynomial reductions compose, so if B ∈ P then A ∈ P. They capture "B is at least as hard as A."

Q: What was the first problem proved NP-complete?
A: Boolean Satisfiability (SAT) — Cook-Levin theorem (1971/1972). SAT asks: given a Boolean formula, does there exist an assignment of variables that makes it true? The proof showed every NP problem can be reduced to SAT.

Q: How do you prove a new problem X is NP-complete?
A: 1. Show X ∈ NP (give a polynomial-time verifier). 2. Show X is NP-hard: choose a known NP-complete problem Y and give a polynomial reduction from Y to X. If Y reduces to X and Y is NP-hard, then X is NP-hard.

Q: Give three examples of NP-complete problems.
A: SAT (Boolean satisfiability), Vertex Cover (minimum vertex cover in a graph), Travelling Salesman Problem (decision version: is there a tour of length ≤ k?).

---

**Halting Problem and Undecidability**

Q: State the Halting Problem.
A: Given a description of a program P and an input I, does P halt (terminate) on input I? The Halting Problem is to decide this for all (P, I) pairs.

Q: Prove the Halting Problem is undecidable (Turing's diagonalisation argument sketch).
A: Suppose a decider H(P, I) exists that returns YES/NO. Construct D(P): runs H(P, P); if H says "halts," D loops forever; if H says "loops forever," D halts. Now run D(D): H(D, D) = YES implies D loops (contradicts YES); H(D, D) = NO implies D halts (contradicts NO). Contradiction — H cannot exist.

Q: What does Rice's Theorem state?
A: Any non-trivial semantic property of programs is undecidable. A semantic property is one about what the program *computes* (e.g., "does it output 42?"); non-trivial means some programs have it and some do not. No general algorithm can decide such properties.

Q: What is the practical implication of Rice's Theorem?
A: No program analysis tool can be both complete and sound for non-trivial semantic properties. Compilers, static analysers, and linters must make trade-offs: either accept some false positives (conservatively safe) or miss some true bugs (unsound).

---

**Approximation Algorithms**

Q: What is an α-approximation algorithm?
A: For a minimisation problem: an algorithm guaranteed to return a solution with cost ≤ α · OPT, where OPT is the true optimal cost and α ≥ 1. Smaller α is better; α = 1 is exact. The ratio α is a worst-case guarantee over all instances.

Q: Why are approximation algorithms a meaningful response to NP-completeness?
A: If a problem is NP-complete, no polynomial-time exact algorithm is known. Approximation algorithms provide polynomial-time solutions with a *provable* quality guarantee — a principled middle ground between exact (exponential) and heuristic (no guarantee).

Q: Describe the 2-approximation for Vertex Cover and prove its ratio.
A: Algorithm: maintain a set C = ∅; while an uncovered edge (u, v) exists, add both u and v to C. Proof: the edges selected form a matching M (no two share a vertex). OPT ≥ |M| (any cover must include ≥ 1 endpoint per matching edge). |C| = 2|M| ≤ 2 · OPT. □

Q: State the proof template for approximation algorithms.
A: 1. Identify an intermediate bound B computable from the instance. 2. Prove OPT ≥ B (the bound is a lower bound on optimal). 3. Prove ALG ≤ α · B (the algorithm output is bounded in terms of B). 4. Conclude ALG ≤ α · OPT by transitivity.

Q: Describe the list scheduling approximation for load balancing.
A: Assign each job to the currently least-loaded machine. Achieves approximation ratio (2 − 1/m) for m machines. Proof: let W = Σpₖ, and let j be the last-finishing job. Before j is assigned, only W − pⱼ work has been scheduled, so the chosen machine's prior load is at most (W − pⱼ)/m. Therefore makespan T ≤ (W − pⱼ)/m + pⱼ = W/m + (1 − 1/m)pⱼ ≤ OPT + (1 − 1/m)OPT = (2 − 1/m)OPT, using W/m ≤ OPT and pⱼ ≤ OPT.

Q: Does a 2-approximation algorithm for Vertex Cover imply P = NP or contradict NP-completeness?
A: No. Approximation algorithms do not resolve P vs NP. They are polynomial algorithms, but they do not find the exact optimal solution. The conjecture that P ≠ NP concerns *exact* polynomial-time solutions.

---

## Compare and Contrast

**P vs NP vs NP-Complete vs NP-Hard**

| Class | Definition | Relationship |
|-------|-----------|-------------|
| P | Decidable in polynomial time | P ⊆ NP |
| NP | Verifiable in polynomial time | P ⊆ NP; NP-complete ⊆ NP |
| NP-Hard | Every NP problem reduces to it | NP-complete ⊆ NP-hard |
| NP-Complete | In NP and NP-hard | The intersection of NP and NP-hard |

If any NP-complete problem is in P, then P = NP.

**Decidable vs Undecidable**

| | Decidable | Semi-decidable | Undecidable |
|--|-----------|---------------|-------------|
| Definition | Always halts with YES/NO | Halts with YES; may loop on NO | No algorithm exists |
| Example | Sorting, primality | Membership in a RE language | Halting Problem, Rice's Theorem |
| Relation to P | P ⊆ decidable | — | Outside decidable |

**Exact vs Approximation vs Heuristic**

| Approach | Polynomial time | Quality guarantee | When to use |
|----------|----------------|-------------------|-------------|
| Exact | No (for NP-hard) | Optimal | Small n; exact optimum required |
| Approximation | Yes | Within α · OPT | Large n; provable bound acceptable |
| Heuristic | Yes | None | Very large n; empirical performance sufficient |

---

## Common Mistakes

1. **NP ≠ "not polynomial"** — NP stands for *non-deterministic polynomial*. It means verifiable in polynomial time. Many NP problems are also in P (NP just means "verifiable", not "hard").

2. **NP-hard vs NP-complete** — NP-hard problems may not be in NP (e.g., the Halting Problem is NP-hard but not in NP because it is undecidable). NP-complete problems are NP-hard *and* in NP.

3. **Reduction direction** — to prove X is NP-hard, reduce a *known* NP-hard problem Y *to* X (not X to Y). The direction means "if X were easy, Y would be easy," which is a contradiction.

4. **Approximation ratio ≥ 1 for minimisation** — α = 0.9 would mean the algorithm finds a solution *better* than optimal, which is impossible. For minimisation, α ≥ 1; for maximisation, the ratio is ≤ 1 or expressed as 1/α ≤ 1.

5. **Rice's Theorem scope** — Rice's Theorem applies to *semantic* properties (what the program computes), not *syntactic* ones (what the code looks like). "Does the program contain a loop?" is syntactic and decidable.

6. **Approximation does not prove P = NP** — having a polynomial approximation algorithm for an NP-complete problem does not break NP-completeness; it is a polynomial algorithm for a *related* (easier) problem, not the exact problem.

---

## Links Back

- [[P vs NP]] — definitions of P, NP, the open question, implications
- [[NP Completeness]] — NP-hard, NP-complete, Cook-Levin, reductions, examples
- [[Halting Problem]] — undecidability, Turing diagonalisation, Rice's Theorem
- [[Approximation Algorithms]] — α-approximation, vertex cover, load balancing, proof template
