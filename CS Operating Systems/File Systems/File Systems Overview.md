---
tags:
  - csos
  - moc
up: "[[CS Operating Systems]]"
---
# File Systems Overview

File systems give persistent, named structure to raw block storage. This domain covers the file abstraction, directory organization, on-disk implementation (inodes, allocation), and crash-consistent journaling.

---

## Learn in This Order

1. [[File System Fundamentals]] — file abstraction; naming; access modes (sequential, random); metadata; open/read/write/close
2. [[Directory Structures]] — flat vs hierarchical vs DAG directories; hard links vs symbolic links; path resolution
3. [[File System Implementation]] — allocation methods (contiguous, linked, indexed); inode structure; free-space management (bitmaps, free lists)
4. [[Journaling File Systems]] — write-ahead logging; atomic transactions; crash consistency; ext3/ext4/NTFS

---

## In This Domain

| Page | One-line summary |
|------|-----------------|
| [[File System Fundamentals]] | File abstraction; metadata; access modes; system call interface |
| [[Directory Structures]] | Hierarchical namespace; links; path resolution |
| [[File System Implementation]] | Inodes; allocation strategies; free-space management |
| [[Journaling File Systems]] | Write-ahead log; crash consistency; journaling modes |

---

## Common Distinctions

| Question | Answer |
|----------|--------|
| Hard link vs soft link? | Hard link = directory entry pointing directly to inode (same file, multiple names). Soft/symbolic link = file containing a path string (can cross file systems, can dangle). |
| Contiguous vs inode allocation? | Contiguous allocation = fast sequential access, fragmentation over time. Inode (indexed) allocation = handles any file size, pointers per inode + indirect blocks. |
| Journaling modes (ordered vs writeback vs data)? | Data journaling logs everything (safest). Ordered (default ext3) journals metadata, writes data first. Writeback journals only metadata (fastest, less safe). |
| Buffer cache vs disk? | Reads/writes go through an in-memory buffer cache; dirty pages are written back asynchronously. Crash before writeback = data loss without journaling. |

---

## How to Navigate

- **First encounter?** [[File System Fundamentals]] → [[Directory Structures]] for the user-visible model, then [[File System Implementation]] for how it actually works on disk.
- **Crash recovery question?** [[Journaling File Systems]] covers write-ahead logging and recovery.

---

## See Also

- [[Disk Scheduling Algorithms]] — file system I/O performance depends on the disk scheduler reordering block requests
- [[Virtual Memory and Paging]] — memory-mapped files (mmap) unify the page cache and file system layers
- [[Access Control]] — file permissions and ACLs are enforced at the file-system level
- [[System Calls]] — open/read/write/close are the system-call interface to the file system

---

## Related Domains

- **[[IO Overview]]** — the I/O subsystem (device drivers, disk scheduling) sits below the file system; file system performance depends heavily on I/O stack efficiency.
- **[[Memory Management Overview]]** — memory-mapped files (mmap) bridge virtual memory and the file system layer.
