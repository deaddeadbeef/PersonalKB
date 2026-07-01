---
tags: [nes, study]
up: "[[NES Emulation]]"
confidence: verified
freshness: stable
tier-coverage: [practice]
---

# NES Emulation — Study Index

## Start Here By Goal

Use this page as an emulator-debugging router before opening drills.

| Goal | Start with | Then use | Proof you should leave behind |
|---|---|---|---|
| Read NES emulation as a book | [[NES Emulation/NES Emulation Book Reading Spine|NES Emulation Book Reading Spine]] | [[NES Emulation/NES Hardware Overview/NES Hardware Overview|NES Hardware Overview]], [[NES Emulation/Emulator Architecture/Emulator Architecture Overview|Emulator Architecture Overview]] | A frame-production story from CPU step to PPU/APU output |
| Debug CPU or memory behavior | [[NES Emulation/CPU — The 6502 Processor/CPU — The 6502 Processor Overview|CPU Overview]] | [[NES Emulation/Memory Map and Bus/Memory Map and Bus Overview|Memory Map and Bus Overview]], [[NES Emulation/Cartridges and Mappers/Cartridges and Mappers Overview|Cartridges and Mappers Overview]] | A trace that names address, bus owner, mapper state, instruction, and expected side effect |
| Debug video or audio output | [[NES Emulation/PPU — Picture Processing Unit/PPU — Picture Processing Unit Overview|PPU Overview]] | [[NES Emulation/APU — Audio Processing Unit/APU — Audio Processing Unit Overview|APU Overview]], [[NES Emulation/CRT Simulation/CRT Simulation Overview|CRT Simulation Overview]] | A timing or state-machine explanation tied to one visible or audible symptom |
| Prepare for recall | [[NES Emulation/Study/Cheatsheet — NES Memory Maps and Registers|NES Cheatsheet - Memory Map and Registers]] | The matching review drill below | A missed-register list plus one test, trace, or ROM that would catch the error |

## Review Drills

- [[NES Emulation/Study/Review Drill — 6502 CPU and Addressing|NES Review — CPU and Addressing Modes]]
- [[NES Emulation/Study/Review Drill — PPU Rendering Pipeline|NES Review — PPU Rendering Pipeline]]
- [[NES Emulation/Study/Review Drill — APU Audio Channels|NES Review — APU Sound Channels]]
- [[NES Emulation/Study/Review Drill — Mappers and Bank Switching|NES Review — Mappers and Bank Switching]]
- [[NES Emulation/Study/Review Drill — Emulator Architecture|NES Review — Emulator Architecture]]

## Cheatsheets

- [[NES Emulation/Study/Cheatsheet — NES Memory Maps and Registers|NES Cheatsheet — Memory Map and Registers]]

## How to Use

1. Read canonical pages for deep understanding
2. Use review drills to test recall
3. Reference cheatsheet for quick lookup
4. Explore chunks for atomic facts and QnA seeds

## Study Loop

Use this index after reading a subsystem overview. The drills are arranged around the failure modes that emulator authors actually debug: CPU addressing mistakes, PPU timing drift, audio channel state, mapper bank selection, and architecture choices that make the core hard to test. Work one domain at a time and keep a short failure log of what you missed.

A good session starts with the cheatsheet, then one review drill, then one implementation trace or test-ROM result. If you cannot explain why a register read has a side effect, why an interrupt fires on a particular boundary, or why a mapper changes the address space visible to the CPU, return to the canonical page before continuing.

## Proof Targets

The study set should eventually support three proofs: a mental model proof, an implementation proof, and a regression proof. The mental model proof is verbal: explain how a frame is produced. The implementation proof is local: point to code or pseudocode for the relevant state machine. The regression proof is durable: name the test, ROM, trace, or checklist that would catch the bug if it came back.

## References

- [[NES Emulation/Study/NES Emulation Study Index]]
- [[NES Emulation/Sources/Sources Index]]
- [[NES Emulation/NES Emulation Book Reading Spine]]
