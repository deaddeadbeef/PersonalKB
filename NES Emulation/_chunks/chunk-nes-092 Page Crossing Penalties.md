---
tags: [chunk, nes-emulation, cpu]
source: "[[raw-nes-011]]"
up: "[[6502 Addressing Modes]]"
---

# Chunk NES 092 — Page Crossing Penalties

When indexed addressing (Absolute X/Y, Indirect Indexed Y) crosses a 256-byte page boundary, read instructions incur an extra cycle. This happens because the CPU first reads from the incorrect address (base low byte plus index, without carry into high byte), then corrects to the true address with an additional cycle. Write instructions always take the penalty cycle because the CPU performs a dummy read regardless of page crossing. In OxideNES, page crosses are efficiently detected by checking (base AND ) + index >  — a single comparison on the low byte without computing the full 16-bit address first.
