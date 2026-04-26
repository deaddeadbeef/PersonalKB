---
tags: [chunk, nes-emulation, apu]
source: "[[raw-nes-003]]"
up: "[[APU — Audio Processing Unit Overview]]"
---

# Chunk NES 106 — Envelope Generator

The APU envelope generator provides either constant volume or a decaying volume effect for pulse and noise channels. In constant mode, the volume register value (0-15) is output directly. In decay mode, a divider counts down at the quarter-frame rate (approximately 240 Hz); each time it reaches zero, the decay level decrements from 15 toward 0. With the loop flag set, the level wraps from 0 back to 15, creating a repeating sawtooth volume envelope. The envelope output serves as the channel's amplitude, multiplied by the duty/noise waveform. This simple hardware mechanism produces the characteristic NES sound attacks and fades.
