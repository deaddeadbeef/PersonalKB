---
tags: [nes-emulation, learning-path]
up: "[[NES Emulation/NES Emulation]]"
confidence: verified
freshness: stable
tier-coverage: [core, practice]
---
# NES Emulation — Learning Path

> A guided, progressive tour through NES hardware and emulation. Four passes, each building on the last.

## Where This Fits

| Need | Use |
|---|---|
| Read NES emulation like a book | [[NES Emulation/NES Emulation Book Reading Spine|NES Emulation Book Reading Spine]] |
| Follow a pass-based curriculum | This learning path |
| Route a bug or review target to a subsystem | [[NES Emulation/Study/NES Emulation Study Index|NES Emulation Study Index]] |
| Verify hardware behavior, timing, tests, or OxideNES-specific claims | [[NES Emulation/Sources/Sources Index|NES Emulation Sources Index]] |

Use this path when you want staged coverage of the machine. Use the book spine for the reconstruction story, and use the study index when you need a trace, test ROM, or regression proof.

## How to Use This Path

| Pass | Focus | Read | Time |
|------|-------|------|------|
| 1 — Intuition | Build mental map | 🎯 sections only | ~2 hrs |
| 2 — Core | Understand mechanics | ⚙️ sections + Warm-Up | ~8 hrs |
| 3 — Deep Dive | Master details | 🔬 sections (selective) | ~15 hrs |
| 4 — Practice | Build skill | 🏋️ sections + drills | Ongoing |

---

## Pass 1 — Intuition (~2 hours)

Read ONLY the 🎯 Intuition section of each page. Build a broad mental map of the NES and how an emulator recreates it.

### NES Hardware Overview
1. [[NES Hardware Overview]] — the console at a glance
2. [[NES Console Architecture]] — how CPU, PPU, APU, and cartridge interconnect
3. [[NES Technical Specifications]] — clock speeds, resolution, palette, memory sizes
4. [[NES History and Legacy]] — the console's place in gaming history
5. [[NES vs Other 8-bit Consoles]] — how the NES compares to competitors

### CPU — The 6502 Processor
6. [[CPU — The 6502 Processor Overview]] — the CPU hub
7. [[6502 Registers and Status Flags]] — A, X, Y, SP, PC, and the status register
8. [[6502 Addressing Modes]] — how the 6502 finds its data
9. [[6502 Instruction Set]] — the ~56 opcodes and what they do
10. [[Interrupts — NMI, IRQ, and Reset]] — how the CPU responds to external events
11. [[CPU Cycle Accuracy and Timing]] — why every cycle matters for emulation

### Memory Map and Bus
12. [[Memory Map and Bus Overview]] — the memory hub
13. [[CPU Memory Map]] — $0000–$FFFF address space layout
14. [[PPU Memory Map]] — pattern tables, nametables, palettes
15. [[OAM DMA]] — fast sprite data transfer

### PPU — Picture Processing Unit
16. [[PPU — Picture Processing Unit Overview]] — the graphics hub
17. [[PPU Registers and Timing]] — PPUCTRL, PPUMASK, PPUSTATUS, and the rendering timeline
18. [[PPU Rendering Pipeline]] — how a frame is drawn scanline by scanline
19. [[Backgrounds and Nametables]] — tile maps, attribute tables, mirroring
20. [[Sprites and OAM]] — sprite evaluation, priority, 8-sprite limit
21. [[PPU Scrolling]] — fine/coarse scroll, split-screen tricks

### APU — Audio Processing Unit
22. [[APU — Audio Processing Unit Overview]] — the audio hub
23. [[Pulse Channels]] — square-wave generators with sweep and envelope
24. [[Triangle and Noise Channels]] — triangle wave and pseudo-random noise
25. [[DMC — Delta Modulation Channel]] — sample playback via delta encoding
26. [[APU Frame Sequencer]] — timing and clocking of audio components

### Cartridges and Mappers
27. [[Cartridges and Mappers Overview]] — the cartridge hub
28. [[iNES ROM Format]] — header, PRG-ROM, CHR-ROM
29. [[Bank Switching Explained]] — how mappers extend the address space
30. [[Common Mappers]] — NROM, MMC1, UxROM, MMC3
31. [[Advanced Mappers]] — MMC5, VRC6/7, and complex mappers
32. [[Expansion Audio]] — extra sound channels from cartridge hardware

### Input and Controllers
33. [[Input and Controllers Overview]] — the input hub
34. [[NES Joypad Protocol]] — serial strobe/shift protocol
35. [[Controller Features in OxideNES]] — implementation details

