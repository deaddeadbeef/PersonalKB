---
tags: [cs-os, chunk]
source: "[[raw-os-011]]"
confidence: high
supports:
  - "[[File System Implementation]]"
qna_seeds:
  - "Q: How does the Unix inode support both small and large files efficiently? A: An inode has 12 direct block pointers (fast access for small files) plus single, double, and triple indirect pointers for large files. With 4 KB blocks, this addresses ~4 TB: (12 + 1024 + 1024² + 1024³) × 4 KB, optimizing for the common case (small files) while supporting the general case."
---

# Indexed Allocation via Unix Inodes

Indexed allocation, used by Unix/Linux inodes, stores all block pointers in an index structure supporting both sequential and random access. A Unix inode contains file type, permissions, owner/group, size, timestamps (atime, mtime, ctime), link count, and block pointers — typically 12 direct pointers plus single, double, and triple indirect pointers. This multi-level indexing wastes no space for small files (served entirely by direct pointers) while extending maximum file size to approximately 4 TB with 4 KB blocks: (12 + 1024 + 1024² + 1024³) × 4 KB.
