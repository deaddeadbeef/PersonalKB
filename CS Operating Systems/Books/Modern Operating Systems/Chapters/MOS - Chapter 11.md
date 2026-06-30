---
id: mos-ch-11
type: book-chapter
chapter: 11
book: "Modern Operating Systems"
author: "Andrew S. Tanenbaum"
status: seeded
chunk_count: 2
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
tags:
  - csos
  - book-chapter
up: "[[Chapter Index]]"
confidence: verified
---
# MOS — Chapter 11: Case Study 2 — Windows 8

## Summary

Windows is the dominant desktop OS and a major server platform. Its architecture descends from Windows NT (1993), designed from scratch for portability and security. The Hardware Abstraction Layer (HAL) isolates the kernel from platform-specific details. The NT kernel is a hybrid: a small microkernel handles interrupt scheduling and multiprocessor synchronisation, while the executive (running in kernel mode) provides object management, memory management, I/O, security, and process management as separate but in-process subsystems. The Win32 subsystem runs as a user-mode server process but performance-critical paths are incorporated into the kernel. The Registry is the system-wide persistent configuration store, replacing the scattered .ini file approach of Win16. The chapter covers the Windows object model, handle tables, and security descriptors, then examines memory management (working sets, VAD trees, section objects) and the I/O model (IRP-based, asynchronous by default).

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| HAL | Hardware Abstraction Layer; isolates NT kernel from platform details |
| NT executive | Kernel-mode subsystems: object manager, process manager, I/O manager, etc. |
| Registry | Hierarchical key-value store for system and application configuration |
| IRP | I/O Request Packet; data structure passed down the driver stack |
| Object manager | Unified handle-based abstraction for all kernel resources |

## Chunk Candidates

- [x] [[Case Studies - Windows NT uses a hybrid architecture with a HAL and an in-process executive]]
- [x] [[Case Studies - The Windows Registry is a hierarchical persistent configuration store replacing ini files]]

## Wiki Pages Seeded

- [[Windows NT Architecture]] — HAL, executive, Win32 subsystem, Registry, object model

## References

See [[Sources Index#Tanenbaum 2015]].
