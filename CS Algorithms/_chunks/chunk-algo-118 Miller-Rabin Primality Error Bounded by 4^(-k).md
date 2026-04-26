---
id: chunk-algo-118
type: chunk
source: "[[raw-algo-020]]"
source_loc: "Randomized Algorithms - Key Claims"
topic: "randomized-algorithms"
claim: "Miller-Rabin is a Monte Carlo primality test with per-witness error at most 1/4; k independent witnesses give error 4^(-k), yielding effective certainty at k=40 (error < 10^(-24)) in O(k log^2 n) time."
confidence: verified
supports:
  - "[[Randomized Algorithms]]"
  - "[[Primality Testing]]"
tags:
  - cs-algorithms
  - cs-algorithms/randomized-algorithms
  - chunk
up: "[[CS Algorithms]]"
---
# Miller-Rabin Primality Error Bounded by 4^(-k)

## Context

Miller-Rabin tests Fermat's little theorem with additional square-root checks. A composite n has at most n/4 'liars' giving error <= 1/4 per trial. With k=40 witnesses, error < 10^(-24)—far below hardware error probability. For a 2048-bit RSA candidate, this is ~10^6 operations, negligible vs key generation. Despite AKS (2002) being deterministic polynomial, Miller-Rabin remains preferred in practice for its simplicity and speed.

## Why It Matters

Miller-Rabin is the standard primality test in cryptographic systems (RSA, Diffie-Hellman). It exemplifies how Monte Carlo algorithms with tunable error can be more practical than deterministic alternatives.

## QnA Seeds

- Q: What is Miller-Rabin's error probability with k witnesses?
- Q: Why is Miller-Rabin preferred over deterministic AKS?
- Q: How many operations for a 2048-bit candidate?