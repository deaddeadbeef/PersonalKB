---
id: chunk-algo-120
type: chunk
source: "[[raw-algo-020]]"
source_loc: "Randomized Algorithms - Atomic Facts"
topic: "randomized-algorithms"
claim: "Chernoff bounds show that for n independent Bernoulli trials with expected sum mu, P(X >= (1+delta)*mu) decays exponentially in mu; for delta=1, P(X >= 2mu) <= (e/4)^mu ~ 0.68^mu."
confidence: verified
supports:
  - "[[Randomized Algorithms]]"
  - "[[Probability Theory]]"
tags:
  - cs-algorithms
  - cs-algorithms/randomized-algorithms
  - chunk
up: "[[CS Algorithms]]"
---
# Chernoff Bounds Give Exponential Tail Decay

## Context

The multiplicative Chernoff bound P(X >= (1+delta)*mu) <= (e^delta/(1+delta)^(1+delta))^mu gives exponential decay in mu. The simplified form P(X >= (1+delta)*mu) <= e^(-mu*delta^2/3) for delta in [0,1] is often more convenient. Applications pervade randomized algorithms: load balancing (max load O(log n/log log n) w.h.p.), randomized rounding, and universal hashing analysis. Chernoff bounds are strictly stronger than Markov's and Chebyshev's when variables are independent.

## Why It Matters

Chernoff bounds are the workhorse tool for 'with high probability' guarantees in randomized algorithms. Every analyst needs them for concentration results in hashing, load balancing, and random graph properties.

## QnA Seeds

- Q: What is the Chernoff bound for P(X >= 2mu)?
- Q: When are Chernoff bounds applicable vs Chebyshev?
- Q: How are Chernoff bounds used in load balancing analysis?