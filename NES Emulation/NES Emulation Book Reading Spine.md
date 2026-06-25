---
type: generated-reading-spine
tags: [nes-emulation, index, book, reading-path, navigation]
up: "[[NES Emulation/NES Emulation|NES Emulation]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# NES Emulation Book Reading Spine

Read NES emulation as a reconstruction project: hardware model first, then CPU, graphics, audio, cartridges, and emulator architecture.

This page is the reader-facing spine. Treat it like the table of contents of a good book: read the chapter openers first, then deepen through the linked articles, then use study notes and sources as appendices.

## How To Read This Topic

1. **First pass: story.** Read the prologue and each Book heading, opening only overview and learning-path pages first.
2. **Second pass: mechanism.** Return to every linked article in order and follow the concepts inside each chapter.
3. **Third pass: practice.** Use study drills, checklists, labs, plans, or recipes to prove the knowledge operationally.
4. **Fourth pass: evidence.** Use source indexes when a claim matters or when the page is time-sensitive.

## Prologue: The Machine To Rebuild

Start with the main map, learning path, and hardware overview.

- [[NES Emulation/NES Emulation|NES Emulation]] — 📚 New here? Start with the Learning Path for a guided, progressive tour.
- [[NES Emulation/NES Emulation — Learning Path|NES Emulation — Learning Path]] — A guided, progressive tour through NES hardware and emulation. Four passes, each building on the last.

## Book I: CPU, Bus, And Memory

Understand instruction execution and the address-space contract before touching pixels.

- [[NES Emulation/CPU — The 6502 Processor/CPU — The 6502 Processor Overview|CPU — The 6502 Processor Overview]] — The Ricoh 2A03 is a modified MOS 6502 running at 1.789773 MHz (NTSC). It lacks the 6502's BCD (Binary Coded Decimal) mode but integrates the APU on t...
- [[NES Emulation/CPU — The 6502 Processor/6502 Addressing Modes|6502 Addressing Modes]] — The 13 ways the 6502 CPU locates data in memory, from simple register operations to complex indirect pointer lookups.
- [[NES Emulation/CPU — The 6502 Processor/6502 Instruction Set|6502 Instruction Set]] — The complete set of 56 official opcodes (plus undocumented extras) that drive the NES CPU, organized by function.
- [[NES Emulation/CPU — The 6502 Processor/6502 Registers and Status Flags|6502 Registers and Status Flags]] — The 6502's six registers and 7-bit status word that form the complete internal state of the NES CPU.
- [[NES Emulation/CPU — The 6502 Processor/CPU Cycle Accuracy and Timing|CPU Cycle Accuracy and Timing]] — How every CPU cycle maps to exactly 3 PPU dots, and why getting this ratio wrong breaks real NES games.
- [[NES Emulation/CPU — The 6502 Processor/Interrupts — NMI, IRQ, and Reset|Interrupts — NMI, IRQ, and Reset]] — The three hardware signals that preempt normal CPU execution: Reset initializes, NMI syncs with the PPU, and IRQ enables mapper/APU-driven events.
- [[NES Emulation/Memory Map and Bus/Memory Map and Bus Overview|Memory Map and Bus Overview]] — The NES CPU sees a 64 KB address space (0x0000-0xFFFF) shared between RAM, PPU registers, APU registers, and cartridge ROM. The PPU has its own separ...
- [[NES Emulation/Memory Map and Bus/CPU Memory Map|CPU Memory Map]] — The 64 KB address space that maps the NES's 2 KB of RAM, PPU registers, APU/IO, and cartridge ROM/RAM through mirroring and bank switching.
- [[NES Emulation/Memory Map and Bus/OAM DMA|OAM DMA]] — A hardware-accelerated bulk transfer that copies 256 bytes of sprite data to the PPU's OAM, halting the CPU for 513-514 cycles.
- [[NES Emulation/Memory Map and Bus/PPU Memory Map|PPU Memory Map]] — The PPU's separate 16 KB address space containing pattern tables (tile graphics), nametables (screen layout), and palette RAM.

