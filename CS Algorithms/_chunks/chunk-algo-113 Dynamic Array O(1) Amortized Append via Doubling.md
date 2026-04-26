---
id: chunk-algo-113
type: chunk
source: "[[raw-algo-019]]"
source_loc: "Amortized Analysis - Key Claims"
topic: "amortized-analysis"
claim: "Dynamic arrays achieve O(1) amortized append by doubling capacity when full; over n appends, doublings at sizes 1,2,4,...,2^floor(log n) yield total copying cost < 2n, making total work < 3n."
confidence: verified
supports:
  - "[[Amortized Analysis]]"
  - "[[Dynamic Arrays]]"
tags:
  - cs-algorithms
  - cs-algorithms/amortized-analysis
  - chunk
up: "[[CS Algorithms]]"
---
# Dynamic Array O(1) Amortized Append via Doubling

## Context

The geometric sum 1 + 2 + 4 + ... + 2^floor(log n) < 2n gives total copying cost. Including n insertions, total work < 3n, so amortized cost per append is O(1). The potential method formalizes this: with Phi = 2*size - capacity, each non-resizing append has amortized cost 3, and each doubling's actual cost is offset by potential drop to 0. This applies to std::vector, Python list, and Java ArrayList.

## Why It Matters

Dynamic array amortized analysis is the most intuitive introduction to amortized analysis and explains why array appends are efficient despite occasional O(n) resizing. This is foundational for understanding hash table resizing.

## QnA Seeds

- Q: What is the total copying cost over n appends to a doubling array?
- Q: What potential function proves O(1) amortized append?
- Q: Why does the growth factor need to exceed 1?