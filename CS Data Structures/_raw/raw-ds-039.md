---
tags: [cs-ds, raw]
id: raw-ds-039
source: "Various (LSM literature, O'Neil et al. 1996)"
up: "[[CS Data Structures]]"
---

# LSM Trees and Write-Optimized Structures

## Key Ideas
- Log-Structured Merge Tree: optimized for write-heavy workloads
- Write path: buffer in memory (memtable), flush to sorted disk runs (SSTables)
- Memtable: typically a balanced BST or skip list (e.g., Red-Black tree in LevelDB)
- SSTable: sorted, immutable file with index block for binary search
- Compaction: merge overlapping SSTables to reduce read amplification
- Leveled compaction (LevelDB/RocksDB): L0 → L1 → ... each level 10x larger
- Size-tiered compaction (Cassandra): merge similarly-sized SSTables
- Write amplification: total bytes written / user bytes — leveled ~10-30x
- Read amplification: may check multiple levels — mitigated by Bloom filters per SSTable
- Space amplification: leveled ~1.1x, size-tiered up to 2x during compaction
- Bloom filters critical: avoid reading SSTables that don't contain the key
- WiscKey: separate keys and values — keys in LSM, values in log — reduces write amp

## Ecosystem
- LevelDB, RocksDB, Cassandra, HBase, CockroachDB, TiKV all use LSM trees
- B-trees dominate read-heavy (OLTP); LSM trees dominate write-heavy (logging, time-series)
