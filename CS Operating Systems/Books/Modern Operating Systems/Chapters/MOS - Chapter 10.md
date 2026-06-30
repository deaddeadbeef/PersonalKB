---
id: mos-ch-10
type: book-chapter
chapter: 10
book: "Modern Operating Systems"
author: "Andrew S. Tanenbaum"
status: seeded
chunk_count: 3
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
tags:
  - csos
  - book-chapter
up: "[[Chapter Index]]"
confidence: verified
---
# MOS — Chapter 10: Case Study 1 — UNIX, Linux, and Android

## Summary

The first case study traces the UNIX lineage from Bell Labs through BSD to the Linux kernel, showing how the theoretical concepts of earlier chapters manifest in a real production system. Linux is a monolithic kernel with loadable modules — a pragmatic compromise between clean microkernel design and raw performance. The VFS (Virtual File System) layer provides a uniform file interface across ext4, tmpfs, procfs, and network file systems. The Completely Fair Scheduler (CFS) uses a red-black tree to provide $O(\log n)$ scheduling with weighted fairness. Memory management follows the buddy system for physical allocation and slab allocator for kernel objects. The Android section explains how Android builds on the Linux kernel while replacing most of the GNU userspace: Binder IPC replaces UNIX sockets for efficient inter-app communication, the permission system enforces app sandboxing, and ART (Android Runtime) compiles Dalvik bytecode to native code ahead-of-time.

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| Linux monolithic kernel | All subsystems in one address space; loadable modules for extensibility |
| VFS | Abstract file-system layer enabling multiple FS implementations |
| CFS | Completely Fair Scheduler; virtual runtime in a red-black tree |
| Binder IPC | Android's fast inter-process communication via shared memory + kernel driver |
| ART | Android Runtime; AOT compilation of Dalvik bytecode |
| Android permissions | App-level sandbox; user grants capabilities at install/runtime |

## Chunk Candidates

- [x] [[Case Studies - Linux uses a monolithic kernel with loadable modules as a performance-reliability compromise]]
- [x] [[Case Studies - The VFS layer lets Linux support heterogeneous file systems behind a uniform interface]]
- [x] [[Case Studies - Android extends Linux with Binder IPC and a permission-based app sandbox]]

## Wiki Pages Seeded

- [[Linux Architecture Overview]] — kernel layers, VFS, CFS, memory subsystem
- [[Android Architecture]] — Binder IPC, permission model, ART runtime

## References

See [[Sources Index#Tanenbaum 2015]].
