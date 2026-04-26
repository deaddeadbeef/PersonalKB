---
tags: [cs-os, chunk]
source: "[[raw-os-010]]"
confidence: high
supports:
  - "[[File Systems]]"
qna_seeds:
  - "Q: How do hard links differ from symbolic links? A: Hard links create multiple directory entries pointing to the same inode; the file data is deleted only when the link count reaches zero (hence 'unlinking'). Symbolic links are special files containing a pathname the OS follows transparently; they can cross filesystem boundaries but become dangling if the target is deleted."
---

# Hard Links vs Symbolic Links

Hard links in Unix create multiple directory entries pointing to the same inode number. The file's data blocks are only freed when the link count reaches zero, which is why deleting a file is called "unlinking." Hard links cannot cross filesystem boundaries since inode numbers are local to a filesystem. Symbolic (soft) links are special files containing a pathname that the OS transparently follows during pathname resolution. Symbolic links can cross filesystem boundaries and can refer to directories, but they can become dangling if the target is deleted, since the link stores only the path — not a direct reference to the inode.
