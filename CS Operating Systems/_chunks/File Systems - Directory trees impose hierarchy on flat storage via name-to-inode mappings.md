---
id: chunk-csos-023
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 4"
topic: "filesystems"
claim: "Directory trees impose hierarchy on flat storage by mapping human-readable names to inode numbers; hard links allow multiple names for the same inode while symlinks are independent path references"
confidence: verified
supports:
  - "[[Directory Structures]]"
  - "[[File System Fundamentals]]"
tags:
  - csos
  - csos/filesystems
  - chunk
up: "[[CS Operating Systems]]"
---
# File Systems — Directory trees impose hierarchy on flat storage via name-to-inode mappings

## Context

On disk, files are just numbered inodes. Directories are special files that record (name → inode number) pairs, creating the navigable tree users see. A hard link is simply a second directory entry pointing to the same inode; the inode's link count tracks how many entries refer to it and the inode is freed only when the count reaches zero. A symbolic link is a small file containing a path string; it is followed by the OS on every access and can point to directories and across file systems.

## Why It Matters

The directory-tree model is universal across UNIX, Windows, and mobile OSes. Understanding the distinction between directory entries, inodes, and data blocks is essential for diagnosing file system problems, implementing backup strategies, and understanding copy-on-write file systems like ZFS and Btrfs. The inode reference count model directly explains why `rm` in UNIX is technically `unlink` — it removes a name, not necessarily the file.

## QnA Seeds

- Q: What does `rm` in UNIX actually do?
- Q: What happens to a file's data when a hard link is deleted but another hard link to the same inode remains?
- Q: Can a symbolic link point to a directory? A hard link?
