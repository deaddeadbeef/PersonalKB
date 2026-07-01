---
type: generated-reading-spine
tags: [cs-algorithms, index, book, reading-path, navigation]
up: "[[CS Algorithms/CS Algorithms|CS Algorithms]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# CS Algorithms Book Reading Spine

Follow the subject from precise procedures, through proof and growth rates, into the classic families of algorithmic ideas.

This page is the reader-facing spine. Treat it like the table of contents of a good book: read the chapter openers first, then deepen through the linked articles, then use study notes and sources as appendices.

## How To Read This Topic

1. **First pass: story.** Read the prologue and each Book heading, opening only overview and learning-path pages first.
2. **Second pass: mechanism.** Return to every linked article in order and follow the concepts inside each chapter.
3. **Third pass: practice.** Use study drills, checklists, labs, plans, or recipes to prove the knowledge operationally.
4. **Fourth pass: evidence.** Use source indexes when a claim matters or when the page is time-sensitive.

## Prologue: What An Algorithm Is

Start with the map, the learning path, and the vocabulary for exact procedures.

- [[CS Algorithms/CS Algorithms|CS Algorithms]] — Master index for the CS Algorithms knowledge base. Built around Thomas H. Cormen's Algorithms Unlocked (MIT Press, 2013) as the primary entry point.
- [[CS Algorithms/CS Algorithms — Learning Path|CS Algorithms — Learning Path]] — Pass-based learning path for CS Algorithms.

## Book I: Proof, Cost, And Recurrence

Build the mental tools: asymptotics, invariants, recurrences, and dynamic programming.

- [[CS Algorithms/Analysis/Foundations and Analysis Overview|Foundations and Analysis Overview]] — The analytical toolkit every algorithm chapter draws on. Master this domain first — asymptotic reasoning, loop-invariant proofs, and recurrence solving appear in every other topic in the knowledge base.
- [[CS Algorithms/Analysis/Algorithm Definition|Algorithm Definition]] — An algorithm is a finite, precisely specified sequence of steps that a computational device can execute to solve a well-defined problem.
- [[CS Algorithms/Analysis/Asymptotic Notation|Asymptotic Notation]] — Asymptotic notation describes how a function's growth rate behaves as input size n → ∞, abstracting away constants and lower-order terms to enable algorithm comparison independent of hardware.
- [[CS Algorithms/Analysis/Comparison Sort Lower Bound|Comparison Sort Lower Bound]] — Any algorithm that determines sorted order exclusively by comparing pairs of elements must make at least $\Omega(n \lg n)$ comparisons in the worst case.
- [[CS Algorithms/Analysis/Dynamic Programming|Dynamic Programming]] — Dynamic programming (DP) solves optimisation and counting problems by breaking them into overlapping subproblems, solving each once, and storing the result for reuse.
- [[CS Algorithms/Analysis/Loop Invariant|Loop Invariant]] — A loop invariant is a property that holds before the first iteration, is maintained by each iteration, and implies correctness when the loop terminates.
- [[CS Algorithms/Analysis/Master Theorem|Master Theorem]] — The Master Theorem is a closed-form solution technique for divide-and-conquer recurrences of the form T(n) = aT(n/b) + f(n), determining T(n) by comparing the combine cost f(n) to the leaf cost $n^{log_b a}$.
- [[CS Algorithms/Analysis/Recurrence Relations|Recurrence Relations]] — A recurrence relation expresses the running time of a recursive algorithm in terms of the running time on smaller inputs.

## Book II: Sorting And Searching

Watch small ordering problems become the laboratory for lower bounds and tradeoffs.

