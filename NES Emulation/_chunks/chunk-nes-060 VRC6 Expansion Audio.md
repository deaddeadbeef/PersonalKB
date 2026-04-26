---
tags: [chunk, nes-emulation, expansion-audio]
source: "[[raw-nes-024]]"
up: "[[Expansion Audio]]"
---

# Chunk NES 060 — VRC6 Expansion Audio

The Konami VRC6 (Mappers 24/26) adds three audio channels: two pulse channels with 8 selectable duty cycles (6.25%-50%) and direct 4-bit volume control (no envelope/sweep needed), plus a unique sawtooth channel using an accumulator that adds a fixed value every 2 CPU cycles, resetting on overflow. The richer duty cycle options and direct volume control surpass the built-in APU pulse channels in capability. Used by Castlevania III (Japanese version) and other Konami titles. OxideNES embeds VRC6 channels in the mapper struct, ticking them at CPU rate and mixing output with APU samples before downsampling.
