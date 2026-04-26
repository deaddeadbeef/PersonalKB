---
id: chunk-csa-141
type: chunk
source: "[[Cormen 2022 - Greedy Algorithms]]"
source_loc: "Greedy Framework"
topic: "greedy"
claim: "A greedy algorithm requires both the greedy choice property and optimal substructure to guarantee a globally optimal solution"
confidence: verified
supports:
  - "[[Greedy Algorithms]]"
  - "[[Algorithm Design Paradigms]]"
tags:
  - csa
  - csa/greedy
  - chunk
up: "[[CS Algorithms]]"
---
# Greedy — Greedy choice property and optimal substructure are both required for correctness

## Context

A greedy algorithm constructs solutions incrementally by making the locally optimal choice at each step, never reconsidering past decisions. Two properties must hold for greedy to yield a globally optimal solution: the greedy choice property (a locally optimal choice leads to a globally optimal solution) and optimal substructure (an optimal solution contains optimal solutions to subproblems). The absence of either property means greedy may produce suboptimal results. Proving correctness typically uses an exchange argument showing any optimal solution can be transformed into the greedy solution without loss.

## Why It Matters

Recognizing these two properties is the essential first step in determining whether a greedy approach is valid for a given optimization problem, preventing incorrect applications of the paradigm.

## QnA Seeds

- Q: What two properties must hold for a greedy algorithm to produce an optimal solution?
- Q: What proof technique is commonly used to show a greedy algorithm is correct?
- Q: Why is it insufficient to show only optimal substructure for greedy correctness?
