---
tags: [spacex, falcon]
up: "[[Falcon Program Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Falcon Performance Specifications

> **A consolidated reference for Falcon 9 and Falcon Heavy propulsion, structural, and payload performance data — the numbers that define what SpaceX's workhorse vehicles can deliver.**

## 🎯 Intuition
**The Core Idea:** Falcon 9 and Falcon Heavy share the same Merlin engine family and LOX/RP-1 propellants, scaling from 9 to 27 engines to cover everything from routine LEO missions to interplanetary probes — all at the lowest cost-per-kg in the industry.
**Analogy:** Think of Falcon 9 as a single-cab pickup and Falcon Heavy as a triple-axle truck — same engine family, same fuel, but chained together for heavier loads at a fraction of the cost of buying a custom heavy hauler.
**Why It Matters:** Performance specifications are the bedrock on which every mission is planned. Falcon 9's specs hit a sweet spot — enough capacity for the vast majority of payloads at a price undercutting all Western competitors. Falcon Heavy extends that envelope to the super-heavy class without requiring an entirely new vehicle, leveraging shared manufacturing and operational infrastructure.

## ⚙️ Core Mechanics
### Propulsion Specifications

| Engine | Thrust (sea level) | Thrust (vacuum) | Isp (sea level) | Isp (vacuum) |
|---|---|---|---|---|
| Merlin 1D | ~845 kN (190,000 lbf) | ~914 kN (205,500 lbf) | 282 s | 311 s |
| Merlin Vacuum (MVac) | — | ~981 kN (220,500 lbf) | — | 348 s |

### Vehicle Specifications

| Parameter | Falcon 9 Block 5 | Falcon Heavy |
|---|---|---|
| First-stage engines | 9 × Merlin 1D | 27 × Merlin 1D (3 cores) |
| Liftoff thrust (kN) | ~7,607 | ~22,819 |
| Height (m) | ~70 | ~70 |
| First-stage propellant mass | ~395,700 kg | ~1,187,100 kg (3 × 395,700) |
| Second-stage propellant mass | ~107,500 kg | ~107,500 kg |
| First-stage burn time | ~162 s | ~150 s (sides) / ~187 s (centre) |
| Second-stage burn time | ~397 s | ~397 s |
| Second-stage restarts | 1 | 1 |

### Payload Capacity

| Destination | Falcon 9 Reusable | Falcon 9 Expendable | FH Reusable | FH Expendable |
|---|---|---|---|---|
| LEO (kg) | ~22,800 | ~25,000 (est.) | ~50,000 (est.) | ~63,800 |
| GTO (kg) | ~8,300 | ~11,200 (est.) | ~8,000 | ~26,700 |
| Mars transfer (kg) | ~4,020 | — | — | ~16,800 |
| Pluto transfer (kg) | — | — | — | ~3,500 |

### Cost Comparison

| Metric | Falcon 9 | Falcon Heavy |
|---|---|---|
| List price (reusable) | ~$67 M | ~$97 M |
| List price (expendable) | — | ~$150 M |
| Cost per kg to LEO (reusable) | ~$2,720 | ~$1,940 (est.) |

### Key Facts
- **Merlin 1D sea-level thrust:** ~845 kN (190,000 lbf) per engine
- **Merlin 1D vacuum thrust:** ~914 kN (205,500 lbf) per engine
- **Merlin Vacuum (MVac) thrust:** ~981 kN (220,500 lbf)
- **Merlin 1D Isp:** 282 s (sea level) / 311 s (vacuum)
- **MVac Isp:** 348 s (vacuum)
- **Falcon 9 first-stage propellant mass:** ~395,700 kg
- **Falcon 9 second-stage propellant mass:** ~107,500 kg
- **Propellants:** Sub-cooled LOX (−207 °C) and chilled RP-1 (−7 °C) on Block 5
- **Falcon 9 list price:** ~$67 M; Falcon Heavy: ~$97 M (reusable) / ~$150 M (expendable)
- **Cost per kg to LEO:** ~$2,720 (F9 reusable) — an order of magnitude less than Shuttle-era costs

