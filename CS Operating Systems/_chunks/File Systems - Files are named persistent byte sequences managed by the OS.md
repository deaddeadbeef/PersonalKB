---
id: chunk-csos-022
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 4"
topic: "filesystems"
claim: "A file is the OS abstraction for a named, persistent byte sequence; the OS manages its metadata (size, owner, permissions, timestamps) and exposes a uniform interface regardless of the underlying storage medium"
confidence: verified
supports:
  - "[[File System Fundamentals]]"
tags:
  - csos
  - csos/filesystems
  - chunk
up: "[[CS Operating Systems]]"
---
# File Systems — Files are named persistent byte sequences managed by the OS

## Context

From a program's perspective, a file is just an array of bytes with a name, accessible via `open/read/write/close`. The OS hides everything else: which disk sectors store the data, whether the storage is a spinning disk, an SSD, or a network share. The OS also manages metadata: file length, owner, group, access permissions (Unix mode bits), and timestamps for creation, last modification, and last access.

## Why It Matters

The file abstraction is the primary persistence mechanism for all software. Databases, configuration files, log streams, and inter-process communication via FIFOs all use the file model. The OS's job is to make this abstraction reliable (survive crashes), efficient (fast sequential and random access), and secure (permission enforcement). Every choice in file system design — allocation strategy, journaling, block size — trades off these goals.

## QnA Seeds

- Q: What metadata does the OS maintain about a file beyond its content?
- Q: What is the difference between a hard link and the underlying file?
- Q: How does memory-mapped file access differ from read/write system calls?
