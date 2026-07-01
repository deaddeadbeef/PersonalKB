---
tags: [spacex, study, drill]
up: "[[SpaceX Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice]
---
# Technology Systems — Review Drill

> 15 Q&A pairs · Avionics, TPS, structures, landing, and more
> **How to use:** Cover the **A** column, answer from memory, then check.

---

## Flight Termination & Safety

**Q1. What does AFTS stand for and what does it replace?**
> **A1.** Autonomous Flight Termination System. It replaces the traditional ground-commanded range-safety destruct system. Instead of a human range safety officer sending a destruct command, AFTS uses onboard GPS and an independent flight computer to autonomously terminate the flight if the vehicle leaves its predefined corridor.

**Q2. What are the main advantages of AFTS over legacy range safety?**
> **A2.** Eliminates the need for ground-based radar tracking and human-in-the-loop commands, enables higher launch cadence (multiple pads, faster turnover), reduces range costs, improves response time (milliseconds vs. seconds), and allows launches from sites without traditional range infrastructure.

---

## Aerodynamic Surfaces & Structures

**Q3. What material are Falcon 9 Block 5 grid fins made of, and what was used before?**
> **A3.** Block 5 uses cast/machined **titanium** grid fins. Earlier versions used aluminum fins with an ablative coating, which were single-use. Titanium fins are reusable across many flights without refurbishment.

**Q4. What is the purpose of grid fins on the Falcon 9 booster?**
> **A4.** They provide aerodynamic steering during descent through the atmosphere (hypersonic through subsonic regimes). Positioned near the top of the booster, they control roll, pitch, and yaw to guide the booster to the landing target.

**Q5. Why did SpaceX choose 304L stainless steel for Starship instead of aluminum-lithium or carbon composites?**
> **A5.** Key reasons: (1) Cost — ~$3/kg vs. $35/kg (Al-Li) or $130/kg (CFRP). (2) Cryogenic performance — steel *increases* in strength at LN₂/LOX temperatures. (3) High-temperature tolerance — retains useful strength up to ~1,100 K, reducing TPS mass requirements. (4) Weldability — field-weldable with commodity equipment. (5) Ductility — fails gracefully rather than catastrophically. (6) Rapid prototyping — easy to cut, form, and iterate.

---

## Thermal Protection

**Q6. What material are Starship's TPS tiles made of?**
> **A6.** Silica-fiber-based hexagonal tiles (similar concept to Space Shuttle tiles but a SpaceX-proprietary formulation). They are lightweight, ablation-resistant, and mechanically attached to the steel hull.

**Q7. Approximately how many TPS tiles cover Starship's windward side?**
> **A7.** ~18,000 hexagonal tiles on the windward (belly) side of the Starship upper stage.

**Q8. What was a key TPS challenge observed during early Starship flight tests?**
> **A8.** Tile loss during ascent and reentry. Gaps between tiles allowed plasma ingress that damaged the underlying steel structure. SpaceX iterated on attachment mechanisms, gap fillers, and tile geometry between IFT flights.

---

## Avionics & Software

**Q9. Describe the Falcon 9 avionics redundancy architecture.**
> **A9.** Triple-redundant flight computers running Linux on x86 processors. Each computer independently processes sensor data and calculates commands. A voting system compares outputs — if one disagrees, it is outvoted by the other two. The vehicle can lose any single flight computer and continue the mission.

**Q10. What programming languages and OS does SpaceX use for flight software?**
> **A10.** Flight software runs on **Linux**. Primary languages are **C++** for flight-critical systems and **Python** for ground support and testing. The Chromium-based displays in Dragon use **JavaScript/HTML**.

---

## Propulsion Systems & Plumbing

**Q11. What is autogenous pressurization and why does Starship use it?**
> **A11.** Autogenous pressurization uses heated propellant vapors (gaseous oxygen and gaseous methane) tapped from the engine cycle to pressurize the propellant tanks, instead of helium (He). Advantages: eliminates heavy, expensive helium COPVs and supply, simplifies plumbing, is self-regulating with engine operation, and removes a historical failure mode (helium COPV strut failure caused CRS-7 and Amos-6 anomalies).

**Q12. What landing propellant system does Falcon 9 use?**
> **A12.** A subset of the main LOX/RP-1 propellant reserved in the tanks. The booster re-ignites one or three Merlin engines (single-engine for final landing burn) using TEA-TEB hypergolic ignition fluid for each relight. Cold-gas nitrogen thrusters provide attitude control above the atmosphere.

---

## Hot Staging & Catch

**Q13. What is hot staging and what advantage does it provide for Starship?**
> **A13.** Hot staging ignites the upper-stage (Ship) engines *before* the stages physically separate. A vented interstage ring on the booster allows exhaust to escape. Advantage: eliminates the coast/gravity-loss penalty of shutting down the booster, separating, then igniting the upper stage — gaining ~10% payload to orbit.

**Q14. How does the Mechazilla tower catch system work?**
> **A14.** The launch tower ("Mechazilla") has two large hydraulic arms ("chopsticks") that close around the descending Super Heavy booster, catching it by hardpoints/grid fins near the top of the vehicle. This eliminates the need for landing legs on the booster, saving dry mass, and positions the booster directly back on the launch mount for rapid restacking.

**Q15. What was the first flight to demonstrate a successful booster tower catch?**
> **A15.** IFT-5 (13 October 2024) achieved the first successful tower catch of a Super Heavy booster.

## References

- [[SpaceX/Study/SpaceX Study Index]]
- [[SpaceX/Sources/Sources Index]]
- [[SpaceX/SpaceX Book Reading Spine]]
