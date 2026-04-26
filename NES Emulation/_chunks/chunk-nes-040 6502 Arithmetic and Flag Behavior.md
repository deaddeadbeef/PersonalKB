---
tags: [chunk, nes-emulation, instruction-set]
source: "[[raw-nes-013]]"
up: "[[6502 Instruction Set]]"
---

# Chunk NES 040 — 6502 Arithmetic and Flag Behavior

ADC (add with carry) computes A = A + M + C, setting Negative, Overflow, Zero, and Carry flags. The NES ignores the Decimal flag so BCD mode never activates. Overflow detection uses (A xor result) AND (M xor result) AND . SBC (subtract with borrow) is implemented as ADC with the operand complemented. CMP/CPX/CPY perform unsigned subtraction setting N, Z, C without storing the result — Carry indicates register >= memory. BIT performs A AND M but sets Z from the result while copying memory bits 7 and 6 directly into N and V flags — a unique behavior among 6502 instructions.
