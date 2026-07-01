---
type: generated-reading-spine
tags: [nes-emulation, index, book, reading-path, navigation]
up: "[[NES Emulation/NES Emulation|NES Emulation]]"
confidence: verified
freshness: stable
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

- [[NES Emulation/NES Emulation|NES Emulation]] — A comprehensive knowledge base covering NES hardware theory and emulation practice, with OxideNES (a cycle-accurate Rust NES emulator) as the concrete implementation reference.
- [[NES Emulation/NES Emulation — Learning Path|NES Emulation — Learning Path]] — Pass-based learning path for NES Emulation.

## Book I: CPU, Bus, And Memory

Understand instruction execution and the address-space contract before touching pixels.

- [[NES Emulation/CPU — The 6502 Processor/CPU — The 6502 Processor Overview|CPU — The 6502 Processor Overview]] — The Ricoh 2A03 is a modified MOS 6502 running at 1.789773 MHz (NTSC). It lacks the 6502's BCD (Binary Coded Decimal) mode but integrates the APU on the same die.
- [[NES Emulation/CPU — The 6502 Processor/6502 Addressing Modes|6502 Addressing Modes]] — Addressing modes are the CPU's vocabulary for describing where data lives — each mode is a different strategy for computing an effective memory address from the instruction bytes.
- [[NES Emulation/CPU — The 6502 Processor/6502 Instruction Set|6502 Instruction Set]] — The instruction set is the CPU's complete repertoire of actions — every game ever made for the NES is expressed entirely through these ~56 operations combined with addressing modes.
- [[NES Emulation/CPU — The 6502 Processor/6502 Registers and Status Flags|6502 Registers and Status Flags]] — The registers are the CPU's tiny scratchpad — just 6 registers hold the entire working state, and the 8-bit status register encodes the outcome of every operation as a set of boolean flags.
- [[NES Emulation/CPU — The 6502 Processor/CPU Cycle Accuracy and Timing|CPU Cycle Accuracy and Timing]] — The NES has no frame buffer — the CPU and PPU run in lockstep, and games exploit exact cycle timing for visual effects, so your emulator must count every cycle precisely.
- [[NES Emulation/CPU — The 6502 Processor/Interrupts — NMI, IRQ, and Reset|Interrupts — NMI, IRQ, and Reset]] — Interrupts are the hardware's way of tapping the CPU on the shoulder and saying "stop what you're doing and handle this" — they're the fundamental mechanism for real-time coordination between the CPU and other chips.
- [[NES Emulation/Memory Map and Bus/Memory Map and Bus Overview|Memory Map and Bus Overview]] — The NES CPU sees a 64 KB address space (0x0000-0xFFFF) shared between RAM, PPU registers, APU registers, and cartridge ROM. The PPU has its own separate 16 KB address space.
- [[NES Emulation/Memory Map and Bus/CPU Memory Map|CPU Memory Map]] — The CPU sees a single flat 64 KB address space, but behind every address is a physical device — RAM, PPU registers, APU, or cartridge.
- [[NES Emulation/Memory Map and Bus/OAM DMA|OAM DMA]] — OAM DMA is a dedicated hardware shortcut that copies an entire page (256 bytes) of sprite data from CPU memory to the PPU's Object Attribute Memory in one atomic operation, freezing the CPU while it works.
- [[NES Emulation/Memory Map and Bus/PPU Memory Map|PPU Memory Map]] — The PPU has its own private address bus and memory, completely separate from the CPU — it maps tile graphics from the cartridge, screen layout in VRAM, and color palettes into a 16 KB space with its own mirroring rules.

## Book II: Picture, Sound, And Input

Move from computation to the user-visible frame, audio stream, and controller state.

