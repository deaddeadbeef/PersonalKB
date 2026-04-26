---
tags: [nes, wiki]
up: "[[NES Hardware Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# NES Technical Specifications

> **The NES is defined by hard numbers: clock rates, frame geometry, memory sizes, and audio channels that become literal emulator constants.**

## 🎯 Intuition
**The Core Idea:** The NES has a fixed hardware envelope: 1.789773 MHz CPU, 256×240 output, 262 scanlines, 5 audio channels, and 2 KB of RAM.
**Analogy:** It is like a car's spec sheet: every number constrains what the machine can do and tells you what the engineer must build around.
**Why It Matters:** These are not just trivia numbers; they become the constants hard-coded into emulator timing, rendering, and memory behavior.

---

## ⚙️ Core Mechanics
### How It Works
The technical specifications define the console's computational budget, display cadence, and sound-generation model. Differences between NTSC and PAL also matter because timing, frame rate, and scanline counts are not identical across regions.

### Key Specifications

| Parameter | NTSC | PAL |
|-----------|------|-----|
| Clock Speed | 1.789773 MHz | 1.662607 MHz |
| Instruction Set | MOS 6502 (no BCD) | Same |
| Registers | A, X, Y, SP, PC, P | Same |
| RAM | 2 KB (mirrored to 8 KB) | Same |

| Parameter | NTSC | PAL |
|-----------|------|-----|
| Resolution | 256 x 240 pixels | 256 x 240 |
| Scanlines | 262 per frame | 312 per frame |
| Dots per scanline | 341 | 341 |
| Frame rate | 60.0988 Hz | 50.007 Hz |
| Colors | 52 unique (64 entries) | Same |
| Sprites | 64 total, 8 per scanline | Same |
| VRAM | 2 KB nametable RAM | Same |
| OAM | 256 bytes (64 x 4) | Same |

| Channel | Type | Notes |
|---------|------|-------|
| Pulse 1 | Square wave | 4 duty cycles, sweep, envelope |
| Pulse 2 | Square wave | Same as Pulse 1 |
| Triangle | Triangle wave | 32-step, no volume control |
| Noise | Pseudo-random | 16 periods, short/long mode |
| DMC | Delta modulation | 1-bit delta PCM samples |

### Key Facts
- The CPU is a Ricoh 2A03 with a MOS 6502-style instruction set and no BCD mode.
- The PPU outputs 256 × 240 pixels and advances 341 dots per scanline.
- NTSC uses 262 scanlines at 60.0988 Hz; PAL uses 312 scanlines at 50.007 Hz.
- The APU provides five channels: two pulse, one triangle, one noise, and one DMC.

---

## 🔬 Deep Dive
### NTSC vs PAL
NTSC and PAL systems differ in CPU clock speed, scanline count, and frame rate. NTSC runs at 1.789773 MHz with 262 scanlines per frame and a frame rate of 60.0988 Hz. PAL runs at 1.662607 MHz with 312 scanlines per frame and a frame rate of 50.007 Hz. An emulator that hardcodes only one region's constants will get game speed, audio pitch, interrupt cadence, and video timing wrong on the other.

### Why "52 unique colors" but "64 entries"?
The PPU exposes a palette space with 64 entries, but only 52 of those correspond to unique visible colors. That distinction matters when documenting the machine because software and hardware interfaces still talk in terms of 64-entry palette addressing even though the actual set of distinct colors is smaller.

### Audio Implications
The five APU channels are not interchangeable. The triangle channel is 32-step and has no volume control. The noise channel is pseudo-random with 16 periods and short/long mode behavior. The DMC channel plays 1-bit delta PCM samples. Accurate emulation requires preserving those differences instead of treating the APU as a generic mixer.

### Reference Implementations
In emulator code, these tables become constants for CPU frequency, PPU geometry, sprite limits, OAM sizing, and audio-channel behavior. OxideNES-style timing math depends directly on values such as 1.789773 MHz, 341 dots per scanline, and 262 scanlines per frame.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. How many PPU dots are in one NTSC frame if there are 341 dots per scanline and 262 scanlines?
2. What does it mean to say the PPU has 64 palette entries but only 52 unique colors?
3. Which APU channel has no volume control?

### Core Problems
1. Explain why PAL timing cannot be emulated correctly by changing only the frame rate and leaving the CPU clock untouched.
2. Trace how the 2 KB RAM mirrored to 8 KB affects CPU memory-map handling.

### Challenge
List the emulator constants you would define first for CPU timing, PPU timing, RAM mirroring, sprite limits, and APU channels, and explain which bugs each constant prevents.

---

*See also:* [[NES Console Architecture]], [[NES History and Legacy]], [[NES vs Other 8-bit Consoles]], [[NES Hardware Overview]]

## References
→ [[Sources Index]]
