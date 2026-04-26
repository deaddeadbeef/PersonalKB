---
tags: [cs-os, chunk]
source: "[[raw-os-011]]"
confidence: high
supports:
  - "[[File System Implementation]]"
qna_seeds:
  - "Q: How do bitmap and linked-list free space management compare? A: Bitmaps use one bit per block (32 MB for a 1 TB disk with 4 KB blocks), enabling efficient location of contiguous free regions. Linked lists of free blocks require no extra space (free blocks store the pointers) but are slow for finding contiguous regions. Bitmaps trade minimal space for dramatically faster contiguous allocation."
---

# Bitmap vs Linked List Free Space Management

Free space management tracks available disk blocks using two primary approaches. Bitmap allocation uses one bit per disk block — the entire bitmap for a 1 TB disk with 4 KB blocks requires only 32 MB — enabling efficient location of contiguous free regions through bit-scanning operations. Linked-list management threads free blocks into a list where each free block stores a pointer to the next, requiring no extra space but making contiguous allocation slow since it requires traversing the list. In practice, bitmaps are strongly preferred because they trade a small, predictable amount of space for dramatically faster allocation of contiguous block runs.
