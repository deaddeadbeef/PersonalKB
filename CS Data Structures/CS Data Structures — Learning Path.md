---
tags: [cs-ds, learning-path]
up: "[[CS Data Structures]]"
confidence: verified
freshness: stable
tier-coverage: [core, practice]
---
# CS Data Structures — Learning Path

> This path is designed for **progressive learning** — you don't read everything at once. Make multiple passes, each going deeper.

## Where This Fits

| Need | Use |
|---|---|
| Read data structures like a book | [[CS Data Structures/CS Data Structures Book Reading Spine|CS Data Structures Book Reading Spine]] |
| Follow a pass-based curriculum | This learning path |
| Choose a structure for code or review costs | [[CS Data Structures/Study/CS Data Structures Study Index|CS Data Structures Study Index]] |
| Verify operation costs, workload assumptions, or source claims | [[CS Data Structures/Sources/Sources Index|CS Data Structures Sources Index]] |

Use this path when you want staged coverage. Use the book spine when you want the story of memory and access patterns, and use the study index when the goal is a concrete selection decision.

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
*$O(1)$ average-case access — the power of hashing.*

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

## References

- [[CS Data Structures/CS Data Structures Book Reading Spine]]
- [[CS Data Structures/Sources/Sources Index]]