## Book II: Picture, Sound, And Input

Move from computation to the user-visible frame, audio stream, and controller state.

- [[NES Emulation/PPU — Picture Processing Unit/PPU — Picture Processing Unit Overview|PPU — Picture Processing Unit Overview]] — The Ricoh 2C02 (NTSC) is the NES's dedicated graphics processor. It renders 256x240 pixels at ~60 Hz by racing the electron beam across 262 scanlines...
- [[NES Emulation/PPU — Picture Processing Unit/Backgrounds and Nametables|Backgrounds and Nametables]] — How the PPU constructs the background layer from a grid of 8x8 tiles, nametable maps, attribute tables for palette selection, and pattern table graph...
- [[NES Emulation/PPU — Picture Processing Unit/PPU Registers and Timing|PPU Registers and Timing]] — The 8 memory-mapped PPU registers at 0x2000-0x2007 and their critical timing-sensitive side effects that drive NES graphics.
- [[NES Emulation/PPU — Picture Processing Unit/PPU Rendering Pipeline|PPU Rendering Pipeline]] — The dot-by-dot, scanline-by-scanline process that renders 256×240 pixels per frame using shift registers, tile fetches, and sprite evaluation.
- [[NES Emulation/PPU — Picture Processing Unit/PPU Scrolling|PPU Scrolling]] — The Loopy register mechanism (v, t, x, w) that enables hardware scrolling across a 512×480 virtual space using a dual-register pipeline.
- [[NES Emulation/PPU — Picture Processing Unit/Sprites and OAM|Sprites and OAM]] — The PPU's sprite system: 64 sprites stored in 256 bytes of OAM, with per-scanline evaluation, an 8-sprite limit, and the critical sprite 0 hit detect...
- [[NES Emulation/APU — Audio Processing Unit/APU — Audio Processing Unit Overview|APU — Audio Processing Unit Overview]] — The APU is integrated into the Ricoh 2A03 alongside the CPU. It generates audio through 5 channels: two pulse waves, one triangle wave, one noise gen...
- [[NES Emulation/APU — Audio Processing Unit/APU Frame Sequencer|APU Frame Sequencer]] — The master timer that clocks envelope, sweep, and length counter units at fixed intervals in either 4-step or 5-step mode, plus the nonlinear mixer t...
- [[NES Emulation/APU — Audio Processing Unit/DMC — Delta Modulation Channel|DMC — Delta Modulation Channel]] — The sample-playback channel that reads 1-bit delta-encoded PCM audio from ROM, stealing CPU cycles to fetch each byte.
- [[NES Emulation/APU — Audio Processing Unit/Pulse Channels|Pulse Channels]] — The two square wave channels that form the melodic backbone of NES audio, with configurable duty cycle, volume envelope, frequency sweep, and length...
- [[NES Emulation/APU — Audio Processing Unit/Triangle and Noise Channels|Triangle and Noise Channels]] — The triangle channel's volume-less 32-step waveform for bass and melody, and the noise channel's LFSR-based pseudo-random generator for percussion an...
- [[NES Emulation/Input and Controllers/Input and Controllers Overview|Input and Controllers Overview]] — The NES controller is a simple but elegant input device with a D-pad, two action buttons (A, B), and two meta buttons (Start, Select). The console co...
- [[NES Emulation/Input and Controllers/Controller Features in OxideNES|Controller Features in OxideNES]] — Bridges modern input hardware to the NES's 8-button protocol with remapping, turbo, multi-player, and TAS recording.
- [[NES Emulation/Input and Controllers/NES Joypad Protocol|NES Joypad Protocol]] — The serial shift-register protocol that reads 8 button states through a strobe-latch-and-shift sequence at $4016/$4017.

## Book III: Cartridges And Mappers

Read cartridges as hardware extensions that change the rules of the base machine.

