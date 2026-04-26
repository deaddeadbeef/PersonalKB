---
id: chunk-csa-015
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 7"
topic: "strings"
claim: "LCS dynamic programming fills an m by n table bottom-up in Theta(mn) by comparing characters at each prefix boundary"
confidence: verified
supports:
  - "[[LCS - Longest Common Subsequence]]"
  - "[[Dynamic Programming]]"
tags:
  - csa
  - csa/strings
  - chunk
up: "[[CS Algorithms]]"
---
# Strings — LCS dynamic programming fills an m×n table in Theta(mn)

## Context

l[i,j] = length of the LCS of X[1..i] and Y[1..j]. Recurrence: if X[i] = Y[j], then l[i,j] = l[i−1,j−1] + 1; otherwise l[i,j] = max(l[i−1,j], l[i,j−1]). Fill the table row-by-row (or column-by-column) in Θ(mn). The value l[m,n] is the LCS length. Reconstruct the actual subsequence by backtracking through the table following the arrows: if X[i]=Y[j] go diagonal; otherwise go in the direction of the larger neighbour. Application: DNA strand comparison for evolutionary distance and mutation analysis.

## Why It Matters

LCS is the canonical introduction to 2D dynamic programming — a richer problem structure than 1D DP. Understanding the recurrence derivation (how to reduce LCS(X,Y) to sub-LCS problems) builds the reasoning pattern used for edit distance, string alignment, and many other DP formulations.

## QnA Seeds

- Q: What is the recurrence for LCS?
- Q: How do you reconstruct the actual LCS from the filled table?
- Q: Why is naïve LCS exponential but DP is polynomial?
