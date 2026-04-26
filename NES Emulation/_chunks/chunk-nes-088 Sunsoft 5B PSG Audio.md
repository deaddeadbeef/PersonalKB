---
tags: [chunk, nes-emulation, expansion-audio]
source: "[[raw-nes-024]]"
up: "[[Expansion Audio]]"
---

# Chunk NES 088 — Sunsoft 5B PSG Audio

The Sunsoft 5B / FME-7 (Mapper 69) contains a YM2149-compatible Programmable Sound Generator providing 3 square wave channels with 12-bit period registers, 4-bit per-channel volume or hardware envelope, and a shared noise generator. Used by Gimmick!, which features one of the most impressive NES soundtracks — its composer exploited the 3 extra channels plus the built-in APU to create rich, layered music impossible with the base NES hardware alone. OxideNES implements the FME-7 audio registers as part of the Mapper 69 struct with cycle-accurate channel updates.
