---
type: generated-reading-spine
tags: [cs-algorithms, index, book, reading-path, navigation]
up: "[[CS Algorithms/CS Algorithms|CS Algorithms]]"
confidence: verified
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

- [[CS Algorithms/CS Algorithms|CS Algorithms]] — 📚 New here? Start with the Learning Path for a guided, progressive tour.
- [[CS Algorithms/CS Algorithms — Learning Path|CS Algorithms — Learning Path]] — This path is designed for progressive learning — you don't read everything at once. Make multiple passes, each going deeper.

## Book I: Proof, Cost, And Recurrence

Build the mental tools: asymptotics, invariants, recurrences, and dynamic programming.

- [[CS Algorithms/Analysis/Foundations and Analysis Overview|Foundations and Analysis Overview]] — The analytical toolkit every algorithm chapter draws on. Master this domain first — asymptotic reasoning, loop-invariant proofs, and recurrence solvi...
- [[CS Algorithms/Analysis/Algorithm Definition|Algorithm Definition]] — An algorithm is a finite, precisely specified sequence of steps that a computational device can execute to solve a well-defined problem.
- [[CS Algorithms/Analysis/Asymptotic Notation|Asymptotic Notation]] — Asymptotic notation describes how a function's growth rate behaves as input size n → ∞, abstracting away constants and lower-order terms to enable al...
- [[CS Algorithms/Analysis/Comparison Sort Lower Bound|Comparison Sort Lower Bound]] — Any algorithm that determines sorted order exclusively by comparing pairs of elements must make at least $\Omega(n \lg n)$ comparisons in the worst c...
- [[CS Algorithms/Analysis/Dynamic Programming|Dynamic Programming]] — Dynamic programming (DP) solves optimisation and counting problems by breaking them into overlapping subproblems, solving each once, and storing the...
- [[CS Algorithms/Analysis/Loop Invariant|Loop Invariant]] — A loop invariant is a property that holds before the first iteration, is maintained by each iteration, and implies correctness when the loop terminat...
- [[CS Algorithms/Analysis/Master Theorem|Master Theorem]] — The Master Theorem is a closed-form solution technique for divide-and-conquer recurrences of the form T(n) = aT(n/b) + f(n), determining T(n) by comp...
- [[CS Algorithms/Analysis/Recurrence Relations|Recurrence Relations]] — A recurrence relation expresses the running time of a recursive algorithm in terms of the running time on smaller inputs.

## Book II: Sorting And Searching

Watch small ordering problems become the laboratory for lower bounds and tradeoffs.

- [[CS Algorithms/Sorting/Sorting Overview|Sorting Overview]] — Note: Binary Search is grouped here because it operates on sorted arrays — its correctness and analysis are tightly coupled to the sorting algorithms...
- [[CS Algorithms/Sorting/Counting Sort|Counting Sort]] — Non-comparison integer sort that achieves Θ(m+n) time by counting key occurrences and computing prefix sums.
- [[CS Algorithms/Sorting/Insertion Sort|Insertion Sort]] — Builds a sorted prefix incrementally by shifting each element leftward into its correct position — optimal for small or nearly-sorted arrays.
- [[CS Algorithms/Sorting/Inversions|Inversions]] — The canonical measure of how unsorted an array is — the count of out-of-order pairs directly determines insertion sort's running time.
- [[CS Algorithms/Sorting/Merge Sort|Merge Sort]] — Divide-and-conquer comparison sort guaranteeing $\Theta(n \lg n)$ time in every case — the benchmark for worst-case-optimal sorting.
- [[CS Algorithms/Sorting/Quicksort|Quicksort]] — The fastest comparison sort in practice — partitions around a pivot to achieve expected $\Theta(n \lg n)$ with minimal overhead.
- [[CS Algorithms/Sorting/Radix Sort|Radix Sort]] — Non-comparison sort that processes keys digit-by-digit from least to most significant, achieving $\Theta(d(m+n)$) via stable counting sort passes.
- [[CS Algorithms/Sorting/Selection Sort|Selection Sort]] — Simple in-place sort that repeatedly selects the minimum from the unsorted suffix — unconditionally $\Theta(n²)$ but guarantees the fewest writes of...
- [[CS Algorithms/Searching/Binary Search|Binary Search]] — Binary search finds a target value in a sorted array by repeatedly halving the search space, running in $O(\lg n)$ worst case.

