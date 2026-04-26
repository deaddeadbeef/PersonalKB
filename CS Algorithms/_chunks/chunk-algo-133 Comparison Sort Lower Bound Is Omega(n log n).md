---
id: chunk-algo-133
type: chunk
source: "[[raw-algo-024]]"
source_loc: "Non-Comparison Sorting - Key Claims"
topic: "sorting"
claim: "The Omega(n log n) comparison sort lower bound is information-theoretic: the decision tree has >= n! leaves requiring height >= ceil(log2(n!)) = Theta(n log n); this is tight (merge sort, heapsort) and model-dependent."
confidence: verified
supports:
  - "[[Sorting Lower Bounds]]"
  - "[[Decision Tree Model]]"
tags:
  - cs-algorithms
  - cs-algorithms/sorting
  - chunk
up: "[[CS Algorithms]]"
---
# Comparison Sort Lower Bound Is Omega(n log n)

## Context

Any comparison sort is modeled as a binary decision tree where internal nodes are comparisons and leaves are permutations. With n! permutations, height h >= log2(n!) = n log2 n - n log2 e + O(log n) = Theta(n log n) by Stirling. Merge sort and heapsort achieve this bound. The result applies only to the comparison model—algorithms using indexing or arithmetic on keys (counting sort, radix sort) can beat it.

## Why It Matters

This is one of the cleanest information-theoretic arguments in CS, proving merge sort and heapsort are asymptotically optimal among comparison sorts and motivating non-comparison approaches.

## QnA Seeds

- Q: Why must comparison sorts make Theta(n log n) comparisons?
- Q: What does the decision tree model assume?
- Q: Why doesn't the bound apply to counting or radix sort?