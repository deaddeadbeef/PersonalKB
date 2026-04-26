---
tags: [cs-ds, study, drill]
up: "[[CS Data Structures Study Index]]"
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
