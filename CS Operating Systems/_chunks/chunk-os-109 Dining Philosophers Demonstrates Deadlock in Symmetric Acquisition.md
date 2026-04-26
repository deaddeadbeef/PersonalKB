---
id: chunk-csos-109
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 2 — Classic Synchronization Problems"
topic: "synchronization"
claim: "The dining philosophers problem demonstrates that even symmetric, simple resource acquisition patterns produce deadlock when all participants simultaneously acquire their left resource; solutions include resource ordering, an arbitrator, or limiting concurrency to N−1"
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
# Synchronization — Dining philosophers demonstrates deadlock in symmetric resource acquisition

## Context

Five philosophers sit at a round table with one fork between each pair. Each needs two forks to eat. Deadlock occurs when all five simultaneously pick up their left fork — each holds one fork and waits for the other, forming a circular wait. Dijkstra's solution assigns each fork a number and requires philosophers to pick up the lower-numbered fork first, breaking the circular wait condition. Other solutions include an arbitrator (a waiter who permits at most 4 philosophers to attempt eating simultaneously) or asymmetry (one philosopher picks up right fork first).

## Why It Matters

The dining philosophers problem distills the deadlock potential in any system where multiple agents compete for multiple resources — database transactions acquiring locks on multiple rows, distributed services acquiring leases on multiple resources, or threads acquiring multiple mutexes. Resource ordering is the most widely used practical solution.

## QnA Seeds

- Q: What specific condition causes deadlock in the dining philosophers problem?
- Q: How does Dijkstra's fork-numbering solution break the circular wait?
- Q: Give a real-world system that exhibits the dining philosophers pattern.
