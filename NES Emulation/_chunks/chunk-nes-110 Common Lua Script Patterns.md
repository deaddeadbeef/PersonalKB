---
tags: [chunk, nes-emulation, scripting]
source: "[[raw-nes-008]]"
up: "[[Lua Scripting Engine]]"
---

# Chunk NES 110 — Common Lua Script Patterns

Typical OxideNES Lua scripts include: memory viewers displaying game state variables in real-time using emu.read() and emu.draw_text(), hitbox visualizers drawing collision rectangles with emu.draw_rect() based on memory-mapped position data, input display overlays showing controller state for TAS recordings, cheat codes writing specific values with emu.write(), automated testing scripts verifying game logic through memory conditions, and bot scripts that read game state and compute optimal inputs via emu.set_input(). Scripts load via command-line argument or hotkey and persist across save state operations since script state is independent of emulation state.
