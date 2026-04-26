---
tags: [chunk, nes-emulation, apu]
source: "[[raw-nes-003]]"
up: "[[APU Frame Sequencer]]"
---

# Chunk NES 015 — APU Frame Sequencer Modes

The APU frame sequencer clocks the length counters, envelopes, sweep units, and linear counter at hardware-defined intervals. In 4-step mode (default): quarter-frame events (envelope and linear counter) fire at all 4 steps; half-frame events (length counter and sweep) fire at steps 2 and 4; an optional IRQ fires at step 4. In 5-step mode: same clocking pattern over 5 steps with no IRQ and slightly different timing feel. OxideNES implements this as a cycle counter that fires events at the exact hardware-documented CPU cycle positions for each mode.
