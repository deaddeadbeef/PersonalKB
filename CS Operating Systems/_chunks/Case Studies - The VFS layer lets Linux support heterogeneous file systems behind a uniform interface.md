---
id: chunk-csos-049
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 10"
topic: "casestudies"
claim: "Linux's VFS (Virtual File System) layer defines abstract operations (lookup, read, write) that any file system driver must implement, enabling ext4, tmpfs, procfs, and NFS to coexist behind a uniform open/read/write interface"
confidence: verified
supports:
  - "[[Linux Architecture Overview]]"
  - "[[File System Implementation]]"
tags:
  - csos
  - csos/casestudies
  - chunk
up: "[[CS Operating Systems]]"
---
# Case Studies — The VFS layer lets Linux support heterogeneous file systems behind a uniform interface

## Context

VFS defines four abstract object types (superblock, inode, dentry, file) each with an operation table of function pointers. An ext4 driver, an NFS driver, and a procfs driver each fill in these tables differently. When a user calls `read(fd, ...)`, VFS dispatches to `file->f_op->read` — which might call ext4's block-reading code or NFS's RPC. The dentry cache (dcache) accelerates path lookups; the inode cache holds recently used inode objects. This is the cleanest example of the mechanism-vs-policy principle in the Linux kernel.

## Why It Matters

VFS is why the UNIX "everything is a file" philosophy works in practice. `/proc/cpuinfo` is a file that procfs generates on-the-fly; `/dev/null` is a device file that discards writes; a tmpfs file lives entirely in RAM. All are accessed with identical system calls. Programmers never need to know which file system type they're talking to — VFS provides the abstraction layer.

## QnA Seeds

- Q: What are the four VFS object types in Linux?
- Q: How does VFS enable the "everything is a file" philosophy?
- Q: What caches does VFS maintain and what do they speed up?
