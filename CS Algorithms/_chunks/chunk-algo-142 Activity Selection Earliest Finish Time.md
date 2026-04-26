---
id: chunk-csa-142
type: chunk
source: "[[Cormen 2022 - Greedy Algorithms]]"
source_loc: "Activity Selection"
topic: "greedy"
claim: "Activity selection with earliest-finish-time ordering produces a maximum-cardinality set of compatible activities in O(n log n) time"
confidence: verified
supports:
  - "[[Greedy Algorithms]]"
  - "[[Activity Selection]]"
tags:
  - csa
  - csa/greedy
  - chunk
up: "[[CS Algorithms]]"
---
# Greedy — Activity selection earliest-finish-time achieves O(n log n) optimal

## Context

The activity selection problem selects the maximum-size subset of mutually compatible activities from a set with given start and finish times. The greedy strategy sorts activities by finish time and iteratively selects the next compatible activity (whose start time is at or after the finish time of the last selected activity). This produces an optimal solution provable by an exchange argument: replacing any activity in an optimal set with the earlier-finishing greedy choice cannot reduce the count. The O(n log n) bound is dominated by sorting.

## Why It Matters

Activity selection is the canonical greedy example and the template for proving greedy optimality via exchange arguments, making it foundational for understanding the paradigm.

## QnA Seeds

- Q: Why does sorting by finish time (not start time) yield the optimal greedy strategy for activity selection?
- Q: What is the time complexity of activity selection and what dominates it?
- Q: How does the exchange argument prove optimality of the earliest-finish-time strategy?