### Emulator Architecture
36. [[Emulator Architecture Overview]] — the emulator-design hub
37. [[Main Loop and Cycle Ratios]] — CPU:PPU:APU synchronization
38. [[OxideNES Module Architecture]] — Rust module layout and design
39. [[Save States and Rewind]] — serialization and time-travel debugging
40. [[Performance Optimization in OxideNES]] — profiling and optimization techniques

### CRT Simulation
41. [[CRT Simulation Overview]] — the CRT-effects hub
42. [[CRT Rendering Pipeline]] — 7-stage post-processing pipeline
43. [[Scanline and Phosphor Effects]] — glow, decay, and scanline gaps
44. [[Barrel Distortion and Shadow Mask]] — geometry and subpixel structure
45. [[Glass Reflections and Chromatic Aberration]] — final polish effects

### Extended Features
46. [[Extended Features Overview]] — the extended-features hub
47. [[Netplay — UDP Multiplayer]] — rollback netcode for online play
48. [[Lua Scripting Engine]] — programmable game interaction
49. [[Achievement System]] — retro-achievements integration
50. [[Input Recording and TAS]] — tool-assisted speedrun support

---

## Pass 2 — Core Mechanics (~8 hours)

Re-read each page's ⚙️ Core Mechanics and 🏋️ Warm-Up sections. Focus on understanding *how* each component works.

### Suggested order
Follow the same sequence as Pass 1. Spend extra time on:
- **6502 addressing modes** — trace each mode through a concrete instruction
- **PPU rendering pipeline** — understand the scanline-by-scanline render process
- **Memory map** — memorize the address ranges and mirror regions
- **Mapper bank switching** — trace a bank-switch write through the mapper
- **Main loop timing** — understand 3:1 PPU:CPU cycle ratio

### Checkpoints
After this pass you should be able to:
- [ ] Map a CPU address to its physical destination (RAM, ROM, I/O register)
- [ ] Describe what happens during each PPU scanline
- [ ] Explain how NMI drives the game loop
- [ ] Trace a bank-switch operation through MMC1
- [ ] Explain how the APU frame sequencer clocks the audio channels

---

## Pass 3 — Deep Dive (selective, ~15 hours)

Read the 🔬 Deep Dive sections for the subsystems you want to master.

### Track A — CPU Deep Dive
- [[6502 Addressing Modes]] — page-crossing penalties, indirect JMP bug
- [[6502 Instruction Set]] — unofficial opcodes, decimal mode (disabled on NES)
- [[CPU Cycle Accuracy and Timing]] — per-instruction cycle counts and edge cases
- [[Interrupts — NMI, IRQ, and Reset]] — interrupt hijacking, NMI during BRK

### Track B — PPU Deep Dive
- [[PPU Rendering Pipeline]] — sprite-0 hit timing, background/sprite priority
- [[PPU Scrolling]] — loopy register model, mid-frame scroll changes
- [[Sprites and OAM]] — sprite overflow bug, OAM corruption
- [[PPU Registers and Timing]] — VRAM address latch behavior, read buffer

### Track C — Mapper Deep Dive
- [[Common Mappers]] — MMC3 scanline counter, IRQ timing
- [[Advanced Mappers]] — MMC5 extended attributes, VRC7 FM synthesis
- [[Expansion Audio]] — mixing expansion audio into the APU output

### Track D — Emulator Engineering
- [[Main Loop and Cycle Ratios]] — catch-up vs lock-step synchronization
- [[Save States and Rewind]] — delta compression, rewind buffer sizing
- [[Performance Optimization in OxideNES]] — cache-friendly memory layout
- [[CRT Rendering Pipeline]] — shader pipeline architecture

---

## Pass 4 — Practice (ongoing)

Build active-recall skill and hands-on emulator development experience.

### Drills
Use the [[NES Emulation Study Index]] for review drills and cheatsheets.

### Implementation Milestones
1. **CPU only** — pass nestest.nes (official/unofficial opcodes)
2. **CPU + PPU** — render a static nametable (Donkey Kong title screen)
3. **Scrolling** — implement PPU scrolling (Super Mario Bros level 1)
4. **Sprites** — sprite evaluation and rendering (moving characters)
5. **APU** — audio output with all five channels
6. **Mappers** — add MMC1 and MMC3 support
7. **Save states** — serialize and restore full emulator state
8. **CRT filter** — implement the 7-stage post-processing pipeline

### Reference Games
| Game | Tests |
|------|-------|
| Donkey Kong | Basic PPU, sprites, no scrolling |
| Super Mario Bros | Scrolling, sprite-0 hit, MMC mapper |
| Mega Man 2 | Complex sprites, MMC3 IRQ |
| Castlevania III | MMC5, expansion audio |
| Kirby's Adventure | MMC3, many sprites, complex scrolling |

## References

- [[NES Emulation/NES Emulation]]
- [[NES Emulation/Sources/Sources Index]]
