---
tags: [cs-ds, raw]
id: raw-ds-022
source: "Various (cache-oblivious algorithms literature)"
up: "[[CS Data Structures]]"
---

# Cache-Oblivious Data Structures

## Key Ideas
- Memory hierarchy: L1, L2, L3, DRAM, SSD, HDD with 10-1000x gaps
- Cache-aware: tuned to specific cache parameters B and M
- Cache-oblivious: optimal for ALL cache levels without knowing parameters
- Van Emde Boas layout: recursive tree layout achieving O(log_B n) search
- Cache-oblivious B-tree: matches B-tree IO complexity without knowing B
- Scanning: sequential access is O(n/B) cache transfers
- Funnel sort: cache-oblivious merge sort with optimal transfer count
- Practical impact: B-tree with page size tuning still beats cache-oblivious in most workloads
