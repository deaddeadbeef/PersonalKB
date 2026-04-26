---
id: chunk-csa-175
type: chunk
source: "[[Pugh 1990 - Skip Lists]]"
source_loc: "Space Analysis"
topic: "data-structures"
claim: "Skip lists with p=1/2 use 2n expected total pointers across all levels, comparable to a binary tree's 2n child pointers"
confidence: verified
supports:
  - "[[Skip List]]"
  - "[[Space Complexity]]"
tags:
  - csa
  - csa/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Data Structures — Skip list 2n expected pointers with promotion probability 1/2

## Context

The expected total number of forward pointers across all levels is n/(1-p). With the standard promotion probability p = 1/2, this gives 2n pointers—comparable to a binary tree's 2n child pointers. Each element has on average 1/(1-p) = 2 forward pointers. The probability of the skip list exceeding c*log(n) levels decreases exponentially in c, so extremely tall towers are vanishingly rare. Redis uses skip lists for sorted sets (ZSET), combined with a hash table for O(1) score lookup by member.

## Why It Matters

Understanding the space overhead justifies skip lists as a practical alternative to balanced trees, with comparable memory usage despite their multi-level structure.

## QnA Seeds

- Q: What is the expected number of pointers per element in a skip list with p=1/2?
- Q: How does skip list space compare to binary tree space?
- Q: How does Redis use skip lists in its sorted set implementation?
