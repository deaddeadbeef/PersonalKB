---
tags: [chunk, nes-emulation, timing]
source: "[[raw-nes-020]]"
up: "[[Main Loop and Cycle Ratios]]"
---

# Chunk NES 078 — Audio Sample Rate Conversion

The APU generates samples at the CPU clock rate of approximately 1.79 MHz but host audio runs at 44,100 or 48,000 Hz. OxideNES uses blip_buf for band-limited downsampling: the APU writes amplitude deltas into the blip buffer at NES timestamps and blip_buf renders these into PCM samples at the host rate. This prevents aliasing artifacts that would occur with naive downsampling. The audio buffer serves as the primary frame pacing mechanism — if audio runs ahead of emulation, the frame loop delays; if behind, frames are dropped to maintain synchronization.
