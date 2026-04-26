---
id: chunk-csa-146
type: chunk
source: "[[Skiena 2020 - Backtracking and Branch-and-Bound]]"
source_loc: "N-Queens"
topic: "backtracking"
claim: "N-queens backtracking places queens row by row, pruning immediately on conflicts, exploring far fewer than n! placements in practice"
confidence: verified
supports:
  - "[[Backtracking]]"
  - "[[N-Queens Problem]]"
tags:
  - csa
  - csa/backtracking
  - chunk
up: "[[CS Algorithms]]"
---
# Backtracking — N-queens row-by-row placement with conflict pruning

## Context

The N-queens problem places n non-attacking queens on an n*n board. Backtracking places queens row by row: for each row, try each column and check for conflicts with previously placed queens (same column, same diagonal). Any placement that conflicts triggers immediate backtracking to the previous row. While the search space is up to n! placements, pruning eliminates the vast majority, enabling solutions for n=20 in milliseconds. This demonstrates how constraint checking at each step reduces an exponential space to a manageable search.

## Why It Matters

N-queens is the most widely used pedagogical example of backtracking, illustrating how constraint-driven pruning converts an intractable brute-force search into a practical algorithm.

## QnA Seeds

- Q: Why does N-queens backtracking explore far fewer than n! configurations?
- Q: What constraints are checked when placing a queen in a new row?
- Q: How does N-queens backtracking illustrate the general pruning principle?
