---
tags: [cs-os, chunk]
source: "[[raw-os-005]]"
confidence: high
supports:
  - "[[Process Synchronization]]"
qna_seeds:
  - "Q: What three properties must a correct critical section solution satisfy? A: Mutual exclusion (at most one process in the critical section), progress (only contending processes participate in the entry decision), and bounded waiting (a finite bound on how many times others can enter before a waiting process)."
---

# Critical Section Problem Three Requirements

Any correct solution to the critical section problem must satisfy three properties simultaneously. Mutual exclusion ensures at most one process executes in the critical section at any time. Progress guarantees that only processes contending for entry participate in the decision of who enters next — non-contending processes cannot block others. Bounded waiting imposes a finite limit on how many times other processes can enter the critical section before a waiting process is granted access, preventing starvation.
