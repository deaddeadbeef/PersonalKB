---
id: chunk-algo-104
type: chunk
source: "[[raw-algo-016]]"
source_loc: "Dynamic Programming Principles - Atomic Facts"
topic: "dynamic-programming"
claim: "Matrix chain multiplication for n matrices is solved in O(n^3) time and O(n^2) space by the recurrence m[i,j] = min over i<=k<j of (m[i,k] + m[k+1,j] + p_{i-1}*p_k*p_j), considering all split points to minimize scalar multiplications."
confidence: verified
supports:
  - "[[Dynamic Programming]]"
tags:
  - cs-algorithms
  - cs-algorithms/dynamic-programming
  - chunk
up: "[[CS Algorithms]]"
---
# Matrix Chain Multiplication Solved in O(n cubed)

## Context

Given a chain of n matrices with dimensions p_0 x p_1, ..., p_{n-1} x p_n, the DP table m[i,j] stores the minimum cost of multiplying matrices i through j, with base case m[i,i] = 0. The algorithm fills the table by increasing chain length. For n=20 matrices, at most 1,140 subproblems are evaluated. The brute-force approach enumerates Catalan number C(n-1) parenthesizations, growing exponentially as 4^n / n^(3/2).

## Why It Matters

Matrix chain multiplication illustrates the optimal-split-point DP pattern, applicable to BST optimization, polygon triangulation, and parser optimization. It demonstrates how DP reduces exponential enumeration to polynomial time.

## QnA Seeds

- Q: What is the recurrence for matrix chain multiplication?
- Q: How many subproblems does matrix chain DP evaluate for n matrices?
- Q: Why would brute-force enumeration of parenthesizations be exponential?