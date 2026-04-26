---
id: chunk-csa-145
type: chunk
source: "[[Skiena 2020 - Backtracking and Branch-and-Bound]]"
source_loc: "Backtracking Framework"
topic: "backtracking"
claim: "Backtracking systematically prunes the search space by abandoning partial solutions that cannot lead to valid complete solutions, dramatically reducing exploration vs brute force"
confidence: verified
supports:
  - "[[Backtracking]]"
  - "[[Algorithm Design Paradigms]]"
tags:
  - csa
  - csa/backtracking
  - chunk
up: "[[CS Algorithms]]"
---
# Backtracking — Systematic pruning abandons infeasible partial solutions early

## Context

Backtracking constructs a solution vector one component at a time using a recursive tree structure where each node represents a partial solution. At each node, if the partial solution cannot lead to a valid complete solution, the entire subtree is pruned—avoiding exponential exhaustive enumeration. The effectiveness depends critically on early pruning: the sooner infeasible branches are identified, the larger the subtrees that can be skipped. Constraint propagation techniques like forward checking strengthen pruning by proactively reducing the domain of future variables.

## Why It Matters

Backtracking is the foundation of SAT solvers, constraint programming, and combinatorial search—understanding its pruning philosophy is essential for tackling NP-hard problems in practice.

## QnA Seeds

- Q: What makes backtracking more efficient than exhaustive brute-force search?
- Q: Why does the order in which variables are assigned affect backtracking efficiency?
- Q: How does forward checking enhance basic backtracking?
