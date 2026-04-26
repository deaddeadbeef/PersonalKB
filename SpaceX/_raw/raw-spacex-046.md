---
tags: [spacex, raw]
source_type: technical_paper
source_title: "Autogenous Pressurization System"
authors: ["SpaceX"]
year: 2023
url: https://www.spacex.com/vehicles/starship/
---

## Summary

One of Starship's most consequential but least publicized innovations is its autogenous pressurization system, which eliminates the traditional reliance on helium for propellant tank pressurization. In conventional launch vehicles—including SpaceX's own Falcon 9—high-pressure helium stored in composite overwrapped pressure vessels (COPVs) is used to maintain tank pressure as propellant is consumed. Starship instead uses heated propellant gases: gaseous methane pressurizes the fuel tank, and gaseous oxygen pressurizes the oxidizer tank. This gas is tapped from the Raptor engine cycle, heated to appropriate temperatures, and routed back to the respective tanks. The approach eliminates helium dependency entirely, simplifies vehicle plumbing, removes COPV failure modes, and critically enables Mars operations where helium is unavailable.

## Key Claims

- Starship's autogenous pressurization system replaces helium with heated propellant vapors—gaseous methane for the CH₄ tank and gaseous oxygen for the LOX tank—tapped from the Raptor engine's gas generator or preburner cycle.
- Falcon 9 relies on helium stored in COPVs submerged in the LOX tank, a system associated with the September 2016 Amos-6 pad explosion caused by solid oxygen formation in COPV liner wrinkle voids; autogenous pressurization eliminates this failure mode entirely.
- Helium is expensive ($30–100+ per kilogram depending on purity and availability), supply-constrained (derived as a byproduct of natural gas extraction), and subject to periodic global shortages that could limit launch cadence for vehicles dependent on it.
- Mars compatibility is a primary design driver: there is no known accessible helium source on Mars, so any vehicle intended for Mars surface refueling and return must use pressurants that can be sourced or manufactured locally.
- The elimination of COPVs removes a significant structural and safety concern, as these vessels operate at pressures exceeding 300 bar and represent a stored-energy hazard during vehicle processing and flight.

## Atomic Facts

1. Autogenous pressurization works by diverting a small fraction of propellant through a heat exchanger or engine tap, vaporizing it, and routing the warm gas back to the top of the respective propellant tank to maintain ullage pressure.
2. The Raptor engine's full-flow staged combustion cycle is particularly well-suited to autogenous pressurization because both propellants are fully gasified before entering the main combustion chamber, providing convenient tap points for pressurization gas.
3. Helium's role in Falcon 9 extends beyond tank pressurization to include pneumatic actuation of valves; Starship replaces these functions with propellant gas or electric actuators.
4. COPV elimination removes approximately dozens of high-pressure vessels per vehicle, reducing both mass and the integration labor associated with helium system leak checks and proof testing.
5. The autogenous system must precisely regulate gas temperature and flow rate to maintain stable tank pressure without overcooling (which would cause condensation and pressure collapse) or overheating (which could damage tank walls).
6. SpaceX's decision to use autogenous pressurization on Starship was informed by COPV-related anomalies on Falcon 9 and the strategic requirement for Mars In-Situ Resource Utilization (ISRU) compatibility.

## Significance

Autogenous pressurization is one of Starship's foundational architectural decisions, enabling the vehicle's Mars mission profile while simultaneously improving reliability and reducing operational costs compared to helium-dependent systems. It exemplifies SpaceX's approach of solving near-term engineering problems (helium cost and supply) with solutions that also address long-term strategic goals (Mars surface operations).

## Chunks Extracted

*Pending*
