---
id: chunk-csos-183
type: chunk
source: "[[raw-os-034]]"
source_loc: "Log-Structured File Systems"
topic: "file-systems"
claim: "Log-structured file systems convert all writes to sequential appends in large contiguous segments, achieving near-maximum disk write bandwidth by eliminating seek overhead"
confidence: verified
supports:
  - "[[Log-Structured File Systems]]"
tags:
  - csos
  - csos/file-systems
  - chunk
up: "[[CS Operating Systems]]"
---
# File Systems — LFS converts all writes to sequential appends

## Context

Rosenblum and Ousterhout (1991) observed that growing memory sizes would let buffer caches absorb most reads, making write performance the bottleneck. LFS buffers all writes (data, inodes, directories, metadata) and writes them sequentially to the log head in large segments. This achieved 65-75% of raw disk bandwidth for small-file writes versus 5-10% for FFS (Fast File System).

## Why It Matters

LFS's insight — that sequential I/O is fundamentally faster than random I/O on disks — influenced flash firmware (FTLs use log-structured writes internally), modern file systems (F2FS), and LSM-tree databases (LevelDB, RocksDB, Cassandra). It remains one of the most influential ideas in storage systems.

## QnA Seeds

- Q: Why does LFS write everything sequentially rather than in-place?
- Q: What performance advantage did LFS show over FFS for small-file writes?
- Q: What observation about memory growth motivated the LFS design?