- [[CS Algorithms/Sorting/Sorting Overview|Sorting Overview]] — Given an array A of n elements with a total order (≤), rearrange A so that A[1] ≤ A[2] ≤ … ≤ A[n].
- [[CS Algorithms/Sorting/Counting Sort|Counting Sort]] — Count how many times each key value appears, then use cumulative counts to place every element directly into its final position.
- [[CS Algorithms/Sorting/External Sorting|External Sorting]] — External sorting is sorting for data sets that do not fit in memory, so the main cost is disk or SSD I/O rather than comparisons alone.
- [[CS Algorithms/Sorting/Insertion Sort|Insertion Sort]] — Pick up each element and slide it into the right spot among the already-sorted elements to its left.
- [[CS Algorithms/Sorting/Inversions|Inversions]] — An inversion is a pair of elements that appear in the wrong order; the total count tells you exactly how far the array is from being sorted.
- [[CS Algorithms/Sorting/Merge Sort|Merge Sort]] — Split the array in half, recursively sort each half, then merge the two sorted halves back together.
- [[CS Algorithms/Sorting/Quicksort|Quicksort]] — Pick a pivot element, rearrange the array so everything ≤ pivot is on the left and everything > pivot is on the right, then recursively sort both sides.
- [[CS Algorithms/Sorting/Radix Sort|Radix Sort]] — Sort by the least-significant digit first, then the next digit, and so on — because each pass uses a stable sort, the order from previous digits is preserved.
- [[CS Algorithms/Sorting/Selection Sort|Selection Sort]] — Find the smallest element in the unsorted portion, swap it into the next position, and repeat.
- [[CS Algorithms/Searching/Binary Search|Binary Search]] — Binary search finds a target value in a sorted array by repeatedly halving the search space, running in $O(\lg n)$ worst case.

## Book III: Divide, Choose, And Backtrack

Compare the main problem-solving patterns by the kind of promise each one needs.

- [[CS Algorithms/Divide and Conquer/Divide and Conquer Overview — Domain|Divide and Conquer Overview — Domain]]
- [[CS Algorithms/Divide and Conquer/Divide and Conquer Overview|Divide and Conquer Overview]] — Divide and conquer solves problems by recursively breaking them into smaller, independent sub-problems, solving each, and combining the results.
- [[CS Algorithms/Divide and Conquer/Master Theorem Applications|Master Theorem Applications]] — The Master Theorem provides a cookbook for solving recurrences of the form T(n) = aT(n/b) + $\Theta(n^c \log^k n)$, covering most divide-and-conquer running times.
- [[CS Algorithms/Greedy/Greedy Algorithms Overview|Greedy Algorithms Overview]] — Greedy algorithms build solutions incrementally, always choosing the locally optimal option at each step, and succeed when local optima guarantee a global optimum.
- [[CS Algorithms/Greedy/Greedy Overview|Greedy Overview]] — Greedy algorithms make the locally optimal choice at each step, hoping to find a global optimum.
- [[CS Algorithms/Greedy/Activity Selection Problem|Activity Selection Problem]] — Select the maximum number of non-overlapping activities from a set with given start and finish times by always choosing the activity that finishes earliest.
- [[CS Algorithms/Greedy/Fractional Knapsack|Fractional Knapsack]] — Maximize the total value in a weight-limited knapsack by greedily taking items in decreasing order of value-to-weight ratio, splitting the last item if needed.
- [[CS Algorithms/Backtracking/Backtracking Overview — Domain|Backtracking Overview — Domain]] — Backtracking is systematic trial-and-error: build a candidate solution incrementally, and as soon as a partial candidate violates the problem constraints, prune that branch and backtrack to try another option.
- [[CS Algorithms/Backtracking/Backtracking Overview|Backtracking Overview]] — Backtracking systematically explores all potential solutions by building candidates incrementally and abandoning ("pruning") a branch as soon as it determines the candidate cannot lead to a valid or optimal solution.
- [[CS Algorithms/Backtracking/N-Queens Problem|N-Queens Problem]] — Place N queens on an N×N chessboard so that no two queens threaten each other — solved elegantly via backtracking with column, diagonal, and anti-diagonal constraint tracking.
- [[CS Algorithms/Techniques/Techniques Overview|Techniques Overview]] — Some algorithmic ideas are not tied to a single problem domain — they are cross-cutting techniques that appear in sorting, searching, graphs, strings, and beyond.
- [[CS Algorithms/Techniques/Amortized Analysis for Algorithms|Amortized Analysis for Algorithms]] — Amortized analysis determines the average cost per operation over a worst-case sequence of operations, proving that expensive operations are rare enough to keep the average cost low.
- [[CS Algorithms/Techniques/Online Algorithms and Competitive Analysis|Online Algorithms and Competitive Analysis]] — Online algorithms make decisions before seeing the full input; competitive analysis compares them with an optimal offline algorithm that sees the future.
- [[CS Algorithms/Techniques/Parallel Algorithms|Parallel Algorithms]] — Parallel algorithms divide work across processors while managing dependence, synchronization, communication, and load balance.
- [[CS Algorithms/Techniques/Randomized Algorithms|Randomized Algorithms]] — Randomized algorithms use random choices to simplify design, improve expected performance, or trade deterministic guarantees for high-probability guarantees.
- [[CS Algorithms/Techniques/Streaming Algorithms|Streaming Algorithms]] — Streaming algorithms process data in one pass or a small number of passes while using much less memory than the input size.
- [[CS Algorithms/Techniques/Two Pointers and Sliding Window|Two Pointers and Sliding Window]] — Two Pointers uses a pair of indices moving inward (or in tandem) to solve problems on sorted arrays or sequences in $O(n)$.

