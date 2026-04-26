---
tags: [cs-os, chunk]
source: "[[raw-os-010]]"
confidence: high
supports:
  - "[[File Systems]]"
qna_seeds:
  - "Q: What is the difference between sequential and direct file access? A: Sequential access reads/writes in order from beginning to end, advancing the file pointer automatically — used by compilers and data processing. Direct (random) access allows reading/writing any block by offset without scanning; databases rely on this to retrieve individual records efficiently."
---

# Sequential vs Direct File Access

Sequential access reads or writes file contents in order from beginning to end, with the file pointer advancing automatically after each operation. This is the dominant access pattern for compilers, text editors, and most data processing programs. Direct (random) access allows reading or writing any block by specifying a byte offset or block number, enabling retrieval of individual records without scanning the entire file. Databases fundamentally depend on direct access for efficient record lookup. The POSIX lseek() call repositions the file pointer, enabling programs to switch between sequential and random access patterns on the same file descriptor.
