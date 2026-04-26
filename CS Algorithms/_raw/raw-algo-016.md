---
tags: [cs-algorithms, raw]
source_type: textbook
source_title: "Dynamic Programming: Principles and Classic Problems"
authors: "Richard Bellman"
year: 1957
---

# Dynamic Programming Principles

## Summary
Dynamic programming (DP) is an algorithm design technique that solves optimization problems by breaking them into overlapping subproblems, solving each subproblem once, and storing results to avoid redundant computation. Two structural properties must hold: optimal substructure (an optimal solution contains optimal solutions to subproblems) and overlapping subproblems (the same subproblems recur across different recursive paths). DP can be implemented top-down with memoization (recursive with caching) or bottom-up with tabulation (iterative, filling a table in dependency order), with both approaches yielding the same asymptotic complexity but different constant factors and space optimization opportunities.

## Key Claims
- Optimal substructure means that an optimal solution to the problem can be constructed from optimal solutions to its subproblems; this must be proved for each DP problem, often via a cut-and-paste argument
- Overlapping subproblems distinguish DP from plain divide-and-conquer: the naive recursive Fibonacci computes F(n) in O(φⁿ) time because it recomputes subproblems exponentially many times, while DP computes it in O(n)
- Top-down memoization solves only the subproblems actually needed (lazy evaluation), while bottom-up tabulation avoids recursion overhead and enables space optimization by discarding no-longer-needed subproblem rows
- The longest common subsequence (LCS) of two strings of lengths m and n is computed in O(mn) time and O(min(m,n)) space using the recurrence LCS[i][j] = LCS[i−1][j−1]+1 if match, else max(LCS[i−1][j], LCS[i][j−1])
- The 0/1 knapsack problem with n items and capacity W is solvable in O(nW) pseudo-polynomial time; this is not polynomial in the input size because W is exponential in its bit representation (log W bits)

## Atomic Facts
1. The Fibonacci DP recurrence F[i] = F[i−1] + F[i−2] has O(n) subproblems each taking O(1) time; bottom-up tabulation with rolling variables uses O(1) space, computing F(50) = 12,586,269,025 in 50 additions
2. Edit distance (Levenshtein distance) between strings of lengths m and n uses a DP table of size (m+1) × (n+1) with O(mn) time; the recurrence considers insertion, deletion, and substitution costs at each cell
3. Matrix chain multiplication for n matrices is solved in O(n³) time and O(n²) space by the recurrence m[i,j] = min_{i≤k<j}(m[i,k] + m[k+1,j] + p_{i−1}·p_k·p_j); for n = 20 matrices, this evaluates at most 1,140 subproblems
4. The knapsack DP table has n × W entries; for n = 100 items and W = 10,000, this is 1,000,000 entries, each computed in O(1) time. Space optimization reduces storage to O(W) using a single row scanned right-to-left
5. The Viterbi algorithm for Hidden Markov Models is a DP over T time steps and S states, running in O(TS²) time; for speech recognition with T = 1000 frames and S = 50 phoneme states, this is 2,500,000 operations
6. The all-pairs shortest paths Floyd-Warshall algorithm is a DP with recurrence dist[i][j][k] = min(dist[i][j][k−1], dist[i][k][k−1] + dist[k][j][k−1]), running in Θ(V³) time and Θ(V²) space (the k dimension can be eliminated)

## Significance
Dynamic programming is one of the most powerful and versatile algorithm design paradigms, applicable to optimization, counting, and decision problems across computer science, operations research, bioinformatics, and economics. Bellman's principle of optimality (1957) formalized the idea that optimal policies have the property that subsequent decisions must constitute an optimal policy from the resulting state. DP problems pervade technical interviews, competitive programming, and real-world applications including sequence alignment (bioinformatics), shortest paths (networking), compiler optimization (register allocation), and reinforcement learning (value iteration and policy iteration are DP algorithms on MDPs).

## Chunks Extracted
*Pending*
