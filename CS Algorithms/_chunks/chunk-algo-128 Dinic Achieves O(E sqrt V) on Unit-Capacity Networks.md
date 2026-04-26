---
id: chunk-algo-128
type: chunk
source: "[[raw-algo-022]]"
source_loc: "Network Flow - Atomic Facts"
topic: "network-flow"
claim: "Dinic's algorithm achieves O(V^2*E) for general networks via blocking flows and level graphs, improving to O(E*sqrt(V)) on unit-capacity networks where at most O(sqrt(V)) phases are needed."
confidence: verified
supports:
  - "[[Network Flow]]"
  - "[[Dinic's Algorithm]]"
tags:
  - cs-algorithms
  - cs-algorithms/network-flow
  - chunk
up: "[[CS Algorithms]]"
---
# Dinic Achieves O(E sqrt V) on Unit-Capacity Networks

## Context

Dinic constructs a level graph via BFS, then finds blocking flows using DFS. After each phase, shortest s-t path length increases by >= 1, limiting phases to O(V). Each phase costs O(VE). On unit-capacity networks, at most O(sqrt(V)) phases suffice (residual shortest path eventually exceeds sqrt(V), leaving few augmentations), and each phase costs O(E), giving O(E*sqrt(V)). Push-relabel offers O(V^2*E) or O(V^3) alternatives.

## Why It Matters

Dinic's O(E*sqrt(V)) on unit-capacity networks is the fastest known general approach for bipartite matching. Level graphs and blocking flows are key concepts in modern flow algorithms.

## QnA Seeds

- Q: Why does Dinic achieve O(E*sqrt(V)) on unit networks?
- Q: What is a blocking flow?
- Q: How does Dinic compare to push-relabel?