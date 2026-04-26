---
id: chunk-csos-026
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 4"
topic: "filesystems"
claim: "Free-space management uses a bitmap (one bit per block) or free list (chained block pointers) to track available disk blocks; bitmaps are compact and support fast contiguous-run searches"
confidence: verified
supports:
  - "[[File System Implementation]]"
tags:
  - csos
  - csos/filesystems
  - chunk
up: "[[CS Operating Systems]]"
---
# File Systems — Free-space management uses bitmaps or free lists to track available blocks

## Context

Every block-allocation decision requires knowing which blocks are free. A bitmap stores one bit per block: 0 = free, 1 = allocated. For a 1 TB disk with 4 KiB blocks, the bitmap is 32 MiB — small enough to keep in memory. Finding N contiguous free blocks means scanning for N consecutive 0-bits, efficient with SIMD instructions. A free list chains free blocks together by storing the next-free-block pointer inside the free block itself, requiring no extra storage but making contiguous-allocation searches O(n).

## Why It Matters

Ext2/ext3/ext4 use per-block-group bitmaps (one per inode, one per block), keeping the bitmap close to the data it tracks for locality. Understanding free-space management explains why file systems prefer "block groups" and why fragmentation occurs over time as files are created and deleted.

## QnA Seeds

- Q: How large is the block bitmap for a 1 TiB disk with 4 KiB blocks?
- Q: What advantage does a bitmap have over a free list for contiguous allocation?
- Q: Where does a free list store its pointers?
