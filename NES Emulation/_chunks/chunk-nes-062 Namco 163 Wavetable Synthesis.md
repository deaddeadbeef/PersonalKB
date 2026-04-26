---
tags: [chunk, nes-emulation, expansion-audio]
source: "[[raw-nes-024]]"
up: "[[Expansion Audio]]"
---

# Chunk NES 062 — Namco 163 Wavetable Synthesis

The Namco 163 (Mapper 19) provides wavetable synthesis supporting up to 8 channels. Each channel plays from a 4-bit wavetable stored in 128 bytes of internal RAM with configurable wave length per channel. The channels share time-division multiplexing — more active channels means lower update rate per channel. Four channels at full quality is typical; eight channels halves the effective sample rate. Used by Rolling Thunder, Megami Tensei II, and King of Kings. This makes the N163 uniquely flexible among NES expansion chips, allowing custom waveforms that no other NES audio hardware can produce.
