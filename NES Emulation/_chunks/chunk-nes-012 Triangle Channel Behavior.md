---
tags: [chunk, nes-emulation, apu]
source: "[[raw-nes-003]]"
up: "[[Triangle and Noise Channels]]"
---

# Chunk NES 012 — Triangle Channel Behavior

The triangle channel produces a triangle wave using a 32-step sequence cycling through values 15 down to 0 then back up. It has both a linear counter (reload controlled by a register) and a length counter — both must be non-zero for output. Unlike pulse channels, the triangle has no volume control; it is either on at full volume or silent. At very low period values, the rapid cycling produces audible buzzing rather than a clear tone, an effect NES composers exploit for percussion-like sounds in game music.