- [[NES Emulation/Cartridges and Mappers/Cartridges and Mappers Overview|Cartridges and Mappers Overview]] — NES cartridges contain ROM chips and optional mapper hardware that extends the console's capabilities far beyond its base specifications. Mappers per...
- [[NES Emulation/Cartridges and Mappers/Advanced Mappers|Advanced Mappers]] — Mapper ICs that go beyond simple bank switching — adding audio, IRQs, multipliers, and RAM subsystems to the cartridge.
- [[NES Emulation/Cartridges and Mappers/Bank Switching Explained|Bank Switching Explained]] — How mapper hardware maps ROM segments larger than 32 KB into the CPU's limited address space by swapping banks.
- [[NES Emulation/Cartridges and Mappers/Common Mappers|Common Mappers]] — Five mapper types that cover ~85% of all licensed NES games, from the trivial NROM to the versatile MMC3.
- [[NES Emulation/Cartridges and Mappers/Expansion Audio|Expansion Audio]] — Cartridge sound chips that add extra channels beyond the NES's standard 5 APU channels, producing the console's richest music.
- [[NES Emulation/Cartridges and Mappers/iNES ROM Format|iNES ROM Format]] — The 16-byte header format that describes a ROM's hardware configuration — the first thing an emulator parses when loading any game.

## Book IV: Emulator Architecture And Polish

Turn component knowledge into a working emulator with timing, presentation, and tooling.

- [[NES Emulation/Emulator Architecture/Emulator Architecture Overview|Emulator Architecture Overview]] — OxideNES is a cycle-accurate NES emulator written in Rust, designed for both accuracy and performance. The architecture follows a modular design with...
- [[NES Emulation/Emulator Architecture/Main Loop and Cycle Ratios|Main Loop and Cycle Ratios]] — OxideNES keeps CPU, PPU, and APU in lock-step so the emulator advances at exact NES hardware timing ratios.
- [[NES Emulation/Emulator Architecture/OxideNES Module Architecture|OxideNES Module Architecture]] — OxideNES is organized around a central Bus that coordinates core chip emulators and optional plugin-style subsystems.
- [[NES Emulation/Emulator Architecture/Performance Optimization in OxideNES|Performance Optimization in OxideNES]] — OxideNES reaches real-time speed by optimizing the hottest paths while preserving cycle-accurate behavior.
- [[NES Emulation/Emulator Architecture/Save States and Rewind|Save States and Rewind]] — Save states capture the whole machine at one moment, while rewind keeps a rolling history of snapshots for short-range time travel.
- [[NES Emulation/CRT Simulation/CRT Simulation Overview|CRT Simulation Overview]] — OxideNES features a comprehensive CRT simulation pipeline that transforms the raw 256x240 NES output into a convincing vintage television image. The...
- [[NES Emulation/CRT Simulation/Barrel Distortion and Shadow Mask|Barrel Distortion and Shadow Mask]] — Barrel distortion curves the image like CRT glass, while shadow mask patterns recreate the visible phosphor structure.
- [[NES Emulation/CRT Simulation/CRT Rendering Pipeline|CRT Rendering Pipeline]] — A seven-stage pipeline transforms the 256×240 NES framebuffer into a stylized CRT image, and the stage order determines both fidelity and performance.
- [[NES Emulation/CRT Simulation/Glass Reflections and Chromatic Aberration|Glass Reflections and Chromatic Aberration]] — Glass reflections add ambient ghosting on the CRT surface, and chromatic aberration adds subtle RGB fringing near the edges.
- [[NES Emulation/CRT Simulation/Scanline and Phosphor Effects|Scanline and Phosphor Effects]] — Scanlines, phosphor warmth, bloom, and vignette recreate the glow, warmth, and edge falloff that make CRT images feel distinct.
- [[NES Emulation/Extended Features/Extended Features Overview|Extended Features Overview]] — Beyond core NES emulation, OxideNES includes several modern quality-of-life features that enhance the retro gaming experience.
- [[NES Emulation/Extended Features/Achievement System|Achievement System]] — OxideNES evaluates RetroAchievements-compatible conditions against CPU RAM every frame to unlock achievements for a specific ROM.
- [[NES Emulation/Extended Features/Input Recording and TAS|Input Recording and TAS]] — OxideNES records frame-perfect controller input for replay, TAS workflows, and cross-emulator export.
- [[NES Emulation/Extended Features/Lua Scripting Engine|Lua Scripting Engine]] — OxideNES embeds a sandboxed Lua 5.4 VM so scripts can inspect memory and draw overlays without changing emulator source code.
- [[NES Emulation/Extended Features/Netplay — UDP Multiplayer|Netplay — UDP Multiplayer]] — OxideNES uses peer-to-peer UDP lockstep networking so both players exchange one frame of input before advancing emulation together.

