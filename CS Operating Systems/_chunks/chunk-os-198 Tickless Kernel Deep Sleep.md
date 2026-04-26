---
id: chunk-csos-198
type: chunk
source: "[[raw-os-037]]"
source_loc: "Power Management in OS"
topic: "design"
claim: "The tickless kernel eliminates periodic timer interrupts on idle CPUs, allowing sustained deep C-state residency and reducing idle power consumption by up to 20-30%"
confidence: verified
supports:
  - "[[Power Management]]"
tags:
  - csos
  - csos/design
  - chunk
up: "[[CS Operating Systems]]"
---
# Design — Tickless kernel enables sustained deep CPU sleep

## Context

Traditional kernels use periodic timer ticks (250 or 1000 Hz) that wake every CPU hundreds of times per second even when idle, preventing deep C-state residency. CONFIG_NO_HZ eliminates ticks on idle CPUs. CONFIG_NO_HZ_FULL extends this to busy CPUs for real-time workloads. Android Doze mode (Android 6.0+) batches background activity into infrequent maintenance windows when the device is stationary with screen off.

## Why It Matters

The tickless kernel was a major breakthrough for power efficiency. Understanding why periodic interrupts waste energy explains why it reduces server idle power by 20-30% and why mobile OS power management requires aggressive timer coalescing.

## QnA Seeds

- Q: What problem does the tickless kernel solve for idle CPU power?
- Q: What is CONFIG_NO_HZ and how does it differ from CONFIG_NO_HZ_FULL?
- Q: How does Android Doze mode extend power management concepts?
