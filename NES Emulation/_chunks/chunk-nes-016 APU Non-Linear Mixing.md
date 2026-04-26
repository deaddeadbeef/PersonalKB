---
tags: [chunk, nes-emulation, apu]
source: "[[raw-nes-003]]"
up: "[[APU — Audio Processing Unit Overview]]"
---

# Chunk NES 016 — APU Non-Linear Mixing

The NES APU mixes all five channels using a non-linear formula matching the hardware DAC. Pulse output uses a lookup table indexed by the sum of pulse 1 and pulse 2 amplitudes. The TND (triangle, noise, DMC) output uses a separate table indexed by 3 times triangle plus 2 times noise plus DMC level. This non-linear mixing means channel volumes interact — louder channels slightly suppress quieter ones, producing the characteristic NES sound. OxideNES uses blip_buf for band-limited synthesis, resampling from the 1.79 MHz NES rate to the host 44.1/48 kHz rate without aliasing.
