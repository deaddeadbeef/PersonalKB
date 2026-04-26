---
tags: [chunk, nes-emulation, module]
source: "[[raw-nes-027]]"
up: "[[Emulator Architecture Overview]]"
---

# Chunk NES 109 — Main.rs as Application Shell

main.rs is OxideNES's largest file at approximately 7,572 lines because it handles everything above the emulation core: window creation via minifb, the full CRT rendering pipeline (7 stages), input polling from keyboard and gamepads, audio output management via cpal, save state file I/O, the rewind ring buffer system, netplay UDP protocol, Lua script loading and execution, achievement evaluation and display, and TOML configuration parsing. This separation keeps the emulation core (bus, cpu, ppu, apu, mapper) pure and testable while main.rs serves as the integration layer connecting emulation to the host operating system.
