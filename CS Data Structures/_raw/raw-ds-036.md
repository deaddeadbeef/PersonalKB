---
tags: [cs-ds, raw]
id: raw-ds-036
source: "Various (Pagh & Rodler 2004)"
up: "[[CS Data Structures]]"
---

# Cuckoo Hashing Deep Dive

## Key Ideas
- Two hash functions h1 and h2, two tables T1 and T2
- Lookup: check T1[h1(k)] and T2[h2(k)] — worst-case O(1)
- Insert: place in T1[h1(k)]; if occupied, evict occupant to its alternative table
- Eviction chain: displaced element goes to its other table, may displace another
- Cycle detection: if chain exceeds threshold (6 log n), rehash with new functions
- Expected amortized O(1) insert with load factor < 50% (per table)
- Bucketized cuckoo: b slots per bucket — supports ~95% load factor with b=4
- Cuckoo filter: approximate membership (like Bloom) using cuckoo hashing — supports deletion
- d-ary cuckoo hashing: d hash functions, d tables — higher load factors
- Memory efficiency: no pointers, no chains — just flat arrays

## Practical Use
- MemC3 (memcached optimization): uses cuckoo hashing for space efficiency
- Network hardware: TCAM replacement in routers — O(1) worst-case lookup critical
- Cuckoo filters: used in RocksDB, networking, deduplication