## 🔬 Deep Dive
### Engineering Details
Falcon 9 Block 5 is powered by the Merlin 1D engine family. At sea level, each Merlin 1D produces approximately 845 kN of thrust with a specific impulse (Isp) of 282 seconds. In vacuum the same engine delivers roughly 914 kN at 311 seconds Isp. The first stage carries about 395,700 kg of sub-cooled LOX and chilled RP-1 and burns for approximately 162 seconds. The second-stage Merlin Vacuum (MVac) engine is optimised for space with a large nozzle expansion ratio, producing 981 kN of thrust at 348 seconds Isp. The upper stage carries approximately 107,500 kg of propellant and burns for about 397 seconds, with a single-restart capability for complex orbital profiles.

Falcon Heavy multiplies these figures by three on the first stage. With 27 Merlin 1D engines producing a combined sea-level thrust of roughly 22,819 kN, it is the most powerful operational rocket in the world. The side boosters separate first (around T+2:30), followed by the centre core (around T+3:30), and the same Falcon 9 second stage completes orbital insertion. Payload capacities scale accordingly: approximately 63,800 kg to LEO and 26,700 kg to GTO in expendable mode, falling to roughly 50,000 kg and 8,000 kg respectively when all three cores are recovered.

SpaceX lists the Falcon 9 launch price at approximately $67 million, translating to roughly $2,720 per kilogram to LEO in reusable mode — an order of magnitude less than Shuttle-era costs and significantly below any current competitor. Falcon Heavy's list price starts at roughly $97 million for the reusable configuration, offering even more dramatic cost-per-kilogram advantages on heavy missions.

### Falcon Family vs. Historical Heavy-Lift Cost

| Vehicle | Era | LEO Capacity (kg) | Approx. Cost per Launch | Cost per kg to LEO |
|---|---|---|---|---|
| Space Shuttle | 1981–2011 | ~27,500 | ~$1.5 B (avg.) | ~$54,500 |
| Delta IV Heavy | 2004–2024 | ~28,790 | ~$350 M | ~$12,150 |
| Falcon 9 Block 5 (reusable) | 2018–present | ~22,800 | ~$67 M | ~$2,720 |
| Falcon Heavy (reusable) | 2018–present | ~50,000 (est.) | ~$97 M | ~$1,940 (est.) |

## 🏋️ Practice
### Warm-Up — 3 Conceptual Questions
1. Why does the Merlin Vacuum engine achieve 348 s Isp compared to the Merlin 1D's 311 s in vacuum — what physical design difference accounts for this?
2. Explain why Falcon Heavy's GTO capacity drops from ~26,700 kg (expendable) to ~8,000 kg (fully reusable) — a far steeper percentage reduction than the LEO figures.
3. At ~$2,720/kg to LEO, Falcon 9 is roughly 20× cheaper than the Space Shuttle per kg. Identify the three largest cost drivers that changed between the two vehicles.

### Core Analysis — 2 "What If" Scenarios
1. **What if** SpaceX switched from RP-1 to methane (CH₄) on Falcon 9 (as on Starship's Raptor) — analyse the expected Isp change, tank volume implications, and whether the existing 3.7 m diameter vehicle could accommodate the switch without a complete redesign.
2. **What if** a customer needs to deliver 15,000 kg to GTO — compare a single Falcon Heavy expendable launch vs. two Falcon 9 expendable launches with on-orbit rendezvous. Analyse cost, risk, schedule, and technical feasibility.

### Challenge
1. A new space agency has a budget of $500 M for its first year of orbital operations and needs to launch 5 GTO satellites (~5,000 kg each) and 3 LEO Earth-observation satellites (~3,000 kg each). Using the performance and cost data above, design an optimal launch manifest combining Falcon 9 and Falcon Heavy options. Maximise payload margin while minimising total cost — justify vehicle selection for each mission.

## References

→ [[Sources Index]]
