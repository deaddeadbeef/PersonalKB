---
tags: [cs-os, chunk]
source: "[[raw-os-002]]"
confidence: high
supports:
  - "[[Process Management]]"
qna_seeds:
  - "Q: What are the five states in the process lifecycle model and key transitions? A: New, ready, running, blocked, and terminated. Key transitions: ready→running (dispatched by scheduler), running→blocked (initiates I/O), blocked→ready (I/O completes)."
---

# Five-State Process Lifecycle Model

The five-state process model captures all meaningful transitions a process undergoes: new (being created), ready (waiting for CPU), running (executing on CPU), blocked (waiting for I/O or event), and terminated (finished execution). A process transitions from ready→running when dispatched by the scheduler, from running→blocked when it initiates I/O, and from blocked→ready when the I/O completes. This model is the foundation for understanding scheduler design and process management.
