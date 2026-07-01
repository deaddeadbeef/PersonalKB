---
tags:
  - csos
  - csos/io
confidence: verified
freshness: stable
up: "[[IO Overview]]"
tier-coverage:
  - intuition
  - core
  - deep-dive
  - practice
---
# IO Hardware Fundamentals

## 🎯 Intuition
**The Core Idea:** Every I/O device hides behind a **device controller** — a chip or circuit board that handles the device's low-level protocol and exposes a small set of registers to the CPU. The OS talks to the controller, not the device directly.

**Analogy:** The controller is a translator between the CPU's language and the device's native protocol.

**Why It Matters:** Understanding this hardware interface explains why I/O software is layered: the OS can use a common structure of commands, status checks, and data movement even though the underlying devices differ.

## ⚙️ Core Mechanics
### Device Controller Registers
Controllers typically expose command, status, and data registers.

| Register | Purpose |
|----------|---------|
| Command register | CPU writes here to start an operation |
| Status register | CPU reads here to check if the device is ready or has an error |
| Data register | Transfers data one unit at a time (programmed I/O) |

### How the CPU Talks to Controllers
#### Port-Mapped I/O
Controller registers appear as I/O ports in a separate address space. Special `IN`/`OUT` instructions (x86) read and write them.

#### Memory-Mapped I/O
Controller registers appear at specific physical memory addresses. Ordinary load/store instructions work; widely used in ARM and modern x86.

### Three I/O Paradigms
The same controller interface can be used in several ways depending on how much work the CPU does.

| Paradigm | How CPU is involved | Cost |
|----------|--------------------|----|
| Programmed I/O (busy-wait) | CPU polls status register continuously | Wastes CPU cycles |
| Interrupt-driven I/O | Device interrupts CPU when done; CPU is free meanwhile | System-call + handler overhead |
| DMA | DMA controller moves data autonomously; interrupts only when block is done | Most efficient for large transfers |

## 🔬 Deep Dive
### Interrupt Handling Overview
1. Device raises an interrupt line.
2. CPU finishes current instruction; saves state; looks up **interrupt vector**.
3. Jumps to interrupt handler (ISR).
4. ISR services the device; acknowledges interrupt.
5. CPU restores state and resumes interrupted work.

### When Each Paradigm Fits Best
- **Programmed I/O** is simplest and is acceptable for tiny transfers or simple devices, but the CPU may sit in a polling loop reading the **status register**.
- **Interrupt-driven I/O** is better when completion may take a while, because the CPU can do other work until the device signals completion.
- **DMA** is best for bulk transfers because the DMA controller handles the block movement and the CPU is interrupted only when the transfer is done.
- **Memory-mapped I/O** is preferred on ARM because ordinary load/store instructions can access device registers directly, avoiding a separate I/O instruction set.

## 🏋️ Practice
### Warm-Up
1. Why does the OS communicate with a device controller instead of the physical device directly?
2. In a polling loop, which controller register does the CPU repeatedly check?
3. Why is memory-mapped I/O preferred on ARM?

### Core Problems
1. Compare CPU utilisation for programmed I/O and DMA during a 1 MB disk read. Which one ties up the CPU more, and why?
2. A controller exposes command, status, and data registers. Describe the likely sequence of CPU actions needed to start an I/O operation and determine when it has finished.
3. Contrast port-mapped I/O and memory-mapped I/O in terms of instruction support and hardware visibility.

### Challenge
1. A device completes an operation rarely but transfers large blocks when it does. Which of the three paradigms is the best fit, and what trade-off does it avoid?
2. Explain how the existence of controller registers helps justify the layered design of I/O software in the OS.

## Supporting Chunks

- [[IO - Interrupts allow devices to signal the CPU asynchronously without busy-waiting]]
- [[IO - DMA offloads bulk data transfers from the CPU to a dedicated controller]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 5.
