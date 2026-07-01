---
tags: [nes, hub]
up: "[[NES Emulation]]"
confidence: established
freshness: stable
tier-coverage: [intuition, core, deep-dive]
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

## How To Read This Chapter

Read this chapter for audio timing and mixer behavior. NES emulation is less about isolated facts than about making several small timed machines agree on the same frame. The overview pages should give you the vocabulary first, then route you into the detailed pages where timing, registers, and test-ROM behavior matter.

A productive pass has three questions. First, what state does this subsystem own? Second, which reads or writes have side effects? Third, what timing relationship can break a game if it is off by even a few CPU or PPU cycles? Keep those questions nearby while reading the linked pages.

## Emulator Checkpoints

Use the deeper notes to turn the concept into implementation proof. The key checkpoints for this chapter are: frame sequencer cadence, envelope decay, sweep units, DMC DMA stalls, and nonlinear mixing. For each checkpoint, prefer a tiny deterministic test before a visual game test. A passing screenshot is useful, but a focused trace is better when the bug is cycle timing, flag behavior, mapper state, or register side effects.

The chapter is mastered when you can explain both the user-visible symptom and the internal cause of a failure. For example, audio pops, scrolling seams, wrong sprite priority, broken controller input, or a mapper crash should point back to a specific piece of state and a specific clock boundary.

## References

→ [[NES Emulation/Sources/Sources Index|Sources Index]]
