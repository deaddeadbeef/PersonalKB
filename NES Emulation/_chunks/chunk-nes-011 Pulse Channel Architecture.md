---
tags: [chunk, nes-emulation, apu]
source: "[[raw-nes-003]]"
up: "[[Pulse Channels]]"
---

# Chunk NES 011 — Pulse Channel Architecture

Each of the two NES pulse channels generates a square wave with selectable duty cycle: 12.5%, 25%, 50%, or 75%. Components include an 11-bit timer controlling pitch, a length counter for automatic silencing, an envelope generator providing constant or decaying volume, and a sweep unit that periodically adjusts the timer period. A hardware quirk: Pulse 1 uses ones complement for sweep negation while Pulse 2 uses twos complement, causing slightly different minimum periods. OxideNES faithfully emulates this asymmetry. The duty cycle is implemented as an 8-step sequence table.
