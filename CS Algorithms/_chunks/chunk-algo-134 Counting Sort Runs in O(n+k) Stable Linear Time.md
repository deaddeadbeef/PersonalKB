---
id: chunk-algo-134
type: chunk
source: "[[raw-algo-024]]"
source_loc: "Non-Comparison Sorting - Key Claims"
topic: "sorting"
claim: "Counting sort sorts n integers in [0,k] in O(n+k) time using count array C[0..k] and prefix sums; stability is achieved by right-to-left placement into the output array, making it the ideal radix sort subroutine."
confidence: verified
supports:
  - "[[Counting Sort]]"
  - "[[Radix Sort]]"
tags:
  - cs-algorithms
  - cs-algorithms/sorting
  - chunk
up: "[[CS Algorithms]]"
---
# Counting Sort Runs in O(n+k) Stable Linear Time

## Context

Three passes: (1) count occurrences C[i]; (2) prefix sums so C[i] = final position of last value-i element; (3) iterate input right-to-left, placing A[j] at output[C[A[j]]] and decrementing C[A[j]]. Right-to-left preserves relative order of equal keys (stability). Time and space are O(n+k). When k=O(n), this is linear; when k >> n, counting sort becomes impractical and comparison sorts are preferable.

## Why It Matters

Counting sort is the foundation for radix sort and the key example of bypassing Omega(n log n). Its stability is not incidental—it is the critical invariant that makes LSD radix sort correct.

## QnA Seeds

- Q: How does counting sort achieve O(n+k)?
- Q: Why does right-to-left placement make counting sort stable?
- Q: When is counting sort impractical?