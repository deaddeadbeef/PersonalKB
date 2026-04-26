---
id: chunk-csos-032
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 6"
topic: "deadlocks"
claim: "Deadlock requires all four Coffman conditions to hold simultaneously: mutual exclusion, hold-and-wait, no preemption, and circular wait — removing any one condition prevents deadlock"
confidence: verified
supports:
  - "[[Deadlock Fundamentals]]"
  - "[[Deadlock Prevention]]"
tags:
  - csos
  - csos/deadlocks
  - chunk
up: "[[CS Operating Systems]]"
---
# Deadlocks — Deadlock requires all four Coffman conditions to hold simultaneously

## Context

Coffman, Elphick, and Shoshani (1971) proved that deadlock is both necessary and sufficient when all four conditions hold simultaneously: (1) at least one resource is held exclusively (mutual exclusion); (2) processes hold resources while requesting others (hold-and-wait); (3) resources cannot be forcibly reclaimed (no preemption); (4) a circular chain of waiters exists (circular wait). Removing any single condition breaks the possibility of deadlock. This analysis directly motivates the three main strategies: prevention attacks one condition structurally; avoidance prevents any unsafe state; detection finds and breaks existing deadlocks.

## Why It Matters

The four-conditions framework is the most important theoretical result in deadlock theory. It immediately suggests four potential prevention strategies (one per condition) and explains why some strategies are impractical (eliminating mutual exclusion is impossible for printers). It also explains why the "ostrich" strategy is reasonable for most desktop systems: the probability of all four conditions coinciding is low, and the cost of prevention may exceed the cost of occasional manual recovery.

## QnA Seeds

- Q: Name the four Coffman conditions for deadlock.
- Q: If we can preempt resources from any process, can deadlock still occur?
- Q: Why is eliminating the mutual exclusion condition usually impractical?
