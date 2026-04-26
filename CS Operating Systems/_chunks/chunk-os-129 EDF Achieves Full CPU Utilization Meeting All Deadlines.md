---
id: chunk-csos-129
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 10 — Real-Time Operating Systems"
topic: "scheduling"
claim: "Earliest Deadline First (EDF) dynamically assigns the highest priority to the task with the nearest deadline; it is optimal among all uniprocessor scheduling algorithms and achieves 100% CPU utilization while meeting all deadlines"
confidence: verified
supports:
  - "[[CPU Scheduling]]"
tags:
  - csos
  - csos/scheduling
  - chunk
up: "[[CS Operating Systems]]"
---
# Scheduling — EDF achieves 100% CPU utilization while meeting all deadlines

## Context

Earliest Deadline First (EDF) dynamically assigns priority at each scheduling point — whichever task has the nearest absolute deadline gets the CPU. Unlike RMS with its ~69.3% utilization ceiling, EDF can schedule any task set whose total utilization does not exceed 100%, making it optimal among all uniprocessor scheduling algorithms. The tradeoff is higher runtime overhead: priorities must be recalculated at each scheduling event based on absolute deadlines, whereas RMS priorities are static. For resource-constrained embedded systems, EDF's ability to use more of the CPU without missing deadlines often outweighs its scheduling overhead.

## Why It Matters

EDF's 100% utilization bound means fewer physical resources are wasted — critical in embedded systems with limited hardware. The RMS vs. EDF choice illustrates a recurring systems tradeoff: simplicity and predictability (static RMS) vs. optimality and complexity (dynamic EDF).

## QnA Seeds

- Q: Why can EDF achieve 100% utilization while RMS cannot?
- Q: What is EDF's runtime overhead compared to RMS?
- Q: When is EDF preferred over RMS in practice?
