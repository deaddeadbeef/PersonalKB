---
tags: [cs-algorithms, raw]
source_type: textbook-chapter
source_title: "B-Trees and External Memory Data Structures"
authors: [Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein]
year: 2022
---

## Summary

B-trees are balanced search trees designed for systems where data resides on disk rather than in RAM. A B-tree of minimum degree t (order m = 2t) maintains the invariant that every non-root internal node has between t and 2t children, all leaves reside at the same depth, and keys within each node are sorted. This design minimizes disk I/O: with branching factor in the thousands, a B-tree storing billions of keys requires only 3–4 levels, meaning any search touches at most 3–4 disk pages. Operations (search, insert, delete) run in O(log_t n) disk accesses and O(t · log_t n) CPU time. Insertion uses a proactive splitting strategy: as the search descends, any full node (2t−1 keys) is split before entering it, guaranteeing space for the new key without backtracking. Deletion similarly performs proactive merging or key rotation to maintain the minimum key invariant. B+ trees, a practical variant, store all data records in the leaves and maintain only keys in internal nodes. Leaves are linked in a doubly-linked list, enabling efficient range queries by sequential leaf traversal. B+ trees are the dominant index structure in relational databases (MySQL InnoDB, PostgreSQL) and file systems (NTFS, HFS+, ext4). The choice of node size typically matches the disk page size (4–16 KB), balancing the cost of reading a node against the branching factor.

## Key Claims

1. B-trees achieve O(log_t n) disk accesses per operation by maintaining high branching factor t, keeping tree height extremely low even for billions of keys.
2. All leaves at the same depth guarantees worst-case balanced performance, unlike binary search trees which can degrade without balancing.
3. Proactive splitting during insertion (top-down) avoids the need for backtracking up the tree, enabling single-pass insertion with at most O(log_t n) splits.
4. B+ trees improve range query performance by storing all records in leaves connected by sibling pointers, enabling sequential access without tree traversal.
5. Node size is tuned to match disk page size, minimizing I/O operations since each node read or write corresponds to exactly one disk access.

## Atomic Facts

1. A B-tree of minimum degree t has nodes with between t−1 and 2t−1 keys (except the root, which may have as few as 1 key).
2. For t = 1001, a tree of height 2 can store over 1 billion keys, requiring at most 3 disk accesses for any search.
3. Splitting a full node (2t−1 keys) promotes the median key to the parent and creates two nodes of t−1 keys each.
4. B+ tree internal nodes contain only keys and child pointers (no data), maximizing the branching factor per node.
5. B+ tree leaves form a linked list, enabling range queries like "all keys between 50 and 100" by scanning consecutive leaf nodes.
6. The I/O model of computation counts disk block transfers rather than CPU operations, making B-tree analysis fundamentally different from RAM-model analysis.

## Significance

B-trees and their variants are arguably the most important data structure in systems programming. Every major relational database uses B+ tree indexes, and most modern file systems use B-tree variants for metadata storage. The design principle—optimize for the disk access pattern rather than CPU operations—illustrates how hardware constraints shape algorithm design. Understanding B-trees is essential for database internals, file system design, and any system dealing with data sets larger than available RAM. LSM-trees (Log-Structured Merge trees) in modern key-value stores (LevelDB, RocksDB) represent an alternative philosophy optimized for write-heavy workloads.

## Chunks Extracted

*Pending*
