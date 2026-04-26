---
id: chunk-csa-005
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 2"
topic: "analysis"
claim: "The RAM model assigns unit cost to each basic operation and uniform cost to memory access, enabling machine-independent analysis"
confidence: verified
supports:
  - "[[Asymptotic Notation]]"
  - "[[Algorithm Definition]]"
tags:
  - csa
  - csa/analysis
  - chunk
up: "[[CS Algorithms]]"
---
# Analysis — The RAM model treats each basic operation as unit cost

## Context

The Random Access Machine model: a single processor executes operations one at a time; each basic operation (arithmetic, comparison, assignment, array access) costs exactly 1 unit; memory access at any location costs the same. This model is a deliberate simplification — real CPUs have caches, branch predictors, SIMD units — but it captures the dominant factor (number of operations) well for most algorithms and input sizes.

## Why It Matters

Without a shared cost model, running-time analysis would be implementation-specific. The RAM model enables universal statements like "this loop runs n−1 times, each iteration doing O(1) work, so the total is O(n)." It is the foundation beneath every asymptotic claim in the book.

## QnA Seeds

- Q: What is the RAM model of computation?
- Q: Why does the RAM model ignore cache effects?
- Q: How does the RAM model handle memory access costs?
