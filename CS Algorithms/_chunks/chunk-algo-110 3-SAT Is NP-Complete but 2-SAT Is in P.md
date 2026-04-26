---
id: chunk-algo-110
type: chunk
source: "[[raw-algo-018]]"
source_loc: "NP-Completeness Theory - Atomic Facts"
topic: "complexity"
claim: "3-SAT (at most 3 literals per clause) is NP-complete, while 2-SAT is solvable in O(V+E) via strongly connected components on the implication graph—a sharp complexity boundary at clause size 3."
confidence: verified
supports:
  - "[[NP-Completeness]]"
  - "[[Satisfiability]]"
tags:
  - cs-algorithms
  - cs-algorithms/complexity
  - chunk
up: "[[CS Algorithms]]"
---
# 3-SAT Is NP-Complete but 2-SAT Is in P

## Context

Each 2-SAT clause (a OR b) equals two implications (NOT a => b) and (NOT b => a). The implication graph has 2n vertices. A formula is satisfiable iff no variable and its negation share an SCC, checkable in O(V+E) via Tarjan's algorithm. The reduction from SAT to 3-SAT introduces auxiliary variables to split long clauses, preserving satisfiability and proving 3-SAT NP-complete. This boundary at clause size 3 is one of the sharpest complexity transitions known.

## Why It Matters

The 3-SAT vs 2-SAT boundary shows how one extra literal per clause shifts a problem from P to NP-complete. This threshold phenomenon recurs throughout complexity theory (e.g., k-colorability at k=3).

## QnA Seeds

- Q: Why is 3-SAT NP-complete while 2-SAT is in P?
- Q: How does the implication graph characterize 2-SAT satisfiability?
- Q: What is the time complexity of solving 2-SAT?