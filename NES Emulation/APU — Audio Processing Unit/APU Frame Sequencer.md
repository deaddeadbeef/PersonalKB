---
tags: [nes, wiki]
up: "[[APU — Audio Processing Unit Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# APU Frame Sequencer

> **The master timer that clocks envelope, sweep, and length counter units at fixed intervals in either 4-step or 5-step mode, plus the nonlinear mixer that combines all channels.**

## 🎯 Intuition
**The Core Idea:** The frame sequencer is the APU's conductor — it doesn't produce sound itself but beats time at ~240 Hz, telling each channel's envelope, sweep, and length counter when to tick forward.
**Analogy:** The APU is a DJ with a mixing board. The frame sequencer is the DJ's metronome — it keeps all the effects (volume fades, pitch sweeps, note durations) synchronized. In 4-step mode, the metronome has 4 beats per cycle with an alarm (IRQ) on beat 4. In 5-step mode, it has 5 beats and no alarm. The mixer is the DJ's final output fader, combining all channels with nonlinear blending that makes loud channels slightly dampen quiet ones.
**Why It Matters:** Without the frame sequencer, envelopes won't decay, sweep units won't bend pitch, and length counters won't silence expired notes. The mixer's nonlinear behavior affects audio quality — linear mixing sounds noticeably different from hardware.

---

## ⚙️ Core Mechanics
### How It Works
The APU frame sequencer is a timer that clocks the envelope, sweep, and length counter units at fixed intervals. It operates in one of two modes selected by writing to register 0x4017.

### Key Specifications

**4-Step Mode (Mode 0)**

| Step | Cycle | Action | IRQ |
|------|-------|--------|-----|
| 1 | 7457 | Envelope, linear counter | - |
| 2 | 14913 | Envelope, linear counter, length, sweep | - |
| 3 | 22371 | Envelope, linear counter | - |
| 4 | 29829 | Envelope, linear counter, length, sweep | Yes |

**5-Step Mode (Mode 1)**

| Step | Cycle | Action | IRQ |
|------|-------|--------|-----|
| 1 | 7457 | Envelope, linear counter | - |
| 2 | 14913 | Envelope, linear counter, length, sweep | - |
| 3 | 22371 | Envelope, linear counter | - |
| 4 | 29829 | - | - |
| 5 | 37281 | Envelope, linear counter, length, sweep | Never |

### Key Facts
- IRQ fires at step 4 in 4-step mode if not inhibited; rate: ~240 Hz for envelope, ~120 Hz for length/sweep
- 5-step mode never generates IRQ; rate slightly different due to extra step
- **Mixer** combines all 5 channels:
  - Pulse channels mixed through a nonlinear lookup table
  - Triangle, noise, and DMC mixed through a separate nonlinear table
  - Final output approximated as: `pulse_out + tnd_out`
- The nonlinear mixing means increasing one channel's volume slightly decreases others — accurately modeling the NES's resistor-based DAC

---

## 🔬 Deep Dive
### Hardware Behavior Details
**Mode Switch Timing:** Writing to 0x4017 to change mode has immediate effects — if switching to 5-step mode, the envelope/length/sweep are clocked immediately on the write. This can cause audible pops if not handled correctly.

**IRQ Behavior:** In 4-step mode, the frame IRQ flag is set at step 4 and remains set until acknowledged by reading 0x4015 or writing to 0x4017. If not acknowledged, it continuously asserts the IRQ line.

**Half-Frame and Quarter-Frame:** The emulation community refers to envelope/linear counter ticks as "quarter-frame" events and length/sweep ticks as "half-frame" events, reflecting their relative frequencies.

### Common Emulation Pitfalls
1. **Not implementing both modes** — If you only implement 4-step mode, games that use 5-step mode (to avoid the IRQ) will have wrong envelope/sweep timing and potentially spurious IRQ fires
2. **Linear vs nonlinear mixing** — Using simple addition for channel mixing sounds notably different from hardware; the nonlinear lookup tables produce the characteristic NES audio warmth
3. **Forgetting the immediate clock on mode switch** — When switching to 5-step mode, failing to immediately clock the half-frame units causes a subtle timing offset in envelope and sweep behavior

### Reference Implementations
OxideNES `apu.rs` implements the frame sequencer with separate counters for 4-step and 5-step modes. The `write_ctrl()` method handles mode switching. `channel_output()` mixes all channels with linear approximation.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. At what rate do envelopes tick in 4-step mode, and at what rate do length counters tick?
2. What is the key difference between 4-step and 5-step mode besides the number of steps?
3. Why does nonlinear mixing cause one channel's volume increase to slightly decrease other channels?

### Core Problems
1. **Implement the frame sequencer:** Write a tick function that tracks the current cycle, triggers the correct combination of envelope/linear counter/length/sweep clocks at the right cycle counts, and fires IRQ in 4-step mode.
2. **Implement the nonlinear mixer:** Using the formulas `pulse_out = 95.88 / (8128 / (pulse1 + pulse2) + 100)` and `tnd_out = 159.79 / (1 / (triangle/8227 + noise/12241 + dmc/22638) + 100)`, build lookup tables for the mixer output.

### Challenge
**Mode switch race condition:** A game writes 0x40 (5-step mode, IRQ inhibit) to 0x4017 at the exact cycle when the 4-step mode's step 4 IRQ would fire. Does the IRQ fire or get suppressed? Implement the cycle-exact interaction and determine whether the old mode's IRQ takes effect before the mode switch, or whether the new mode suppresses it.

---

*See also:* [[Pulse Channels]], [[Triangle and Noise Channels]], [[DMC — Delta Modulation Channel]], [[APU — Audio Processing Unit Overview]]

## References
→ [[Sources Index]]
