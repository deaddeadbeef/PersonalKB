---
id: mos-ch-05
type: book-chapter
chapter: 5
book: "Modern Operating Systems"
author: "Andrew S. Tanenbaum"
status: seeded
chunk_count: 5
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
tags:
  - csos
  - book-chapter
up: "[[CS Operating Systems/Books/Modern Operating Systems/Chapter Index|Chapter Index]]"
confidence: established
freshness: stable
tier-coverage: [core]
---
# MOS — Chapter 05: Input/Output

## Summary

I/O is the bridge between the OS and the physical world. The chapter surveys the hardware side: device controllers, registers, ports, interrupts, and DMA. Three ways for a CPU to interact with a device — programmed I/O (busy-wait), interrupt-driven I/O, and DMA (hardware-managed bulk transfer) — are compared for efficiency. The software architecture is layered: interrupt handlers at the bottom catch device signals and unblock waiting processes; device drivers translate OS-generic requests into device-specific command sequences; the OS-independent layer provides uniform block/character interfaces and buffering; and user-space I/O libraries add formatting. Disk scheduling algorithms (SSTF, SCAN, C-SCAN) reduce average seek time to improve throughput. The chapter ends with clocks, terminals, and network I/O as representative device classes.

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| Device controller | Hardware component managing a class of devices; exposes registers |
| Interrupt | Asynchronous hardware signal requesting CPU attention |
| DMA | Direct Memory Access — controller moves data without CPU per-byte involvement |
| Device driver | OS module translating generic I/O requests to device-specific commands |
| SCAN scheduling | Disk arm sweeps back and forth servicing requests in order; elevator |
| Interrupt vector | Table mapping IRQ numbers to handler addresses |

## Chunk Candidates

- [x] [[IO - Interrupts allow devices to signal the CPU asynchronously without busy-waiting]]
- [x] [[IO - DMA offloads bulk data transfers from the CPU to a dedicated controller]]
- [x] [[IO - Device drivers form the OS-to-hardware interface translating generic to device-specific commands]]
- [x] [[IO - IO software uses four layers from interrupt handler to user-space library]]
- [x] [[IO - SCAN disk scheduling services requests in sweep order to reduce average seek time]]

## Wiki Pages Seeded

- [[IO Hardware Fundamentals]] — controllers, ports, interrupts, DMA overview
- [[Interrupts and DMA]] — interrupt mechanism, DMA transfer cycle
- [[IO Software Layers]] — four-layer model: handler → driver → OS layer → user space
- [[Device Drivers]] — driver model, kernel modules
- [[Disk Scheduling Algorithms]] — SSTF, SCAN, C-SCAN

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Tanenbaum 2015]].
