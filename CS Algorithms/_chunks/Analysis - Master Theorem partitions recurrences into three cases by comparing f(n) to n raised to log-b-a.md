---
id: chunk-csa-039
type: chunk
source: "[[MIT OCW 6006 - Introduction to Algorithms]]"
source_loc: "Lecture 2 — Models of Computation, Recurrences"
topic: "analysis"
claim: "The Master Theorem resolves T(n) = aT(n/b) + f(n) in three cases determined by comparing f(n) to n^(log_b a)"
confidence: verified
supports:
  - "[[Recurrence Relations]]"
  - "[[Master Theorem]]"
tags:
  - csa
  - csa/analysis
  - chunk
up: "[[CS Algorithms]]"
---
# Analysis — Master Theorem partitions recurrences into three cases by comparing f(n) to n raised to log-b-a

## Context

The Master Theorem applies to recurrences of the form T(n) = aT(n/b) + f(n), where a ≥ 1 subproblems of size n/b are solved recursively and f(n) is the cost of the divide-and-combine work. The critical quantity is n^(log_b a) — the number of leaves in the recursion tree.

**Case 1 — Leaf-dominated**: If f(n) = O(n^(log_b a − ε)) for some ε > 0, then the leaf level dominates and T(n) = Θ(n^(log_b a)). The combine work is negligible.

**Case 2 — Balanced**: If f(n) = Θ(n^(log_b a) · lg^k n) for k ≥ 0, then both leaf and combine levels contribute equally and T(n) = Θ(n^(log_b a) · lg^(k+1) n). Merge sort (a=2, b=2, f(n)=Θ(n), k=0) falls here with T(n) = Θ(n lg n).

**Case 3 — Root-dominated**: If f(n) = Ω(n^(log_b a + ε)) and the regularity condition af(n/b) ≤ cf(n) holds, then the root level dominates and T(n) = Θ(f(n)).

## Why It Matters

The Master Theorem is the primary shortcut for solving divide-and-conquer recurrences without expanding the full recursion tree. Identifying which case applies — and verifying the regularity condition in Case 3 — is the central skill. Binary search falls in Case 2 (k=0, a=1, b=2, f(n)=Θ(1)): T(n) = Θ(lg n).

## QnA Seeds

- Q: What are the three cases of the Master Theorem and what determines which applies?
- Q: In which Master Theorem case does merge sort fall, and why?
- Q: What is the regularity condition in Case 3 and why is it needed?
- Q: Why doesn't the Master Theorem apply to T(n) = 2T(n/2) + n lg n directly?
