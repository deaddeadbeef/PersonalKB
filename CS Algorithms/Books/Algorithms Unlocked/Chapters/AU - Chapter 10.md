---
id: au-ch-10
type: book-chapter
chapter: 10
book: "Algorithms Unlocked"
author: "Thomas H. Cormen"
status: processed
chunk_count: 3
source: "[[Cormen 2013 - Algorithms Unlocked]]"
tags:
  - csa
  - book-chapter
up: "[[Chapter Index]]"
confidence: verified
---
# AU — Chapter 10: Hard? Problems

## Summary

The final chapter tackles the deepest question in algorithmic theory: which problems are truly hard? Cormen begins with the Travelling Salesman Problem — with n stops, the number of possible routes is n!, which grows super-exponentially. He distinguishes tractable problems (solvable in polynomial time, class **P**) from problems whose solutions are merely *verifiable* in polynomial time (class **NP**). Every P problem is in NP; whether P = NP is the central unsolved question of computer science. The **Cook-Levin theorem** (1971) established that **3-SAT** is **NP-complete** — both in NP and at least as hard as any NP problem (NP-hard) via polynomial reduction. Hundreds of problems have since been shown NP-complete by reduction chains: Hamiltonian cycle, TSP, graph colouring, vertex cover, subset sum. If any one NP-complete problem is in P, then P = NP. When facing an NP-complete problem in practice: use exact algorithms with good average-case behaviour, **approximation algorithms** (polynomial-time with provable sub-optimal ratio), or heuristics. The chapter closes with **undecidability**: the **Halting Problem** — deciding whether an arbitrary program halts — has no algorithm at all. Turing's diagonalisation proof (1936) showed it is undecidable; undecidability is strictly harder than NP-completeness.

Cormen closes with a broader perspective: the theory of computational complexity, while abstract, shapes every practical algorithmic decision. Knowing that a problem is NP-complete redirects effort from a futile search for an exact polynomial algorithm toward approximations and heuristics. Knowing that some problems are undecidable sets absolute limits — no amount of engineering can produce a general halting detector or a complete program verifier. The boundary between the tractable, the intractable, and the impossible is the conceptual framework that gives meaning to all the efficient algorithms studied in the rest of the book.

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| Class P | Decision problems solvable in polynomial time |
| Class NP | Decision problems with polynomial-time verifiable certificates |
| P vs NP | Is every verifiable problem also efficiently solvable? Open question |
| Polynomial reduction | Transform A to B in poly time; if A hard and A ≤ₚ B, then B is hard |
| NP-complete | In NP and NP-hard; hardest problems in NP |
| Cook-Levin theorem | 3-SAT is NP-complete — first such proof (1971) |
| Approximation algorithm | Polynomial time; solution within factor α of optimal |
| Halting Problem | No algorithm can decide whether an arbitrary program halts |
| Undecidability | Problems for which no algorithm exists at all |

## Chunk Candidates

- [x] [[Complexity - NP-complete problems are in NP and NP-hard with no known poly-time solution]]
- [x] [[Complexity - The Halting Problem is undecidable via Turing's diagonalisation argument]]
- [x] [[Complexity - Approximation algorithms trade optimality for polynomial running time with a provable ratio]]

## Wiki Pages Seeded

- [[P vs NP]] — definitions, open question, implications
- [[NP Completeness]] — reductions, Cook-Levin, classic NP-complete problems
- [[Approximation Algorithms]] — α-approximation, vertex cover example, hardness of approximation
- [[Halting Problem]] — Turing's diagonalisation proof, undecidability vs NP-completeness

## References

See [[CS Algorithms/Sources/Sources Index#Cormen 2013|Cormen 2013]].
