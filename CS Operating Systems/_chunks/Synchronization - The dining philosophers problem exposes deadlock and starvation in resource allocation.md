---
id: chunk-csos-015
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 2"
topic: "synchronization"
claim: "The dining philosophers problem shows that naïve resource acquisition (pick up left fork then right) causes deadlock; correct solutions break circular wait via resource ordering, arbitration, or occupancy limits"
confidence: verified
supports:
  - "[[Classic Synchronization Problems]]"
  - "[[Deadlock Fundamentals]]"
tags:
  - csos
  - csos/synchronization
  - chunk
up: "[[CS Operating Systems]]"
---
# Synchronization — The dining philosophers problem exposes deadlock and starvation in resource allocation

## Context

Five philosophers sit at a circular table; each needs two forks (shared with neighbours) to eat. If all simultaneously pick up their left fork, all five are blocked waiting for their right fork — a deadlock. Solutions include: asymmetry (one philosopher picks up right first, breaking the circular wait), an arbitrator process (philosophers request permission before picking up any fork), or limiting occupancy (only four philosophers may sit at once, guaranteeing at least one can proceed).

## Why It Matters

The problem is a concise model of any system where processes hold resources while waiting for others. Its solutions map directly to deadlock prevention techniques: resource ordering (Coffman condition 4 attack), arbitration (deadlock avoidance by central control), and occupancy limits (Coffman condition 2 attack). The problem also illustrates starvation: even in deadlock-free solutions, an individual philosopher might starve if neighbouring philosophers always eat in turn.

## QnA Seeds

- Q: Why does the naïve "pick up left then right" strategy cause deadlock?
- Q: How does the asymmetric solution break the deadlock?
- Q: What Coffman condition does the occupancy-limit solution attack?
