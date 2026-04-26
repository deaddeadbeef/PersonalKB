---
id: chunk-algo-135
type: chunk
source: "[[raw-algo-024]]"
source_loc: "Non-Comparison Sorting - Key Claims"
topic: "sorting"
claim: "LSD radix sort applies stable counting sort on each digit from least to most significant in O(d(n+k)) time; for n integers in [0, n^c-1] with base n, this is O(cn) linear time when c is constant."
confidence: verified
supports:
  - "[[Radix Sort]]"
  - "[[Counting Sort]]"
tags:
  - cs-algorithms
  - cs-algorithms/sorting
  - chunk
up: "[[CS Algorithms]]"
---
# LSD Radix Sort Runs in O(d(n+k)) Digit-by-Digit

## Context

Processing digits position 0 to d-1, stability ensures elements with equal digit i retain their order from previous passes (sorted by digits 0 through i-1). Each pass costs O(n+k). Choice of radix k trades passes for per-pass cost: larger k reduces d = ceil(log_k(max)) but increases counting sort cost. For [0, n^c-1] with base n: d=c passes of O(2n) each = O(cn). MSD radix sort recursively partitions by most significant digit, enabling early termination.

## Why It Matters

LSD radix sort is the practical linear-time integer sorting algorithm, used in databases, suffix array construction, and GPU sorting. Its correctness depends entirely on per-digit sort stability.

## QnA Seeds

- Q: Why must the per-digit sort be stable for LSD radix sort?
- Q: How does radix choice k affect performance?
- Q: How does LSD radix sort achieve O(cn) for [0, n^c-1]?