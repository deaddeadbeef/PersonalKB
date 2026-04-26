---
tags: [chunk, nes-emulation, timing]
source: "[[raw-nes-020]]"
up: "[[Main Loop and Cycle Ratios]]"
---

# Chunk NES 120 — PPU-CPU Synchronization Critical Points

The PPU and CPU need tight synchronization because they interact through shared registers. Critical timing points include: NMI assertion at PPU cycle 1 of scanline 241 must be visible to the CPU at the exact corresponding CPU cycle. Sprite-0 hit timing depends on the precise PPU cycle the hit occurs. Mid-frame PPU register writes must take effect at the correct cycle position. OxideNES achieves this through per-tick interleaving: for every CPU cycle, exactly 3 PPU cycles execute beforehand, ensuring PPU state is always up-to-date when the CPU reads PPU registers. This is the fundamental correctness guarantee of the emulation.
