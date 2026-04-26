---
id: chunk-csa-054
type: chunk
source: "[[Erickson 2019 - Algorithms]]"
source_loc: "Chapter 13 — Approximation Algorithms"
topic: "complexity"
claim: "The list-scheduling greedy algorithm for identical-machine load balancing achieves a (2 − 1/m)-approximation, proved by bounding the algorithm's makespan against OPT through the average-load and maximum-job-length intermediate quantities"
confidence: verified
supports:
  - "[[Approximation Algorithms]]"
tags:
  - csa
  - csa/complexity
  - chunk
up: "[[CS Algorithms]]"
---
# Complexity — List scheduling approximation for load balancing achieves a (2 − 1/m) factor guarantee

## Context

**Problem**: assign n jobs with processing times p₁, …, pₙ to m identical machines to minimise the makespan (the time when the last job finishes).

**List scheduling algorithm**: assign each job in turn to the currently least-loaded machine.

**Approximation guarantee**: the makespan produced is at most (2 − 1/m) · OPT.

**Proof (correct derivation)**:

Let W = Σpₖ (total work), let T be the algorithm's makespan, and let j be the last job to finish. Before j is assigned, only W − pⱼ work has been scheduled across all m machines. Because list scheduling assigns j to the **least-loaded** machine, that machine's prior load is at most (W − pⱼ)/m. Therefore:

```
T = (machine load before j) + pⱼ
  ≤ (W − pⱼ)/m + pⱼ
  = W/m + (1 − 1/m)pⱼ
  ≤ OPT + (1 − 1/m)·OPT
  = (2 − 1/m)·OPT
```

using **W/m ≤ OPT** (any valid schedule must process all W work across m machines) and **pⱼ ≤ OPT** (no single job can exceed the optimal makespan). □

**Why this matters**: load balancing is a practical NP-hard problem and this result shows the two-step proof template in action: the intermediate bounds are (1) W/m ≤ OPT and (2) pⱼ ≤ OPT.

## QnA Seeds

- Q: What is the list-scheduling algorithm for load balancing and what approximation ratio does it achieve?
- Q: What two intermediate bounds are used to prove the (2 − 1/m) guarantee for list scheduling?
- Q: Why does the approximation ratio for list scheduling approach 2 as m → ∞?
