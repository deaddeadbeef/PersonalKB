---
tags: [cs-os, raw]
source_type: textbook_topic
source_title: "Log-Structured File Systems"
authors: Rosenblum, Ousterhout; Tanenbaum, Bos
year: 1991
---

# Log-Structured File Systems

## Summary

Log-Structured File Systems (LFS) fundamentally rethink filesystem design by treating the entire disk as an append-only circular log. All writes—data blocks, inodes, directory entries, and metadata—are buffered in memory and written sequentially to the head of the log in large contiguous segments. This design was proposed by Rosenblum and Ousterhout in their 1991 paper, motivated by the observation that as memory sizes grew, read traffic would increasingly be served from the buffer cache, making write performance the dominant bottleneck. By converting all writes to sequential I/O, LFS achieves near-maximum disk bandwidth for writes, avoiding the costly seeks required by traditional file systems that update data and metadata in fixed on-disk locations.

The key challenge for LFS is garbage collection. Because data is never updated in place, old versions of blocks remain scattered throughout the log as "dead" data after files are modified or deleted. A cleaner process must periodically identify segments with high ratios of dead blocks, copy any live blocks to the head of the log, and reclaim the cleaned segments as free space. The efficiency of the cleaner determines LFS's overall performance—aggressive cleaning wastes bandwidth copying live data, while infrequent cleaning leads to space exhaustion. Rosenblum and Ousterhout proposed cost-benefit segment selection policies that preferentially clean segments with the highest dead-to-live ratios and the oldest age, achieving 70–80% disk utilization with acceptable overhead.

Write amplification is the ratio of total physical writes to logical writes requested by applications. LFS incurs write amplification through cleaning: copying live data from partially-dead segments generates additional writes. At high disk utilization (above 80–90%), write amplification increases sharply as the cleaner must process increasingly full segments.

Modern LFS derivatives include F2FS (Flash-Friendly File System), developed by Samsung for NAND flash storage. F2FS adapts LFS principles to the unique characteristics of flash: it aligns writes to flash erase block boundaries, uses multi-head logging to separate hot and cold data (reducing cleaning overhead), and implements adaptive logging that switches between normal and threaded logging modes based on free space availability. F2FS is the default filesystem on many Android devices.

## Key Claims

- Log-structured file systems convert all writes to sequential appends, achieving near-maximum disk write bandwidth by eliminating seek overhead inherent in update-in-place file systems
- Garbage collection is the fundamental challenge: dead blocks accumulate as files are modified, requiring a cleaner to copy live data and reclaim segments, which generates write amplification
- Write amplification increases sharply at high disk utilization because the cleaner must process segments with fewer dead blocks, copying more live data per reclaimed segment
- The cost-benefit segment selection policy from the original LFS paper balances cleaning efficiency by considering both the dead-block ratio and segment age
- F2FS adapts LFS principles for flash storage by aligning writes to erase block boundaries, separating hot and cold data, and using adaptive logging strategies to reduce write amplification

## Atomic Facts

1. The original LFS paper by Rosenblum and Ousterhout (1991, SOSP) demonstrated that LFS could achieve 65–75% of raw disk bandwidth for small-file writes, compared to 5–10% for FFS (Fast File System)
2. An LFS segment is typically 512 KB to several MB and contains a segment summary block that records which inodes and offsets each data block belongs to, enabling the cleaner to identify live blocks
3. Finding inodes in LFS requires an inode map (imap) that maps inode numbers to current log positions, since inodes move with each update; the imap itself is written to the log
4. LFS uses checkpoints (periodically written to a fixed disk location) to record the current log head and imap positions, enabling crash recovery by replaying from the last checkpoint
5. F2FS uses six active log areas (hot/warm/cold for both data and node blocks) to separate data by update frequency, improving cleaner efficiency by concentrating dead blocks in hot segments
6. The write amplification factor for LFS cleaning at utilization u is approximately 2/(1-u) in the worst case, meaning 90% utilization can produce 20x write amplification

## Significance

The log-structured file system represents one of the most influential ideas in storage systems design. While the original disk-based LFS saw limited adoption due to cleaning overhead at high utilization, its principles directly influenced the design of flash storage firmware (FTLs use log-structured writes internally), modern file systems (F2FS, NILFS2), and log-structured merge trees (LSM-trees) used in databases like LevelDB, RocksDB, and Cassandra. Understanding LFS is essential for comprehending how modern storage stacks optimize write performance.

## Chunks Extracted

*Pending*
