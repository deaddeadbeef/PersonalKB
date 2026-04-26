---
id: chunk-csos-120
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 7 — Containers and OS-Level Virtualization"
topic: "virtualization"
claim: "Control groups (cgroups) complement namespaces by enforcing resource limits (CPU, memory, I/O bandwidth) and accounting — without cgroups, a container could monopolize host resources, defeating multi-tenant isolation"
confidence: verified
supports:
  - "[[Virtualization Overview]]"
  - "[[Virtualization Fundamentals]]"
tags:
  - csos
  - csos/virtualization
  - chunk
up: "[[CS Operating Systems]]"
---
# Virtualization — Cgroups enforce resource limits complementing namespace isolation

## Context

Namespaces provide visibility isolation (what a process can see), but not resource limits (how much it can consume). Cgroups fill this gap by imposing limits on CPU time, memory usage, I/O bandwidth, number of PIDs, and network bandwidth per process group. Cgroups v2 (unified hierarchy, default since Linux 5.2/systemd 243) organizes resource controllers in a single tree structure, replacing v1's separate per-controller hierarchies. Without cgroups, a "noisy neighbor" container running a memory-intensive workload could exhaust host memory and OOM-kill other containers — cgroups prevent this by enforcing per-container memory caps with configurable OOM behavior.

## Why It Matters

Cgroups are what make container density practical on shared infrastructure. Every container orchestrator (Kubernetes, Docker Swarm) uses cgroups to implement resource requests and limits. The cgroups v1 → v2 migration also illustrates the cost of getting abstractions wrong initially — v1's per-controller hierarchies created inconsistencies that took a decade to resolve.

## QnA Seeds

- Q: What is the difference between namespace isolation and cgroup isolation?
- Q: What problem does cgroups v2 solve that v1 had?
- Q: How do cgroups prevent noisy-neighbor problems in container deployments?
