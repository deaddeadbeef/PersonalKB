---
id: chunk-csos-197
type: chunk
source: "[[raw-os-037]]"
source_loc: "Power Management in OS"
topic: "design"
claim: "DVFS exploits the cubic relationship P proportional to V-squared times f to achieve significant energy savings by reducing both CPU voltage and frequency together"
confidence: verified
supports:
  - "[[Power Management]]"
tags:
  - csos
  - csos/design
  - chunk
up: "[[CS Operating Systems]]"
---
# Design — DVFS uses cubic voltage-power relationship

## Context

Dynamic Voltage and Frequency Scaling reduces voltage and frequency proportionally, saving power approximately cubically with voltage reduction (P is proportional to V-squared times f). Linux implements this via cpufreq governors: performance (max frequency), powersave (minimum), ondemand (reactive scaling), and schedutil (scheduler-integrated, sets frequency proportional to util_avg). The race-to-idle strategy — running at max speed then entering deep sleep — is often more efficient than slow sustained execution.

## Why It Matters

DVFS is the primary mechanism for active power management. Understanding the cubic relationship explains why even small voltage reductions yield large power savings, and why race-to-idle can beat sustained low-frequency operation due to leakage power dominance.

## QnA Seeds

- Q: Why does reducing voltage save power cubically rather than linearly?
- Q: What are the Linux cpufreq governors and how do they differ?
- Q: Why is race-to-idle sometimes more efficient than running at low frequency?
