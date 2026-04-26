---
tags: [chunk, nes-emulation, cpu]
source: "[[raw-nes-001]]"
up: "[[CPU — The 6502 Processor Overview]]"
---

# Chunk NES 005 — CPU Bus Interface Design

All CPU memory access in OxideNES goes through a Bus trait, enabling memory-mapped I/O. The CPU never directly accesses RAM, PPU registers, or cartridge ROM — every read and write is routed through bus.read(addr) and bus.write(addr, val). This abstraction allows the bus to intercept accesses for PPU register side effects, APU register handling, controller I/O, and mapper bank switching. The CPU also exposes a cycle_count field used by the bus for synchronization with the PPU (3:1 ratio) and APU (1:1 ratio).
