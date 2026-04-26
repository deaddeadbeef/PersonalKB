---
id: chunk-csa-001
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 1"
topic: "analysis"
claim: "Algorithm correctness exists on a spectrum from exact to probabilistic to approximation"
confidence: verified
supports:
  - "[[Algorithm Definition]]"
tags:
  - csa
  - csa/analysis
  - chunk
up: "[[CS Algorithms]]"
---
# Analysis — Algorithm correctness exists on a spectrum from exact to probabilistic to approximation

## Context

Cormen introduces correctness as more nuanced than "always right or wrong." Three flavours: (1) **exact correctness** — the algorithm produces the right answer for every valid input; (2) **probabilistic correctness** — the algorithm may be wrong, but the error probability can be bounded to an arbitrarily small value (e.g., Miller-Rabin primality testing can be run k times to reduce error below 4⁻ᵏ); (3) **approximation** — the algorithm returns a solution within a provable factor α of optimal, redefining correctness as "close enough."

## Why It Matters

Understanding this spectrum prevents over-demanding from algorithms. Requiring exact correctness for every problem would make many practically useful algorithms inadmissible. Cryptographic primality testing relies on probabilistic correctness; routing and scheduling often use approximation algorithms for NP-complete variants.

## QnA Seeds

- Q: What is an approximation algorithm and when is it considered correct?
- Q: How does Miller-Rabin primality testing handle the correctness question?
- Q: What is the difference between exact and probabilistic algorithm correctness?