## Book IV: Graphs As Worlds

Move from arrays to relationships: traversal, paths, spanning trees, and flow.

- [[CS Algorithms/Graphs/Graphs Overview|Graphs Overview]] — Graph algorithms model relationships between entities. This domain covers graph vocabulary, ordering via topological sort, and the family of shortest-path algorithms.
- [[CS Algorithms/Graphs/Shortest Path Overview|Shortest Path Overview]] — Shortest-path algorithms find minimum-weight paths in weighted graphs, varying by single-source vs all-pairs, weight constraints, and graph structure.
- [[CS Algorithms/Graphs/Bellman-Ford Algorithm|Bellman-Ford Algorithm]] — Relax every edge n−1 times; after k passes, shortest paths using at most k edges are correct.
- [[CS Algorithms/Graphs/BFS and DFS|BFS and DFS]] — Breadth-First Search explores a graph level by level using a queue, while Depth-First Search dives as deep as possible along each branch using a stack, together forming the foundation of nearly all graph algorithms.
- [[CS Algorithms/Graphs/DAG and Topological Sort|DAG and Topological Sort]] — Repeatedly remove vertices with no incoming edges; the removal order is a valid topological sort.
- [[CS Algorithms/Graphs/Dijkstra's Algorithm|Dijkstra's Algorithm]] — Greedily extract the closest unvisited vertex and finalise its distance; non-negative weights guarantee no future path can improve it.
- [[CS Algorithms/Graphs/Floyd-Warshall Algorithm|Floyd-Warshall Algorithm]] — For each possible intermediate vertex x, check whether routing through x improves the shortest path between every pair (u, v).
- [[CS Algorithms/Graphs/Graph Fundamentals|Graph Fundamentals]] — Graphs model pairwise relationships; the representation you choose (list vs matrix) determines the efficiency of every algorithm built on top.
- [[CS Algorithms/Graphs/Kruskal's Algorithm|Kruskal's Algorithm]] — Kruskal's algorithm builds a Minimum Spanning Tree by sorting all edges by weight and greedily adding each edge that doesn't create a cycle, using a Union-Find structure for efficient cycle detection.
- [[CS Algorithms/Graphs/Minimum Spanning Trees|Minimum Spanning Trees]] — A Minimum Spanning Tree (MST) is a subset of edges in a weighted, connected, undirected graph that connects all vertices with the minimum total edge weight and no cycles.
- [[CS Algorithms/Graphs/Network Flow — Ford-Fulkerson|Network Flow — Ford-Fulkerson]] — The Ford-Fulkerson method computes the maximum flow in a flow network by repeatedly finding augmenting paths from source to sink in the residual graph and pushing flow along them until no more paths exist.
- [[CS Algorithms/Graphs/Prim's Algorithm|Prim's Algorithm]] — Prim's algorithm grows a Minimum Spanning Tree from a single source vertex by repeatedly adding the cheapest edge that connects the growing tree to a vertex not yet in the tree.

## Book V: Strings, Compression, And Cryptography

Read sequence algorithms, coding, and secrecy as applied versions of the same design discipline.

