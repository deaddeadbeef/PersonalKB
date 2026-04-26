---
id: chunk-csa-008
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 4"
topic: "sorting"
claim: "Radix sort applies a stable counting sort to each digit from least-significant to most-significant in Theta(d(m+n))"
confidence: verified
supports:
  - "[[Radix Sort]]"
  - "[[Sorting Overview]]"
tags:
  - csa
  - csa/sorting
  - chunk
up: "[[CS Algorithms]]"
---
# Sorting — Radix sort applies stable counting sort digit-by-digit from least to most significant

## Context

Radix sort treats each key as a d-digit number in base m. It applies a stable sort (counting sort) on digit position 1 (least significant), then digit 2, …, then digit d (most significant). Correctness relies on stability: when two elements have the same digit at position k, their relative order from the previous pass is preserved, so lower digits are correctly handled. Total time Θ(d(m+n)); for fixed d and base, this is Θ(n). Example from the book: airline confirmation codes (6 alphanumeric characters, base 36) sorted in 6 passes.

## Why It Matters

Radix sort demonstrates a composition principle: build a complex algorithm from a simpler stable subroutine. It also shows that the digit representation of data (not just the comparison ordering) can be exploited algorithmically. In practice it is competitive with merge sort for fixed-width integer keys.

## QnA Seeds

- Q: Why does radix sort process digits from least significant to most significant?
- Q: What happens if the subroutine used by radix sort is not stable?
- Q: What is the running time of radix sort on 32-bit integers?
