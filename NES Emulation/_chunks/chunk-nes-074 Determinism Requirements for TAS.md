---
tags: [chunk, nes-emulation, tas]
source: "[[raw-nes-030]]"
up: "[[Input Recording and TAS]]"
---

# Chunk NES 074 — Determinism Requirements for TAS

TAS replay correctness demands perfect determinism — identical inputs must always produce identical output. OxideNES ensures this by eliminating real-time clock dependencies during emulation, using fixed-point arithmetic to avoid floating-point platform variance, deterministically initializing all state with no uninitialized memory, and maintaining consistent instruction timing without accuracy-compromising optimizations. Frame advance (period key) steps exactly one frame and pauses, enabling frame-by-frame analysis. The input display overlay shows controller state visually. RAM watch via Lua scripts monitors game variables in real-time for strategy optimization.
