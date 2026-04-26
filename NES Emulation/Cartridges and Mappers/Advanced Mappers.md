---
tags: [nes, wiki]
up: "[[Cartridges and Mappers Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Advanced Mappers

> **Mapper ICs that go beyond simple bank switching — adding audio, IRQs, multipliers, and RAM subsystems to the cartridge.**

## 🎯 Intuition
**The Core Idea:** Advanced mappers add entire subsystems (audio, IRQs, multipliers, RAM) beyond simple bank switching, turning the cartridge into a miniature co-processor board.
**Analogy:** Think of expansion packs installing new instruments and clocks into the console — each advanced mapper bolts on capabilities the base NES never had.
**Why It Matters:** These are the most complex components to emulate. Every subsystem (scanline counters, FM synthesis, hardware multiply) requires its own accurate state machine.

---

## ⚙️ Core Mechanics
### How It Works
Advanced mappers intercept CPU and PPU bus activity just like simple mappers, but they also contain additional hardware: sound generators, scanline counters, multiplier circuits, and extra RAM. The emulator must model each subsystem and clock it in sync with the CPU/PPU.

### Key Specifications

| Mapper | Chip | Extra Channels | Extra Features | Notable Games |
|--------|------|---------------|----------------|---------------|
| 5 | MMC5 | 2 pulse + PCM | Scanline counter, 8×8 multiplier, vertical split, 1 KB ExRAM | Castlevania III, Just Breed |
| 024/026 | VRC6 | 2 pulse + 1 sawtooth | Scanline IRQ counter | Akumajou Densetsu |
| 019 | Namco 163 | 1–8 wavetable | 128-byte wave RAM, scanline IRQ | Various Namco games |
| 069 | FME7 (5B) | 3 tone (AY-3-8910) | IRQ timer | Gimmick!, Batman: Return of the Joker |
| 085 | VRC7 | 6 FM synthesis (OPLL) | Most sophisticated NES expansion audio | Lagrange Point |

### Key Facts
- MMC5 is the most complex NES mapper: 8 KB PRG banking with 5 modes, 1 KB CHR banking with 4 modes, extra 1 KB internal RAM, expansion audio, scanline counter, multiplier, and vertical split mode
- VRC6 pulse channels offer 8 duty-cycle options (vs. the standard APU's 4), and the sawtooth has a 5-bit DAC
- Namco 163 shares 128 bytes of internal RAM for wave samples across all active channels — more channels means shorter, lower-quality waveforms
- FME7's 3 tone channels are AY-3-8910 compatible, supporting tone, noise, and envelope generation
- VRC7 uses a YM2413 subset for 6 FM synthesis channels — the most musically sophisticated NES expansion audio

---

## 🔬 Deep Dive
### MMC5 Subsystems
MMC5 is essentially a co-processor. Its 8 KB PRG banking (5 modes) and 1 KB CHR banking (4 modes) are already complex, but the mapper also provides:
- **ExRAM (1 KB):** Used for extended nametable attributes or as general-purpose RAM
- **Scanline counter:** Generates IRQs at configurable scanlines, clocked by PPU rendering
- **Hardware multiplier:** 8×8 unsigned multiply with instant result — games use it for math-heavy routines
- **Vertical split mode:** Splits the screen vertically with independent scroll/nametable for each half

### VRC6 Audio Detail
The two pulse channels each have a 4-bit volume DAC and 8 selectable duty cycles (1/16 through 8/16). The sawtooth channel accumulates a value at a programmable rate, producing the characteristic sawtooth wave through its 5-bit DAC output.

### Namco 163 Wavetable
Channels share 128 bytes of wave RAM. Each active channel uses a portion of this RAM for its waveform sample data. With 8 channels active, each gets only 16 bytes of sample data, reducing audio fidelity. Games carefully balance channel count against waveform quality.

### VRC7 FM Synthesis
Uses a YM2413-compatible FM synthesis core with 6 channels. 15 built-in instrument patches plus 1 user-programmable patch. Each channel has a 2-operator FM voice with configurable modulation.

### Reference Implementations
All advanced mappers are implemented in mapper.rs. Expansion audio channels implement `audio_output()` on the Mapper trait, mixed into the final audio stream by the APU.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What makes MMC5 the most complex NES mapper? List at least four subsystems it provides beyond bank switching.
2. Why does increasing the number of active Namco 163 channels reduce audio quality?
3. Which advanced mapper would you implement first if you wanted the simplest expansion audio, and why?

### Core Problems
1. **MMC5 Multiplier:** Implement the MMC5 8×8 hardware multiplier — writes to $5205/$5206 set the operands, and reads from $5205/$5206 return the 16-bit product low/high bytes. Verify with a test that multiplies 0xFF × 0xFF = 0xFE01.
2. **VRC6 Sawtooth:** Implement the VRC6 sawtooth channel. The accumulator adds a rate value every 2 CPU clocks, and the top 5 bits form the output. Reset the accumulator to 0 every 7 steps. Verify the output waveform shape.

### Challenge
**Namco 163 Channel Sharing:** Implement the Namco 163 wavetable engine with configurable channel count (1–8). Each channel reads waveform data from shared 128-byte RAM. Demonstrate that enabling all 8 channels limits each to 16-byte waveforms while a single channel can use the full 128 bytes.

---

*See also:* [[Bank Switching Explained]], [[Common Mappers]], [[Expansion Audio]], [[Cartridges and Mappers Overview]]

## References
→ [[Sources Index]]
