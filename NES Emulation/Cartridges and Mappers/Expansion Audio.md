---
tags: [nes, wiki]
up: "[[Cartridges and Mappers Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---

# Expansion Audio

> **Cartridge sound chips that add extra channels beyond the NES's standard 5 APU channels, producing the console's richest music.**

## 🎯 Intuition
**The Core Idea:** Some NES cartridges contain extra sound chips that add channels beyond the standard 5, enabling richer and more complex music.
**Analogy:** Like plugging a synthesizer into a guitar amp — the cartridge brings its own instrument that plays alongside the console's built-in sounds.
**Why It Matters:** Expansion audio produced the best NES music ever made. Proper mixing of expansion channels with the base APU is a key emulation challenge, and getting it wrong is immediately audible.

---

## ⚙️ Core Mechanics
### How It Works
Some NES cartridges contain additional sound hardware that augments the standard 5 APU channels. The cartridge generates additional audio samples that are mixed with the standard APU output. On the Famicom, this was done through a dedicated audio pin on the cartridge connector. The NES (Western version) lacks this pin, so expansion audio only works through emulation.

### Key Specifications

| Chip | Mapper | Channels | Type | Notable Game |
|------|--------|----------|------|-------------|
| VRC6 | 024/026 | 3 | 2 pulse + 1 sawtooth | Akumajou Densetsu |
| Namco 163 | 019 | 1–8 | Wavetable synthesis | Rolling Thunder |
| FME7 (5B) | 069 | 3 | Tone + noise + envelope | Gimmick! |
| VRC7 | 085 | 6 | FM synthesis (OPLL) | Lagrange Point |

### Key Facts
- Expansion chips were more common in Japan (Famicom) due to the Famicom's cartridge audio mixing pin
- The Western NES lacks the audio mixing pin, so expansion audio was not available on original hardware outside Japan
- VRC6 adds 2 pulse channels (8 duty-cycle options each) plus 1 sawtooth channel (5-bit DAC)
- Namco 163 supports 1–8 wavetable channels sharing 128 bytes of wave RAM
- FME7 provides 3 AY-3-8910-compatible tone channels with noise and envelope
- VRC7 offers 6 FM synthesis channels (YM2413 subset) — the most musically sophisticated NES expansion audio

---

## 🔬 Deep Dive
### Famicom vs. NES Hardware
The Famicom's cartridge connector includes pin 46 (audio out) and pin 45 (audio in), forming a loop through the cartridge. Expansion audio is mixed in analog by the cartridge hardware before returning to the console's amplifier. The NES (Western) redesigned the cartridge connector and omitted these audio pins, so no retail NES game uses expansion audio — it exists only in Japanese Famicom releases and emulators.

### Mixing Behavior
On real Famicom hardware, expansion audio is mixed in analog with the internal APU output. The resulting volume balance depends on resistor values on the cartridge PCB, which vary by manufacturer. Emulators approximate this by digitally summing the expansion output with the APU output, applying per-chip volume scaling to match the original hardware balance.

### Per-Chip Details
- **VRC6:** Two pulse channels each have 4-bit volume, 12-bit period, and 8 selectable duty cycles (1/16 through 8/16). The sawtooth accumulates at a programmable rate with 5-bit DAC output.
- **Namco 163:** Channels share 128 bytes of internal wave RAM. More active channels = shorter waveforms per channel = lower quality. The chip cycles through active channels in round-robin fashion.
- **FME7 (5B):** AY-3-8910-compatible with 3 tone generators, 1 noise generator, and hardware envelope. Accessed through an address/data register pair.
- **VRC7:** YM2413-compatible FM synthesis with 15 built-in instrument patches plus 1 custom patch. Each of 6 channels has a 2-operator FM voice.

### Reference Implementations
OxideNES mixes expansion audio by summing the mapper's `audio_output()` with the standard APU output. Each expansion chip's volume is balanced to approximate the analog mixing on real Famicom hardware.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why was expansion audio common in Japan but absent from Western NES games?
2. How many expansion audio chips are supported in OxideNES, and which one has the most channels?
3. What makes mixing expansion audio with the base APU a challenge for emulators?

### Core Problems
1. **VRC6 Pulse Channel:** Implement a VRC6 pulse channel with configurable duty cycle (8 options), 4-bit volume, and 12-bit period timer. Verify that changing the duty cycle alters the waveform shape while keeping the same frequency.
2. **Audio Mixing:** Write a mixing function that combines the standard APU output with one expansion chip's output. Apply a volume scaling factor to balance the expansion audio. Test with VRC6 and verify the mixed signal contains both the APU and expansion components.

### Challenge
**Namco 163 Wavetable Engine:** Implement the full Namco 163 audio engine with configurable channel count. Each channel reads its waveform from shared 128-byte wave RAM. Demonstrate correct round-robin channel cycling and verify that enabling more channels reduces the available waveform length per channel.

---

*See also:* [[Advanced Mappers]], [[Common Mappers]], [[Cartridges and Mappers Overview]]

## References
→ [[NES Emulation/Sources/Sources Index|Sources Index]]
