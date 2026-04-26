---
id: chunk-csa-183
type: chunk
source: "[[Bentley 1984 - Maximum Subarray]]"
source_loc: "Divide and Conquer"
topic: "divide-and-conquer"
claim: "The divide-and-conquer maximum subarray solution achieves O(n log n) via recurrence T(n) = 2T(n/2) + O(n) but is suboptimal compared to Kadane's linear scan"
confidence: verified
supports:
  - "[[Maximum Subarray]]"
  - "[[Divide and Conquer]]"
tags:
  - csa
  - csa/divide-and-conquer
  - chunk
up: "[[CS Algorithms]]"
---
# Divide-and-Conquer — Maximum subarray O(n log n) via midpoint crossing

## Context

The divide-and-conquer approach splits the array in half, recursively finds the maximum subarray in each half, and finds the maximum subarray crossing the midpoint in O(n) by extending left and right from the midpoint. The overall maximum is the largest of these three candidates. The recurrence T(n) = 2T(n/2) + O(n) resolves to O(n log n) by Master Theorem Case 2. While clean and illustrative of the paradigm, it is suboptimal compared to Kadane's O(n) dynamic programming solution.

## Why It Matters

This problem perfectly illustrates how different algorithmic paradigms (brute force O(n^2), divide-and-conquer O(n log n), DP O(n)) yield progressively better solutions, making it ideal for teaching.

## QnA Seeds

- Q: What are the three candidate subarrays in the divide-and-conquer approach?
- Q: What Master Theorem case applies to the maximum subarray recurrence?
- Q: Why is divide-and-conquer suboptimal here compared to DP?
