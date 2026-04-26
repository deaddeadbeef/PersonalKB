---
id: chunk-algo-103
type: chunk
source: "[[raw-algo-016]]"
source_loc: "Dynamic Programming Principles - Key Claims"
topic: "dynamic-programming"
claim: "The 0/1 knapsack problem with n items and integer capacity W is solvable in O(nW) time via DP, but this is pseudo-polynomial because W is exponential in its bit representation (log W bits), making the algorithm exponential in input encoding length."
confidence: verified
supports:
  - "[[Dynamic Programming]]"
  - "[[NP-Completeness]]"
tags:
  - cs-algorithms
  - cs-algorithms/dynamic-programming
  - chunk
up: "[[CS Algorithms]]"
---
# 0-1 Knapsack Is Pseudo-Polynomial in O(nW)

## Context

The knapsack DP table has n rows and W+1 columns, each entry computed in O(1). For n=100 items and W=10,000, this is 1,000,000 entries—tractable in practice. However, the input size is O(n log W) bits, not O(nW), because W is encoded in binary. The running time O(nW) is exponential in log W, making this pseudo-polynomial. This is why knapsack is NP-complete: if W were encoded in unary, the algorithm would be polynomial. Space can be optimized to O(W) using a single row scanned right-to-left.

## Why It Matters

Understanding pseudo-polynomial time is critical for recognizing the boundary between P and NP-complete problems. Knapsack is the canonical example of a problem that is NP-complete yet efficiently solvable when numeric parameters are small.

## QnA Seeds

- Q: Why is the O(nW) knapsack algorithm pseudo-polynomial rather than polynomial?
- Q: How large is the knapsack DP table for n=100 and W=10,000?
- Q: How is knapsack space optimized from O(nW) to O(W)?