- [[NES Emulation/PPU — Picture Processing Unit/PPU — Picture Processing Unit Overview|PPU — Picture Processing Unit Overview]] — The Ricoh 2C02 (NTSC) is the NES's dedicated graphics processor. It renders 256x240 pixels at ~60 Hz by racing the electron beam across 262 scanlines of 341 dots each.
- [[NES Emulation/PPU — Picture Processing Unit/Backgrounds and Nametables|Backgrounds and Nametables]] — The NES background is a mosaic — a 32×30 grid of 8×8 pixel tiles where each cell is just an index pointing to a tile graphic, and the attribute table assigns a color palette to each 2×2 group of tiles.
- [[NES Emulation/PPU — Picture Processing Unit/PPU Registers and Timing|PPU Registers and Timing]] — The CPU controls the PPU through just 8 registers — but these registers have complex side effects, shared internal state (the write toggle and read buffer).
- [[NES Emulation/PPU — Picture Processing Unit/PPU Rendering Pipeline|PPU Rendering Pipeline]] — The PPU is a state machine that processes one dot (pixel) every cycle, fetching tile data in an 8-dot pipeline while simultaneously outputting pixels through shift registers.
- [[NES Emulation/PPU — Picture Processing Unit/PPU Scrolling|PPU Scrolling]] — PPU scrolling uses two 15-bit address registers (v and t) plus a 3-bit fine X register.
- [[NES Emulation/PPU — Picture Processing Unit/Sprites and OAM|Sprites and OAM]] — Sprites are the movable objects layered on top of (or behind) the background.
- [[NES Emulation/APU — Audio Processing Unit/APU — Audio Processing Unit Overview|APU — Audio Processing Unit Overview]] — The APU is integrated into the Ricoh 2A03 alongside the CPU. It generates audio through 5 channels: two pulse waves, one triangle wave, one noise generator, and one delta modulation channel (DMC).
- [[NES Emulation/APU — Audio Processing Unit/APU Frame Sequencer|APU Frame Sequencer]] — The frame sequencer is the APU's conductor — it doesn't produce sound itself but beats time at ~240 Hz, telling each channel's envelope, sweep, and length counter when to tick forward.
- [[NES Emulation/APU — Audio Processing Unit/DMC — Delta Modulation Channel|DMC — Delta Modulation Channel]] — The DMC is the NES's sampler — it plays pre-recorded audio by reading bytes from ROM and interpreting each bit as "output level goes slightly up" or "slightly down," producing rough but recognizable reproductions of.
- [[NES Emulation/APU — Audio Processing Unit/Pulse Channels|Pulse Channels]] — Each pulse channel generates a rectangular wave at a programmable frequency and duty cycle.
- [[NES Emulation/APU — Audio Processing Unit/Triangle and Noise Channels|Triangle and Noise Channels]] — The triangle channel produces a smooth, pure tone (no volume control — it's either on or off) perfect for bass lines.
- [[NES Emulation/Input and Controllers/Input and Controllers Overview|Input and Controllers Overview]] — The NES controller is a simple but elegant input device with a D-pad, two action buttons (A, B), and two meta buttons (Start, Select). The console communicates with controllers via a serial shift register protocol.
- [[NES Emulation/Input and Controllers/Controller Features in OxideNES|Controller Features in OxideNES]] — OxideNES bridges modern input hardware (keyboards, gamepads) to the NES's simple 8-button serial protocol, adding convenience features like remapping, turbo buttons, and input recording.
- [[NES Emulation/Input and Controllers/NES Joypad Protocol|NES Joypad Protocol]] — The NES reads controllers through a serial shift register — a strobe signal latches all 8 button states, then 8 sequential reads shift out one bit at a time.

## Book III: Cartridges And Mappers

Read cartridges as hardware extensions that change the rules of the base machine.

- [[NES Emulation/Cartridges and Mappers/Cartridges and Mappers Overview|Cartridges and Mappers Overview]] — NES cartridges contain ROM chips and optional mapper hardware that extends the console's capabilities far beyond its base specifications.
- [[NES Emulation/Cartridges and Mappers/Advanced Mappers|Advanced Mappers]] — Advanced mappers add entire subsystems (audio, IRQs, multipliers, RAM) beyond simple bank switching, turning the cartridge into a miniature co-processor board.
- [[NES Emulation/Cartridges and Mappers/Bank Switching Explained|Bank Switching Explained]] — Bank switching is a hardware sliding-window mechanism that maps different ROM segments into the CPU's 32 KB address space, letting games far exceed the processor's native addressing limit.
- [[NES Emulation/Cartridges and Mappers/Common Mappers|Common Mappers]] — Five mapper types cover ~85% of all NES games — mastering these five gets you from "hello world" to running most of the NES library.
- [[NES Emulation/Cartridges and Mappers/Expansion Audio|Expansion Audio]] — Some NES cartridges contain extra sound chips that add channels beyond the standard 5, enabling richer and more complex music.
- [[NES Emulation/Cartridges and Mappers/iNES ROM Format|iNES ROM Format]] — A 16-byte header prepended to raw ROM data describes the cartridge's hardware configuration — mapper, ROM sizes, mirroring, and battery.

## Book IV: Emulator Architecture And Polish

Turn component knowledge into a working emulator with timing, presentation, and tooling.

- [[NES Emulation/Emulator Architecture/Emulator Architecture Overview|Emulator Architecture Overview]] — OxideNES is a cycle-accurate NES emulator written in Rust, designed for both accuracy and performance. The architecture follows a modular design with the Bus as central coordinator.
- [[NES Emulation/Emulator Architecture/Main Loop and Cycle Ratios|Main Loop and Cycle Ratios]] — The main loop steps the emulated chips together at the correct hardware ratios: 1 CPU cycle corresponds to 3 PPU dots, while the APU is also advanced from the CPU-driven loop.
- [[NES Emulation/Emulator Architecture/OxideNES Module Architecture|OxideNES Module Architecture]] — A single Bus coordinates CPU, PPU, APU, cartridge logic, and controller input while optional subsystems plug into the application layer around that core.
- [[NES Emulation/Emulator Architecture/Performance Optimization in OxideNES|Performance Optimization in OxideNES]] — The emulator stays accurate first, then tunes only the parts that run often enough to matter.
- [[NES Emulation/Emulator Architecture/Save States and Rewind|Save States and Rewind]] — A save state is a complete machine snapshot, and rewind is a circular buffer of those snapshots. Analogy: A save state is a bookmark; rewind is a DVR that lets you scrub backward through recent history.
- [[NES Emulation/CRT Simulation/CRT Simulation Overview|CRT Simulation Overview]] — OxideNES features a comprehensive CRT simulation pipeline that transforms the raw 256x240 NES output into a convincing vintage television image.
- [[NES Emulation/CRT Simulation/Barrel Distortion and Shadow Mask|Barrel Distortion and Shadow Mask]] — Barrel distortion simulates curved CRT glass; shadow mask reproduces the RGB phosphor dot pattern. Analogy: Looking through a fishbowl at a mosaic. Why It Matters: These two effects most define the CRT look.
- [[NES Emulation/CRT Simulation/CRT Rendering Pipeline|CRT Rendering Pipeline]] — Seven sequential stages transform the 256×240 NES framebuffer into a CRT display. Analogy: Like an Instagram filter chain — order matters.
- [[NES Emulation/CRT Simulation/Glass Reflections and Chromatic Aberration|Glass Reflections and Chromatic Aberration]] — Glass reflections are ambient light bouncing off the CRT surface; chromatic aberration is RGB separation at the edges. Analogy: A TV in a bright room — a ghost reflection plus color fringing at curved edges.
- [[NES Emulation/CRT Simulation/Scanline and Phosphor Effects|Scanline and Phosphor Effects]] — Scanlines, phosphor warmth, bloom, and vignette reproduce a CRT's characteristic glow and falloff. Analogy: Candlelight vs LED — CRT phosphors have natural glow, fade, and color temperature.
- [[NES Emulation/Extended Features/Extended Features Overview|Extended Features Overview]] — Beyond core NES emulation, OxideNES includes several modern quality-of-life features that enhance the retro gaming experience.
- [[NES Emulation/Extended Features/Achievement System|Achievement System]] — This is a frame-by-frame RAM inspector evaluating RetroAchievements-compatible conditions. Analogy: A sports referee watching instant replay every frame.
- [[NES Emulation/Extended Features/Input Recording and TAS|Input Recording and TAS]] — Frame-perfect input capture enables replay, TAS, and cross-emulator sharing. Analogy: A player piano roll — every press is timestamped for exact playback.
- [[NES Emulation/Extended Features/Lua Scripting Engine|Lua Scripting Engine]] — A sandboxed Lua 5.4 VM enables memory inspection and overlay drawing without modifying emulator source. Analogy: Browser DevTools for NES — inspect state, add overlays, and log data safely.
- [[NES Emulation/Extended Features/Netplay — UDP Multiplayer|Netplay — UDP Multiplayer]] — Peer-to-peer lockstep multiplayer over UDP exchanges input every frame. Analogy: A synchronized dance over the phone — both players call out moves each beat, wait to hear the partner, then step together.

## Appendices: Practice And Sources

Use drills, cheatsheets, and source registries to test the emulator model.

- [[NES Emulation/Study/NES Emulation Study Index|NES Emulation — Study Index]] — Study router for NES Emulation drills, labs, proof artifacts, and review sessions.
- [[NES Emulation/Study/Cheatsheet — NES Memory Maps and Registers|Cheatsheet — NES Memory Maps and Registers]] — Quick reference for NES address spaces and register layouts.
- [[NES Emulation/Study/Review Drill — 6502 CPU and Addressing|Review Drill — 6502 CPU and Addressing]] — Review drill for 6502 CPU and Addressing.
- [[NES Emulation/Study/Review Drill — APU Audio Channels|Review Drill — APU Audio Channels]] — Review drill for APU Audio Channels.
- [[NES Emulation/Study/Review Drill — Emulator Architecture|Review Drill — Emulator Architecture]] — Review drill for Emulator Architecture.
- [[NES Emulation/Study/Review Drill — Mappers and Bank Switching|Review Drill — Mappers and Bank Switching]] — Review drill for Mappers and Bank Switching.
- [[NES Emulation/Study/Review Drill — PPU Rendering Pipeline|Review Drill — PPU Rendering Pipeline]] — Review drill for PPU Rendering Pipeline.
- [[NES Emulation/Sources/Sources Index|Sources Index — NES Emulation]] — Source and provenance map for NES Emulation.

## Appendix: Remaining Reader-Facing Notes

These notes are part of the topic corpus but do not belong cleanly to the main narrative chapters yet.

- [[NES Emulation/NES Hardware Overview/NES Hardware Overview|NES Hardware Overview]] — The Nintendo Entertainment System (1983 in Japan as Famicom, 1985 in North America) defined console gaming for a generation. Understanding its hardware is the foundation for building an accurate emulator.
- [[NES Emulation/NES Hardware Overview/NES Console Architecture|NES Console Architecture]] — The console centers on three major pieces of hardware: the Ricoh 2A03, the Ricoh 2C02, and the cartridge, all connected through two distinct buses.
- [[NES Emulation/NES Hardware Overview/NES History and Legacy|NES History and Legacy]] — From 1983 to 1995, the NES established patterns that outlived the platform itself, and its influence still shows up in modern emulators.
- [[NES Emulation/NES Hardware Overview/NES Technical Specifications|NES Technical Specifications]] — The NES has a fixed hardware envelope: 1.789773 MHz CPU, 256×240 output, 262 scanlines, 5 audio channels, and 2 KB of RAM.
- [[NES Emulation/NES Hardware Overview/NES vs Other 8-bit Consoles|NES vs Other 8-bit Consoles]] — The NES traded some headline specs for better sprite handling, integrated audio design, and mapper-based expansion. Analogy: It is like a smaller engine with better handling and far better aftermarket parts.

## Coverage

- Reader-facing articles linked here: 60
- Protected raw, chunk, template, query, audio, and operations folders are intentionally not expanded here.
- The root vault index remains the exhaustive generated listing across every topic.

## References

- [[NES Emulation/NES Emulation|NES Emulation]]
- [[NES Emulation/Sources/Sources Index|Sources Index — NES Emulation]]
