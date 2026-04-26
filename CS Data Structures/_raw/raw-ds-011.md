---
tags: [cs-ds, raw]
source_type: textbook_chapter
source_title: "Skip Lists"
authors: [Pat Morin]
year: 2013
up: "[[Sources Index]]"
---

# Skip Lists — Randomized Search Structure

## Summary

Skip lists are layered linked lists where each element is promoted to higher layers with probability 1/2. Expected O(log n) search/insert/delete. O(n) expected space. Simpler than balanced BSTs with natural concurrent access support. Used in Redis and LevelDB.

## Key Claims

1. Skip lists achieve O(log n) expected time for all operations
2. Promotion probability 1/2 gives expected O(log n) levels
3. Simpler to implement than balanced BSTs
4. Concurrent skip lists are easier than concurrent balanced trees
5. Lock-free implementations exist with practical performance

## Atomic Facts

1. Expected height: O(log n) levels
2. Expected space: O(n) total nodes (2n with p=1/2)
3. Pugh, 1990: Skip Lists: A Probabilistic Alternative to Balanced Trees
4. Redis sorted sets: implemented as skip lists
5. LevelDB/RocksDB MemTable: skip list
6. Java ConcurrentSkipListMap: lock-free concurrent sorted map

## Significance

Skip lists demonstrate that randomization can replace complex deterministic balancing while providing practical advantages for concurrent systems.

## Chunks Extracted

*Pending*
