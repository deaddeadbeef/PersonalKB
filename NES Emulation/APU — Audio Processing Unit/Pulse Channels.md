---
tags: [nes, wiki]
up: "[[APU — Audio Processing Unit Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# Pulse Channels

> **The two square wave channels that form the melodic backbone of NES audio, with configurable duty cycle, volume envelope, frequency sweep, and length counter.**

## 🎯 Intuition
**The Core Idea:** Each pulse channel generates a rectangular wave at a programmable frequency and duty cycle — the duty cycle shapes the timbre from thin and reedy (12.5%) to full and hollow (50%), while the envelope and sweep units add dynamic volume fades and pitch bends.
**Analogy:** Each pulse channel is like a DJ's synthesizer keyboard: the timer sets the pitch (which note), the duty cycle selects the tone quality (like switching between instrument sounds), the envelope is an auto-fader that gradually reduces volume after each note, and the sweep unit is a pitch bend wheel that slides the note up or down over time.
**Why It Matters:** Pulse channels carry the main melody and harmony in nearly every NES game. The subtle difference between Pulse 1 and Pulse 2's sweep behavior is a common emulation bug that causes wrong pitch bends, and incorrect envelope timing makes notes sound flat or robotic.

---

## ⚙️ Core Mechanics
### How It Works
The NES has two nearly identical pulse (square wave) channels. Each produces a rectangular wave with configurable duty cycle, frequency sweep, volume envelope, and length counter.

### Key Specifications

**Duty Cycles**

| Duty | Waveform | Use |
|------|----------|-----|
| 12.5% | _X______ | Thin, reedy sound |
| 25% | _XX_____ | Common melody tone |
| 50% | _XXXX___ | Hollow, full sound |
| 75% | X__XXXXX | Same as 25% inverted |

### Key Facts
- **Timer (Frequency):** An 11-bit timer period sets the frequency: `f = CPU_CLOCK / (16 × (period + 1))`. Range: ~54 Hz to ~12.4 kHz
- **Envelope (Volume):** A 4-bit volume with optional decay. In decay mode, volume starts at 15 and decreases to 0 at envelope rate, optionally looping
- **Sweep Unit:** Shifts the timer period up or down over time, creating pitch slides. Pulse 1 and Pulse 2 have slightly different sweep behavior (Pulse 1 uses one's complement for downward sweep)
- **Length Counter:** Counts down and silences the channel when it reaches zero. Used for note duration control. Can be halted by the halt flag

---

## 🔬 Deep Dive
### Hardware Behavior Details
**Pulse 1 vs Pulse 2 Sweep Difference:** When the sweep unit decreases the period (upward pitch sweep), Pulse 1 uses one's complement (inverts all bits, which is equivalent to negating and subtracting 1), while Pulse 2 uses two's complement (standard negation). This means Pulse 1's downward sweep produces a slightly different target period. At period=0, Pulse 1's sweep to negative wraps differently than Pulse 2's.

**Sweep Muting:** If the target period (after sweep adjustment) would be less than 8 or greater than 0x7FF, the channel is silenced regardless of whether the sweep is actually active. This muting check happens continuously, not just when the sweep shifts.

**Duty Cycle Sequence:** The duty cycle is implemented as an 8-step sequence. The current position in the sequence is maintained and stepped each timer cycle. The duty value selects which of four predefined 8-bit patterns to use.

### Common Emulation Pitfalls
1. **Using the same sweep formula for both channels** — The one's complement vs two's complement difference between Pulse 1 and Pulse 2 is subtle but audible; games like Castlevania have music that sounds wrong if this is not implemented
2. **Not implementing sweep muting** — Even when the sweep unit is disabled, the target period check still mutes the channel if the period would be out of range. Missing this causes notes to play when they should be silent
3. **Envelope ticking at wrong rate** — The envelope is clocked by the frame sequencer's quarter-frame signal (~240 Hz). If you clock it per CPU cycle or per APU cycle, volumes will decay thousands of times too fast

### Reference Implementations
The OxideNES `Pulse` struct in `apu.rs` contains timer, duty_cycle, envelope, sweep, and length_counter fields. Sweep difference between Pulse 1 and Pulse 2 is handled by a `channel_id` parameter.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What frequency does a pulse channel produce with a timer period of 0x0FE (254)?
2. Why does 75% duty sound identical to 25% duty (but inverted)?
3. What happens to the pulse channel output when the length counter reaches zero?

### Core Problems
1. **Implement the pulse channel timer:** Write the timer that counts down from the period value, advancing the duty cycle sequence position each time it reaches zero, and outputting 0 or 1 based on the current duty cycle pattern position.
2. **Implement the sweep unit:** Write the sweep logic that periodically shifts the timer period by a configurable amount in a configurable direction, with the Pulse 1 vs Pulse 2 negation difference and the muting check on the target period.

### Challenge
**Sweep edge case:** Set Pulse 1's period to 0x001 with sweep enabled, shift amount 1, and downward direction. Calculate the target period using one's complement negation. Is the channel muted by the target period check? Now do the same for Pulse 2 using two's complement. Do both channels produce the same result? Show the exact bit math for each.

---

*See also:* [[Triangle and Noise Channels]], [[APU Frame Sequencer]], [[DMC — Delta Modulation Channel]], [[APU — Audio Processing Unit Overview]]

## References
→ [[NES Emulation/Sources/Sources Index|Sources Index]]
