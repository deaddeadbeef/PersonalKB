---
id: chunk-csos-029
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 5"
topic: "io"
claim: "Device drivers form the OS-to-hardware interface by translating generic OS I/O requests (read block N) into device-specific command sequences (ATA command registers, USB bulk-only transport)"
confidence: verified
supports:
  - "[[Device Drivers]]"
  - "[[IO Software Layers]]"
tags:
  - csos
  - csos/io
  - chunk
up: "[[CS Operating Systems]]"
---
# IO — Device drivers form the OS-to-hardware interface translating generic to device-specific commands

## Context

The OS issues generic requests: "read 512 bytes from logical block address 1000". The driver for a SATA disk translates this to the specific sequence of ATA registers that the disk controller understands. The driver for a USB mass-storage device uses the USB Bulk-Only Transport (BOT) protocol to wrap that same request. The calling code above the driver never changes — only the driver differs.

## Why It Matters

Drivers are simultaneously the most important and most dangerous code in the OS. They are important because every hardware interaction goes through them. They are dangerous because they run with full kernel privilege — a null-pointer dereference in an Nvidia driver panics Linux. This is why Windows requires signed drivers and why Tanenbaum argues microkernels (where drivers run in user space) are the right architecture for reliability.

## QnA Seeds

- Q: Why must device drivers run in kernel mode rather than user mode?
- Q: What interface does a Linux block device driver expose to the kernel?
- Q: What happens if a driver has a bug in a monolithic kernel vs a microkernel?
