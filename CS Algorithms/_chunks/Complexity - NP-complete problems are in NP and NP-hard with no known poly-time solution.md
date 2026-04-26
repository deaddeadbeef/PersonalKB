---
id: chunk-csa-021
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 10"
topic: "complexity"
claim: "NP-complete problems are both in NP and NP-hard — no polynomial-time algorithm is known for any of them, and solving one in poly-time would solve all of NP"
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
# Complexity — NP-complete problems are both in NP and NP-hard with no known poly-time solution

## Context

A problem Q is NP-complete if: (1) Q ∈ NP — a proposed solution can be verified in polynomial time; (2) Q is NP-hard — every problem in NP can be polynomially reduced to Q. Cook and Levin (independently, 1971) proved 3-SAT is NP-complete — the first such result. Since then, hundreds of problems have been shown NP-complete by polynomial reduction chains: Hamiltonian cycle, TSP, graph colouring, vertex cover, clique, subset sum. If any one NP-complete problem is solvable in polynomial time, then P = NP and *all* NP problems become tractable.

## Why It Matters

Recognising that a problem is NP-complete stops wasted effort searching for a polynomial algorithm that does not exist (or would prove P=NP). It redirects effort toward approximation algorithms, heuristics, or special-case solvers. NP-completeness results are also practically important for cryptography: many cryptographic hardness assumptions are believed equivalent to NP-hard problems.

## QnA Seeds

- Q: What is the difference between NP-hard and NP-complete?
- Q: What does it mean to polynomial-reduce problem A to problem B?
- Q: Why does solving one NP-complete problem in poly-time solve all of them?