## Appendices: Practice And Sources

Use drills, cheatsheets, and source registries to test the emulator model.

- [[NES Emulation/Study/NES Emulation Study Index|NES Emulation — Study Index]] — 1. Read canonical pages for deep understanding
- [[NES Emulation/Study/Cheatsheet — NES Memory Maps and Registers|Cheatsheet — NES Memory Maps and Registers]] — Quick reference for NES address spaces and register layouts.
- [[NES Emulation/Study/Review Drill — 6502 CPU and Addressing|Review Drill — 6502 CPU and Addressing]] — A, X, Y (8-bit each), SP (8-bit, stack pointer into page -), PC (16-bit, program counter), P (8-bit, status flags: N V - B D I Z C)
- [[NES Emulation/Study/Review Drill — APU Audio Channels|Review Drill — APU Audio Channels]] — Pulse 1 (square, 4 duty cycles), Pulse 2 (square, 4 duty cycles), Triangle (32-step triangle wave), Noise (LFSR pseudo-random), DMC (1-bit delta-enco...
- [[NES Emulation/Study/Review Drill — Emulator Architecture|Review Drill — Emulator Architecture]] — 3:1. The bus clock() method calls ppu.tick() three times, then cpu.tick() once (unless DMA-stalled), then apu.tick() once. This interleaving ensures...
- [[NES Emulation/Study/Review Drill — Mappers and Bank Switching|Review Drill — Mappers and Bank Switching]] — The CPU can only address 32 KB PRG ROM and the PPU 8 KB CHR. Games exceeding these limits use mapper hardware on the cartridge to dynamically remap (...
- [[NES Emulation/Study/Review Drill — PPU Rendering Pipeline|Review Drill — PPU Rendering Pipeline]] — 262 total: pre-render (-1/261), visible (0-239), post-render (240), VBlank (241-260). Each scanline is 341 PPU cycles.
- [[NES Emulation/Sources/Sources Index|Sources Index — NES Emulation]]

## Appendix: Remaining Reader-Facing Notes

These notes are part of the topic corpus but do not belong cleanly to the main narrative chapters yet.

- [[NES Emulation/NES Hardware Overview/NES Hardware Overview|NES Hardware Overview]] — The Nintendo Entertainment System (1983 in Japan as Famicom, 1985 in North America) defined console gaming for a generation. Understanding its hardwa...
- [[NES Emulation/NES Hardware Overview/NES Console Architecture|NES Console Architecture]] — The NES is a three-chip system built around separate CPU and PPU buses, with the cartridge bridging both worlds.
- [[NES Emulation/NES Hardware Overview/NES History and Legacy|NES History and Legacy]] — The NES reshaped the game industry, defined long-lived console conventions, and still inspires modern emulation work.
- [[NES Emulation/NES Hardware Overview/NES Technical Specifications|NES Technical Specifications]] — The NES is defined by hard numbers: clock rates, frame geometry, memory sizes, and audio channels that become literal emulator constants.
- [[NES Emulation/NES Hardware Overview/NES vs Other 8-bit Consoles|NES vs Other 8-bit Consoles]] — The NES succeeded less by winning every raw spec and more by combining balanced hardware with an unusually powerful cartridge ecosystem.

## Coverage

- Reader-facing articles linked here: 60
- Protected raw, chunk, template, query, audio, and operations folders are intentionally not expanded here.
- The root vault index remains the exhaustive generated listing across every topic.

## References

- [[NES Emulation/NES Emulation|NES Emulation]]
- [[NES Emulation/Sources/Sources Index|Sources Index — NES Emulation]]
