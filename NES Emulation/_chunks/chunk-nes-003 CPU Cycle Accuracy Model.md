---
tags: [chunk, nes-emulation, cpu]
source: "[[raw-nes-001]]"
up: "[[CPU Cycle Accuracy and Timing]]"
---

# Chunk NES 003 — CPU Cycle Accuracy Model

OxideNES achieves cycle-accurate CPU emulation through a remaining_cycles counter. When an instruction begins, remaining_cycles is set to the instruction's base cycle count. The bus calls cpu.tick() each master clock cycle; the CPU only executes a new instruction when remaining_cycles reaches zero. Page-crossing penalties (extra cycle when indexed addressing crosses a 256-byte page boundary) and branch-taken penalties are added dynamically. This approach produces correct timing without requiring a full per-cycle pipeline simulation, balancing accuracy with implementation simplicity.
