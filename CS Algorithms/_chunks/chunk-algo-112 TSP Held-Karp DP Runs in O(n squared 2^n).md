---
id: chunk-algo-112
type: chunk
source: "[[raw-algo-018]]"
source_loc: "NP-Completeness Theory - Atomic Facts"
topic: "complexity"
claim: "The Held-Karp DP algorithm solves TSP exactly in O(n^2 * 2^n) time and O(n * 2^n) space by DP over subsets of visited cities, yielding ~838 million states for n=25—vastly better than the n!/2n brute-force enumeration."
confidence: verified
supports:
  - "[[NP-Completeness]]"
  - "[[Dynamic Programming]]"
tags:
  - cs-algorithms
  - cs-algorithms/complexity
  - chunk
up: "[[CS Algorithms]]"
---
# TSP Held-Karp DP Runs in O(n squared 2^n)

## Context

Held-Karp defines dp[S][j] = minimum cost to visit all cities in subset S ending at j. The recurrence is dp[S][j] = min over i in S minus j of (dp[S minus j][i] + dist(i,j)). With 2^n subsets and n endpoints, there are n*2^n states each computed in O(n). For n=25: 25*2^25 ~ 838M states vs. 25!/50 ~ 3*10^23 brute-force tours. Held-Karp remains the best known exact TSP algorithm asymptotically.

## Why It Matters

Held-Karp demonstrates that even NP-hard problems admit dramatically improved exact algorithms. The subset-DP technique recurs in Hamiltonian path, graph coloring, and Steiner tree problems.

## QnA Seeds

- Q: What is the Held-Karp recurrence for TSP?
- Q: How does Held-Karp improve over brute-force TSP?
- Q: How many states for n=25 cities?