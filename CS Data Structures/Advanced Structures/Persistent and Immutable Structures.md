---
tags: [cs-ds, persistent]
up: "[[Advanced Structures Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Persistent and Immutable Structures

> **One-line summary**: Data structures that preserve all previous versions of themselves after modification — partially persistent structures allow querying old versions, while fully persistent structures allow branching modifications from any version.

## 🎯 Intuition
**The Core Idea:** Instead of mutating data in place, every "modification" produces a new version while keeping old versions accessible. This is achieved efficiently through structural sharing — new versions reuse most of the old structure.
**Analogy:** Think of a Git repository: each commit creates a new snapshot, but files that didn't change are shared between commits (not copied). You can check out any past commit, branch from it, and all versions coexist. Persistent data structures work the same way internally.
**Why It Matters:** Functional programming languages, version control, undo/redo systems, database MVCC (multi-version concurrency control), and time-travel debugging all rely on persistent data structures.

---

## ⚙️ Core Mechanics
### How It Works

**Levels of persistence:**
1. **Ephemeral**: traditional mutable structure — only the current version exists.
2. **Partially persistent**: all versions can be read, but only the latest version can be modified.
3. **Fully persistent**: any version can be both read and modified, creating a version tree.
4. **Confluently persistent**: versions can be merged (combining two version histories).

**Path copying (the fundamental technique):**
When modifying a node in a tree, copy only the nodes on the path from root to the modified node. All other nodes are shared with the previous version.

Example — persistent binary search tree insert:
- To insert key K, walk from root to leaf as usual.
- Copy each node on the path (creating new nodes with updated child pointers).
- Nodes not on the path remain shared between old and new versions.
- Cost: $O(\log n)$ new nodes per update (for balanced trees).

**Fat nodes (alternative technique):**
Instead of copying, each node stores a list of (version, value) pairs. Queries specify a version number and read the appropriate value. Space-efficient but queries become slower.

### Key Operations

| Operation | Path Copying | Fat Nodes | Notes |
|-----------|-------------|-----------|-------|
| Query (any version) | $O(\log n)$ | $O(\log n + \log v)$ | v = number of versions |
| Update (latest) | $O(\log n)$ time, $O(\log n)$ space | $O(1)$ space | Path copying copies path |
| Update (any version) | $O(\log n)$ | $O(1)$ amortized | Fully persistent |
| Space per update | $O(\log n)$ | $O(1)$ | Path copying vs. fat nodes |

### Key Facts
- **Structural sharing** is the key to efficiency: a persistent balanced BST with N elements and V versions uses $O(N + V \log N)$ total space, not $O(NV)$.
- **Immutable structures** are a subset: they're never modified at all — you always build new structures. They're inherently thread-safe (no concurrent mutation).
- Persistent structures are automatically **thread-safe for reads**: old versions are never modified, so any thread can read any version without synchronization.
- **Functional languages** use persistent structures as defaults: Clojure's vectors/maps (HAMTs), Haskell's `Data.Map` (balanced BST), Scala's `Vector` (radix-balanced trees).
- Fat nodes achieve $O(1)$ amortized space per update (Driscoll et al., 1989) — optimal.

---

## 🔬 Deep Dive
### Formal Properties
**Driscoll-Sarnak-Sleator-Tarjan (1989):**
Any pointer-based ephemeral data structure with in-degree bounded by a constant can be made partially persistent with:
- $O(1)$ amortized space overhead per modification.
- $O(1)$ time overhead per access (for partial persistence).

For full persistence, the overhead is $O(1)$ amortized space and time per modification, using a combination of fat nodes and node copying.

**Path copying analysis (balanced BST):**
- Each update copies $O(\log n)$ nodes.
- Total space for N inserts: $O(N \log N)$.
- Each version is a full BST sharing structure with neighbors — any version can be queried in $O(\log n)$.

**Hash Array Mapped Trie (HAMT) — Bagwell, 2001:**
- Used in Clojure and Scala for persistent vectors and maps.
- 32-way branching trie with path copying for updates.
- Depth is at most 7 for 32-bit keys (32-way branching → log₃₂).
- Update cost: $O(log₃₂ N)$ ≈ $O(7)$ — effectively constant for practical N.

### Edge Cases and Pitfalls
- **Space leaks**: if old versions are retained but never garbage-collected, memory grows without bound. Functional languages with GC handle this; in C/C++ you must implement reference counting or use an arena.
- **Garbage collection pressure**: persistent structures generate many short-lived intermediate objects, stressing the GC. Use structure-sharing and avoid unnecessary version creation.
- **Confluent persistence is hard**: merging two version histories is fundamentally more complex. The best known general result (Fiat and Kaplan, 2001) has $O(\log \log n)$ overhead per operation.
- **Not always faster**: for single-threaded, mutation-heavy workloads, ephemeral structures with in-place updates are faster due to cache locality and no allocation overhead.
- **Balancing is critical**: persistent unbalanced BSTs degrade to $O(n)$ per operation. Always use balanced variants (red-black, AVL, or weight-balanced).

### Real-World Usage
- **Clojure**: all core data structures (vector, map, set) are persistent using HAMTs and radix-balanced trees. `(assoc m :key val)` returns a new map sharing structure with `m`.
- **Git**: the object store is a persistent data structure — blobs, trees, and commits form an immutable DAG with structural sharing.
- **Database MVCC**: PostgreSQL, MySQL InnoDB, and Oracle use multi-version concurrency control — each transaction sees a consistent snapshot (a "version") of the database.
- **Redux (JavaScript)**: state management in React apps uses immutable state updates, conceptually similar to persistent data structures.
- **Datomic**: an immutable database by Rich Hickey (Clojure creator) where the entire database history is preserved as persistent data.
- **Undo/redo**: text editors and design tools use persistent structures to implement unlimited undo with minimal memory overhead.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What is the difference between partial and full persistence?
2. How much extra space does inserting into a persistent balanced BST require per operation?
3. Why are persistent data structures inherently thread-safe for reads?

### Core Problems
1. **Persistent Stack**: Implement a fully persistent stack using a singly linked list (naturally persistent via structural sharing). Support `push(version, value)` → new version, `pop(version)` → (value, new version), `peek(version)`.
2. **Persistent BST**: Implement a persistent balanced BST (use a treap or red-black tree). Support `insert(version, key)` and `query(version, key)`. Verify that querying old versions returns correct results.

### Challenge
Implement a **persistent segment tree** that supports:
- `update(version, index, value)` → new version
- `query(version, l, r)` → aggregate over range [l, r] in the given version
Use path copying. Given an initial array of N elements and Q updates, analyze total space usage. Apply this to solve the "Kth smallest in a range" problem using persistent merge sort trees.

---

*See also:* [[Red-Black Trees]] · [[Concurrent Data Structures]] · [[Rope Data Structure]] | **CS Algorithms:** [[Functional Programming Patterns]] · [[Version Control Internals]]

## References
-> [[Sources Index]]
