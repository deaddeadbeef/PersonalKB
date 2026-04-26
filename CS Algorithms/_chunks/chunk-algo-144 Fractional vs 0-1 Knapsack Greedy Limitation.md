---
id: chunk-csa-144
type: chunk
source: "[[Cormen 2022 - Greedy Algorithms]]"
source_loc: "Knapsack Problems"
topic: "greedy"
claim: "Fractional knapsack admits a greedy O(n log n) solution by value-per-weight ratio, but 0-1 knapsack requires DP in O(nW) pseudo-polynomial time"
confidence: verified
supports:
  - "[[Greedy Algorithms]]"
  - "[[Knapsack Problem]]"
tags:
  - csa
  - csa/greedy
  - chunk
up: "[[CS Algorithms]]"
---
# Greedy — Fractional knapsack is greedy but 0-1 knapsack requires DP

## Context

The fractional knapsack problem allows splitting items and admits a greedy solution: sort items by value-per-weight ratio in decreasing order and take as much as possible of each item until the knapsack is full, running in O(n log n). The 0-1 knapsack problem (items are indivisible) does not satisfy the greedy choice property—the value-per-weight strategy can fail because taking a high-ratio item may prevent taking a combination of items with greater total value. The 0-1 variant requires dynamic programming in O(nW) pseudo-polynomial time where W is the capacity.

## Why It Matters

This contrast demonstrates that small problem changes can invalidate greedy approaches, making it a critical example for understanding when greedy fails and DP is necessary.

## QnA Seeds

- Q: Why does the greedy value-per-weight strategy fail for 0-1 knapsack?
- Q: What is the time complexity of the greedy fractional knapsack solution?
- Q: Why is O(nW) for 0-1 knapsack called pseudo-polynomial?
