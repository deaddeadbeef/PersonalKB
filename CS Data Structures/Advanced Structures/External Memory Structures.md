---
tags: [cs-ds, external-memory]
up: "[[Advanced Structures Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# External Memory Structures

> **One-line summary**: Data structures designed to minimize disk I/O (block transfers) when data exceeds main memory, using the external memory (I/O) model where performance is measured in page transfers rather than CPU operations.

## 🎯 Intuition
**The Core Idea:** When data is too large for RAM, every disk read/write is thousands of times slower than a memory access. External memory structures organize data to maximize useful work per disk block transfer.
**Analogy:** Imagine a librarian who can only carry one box of books at a time between the archive basement and the reading room. A smart librarian groups related books into the same box, fetches boxes in bulk, and sorts the reading list to minimize trips. That's external memory design — minimizing "trips to the basement."
**Why It Matters:** Databases, file systems, search engines, and big-data systems all process data far larger than available RAM. B-trees, LSM-trees, and external sorting are the backbone of every major database engine.

---

## ⚙️ Core Mechanics
### How It Works
The **external memory model** (Aggarwal & Vitter, 1988):
- Data resides on disk in blocks of size `B`.
- Main memory (cache) holds `M/B` blocks.
- The cost metric is the number of **I/O operations** (block transfers), not CPU operations.

**Core structures:**

**B-Tree / B+ Tree:** The canonical external memory search structure.
- Each node fills one disk block, holding `Θ(B)` keys and children.
- Tree height is `O(log_B N)`, so search costs `O(log_B N)` I/Os.
- Range queries cost `O(log_B N + k/B)` I/Os for k results.

**LSM-Tree (Log-Structured Merge Tree):**
- Writes go to an in-memory buffer; when full, flush sorted runs to disk.
- Disk contains multiple levels of sorted runs with exponentially increasing sizes.
- Background compaction merges runs to maintain read performance.
- Write cost: `O((1/B) × (log_(size ratio) (N/M)))` amortized per element.

**External Merge Sort:**
- Phase 1: Load `M` elements into RAM, sort, write as a sorted "run" to disk. Repeat for all `N/M` runs.
- Phase 2: Merge `M/B − 1` runs simultaneously (limited by available memory for input buffers + 1 output buffer).
- If `N/M` runs exceed `M/B − 1`, do multi-pass merging.
- Total I/Os: `O((N/B) × log_(M/B)(N/B))` — this is optimal.

### Key Operations

| Operation | B-Tree I/Os | LSM-Tree I/Os | Notes |
|-----------|-------------|---------------|-------|
| Point lookup | $O(log_B N)$ | $O(L × log_B(N/L)$) worst | L = number of levels; Bloom filters help |
| Insert | $O(log_B N)$ | $O((1/B)$ log(N/M)) amort. | LSM far cheaper for writes |
| Range query (k) | $O(log_B N + k/B)$ | $O(L × (log_B N + k/B)$) | B-tree superior for reads |
| Sort N elements | — | — | $O((N/B)$ log_(M/B)(N/B)) |
| Scan N elements | $O(N/B)$ | $O(N/B)$ | Sequential I/O |

### Key Facts
- **B-trees dominate reads**, LSM-trees dominate writes — this is the fundamental read-write tradeoff in external memory.
- Block size `B` is typically 4 KB (SSD page) to 64 KB (HDD optimal transfer).
- The branching factor of a B-tree is `Θ(B)`, giving logarithmic base B — very shallow trees even for billions of keys.
- **SSDs change the equation**: random reads are much cheaper on SSDs, reducing B-tree's I/O cost. But sequential write advantage of LSM-trees remains because of SSD write amplification.
- Buffer trees combine B-tree structure with message buffering — each node has a buffer that batches updates before pushing them down.

---

## 🔬 Deep Dive
### Formal Properties
**I/O lower bounds (Aggarwal-Vitter):**
- Sorting: `Ω((N/B) log_(M/B)(N/B))` — no comparison-based algorithm can do better.
- Searching: `Ω(log_B N)` — B-tree is optimal.
- Scanning: `Θ(N/B)` — trivially optimal.

