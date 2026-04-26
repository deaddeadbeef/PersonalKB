---
tags: [chunk, nes-emulation, memory]
source: "[[raw-nes-004]]"
up: "[[OAM DMA]]"
---

# Chunk NES 019 — OAM DMA Transfer Mechanism

Writing byte N to  triggers a 256-byte bulk copy from CPU page - to PPU OAM. The transfer takes 513 CPU cycles (514 on odd-cycle starts): 1 dummy read cycle, optional alignment cycle, then 256 alternating read/write pairs. During DMA, the CPU is completely stalled. OxideNES implements this by setting a dma_cycles counter in the bus; each clock tick decrements it while performing the read-write sequence. This is over 2x faster than manual LDA/STA loops and is used by virtually every NES game for sprite updates.
