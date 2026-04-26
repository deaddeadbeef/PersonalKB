---
id: chunk-csa-173
type: chunk
source: "[[Pugh 1990 - Skip Lists]]"
source_loc: "Basic Structure"
topic: "data-structures"
claim: "Skip lists achieve O(log n) expected time for search, insert, and delete using randomized multi-level linked lists with geometric level assignment"
confidence: verified
supports:
  - "[[Skip List]]"
  - "[[Randomized Data Structures]]"
tags:
  - csa
  - csa/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Data Structures — Skip list O(log n) expected via randomized level promotion

## Context

A skip list consists of multiple levels of sorted linked lists. Level 0 contains all elements; each higher level contains a random subset with each element promoted independently with probability p (typically 1/2). Search starts at the top level and moves right until exceeding the target, then drops down—combining binary search speed with linked list simplicity. The expected height is O(log n) and expected comparisons per search is (log n)/log(1/p) + O(1). New elements' levels are determined by a geometric random variable (coin flips), giving the structure its probabilistic performance guarantees.

## Why It Matters

Skip lists demonstrate that randomization can replace complex deterministic balancing, providing an elegant alternative to red-black/AVL trees that is particularly valuable for concurrent data structures.

## QnA Seeds

- Q: How is a new element's level determined in a skip list?
- Q: What is the expected number of levels in a skip list with n elements?
- Q: How does search traverse the skip list structure?
