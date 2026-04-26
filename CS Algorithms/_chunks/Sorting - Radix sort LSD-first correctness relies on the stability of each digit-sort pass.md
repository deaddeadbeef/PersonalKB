---
id: chunk-csa-046
type: chunk
source: "[[CP Algorithms - Online Reference]]"
source_loc: "Radix Sort article"
topic: "sorting"
claim: "Radix sort processes digits least-significant first, and correctness follows by induction on digit position: stability of each pass preserves the ordering established by all prior passes"
confidence: verified
supports:
  - "[[Radix Sort]]"
tags:
  - csa
  - csa/sorting
  - chunk
up: "[[CS Algorithms]]"
---
# Sorting — Radix sort LSD-first correctness relies on the stability of each digit-sort pass

## Context

Radix sort (LSD-first) runs d passes of a stable sort (typically counting sort), one per digit position from least to most significant. Correctness follows by induction:

**Inductive claim**: after processing digits 1 through i (least to most significant), the array is sorted by the i-digit number formed by digits 1..i.

**Base case (i=1)**: After the first pass (least significant digit), elements are sorted by digit 1. ✓

**Inductive step**: Assume the array is sorted by digits 1..i after pass i. Pass i+1 sorts by digit i+1 using a stable sort.
- Elements that differ on digit i+1 are placed in the correct relative order by pass i+1. ✓
- Elements that agree on digit i+1 are not reordered (stability), so their relative order from pass i — which sorted them correctly by digits 1..i — is preserved. ✓

After d passes, the array is sorted by all d digits, i.e., fully sorted. □

**Why MSD-first is harder**: Processing most-significant digit first creates d separate buckets, each requiring its own recursive sort — the induction does not apply cleanly, and the implementation requires partitioning and recursing into each bucket separately.

## Why It Matters

The stability argument is the entire correctness story for radix sort. Without stability, the LSD-first approach fails: each new pass can overwrite the ordering established by previous passes. This is why counting sort (stable) is used as the subroutine rather than, say, quicksort (not stable).

## QnA Seeds

- Q: Prove by induction that LSD-first radix sort is correct.
- Q: What happens to radix sort if an unstable subroutine is used?
- Q: Why is LSD-first simpler to implement correctly than MSD-first?
