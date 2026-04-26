---
tags: [chunk, nes-emulation, cpu]
source: "[[raw-nes-013]]"
up: "[[6502 Instruction Set]]"
---

# Chunk NES 083 — Stack and Subroutine Instructions

The 6502 stack lives in page 1 (-) growing downward. PHA pushes the accumulator; PLA pulls it (setting N and Z flags). PHP pushes the processor status with the B flag set; PLP pulls it. JSR pushes PC minus 1 (the last byte of the JSR instruction) then jumps to the target — 6 cycles. RTS pulls PC from the stack and adds 1 to resume after the JSR — 6 cycles. RTI pulls the processor status then PC from the stack, used for returning from interrupt handlers. BRK pushes PC plus 2 and status with B flag set, then loads the IRQ vector.
