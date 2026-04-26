---
tags: [chunk, nes-emulation, apu]
source: "[[raw-nes-003]]"
up: "[[DMC — Delta Modulation Channel]]"
---

# Chunk NES 014 — DMC Sample Playback

The Delta Modulation Channel (DMC) plays 1-bit delta-encoded audio samples stored in CPU address space (-). Each sample byte is fetched via DMA, stalling the CPU 1-4 cycles per read. Individual bits shift out sequentially: a 1-bit increments the 7-bit output level by 2, a 0-bit decrements by 2, clamped to the range 0-127. The DMC can trigger an IRQ upon sample completion and optionally loop playback. This channel enables digitized speech, drum samples, and sound effects beyond what the synthesis channels can produce.
