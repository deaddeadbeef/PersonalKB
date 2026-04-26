---
tags: [chunk, nes-emulation, achievement]
source: "[[raw-nes-009]]"
up: "[[Achievement System]]"
---

# Chunk NES 095 — Achievement Persistence and Display

Triggered achievements are saved to JSON files in ~/.nes-emulator/achievements/<rom-crc32>.json. On ROM load, previously triggered achievements are loaded and excluded from further evaluation. Save states do NOT affect achievement state — reloading a save cannot re-trigger earned achievements. When an achievement triggers, a toast notification overlay appears: a semi-transparent rectangle with title and description text that fades out over 3 seconds, composited on top of the CRT pipeline output. The system does not implement anti-cheat measures; Lua scripts remain active during achievement evaluation. Future RetroAchievements service integration could add server-side validation.
