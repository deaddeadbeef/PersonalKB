---
tags: [cs-os, chunk]
source: "[[raw-os-010]]"
confidence: high
supports:
  - "[[File Systems]]"
qna_seeds:
  - "Q: What are the six fundamental file operations defined by the OS? A: Create (allocate space/directory entry), open (load metadata, return file descriptor), read (copy from file position to buffer), write (copy from buffer to file position), seek (reposition file pointer), and close (release descriptor, flush buffers). The open() call performs pathname resolution, permission checks, and file descriptor allocation."
---

# File Abstraction Decouples Logic from Storage

A file is the OS's abstraction of persistent, named data — it decouples the logical view of information from physical disk block layout. The six fundamental operations are: create, open, read, write, seek, and close. The open() system call is the critical gateway: it performs pathname resolution, checks permissions, allocates a file descriptor, and loads metadata into kernel memory. Subsequent read/write operations use the lightweight file descriptor rather than repeating pathname resolution, making the open-before-use pattern essential for performance.
