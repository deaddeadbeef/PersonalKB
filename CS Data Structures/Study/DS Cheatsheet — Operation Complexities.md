---
tags: [cs-ds, study, cheatsheet]
up: "[[CS Data Structures Study Index]]"
---

# DS Cheatsheet — Operation Complexities

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

*Average/amortized. **At known node.
