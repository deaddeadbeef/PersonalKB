---
tags: [nes, wiki]
up: "[[CPU — The 6502 Processor Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# Interrupts — NMI, IRQ, and Reset

> **The three hardware signals that preempt normal CPU execution: Reset initializes, NMI syncs with the PPU, and IRQ enables mapper/APU-driven events.**

## 🎯 Intuition
**The Core Idea:** Interrupts are the hardware's way of tapping the CPU on the shoulder and saying "stop what you're doing and handle this" — they're the fundamental mechanism for real-time coordination between the CPU and other chips.
**Analogy:** Think of the CPU as a worker reading through a checklist (program). Reset is the boss saying "start over from the beginning." NMI is an urgent alarm that can't be ignored (fire drill) — it happens every frame when VBlank starts. IRQ is a polite knock on the door that can be ignored if the worker put up a "do not disturb" sign (I flag).
**Why It Matters:** NMI is the heartbeat of every NES game — it fires 60 times per second at VBlank and drives the main game loop. Getting NMI timing wrong by even one cycle can cause graphical corruption; getting IRQ wrong breaks mapper-driven games entirely.

---

## ⚙️ Core Mechanics
### How It Works
When an interrupt is detected at an instruction boundary, the CPU performs a 7-cycle sequence: push PC and status register to the stack, set the I flag, and load the new PC from the appropriate vector in the top of memory.

### Key Specifications

**Three Interrupt Types**

| Interrupt | Vector | Priority | Maskable | Trigger |
|-----------|--------|----------|----------|---------|
| **RESET** | 0xFFFC-0xFFFD | Highest | No | Power on / reset button |
| **NMI** | 0xFFFA-0xFFFB | High | No | PPU vertical blank (pin edge) |
| **IRQ** | 0xFFFE-0xFFFF | Normal | Yes (I flag) | APU frame, mapper, BRK |

**Interrupt Sequence (7 cycles)**
1. Push PC high byte to stack
2. Push PC low byte to stack
3. Push P register (with B=0 for hardware, B=1 for BRK)
4. Set I flag (disable further IRQs)
5. Load PC from interrupt vector

### Key Facts
- **NMI is edge-triggered** — it fires on the 0→1 transition of the NMI line, not while it is held high
- **IRQ is level-triggered** — it fires continuously as long as the IRQ line is held low and I flag is clear
- **NMI is the primary synchronization mechanism** between CPU and PPU — game main loops typically wait for NMI to update graphics during vblank
- IRQ sources on the NES: APU frame counter (4-step mode), mapper IRQs (MMC3, MMC5, VRC, FME7), DMC completion
- Toggling PPUCTRL bit 7 can trigger additional NMIs due to edge detection

---

## 🔬 Deep Dive
### Hardware Behavior Details
**NMI Edge Detection:** The PPU asserts NMI at the start of vertical blank (scanline 241, dot 1) if the NMI enable bit (PPUCTRL bit 7) is set. Because NMI is edge-triggered, toggling PPUCTRL bit 7 off and on during VBlank can generate a second NMI. This is used by some games intentionally.

**NMI Suppression:** Reading PPUSTATUS (0x2002) at the exact cycle when VBlank begins can suppress the NMI entirely — the VBlank flag is cleared before the edge detector sees it.

**IRQ Acknowledge:** Unlike NMI, IRQ has no automatic acknowledge. The CPU sets the I flag during the interrupt sequence, but the source must be explicitly cleared (e.g., reading APU status register) or IRQ will fire again immediately after RTI clears I.

**Interrupt Hijacking:** If NMI occurs during an IRQ's push sequence, the NMI can "hijack" the IRQ — the pushed return address is from the IRQ, but the vector loaded is NMI's vector.

### Common Emulation Pitfalls
1. **Polling NMI incorrectly** — NMI must be detected at instruction boundaries, not mid-instruction. Checking at the wrong time can cause NMI to fire one instruction too early or late
2. **Treating NMI as level-triggered** — If you fire NMI every cycle that the VBlank flag is set (instead of on the edge), games will receive dozens of spurious NMIs and crash
3. **Not consuming the NMI pending flag** — After servicing NMI, the pending flag must be cleared. Forgetting this causes infinite NMI loops

### Reference Implementations
The OxideNES `Bus` struct provides `poll_nmi()`, `poll_apu_irq()`, and `poll_mapper_irq()` methods. The main loop checks these at instruction boundaries. NMI and IRQ pending flags are consumed (cleared) after being serviced.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why can't the CPU ignore an NMI even if the I flag is set?
2. What happens if a game's NMI handler takes longer than VBlank (more than ~2273 CPU cycles at ~20 scanlines)?
3. How does BRK differ from a hardware IRQ in terms of the byte pushed as the status register?

### Core Problems
1. **Implement the interrupt check:** Write the instruction-boundary logic that checks for pending NMI, then IRQ (if I flag clear), executes the 7-cycle push sequence, loads the correct vector, and clears the pending flag.
2. **NMI edge detector:** Implement a function that tracks the previous and current state of the NMI line and only triggers on a 0→1 transition. Test with rapid toggling of PPUCTRL bit 7.

### Challenge
**NMI suppression race:** The CPU reads PPUSTATUS at the exact cycle when VBlank begins (scanline 241, dot 1). Does NMI fire or get suppressed? Trace the exact sequence: at what point does the PPU set the VBlank flag, at what point does the read clear it, and at what point does the edge detector sample it? Implement this race condition and verify against known test ROM results (e.g., `vbl_nmi_timing`).

---

*See also:* [[CPU Cycle Accuracy and Timing]], [[6502 Registers and Status Flags]], [[PPU Registers and Timing]], [[CPU — The 6502 Processor Overview]]

## References
→ [[NES Emulation/Sources/Sources Index|Sources Index]]
