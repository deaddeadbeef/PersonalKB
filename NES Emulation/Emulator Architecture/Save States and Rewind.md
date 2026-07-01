---
tags: [nes, wiki]
up: "[[Emulator Architecture Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# Save States and Rewind

> **Save states capture the whole machine at one moment, while rewind keeps a rolling history of snapshots for short-range time travel.**

## 🎯 Intuition
**The Core Idea:** A save state is a complete machine snapshot, and rewind is a circular buffer of those snapshots.
**Analogy:** A save state is a bookmark; rewind is a DVR that lets you scrub backward through recent history.
**Why It Matters:** These are among the most-used quality-of-life features in an emulator, and they only work if every component serializes and restores correctly.

---

## ⚙️ Core Mechanics
### How It Works
OxideNES supports 4 save state slots with thumbnail previews:
- **F5:** Quick save to current slot
- **F9:** Quick load from current slot

Each component implements `save_state()`/`load_state()` methods that serialize their complete internal state. The Bus orchestrates full system snapshot creation.

Rewind extends the same idea by taking state snapshots repeatedly instead of only on explicit user request. Holding Backspace rewinds gameplay with a VHS tape visual effect.

Games with battery-backed SRAM persist save data separately from transient save states.

### Key Specifications
- **State includes:** CPU registers, RAM, PPU state, APU state, mapper state, OAM
- **RewindBuffer:** Circular buffer of state snapshots captured every N frames
- **Efficient serialization:** Bulk byte serialization with pre-allocated snapshot buffers
- **Vectorization-friendly:** Uses `chunks_exact` iterator pattern for deserialization
- **Memory:** Trades RAM for functionality (~30-60 MB for several seconds of rewind)
- **Battery saves path:** `~/.nes-emulator/saves/{rom_hash}.sav`
- **Battery save load behavior:** Loaded automatically on ROM open
- **Battery save gating:** Only for mappers with `battery` flag set in ROM header

### Key Facts
- Save states and battery saves are distinct systems.
- Rewind is implemented as repeated snapshot capture, not magic reverse execution.
- Thumbnail previews make slot-based save states easier to navigate.
- The VHS effect is intentional user feedback, not just decoration.

---

## 🔬 Deep Dive
### Save State Coverage
A complete state must include CPU registers, RAM, PPU state, APU state, mapper state, and OAM. If any hardware block is omitted, a restored game can appear to work briefly and then diverge because hidden internal state was lost.

### RewindBuffer Design
The rewind system is built around a `RewindBuffer`, which is a circular buffer of snapshots captured every N frames. Using a circular structure caps memory use while still giving the user several seconds of history. Bulk byte serialization with pre-allocated snapshot buffers reduces allocation churn, and `chunks_exact` is used on deserialization to keep the code vectorization-friendly.

### VHS Effect and Memory Budget
During rewind, a visual overlay simulates VHS tape artifacts: scan lines shift and colors distort so the player gets unmistakable feedback that time is moving backward. The cost is RAM. Several seconds of rewind typically consume about 30-60 MB, which is a reasonable trade for a modern desktop emulator.

### Battery Saves
Battery-backed SRAM persists independently of save-state slots. Games such as Zelda and Final Fantasy automatically save to `~/.nes-emulator/saves/{rom_hash}.sav`, reload that data when the ROM opens, and only use the path when the ROM header indicates a mapper with the `battery` flag set.

### Reference Implementations
OxideNES uses per-component `save_state()` and `load_state()` methods, a Bus-orchestrated whole-machine snapshot, and a circular-buffer `RewindBuffer` built on bulk serialization and `chunks_exact`-friendly deserialization.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What machine components must be present in a correct save state?
2. Why is rewind implemented with a circular buffer instead of storing an unlimited history?
3. What is the UX purpose of the VHS-style rewind effect?

### Core Problems
1. Estimate rewind memory usage for 10 seconds if the implementation currently uses about 30-60 MB for several seconds of history.
2. Explain why battery-backed SRAM should not be treated as identical to a save-state slot.

### Challenge
Design a validation test that would prove `load_state()` restores not only visible screen state but also hidden timing-sensitive state in the CPU, PPU, APU, and mapper.

---

*See also:* [[OxideNES Module Architecture]], [[Main Loop and Cycle Ratios]], [[Emulator Architecture Overview]]

## References
→ [[NES Emulation/Sources/Sources Index|Sources Index]]
