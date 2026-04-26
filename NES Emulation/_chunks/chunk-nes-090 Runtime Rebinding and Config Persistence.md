---
tags: [chunk, nes-emulation, input]
source: "[[raw-nes-016]]"
up: "[[Controller Features in OxideNES]]"
---

# Chunk NES 090 — Runtime Rebinding and Config Persistence

OxideNES supports runtime input rebinding via F9 hotkey, which pauses emulation and prompts for each button sequentially: A, B, Select, Start, Up, Down, Left, Right. New mappings activate immediately and persist to ~/.nes-emulator/config.toml in a structured format with separate sections for keyboard and gamepad bindings per player. The config file is created with defaults if missing and loaded at startup. Gamepad analog-to-digital conversion uses a configurable dead zone (default 0.5). Hot-plugging is supported — connecting a gamepad mid-game registers it automatically via the gilrs crate's event system.
