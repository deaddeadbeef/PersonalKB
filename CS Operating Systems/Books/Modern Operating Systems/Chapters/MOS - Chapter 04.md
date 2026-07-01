---
id: mos-ch-04
type: book-chapter
chapter: 4
book: "Modern Operating Systems"
author: "Andrew S. Tanenbaum"
status: seeded
chunk_count: 5
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
tags:
  - csos
  - book-chapter
up: "[[CS Operating Systems/Books/Modern Operating Systems/Chapter Index|Chapter Index]]"
confidence: established
freshness: stable
tier-coverage: [core]
---
# MOS — Chapter 04: File Systems

## Summary

The file system chapter addresses the challenge of making data persist across reboots, process deaths, and hardware failures while presenting a friendly interface to programs. Files are named, typed, byte-sequence abstractions with metadata (size, permissions, timestamps). Directory trees impose hierarchy on flat storage, with hard links and symbolic links enabling non-tree structures. Implementation topics include contiguous, linked, and indexed (inode) allocation; free-space management via bitmaps or free lists; and the full inode structure used in Unix-family systems. The chapter concludes with crash consistency: write-ahead logging (journaling) guarantees that metadata structures remain consistent after a crash even if some writes were partially applied. NFS and distributed file system concepts close the chapter.

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| File | Named, persistent byte sequence with associated metadata |
| Inode | Unix metadata block holding file attributes and block pointers |
| Directory | Special file mapping names to inode numbers |
| Hard link | Second directory entry pointing to same inode; reference counted |
| Journaling | Write-ahead log ensures metadata consistency after crash |
| Free-space bitmap | Bit per block indicating free/allocated; efficient scan |

## Chunk Candidates

- [x] [[File Systems - Files are named persistent byte sequences managed by the OS]]
- [x] [[File Systems - Directory trees impose hierarchy on flat storage via name-to-inode mappings]]
- [x] [[File Systems - Inode-based allocation stores metadata and block pointers in fixed-size structures]]
- [x] [[File Systems - Journaling uses write-ahead logging to guarantee crash-consistent metadata]]
- [x] [[File Systems - Free-space management uses bitmaps or free lists to track available blocks]]

## Wiki Pages Seeded

- [[File System Fundamentals]] — file abstraction, naming, metadata, access modes
- [[Directory Structures]] — hierarchical directories, hard links, symlinks
- [[File System Implementation]] — allocation methods, inodes, free-space management
- [[Journaling File Systems]] — write-ahead logging, crash consistency

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Tanenbaum 2015]].
