---
tags: [cs-os, chunk]
source: "[[raw-os-005]]"
confidence: high
supports:
  - "[[Process Synchronization]]"
  - "[[Concurrency Primitives]]"
qna_seeds:
  - "Q: What is the difference between a semaphore and a mutex? A: Dijkstra's semaphore supports wait(P/down) and signal(V/up) operations. A binary semaphore (0/1) acts like a mutex, but a true mutex adds ownership semantics — only the acquiring thread can release it — enabling priority inheritance to combat priority inversion."
---

# Semaphore Wait and Signal Operations

Dijkstra introduced semaphores in 1965 with two atomic operations: wait (P/down) decrements the semaphore value and blocks the caller if the result is negative, while signal (V/up) increments the value and wakes a blocked process if any exist. A binary semaphore (values 0 and 1) behaves like a mutex lock, while a counting semaphore (values 0 to N) controls access to a pool of N identical resources. A true mutex differs from a binary semaphore by adding ownership semantics — only the acquiring thread may release it — which enables priority inheritance to combat priority inversion.
