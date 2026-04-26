---
id: chunk-csos-051
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 11"
topic: "casestudies"
claim: "Windows NT uses a hybrid architecture: a minimal NT kernel for scheduling and synchronisation, plus an in-kernel executive providing object management, I/O, and security, isolated from hardware by the HAL"
confidence: verified
supports:
  - "[[Windows NT Architecture]]"
  - "[[OS Structure]]"
tags:
  - csos
  - csos/casestudies
  - chunk
up: "[[CS Operating Systems]]"
---
# Case Studies — Windows NT uses a hybrid architecture with a HAL and an in-process executive

## Context

Windows NT's architecture was influenced by Mach and VMS (key designers came from DEC VMS). The Hardware Abstraction Layer (HAL) isolates the kernel from platform-specific details, enabling NT to be ported to MIPS, Alpha, and PowerPC in its early years. The NT kernel itself is small — scheduling, interrupt handling, and multiprocessor synchronisation. Above it, the executive runs in kernel mode but is structured as loosely coupled managers (Object Manager, I/O Manager, Memory Manager, Security Reference Monitor) that communicate via defined interfaces. User-mode subsystems (Win32 via csrss.exe) provide the programming API.

## Why It Matters

NT's architecture explains why Windows can run Win32, POSIX, and OS/2 applications through environment subsystems without changing the kernel. The IRP-based I/O model (all I/O as data-structure packets passed through a driver stack) is why Windows can transparently compose filter drivers (antivirus, encryption, compression) on any device. Understanding NT architecture is foundational for Windows internals, driver development, and Windows security research.

## QnA Seeds

- Q: What is the HAL and why was it important for Windows NT portability?
- Q: What is an IRP and how does it flow through the Windows I/O manager?
- Q: How does the NT Object Manager provide unified access to kernel resources?
