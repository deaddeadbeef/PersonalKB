---
id: chunk-csos-098
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 4 — ext4 and Linux File Systems"
topic: "file-systems"
claim: "Btrfs and ZFS use copy-on-write semantics where writes never overwrite existing blocks, enabling atomic snapshots, built-in checksumming, and integrated volume management — features ext4 cannot add without fundamental redesign"
confidence: verified
supports:
  - "[[File System Implementation]]"
  - "[[File Systems Overview]]"
tags:
  - csos
  - csos/file-systems
  - chunk
up: "[[CS Operating Systems]]"
---
# File Systems — Btrfs copy-on-write enables atomic snapshots and checksumming

## Context

Btrfs implements copy-on-write for all data and metadata: a write never overwrites existing blocks but instead writes new blocks and atomically updates pointers. This makes snapshots essentially free — a snapshot is a lightweight reference copy that shares all unmodified blocks with the original. Because old blocks are preserved until explicitly reclaimed, the file system can also checksum every block for data integrity verification and detect silent corruption (bit rot). ZFS follows the same philosophy. ext4's in-place update model fundamentally precludes these features.

## Why It Matters

Copy-on-write file systems represent a different design philosophy from the ext lineage: they trade slightly higher write amplification for atomic operations, built-in data integrity, and snapshot capability. This tradeoff is particularly valuable for container storage (Docker uses Btrfs/overlay), databases, and backup workflows where point-in-time consistency is critical.

## QnA Seeds

- Q: How does copy-on-write make snapshots essentially free?
- Q: Why can't ext4 add snapshot support without a fundamental redesign?
- Q: What is the write amplification tradeoff of copy-on-write file systems?
