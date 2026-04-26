---
tags: [chunk, nes-emulation, timing]
source: "[[raw-nes-020]]"
up: "[[Main Loop and Cycle Ratios]]"
---

# Chunk NES 077 — NTSC Frame Timing

One NTSC frame is 262 scanlines times 341 PPU cycles equals 89,342 PPU cycles, or approximately 29,780.67 CPU cycles at the 3:1 ratio. The fractional cycle is handled by the odd frame skip: on odd frames, the pre-render scanline is 340 cycles instead of 341. This alternation produces frame lengths of 29,780 and 29,781 CPU cycles, yielding a frame rate of approximately 60.0988 FPS. PAL uses 312 scanlines at approximately 50.007 FPS. OxideNES uses std::time::Instant for high-resolution frame pacing with optional VSync support through the minifb window library.
