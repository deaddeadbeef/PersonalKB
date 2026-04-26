---
id: chunk-csa-181
type: chunk
source: "[[Bentley 1984 - Maximum Subarray]]"
source_loc: "Kadane Algorithm"
topic: "dynamic-programming"
claim: "Kadane's algorithm solves the maximum subarray problem in O(n) time and O(1) space with a single pass, which is optimal since every element must be examined"
confidence: verified
supports:
  - "[[Kadane Algorithm]]"
  - "[[Maximum Subarray]]"
tags:
  - csa
  - csa/dynamic-programming
  - chunk
up: "[[CS Algorithms]]"
---
# DP — Kadane's algorithm O(n) time O(1) space maximum subarray

## Context

Kadane's algorithm maintains current_max (maximum subarray sum ending at the current position) and best_max (global maximum). At each step: current_max = max(A[i], current_max + A[i])—either extend the previous subarray or start fresh. Initialize both to A[0] and iterate from index 1 to n-1. For all-negative arrays, it correctly returns the largest single element. The single pass and O(1) space make it optimal: every element must be examined at least once. To recover the actual subarray indices, track start and end positions, resetting start when a new subarray begins.

## Why It Matters

Kadane's algorithm is a canonical example of dynamic programming transforming a seemingly quadratic problem into linear time, and appears frequently in coding interviews and financial analysis.

## QnA Seeds

- Q: What is the DP recurrence in Kadane's algorithm?
- Q: How does Kadane's handle all-negative arrays correctly?
- Q: Why is O(n) optimal for the maximum subarray problem?
