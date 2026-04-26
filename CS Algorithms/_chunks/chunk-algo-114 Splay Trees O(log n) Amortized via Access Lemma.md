---
id: chunk-algo-114
type: chunk
source: "[[raw-algo-019]]"
source_loc: "Amortized Analysis - Atomic Facts"
topic: "amortized-analysis"
claim: "Splay trees achieve O(log n) amortized time per operation using potential Phi = sum of log(size(v)) over all nodes; individual operations may take O(n) but any sequence of m operations on n nodes takes O((m+n) log n) total."
confidence: verified
supports:
  - "[[Amortized Analysis]]"
  - "[[Splay Trees]]"
tags:
  - cs-algorithms
  - cs-algorithms/amortized-analysis
  - chunk
up: "[[CS Algorithms]]"
---
# Splay Trees O(log n) Amortized via Access Lemma

## Context

The splay operation moves the accessed node to the root via zig, zig-zig, and zig-zag rotations. The access lemma proves amortized cost of splaying node x is at most 3(log(n) - log(size(x))) + 1. Although a single splay can take O(n) on a degenerate chain, the restructuring pays for itself by improving future accesses. Splay trees also adapt to access frequency patterns, performing within a constant factor of any static BST on the same sequence.

## Why It Matters

Splay trees demonstrate self-adjusting data structures and require no balance metadata per node. Their amortized analysis via the potential method is one of the most elegant applications in the field.

## QnA Seeds

- Q: What potential function proves O(log n) amortized for splay trees?
- Q: What is the total time for m operations on n-node splay tree?
- Q: How can a single O(n) splay be consistent with O(log n) amortized?