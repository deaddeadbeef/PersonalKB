---
tags: [chunk, nes-emulation, expansion-audio]
source: "[[raw-nes-024]]"
up: "[[Expansion Audio]]"
---

# Chunk NES 089 — Expansion Audio Mixing

On real NES hardware, expansion audio from cartridge chips mixes with APU output through the cartridge connector's audio pin. Mixing ratios vary by expansion chip and cartridge design — no single standard exists. OxideNES uses configurable mixing levels defaulting to community-researched balanced ratios. Expansion audio samples are generated at the CPU clock rate alongside APU samples and summed before band-limited downsampling via blip_buf. The Famicom's audio path routed cartridge audio through the console's mixer; the NES's different pin configuration meant some expansion audio features were region-dependent.
