---
tags: [cs-os, raw]
source_type: textbook_topic
source_title: "Linux Kernel Architecture"
authors: Love; Tanenbaum, Bos
year: 2010
---

# Linux Kernel Architecture

## Summary

Linux is a monolithic kernel with loadable module support, meaning all core OS services—process scheduling, memory management, file systems, networking, and device drivers—run in a single address space in kernel mode. Unlike microkernels, there are no user-space servers for core services, which eliminates IPC overhead for operations like file I/O. However, loadable kernel modules (LKMs) allow device drivers and filesystem implementations to be compiled separately and inserted at runtime via `insmod`/`modprobe`, providing some of the extensibility benefits of a modular architecture without the performance penalty of message passing.

The Linux kernel comprises several major subsystems. The **process scheduler** implements the Completely Fair Scheduler (CFS), which uses a red-black tree to track per-task virtual runtime, ensuring CPU time is distributed proportionally. Real-time tasks use SCHED_FIFO or SCHED_RR policies with static priorities above the CFS range. The **memory manager** handles virtual memory (demand paging, COW), the buddy allocator for physical page frames, SLUB for slab allocation, and the OOM (Out-of-Memory) killer that terminates processes when memory is critically low. The **Virtual File System (VFS)** provides a unified interface (open, read, write, close) across all filesystem types (ext4, XFS, Btrfs, NFS) by defining abstract operations (inode_operations, file_operations, super_operations) that each filesystem implements.

The **network stack** implements the TCP/IP protocol suite with a socket-based interface. The **device driver** subsystem accounts for the majority of kernel code—over 60% of the kernel source tree is drivers. The `/proc` virtual filesystem exposes process and kernel information as readable files (e.g., `/proc/cpuinfo`, `/proc/meminfo`, `/proc/[pid]/maps`). The `/sys` filesystem (sysfs) exports the kernel's device model, representing devices, drivers, and buses as a hierarchical directory structure.

Kernel compilation is configured via `make menuconfig` or `make defconfig`, producing a `.config` file that enables or disables thousands of options. The kernel build system (Kbuild) produces `vmlinuz` (compressed kernel image) and optional modules. The kernel is versioned as major.minor.patch (e.g., 6.8.1), with Linus Torvalds managing releases.

## Key Claims

- Linux is monolithic in design—all core subsystems share a single kernel address space—but supports runtime extensibility through loadable kernel modules that can be inserted and removed without reboot
- CFS uses virtual runtime tracked in a red-black tree to achieve proportional CPU allocation, replacing the O(1) scheduler with a more mathematically fair approach
- VFS decouples the system call interface from filesystem implementation, allowing any filesystem to be mounted transparently by implementing a standard set of operations structs
- Device drivers constitute over 60% of the Linux kernel source code, making driver quality and stability a dominant factor in overall kernel reliability
- The /proc and /sys virtual filesystems expose kernel internals to user space as file hierarchies, enabling monitoring, tuning, and debugging without specialized tools

## Atomic Facts

1. CFS assigns each task a virtual runtime (`vruntime`) that advances inversely proportional to the task's weight (derived from its nice value); the task with the smallest `vruntime` is always scheduled next
2. Loadable modules use `module_init()` and `module_exit()` macros to register setup and teardown functions, and are loaded into kernel address space with full kernel privileges
3. VFS defines four key structure types: `super_block` (filesystem instance), `inode` (file metadata), `dentry` (directory entry cache), and `file` (open file instance)
4. The OOM killer selects victim processes using an `oom_score` that factors in memory usage, nice value, and the `oom_score_adj` tunable in `/proc/[pid]/oom_score_adj`
5. `/proc/sys/` contains writable files for kernel tuning (e.g., `/proc/sys/vm/swappiness` controls swap aggressiveness, default 60)
6. The kernel source tree exceeds 30 million lines of code as of version 6.x, with `drivers/` being the largest subdirectory

## Significance

Linux is the most widely deployed operating system kernel in history, running on everything from smartphones (Android) to supercomputers (100% of the Top 500). Its monolithic-with-modules architecture represents a pragmatic compromise between the performance of monolithic design and the flexibility of modular systems. Understanding Linux kernel architecture is essential for systems programming, performance tuning, driver development, and comprehending how modern computing infrastructure operates.

## Chunks Extracted

*Pending*
