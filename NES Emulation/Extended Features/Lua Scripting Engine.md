---
tags: [nes, wiki]
up: "[[Extended Features Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# Lua Scripting Engine

> **OxideNES embeds a sandboxed Lua 5.4 VM so scripts can inspect memory and draw overlays without changing emulator source code.**

## 🎯 Intuition
**The Core Idea:** A sandboxed Lua 5.4 VM enables memory inspection and overlay drawing without modifying emulator source.
**Analogy:** Browser DevTools for NES — inspect state, add overlays, and log data safely.
**Why It Matters:** It enables community tools without recompilation, and sandboxing keeps the system safe.

---

## ⚙️ Core Mechanics
### How It Works
OxideNES embeds a Lua `5.4` interpreter (via `mlua` crate) for runtime scripting. Scripts can read NES memory, draw overlay graphics, display messages, and register per-frame callbacks.

### Key Specifications

| Function | Description |
|----------|-------------|
| `nes.read(addr)` | Read byte from CPU memory (0x0000-0xFFFF) |
| `nes.framecount()` | Current emulated frame number |
| `nes.pixel(x, y, color)` | Draw colored pixel on overlay layer |
| `nes.message(text)` | Display HUD notification |
| `nes.log(text)` | Print to stderr for debugging |
| `nes.onframe(fn)` | Register callback called every frame |

### Key Facts
- **Removed:** `io`, `os`, `require`, `debug`, `package` libraries.
- **Read-only:** Scripts can only read NES memory, not write.
- **Scoped:** RAM snapshot is provided per-frame, not a live reference.

### Example Script
```lua
nes.onframe(function()
    local lives = nes.read(0x0075)
    nes.message("Lives: " .. lives)
end)
```

---

## 🔬 Deep Dive
### `scripting.rs`
The OxideNES implementation lives in `scripting.rs` (`174` lines).

### Script Engine
`ScriptEngine` creates a sandboxed Lua VM on init.

### Frame Callback Model
`on_frame()` is called each emulated frame, providing a RAM snapshot to the script's registered callback.

### Overlay Pixel Collection
Overlay pixels are collected and rendered on the display layer.

### Reference Implementations
In OxideNES, the `mlua`-backed `ScriptEngine` exposes a narrow API for memory reads, frame counting, overlay drawing, messaging, logging, and per-frame callbacks while keeping scripts read-only and sandboxed.

---

## 🏋️ Practice
### Warm-Up (5 min)
- Write a Lua script that displays `X` and `Y` position values if you know their RAM addresses.
- Explain why removing `io` and `os` improves sandbox safety.
- Describe what the overlay pixel system is responsible for.

### Core Problems
- Explain the difference between a per-frame RAM snapshot and a live writable memory reference.
- Describe how `nes.onframe(fn)` and `nes.pixel(x, y, color)` can work together to build an on-screen debugging overlay.

### Challenge
- Design a small script tool that reads game state each frame and renders a custom diagnostic overlay without modifying emulator source code.

---

*See also:* [[Achievement System]], [[Input Recording and TAS]], [[Netplay — UDP Multiplayer]], [[Extended Features Overview]]

## References
→ [[NES Emulation/Sources/Sources Index|Sources Index]]