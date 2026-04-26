---
id: chunk-csos-178
type: chunk
source: "[[raw-os-032]]"
source_loc: "Copy-on-Write Mechanism"
topic: "memory"
claim: "COW extends beyond fork to Btrfs/ZFS snapshots, KSM memory deduplication across VMs, and MAP_PRIVATE mappings, making it one of the most widely applied OS optimizations"
confidence: verified
supports:
  - "[[Copy-on-Write]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — COW applies to filesystems VMs and private mappings

## Context

Btrfs and ZFS use COW for data blocks: writes allocate new blocks rather than overwriting, enabling instant snapshots by preserving old root pointers. KSM (Kernel Same-page Merging) finds identical pages across VMs via content hashing, merges them with COW protection, and can reduce host memory by 30-50% for similar VMs. MAP_PRIVATE mmap uses COW to create process-local copies of file-backed pages on write.

## Why It Matters

COW is a universal optimization pattern that appears across every layer of the OS. Understanding its breadth explains how snapshots work, why VM consolidation ratios are so high, and why private mmap is safe for shared library loading.

## QnA Seeds

- Q: How do Btrfs and ZFS use COW for instant snapshots?
- Q: What is KSM and how much memory can it save across VMs?
- Q: How does MAP_PRIVATE use COW for shared library data segments?
