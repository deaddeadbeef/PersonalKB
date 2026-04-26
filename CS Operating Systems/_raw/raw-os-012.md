---
tags: [cs-os, raw]
source_type: textbook_chapter
source_title: "ext4 and Linux File Systems"
authors: "Andrew S. Tanenbaum, Herbert Bos"
year: 2015
---

# ext4 and Linux File Systems

## Summary
The ext family of file systems has been the default Linux file system for over two decades, evolving from ext2's simple block-mapped design through ext3's addition of journaling to ext4's extent-based allocation and scalability improvements. Journaling (write-ahead logging) ensures file system consistency after crashes by recording intended changes before committing them to disk. Modern alternatives like Btrfs and XFS offer advanced features such as copy-on-write snapshots, checksumming, and superior large-file performance.

## Key Claims
- Journaling is the single most important reliability feature in modern file systems—it replaces the slow, incomplete fsck (file system check) recovery process with fast journal replay that restores consistency in seconds regardless of file system size
- ext4's extent-based allocation replaces ext3's indirect block mapping with contiguous block ranges described as (start block, length) tuples, dramatically reducing metadata overhead for large files and improving sequential I/O performance
- Delayed allocation (allocate-on-flush) defers physical block allocation until data is actually written to disk, enabling the allocator to see the full size of pending writes and make better contiguous allocation decisions
- ext4 maintains backward compatibility with ext3/ext2 (an ext3 volume can be mounted as ext4 without reformatting), which contributed to its widespread adoption but also limits how aggressively it can change on-disk structures
- Btrfs and ZFS offer copy-on-write semantics that enable atomic snapshots, built-in checksumming for data integrity verification, and integrated volume management—features that ext4 cannot add without fundamental redesign

## Atomic Facts
1. ext2 (1993) introduced the basic ext structure: block groups each containing a superblock copy, block bitmap, inode bitmap, inode table, and data blocks; it had no journaling and required full fsck after unclean shutdown, which could take hours on large volumes
2. ext3 (2001) added three journaling modes: journal (both metadata and data logged—safest but slowest), ordered (only metadata logged, but data written before metadata commit—the default), and writeback (only metadata logged, data may lag—fastest but risks stale data exposure)
3. An ext4 extent descriptor stores a 48-bit starting block number and a 15-bit length, covering up to 128 MB of contiguous space per extent (with 4 KB blocks); an inode can hold 4 extents inline, with additional extents stored in an extent tree
4. ext4 supports volumes up to 1 exbibyte (2^60 bytes) and individual files up to 16 tebibytes (2^44 bytes), compared to ext3's limits of 16 TB volume and 2 TB file size
5. XFS (originally from SGI IRIX, ported to Linux in 2001) uses B+ trees for directory indexing and free space management, excelling at parallel I/O on large files; it is the default file system on RHEL/CentOS since version 7
6. Btrfs implements copy-on-write for all data and metadata: a write never overwrites existing blocks but instead writes new blocks and atomically updates pointers, enabling instant snapshots as lightweight reference copies that share unmodified blocks

## Significance
The evolution from ext2 to ext4 mirrors the broader story of systems software: each generation addressed the most pressing limitation of its predecessor (reliability via journaling, scalability via extents) while maintaining compatibility with the installed base. The ongoing competition between ext4, XFS, and Btrfs illustrates that no single file system design optimally serves all workloads—databases, media streaming, and container storage each have different access patterns and reliability requirements.

## Chunks Extracted
- [[chunk-os-095 Journaling Replaces fsck With Fast Log Replay]]
- [[chunk-os-096 ext4 Extents Replace Indirect Block Maps]]
- [[chunk-os-097 Delayed Allocation Defers Block Assignment Until Flush]]
- [[chunk-os-098 Btrfs Copy-on-Write Enables Atomic Snapshots]]
