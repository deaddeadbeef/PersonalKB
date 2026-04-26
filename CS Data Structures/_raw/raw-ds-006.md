---
tags: [cs-ds, raw]
source_type: textbook_chapter
source_title: "B-Trees and Database Indexing"
authors: [Jeff Erickson]
year: 2019
up: "[[Sources Index]]"
---

# B-Trees and Database Indexing

## Summary

B-trees are balanced multi-way search trees minimizing disk I/O by matching node size to disk pages. All leaves at same depth gives O(log_m n) height. B+ trees store data only in leaves with a leaf linked list for range queries. Dominant index structure in databases and file systems.

## Key Claims

1. B-trees minimize disk I/O by matching node size to disk page size
2. All leaves at same depth guarantees O(log_m n) height
3. B+ trees optimize range queries via leaf linked list
4. Order 1000 can index billions of records in 3-4 levels
5. Split and merge maintain balance during insert and delete

## Atomic Facts

1. Typical order: 100-1000 for disk-based systems
2. Node occupancy: at least ceil(m/2) children except root
3. B+ leaf linked list enables O(k) range queries after O(log n) seek
4. Used in MySQL InnoDB, PostgreSQL, SQLite, NTFS, ext4
5. Invented by Bayer and McCreight at Boeing, 1970
6. B+ tree is the standard for database indexes

## Significance

B-trees bridge the gap between in-memory data structures and disk-based storage, making efficient database indexing possible.

## Chunks Extracted

*Pending*
