---
id: chunk-algo-109
type: chunk
source: "[[raw-algo-018]]"
source_loc: "NP-Completeness Theory - Key Claims"
topic: "complexity"
claim: "The Cook-Levin theorem (1971) proves Boolean satisfiability (SAT) is NP-complete by encoding any nondeterministic Turing machine computation of polynomial length as a polynomial-size Boolean formula satisfiable iff the machine accepts."
confidence: verified
supports:
  - "[[NP-Completeness]]"
  - "[[Satisfiability]]"
tags:
  - cs-algorithms
  - cs-algorithms/complexity
  - chunk
up: "[[CS Algorithms]]"
---
# Cook-Levin Theorem Proves SAT Is NP-Complete

## Context

The proof constructs a Boolean formula encoding the computation tableau: variables represent state, head position, and tape contents at each step, and clauses enforce the transition function, initial configuration, and acceptance. The formula has polynomial size because the computation runs in polynomial time. This establishes SAT as the first NP-complete problem. Karp (1972) then showed 21 further NP-complete problems via reductions from SAT.

## Why It Matters

The Cook-Levin theorem is the cornerstone of computational complexity theory, providing the first NP-complete problem and enabling the entire NP-completeness reduction framework.

## QnA Seeds

- Q: What does the Cook-Levin theorem establish about SAT?
- Q: How does the proof encode a TM computation as a Boolean formula?
- Q: Why is the resulting formula polynomial in size?