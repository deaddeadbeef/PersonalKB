---
id: chunk-csa-028
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 7"
topic: "strings"
claim: "Edit distance is defined via a recurrence over prefix pairs — the minimum cost to align X[1..i] with Y[1..j] reduces to smaller subproblems by considering the last operation applied"
confidence: verified
supports:
  - "[[Edit Distance]]"
  - "[[Dynamic Programming]]"
tags:
  - csa
  - csa/strings
  - chunk
up: "[[CS Algorithms]]"
---
# Strings — Edit Distance recurrence computes minimum-cost alignment via DP over prefixes

## Context

Define cost[i, j] as the minimum cost to transform X[1..i] into Y[1..j]. The recurrence considers the last operation:

- **Copy/Replace** (X[i] and Y[j] both consumed): cost[i, j] = cost[i−1, j−1] + (0 if X[i]=Y[j], else replace_cost)
- **Delete X[i]** (advance only in X): cost[i, j] = cost[i−1, j] + delete_cost
- **Insert Y[j]** (advance only in Y): cost[i, j] = cost[i, j−1] + insert_cost

Take the minimum over all applicable operations. Base cases: cost[0, j] = j · insert_cost (build Y[1..j] from scratch); cost[i, 0] = i · delete_cost (delete all of X[1..i]).

The recurrence has **optimal substructure**: an optimal alignment of X[1..i] with Y[1..j] necessarily contains an optimal alignment of the relevant prefix pair. This is what makes dynamic programming applicable.

## Why It Matters

The recurrence makes precise the informal idea of "minimum edits." It cleanly separates the three cases, each consuming one or both characters, and the base cases handle the empty-string boundary. Once the recurrence is established, filling the table is mechanical. The same reasoning pattern — define cost on prefixes, observe optimal substructure, memoize — transfers directly to other DP string problems.

## QnA Seeds

- Q: What are the three cases in the edit distance recurrence, and which string pointers does each advance?
- Q: What base cases does the edit distance DP table require, and why?
- Q: Why does optimal substructure hold for edit distance?
