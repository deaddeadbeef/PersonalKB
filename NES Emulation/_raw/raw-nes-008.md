---
tags: [raw, nes-emulation, scripting]
source: "OxideNES main.rs Lua scripting"
---

# Raw NES 008 — Lua Scripting Engine

OxideNES embeds a Lua 5.4 scripting engine via the mlua crate, enabling users to write custom scripts that interact with the running emulation. This is a powerful feature for tool-assisted speedrunning (TAS), debugging, and custom game modifications.

## API Surface

Scripts access the emulation through a set of Lua functions registered by the emulator:

**Memory Access:**
- mu.read(addr) — Read a byte from CPU address space
- mu.write(addr, val) — Write a byte to CPU address space
- mu.read_range(addr, len) — Read a range of bytes (returns table)
- mu.read_ppu(addr) — Read from PPU address space

**State:**
- mu.frame_count() — Current frame number
- mu.get_register(name) — Read CPU register (A, X, Y, SP, PC, P)
- mu.set_register(name, val) — Write CPU register

**Input:**
- mu.get_input(player) — Get current controller state as bitmask
- mu.set_input(player, bitmask) — Override controller input (for TAS)

**Display:**
- mu.draw_text(x, y, text, color) — Draw overlay text on the screen
- mu.draw_rect(x, y, w, h, color) — Draw overlay rectangle
- mu.draw_line(x1, y1, x2, y2, color) — Draw overlay line
- mu.screenshot(path) — Save current frame to PNG

**Callbacks:**
- mu.on_frame(fn) — Called every frame before rendering
- mu.on_scanline(n, fn) — Called when scanline N begins
- mu.on_read(addr, fn) — Called when CPU reads from addr
- mu.on_write(addr, fn) — Called when CPU writes to addr
- mu.on_exec(addr, fn) — Called when CPU executes instruction at addr

## Sandboxing

The Lua environment is sandboxed: os.execute, io.open, and other dangerous functions are removed. Scripts can only interact with the emulation through the mu API. Memory allocation is limited to prevent runaway scripts from consuming all RAM. Script execution time per frame is capped — if a script takes too long, it's forcibly paused with an error.

## Use Cases

Common script patterns include: memory viewers showing game state in real-time, hitbox visualizers drawing collision boxes, input display overlays for TAS recording, custom cheat codes by writing memory values, automated testing of game logic, and bot scripts that play the game based on memory state analysis.

## Script Loading

Scripts are loaded via command-line argument (--script path.lua) or hotkey during runtime. Multiple scripts can be loaded simultaneously, each running in its own Lua state. Scripts persist across save state loads/rewinds — the script state is independent of emulation state.
