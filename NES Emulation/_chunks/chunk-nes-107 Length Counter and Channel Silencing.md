---
tags: [chunk, nes-emulation, apu]
source: "[[raw-nes-003]]"
up: "[[APU — Audio Processing Unit Overview]]"
---

# Chunk NES 107 — Length Counter and Channel Silencing

The APU length counter provides automatic channel silencing after a programmable duration. Loading the length counter register sets the counter to one of 32 pre-defined values (stored in a lookup table, ranging from 1 to 254 half-frames). The counter decrements at the half-frame rate (approximately 120 Hz). When it reaches zero, the channel is silenced until a new length value is loaded. A halt flag can freeze the counter, preventing it from decrementing. This mechanism lets games play notes of specific durations without CPU intervention — the sound engine just writes the note frequency and length, then moves on.
