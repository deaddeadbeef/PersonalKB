---
id: chunk-csa-184
type: chunk
source: "[[Bentley 1984 - Maximum Subarray]]"
source_loc: "2D Extension"
topic: "dynamic-programming"
claim: "The 2D maximum subrectangle in an m-by-n matrix is solvable in O(m squared n) by fixing row pairs and applying Kadane's algorithm to column prefix sums"
confidence: verified
supports:
  - "[[Maximum Subarray]]"
  - "[[2D Dynamic Programming]]"
tags:
  - csa
  - csa/dynamic-programming
  - chunk
up: "[[CS Algorithms]]"
---
# DP — 2D maximum subrectangle O(m squared n) via Kadane on column sums

## Context

For an m x n matrix, fix all O(m^2) pairs of rows (top, bottom). For each pair, compute column prefix sums between those rows to produce a 1D array of column sums, then apply Kadane's algorithm in O(n) to find the maximum contiguous column range. The overall maximum across all row pairs is the answer. Total time is O(m^2 * n). This originated from Ulf Grenander's 2D image processing problem (finding the maximum-brightness rectangular region) that motivated Kadane's 1D solution.

## Why It Matters

The 2D extension shows how 1D algorithms can be lifted to higher dimensions through systematic reduction, a technique applicable to many array and matrix problems.

## QnA Seeds

- Q: How does the 2D maximum subrectangle reduce to 1D Kadane applications?
- Q: What is the time complexity of the 2D maximum subrectangle algorithm?
- Q: What was the original motivation for the maximum subarray problem?
