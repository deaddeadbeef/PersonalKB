---
tags: [chunk, nes-emulation, mapper]
source: "[[raw-nes-005]]"
up: "[[Common Mappers]]"
---

# Chunk NES 024 — MMC1 Serial Load Interface

MMC1 (Mapper 1) uses a unique 5-bit serial shift register interface. To set a register value, the CPU writes 5 times to -, each time loading bit 0 of the data byte into the shift register. On the fifth write, the accumulated 5-bit value transfers to one of four internal registers based on address bits 14-13. Writing with bit 7 set resets the shift register immediately. This serial interface was a cost-saving measure — it required fewer address decoder pins on the mapper chip. OxideNES implements write_serial() tracking shift state and write count.
