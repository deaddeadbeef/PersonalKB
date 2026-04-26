---
id: chunk-algo-102
type: chunk
source: "[[raw-algo-016]]"
source_loc: "Dynamic Programming Principles - Key Claims"
topic: "dynamic-programming"
claim: "The longest common subsequence of two strings of lengths m and n is computed in O(mn) time using the recurrence LCS[i][j] = LCS[i-1][j-1]+1 if characters match, else max(LCS[i-1][j], LCS[i][j-1]), with space reducible to O(min(m,n)) by retaining only two rows."
confidence: verified
supports:
  - "[[Dynamic Programming]]"
  - "[[Longest Common Subsequence]]"
tags:
  - cs-algorithms
  - cs-algorithms/dynamic-programming
  - chunk
up: "[[CS Algorithms]]"
---
# LCS Computed in O(mn) Time and O(min(m,n)) Space

## Context

The LCS DP fills an (m+1) x (n+1) table where entry LCS[i][j] represents the length of the longest common subsequence of the first i characters of string X and first j characters of string Y. Each cell depends only on three neighbors: above, left, and diagonal. This dependency structure means only two rows are needed at any time, reducing space from O(mn) to O(min(m,n)) by iterating along the shorter dimension. Reconstructing the actual subsequence requires the full table or O(mn) additional backtracking storage.

## Why It Matters

LCS is a foundational DP problem in bioinformatics (sequence alignment), diff utilities (computing file differences), and version control systems. The space optimization to O(min(m,n)) is a practical technique applicable to many two-sequence DP problems.

## QnA Seeds

- Q: What is the LCS recurrence relation?
- Q: How can LCS space be reduced from O(mn) to O(min(m,n))?
- Q: Why does reconstructing the actual LCS require the full DP table?