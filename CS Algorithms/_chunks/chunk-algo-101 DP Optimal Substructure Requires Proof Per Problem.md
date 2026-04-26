---
id: chunk-algo-101
type: chunk
source: "[[raw-algo-016]]"
source_loc: "Dynamic Programming Principles - Key Claims"
topic: "dynamic-programming"
claim: "Dynamic programming requires that a problem exhibit optimal substructure—an optimal solution must be constructible from optimal solutions to subproblems—and this property must be proved individually for each DP problem, typically via a cut-and-paste exchange argument."
confidence: verified
supports:
  - "[[Dynamic Programming]]"
tags:
  - cs-algorithms
  - cs-algorithms/dynamic-programming
  - chunk
up: "[[CS Algorithms]]"
---
# DP Optimal Substructure Requires Proof Per Problem

## Context

Optimal substructure is one of two necessary conditions for dynamic programming (the other being overlapping subproblems). A problem has optimal substructure if an optimal solution contains within it optimal solutions to subproblems. This is not automatic—each DP formulation requires a proof, usually by contradiction: assume a subproblem solution is not optimal, then cut it out and paste in the optimal one, contradicting the optimality of the overall solution. Without optimal substructure, greedy or DP approaches may yield incorrect results.

## Why It Matters

Optimal substructure is the theoretical foundation that justifies the DP recurrence. Recognizing and proving it is the first step in any DP problem formulation, and misidentifying it is a common source of incorrect algorithms.

## QnA Seeds

- Q: What does optimal substructure mean in the context of dynamic programming?
- Q: How is optimal substructure typically proved for a DP problem?
- Q: Give an example of a problem that lacks optimal substructure.