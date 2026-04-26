---
tags: [chunk, nes-emulation, dma]
source: "[[raw-nes-029]]"
up: "[[OAM DMA]]"
---

# Chunk NES 071 — OAM DMA Cycle-Accurate Timing

OAM DMA () transfers 256 bytes from CPU memory to PPU OAM in exactly 513 CPU cycles (514 on odd-cycle start). The sequence: 1 dummy read cycle for synchronization, 1 optional alignment cycle on odd CPU cycles, then 256 alternating read-write pairs. During the entire transfer the CPU is halted — it cannot execute instructions or respond to interrupts. This precise timing matters because games using sprite-0 hit for raster effects depend on OAM DMA completing at exactly the right cycle. OxideNES counts DMA cycles exactly, including the odd-cycle alignment penalty.
