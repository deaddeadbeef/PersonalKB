---
id: chunk-csos-127
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 10 — Real-Time Operating Systems"
topic: "scheduling"
claim: "In hard real-time systems, missing a deadline constitutes system failure — an airbag controller that deploys 100ms late is functionally useless; in soft real-time, occasional misses degrade quality but are tolerable, as in video streaming dropped frames"
confidence: verified
supports:
  - "[[CPU Scheduling]]"
tags:
  - csos
  - csos/scheduling
  - chunk
up: "[[CS Operating Systems]]"
---
# Scheduling — Hard real-time treats a missed deadline as system failure

## Context

Real-time operating systems guarantee that tasks meet timing deadlines. The fundamental distinction is between hard and soft real-time. In hard real-time systems (airbag controllers, anti-lock brakes, pacemakers), missing a deadline means the result is worthless or dangerous — correctness requires both the right answer and timely delivery. In soft real-time systems (video/audio streaming, UI responsiveness), occasional deadline misses cause quality degradation (a dropped frame, a UI stutter) but are tolerable. This distinction drives all subsequent design decisions: scheduling algorithm choice, interrupt latency requirements, and certification standards.

## Why It Matters

Understanding the hard/soft distinction prevents over-engineering (applying hard real-time techniques to soft real-time problems) and under-engineering (using general-purpose scheduling for safety-critical systems). It also explains why RTOS kernels (FreeRTOS, VxWorks, QNX) exist as a separate category from general-purpose kernels.

## QnA Seeds

- Q: What is the difference between hard and soft real-time systems?
- Q: Give an example where a missed hard real-time deadline causes physical harm.
- Q: Why can't a general-purpose OS like Linux serve as a hard real-time system?
