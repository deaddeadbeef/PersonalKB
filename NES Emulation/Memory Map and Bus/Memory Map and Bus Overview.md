---
tags: [nes, hub]
up: "[[NES Emulation]]"
confidence: plausible
---
# Memory Map and Bus Overview

The NES CPU sees a 64 KB address space (0x0000-0xFFFF) shared between RAM, PPU registers, APU registers, and cartridge ROM. The PPU has its own separate 16 KB address space. Understanding the memory map is essential for emulating how all components communicate.

## Pages

- [[CPU Memory Map]] — Complete CPU address space layout
- [[PPU Memory Map]] — VRAM, pattern tables, palettes
- [[OAM DMA]] — The 513-cycle sprite transfer mechanism

## Key Facts

- **CPU bus:** 16-bit addressing, 0x0000-0xFFFF
- **PPU bus:** 14-bit addressing, 0x0000-0x3FFF
- **Extensive mirroring** saves address decode logic
- **DMA** is the only bulk data transfer mechanism

## OxideNES Implementation

us.rs (351 lines): The Bus struct is the central arbitration layer, implementing cpu_read()/cpu_write() with proper address mapping and mirroring. Game Genie intercepts reads transparently.

## References

→ [[Sources Index]]
