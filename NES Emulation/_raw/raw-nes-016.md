---
tags: [raw, nes-emulation, input]
source: "OxideNES main.rs + INPUT_REBINDING_IMPLEMENTATION.md"
---

# Raw NES 016 — Input System and Controller Rebinding

OxideNES implements a flexible input system supporting keyboard, USB gamepads (via the gilrs crate), and network-delivered inputs. The system includes runtime rebinding with persistent configuration.

## Controller Abstraction

Internally, controller state is represented as an 8-bit bitmask matching the NES hardware shift register order: A (bit 0), B (bit 1), Select (bit 2), Start (bit 3), Up (bit 4), Down (bit 5), Left (bit 6), Right (bit 7). All input sources (keyboard, gamepad, Lua script, netplay) produce this same 8-bit format, which is what the PPU reads via /.

## Keyboard Mapping

Default keyboard mappings: Arrow keys for D-pad, Z for A, X for B, Right Shift for Select, Enter for Start. Player 2 uses a separate set (WASD + JK + G/H). All keys are configurable. Key states are polled each frame from the minifb window event loop.

## Gamepad Support

The gilrs crate provides cross-platform gamepad support (DirectInput, XInput, evdev). OxideNES auto-detects connected gamepads and assigns them to player 1/2. Button mapping follows a default layout (face button A → NES A, etc.) but is fully rebindable. Analog stick inputs are converted to digital D-pad presses using a configurable dead zone (default 0.5). Gamepad hot-plugging is supported — connecting a gamepad mid-game automatically registers it.

## Rebinding System

Runtime rebinding is triggered via a hotkey (F9). The emulator enters "rebind mode," pausing emulation and prompting for each button in sequence: A, B, Select, Start, Up, Down, Left, Right. The user presses the desired key/button for each. The new mapping is immediately active and persisted to ~/.nes-emulator/config.toml.

## Configuration Persistence

Input mappings are stored in a TOML configuration file:
`	oml
[input.player1.keyboard]
a = "Z"
b = "X"
select = "RShift"
start = "Return"
up = "Up"
down = "Down"
left = "Left"
right = "Right"

[input.player1.gamepad]
a = "South"
b = "East"
select = "Select"
start = "Start"
`

The config file is loaded at startup and created with defaults if missing. Changes via rebinding overwrite the relevant section.

## Turbo Buttons

OxideNES supports turbo (auto-fire) mode for A and B buttons. When enabled, the button rapidly toggles on/off every other frame (30 Hz), simulating rapid button presses. Turbo is toggled via keyboard shortcuts and persists in the config.

## Input Recording

The input recording system (for TAS) captures the full 8-bit controller state for both players every frame. Recordings are stored as binary files (2 bytes per frame: player 1 + player 2). Playback reads these bytes and overrides controller input, replaying the exact input sequence. Combined with deterministic emulation, this reproduces identical gameplay.
