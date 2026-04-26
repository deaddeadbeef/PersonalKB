---
tags: [cs-ds, raw]
id: raw-ds-024
source: "Purely Functional Data Structures (Okasaki)"
up: "[[CS Data Structures]]"
---

# Persistent and Immutable Data Structures

## Key Ideas
- Persistent: preserves all previous versions after mutation
- Path copying: copy only modified path from root to changed node
- Structural sharing: unchanged subtrees shared between versions
- Persistent BST: path copying gives O(log n) update with O(log n) extra space
- Clojure vectors: 32-way tries with structural sharing, near O(1) operations
- Git object model: content-addressed persistent tree
- Immutability enables: safe concurrency, time-travel debugging, undo/redo
- Cons lists: immutable SLL, O(1) prepend, structural sharing on tail
- Finger trees: O(1) amortized access at both ends, persistent
- Trade-off: more allocations and GC pressure vs safety and simplicity
