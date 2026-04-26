---
tags: [spacex, chunk]
source: "[[raw-spacex-011]]"
confidence: high
supports:
  - "[[Propulsive Landing Technology]]"
  - "[[Landing Hardware]]"
qna_seeds:
  - "Q: What algorithm does Falcon 9 use for landing guidance? A: SpaceX adapted the G-FOLD convex optimization algorithm, originally developed by Behçet Açıkmeşe at JPL for Mars landing, to compute fuel-optimal landing trajectories in real time with guaranteed convergence."
---

# G-FOLD Landing Guidance Algorithm

SpaceX's booster landing guidance relies on the G-FOLD (Guidance for Fuel-Optimal Large Diverts) convex optimization algorithm, originally developed by Behçet Açıkmeşe at JPL for Mars landing applications. The algorithm computes fuel-optimal trajectories in real time with guaranteed convergence, enabling supersonic retropropulsion — demonstrated operationally for the first time in spaceflight history. The landing sequence transitions autonomously from a three-engine entry burn to a single-engine landing burn, executing from MECO to touchdown in approximately eight minutes.
