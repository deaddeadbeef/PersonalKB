---
tags: [nes, wiki]
up: "[[APU — Audio Processing Unit Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# Triangle and Noise Channels

> **The triangle channel's volume-less 32-step waveform for bass and melody, and the noise channel's LFSR-based pseudo-random generator for percussion and effects.**

## 🎯 Intuition
**The Core Idea:** The triangle channel produces a smooth, pure tone (no volume control — it's either on or off) perfect for bass lines, while the noise channel generates hissing or buzzing using a shift register that produces pseudo-random patterns — together they form the rhythm section of NES audio.
**Analogy:** In the DJ's setup, the triangle channel is like a theremin — a smooth, unwavering tone with no volume knob, you can only change its pitch or turn it completely off. The noise channel is like a drum machine with two modes: "white noise" mode (hi-hats, cymbals — the LFSR's long 32,767-step loop) and "metallic" mode (snares with a buzzy ring — the short 93-step loop). Neither has the pulse channel's fancy volume fader.
**Why It Matters:** The triangle's lack of volume control means games use creative workarounds (rapid toggling, ultrasonic frequencies) for "volume" effects — your emulator must handle these correctly. The noise LFSR is simple to implement but the two feedback modes (long vs short) produce dramatically different sounds.

---

## ⚙️ Core Mechanics
### How It Works

**Triangle Channel:** Produces a 32-step triangle wave with no volume control — it is either on at full volume or silent. This gives it a distinctive pure tone, commonly used for bass lines and melodic fills.

**Noise Channel:** Generates pseudo-random noise using a 15-bit Linear Feedback Shift Register (LFSR) with two selectable feedback tap configurations.

### Key Specifications

**Triangle Components:**
- **Timer:** 11-bit period, frequency = CPU_CLOCK / (32 × (period + 1))
- **Linear counter:** Separate from length counter; counts down and silences when zero
- **Length counter:** Standard length counter for note duration
- **Sequence:** Steps through 32 values: 15, 14, 13, ..., 1, 0, 0, 1, ..., 13, 14, 15

**Noise LFSR:**
- 15-bit shift register
- Feedback tapped from bits 0 and 1 (long mode) or bits 0 and 6 (short mode)
- **Long mode:** 32,767-step sequence — white noise
- **Short mode:** 93-step sequence — metallic, buzzy tone

**Noise Components:**
- **Timer:** 4-bit index into lookup table (16 preset periods)
- **Envelope:** Same as pulse channels (4-bit with decay)
- **Length counter:** Standard length counter
- **Mode flag:** Short (metallic) vs long (white noise)

### Key Facts
- **Triangle Quirk — No Volume Control:** Unlike pulse channels, the triangle has no envelope. Games achieve "volume" effects by rapidly toggling the channel on/off or using very high frequencies (inaudible, producing effective silence)
- **Noise Timer Periods:** 16 preset periods selected via 4-bit index; each produces a different noise pitch
- The triangle channel's timer runs at CPU clock rate, but the sequence advances at half that rate (divided by 32 steps)

---

## 🔬 Deep Dive
### Hardware Behavior Details
**Triangle Pop/Click:** When the triangle channel is silenced (by length counter or linear counter reaching zero), it freezes at its current position in the 32-step sequence. If it freezes at a non-zero value, re-enabling it can cause an audible pop because the output jumps. Some emulators mitigate this with audio filtering.

**Triangle Ultrasonic Silencing:** Games set the triangle's timer period to very low values (0 or 1) to produce frequencies above human hearing (~894 kHz with period 0). This effectively "silences" the channel while keeping the length counter active. Emulators should handle this to avoid aliasing artifacts.

**Noise LFSR Feedback:** The feedback bit is computed as `XOR(bit 0, bit N)` where N is 1 (long mode) or 6 (short mode). The result is placed in bit 14 (the top of the 15-bit register) after shifting right by 1. Output is bit 0 of the register — when it's 1, the channel is silent; when it's 0, the envelope volume passes through.

**Noise Output Inversion:** The noise channel outputs sound when LFSR bit 0 is 0 (not 1). This is a common source of confusion — the shift register's low bit acts as a gate where 0 = "pass audio" and 1 = "silence."

### Common Emulation Pitfalls
1. **Wrong LFSR feedback taps** — Using bits 0 and 1 for both modes (forgetting bit 6 for short mode) makes all noise sound like white noise, losing the metallic/buzzy percussion sounds
2. **Triangle volume at wrong level** — The triangle outputs values 0-15 directly (no envelope). If you accidentally scale it to 0-1 or apply an envelope, the triangle will be too quiet or too loud in the mix
3. **Linear counter vs length counter confusion** — The triangle has both, and they operate independently. The linear counter is reloaded on specific frame sequencer events; mixing up the two will produce wrong note durations

### Reference Implementations
OxideNES `apu.rs` implements `Triangle` and `Noise` structs. The triangle steps through its 32-value sequence. The noise LFSR uses XOR feedback: `bit = (shift & 1) ^ ((shift >> mode_bit) & 1)`.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why does the triangle channel have a linear counter in addition to a length counter?
2. In noise short mode (93-step), why does the noise sound metallic instead of random?
3. How do NES games simulate "quiet" triangle when the channel has no volume control?

### Core Problems
1. **Implement the triangle channel:** Write the 32-step sequence generator with timer, linear counter, and length counter. Output the correct amplitude value (0-15) at each step, handling the freeze behavior when counters expire.
2. **Implement the noise LFSR:** Write the 15-bit shift register with selectable feedback taps (bit 1 for long mode, bit 6 for short mode). Step it at the rate determined by the 4-bit timer index, and output 0 or envelope volume based on bit 0.

### Challenge
**Noise mode audio verification:** Generate 93 output samples from the noise LFSR starting from the initial value of 0x0001 in short mode (feedback taps: bits 0 and 6). Verify that the sequence repeats after exactly 93 steps. Then switch to long mode and verify the sequence length is 32,767. Explain mathematically why the short mode produces exactly 93 steps (hint: the polynomial $x^{15}$ + $x^{7}$ + 1 factors differently than $x^{15}$ + $x^{2}$ + 1).

---

*See also:* [[Pulse Channels]], [[APU Frame Sequencer]], [[DMC — Delta Modulation Channel]], [[APU — Audio Processing Unit Overview]]

## References
→ [[NES Emulation/Sources/Sources Index|Sources Index]]
