---
id: chunk-csos-119
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 7 — Containers and OS-Level Virtualization"
topic: "virtualization"
claim: "Linux namespaces provide the isolation foundation for containers: each namespace type creates an independent view of a system resource so a containerized process sees its own PID tree, network stack, filesystem mounts, and user IDs"
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
# Virtualization — Linux namespaces isolate resource visibility for containers

## Context

Linux provides eight namespace types that each isolate a specific aspect of the system: PID (process IDs), Network (network interfaces, routing), Mount (filesystem mount points), UTS (hostname), IPC (System V IPC, POSIX message queues), User (UID/GID mapping), Cgroup (cgroup root), and Time (clock offsets, added in Linux 5.6). When a container is created, the runtime creates new instances of these namespaces. A process inside the container sees PID 1 as its init process, its own network interfaces, its own filesystem root — a complete illusion of being the only occupant of the machine, all achieved by kernel-level resource view partitioning rather than hardware virtualization.

## Why It Matters

Namespaces are the "how" behind container isolation. Understanding them explains container behaviors that seem mysterious — why a container process has PID 1 inside but a different PID on the host, why container networking requires bridges/veth pairs, and why user namespace mapping is critical for rootless container security.

## QnA Seeds

- Q: What are the eight Linux namespace types and what does each isolate?
- Q: How do namespaces differ from hypervisor-based isolation?
- Q: Why does a containerized process see itself as PID 1?
