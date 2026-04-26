---
id: chunk-algo-136
type: chunk
source: "[[raw-algo-024]]"
source_loc: "Non-Comparison Sorting - Atomic Facts"
topic: "sorting"
claim: "Bucket sort distributes n elements into n buckets assuming uniform distribution over [0,1), sorts each with insertion sort, achieving O(n) expected time since each bucket has O(1) expected elements; worst case is O(n^2)."
confidence: verified
supports:
  - "[[Bucket Sort]]"
  - "[[Sorting Algorithms]]"
tags:
  - cs-algorithms
  - cs-algorithms/sorting
  - chunk
up: "[[CS Algorithms]]"
---
# Bucket Sort O(n) Expected with Uniform Distribution

## Context

Elements go into bucket floor(n*value) in O(1). Under uniform distribution, each bucket receives O(1) expected elements, so insertion sort per bucket is O(1) expected. Total: O(n) distribution + O(n*O(1)) sorting = O(n) expected. Worst case (all in one bucket) degrades to O(n^2). The uniformity assumption is critical—bucket sort is only efficient when the distribution is approximately known.

## Why It Matters

Bucket sort shows how distributional assumptions bypass comparison sort lower bounds. It is used for floating-point sorting, histogram generation, and distribution-sensitive algorithms.

## QnA Seeds

- Q: What distributional assumption does bucket sort require?
- Q: Why O(n) expected under uniform distribution?
- Q: What is bucket sort worst case?