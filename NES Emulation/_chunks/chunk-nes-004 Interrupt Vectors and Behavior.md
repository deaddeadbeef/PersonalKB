---
tags: [chunk, nes-emulation, cpu]
source: "[[raw-nes-001]]"
up: "[[Interrupts — NMI, IRQ, and Reset]]"
---

# Chunk NES 004 — Interrupt Vectors and Behavior

The 6502 supports three interrupt vectors stored at fixed addresses: NMI at -, RESET at -, and IRQ/BRK at -. NMI is edge-triggered with highest priority, asserted by the PPU at the start of vertical blank (scanline 241). IRQ is level-triggered and masked by the I flag. The interrupt sequence pushes PC and the status register P to the stack (consuming 7 cycles total), sets the I flag to prevent nested interrupts, and loads PC from the appropriate vector. OxideNES polls for pending interrupts between instructions, matching real hardware behavior.
