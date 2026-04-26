---
id: chunk-csa-200
type: chunk
source: "[[Cormen 2022 - Linear Programming]]"
source_loc: "LP Relaxation"
topic: "optimization"
claim: "LP relaxation of integer programs provides bounds for branch-and-bound; network flow problems have totally unimodular matrices guaranteeing integer LP solutions"
confidence: verified
supports:
  - "[[Linear Programming]]"
  - "[[Integer Programming]]"
tags:
  - csa
  - csa/optimization
  - chunk
up: "[[CS Algorithms]]"
---
# Optimization — LP relaxation provides integer programming bounds

## Context

LP relaxation replaces integer constraints with linear ones (x in {0,1} becomes 0 <= x <= 1), yielding a tractable lower bound for minimization problems. The tightness of this bound determines branch-and-bound solver efficiency. Network flow problems (max flow, min-cost flow, assignment) are special LP cases with totally unimodular constraint matrices, guaranteeing that LP relaxation solutions are automatically integer—no rounding needed. This explains why network flow is polynomial despite being expressible as integer programming.

## Why It Matters

LP relaxation is the bridge between tractable and intractable optimization—understanding it explains why branch-and-bound works and why network flow is efficient despite its IP formulation.

## QnA Seeds

- Q: What does LP relaxation replace in an integer program?
- Q: Why does total unimodularity guarantee integer LP solutions?
- Q: How does LP relaxation bound quality affect branch-and-bound performance?
