---
id: chunk-csa-045
type: chunk
source: "[[CP Algorithms - Online Reference]]"
source_loc: "Counting Sort article"
topic: "sorting"
claim: "Counting sort's right-to-left output pass is what makes it stable: scanning backwards ensures that among elements sharing a key, those appearing later in the input are placed later in the output"
confidence: verified
supports:
  - "[[Counting Sort]]"
  - "[[Radix Sort]]"
tags:
  - csa
  - csa/sorting
  - chunk
up: "[[CS Algorithms]]"
---
# Sorting — Counting sort right-to-left pass preserves input order of equal keys ensuring stability

## Context

After counting occurrences and computing prefix sums, counting sort places each element into the output array in **reverse input order** — scanning the input from right to left. This is the mechanism that makes the algorithm stable.

**Why right-to-left works**: The prefix sum C[k] gives the last (rightmost) output position for elements with key k. When the right-to-left scan encounters the last element with key k, it is placed at position C[k] and C[k] is decremented. The second-to-last element with key k then gets position C[k]−1. The result is that among all elements sharing key k, the one that appeared latest in the input appears latest in the output — exactly the definition of stability.

**Left-to-right would break stability**: If the scan went left-to-right, the first element with key k would be placed at the highest available slot (C[k]) and the last element with key k would occupy the lowest slot — reversing their relative order, breaking stability.

**Consequence for radix sort**: Counting sort is the subroutine in radix sort. Each digit pass must be stable so that the ordering established by the less-significant-digit pass is preserved when the more-significant-digit pass encounters ties.

## Why It Matters

The right-to-left direction is a non-obvious implementation detail that is frequently tested and frequently gotten wrong. Understanding *why* it is needed (not just that it is needed) allows correct implementation from first principles and explains why a naive left-to-right scan silently produces incorrect results for equal keys.

## QnA Seeds

- Q: Why does counting sort scan the input right-to-left in the output phase?
- Q: What would happen to stability if counting sort scanned left-to-right instead?
- Q: Why does radix sort's correctness depend on counting sort being stable?
