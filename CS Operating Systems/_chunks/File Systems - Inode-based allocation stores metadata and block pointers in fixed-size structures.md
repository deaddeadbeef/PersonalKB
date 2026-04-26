---
id: chunk-csos-024
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 4"
topic: "filesystems"
claim: "Inode-based allocation stores file metadata and up to three levels of block pointer indirection in a fixed-size inode structure, supporting files from bytes to terabytes without wasting space on small files"
confidence: verified
supports:
  - "[[File System Implementation]]"
tags:
  - csos
  - csos/filesystems
  - chunk
up: "[[CS Operating Systems]]"
---
# File Systems — Inode-based allocation stores metadata and block pointers in fixed-size structures

## Context

A Unix inode is a fixed-size (typically 128 or 256 byte) structure on disk. It holds: file type and permissions, link count, owner UID/GID, file size, timestamps, and an array of block pointers. The first 12 are direct (point directly to 4 KiB data blocks). A single-indirect pointer points to a block of 1024 pointers. A double-indirect pointer adds another level. For a 4 KiB block and 4-byte pointers, this supports files up to ~4 TB. Small files (most files) access their data in a single disk read (inode + data block).

## Why It Matters

The inode design is a masterpiece of space efficiency: small files use only direct pointers (fast, minimal overhead); large files pay the indirection cost only for the blocks that need it. This structure directly influenced every Unix-derived file system (ext2/3/4, UFS, HFS+) and is essential knowledge for understanding Linux storage internals and tools like `stat`, `ls -i`, and `debugfs`.

## QnA Seeds

- Q: How many disk accesses does reading the first block of a small file require with an inode system?
- Q: What limits the maximum file size in an inode-based file system?
- Q: What information is NOT stored in an inode?
