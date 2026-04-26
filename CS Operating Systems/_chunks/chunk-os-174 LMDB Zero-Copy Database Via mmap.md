---
id: chunk-csos-174
type: chunk
source: "[[raw-os-031]]"
source_loc: "Memory-Mapped Files"
topic: "memory"
claim: "LMDB maps its entire database file and returns pointers directly into mmap'd pages for zero-copy reads, delegating caching entirely to the OS page cache"
confidence: verified
supports:
  - "[[Memory-Mapped IO]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — LMDB uses mmap for zero-copy database reads

## Context

LMDB (Lightning Memory-Mapped Database) maps the entire database file and uses copy-on-write B+ trees for ACID transactions. Read transactions return pointers directly into mmap'd pages with zero buffer copies. SQLite also offers an mmap mode for read-heavy workloads. However, mmap has limitations: errors arrive as SIGBUS rather than return codes, and the kernel controls page eviction independent of application access patterns.

## Why It Matters

LMDB demonstrates the extreme case of delegating all caching to the OS. Understanding its design explains when mmap-based database architectures excel (read-heavy, memory-fits-in-RAM) and their limitations (no application-level cache control, SIGBUS error handling complexity).

## QnA Seeds

- Q: How does LMDB achieve zero-copy reads?
- Q: What limitation does SIGBUS create for mmap-based databases?
- Q: Why does LMDB delegate caching to the OS rather than managing its own buffer pool?