## Book III: Divide, Choose, And Backtrack

Compare the main problem-solving patterns by the kind of promise each one needs.

- [[CS Algorithms/Divide and Conquer/Divide and Conquer Overview — Domain|Divide and Conquer Overview — Domain]] — Divide and conquer breaks a problem into smaller subproblems of the same type, solves each recursively, and combines the results. It is the engine be...
- [[CS Algorithms/Divide and Conquer/Divide and Conquer Overview|Divide and Conquer Overview]] — Divide and conquer solves problems by recursively breaking them into smaller, independent sub-problems, solving each, and combining the results.
- [[CS Algorithms/Divide and Conquer/Master Theorem Applications|Master Theorem Applications]] — The Master Theorem provides a cookbook for solving recurrences of the form T(n) = aT(n/b) + $\Theta(n^c \log^k n)$, covering most divide-and-conquer...
- [[CS Algorithms/Greedy/Greedy Algorithms Overview|Greedy Algorithms Overview]] — Greedy algorithms build solutions incrementally, always choosing the locally optimal option at each step, and succeed when local optima guarantee a g...
- [[CS Algorithms/Greedy/Greedy Overview|Greedy Overview]] — Greedy algorithms make the locally optimal choice at each step, hoping to find a global optimum. When a problem exhibits the greedy-choice property (...
- [[CS Algorithms/Greedy/Activity Selection Problem|Activity Selection Problem]] — Select the maximum number of non-overlapping activities from a set with given start and finish times by always choosing the activity that finishes ea...
- [[CS Algorithms/Greedy/Fractional Knapsack|Fractional Knapsack]] — Maximize the total value in a weight-limited knapsack by greedily taking items in decreasing order of value-to-weight ratio, splitting the last item...
- [[CS Algorithms/Backtracking/Backtracking Overview — Domain|Backtracking Overview — Domain]] — Backtracking is systematic trial-and-error: build a candidate solution incrementally, and as soon as a partial candidate violates the problem constra...
- [[CS Algorithms/Backtracking/Backtracking Overview|Backtracking Overview]] — Backtracking systematically explores all potential solutions by building candidates incrementally and abandoning ("pruning") a branch as soon as it d...
- [[CS Algorithms/Backtracking/N-Queens Problem|N-Queens Problem]] — Place N queens on an N×N chessboard so that no two queens threaten each other — solved elegantly via backtracking with column, diagonal, and anti-dia...
- [[CS Algorithms/Techniques/Techniques Overview|Techniques Overview]] — Some algorithmic ideas are not tied to a single problem domain — they are cross-cutting techniques that appear in sorting, searching, graphs, strings...
- [[CS Algorithms/Techniques/Amortized Analysis for Algorithms|Amortized Analysis for Algorithms]] — Amortized analysis determines the average cost per operation over a worst-case sequence of operations, proving that expensive operations are rare eno...
- [[CS Algorithms/Techniques/Two Pointers and Sliding Window|Two Pointers and Sliding Window]] — Two Pointers uses a pair of indices moving inward (or in tandem) to solve problems on sorted arrays or sequences in $O(n)$, while Sliding Window main...

## Book IV: Graphs As Worlds

Move from arrays to relationships: traversal, paths, spanning trees, and flow.

- [[CS Algorithms/Graphs/Graphs Overview|Graphs Overview]] — Navigating shortest paths: Shortest Path Overview is the decision hub — it tells you which algorithm to use and why. Dijkstra, Bellman-Ford, and Floy...
- [[CS Algorithms/Graphs/Shortest Path Overview|Shortest Path Overview]] — Shortest-path algorithms find minimum-weight paths in weighted graphs, varying by single-source vs all-pairs, weight constraints, and graph structure.
- [[CS Algorithms/Graphs/Bellman-Ford Algorithm|Bellman-Ford Algorithm]] — Single-source shortest paths with negative edge weights and negative-cycle detection in $O(nm)$.
- [[CS Algorithms/Graphs/BFS and DFS|BFS and DFS]] — Breadth-First Search explores a graph level by level using a queue, while Depth-First Search dives as deep as possible along each branch using a stac...
- [[CS Algorithms/Graphs/DAG and Topological Sort|DAG and Topological Sort]] — Linear ordering of DAG vertices respecting all edge directions, computed in $\Theta(n+m)$ via Kahn's algorithm.
- [[CS Algorithms/Graphs/Dijkstra's Algorithm|Dijkstra's Algorithm]] — Single-source shortest paths in graphs with non-negative edge weights, driven by a min-priority queue.
- [[CS Algorithms/Graphs/Floyd-Warshall Algorithm|Floyd-Warshall Algorithm]] — All-pairs shortest paths via dynamic programming in $\Theta(n³)$, handling negative weights.
- [[CS Algorithms/Graphs/Graph Fundamentals|Graph Fundamentals]] — Core vocabulary and representations for all graph algorithms — vertices, edges, adjacency structures, and DAGs.
- [[CS Algorithms/Graphs/Kruskal's Algorithm|Kruskal's Algorithm]] — Kruskal's algorithm builds a Minimum Spanning Tree by sorting all edges by weight and greedily adding each edge that doesn't create a cycle, using a...
- [[CS Algorithms/Graphs/Minimum Spanning Trees|Minimum Spanning Trees]] — A Minimum Spanning Tree (MST) is a subset of edges in a weighted, connected, undirected graph that connects all vertices with the minimum total edge...
- [[CS Algorithms/Graphs/Network Flow — Ford-Fulkerson|Network Flow — Ford-Fulkerson]] — The Ford-Fulkerson method computes the maximum flow in a flow network by repeatedly finding augmenting paths from source to sink in the residual grap...
- [[CS Algorithms/Graphs/Prim's Algorithm|Prim's Algorithm]] — Prim's algorithm grows a Minimum Spanning Tree from a single source vertex by repeatedly adding the cheapest edge that connects the growing tree to a...

## Book V: Strings, Compression, And Cryptography

Read sequence algorithms, coding, and secrecy as applied versions of the same design discipline.

- [[CS Algorithms/Strings/Strings Overview|Strings Overview]] — String algorithms compute relationships between sequences — exact matches, longest common parts, and minimum-cost transformations. All three algorith...
- [[CS Algorithms/Strings/Edit Distance|Edit Distance]] — Minimum-cost transformation between two strings via insert, delete, and replace operations, solved by DP in $\Theta(mn)$.
- [[CS Algorithms/Strings/LCS - Longest Common Subsequence|LCS — Longest Common Subsequence]] — Find the longest subsequence common to two strings using DP in $\Theta(mn)$, with $O(m+n)$ backtracking for reconstruction.
- [[CS Algorithms/Strings/String Matching - KMP|String Matching — KMP]] — Find all occurrences of pattern P in text T in $\Theta(n+m)$ by precomputing a failure function that avoids redundant comparisons.
- [[CS Algorithms/Compression/Data Compression Overview|Data Compression Overview]] — Data compression reduces the number of bits needed to represent information. This page covers lossless compression only — perfect reconstruction guar...
- [[CS Algorithms/Compression/Huffman Coding|Huffman Coding]] — Greedy construction of the optimal prefix-free binary code for a given symbol frequency distribution in $\Theta(n \lg n)$.
- [[CS Algorithms/Compression/LZW Compression|LZW Compression]] — Lossless dictionary-based compression that builds a shared codebook on the fly — no dictionary transmission needed, single-pass encoding.
- [[CS Algorithms/Compression/Run-Length Encoding|Run-Length Encoding]] — Lossless compression that replaces contiguous runs of the same symbol with (count, symbol) pairs — $O(n)$ and self-describing.
- [[CS Algorithms/Cryptography/Cryptography Overview|Cryptography Overview]] — Cryptographic algorithms secure communication and data by exploiting mathematical hardness. This domain covers classical ciphers, the one-time pad, p...
- [[CS Algorithms/Cryptography/Cryptography Foundations|Cryptography Foundations]] — From substitution ciphers to hybrid encryption — the evolution of secret communication and why modern systems combine public-key exchange with symmet...
- [[CS Algorithms/Cryptography/Random Number Generation|Random Number Generation]] — Cryptographic security depends on unpredictable randomness — pseudorandom bit generators stretch a short secret seed into a long keystream that appea...
- [[CS Algorithms/Cryptography/RSA Algorithm|RSA Algorithm]] — Public-key cryptosystem where security rests on the hardness of integer factorisation — encrypt with a public key, decrypt with the matching private...

## Book VI: Hardness And Limits

End the theory arc with what efficient computation can and cannot plausibly do.

- [[CS Algorithms/Complexity/Complexity Theory Overview|Complexity Theory Overview]] — The study of what computers fundamentally can and cannot compute efficiently — covering P vs NP, NP-completeness, undecidability, and approximation a...
- [[CS Algorithms/Complexity/Approximation Algorithms|Approximation Algorithms]] — An approximation algorithm runs in polynomial time and returns a solution guaranteed to be within a constant factor of optimal — a principled respons...
- [[CS Algorithms/Complexity/Halting Problem|Halting Problem]] — The Halting Problem asks whether an arbitrary program halts on a given input — Turing (1936) proved no algorithm can decide this for all programs.
- [[CS Algorithms/Complexity/NP Completeness|NP Completeness]] — NP-complete problems are the hardest problems in NP — every NP problem reduces to them, yet no polynomial-time algorithm is known for any of them.
- [[CS Algorithms/Complexity/P vs NP|P vs NP]] — The P vs NP problem asks whether every problem whose solution can be verified quickly can also be solved quickly — the central unsolved question in t...

## Book VII: The Textbook Walkthrough

Use chapter notes as the guided classroom route through the source material.

- [[CS Algorithms/Books/Algorithms Unlocked/Chapter Index|Chapter Index — Algorithms Unlocked]] — Navigation table for all chapter notes. See Algorithms Unlocked for the full book MOC.
- [[CS Algorithms/Books/Algorithms Unlocked/Chapters/AU - Chapter 01|AU — Chapter 01: What Are Algorithms and Why Should You Care?]] — Cormen opens by establishing what distinguishes a computer algorithm from a vague human procedure: the algorithm must be precise enough that a machin...
- [[CS Algorithms/Books/Algorithms Unlocked/Chapters/AU - Chapter 02|AU — Chapter 02: How to Describe and Evaluate Computer Algorithms]] — Chapter 2 builds the notational and proof vocabulary used throughout the rest of the book. Cormen introduces the RAM model: a single processor, one u...
- [[CS Algorithms/Books/Algorithms Unlocked/Chapters/AU - Chapter 03|AU — Chapter 03: Algorithms for Sorting and Searching]] — The book's most algorithm-dense chapter covers one search and four sort algorithms. Binary search on a sorted array eliminates half the search space...
- [[CS Algorithms/Books/Algorithms Unlocked/Chapters/AU - Chapter 04|AU — Chapter 04: A Lower Bound for Sorting and How to Beat It]] — Chapter 4 answers a fundamental question: is $\Theta(n \lg n)$ the best we can do for sorting? The answer depends on the rules. Any algorithm that de...
- [[CS Algorithms/Books/Algorithms Unlocked/Chapters/AU - Chapter 05|AU — Chapter 05: Directed Acyclic Graphs]] — Cormen introduces graphs through a vivid concrete example: putting on hockey goalie equipment in dependency order. The diagram of items with "must go...
- [[CS Algorithms/Books/Algorithms Unlocked/Chapters/AU - Chapter 06|AU — Chapter 06: Shortest Paths]] — Chapter 6 extends shortest-path finding from acyclic graphs (Chapter 5) to general directed graphs with cycles. Three landmark algorithms address dif...
- [[CS Algorithms/Books/Algorithms Unlocked/Chapters/AU - Chapter 07|AU — Chapter 07: Algorithms on Strings]] — Chapter 7 covers three classical string problems. Longest Common Subsequence (LCS): a subsequence preserves relative character order but need not be...
- [[CS Algorithms/Books/Algorithms Unlocked/Chapters/AU - Chapter 08|AU — Chapter 08: Foundations of Cryptography]] — Chapter 8 surveys cryptographic algorithms motivated by the practical problem of transmitting sensitive data over a public network. Simple substituti...
- [[CS Algorithms/Books/Algorithms Unlocked/Chapters/AU - Chapter 09|AU — Chapter 09: Data Compression]] — Chapter 9 asks: if the previous chapter was about hiding information, how do we shrink it? The focus is entirely on lossless compression — perfect re...
- [[CS Algorithms/Books/Algorithms Unlocked/Chapters/AU - Chapter 10|AU — Chapter 10: Hard? Problems]] — The final chapter tackles the deepest question in algorithmic theory: which problems are truly hard? Cormen begins with the Travelling Salesman Probl...
- [[CS Algorithms/Books/Algorithms Unlocked/Algorithms Unlocked|Algorithms Unlocked]] — Author: Thomas H. Cormen

## Appendices: Practice And Sources

Switch from reading to recall, selection, and provenance.

- [[CS Algorithms/Study/Algorithms Study Index|Algorithms Study Index]] — Central index for all CS Algorithms active-recall drill notes. Each drill note covers one domain of the wiki, distilled into questions, contrasts, an...
- [[CS Algorithms/Study/Algorithm Complexity Cheatsheet|Algorithm Complexity Cheatsheet]] — Compiled quick-reference for time and space complexities across all domains in the CS Algorithms knowledge base. Use for rapid review, algorithm sele...
- [[CS Algorithms/Study/Complexity Theory - Review Drill|Complexity Theory — Review Drill]] — Active-recall drill covering computational complexity classes, undecidability, NP-completeness, and approximation algorithms.
- [[CS Algorithms/Study/Cryptography - Review Drill|Cryptography — Review Drill]] — Active-recall drill covering classical ciphers, modern cryptographic primitives, RSA, and randomness security.
- [[CS Algorithms/Study/Data Compression - Review Drill|Data Compression — Review Drill]] — Active-recall drill covering lossless compression algorithms: run-length encoding, Huffman coding, and LZW.
- [[CS Algorithms/Study/Foundations and Analysis - Review Drill|Foundations and Analysis — Review Drill]] — Active-recall drill for the core vocabulary, proof machinery, and analysis tools used throughout CS Algorithms.
- [[CS Algorithms/Study/Graphs and Shortest Paths - Review Drill|Graphs and Shortest Paths — Review Drill]] — Active-recall drill covering graph vocabulary, DAG processing, and all major shortest-path algorithms.
- [[CS Algorithms/Study/Sorting and Searching - Review Drill|Sorting and Searching — Review Drill]] — Active-recall drill covering comparison sorts, non-comparison sorts, the sorting lower bound, inversion analysis, and binary search.
- [[CS Algorithms/Study/Strings - Review Drill|Strings — Review Drill]] — Active-recall drill covering dynamic programming on strings and linear-time string matching.
- [[CS Algorithms/Sources/Sources Index|Sources Index]]

## Coverage

- Reader-facing articles linked here: 83
- Protected raw, chunk, template, query, audio, and operations folders are intentionally not expanded here.
- The root vault index remains the exhaustive generated listing across every topic.

## References

- [[CS Algorithms/CS Algorithms|CS Algorithms]]
- [[CS Algorithms/Sources/Sources Index|Sources Index]]
