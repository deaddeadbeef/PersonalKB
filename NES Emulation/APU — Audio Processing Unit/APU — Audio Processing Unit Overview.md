---
tags: [nes, hub]
up: "[[NES Emulation]]"
confidence: plausible
---
# APU — Audio Processing Unit Overview

The APU is integrated into the Ricoh 2A03 alongside the CPU. It generates audio through 5 channels: two pulse waves, one triangle wave, one noise generator, and one delta modulation channel (DMC). The APU's distinctive sound defined the 8-bit era.

## Pages

- [[Pulse Channels]] — Square wave generation with duty cycle, sweep, and envelope
- [[Triangle and Noise Channels]] — Triangle wave and pseudo-random noise generation
- [[DMC — Delta Modulation Channel]] — 1-bit delta PCM sample playback
- [[APU Frame Sequencer]] — The 240 Hz timing system controlling channel updates

## Key Facts

- **5 independent channels** producing the classic NES sound
- **Frame sequencer** clocks envelopes at ~240 Hz and sweep/length at ~120 Hz
- **Two modes:** 4-step (with IRQ) and 5-step (no IRQ)
- **Mixer** combines all channels with non-linear approximation

## OxideNES Implementation

`apu.rs` (973 lines): Models all 5 channels with separate structs (Pulse, Triangle, Noise, Dmc). Audio output fed to ring buffer connected to cpal audio device. Frame sequencer implements both 4-step and 5-step timing modes.

## References

→ [[Sources Index]]
