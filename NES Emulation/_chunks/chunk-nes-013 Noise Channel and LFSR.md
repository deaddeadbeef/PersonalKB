---
tags: [chunk, nes-emulation, apu]
source: "[[raw-nes-003]]"
up: "[[Triangle and Noise Channels]]"
---

# Chunk NES 013 — Noise Channel and LFSR

The noise channel uses a 15-bit Linear Feedback Shift Register (LFSR) for pseudo-random noise generation. Long mode (tapping bits 0 and 1) produces white noise with a period of 32,767 samples. Short mode (tapping bits 0 and 6) creates a metallic, tonal buzzing with a period of only 93 samples. One of 16 preset timer periods controls the LFSR clock rate. Like pulse channels, the noise channel has an envelope generator for volume shaping and a length counter for duration control. Short-mode noise is commonly used for metallic percussion effects.
