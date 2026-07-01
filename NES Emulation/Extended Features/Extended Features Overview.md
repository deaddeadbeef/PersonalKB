---
tags: [nes, hub]
up: "[[NES Emulation]]"
confidence: established
freshness: stable
tier-coverage: [intuition, core, deep-dive]
---
# Extended Features Overview

Beyond core NES emulation, OxideNES includes several modern quality-of-life features that enhance the retro gaming experience.

## Pages

- [[Netplay — UDP Multiplayer]] — Local network two-player over UDP
- [[Lua Scripting Engine]] — Runtime scripting with memory access and overlay drawing
- [[Achievement System]] — RetroAchievements-compatible local achievements
- [[Input Recording and TAS]] — Frame-perfect recording with FM2 export

## Additional Features

- **ROM Database** — Auto-identifies ~71 classic games, corrects bad headers
- **Game Genie** — Cheat code support (6 and 8 character codes)
- **Auto-Updater** — Checks GitHub Releases for new versions
- **Performance Overlay** — Real-time FPS, frame time, and CPU usage display

## How To Read This Chapter

Read this chapter for features beyond baseline accuracy. NES emulation is less about isolated facts than about making several small timed machines agree on the same frame. The overview pages should give you the vocabulary first, then route you into the detailed pages where timing, registers, and test-ROM behavior matter.

A productive pass has three questions. First, what state does this subsystem own? Second, which reads or writes have side effects? Third, what timing relationship can break a game if it is off by even a few CPU or PPU cycles? Keep those questions nearby while reading the linked pages.

## Emulator Checkpoints

Use the deeper notes to turn the concept into implementation proof. The key checkpoints for this chapter are: rewind, save states, debugging overlays, netplay, cheats, shaders, and configuration persistence. For each checkpoint, prefer a tiny deterministic test before a visual game test. A passing screenshot is useful, but a focused trace is better when the bug is cycle timing, flag behavior, mapper state, or register side effects.

The chapter is mastered when you can explain both the user-visible symptom and the internal cause of a failure. For example, audio pops, scrolling seams, wrong sprite priority, broken controller input, or a mapper crash should point back to a specific piece of state and a specific clock boundary.

## References

→ [[NES Emulation/Sources/Sources Index|Sources Index]]
