---
tags: [spacex, raw]
source_type: technical_analysis
source_title: "Avionics and Flight Software"
authors: ["SpaceX"]
year: 2022
url: https://www.spacex.com/
---

## Summary

SpaceX's avionics and flight software architecture represents a deliberate departure from traditional aerospace approaches that rely on expensive radiation-hardened processors and formally verified software. Instead, SpaceX employs commercial-off-the-shelf (COTS) x86 Linux-based flight computers in a triple-redundant voting architecture, where three independent computers execute the same calculations simultaneously and a majority-vote mechanism masks single-point failures. This approach trades per-unit radiation hardness for system-level fault tolerance, enabling the use of vastly more powerful (and cheaper) processors. The software stack spans autonomous docking, propulsive landing guidance, satellite constellation management, and human-rated crew vehicle operations.

## Key Claims

- Falcon 9 and Starship use triple-redundant x86 flight computers running Linux, where three identical computers process sensor inputs independently, and a voting system selects the majority output—masking single-event upsets or hardware failures without rad-hardened components.
- Dragon crew vehicles employ a different avionics philosophy with radiation-hardened processors for crew safety, reflecting NASA human-rating requirements that demand higher single-unit reliability for crewed missions.
- SpaceX developed custom avionics boards in-house, including flight computers, power distribution units, and sensor interface cards, maintaining its vertical integration philosophy in electronics as well as structures and propulsion.
- The G-FOLD (Guidance for Fuel-Optimal Large Diverts) algorithm, based on convex optimization principles, enables real-time computation of fuel-optimal landing trajectories for Falcon 9 booster recovery and is adapted for Starship landing guidance.
- Starlink satellite avionics include autonomous collision avoidance systems that process conjunction data and execute maneuvers without ground operator intervention, managing a constellation of thousands of satellites in low Earth orbit.

## Atomic Facts

1. The triple-redundant voting architecture operates on a principle where if one of three computers produces a divergent output (due to a radiation-induced bit flip or hardware fault), the other two outvote it and the faulty unit is flagged for monitoring or reset.
2. Using COTS x86 processors (rather than space-grade rad-hardened chips costing 10–100x more) gives SpaceX access to processor performance generations ahead of traditional space-qualified hardware, enabling more complex real-time algorithms.
3. Dragon's touchscreen-based crew interface runs on separate display computers from the flight-critical avionics, ensuring that a display system failure cannot affect vehicle control.
4. The G-FOLD algorithm solves a convex optimization problem in real time to compute a fuel-optimal trajectory from any point in the landing approach envelope to the target landing site, accounting for aerodynamic drag, thrust constraints, and exclusion zones.
5. Starlink satellites use krypton-fueled Hall-effect ion thrusters for orbit raising and station-keeping, controlled by onboard avionics that autonomously plan and execute maneuvers based on orbital parameters and conjunction warnings.
6. SpaceX's flight software development follows an iterative software engineering process with extensive hardware-in-the-loop simulation, rather than the DO-178C formal verification process used in traditional aerospace avionics certification.

## Significance

SpaceX's avionics philosophy demonstrates that system-level redundancy can substitute for component-level hardening, enabling dramatically lower costs and higher computational performance. The G-FOLD algorithm's real-time convex optimization approach has become a benchmark in aerospace guidance, and the Starlink constellation's autonomous operations at scale represent the most complex distributed satellite management system ever deployed.

## Chunks Extracted

*Pending*