**Write optimization spectrum:**
From B-tree to LSM-tree, there's a smooth tradeoff parameterized by "write amplification":
- B-tree write amplification: `O(log_B N)` (each insert touches one node per level).
- Leveled LSM write amplification: `O(size_ratio × L)` where L ≈ `log_(size_ratio)(N/M)`.
- Tiered LSM (e.g., Universal compaction): lower write amplification but worse read performance.

**Bε-tree (Brodal-Fagerberg):**
A generalization: each node has a buffer of size `B^ε` for some `0 < ε ≤ 1`. Inserts cost `O((1/(εB^(1−ε))) × log_B N)`. Setting ε=1 gives a B-tree; ε→0 approaches LSM behavior.

### Edge Cases and Pitfalls
- **Write amplification**: LSM-trees suffer from compaction overhead — RocksDB's leveled compaction can amplify writes by 10-30×. Tune level-size ratio and compaction strategy carefully.
- **Space amplification**: tiered LSM compaction can temporarily use 2× disk space during compaction. Size-tiered compaction in Cassandra is notorious for this.
- **Read amplification**: without Bloom filters, an LSM-tree read may probe every level. Bloom filters add memory cost but make point reads feasible.
- **B-tree fragmentation**: after many random inserts/deletes, B-tree leaf pages become ~69% full on average (natural fill factor), wasting space.
- **SSD wear leveling**: high write amplification from LSM compaction accelerates SSD wear. Consider using compaction-free structures (e.g., Bw-tree) for SSD-optimized databases.

### Real-World Usage
- **B-trees**: PostgreSQL, MySQL InnoDB, SQLite, every traditional RDBMS. Also used in file systems (NTFS, ext4 extent trees, Btrfs).
- **LSM-trees**: RocksDB (Facebook), LevelDB (Google), Cassandra, HBase, CockroachDB, TiKV. The dominant write-optimized store.
- **Bε-trees**: TokuDB/TokuMX (Percona) used fractal tree indexes (a Bε-tree variant) for write-heavy MySQL workloads.
- **External sorting**: used in every MapReduce/Spark shuffle phase. Hadoop's TeraSort benchmark is essentially optimized external merge sort.
- **Buffer trees**: used in computational geometry for batched point location and range searching in GIS databases.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why is a B-tree with branching factor B better than a binary search tree for on-disk data?
2. In the external memory model, how many I/Os does it cost to scan an array of N elements stored contiguously on disk with block size B?
3. Why do LSM-trees have better write performance than B-trees?

### Core Problems
1. **External Merge Sort**: Implement a two-phase external merge sort. Phase 1: create sorted runs of size M. Phase 2: k-way merge using a min-heap. Measure actual I/O count versus the theoretical `O((N/B) log_(M/B)(N/B))`.
2. **B+ Tree Implementation**: Build a disk-backed B+ tree that stores nodes as fixed-size pages. Implement insert, point lookup, and range scan. Test with 10M random keys.

### Challenge
Design and implement an **LSM-tree storage engine** with: (a) an in-memory AVL/red-black tree memtable, (b) sorted string table (SSTable) files on disk, (c) a compaction thread that merges overlapping SSTables, and (d) Bloom filters for each SSTable. Benchmark read/write throughput and measure write amplification.

---

*See also:* [[B-Trees and B-Plus Trees]] · [[Cache-Oblivious Structures]] · [[LRU and LFU Caches]] | **CS Algorithms:** [[CS Algorithms/Sorting/External Sorting|External Sorting]] · [[CS Operating Systems/IO/Disk Scheduling Algorithms|Disk-Based Algorithms]]

## Supporting Chunks
- [[chunk-ds-009 B-trees minimize disk IO by matching node size to pages]]
- [[chunk-ds-055 LSM trees trade read performance for write throughput]]
- [[chunk-ds-056 Bloom filters in LSM avoid 90pct unnecessary reads]]

## References
- [[CS Data Structures/Sources/Sources Index|Sources Index]]
