import os
from pathlib import Path

VAULT = Path(r"D:\Vaults\PersonalKB")

def write(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Created: {path.name} ({len(content)} chars)")

def insert_after(filepath, search_line, insert_text):
    p = Path(filepath)
    lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
    new_lines = []
    inserted = False
    for line in lines:
        new_lines.append(line)
        if not inserted and search_line in line:
            if not line.endswith("\n"):
                new_lines.append("\n")
            new_lines.append(insert_text + "\n")
            new_lines.append("\n")
            inserted = True
    if inserted:
        p.write_text("".join(new_lines), encoding="utf-8")
        print(f"  Modified: {p.name} (inserted Learning Path link)")
    else:
        print(f"  WARNING: Could not find '{search_line}' in {p.name}")

# === TEMPLATE ===
TEMPLATE = """---
tags: []
tier-coverage: [intuition, core, deep-dive, practice]
---
# {Topic Name}

> **One-line summary**: {What this is and why it matters}

## 🎯 Intuition

{2-minute read. Analogy-driven. No jargon. Build a mental picture.}

**The Core Idea:** {One sentence}

**Analogy:** {Real-world comparison}

**Why It Matters:** {When you'd reach for this}

---

## ⚙️ Core Mechanics

{Textbook level. Pseudocode, operations, complexity.}

### How It Works
{Step-by-step description}

### Key Operations

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| ... | ... | ... | ... |

### Pseudocode
{Clean pseudocode for the main algorithm/operations}

---

## 🔬 Deep Dive

{Proofs, optimizations, edge cases, variants, real-world tradeoffs.}

### Correctness / Proof Sketch
{Why it works}

### Optimizations and Variants
{Practical improvements}

### Edge Cases and Pitfalls
{What can go wrong}

### Real-World Usage
{Where this appears in production systems}

---

## 🏋️ Practice

### Warm-Up (5 min)
{Conceptual questions — no code needed}

### Core Problems
{2-3 coding/analysis problems, increasing difficulty}

### Challenge
{1 hard problem or open-ended design question}

---

*See also:* {Cross-links to related pages in both wikis}
"""

# === ALGORITHMS LEARNING PATH ===
ALGO_LP = """---
tags: [csa, learning-path]
up: "[[CS Algorithms]]"
---
# CS Algorithms — Learning Path

> This path is designed for **progressive learning** — you don't read everything at once. Make multiple passes, each going deeper.

## How to Use This Path

| Pass | Read | Goal | Time |
|------|------|------|------|
| 🎯 **Pass 1 — Intuition** | Only `🎯 Intuition` sections | Build mental models, see the landscape | ~2 hrs |
| ⚙️ **Pass 2 — Core** | Add `⚙️ Core Mechanics` sections | Understand how things work, pseudocode fluency | ~8 hrs |
| 🔬 **Pass 3 — Mastery** | Add `🔬 Deep Dive` on topics you choose | Proofs, optimizations, expert-level understanding | ~15 hrs |
| 🏋️ **Pass 4 — Practice** | `🏋️ Practice` sections + Study Drills | Solve problems, build muscle memory | Ongoing |

> **Rule:** Don't move to Pass 2 until you've completed Pass 1 for the entire sequence. Breadth before depth.

---

## The Sequence

### 1. Foundations and Analysis
*What algorithms are, how we measure them, and the tools for reasoning about them.*

1. [[Algorithm Definition]]
2. [[Asymptotic Notation]]
3. [[Loop Invariant]]
4. [[Recurrence Relations]]
5. [[Master Theorem]]

📝 *After Pass 2:* [[Foundations and Analysis - Review Drill]]

### 2. Sorting and Searching
*The classic algorithms that introduce algorithmic thinking patterns.*

6. [[Selection Sort]]
7. [[Insertion Sort]]
8. [[Merge Sort]]
9. [[Quicksort]]
10. [[Counting Sort]]
11. [[Radix Sort]]
12. [[Comparison Sort Lower Bound]]
13. [[Binary Search]]
14. [[Inversions]]

📝 *After Pass 2:* [[Sorting and Searching - Review Drill]]

### 3. Graphs and Shortest Paths
*Structures and algorithms for connected data — the backbone of CS.*

15. [[Graph Fundamentals]]
16. [[BFS and DFS]]
17. [[DAG and Topological Sort]]
18. [[Shortest Path Overview]]
19. [[Dijkstra's Algorithm]]
20. [[Bellman-Ford Algorithm]]
21. [[Floyd-Warshall Algorithm]]
22. [[Minimum Spanning Trees]]
23. [[Kruskal's Algorithm]]
24. [[Prim's Algorithm]]

📝 *After Pass 2:* [[Graphs and Shortest Paths - Review Drill]]

### 4. Greedy Algorithms
*When locally optimal choices lead to globally optimal solutions.*

25. [[Greedy Algorithms Overview]]
26. [[Activity Selection Problem]]
27. [[Fractional Knapsack]]

### 5. Divide and Conquer
*Breaking problems into subproblems, solving recursively, combining results.*

28. [[Divide and Conquer Overview]]
29. [[Master Theorem Applications]]

### 6. Dynamic Programming
*When subproblems overlap — memoize and build up solutions.*

30. [[Dynamic Programming]]

### 7. Backtracking
*Systematic trial-and-error with pruning.*

31. [[Backtracking Overview]]
32. [[N-Queens Problem]]

### 8. Algorithmic Techniques
*Cross-cutting patterns that appear everywhere.*

33. [[Two Pointers and Sliding Window]]
34. [[Amortized Analysis for Algorithms]]

### 9. Strings
*Pattern matching, sequence comparison, and text algorithms.*

35. [[LCS - Longest Common Subsequence]]
36. [[Edit Distance]]
37. [[String Matching - KMP]]

📝 *After Pass 2:* [[Strings - Review Drill]]

### 10. Cryptography
*Mathematical foundations of secure communication.*

38. [[Cryptography Foundations]]
39. [[Random Number Generation]]
40. [[RSA Algorithm]]

📝 *After Pass 2:* [[Cryptography - Review Drill]]

### 11. Data Compression
*Representing information with fewer bits.*

41. [[Huffman Coding]]
42. [[Run-Length Encoding]]
43. [[LZW Compression]]

📝 *After Pass 2:* [[Data Compression - Review Drill]]

### 12. Complexity Theory
*The limits of computation — what can and can't be solved efficiently.*

44. [[P vs NP]]
45. [[NP Completeness]]
46. [[Halting Problem]]
47. [[Approximation Algorithms]]
48. [[Network Flow — Ford-Fulkerson]]

📝 *After Pass 2:* [[Complexity Theory - Review Drill]]

---

## Cross-Reference

> 🔗 Many algorithm topics have a companion page in [[CS Data Structures]]. When you study graph algorithms, also read [[Graph Properties and Terminology]] in the DS wiki. When you study heapsort/Dijkstra, read [[Binary Heaps]].

---

## Progress Tracker

| # | Topic | Pass 1 | Pass 2 | Pass 3 | Pass 4 |
|---|-------|--------|--------|--------|--------|
| 1 | Algorithm Definition | ☐ | ☐ | ☐ | ☐ |
| 2 | Asymptotic Notation | ☐ | ☐ | ☐ | ☐ |
| 3 | Loop Invariant | ☐ | ☐ | ☐ | ☐ |
| 4 | Recurrence Relations | ☐ | ☐ | ☐ | ☐ |
| 5 | Master Theorem | ☐ | ☐ | ☐ | ☐ |
| 6 | Selection Sort | ☐ | ☐ | ☐ | ☐ |
| 7 | Insertion Sort | ☐ | ☐ | ☐ | ☐ |
| 8 | Merge Sort | ☐ | ☐ | ☐ | ☐ |
| 9 | Quicksort | ☐ | ☐ | ☐ | ☐ |
| 10 | Counting Sort | ☐ | ☐ | ☐ | ☐ |
| 11 | Radix Sort | ☐ | ☐ | ☐ | ☐ |
| 12 | Comparison Sort Lower Bound | ☐ | ☐ | ☐ | ☐ |
| 13 | Binary Search | ☐ | ☐ | ☐ | ☐ |
| 14 | Inversions | ☐ | ☐ | ☐ | ☐ |
| 15 | Graph Fundamentals | ☐ | ☐ | ☐ | ☐ |
| 16 | BFS and DFS | ☐ | ☐ | ☐ | ☐ |
| 17 | DAG and Topological Sort | ☐ | ☐ | ☐ | ☐ |
| 18 | Shortest Path Overview | ☐ | ☐ | ☐ | ☐ |
| 19 | Dijkstra's Algorithm | ☐ | ☐ | ☐ | ☐ |
| 20 | Bellman-Ford Algorithm | ☐ | ☐ | ☐ | ☐ |
| 21 | Floyd-Warshall Algorithm | ☐ | ☐ | ☐ | ☐ |
| 22 | Minimum Spanning Trees | ☐ | ☐ | ☐ | ☐ |
| 23 | Kruskal's Algorithm | ☐ | ☐ | ☐ | ☐ |
| 24 | Prim's Algorithm | ☐ | ☐ | ☐ | ☐ |
| 25 | Greedy Algorithms Overview | ☐ | ☐ | ☐ | ☐ |
| 26 | Activity Selection Problem | ☐ | ☐ | ☐ | ☐ |
| 27 | Fractional Knapsack | ☐ | ☐ | ☐ | ☐ |
| 28 | Divide and Conquer Overview | ☐ | ☐ | ☐ | ☐ |
| 29 | Master Theorem Applications | ☐ | ☐ | ☐ | ☐ |
| 30 | Dynamic Programming | ☐ | ☐ | ☐ | ☐ |
| 31 | Backtracking Overview | ☐ | ☐ | ☐ | ☐ |
| 32 | N-Queens Problem | ☐ | ☐ | ☐ | ☐ |
| 33 | Two Pointers and Sliding Window | ☐ | ☐ | ☐ | ☐ |
| 34 | Amortized Analysis for Algorithms | ☐ | ☐ | ☐ | ☐ |
| 35 | LCS | ☐ | ☐ | ☐ | ☐ |
| 36 | Edit Distance | ☐ | ☐ | ☐ | ☐ |
| 37 | String Matching - KMP | ☐ | ☐ | ☐ | ☐ |
| 38 | Cryptography Foundations | ☐ | ☐ | ☐ | ☐ |
| 39 | Random Number Generation | ☐ | ☐ | ☐ | ☐ |
| 40 | RSA Algorithm | ☐ | ☐ | ☐ | ☐ |
| 41 | Huffman Coding | ☐ | ☐ | ☐ | ☐ |
| 42 | Run-Length Encoding | ☐ | ☐ | ☐ | ☐ |
| 43 | LZW Compression | ☐ | ☐ | ☐ | ☐ |
| 44 | P vs NP | ☐ | ☐ | ☐ | ☐ |
| 45 | NP Completeness | ☐ | ☐ | ☐ | ☐ |
| 46 | Halting Problem | ☐ | ☐ | ☐ | ☐ |
| 47 | Approximation Algorithms | ☐ | ☐ | ☐ | ☐ |
| 48 | Network Flow | ☐ | ☐ | ☐ | ☐ |

---

*Part of [[CS Algorithms]]. See also: [[CS Data Structures — Learning Path]]*
"""

# === DATA STRUCTURES LEARNING PATH ===
DS_LP = """---
tags: [cs-ds, learning-path]
up: "[[CS Data Structures]]"
---
# CS Data Structures — Learning Path

> This path is designed for **progressive learning** — you don't read everything at once. Make multiple passes, each going deeper.

## How to Use This Path

| Pass | Read | Goal | Time |
|------|------|------|------|
| 🎯 **Pass 1 — Intuition** | Only `🎯 Intuition` sections | Build mental models, see the landscape | ~2 hrs |
| ⚙️ **Pass 2 — Core** | Add `⚙️ Core Mechanics` sections | Understand operations, complexity, tradeoffs | ~8 hrs |
| 🔬 **Pass 3 — Mastery** | Add `🔬 Deep Dive` on topics you choose | Implementation details, proofs, real-world usage | ~12 hrs |
| 🏋️ **Pass 4 — Practice** | `🏋️ Practice` sections + Study Drills | Implement from scratch, solve problems | Ongoing |

> **Rule:** Don't move to Pass 2 until you've completed Pass 1 for the entire sequence. Breadth before depth.

---

## The Sequence

### 1. Foundational Concepts
*The vocabulary and analytical tools for reasoning about data structures.*

1. [[Abstract Data Types]]
2. [[Asymptotic Analysis and Big-O Notation]]
3. [[Amortized Analysis]]
4. [[Memory Layout and Cache Performance]]
5. [[Pointer-Based vs Array-Based Structures]]
6. [[Data Structure Comparison and Selection]]

### 2. Linear Structures
*Sequential storage — the building blocks everything else is built on.*

7. [[Arrays and Dynamic Arrays]]
8. [[Singly Linked Lists]]
9. [[Doubly Linked Lists and Circular Lists]]
10. [[Stacks]]
11. [[Queues and Deques]]
12. [[Circular Buffers]]

📝 *After Pass 2:* [[DS Review — Linear Structures]]

### 3. Trees
*Hierarchical structures — the workhorse of CS.*

13. [[Binary Trees and Traversals]]
14. [[Binary Search Trees]]
15. [[AVL Trees]]
16. [[Red-Black Trees]]
17. [[B-Trees and B-Plus Trees]]
18. [[Splay Trees and Treaps]]

📝 *After Pass 2:* [[DS Review — Trees and Balancing]]

### 4. Heaps and Priority Queues
*Efficient access to the most important element.*

19. [[Priority Queue ADT]]
20. [[Binary Heaps]]
21. [[Binomial Heaps]]
22. [[Fibonacci Heaps]]
23. [[Heap Applications and d-ary Heaps]]

📝 *After Pass 2:* [[DS Review — Heaps and Priority Queues]]

### 5. Hash-Based Structures
*O(1) average-case access — the power of hashing.*

24. [[Hash Tables and Hash Functions]]
25. [[Collision Resolution Strategies]]
26. [[Universal and Perfect Hashing]]
27. [[Cuckoo Hashing]]
28. [[Consistent Hashing]]
29. [[Bloom Filters and Probabilistic Structures]]
30. [[Count-Min Sketch]]
31. [[HyperLogLog]]

📝 *After Pass 2:* [[DS Review — Hash Tables]]

### 6. Graph Representations
*How to store and traverse connected data.*

32. [[Graph Properties and Terminology]]
33. [[Adjacency List and Adjacency Matrix]]
34. [[Weighted and Directed Graphs]]
35. [[Implicit and Compressed Graph Representations]]

### 7. Tries and String Structures
*Specialized trees for string and prefix operations.*

36. [[Tries and Prefix Trees]]
37. [[Compressed Tries and Radix Trees]]
38. [[Ternary Search Trees]]
39. [[Suffix Trees]]
40. [[Suffix Arrays]]
41. [[Rope Data Structure]]

### 8. Advanced Structures
*Sophisticated tools for specialized problems.*

42. [[Skip Lists]]
43. [[Disjoint Sets and Union-Find]]
44. [[Segment Trees]]
45. [[Fenwick Trees]]
46. [[Interval Trees and Range Trees]]
47. [[k-d Trees and Spatial Data Structures]]
48. [[LRU and LFU Caches]]

### 9. Frontier Topics
*Modern and specialized structures for production systems.*

49. [[Concurrent Data Structures]]
50. [[Lock-Free Queues and Stacks]]
51. [[Persistent and Immutable Structures]]
52. [[Cache-Oblivious Structures]]
53. [[External Memory Structures]]
54. [[Succinct and Compressed Data Structures]]

📝 *After Pass 2:* [[DS Review — Advanced Structures]]

---

## Cross-Reference

> 🔗 Many data structure topics have a companion page in [[CS Algorithms]]. When you study heaps, also read [[Dijkstra's Algorithm]] which uses them. When you study graphs, see the full family of [[Shortest Path Overview|shortest-path algorithms]].

---

## Progress Tracker

| # | Topic | Pass 1 | Pass 2 | Pass 3 | Pass 4 |
|---|-------|--------|--------|--------|--------|
| 1 | Abstract Data Types | ☐ | ☐ | ☐ | ☐ |
| 2 | Asymptotic Analysis | ☐ | ☐ | ☐ | ☐ |
| 3 | Amortized Analysis | ☐ | ☐ | ☐ | ☐ |
| 4 | Memory Layout | ☐ | ☐ | ☐ | ☐ |
| 5 | Pointer vs Array | ☐ | ☐ | ☐ | ☐ |
| 6 | Comparison and Selection | ☐ | ☐ | ☐ | ☐ |
| 7 | Arrays and Dynamic Arrays | ☐ | ☐ | ☐ | ☐ |
| 8 | Singly Linked Lists | ☐ | ☐ | ☐ | ☐ |
| 9 | Doubly Linked Lists | ☐ | ☐ | ☐ | ☐ |
| 10 | Stacks | ☐ | ☐ | ☐ | ☐ |
| 11 | Queues and Deques | ☐ | ☐ | ☐ | ☐ |
| 12 | Circular Buffers | ☐ | ☐ | ☐ | ☐ |
| 13 | Binary Trees | ☐ | ☐ | ☐ | ☐ |
| 14 | BST | ☐ | ☐ | ☐ | ☐ |
| 15 | AVL Trees | ☐ | ☐ | ☐ | ☐ |
| 16 | Red-Black Trees | ☐ | ☐ | ☐ | ☐ |
| 17 | B-Trees | ☐ | ☐ | ☐ | ☐ |
| 18 | Splay Trees / Treaps | ☐ | ☐ | ☐ | ☐ |
| 19 | Priority Queue ADT | ☐ | ☐ | ☐ | ☐ |
| 20 | Binary Heaps | ☐ | ☐ | ☐ | ☐ |
| 21 | Binomial Heaps | ☐ | ☐ | ☐ | ☐ |
| 22 | Fibonacci Heaps | ☐ | ☐ | ☐ | ☐ |
| 23 | Heap Applications | ☐ | ☐ | ☐ | ☐ |
| 24 | Hash Tables | ☐ | ☐ | ☐ | ☐ |
| 25 | Collision Resolution | ☐ | ☐ | ☐ | ☐ |
| 26 | Universal Hashing | ☐ | ☐ | ☐ | ☐ |
| 27 | Cuckoo Hashing | ☐ | ☐ | ☐ | ☐ |
| 28 | Consistent Hashing | ☐ | ☐ | ☐ | ☐ |
| 29 | Bloom Filters | ☐ | ☐ | ☐ | ☐ |
| 30 | Count-Min Sketch | ☐ | ☐ | ☐ | ☐ |
| 31 | HyperLogLog | ☐ | ☐ | ☐ | ☐ |
| 32 | Graph Properties | ☐ | ☐ | ☐ | ☐ |
| 33 | Adjacency List/Matrix | ☐ | ☐ | ☐ | ☐ |
| 34 | Weighted/Directed Graphs | ☐ | ☐ | ☐ | ☐ |
| 35 | Compressed Graphs | ☐ | ☐ | ☐ | ☐ |
| 36 | Tries | ☐ | ☐ | ☐ | ☐ |
| 37 | Compressed Tries | ☐ | ☐ | ☐ | ☐ |
| 38 | Ternary Search Trees | ☐ | ☐ | ☐ | ☐ |
| 39 | Suffix Trees | ☐ | ☐ | ☐ | ☐ |
| 40 | Suffix Arrays | ☐ | ☐ | ☐ | ☐ |
| 41 | Rope | ☐ | ☐ | ☐ | ☐ |
| 42 | Skip Lists | ☐ | ☐ | ☐ | ☐ |
| 43 | Union-Find | ☐ | ☐ | ☐ | ☐ |
| 44 | Segment Trees | ☐ | ☐ | ☐ | ☐ |
| 45 | Fenwick Trees | ☐ | ☐ | ☐ | ☐ |
| 46 | Interval Trees | ☐ | ☐ | ☐ | ☐ |
| 47 | k-d Trees | ☐ | ☐ | ☐ | ☐ |
| 48 | LRU/LFU Caches | ☐ | ☐ | ☐ | ☐ |
| 49 | Concurrent DS | ☐ | ☐ | ☐ | ☐ |
| 50 | Lock-Free Structures | ☐ | ☐ | ☐ | ☐ |
| 51 | Persistent Structures | ☐ | ☐ | ☐ | ☐ |
| 52 | Cache-Oblivious | ☐ | ☐ | ☐ | ☐ |
| 53 | External Memory | ☐ | ☐ | ☐ | ☐ |
| 54 | Succinct DS | ☐ | ☐ | ☐ | ☐ |

---

*Part of [[CS Data Structures]]. See also: [[CS Algorithms — Learning Path]]*
"""

print("=== Phase 1: Creating files ===")

# 1. Templates
write(VAULT / "CS Algorithms" / "_templates" / "Tiered Page Template.md", TEMPLATE)
write(VAULT / "CS Data Structures" / "_templates" / "Tiered Page Template.md", TEMPLATE)

# 2. Learning Paths
write(VAULT / "CS Algorithms" / "CS Algorithms — Learning Path.md", ALGO_LP)
write(VAULT / "CS Data Structures" / "CS Data Structures — Learning Path.md", DS_LP)

# 3. Update MOCs
print("\n=== Updating MOCs ===")
insert_after(
    VAULT / "CS Algorithms" / "CS Algorithms.md",
    "complexity theory.",
    '> 📚 **New here?** Start with the [[CS Algorithms — Learning Path|Learning Path]] for a guided, progressive tour.'
)
insert_after(
    VAULT / "CS Data Structures" / "CS Data Structures.md",
    "efficient software.",
    '> 📚 **New here?** Start with the [[CS Data Structures — Learning Path|Learning Path]] for a guided, progressive tour.'
)

# 4. Verify
print("\n=== Verification ===")
for f in [
    VAULT / "CS Algorithms" / "_templates" / "Tiered Page Template.md",
    VAULT / "CS Data Structures" / "_templates" / "Tiered Page Template.md",
    VAULT / "CS Algorithms" / "CS Algorithms — Learning Path.md",
    VAULT / "CS Data Structures" / "CS Data Structures — Learning Path.md",
]:
    if f.exists():
        print(f"✓ {f.name} ({f.stat().st_size} bytes)")
    else:
        print(f"✗ {f.name} MISSING!")

print("\nDone!")
