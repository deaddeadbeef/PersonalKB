---
id: chunk-csa-182
type: chunk
source: "[[Bentley 1984 - Maximum Subarray]]"
source_loc: "DP Recurrence"
topic: "dynamic-programming"
claim: "Kadane's DP recurrence current_max = max(A[i], current_max + A[i]) captures the binary decision to extend the current subarray or start a new one at each position"
confidence: verified
supports:
  - "[[Kadane Algorithm]]"
  - "[[Dynamic Programming]]"
tags:
  - csa
  - csa/dynamic-programming
  - chunk
up: "[[CS Algorithms]]"
---
# DP — Kadane's recurrence: extend current subarray or restart at each position

## Context

The key insight is that at each position i, there are exactly two choices: extend the maximum subarray ending at i-1 by including A[i], or start a fresh subarray beginning at A[i]. If current_max + A[i] < A[i] (equivalently, current_max < 0), starting fresh is better. This DP recurrence collapses the O(n^2) brute-force examination of all subarrays into a single linear scan. The recurrence defines a 1D DP table where each entry depends only on the previous entry, enabling O(1) space via a rolling variable.

## Why It Matters

Understanding this recurrence at a deep level reveals how DP identifies and exploits the problem's optimal substructure, a pattern that transfers to many other DP problems.

## QnA Seeds

- Q: When does Kadane's algorithm decide to start a new subarray?
- Q: How does the recurrence reduce O(n^2) subarray enumeration to O(n)?
- Q: Why does the recurrence need only O(1) space?
