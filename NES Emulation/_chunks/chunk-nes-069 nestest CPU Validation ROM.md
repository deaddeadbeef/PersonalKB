---
tags: [chunk, nes-emulation, testing]
source: "[[raw-nes-028]]"
up: "[[Emulator Architecture Overview]]"
---

# Chunk NES 069 — nestest CPU Validation ROM

nestest.nes is the most important NES CPU test ROM, originally by kevtris. It executes every official and many unofficial opcodes, verifying all addressing modes, flag behaviors (N, V, Z, C for every instruction), page-crossing cycle behavior, stack operations, and BRK/RTI sequences. It produces a log of each instruction with expected vs actual register states. OxideNES can run headless, comparing its execution log against the golden reference. Any deviation indicates a CPU bug. OxideNES passes nestest completely for all official opcodes and the commonly-used unofficial opcodes.
