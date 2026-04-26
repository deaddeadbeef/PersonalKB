---
tags: [raw, nes-emulation, history]
source: "NES hardware history references"
---

# Raw NES 023 — NES Hardware History and Design

The Nintendo Entertainment System (NES), known as the Famicom (Family Computer) in Japan, was a pivotal console that revived the video game industry after the 1983 crash. Its hardware design reflects the cost-optimization philosophy of 1983-era consumer electronics.

## Timeline

- **1983 July 15:** Famicom launches in Japan for ¥14,800 (~$100 USD). Initial units have a defective chip that causes freezing — Nintendo recalls and replaces all units with a new motherboard revision.
- **1985 October 18:** NES launches in US test markets (New York). Bundled with R.O.B. (Robotic Operating Buddy) to market it as a "toy" rather than a "video game console" — distancing from the crashed Atari-era market.
- **1986:** US nationwide launch. Zelda and Metroid release, establishing the NES as a serious gaming platform.
- **1988:** NES reaches 33% of US households. Third-party developer ecosystem thrives under Nintendo's lockout chip (10NES) and licensing program.
- **1990s:** Super NES launches (1991 Japan, 1991 US) but NES continues selling. Last official NES game in North America: Wario's Woods (1994).
- **1995:** NES officially discontinued in North America. Total lifetime sales: ~61.9 million units worldwide.

## Key Hardware Designers

- **Masayuki Uemura:** Lead architect of the Famicom/NES. Made the critical decision to use the Ricoh 2A03 (a 6502 variant with built-in audio) to reduce chip count and cost.
- **Ricoh:** Manufactured the 2A03 CPU and 2C02 PPU as custom silicon. The 6502 core was licensed from MOS Technology with the BCD mode disabled to avoid patent royalties.

## Design Philosophy

The NES was designed for maximum capability per dollar:
- **CPU (Ricoh 2A03):** Combined a 6502 CPU core with APU on one chip, saving board space and cost. The PSG-style audio channels eliminated the need for a separate sound chip.
- **PPU (Ricoh 2C02):** Dedicated graphics processor handling scrolling, sprites, and background rendering in hardware. This freed the CPU from pixel-level work — a key advantage over home computers of the era.
- **Cartridge bus:** Exposed raw address/data lines to the cartridge, enabling mapper hardware to extend capabilities. This was revolutionary — it meant the console could grow in capability without hardware revisions.
- **2 KB RAM + 2 KB VRAM:** Minimal onboard memory kept costs down. Game-specific RAM was placed on cartridges where needed.

## Regional Differences

- **Famicom (Japan):** 60-pin cartridge connector, hardwired controllers (no detachable), microphone on controller 2, expansion port on front, RF output only.
- **NES (North America/Europe):** 72-pin front-loading cartridge connector, detachable controllers, no microphone, expansion port on bottom (rarely used), RF + composite output. The front-loading design was chosen to differentiate from top-loading consoles associated with the 1983 crash, but the ZIF (Zero Insertion Force) connector was prone to reliability issues (the "blinking screen" problem).

## The 10NES Lockout Chip

The NES included the CIC (Checking Integrated Circuit) lockout chip — a security system requiring authorized cartridges to contain a matching chip. This gave Nintendo control over third-party publishing (requiring licensing and approval). It was eventually circumvented by voltage spike techniques (Tengen/Atari), leading to legal battles.
