---
tags: [chunk, nes-emulation, scripting]
source: "[[raw-nes-008]]"
up: "[[Lua Scripting Engine]]"
---

# Chunk NES 031 — Lua API Memory and State Access

OxideNES exposes emulation state to Lua 5.4 scripts via the mlua crate. Memory functions include emu.read(addr) and emu.write(addr, val) for CPU address space, emu.read_range(addr, len) returning a table, and emu.read_ppu(addr) for PPU space. State functions include emu.get_register(name) and emu.set_register(name, val) for CPU registers A, X, Y, SP, PC, and P. Input overrides via emu.set_input(player, bitmask) enable TAS automation. The Lua environment is sandboxed with dangerous functions like os.execute removed, memory allocation limited, and per-frame execution time capped.
