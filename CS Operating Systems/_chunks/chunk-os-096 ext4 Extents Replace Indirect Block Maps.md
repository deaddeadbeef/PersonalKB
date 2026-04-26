---
id: chunk-csos-096
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 4 — ext4 and Linux File Systems"
topic: "file-systems"
claim: "ext4's extent-based allocation replaces ext3's indirect block mapping with contiguous block ranges described as (start block, length) tuples, dramatically reducing metadata overhead for large files"
confidence: verified
supports:
  - "[[File System Implementation]]"
  - "[[Journaling File Systems]]"
tags:
  - csos
  - csos/file-systems
  - chunk
up: "[[CS Operating Systems]]"
---
# File Systems — ext4 extents replace indirect block maps with contiguous range descriptors

## Context

ext3 used indirect block mapping inherited from ext2: for each file, the inode stored direct block pointers plus single, double, and triple indirect blocks to reach further blocks. This meant a 1 GB file required thousands of individual block pointers. ext4 replaced this with extents — each extent descriptor stores a 48-bit starting block number and a 15-bit length, covering up to 128 MB of contiguous space per extent (with 4 KB blocks). An inode holds 4 extents inline; additional extents are stored in a B-tree (extent tree). This reduces metadata overhead by orders of magnitude for large, sequentially-allocated files and improves sequential I/O performance.

## Why It Matters

Extent-based allocation is what made ext4 scalable to modern storage volumes (up to 1 EiB) and file sizes (up to 16 TiB), compared to ext3's 16 TB / 2 TB limits. The design illustrates a broader systems principle: representing contiguous ranges compactly instead of enumerating every unit individually.

## QnA Seeds

- Q: How does an ext4 extent descriptor differ from ext3's indirect block pointers?
- Q: What are the volume and file size limits of ext4 versus ext3?
- Q: Why do extents improve sequential I/O performance?
