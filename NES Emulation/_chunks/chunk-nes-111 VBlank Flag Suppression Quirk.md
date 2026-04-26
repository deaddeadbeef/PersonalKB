---
tags: [chunk, nes-emulation, ppu]
source: "[[raw-nes-002]]"
up: "[[PPU Registers and Timing]]"
---

# Chunk NES 111 — VBlank Flag Suppression Quirk

The NES PPU has a timing quirk where reading PPUSTATUS () within a 1-2 cycle window of VBlank start (cycle 1 of scanline 241) suppresses the VBlank flag — it reads as clear even though VBlank is beginning. Additionally, if the VBlank flag is read during this window, the NMI that would normally fire is also suppressed. This race condition between the CPU reading the flag and the PPU setting it must be emulated at cycle-level precision. Blargg's vbl_nmi_timing test ROM specifically validates this behavior, and several commercial games are sensitive to its exact timing.
