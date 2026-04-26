---
id: chunk-csos-128
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 10 — Real-Time Operating Systems"
topic: "scheduling"
claim: "Rate-Monotonic Scheduling assigns fixed priorities based on period — shorter period means higher priority; Liu and Layland (1973) proved it optimal among fixed-priority algorithms with a utilization bound converging to ln(2) ≈ 69.3%"
confidence: verified
supports:
  - "[[CPU Scheduling]]"
tags:
  - csos
  - csos/scheduling
  - chunk
up: "[[CS Operating Systems]]"
---
# Scheduling — Rate-monotonic scheduling is optimal among fixed-priority algorithms

## Context

Rate-Monotonic Scheduling (RMS) assigns static priorities inversely proportional to task period — the task that runs most frequently gets the highest priority. Liu and Layland (1973) proved this optimal among all fixed-priority preemptive algorithms: if any fixed-priority assignment can schedule a task set, RMS can too. The utilization bound is U ≤ n(2^(1/n) − 1), which gives 100% for 1 task, 82.8% for 2, 78.0% for 3, and converges to ln(2) ≈ 69.3% as n → ∞. This bound is sufficient but not necessary — task sets exceeding it may still be schedulable depending on period relationships.

## Why It Matters

RMS provides a provable guarantee: if your total CPU utilization is under the bound, all deadlines will be met. This transforms real-time scheduling from trial-and-error testing into mathematical engineering. The ~30% "wasted" utilization at the bound is the price of deterministic correctness — a tradeoff gladly made in safety-critical systems.

## QnA Seeds

- Q: Why does RMS assign higher priority to shorter-period tasks?
- Q: What is the Liu and Layland utilization bound and what happens as n → ∞?
- Q: Why is the RMS utilization bound sufficient but not necessary?
