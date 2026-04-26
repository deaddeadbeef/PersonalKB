---
tags: [chunk, nes-emulation, memory]
source: "[[raw-nes-004]]"
up: "[[Memory Map and Bus Overview]]"
---

# Chunk NES 117 — Controller Port Dual Purpose

The controller ports at  and  serve dual purposes.  handles player 1 controller strobe and data reads.  serves both player 2 controller data AND the APU frame counter mode register on writes. Writing to  configures the APU frame sequencer (4-step or 5-step mode, IRQ inhibit), while reading from  returns controller 2 button data. This dual-purpose mapping is an example of the NES's aggressive address space economy. OxideNES routes  writes to the APU and reads to the controller subsystem, maintaining both functions correctly.
