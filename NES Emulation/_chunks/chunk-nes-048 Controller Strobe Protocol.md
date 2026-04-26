---
tags: [chunk, nes-emulation, input]
source: "[[raw-nes-016]]"
up: "[[NES Joypad Protocol]]"
---

# Chunk NES 048 — Controller Strobe Protocol

The NES reads controller state through  (player 1) and  (player 2). Writing 1 then 0 to  strobes both controllers, latching the current button states into internal shift registers. Each subsequent read from  or  returns one bit of the 8-button state in order: A, B, Select, Start, Up, Down, Left, Right. After all 8 bits are read, subsequent reads return 1 (for standard controllers). OxideNES models this shift register behavior precisely, supporting both standard polling patterns and the unusual read patterns some games use for controller detection.
