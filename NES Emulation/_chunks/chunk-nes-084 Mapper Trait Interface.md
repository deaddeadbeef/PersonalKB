---
tags: [chunk, nes-emulation, mapper]
source: "[[raw-nes-005]]"
up: "[[Cartridges and Mappers Overview]]"
---

# Chunk NES 084 — Mapper Trait Interface

OxideNES defines a Mapper trait with methods: cpu_read(addr) and cpu_write(addr, val) for CPU address space access, ppu_read(addr) and ppu_write(addr, val) for PPU space, mirror_mode() returning the current nametable mirroring configuration, and optional irq_tick() for mappers with scanline counters. Each of the 20 supported mappers implements this trait as a separate struct. The Cartridge struct holds the active mapper instance and delegates all ROM and RAM access through it. This trait-based design makes adding new mapper support straightforward without modifying the bus or PPU code.
