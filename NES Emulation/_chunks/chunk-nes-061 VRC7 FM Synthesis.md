---
tags: [chunk, nes-emulation, expansion-audio]
source: "[[raw-nes-024]]"
up: "[[Expansion Audio]]"
---

# Chunk NES 061 — VRC7 FM Synthesis

The Konami VRC7 (Mapper 85) contains a YM2413-derivative FM synthesis chip providing 6 independent channels. Each channel uses 2-operator FM synthesis (modulator feeding carrier) with ADSR envelopes, vibrato, and tremolo. Fifteen built-in instrument patches are stored as ROM data matching YM2413 register format, plus one user-definable custom patch. FM synthesis computes output = sin(carrier_freq * t + modulation_index * sin(mod_freq * t)). Used only by Lagrange Point, it represents the most powerful NES expansion audio. OxideNES implements a simplified FM model producing accurate-sounding synthesis.
