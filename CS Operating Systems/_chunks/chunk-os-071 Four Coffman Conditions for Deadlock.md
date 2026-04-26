---
tags: [cs-os, chunk]
source: "[[raw-os-006]]"
confidence: high
supports:
  - "[[Deadlock Theory]]"
qna_seeds:
  - "Q: What are the four Coffman conditions for deadlock? A: Mutual exclusion (resources are non-sharable), hold-and-wait (processes hold resources while requesting more), no preemption (resources cannot be forcibly taken), and circular wait (a cycle exists in the wait-for graph). All four must hold simultaneously; eliminating any one prevents deadlock."
---

# Four Coffman Conditions for Deadlock

Deadlock requires all four Coffman conditions (1971) to hold simultaneously: mutual exclusion (resources are non-sharable), hold-and-wait (processes hold allocated resources while requesting additional ones), no preemption (resources cannot be forcibly reclaimed from a holding process), and circular wait (a cycle exists in the process wait-for graph). Eliminating any single condition is sufficient to prevent deadlock entirely. The most practical prevention strategy is eliminating circular wait by imposing a total ordering on resource types and requiring acquisition in strictly increasing order.
