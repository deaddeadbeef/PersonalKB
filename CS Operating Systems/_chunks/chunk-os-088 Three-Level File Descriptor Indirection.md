---
tags: [cs-os, chunk]
source: "[[raw-os-010]]"
confidence: high
supports:
  - "[[File Systems]]"
  - "[[Unix Design]]"
qna_seeds:
  - "Q: What are the three levels of file system indirection in Unix? A: The per-process file descriptor table maps FDs to entries in the system-wide open file table (which tracks file position and mode), which in turn points to the system-wide inode/vnode table (actual file metadata). This enables independent file positions per process while sharing underlying kernel structures."
---

# Three-Level File Descriptor Indirection

Unix file systems use a three-level indirection structure: the per-process file descriptor table maps small integer file descriptors to entries in the system-wide open file table, which tracks the current file position and access mode. The open file table entries in turn point to the system-wide inode/vnode table containing the actual on-disk file metadata. This architecture enables independent file positions per process (two processes reading the same file maintain separate offsets) while sharing the underlying kernel metadata structures, and is why dup() and fork() can create multiple descriptors pointing to the same open file table entry.
