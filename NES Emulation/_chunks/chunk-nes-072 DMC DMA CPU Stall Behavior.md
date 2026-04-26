---
tags: [chunk, nes-emulation, dma]
source: "[[raw-nes-029]]"
up: "[[DMC — Delta Modulation Channel]]"
---

# Chunk NES 072 — DMC DMA CPU Stall Behavior

DMC sample playback uses DMA to fetch audio bytes from CPU memory, stalling the CPU for 1-4 cycles per read depending on CPU state: 4 cycles during a CPU write, 3 during a standard read, 2 during penultimate instruction cycle, 1 when perfectly aligned. DMC DMA can interrupt OAM DMA — the OAM transfer pauses for the DMC read then resumes, potentially corrupting one OAM byte (a glitch byte). This interaction is emulated in OxideNES: the APU sets a dmc_dma_request flag, and the bus handles the stall with correct cycle counting based on the CPU's current operation state.
