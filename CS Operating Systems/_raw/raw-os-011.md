---
tags: [cs-os, raw]
source_type: textbook_chapter
source_title: "File System Implementation"
authors: "Andrew S. Tanenbaum, Herbert Bos"
year: 2015
---

# File System Implementation

## Summary
File system implementation bridges the gap between the user-facing file abstraction and the physical reality of disk blocks. On-disk structures—boot blocks, superblocks, inode tables, and data blocks—organize metadata and content, while allocation methods (contiguous, linked, indexed) determine how file data is mapped to disk blocks. Free space management using bitmaps or linked lists tracks available blocks. The implementation choices directly impact performance, reliability, and maximum file/volume sizes.

## Key Claims
- The superblock is the most critical on-disk structure, containing file system metadata (block size, total blocks, free block count, inode count, and pointers to key structures); corruption of the superblock can render the entire file system unmountable, which is why multiple backup copies are stored
- Contiguous allocation provides excellent read performance and simple implementation but suffers from external fragmentation and requires knowing file size at creation time, making it impractical for general-purpose use
- Linked allocation eliminates external fragmentation by chaining disk blocks via pointers, but random access requires O(n) sequential traversal and a single broken pointer can lose the remainder of the file; FAT improves this by moving pointers into a centralized table
- Indexed allocation (used by Unix/Linux inodes) stores all block pointers in an index structure, supporting both sequential and random access efficiently; multi-level indexing (indirect, double-indirect, triple-indirect blocks) extends maximum file size without wasting space for small files
- Bitmap-based free space management uses one bit per disk block, enabling efficient location of contiguous free regions; the entire bitmap for a 1 TB disk with 4 KB blocks requires only 32 MB of storage

## Atomic Facts
1. A Unix inode contains: file type, permissions, owner/group, size, timestamps (atime, mtime, ctime), link count, and block pointers—typically 12 direct pointers, plus single/double/triple indirect pointers enabling files up to multiple terabytes
2. With 12 direct block pointers, 1 single-indirect, 1 double-indirect, and 1 triple-indirect pointer on a 4 KB block size, a Unix inode can address approximately 4 TB of data: (12 + 1024 + 1024² + 1024³) × 4 KB
3. The boot block occupies the first sector(s) of a partition and contains the bootstrap code needed to load the operating system; it exists even on non-bootable partitions by convention
4. FAT (File Allocation Table), used in MS-DOS and still used for USB drives and SD cards, replaces per-block next pointers with a centralized table—FAT16 supports volumes up to 2 GB, FAT32 up to 2 TB (practically 8 TB with 32 KB clusters)
5. A directory in Unix is simply a file containing a list of (filename, inode number) pairs; the directory file itself has an inode, and directory operations are implemented as reads and writes to this special file
6. Free space management via a linked list of free blocks requires no extra space (free blocks store the pointers themselves) but is slow for finding contiguous free regions; bitmaps trade a small amount of space for dramatically faster allocation of contiguous blocks

## Significance
File system implementation is where abstract data organization meets the physical constraints of storage hardware. The Unix inode design—using direct pointers for small files and multi-level indirection for large files—exemplifies a principle that appears throughout systems design: optimize for the common case (small files) while still supporting the general case (large files) without fundamental redesign.

## Chunks Extracted
*Pending*
