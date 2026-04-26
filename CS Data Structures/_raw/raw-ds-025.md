---
tags: [cs-ds, raw]
id: raw-ds-025
source: "Open Data Structures (Morin, Ch. 7)"
up: "[[CS Data Structures]]"
---

# Treaps and Randomized BSTs

## Key Ideas
- Treap = Tree + Heap: BST by keys, heap by random priorities
- Each node has key and randomly assigned priority
- BST property on keys, heap property on priorities
- Expected height: O(log n), same as randomly built BST
- Insert: BST insert then rotate up to restore heap property
- Delete: rotate node down until leaf, then remove
- Split: split tree into two treaps by key threshold, O(log n) expected
- Merge: merge two treaps, O(log n) expected
- Implicit treap: use subtree sizes as implicit keys for array operations
- Advantages over AVL and RB: simpler implementation, supports split/merge natively
- vs Skip List: similar expected bounds, treap is tree-shaped vs layered
