---
tags: [cs-algorithms, raw]
source_type: textbook-chapter
source_title: "Skip Lists: A Probabilistic Alternative to Balanced Trees"
authors: [William Pugh]
year: 1990
---

## Summary

A skip list is a probabilistic data structure that provides O(log n) expected time for search, insertion, and deletion, serving as a randomized alternative to deterministic balanced trees like red-black trees and AVL trees. The structure consists of multiple levels of sorted linked lists. The bottom level (level 0) contains all elements. Each higher level contains a random subset of the elements from the level below, with each element independently promoted to the next level with probability p (typically p = 1/2). Search starts at the top level and moves right until the next element exceeds the target, then drops down one level and continues—combining the speed of binary search with the simplicity of linked lists. The expected number of levels is O(log n), and the expected number of comparisons per search is (log n)/log(1/p) + O(1). Insertion generates a random level for the new element by flipping coins (geometric distribution), then inserts the element into all lists from level 0 up to its assigned level. Deletion simply removes the element from all levels. The implementation requires no rotations, recoloring, or complex case analysis—dramatically simpler than balanced tree implementations. Skip lists support efficient range queries by scanning the bottom level after locating the range start. With p = 1/2, the expected space overhead is 2n pointers (each element has on average 2 forward pointers across all levels). Skip lists are used in Redis for sorted sets, LevelDB and RocksDB for in-memory MemTable indexing, and Lucene for term dictionary lookup.

## Key Claims

1. Skip lists achieve O(log n) expected time for search, insert, and delete with high probability, matching balanced BST performance without deterministic balancing mechanisms.
2. The implementation is dramatically simpler than balanced trees: no rotations, no recoloring, no complex case analysis—just linked list operations with randomized level assignment.
3. The expected height of a skip list with n elements and promotion probability p = 1/2 is O(log n), and the probability of exceeding c·log n levels decreases exponentially in c.
4. Skip lists support efficient ordered operations (range queries, rank, successor/predecessor) that hash tables cannot provide, while being simpler to implement than balanced trees.
5. Concurrent skip lists are easier to implement correctly than concurrent balanced trees because insertions and deletions affect only local pointers at each level.

## Atomic Facts

1. A new element's level is determined by a geometric random variable: flip a coin repeatedly, promoting the element each time heads appears, stopping at the first tails.
2. Search examines O(log n) expected elements by traversing O(1/p) expected nodes at each level before descending, across O(log_{1/p} n) levels.
3. The space overhead is n/(1−p) expected total pointers across all levels; with p = 1/2, this is 2n pointers, comparable to a binary tree's 2n child pointers.
4. Deterministic skip lists (1-2 skip lists, 1-2-3 skip lists) eliminate randomization by maintaining explicit level invariants, guaranteeing O(log n) worst-case performance.
5. In Redis, sorted sets (ZSET) use a skip list combined with a hash table: the skip list provides ordered access while the hash table provides O(1) score lookup by member.
6. Lock-free skip list implementations use compare-and-swap (CAS) operations for concurrent modifications, avoiding the complexity of hand-over-hand locking required by balanced trees.

## Significance

Skip lists demonstrate that randomization can replace complex deterministic balancing with a simpler, equally effective mechanism. Introduced by William Pugh in 1990, they offer an attractive alternative when implementation simplicity, concurrency, or cache behavior matter more than worst-case guarantees. Their adoption in production systems like Redis, LevelDB, and RocksDB validates their practical utility. In concurrent programming, skip lists are particularly valuable because their structure allows fine-grained locking or lock-free implementations more naturally than tree rotations. The skip list also serves as an important pedagogical tool, illustrating how randomization achieves expected performance matching deterministic lower bounds.

## Chunks Extracted

chunk-algo-173 through chunk-algo-176
