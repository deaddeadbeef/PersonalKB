---
tags:
  - csos
  - moc
up: "[[CS Operating Systems]]"
confidence: verified
---
# Design Principles Overview

High-level principles that guide OS design decisions. These principles recur throughout every OS domain and explain *why* systems are structured the way they are rather than just *how* they work.

---

## Learn in This Order

1. [[OS Design Principles]] — goals (correctness, performance, reliability, portability, security); trade-offs; why no single optimal design exists
2. [[Mechanism vs Policy]] — separating *what can be done* (mechanism) from *decisions about when* (policy); examples in scheduling, memory, file systems

---

## In This Domain

| Page | One-line summary |
|------|-----------------|
| [[OS Design Principles]] | Design goals; trade-offs; correctness vs performance; portability |
| [[Mechanism vs Policy]] | Principle of separation; why it enables flexible, evolvable systems |

---

## Common Distinctions

| Question | Answer |
|----------|--------|
| Mechanism vs policy? | Mechanism = the capability (e.g., priority queues in the scheduler). Policy = the decision (e.g., which process gets highest priority). Separating them lets policy change without touching mechanism. |
| Why does simplicity matter in OS design? | Complex OSes have more failure modes, harder security audits, and larger attack surfaces. Simplicity enables correctness. |
| Performance vs portability trade-off? | Hardware-specific optimisation (e.g., assembly spinlocks) improves performance but hurts portability. Abstraction layers (HAL, VFS) restore portability at a small runtime cost. |

---

## How to Navigate

- **Studying for a design question?** Both pages are short and high-impact — read them together.
- **Seeing mechanism-vs-policy in practice?** [[Case Studies Overview]] shows VFS (Linux) and HAL (Windows NT) as textbook applications.

---

## Related Domains

- **[[OS Foundations Overview]]** — OS structural decisions (monolithic vs microkernel) are direct applications of the design principles here.
- **[[Case Studies Overview]]** — Linux VFS, Windows NT HAL, and Android's Binder are mechanism-vs-policy in real systems.

## References
- [[CS Operating Systems/Sources/Sources Index|CS Operating Systems Sources Index]]
