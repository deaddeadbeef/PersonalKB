---
id: chunk-algo-117
type: chunk
source: "[[raw-algo-020]]"
source_loc: "Randomized Algorithms - Key Claims"
topic: "randomized-algorithms"
claim: "Randomized quicksort selects pivots uniformly at random, achieving expected 2n*H_n ~ 2n ln n ~ 1.39n log2 n comparisons for any input, eliminating adversarial worst cases while exceeding 4n ln n with probability at most 1/n."
confidence: verified
supports:
  - "[[Quicksort]]"
  - "[[Randomized Algorithms]]"
tags:
  - cs-algorithms
  - cs-algorithms/randomized-algorithms
  - chunk
up: "[[CS Algorithms]]"
---
# Randomized Quicksort Expected 2n ln n Comparisons

## Context

The analysis uses indicator variables: X_ij = 1 if elements i and j (sorted order) are compared, giving Pr[X_ij=1] = 2/(j-i+1). By linearity of expectation, E[comparisons] = 2n*H_n ~ 2n ln n. Exceeding 4n ln n has probability at most 1/n by Markov's inequality. This is Las Vegas: always correct, only runtime is random. The 1.39 factor vs log2 n explains the gap from the information-theoretic lower bound, yet quicksort wins in practice via cache efficiency.

## Why It Matters

Randomized quicksort's analysis via linearity of expectation is one of the most elegant probabilistic arguments in CS. The algorithm remains the fastest general-purpose comparison sort in practice.

## QnA Seeds

- Q: What is the exact expected comparison count for randomized quicksort?
- Q: Why does random pivot selection eliminate adversarial worst cases?
- Q: What is the probability of exceeding 4n ln n comparisons?