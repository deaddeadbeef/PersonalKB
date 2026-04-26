---
tags: [chunk, nes-emulation, performance]
source: "[[raw-nes-015]]"
up: "[[Performance Optimization in OxideNES]]"
---

# Chunk NES 045 — CPU Optimization Techniques

OxideNES optimizes CPU emulation through several strategies. Pre-computed lookup tables index instruction cycle counts, addressing mode handlers, and NZ flag calculations by opcode, eliminating decode-stage branching. The NZ flag table maps all 256 byte values to their Negative and Zero flag states. Page-cross detection checks only the low byte: (base AND ) + offset > . Rust compiler hints mark hot paths (loads, stores, taken branches) as likely. All memory access flows through the bus trait with no runtime polymorphism cost thanks to monomorphization. No heap allocation occurs during emulation frames.
