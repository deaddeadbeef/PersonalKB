---
tags: [cs-ds, study, cheatsheet]
up: "[[CS Data Structures Study Index]]"
confidence: verified
freshness: stable
---

# DS Cheatsheet — Operation Complexities

Use this page to compare typical operation costs quickly, then verify assumptions against the linked canonical notes when implementation details matter.

## Linear Structures

| Structure | Access | Search | Insert Front | Insert Back | Delete |
|-----------|--------|--------|-------------|-------------|--------|
| Array | $O(1)$ | $O(n)$ | $O(n)$ | $O(1)$* | $O(n)$ |
| SLL | $O(n)$ | $O(n)$ | $O(1)$ | $O(n)$ | $O(n)$ |
| DLL | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ | $O(1)$** |
| Stack | $O(n)$ | $O(n)$ | $O(1)$ | - | $O(1)$ |
| Queue | $O(n)$ | $O(n)$ | - | $O(1)$ | $O(1)$ |

## Trees

| Structure | Search | Insert | Delete | Space |
|-----------|--------|--------|--------|-------|
| BST | $O(\log n)$* | $O(\log n)$* | $O(\log n)$* | $O(n)$ |
| AVL | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ |
| Red-Black | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ |
| B-Tree | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ |

## Hash Tables

| Operation | Average | Worst |
|-----------|---------|-------|
| Search | $O(1)$ | $O(n)$ |
| Insert | $O(1)$ | $O(n)$ |
| Delete | $O(1)$ | $O(n)$ |

## Heaps

| Operation | Binary | Fibonacci |
|-----------|--------|-----------|
| Insert | $O(\log n)$ | $O(1)$* |
| Extract-Min | $O(\log n)$ | $O(\log n)$* |
| Decrease-Key | $O(\log n)$ | $O(1)$* |

## How to Read This Sheet

- Treat starred entries as context-dependent average or amortized bounds, not blanket worst-case guarantees.
- Constant factors and memory locality still matter: contiguous layouts often beat pointer-heavy structures for real workloads.
- For exam recall, pair each row with a mental "why" (resizing, rotations, probing, consolidation) rather than memorizing symbols alone.

A quick navigation path:
- Linear: [[Linear Structures Overview]], [[Arrays and Dynamic Arrays]], [[Circular Buffers]]
- Trees: [[Trees Overview]], [[Binary Search Trees]], [[AVL Trees]], [[Red-Black Trees]], [[B-Trees and B-Plus Trees]]
- Hashing: [[Hash-Based Structures Overview]], [[Hash Tables and Hash Functions]], [[Collision Resolution Strategies]]

*Average/amortized. **At known node.

## References

- [[Asymptotic Analysis and Big-O Notation]]
- [[Amortized Analysis]]
- [[Memory Layout and Cache Performance]]
- [[Data Structure Comparison and Selection]]
- [[CS Data Structures/Sources/Sources Index|Sources Index]]
