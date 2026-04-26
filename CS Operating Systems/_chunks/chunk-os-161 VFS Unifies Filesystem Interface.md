---
id: chunk-csos-161
type: chunk
source: "[[raw-os-028]]"
source_loc: "Linux Kernel Architecture"
topic: "case-studies"
claim: "VFS decouples the system call interface from filesystem implementation by defining abstract operation structs (inode_operations, file_operations) that each filesystem implements"
confidence: verified
supports:
  - "[[Linux Kernel]]"
tags:
  - csos
  - csos/case-studies
  - chunk
up: "[[CS Operating Systems]]"
---
# Case Studies — VFS unifies filesystem interface via operation structs

## Context

The Virtual File System provides a unified open/read/write/close interface across all filesystem types (ext4, XFS, Btrfs, NFS). VFS defines four key structures: super_block (filesystem instance), inode (file metadata), dentry (directory entry cache), and file (open file instance). Each filesystem implements these operation structs, allowing transparent mounting of any filesystem.

## Why It Matters

VFS is why `cat /etc/passwd` works identically whether the file is on ext4, NFS, or a FUSE filesystem. Understanding VFS explains Linux's remarkable filesystem diversity and how new filesystems can be added without modifying user-space programs.

## QnA Seeds

- Q: What are the four key VFS structures and what does each represent?
- Q: How does VFS enable transparent support for multiple filesystem types?
- Q: What operation structs must a new filesystem implement for VFS?
