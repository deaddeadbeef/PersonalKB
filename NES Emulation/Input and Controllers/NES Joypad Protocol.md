---
tags: [nes, wiki]
up: "[[Input and Controllers Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---

# NES Joypad Protocol

> **The serial shift-register protocol that reads 8 button states through a strobe-latch-and-shift sequence at $4016/$4017.**

## 🎯 Intuition
**The Core Idea:** The NES reads controllers through a serial shift register — a strobe signal latches all 8 button states, then 8 sequential reads shift out one bit at a time.
**Analogy:** Like a snapshot camera at a turnstile — the strobe captures everyone's position at one instant, then you check each person one-by-one as they pass through.
**Why It Matters:** Every NES game reads input through this protocol. Get it wrong and all input breaks — there's no fallback mechanism.

---

## ⚙️ Core Mechanics
### How It Works
The NES reads controllers through a serial shift register protocol:

1. **Strobe:** CPU writes 1 then 0 to $4016 — this latches all button states
2. **Read:** Each read from $4016 (P1) or $4017 (P2) shifts out one button bit
3. **Bit order:** A, B, Select, Start, Up, Down, Left, Right (bits 0–7)

### Key Specifications

| Step | CPU Action | Address | Effect |
|------|-----------|---------|--------|
| 1 | Write 1 | $4016 | Strobe ON — continuously samples buttons |
| 2 | Write 0 | $4016 | Strobe OFF — latches current button state |
| 3 | Read | $4016 | Returns bit 0 (A button), shifts register |
| 4 | Read | $4016 | Returns bit 1 (B button), shifts register |
| … | Read × 6 more | $4016 | Bits 2–7 (Select, Start, Up, Down, Left, Right) |
| 11 | Read | $4016 | Returns 1 (open bus after 8 reads) |

### Key Facts
- The strobe signal (write 1 then 0 to $4016) latches button state on the falling edge (1→0 transition)
- Button bits are read LSB-first: A, B, Select, Start, Up, Down, Left, Right
- After 8 reads, the shift register returns 1 for all subsequent reads (open bus)
- P1 is read from $4016, P2 from $4017
- Some games read more than 8 times to detect specific controller types (Zapper, Power Pad)

---

## 🔬 Deep Dive
### Strobe Behavior
While the strobe is held high (1 written to $4016), the controller continuously samples button states — reads during this time always return the current state of the A button. Only when the strobe goes low (0 written) are button states latched into the shift register for sequential readout.

### Open Bus After 8 Reads
After all 8 button bits have been shifted out, subsequent reads return 1 (the open bus value). Some games exploit this behavior:
- Reading more than 8 times to detect special controllers (Zapper, Power Pad, Four Score)
- Using the open bus value as a sentinel to detect the end of valid data

### Timing Detail
```
CPU writes $4016 = 1  → Strobe ON (continuously samples buttons)
CPU writes $4016 = 0  → Strobe OFF (latches current state)
CPU reads $4016       → Returns bit 0 (A button), shifts register
CPU reads $4016       → Returns bit 1 (B button), shifts register
... 8 reads total ...
CPU reads $4016       → Returns 1 (open bus after 8 reads)
```

### Reference Implementations
joypad.rs `write()` handles the strobe signal. On strobe falling edge (1→0), button state is latched into the shift register. Each `read()` returns the LSB and shifts right. After 8 shifts, returns 1.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What sequence of writes to $4016 latches the button states into the shift register?
2. In what order are the 8 button bits shifted out?
3. What value is returned after all 8 buttons have been read?

### Core Problems
1. **Shift Register:** Implement a joypad shift register. Support `write()` for strobe control and `read()` for shifting out bits. Verify the sequence: strobe ON, strobe OFF, then 8 reads return A, B, Select, Start, Up, Down, Left, Right in order.
2. **Two-Player Reads:** Extend your implementation to handle both $4016 (P1) and $4017 (P2) with independent shift registers. Verify that reading P1 does not affect P2's state.

### Challenge
**Controller Detection:** Some games read more than 8 times from $4016 to detect peripherals like the Zapper or Four Score. Implement extended read behavior where reads 9+ return open bus (1), and write a test that distinguishes a standard controller from a simulated Four Score by checking the signature bits at positions 19–24.

---

*See also:* [[Controller Features in OxideNES]], [[Input and Controllers Overview]]

## References
→ [[NES Emulation/Sources/Sources Index|Sources Index]]
