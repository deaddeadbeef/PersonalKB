---
tags: [cs-ds, study, drill]
up: "[[CS Data Structures Study Index]]"
confidence: verified
freshness: stable
---

# DS Review — Trees and Balancing

## Quick-Fire Questions

1. What are the four binary tree traversal orders?
2. Why does a BST degenerate with sorted input?
3. What are the four AVL rotation cases?
4. Name the five Red-Black tree properties.
5. Why do databases use B+ trees instead of BSTs?
6. How do splay trees achieve amortized $O(\log n)$ without balance info?

## Compare and Contrast

| Tree | Height Guarantee | Rotations per Insert | Best For |
|------|-----------------|---------------------|----------|
| BST | None ($O(n)$ worst) | 0 | Simple, random data |
| AVL | 1.44 log n | $O(\log n)$ | Read-heavy |
| Red-Black | 2 log n | At most 2 | Write-heavy, libraries |
| B-Tree | log_m n | 0 (split instead) | Disk/database |
| Splay | None (amortized) | $O(\log n)$ amortized | Locality of access |

## Orientation

- Read the table as a balance-policy comparison: stricter balancing improves lookup predictability, while looser balancing reduces maintenance work.
- Separate binary-search-tree ordering from traversal knowledge; both matter in exams and interviews.
- For storage systems, think in pages and fan-out first, which is why [[B-Trees and B-Plus Trees]] dominate over pointer-heavy binary trees.

## Common Traps

- Forgetting that plain BST guarantees disappear under adversarial or sorted insertion orders.
- Memorizing rotation names without being able to identify the imbalance that triggers them.
- Treating amortized guarantees in [[Splay Trees and Treaps]] as per-operation worst-case guarantees.

## Practice Loop

1. Recite the four AVL imbalance cases and what single or double rotation fixes each one.
2. Explain why red-black trees usually trade slightly taller height for cheaper updates.
3. Contrast when you would reach for [[Binary Search Trees]], [[AVL Trees]], [[Red-Black Trees]], or [[B-Trees and B-Plus Trees]].

## References

- [[Trees Overview]]
- [[Binary Trees and Traversals]]
- [[Binary Search Trees]]
- [[AVL Trees]]
- [[Red-Black Trees]]
- [[B-Trees and B-Plus Trees]]
- [[Splay Trees and Treaps]]
- [[Data Structure Comparison and Selection]]
- [[CS Data Structures/Sources/Sources Index|Sources Index]]
