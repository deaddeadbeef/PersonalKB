---
id: chunk-csos-025
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 4"
topic: "filesystems"
claim: "Journaling guarantees crash-consistent metadata by writing intended changes to a sequential write-ahead log before applying them to their final locations; on crash, incomplete transactions are discarded or replayed"
confidence: verified
supports:
  - "[[Journaling File Systems]]"
tags:
  - csos
  - csos/filesystems
  - chunk
up: "[[CS Operating Systems]]"
---
# File Systems — Journaling uses write-ahead logging to guarantee crash-consistent metadata

## Context

Before journaling, a crash mid-update could leave the file system in an inconsistent state — an inode claiming more blocks than allocated, a directory entry pointing to a freed inode. Traditional recovery (fsck) scanned the entire disk, taking minutes on large volumes. Journaling writes all metadata changes to a sequential circular log first. After a crash, the OS checks the journal: complete transactions are replayed; incomplete ones are discarded. Recovery is O(journal size) — seconds, not minutes.

## Why It Matters

Journaling is why `ext3/ext4` and NTFS can be unmounted uncleanly (power failure, kernel crash) and remount cleanly in seconds. It is the difference between a reliable production OS and a system where any crash requires manual disk repair. The trade-off (journaling mode: ordered vs data vs writeback) is a real production configuration decision on Linux servers.

## QnA Seeds

- Q: What problem does journaling solve that fsck does not?
- Q: What is the difference between ordered and data journaling modes?
- Q: What happens to a journal transaction that was not completed before a crash?
