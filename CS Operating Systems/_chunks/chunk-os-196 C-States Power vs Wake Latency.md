---
id: chunk-csos-196
type: chunk
source: "[[raw-os-037]]"
source_loc: "Power Management in OS"
topic: "design"
claim: "C-states control idle CPU power by progressively shutting down components: deeper states save more power but require longer wake-up transitions measured in microseconds to milliseconds"
confidence: verified
supports:
  - "[[Power Management]]"
tags:
  - csos
  - csos/design
  - chunk
up: "[[CS Operating Systems]]"
---
# Design — Deeper C-states save power at wake-up latency cost

## Context

C0 is active execution. C1 halts the clock (~10 us wake). C2 stops the clock (~100 us wake). C3 flushes caches and enters sleep (~1 ms wake). The Linux intel_idle or acpi_idle driver selects states based on expected idle duration using the menu or TEO governor. The idle state selection is latency-sensitive: choosing too deep a state adds unacceptable wake-up delay for latency-critical workloads.

## Why It Matters

C-state selection is a continuous optimization problem the OS solves thousands of times per second. Understanding the latency-power tradeoff explains why real-time systems disable deep C-states and why server tuning guides often recommend specific C-state limits.

## QnA Seeds

- Q: What components are shut down progressively through C-states?
- Q: How does the Linux kernel select which C-state to enter?
- Q: Why might a latency-sensitive workload disable deep C-states?
