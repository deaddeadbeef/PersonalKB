---
tags: [chunk, nes-emulation, apu]
source: "[[raw-nes-003]]"
up: "[[Pulse Channels]]"
---

# Chunk NES 105 — Sweep Unit Operation

Each pulse channel has a sweep unit that periodically adjusts the timer period, creating pitch slides. The sweep divider counts down at the half-frame rate (approximately 120 Hz). When it reaches zero, the timer period is shifted right by 0-7 positions (the shift count), and the result is either added to or subtracted from the current period. If the resulting period is less than 8 or greater than , the channel is silenced (muted). Pulse 1 uses ones complement negation (giving a slightly different result than twos complement), while Pulse 2 uses twos complement — a hardware asymmetry faithfully emulated by OxideNES.
