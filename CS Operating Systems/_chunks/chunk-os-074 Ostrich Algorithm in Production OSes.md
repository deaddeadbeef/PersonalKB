---
tags: [cs-os, chunk]
source: "[[raw-os-006]]"
confidence: high
supports:
  - "[[Deadlock Theory]]"
  - "[[OS Design Philosophy]]"
qna_seeds:
  - "Q: Why do most production OSes ignore deadlock rather than preventing it? A: Linux, Windows, and macOS use the ostrich algorithm — they accept the possibility of deadlock because the performance and complexity costs of prevention/avoidance exceed the cost of occasional manual intervention (e.g., killing stuck processes)."
---

# Ostrich Algorithm in Production OSes

Most general-purpose operating systems — Linux, Windows, macOS — use the ostrich algorithm: they deliberately ignore deadlock rather than preventing or detecting it. This pragmatic choice reflects the engineering tradeoff that the runtime cost and design constraints of deadlock prevention or avoidance (reduced resource utilization, advance declaration requirements, O(m×n²) checking) exceed the cost of occasional manual intervention when deadlocks do occur. This illustrates a recurring systems design theme: theoretical completeness often yields to engineering pragmatism in production systems.
