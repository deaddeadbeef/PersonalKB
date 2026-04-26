---
tags:
  - csos
  - csos/casestudies
confidence: verified
up: "[[Case Studies Overview]]"
---
# Linux Architecture Overview

Linux is a **monolithic kernel** with loadable modules — all core OS services (scheduling, memory management, VFS, networking, device drivers) run in a single kernel address space. This delivers high performance at the cost of fault isolation: a buggy driver can corrupt kernel state.

---

## Kernel Layers

```
┌─────────────────────────────────────────────┐
│          System Call Interface              │
├──────────┬──────────────┬───────────────────┤
│ Process  │   Memory     │   VFS             │
│ Scheduler│   Manager    │   (Virtual FS)    │
├──────────┴──────────────┴───────────────────┤
│       Network Stack  │  Device Drivers      │
├─────────────────────────────────────────────┤
│            Hardware Abstraction             │
└─────────────────────────────────────────────┘
```

---

## Completely Fair Scheduler (CFS)

Linux's default scheduler uses a **red-black tree** keyed by **virtual runtime** (vruntime) — time the process has run, weighted inversely by priority. The process with the smallest vruntime is always next. This achieves $O(\log n)$ pick-next; provides proportional fairness without discrete time slices.

---

## Virtual File System (VFS)

VFS defines a set of abstract objects (superblock, inode, dentry, file) and operations (lookup, read, write, fsync). Any file system driver that implements this interface plugs into the kernel. A `read()` system call on an ext4 file, a procfs virtual file, and an NFS-mounted file all follow the same VFS path.

---

## Memory Management

- **Buddy system** allocates physical frames in power-of-two blocks; fast merge on free.
- **Slab allocator** manages kernel object caches (inodes, PCBs, socket buffers) to avoid fragmentation from repeated small allocations.
- **Anonymous memory and file-backed pages** are managed through the page cache; pages are evicted using an active/inactive list approximating LRU.

---

## Loadable Kernel Modules

Drivers and file systems can be compiled as `.ko` files and loaded at runtime with `insmod`/`modprobe`. They run in kernel space with full privilege. `lsmod` lists loaded modules; `rmmod` unloads.

---

## Supporting Chunks

- [[Case Studies - Linux uses a monolithic kernel with loadable modules as a performance-reliability compromise]]
- [[Case Studies - The VFS layer lets Linux support heterogeneous file systems behind a uniform interface]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 10.
