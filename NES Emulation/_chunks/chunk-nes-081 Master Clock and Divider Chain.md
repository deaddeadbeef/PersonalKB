---
tags: [chunk, nes-emulation, timing]
source: "[[raw-nes-020]]"
up: "[[Main Loop and Cycle Ratios]]"
---

# Chunk NES 081 — Master Clock and Divider Chain

The NTSC NES master clock runs at 21.477272 MHz, derived from a crystal oscillator at exactly 6 times the NTSC colorburst frequency (3.579545 MHz times 6). The CPU divides this by 12 yielding 1.789773 MHz. The PPU divides by 4 yielding 5.369318 MHz. This produces the fundamental 3-to-1 PPU-to-CPU cycle ratio. The APU runs at CPU rate with its frame sequencer further dividing for envelope clocking at approximately 240 Hz and length counter clocking at approximately 120 Hz. All timing in the emulator flows from these fixed hardware ratios.