- [[CS Algorithms/Strings/Strings Overview|Strings Overview]] — String algorithms compute relationships between sequences — exact matches, longest common parts, and minimum-cost transformations.
- [[CS Algorithms/Strings/Edit Distance|Edit Distance]] — Build a 2D table where each cell cost[i][j] stores the cheapest way to transform the first i characters of X into the first j characters of Y. Analogy.
- [[CS Algorithms/Strings/LCS - Longest Common Subsequence|LCS — Longest Common Subsequence]] — Build a 2D table where l[i][j] stores the LCS length of the first i characters of X and the first j characters of Y; matching characters extend the LCS, mismatches take the better of skipping either character.
- [[CS Algorithms/Strings/String Matching - KMP|String Matching — KMP]] — Precompute how much of the pattern you can reuse after a mismatch, so the text pointer never moves backward.
- [[CS Algorithms/Compression/Data Compression Overview|Data Compression Overview]] — Data compression reduces the number of bits needed to represent information. This page covers lossless compression only — perfect reconstruction guaranteed.
- [[CS Algorithms/Compression/Huffman Coding|Huffman Coding]] — Repeatedly merge the two least-frequent symbols into a single node; the resulting binary tree assigns short codes to frequent symbols and long codes to rare ones.
- [[CS Algorithms/Compression/LZW Compression|LZW Compression]] — Both encoder and decoder start with the same initial dictionary and extend it identically as data is processed, so the dictionary never needs to be transmitted.
- [[CS Algorithms/Compression/Run-Length Encoding|Run-Length Encoding]] — Instead of storing every repeated symbol individually, count consecutive identical symbols and store the count once.
- [[CS Algorithms/Cryptography/Cryptography Overview|Cryptography Overview]] — Cryptographic algorithms secure communication and data by exploiting mathematical hardness.
- [[CS Algorithms/Cryptography/Cryptography Foundations|Cryptography Foundations]] — Modern cryptography solves two problems: making data unreadable (encryption) and sharing keys securely (key distribution); the hybrid model addresses both.
- [[CS Algorithms/Cryptography/Random Number Generation|Random Number Generation]] — A pseudorandom bit generator (PRBG) takes a short, secret seed and deterministically expands it into a long bitstream indistinguishable from true randomness by any efficient observer.
- [[CS Algorithms/Cryptography/RSA Algorithm|RSA Algorithm]] — Multiplying two large primes is fast; factoring their product is computationally infeasible — this asymmetry enables secure public-key encryption.

## Book VI: Hardness And Limits

End the theory arc with what efficient computation can and cannot plausibly do.

- [[CS Algorithms/Complexity/Complexity Theory Overview|Complexity Theory Overview]] — The study of what computers fundamentally can and cannot compute efficiently — covering P vs NP, NP-completeness, undecidability, and approximation algorithms.
- [[CS Algorithms/Complexity/Approximation Algorithms|Approximation Algorithms]] — An approximation algorithm runs in polynomial time and returns a solution guaranteed to be within a constant factor of optimal — a principled response to NP-complete problems.
- [[CS Algorithms/Complexity/Halting Problem|Halting Problem]] — The Halting Problem asks whether an arbitrary program halts on a given input — Turing (1936) proved no algorithm can decide this for all programs.
- [[CS Algorithms/Complexity/NP Completeness|NP Completeness]] — NP-complete problems are the hardest problems in NP — every NP problem reduces to them, yet no polynomial-time algorithm is known for any of them.
- [[CS Algorithms/Complexity/P vs NP|P vs NP]] — The P vs NP problem asks whether every problem whose solution can be verified quickly can also be solved quickly — the central unsolved question in theoretical computer science.

## Book VII: The Textbook Walkthrough

Use chapter notes as the guided classroom route through the source material.

