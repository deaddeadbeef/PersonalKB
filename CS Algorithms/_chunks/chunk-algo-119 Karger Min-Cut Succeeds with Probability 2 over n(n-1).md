---
id: chunk-algo-119
type: chunk
source: "[[raw-algo-020]]"
source_loc: "Randomized Algorithms - Key Claims"
topic: "randomized-algorithms"
claim: "Karger's contraction algorithm finds a minimum cut with probability >= 2/(n(n-1)) per trial; O(n^2 log n) repetitions yield the min-cut with high probability, improved to O(n^2 log^3 n) total time by Karger-Stein's recursive refinement."
confidence: verified
supports:
  - "[[Randomized Algorithms]]"
  - "[[Graph Algorithms]]"
tags:
  - cs-algorithms
  - cs-algorithms/randomized-algorithms
  - chunk
up: "[[CS Algorithms]]"
---
# Karger Min-Cut Succeeds with Probability 2 over n(n-1)

## Context

The algorithm contracts uniformly random edges until two vertices remain; edges between the super-vertices form a cut. Success probability >= 2/(n(n-1)) because at each step, the min-cut has >= n_i - 2 safe edges. For n=100, one trial succeeds with >= 0.02%. Running n(n-1)/2 * ln n ~ 22,800 trials finds the min-cut with probability >= 1-1/n. Karger-Stein contracts to n/sqrt(2) then branches into two independent trials, reducing total time from O(n^4 log n) to O(n^2 log^3 n).

## Why It Matters

Karger's algorithm is a landmark result showing that a simple random process solves a fundamental graph problem. It introduced the contraction technique and amplification by repetition.

## QnA Seeds

- Q: What is Karger's per-trial success probability?
- Q: How many trials for high-probability min-cut?
- Q: How does Karger-Stein improve the basic algorithm?