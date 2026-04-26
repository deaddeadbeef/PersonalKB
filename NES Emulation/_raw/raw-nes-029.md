---
tags: [raw, nes-emulation, dma]
source: "NESdev DMA reference + OxideNES bus.rs"
---

# Raw NES 029 — DMA Mechanisms

The NES uses Direct Memory Access (DMA) to efficiently transfer data without burdening the CPU with byte-by-byte copies. Two DMA mechanisms exist: OAM DMA and DMC DMA.

## OAM DMA ($4014)

OAM DMA is the primary mechanism for updating sprite data. Writing a byte to $4014 triggers a 256-byte copy from CPU memory to PPU OAM.

**Trigger:** CPU writes byte N to $4014. This initiates a copy from CPU address $NN00-$NNFF to OAM addresses $00-$FF.

**Timing:** The transfer takes 513 CPU cycles (514 if started on an odd CPU cycle):
- 1 cycle: Initial wait (dummy read)
- 1 cycle: Additional alignment wait (only on odd CPU cycles)
- 256 × 2 cycles: Alternating read (from CPU bus) and write (to OAM) cycles

**CPU Stall:** During the entire DMA transfer, the CPU is halted. It cannot execute instructions or respond to interrupts. The bus handles this by setting a `dma_stall` counter that prevents CPU ticks until the transfer completes.

**Why Games Use It:** Copying 256 bytes manually would require ~1,280 CPU cycles (LDA abs,X / STA $2004 loop). OAM DMA does it in 513 cycles — more than 2× faster — and is simpler to program (single write to $4014). Nearly every NES game uses OAM DMA; direct $2003/$2004 access is unreliable during rendering.

**OxideNES Implementation:** When the bus detects a write to $4014:
1. Records the source page number
2. Sets `dma_cycles = 513` (or 514 on odd cycle)
3. During each subsequent bus clock, if dma_cycles > 0: on even cycles reads from source, on odd cycles writes to OAM, decrements dma_cycles
4. CPU remains stalled until dma_cycles reaches 0

## DMC DMA (Automatic)

The DMC channel's sample playback also uses DMA to fetch audio data bytes from CPU memory.

**Trigger:** When the DMC's sample buffer is empty and there are remaining bytes to read in the current sample, the DMC requests a DMA read.

**Timing:** Each DMC DMA read stalls the CPU for 1-4 cycles depending on the CPU's current state:
- 4 cycles if the CPU is performing a write cycle
- 3 cycles if the CPU is performing a read cycle on a non-get cycle
- 2 cycles if the CPU is performing the penultimate cycle of an instruction
- 1 cycle if aligned perfectly

**Conflict with OAM DMA:** DMC DMA can interrupt OAM DMA. If a DMC read is requested during OAM DMA, the OAM transfer pauses for the DMC read, then resumes. This can cause a "glitch byte" — the DMC read interferes with the OAM read, causing a byte in OAM to be corrupted. Some games are affected by this (slight sprite glitch for one frame).

**OxideNES Implementation:** DMC DMA is handled in the APU's tick method. When the sample buffer empties, the APU sets a `dmc_dma_request` flag. The bus checks this flag each clock cycle and, when set, stalls the CPU for the appropriate number of cycles while routing the memory read to the DMC.

## DMA and Cycle Accuracy

Accurate DMA emulation is critical for NES timing. Games that use sprite-0 hit for raster effects depend on OAM DMA completing at exactly the right time. If DMA takes too few or too many cycles, the sprite-0 hit detection occurs at the wrong scanline position, causing visual glitches. OxideNES counts DMA cycles exactly, including the odd-cycle alignment penalty.