- [[CS Algorithms/Books/Algorithms Unlocked/Chapter Index|Chapter Index — Algorithms Unlocked]] — Chapter-by-chapter route through Algorithms Unlocked.
- [[CS Algorithms/Books/Algorithms Unlocked/Chapters/AU - Chapter 01|AU — Chapter 01: What Are Algorithms and Why Should You Care?]] — Cormen opens by establishing what distinguishes a computer algorithm from a vague human procedure: the algorithm must be precise enough that a machine can execute it without interpretation.
- [[CS Algorithms/Books/Algorithms Unlocked/Chapters/AU - Chapter 02|AU — Chapter 02: How to Describe and Evaluate Computer Algorithms]] — Chapter 2 builds the notational and proof vocabulary used throughout the rest of the book.
- [[CS Algorithms/Books/Algorithms Unlocked/Chapters/AU - Chapter 03|AU — Chapter 03: Algorithms for Sorting and Searching]] — The book's most algorithm-dense chapter covers one search and four sort algorithms. Binary search on a sorted array eliminates half the search space per comparison, yielding $O(\lg n)$ worst case — a fundamental result.
- [[CS Algorithms/Books/Algorithms Unlocked/Chapters/AU - Chapter 04|AU — Chapter 04: A Lower Bound for Sorting and How to Beat It]] — Chapter 4 answers a fundamental question: is $\Theta(n \lg n)$ the best we can do for sorting? The answer depends on the rules.
- [[CS Algorithms/Books/Algorithms Unlocked/Chapters/AU - Chapter 05|AU — Chapter 05: Directed Acyclic Graphs]] — Cormen introduces graphs through a vivid concrete example: putting on hockey goalie equipment in dependency order.
- [[CS Algorithms/Books/Algorithms Unlocked/Chapters/AU - Chapter 06|AU — Chapter 06: Shortest Paths]] — Chapter 6 extends shortest-path finding from acyclic graphs (Chapter 5) to general directed graphs with cycles. Three landmark algorithms address different problem variants.
- [[CS Algorithms/Books/Algorithms Unlocked/Chapters/AU - Chapter 07|AU — Chapter 07: Algorithms on Strings]] — Chapter 7 covers three classical string problems. Longest Common Subsequence (LCS): a subsequence preserves relative character order but need not be contiguous.
- [[CS Algorithms/Books/Algorithms Unlocked/Chapters/AU - Chapter 08|AU — Chapter 08: Foundations of Cryptography]] — Chapter 8 surveys cryptographic algorithms motivated by the practical problem of transmitting sensitive data over a public network.
- [[CS Algorithms/Books/Algorithms Unlocked/Chapters/AU - Chapter 09|AU — Chapter 09: Data Compression]] — Chapter 9 asks: if the previous chapter was about hiding information, how do we shrink it? The focus is entirely on lossless compression — perfect reconstruction guaranteed.
- [[CS Algorithms/Books/Algorithms Unlocked/Chapters/AU - Chapter 10|AU — Chapter 10: Hard? Problems]] — The final chapter tackles the deepest question in algorithmic theory: which problems are truly hard?
- [[CS Algorithms/Books/Algorithms Unlocked/Algorithms Unlocked|Algorithms Unlocked]] — Primary algorithms textbook route through correctness, growth rates, sorting, graphs, strings, cryptography, compression, and complexity.

## Appendices: Practice And Sources

Switch from reading to recall, selection, and provenance.

- [[CS Algorithms/Study/Algorithms Study Index|Algorithms Study Index]] — Study router for Algorithms drills, labs, proof artifacts, and review sessions.
- [[CS Algorithms/Study/Algorithm Complexity Cheatsheet|Algorithm Complexity Cheatsheet]] — Compiled quick-reference for time and space complexities across all domains in the CS Algorithms knowledge base. Use for rapid review, algorithm selection, and exam preparation.
- [[CS Algorithms/Study/Complexity Theory - Review Drill|Complexity Theory — Review Drill]] — Review drill for Complexity Theory.
- [[CS Algorithms/Study/Cryptography - Review Drill|Cryptography — Review Drill]] — Review drill for Cryptography.
- [[CS Algorithms/Study/Data Compression - Review Drill|Data Compression — Review Drill]] — Review drill for Data Compression.
- [[CS Algorithms/Study/Foundations and Analysis - Review Drill|Foundations and Analysis — Review Drill]] — Review drill for Foundations and Analysis.
- [[CS Algorithms/Study/Graphs and Shortest Paths - Review Drill|Graphs and Shortest Paths — Review Drill]] — Review drill for Graphs and Shortest Paths.
- [[CS Algorithms/Study/Sorting and Searching - Review Drill|Sorting and Searching — Review Drill]] — Review drill for Sorting and Searching.
- [[CS Algorithms/Study/Strings - Review Drill|Strings — Review Drill]] — Review drill for Strings.
- [[CS Algorithms/Sources/Sources Index|Sources Index]] — Source and provenance map.

## Coverage

- Reader-facing articles linked here: 88
- Protected raw, chunk, template, query, audio, and operations folders are intentionally not expanded here.
- The root vault index remains the exhaustive generated listing across every topic.

## References

- [[CS Algorithms/CS Algorithms|CS Algorithms]]
- [[CS Algorithms/Sources/Sources Index|Sources Index]]
