---
tags: [chunk, nes-emulation, memory]
source: "[[raw-nes-004]]"
up: "[[Memory Map and Bus Overview]]"
---

# Chunk NES 020 — Bus Timing and Clock Ratios

The NES bus runs at the NTSC master clock of 21.477272 MHz. The CPU divides this by 12 (1.789773 MHz) and the PPU by 4 (5.369318 MHz), yielding a 3:1 PPU-to-CPU ratio. OxideNES implements this in the bus clock() method: each call ticks the PPU three times, then the CPU once (unless DMA-stalled), then the APU once at CPU rate. The outer loop calls clock() until ppu.frame_complete is set, then renders and sleeps to maintain 60 FPS. This interleaved ticking ensures the PPU state is always current when the CPU reads PPU registers.
