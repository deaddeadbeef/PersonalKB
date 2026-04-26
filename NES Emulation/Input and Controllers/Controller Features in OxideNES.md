---
tags: [nes, wiki]
up: "[[Input and Controllers Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Controller Features in OxideNES

> **Bridges modern input hardware to the NES's 8-button protocol with remapping, turbo, multi-player, and TAS recording.**

## 🎯 Intuition
**The Core Idea:** OxideNES bridges modern input hardware (keyboards, gamepads) to the NES's simple 8-button serial protocol, adding convenience features like remapping, turbo buttons, and input recording.
**Analogy:** Like a universal remote that can map any device's buttons to the 8 NES inputs — plus it can record and replay every button press.
**Why It Matters:** Controller input is the most direct player-to-emulator interface. Responsive, configurable input with recording capability is essential for both casual play and tool-assisted speedruns.

---

## ⚙️ Core Mechanics
### How It Works
OxideNES reads keyboard events (via minifb) and gamepad events (via gilrs crate), maps them through configurable bindings to NES button states, and feeds those states into the joypad emulation. Additional features like turbo and input recording operate on top of this pipeline.

### Key Specifications

| Feature | P1 Default | P2 Default |
|---------|-----------|-----------|
| D-Pad | WASD | Arrow keys |
| A Button | K | Period |
| B Button | J | Comma |
| Start | Enter | Slash |
| Select | RShift | RCtrl |
| Turbo A | Z | — |
| Turbo B | X | — |
| Controllers | Any gamepad via gilrs with auto-detection | — |

### Key Facts
- Fully configurable input bindings with in-app rebinding and conflict detection
- Turbo A (Z key) and Turbo B (X key) auto-press at 30 Hz (every other frame)
- Two-player support: P1 keyboard + P2 keyboard, P1 controller + P2 keyboard, or P1 local + P2 remote via netplay
- Input recording captures frame-by-frame controller states for TAS support with ROM hash verification
- Recordings export to FM2 format for FCEUX compatibility

---

## 🔬 Deep Dive
### Input Remapping System
OxideNES supports fully configurable input bindings:
- **Keyboard P1:** WASD + K/J + Enter/RShift (default)
- **Keyboard P2:** Arrows + Period/Comma + Slash/RCtrl
- **Controllers:** Any gamepad via gilrs crate with automatic detection
- **In-app rebinding:** Settings menu with conflict detection

Bindings are stored in config.json. The settings menu provides in-app rebinding with conflict detection — if two actions are mapped to the same key, the user is warned.

### Turbo Implementation
Turbo A (Z key) and Turbo B (X key) auto-press at 30 Hz (every other frame), useful for games requiring rapid button presses. The turbo mechanism toggles a flag each frame during emulation. When turbo is held, the corresponding button alternates between pressed and released every frame, producing a 30 Hz press rate at 60 FPS.

### Two-Player Support
Both controllers are fully emulated:
- **Local:** P1 keyboard + P2 keyboard, or P1 controller + P2 keyboard
- **Netplay:** P1 local + P2 remote via UDP (see [[Extended Features Overview]])

### Input Recording and TAS
OxideNES records controller inputs frame-by-frame for TAS (Tool-Assisted Speedrun) support. Recordings include both P1 and P2 inputs with ROM hash verification to ensure the recording matches the correct game. Export to FM2 format provides compatibility with FCEUX, a widely-used NES emulator.

### Reference Implementations
main.rs handles input through minifb keyboard events and gilrs gamepad events. Bindings are stored in config.json. The turbo mechanism toggles a flag each frame during emulation.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What crate does OxideNES use for gamepad input, and how are gamepads detected?
2. At what frequency do turbo buttons press, and how is this implemented?
3. What format does OxideNES use for exporting input recordings?

### Core Problems
1. **Input Mapping:** Design a data structure for configurable input bindings that maps physical keys/buttons to NES buttons for two players. Include conflict detection that warns when two actions share the same physical input.
2. **Turbo Implementation:** Implement a turbo button system that alternates between pressed and released every frame. Given a 60 FPS emulation loop, verify the turbo produces exactly 30 presses per second.

### Challenge
**Input Recording System:** Implement a frame-by-frame input recording system that captures P1 and P2 button states each frame, stores the ROM hash for verification, and can export to FM2 format. Test by recording a short sequence, saving it, reloading it, and verifying frame-perfect playback.

---

*See also:* [[NES Joypad Protocol]], [[Input and Controllers Overview]]

## References
→ [[Sources Index]]
