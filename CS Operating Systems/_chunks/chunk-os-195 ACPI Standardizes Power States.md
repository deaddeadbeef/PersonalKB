---
id: chunk-csos-195
type: chunk
source: "[[raw-os-037]]"
source_loc: "Power Management in OS"
topic: "design"
claim: "ACPI defines a standardized firmware interface for OS power management including system sleep states (S0-S5), processor idle states (C-states), and performance states (P-states)"
confidence: verified
supports:
  - "[[Power Management]]"
tags:
  - csos
  - csos/design
  - chunk
up: "[[CS Operating Systems]]"
---
# Design — ACPI standardizes OS power state management

## Context

ACPI provides system sleep states: S0 (operational), S3 (suspend-to-RAM, ~1-5W, resumes in 1-3s), S4 (hibernate to disk), S5 (soft-off). Processor C-states control idle power: C0 (active), C1 (halt, ~10 us wake), C3 (sleep, ~1 ms wake). P-states use DVFS (Dynamic Voltage and Frequency Scaling) for active power control. Modern Intel CPUs use HWP (Hardware P-states) for autonomous frequency adjustment.

## Why It Matters

ACPI is the universal interface between OS and hardware power management. Understanding sleep states, C-states, and P-states explains laptop battery life, server energy costs, and why the OS must balance latency requirements against power savings.

## QnA Seeds

- Q: What are ACPI system sleep states S0 through S5?
- Q: How do C-states trade power savings for wake-up latency?
- Q: What is the difference between C-states and P-states?
