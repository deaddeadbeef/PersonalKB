---
tags:
  - csos
  - moc
up: "[[CS Operating Systems]]"
confidence: verified
---
# Case Studies Overview

Abstract OS concepts become concrete in real systems. This domain examines three major operating systems — Linux, Android, and Windows NT — applying Foundations, Processes, Memory, Security, and File System concepts to real architectures.

---

## Learn in This Order

1. [[Linux Architecture Overview]] — monolithic + loadable modules; VFS; CFS scheduler; kernel memory subsystem
2. [[Android Architecture]] — Android on Linux; Binder IPC; permission model; Dalvik/ART runtime
3. [[Windows NT Architecture]] — NT kernel; HAL; executive subsystems; Registry; hybrid architecture

---

## In This Domain

| Page | One-line summary |
|------|-----------------|
| [[Linux Architecture Overview]] | Kernel layers; VFS; CFS; memory management in Linux |
| [[Android Architecture]] | Android atop Linux; Binder; permissions; Dalvik/ART |
| [[Windows NT Architecture]] | NT kernel; HAL; executive; Registry; hybrid design |

---

## Common Distinctions

| Question | Answer |
|----------|--------|
| Linux (monolithic) vs Windows NT (hybrid)? | Linux is monolithic with dynamic module loading. Windows NT separates a microkernel-like executive from subsystem servers but keeps most in kernel space — called hybrid. |
| Android vs Linux kernel? | Android runs on a modified Linux kernel but adds Binder IPC (replacing traditional Unix IPC), a capability-based permission model, and ART runtime instead of bare native execution. |
| VFS in Linux? | The Virtual File System layer provides a uniform file API that routes to ext4, FAT, NFS, etc. — concrete example of mechanism-vs-policy separation. |

---

## How to Navigate

- **Consolidating your OS knowledge?** Work through the case studies *after* the foundational domains — each page assumes you know the concepts from those domains.
- **Linux internals?** [[Linux Architecture Overview]]
- **Mobile OS / Android?** [[Android Architecture]]
- **Windows design?** [[Windows NT Architecture]]

---

## Related Domains

- **[[OS Foundations Overview]]** — Linux and Windows NT are direct applications of the monolithic/hybrid architecture concepts.
- **[[Processes Overview]]** — CFS scheduling (Linux) and Windows NT process model are Processes concepts in practice.
- **[[Memory Management Overview]]** — Linux's memory subsystem (zone allocator, SLUB, mmap) is virtual memory applied.
- **[[Security Overview]]** — Android's permission model and Windows NT's access token system are Security concepts in action.
- **[[Design Principles Overview]]** — VFS (Linux) and HAL (Windows NT) are textbook applications of mechanism-vs-policy.

## References
- [[CS Operating Systems/Sources/Sources Index|CS Operating Systems Sources Index]]
