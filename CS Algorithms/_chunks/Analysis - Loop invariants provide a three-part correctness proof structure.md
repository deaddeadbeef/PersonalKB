---
id: chunk-csa-004
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 2"
topic: "analysis"
claim: "Loop invariants prove algorithm correctness through initialization, maintenance, and termination"
confidence: verified
supports:
  - "[[Loop Invariant]]"
tags:
  - csa
  - csa/analysis
  - chunk
up: "[[CS Algorithms]]"
---
# Analysis — Loop invariants provide a three-part correctness proof structure

## Context

A loop invariant is a property that holds before the first iteration (initialization), is maintained after each iteration (maintenance), and whose truth after the loop terminates implies the algorithm's correctness (termination). The technique is analogous to mathematical induction: base case = initialization, inductive step = maintenance, conclusion = termination. Cormen uses loop invariants to prove binary search and sorting algorithms correct throughout the book.

## Why It Matters

Loop invariants provide a rigorous, structured way to reason about iterative algorithms without running all possible inputs. They bridge the gap between informal algorithm descriptions and formal proofs, and they're practical enough to apply by hand for interview and exam proofs.

## QnA Seeds

- Q: What are the three parts of a loop invariant proof?
- Q: How is a loop invariant analogous to mathematical induction?
- Q: How would you apply a loop invariant to prove binary search correct?
