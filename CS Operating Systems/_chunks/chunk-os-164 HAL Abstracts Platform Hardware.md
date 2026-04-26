---
id: chunk-csos-164
type: chunk
source: "[[raw-os-029]]"
source_loc: "Windows NT Kernel Architecture"
topic: "case-studies"
claim: "The HAL provides a uniform interface to platform-specific hardware, allowing the same kernel binary to run on different hardware with only HAL replacement"
confidence: verified
supports:
  - "[[Windows NT Architecture]]"
tags:
  - csos
  - csos/case-studies
  - chunk
up: "[[CS Operating Systems]]"
---
# Case Studies — HAL abstracts platform hardware differences

## Context

The Hardware Abstraction Layer sits at the lowest level, abstracting differences in interrupt controllers, timers, DMA, and multiprocessor management. IRQL (Interrupt Request Level) ranges from PASSIVE_LEVEL (0, normal threads) to HIGH_LEVEL (31, machine check), with higher IRQL code preempting lower. The HAL enables hardware portability without recompiling the kernel.

## Why It Matters

The HAL is a clean example of the mechanism/policy separation principle. It explains how Windows runs across diverse hardware platforms and why hardware vendors provide HAL-level drivers. Understanding IRQL is essential for Windows driver development.

## QnA Seeds

- Q: What hardware differences does the HAL abstract?
- Q: What is IRQL and how does it relate to interrupt priority?
- Q: How does the HAL enable kernel portability across hardware platforms?
