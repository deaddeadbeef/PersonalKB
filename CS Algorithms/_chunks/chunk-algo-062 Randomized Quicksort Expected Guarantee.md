---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-006]]"
confidence: high
supports:
  - "[[Quicksort]]"
  - "[[Randomized Algorithms]]"
qna_seeds:
  - "Q: What guarantee does randomized quicksort provide? A: Expected O(n log n) time regardless of input distribution; the probability of exceeding 4n ln n comparisons is at most 1/n by a Chernoff bound."
---

# Randomized Quicksort Expected Guarantee

Randomized quicksort achieves expected O(n log n) time regardless of input distribution by selecting pivots uniformly at random. The expectation is taken over random pivot choices, not input distribution. By a Chernoff bound argument, the probability that randomized quicksort exceeds 4n ln n comparisons on any input of size n is at most 1/n.