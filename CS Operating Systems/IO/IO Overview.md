---
tags:
  - csos
  - moc
up: "[[CS Operating Systems]]"
confidence: established
freshness: stable
tier-coverage: [intuition, core]
---
# IO Overview

The I/O subsystem connects the OS to storage, network, and peripheral hardware. This domain covers the hardware model (controllers, interrupts, DMA), the layered software stack, device drivers, and disk scheduling algorithms.

---

## Learn in This Order

1. [[IO Hardware Fundamentals]] — device controllers; memory-mapped I/O; polling vs interrupt-driven; DMA
2. [[Interrupts and DMA]] — interrupt vector; ISR; DMA transfer lifecycle; programmed I/O comparison
3. [[IO Software Layers]] — interrupt handlers → device drivers → OS-independent layer → user-space libraries
4. [[Device Drivers]] — driver model; kernel modules; driver lifecycle; driver/kernel interface
5. [[Disk Scheduling Algorithms]] — FCFS, SSTF, SCAN/elevator, C-SCAN; seek time optimisation

---

## In This Domain

| Page | One-line summary |
|------|-----------------|
| [[IO Hardware Fundamentals]] | Controllers; memory-mapped I/O; polling vs interrupts; DMA |
| [[Interrupts and DMA]] | Interrupt vector; ISR; DMA offload; programmed I/O |
| [[IO Software Layers]] | Four-layer I/O software stack from interrupt handler to user space |
| [[Device Drivers]] | Kernel modules; driver model; initialization and cleanup |
| [[Disk Scheduling Algorithms]] | FCFS/SSTF/SCAN/C-SCAN seek optimization |

---

## Common Distinctions

| Question | Answer |
|----------|--------|
| Programmed I/O vs interrupt-driven vs DMA? | PIO = CPU busy-waits (wastes CPU). Interrupt-driven = CPU does other work, device interrupts when ready. DMA = device controller transfers directly to RAM, CPU only handles start/end. |
| SSTF vs SCAN? | SSTF (shortest seek) minimizes seek time but can starve far-away requests. SCAN (elevator) sweeps in one direction — fairer but slightly higher average seek time. |
| Device driver vs OS-independent layer? | Device drivers are hardware-specific. The OS-independent (or device-independent) layer handles buffering, error reporting, and uniform interfaces above the driver. |

---

## How to Navigate

- **Hardware side?** [[IO Hardware Fundamentals]] and [[Interrupts and DMA]]
- **Software side?** [[IO Software Layers]] and [[Device Drivers]]
- **Disk performance question?** [[Disk Scheduling Algorithms]]

---

## Related Domains

- **[[File Systems Overview]]** — file systems sit directly above the I/O subsystem; disk scheduling affects file-system throughput.
- **[[OS Foundations Overview]]** — interrupts are the general mechanism by which devices signal the OS; system calls and interrupts share the same trap mechanism.

## References

- [[CS Operating Systems/Sources/Sources Index]]
- [[CS Operating Systems/CS Operating Systems Book Reading Spine]]
