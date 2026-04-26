---
tags: [cs-os, chunk]
source: "[[raw-os-011]]"
confidence: high
supports:
  - "[[File System Implementation]]"
qna_seeds:
  - "Q: What are the tradeoffs between contiguous, linked, and indexed file allocation? A: Contiguous gives excellent read performance but suffers external fragmentation. Linked eliminates fragmentation but requires O(n) traversal for random access. FAT improves linked by centralizing pointers. Indexed (inodes) supports both access patterns efficiently via multi-level indirection."
---

# Contiguous vs Linked vs Indexed Allocation

Three disk block allocation methods offer distinct tradeoffs. Contiguous allocation provides excellent sequential read performance and simple implementation but suffers external fragmentation and requires knowing file size at creation. Linked allocation chains blocks via embedded pointers, eliminating fragmentation, but random access costs O(n) and a broken pointer loses the rest of the file; FAT (File Allocation Table) improves this by centralizing pointers in a separate table. Indexed allocation (Unix inodes) stores all block pointers in an index structure, supporting efficient sequential and random access through multi-level indirection without fragmentation.
