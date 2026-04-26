---
tags:
  - csos
  - moc
up: "[[CS Operating Systems]]"
---
# OS Foundations Overview

The conceptual bedrock of operating systems: what an OS is, why it exists, how it enforces the kernel/user-space boundary, and how its internal structure (monolithic, microkernel, hybrid) shapes every other property.

---

## Learn in This Order

1. [[OS Fundamentals]] — purpose of an OS; extended-machine view; resource-manager view; kernel vs user space
2. [[System Calls]] — the OS–application boundary; trap mechanism; POSIX examples; context switch overhead
3. [[OS Structure]] — monolithic, microkernel, hybrid, exokernel architectures; trade-offs

---

## In This Domain

| Page | One-line summary |
|------|-----------------|
| [[OS Fundamentals]] | What OSes are; hardware abstraction; extended machine vs resource manager |
| [[System Calls]] | Application/OS boundary; trap; POSIX interface |
| [[OS Structure]] | Monolithic vs microkernel vs hybrid; reliability/performance trade-off |

---

## Common Distinctions

| Question | Answer |
|----------|--------|
| Kernel mode vs user mode? | Kernel mode = full hardware access. User mode = restricted. User programs cross into kernel mode via system calls. |
| Monolithic vs microkernel? | Monolithic colocates all services in kernel space (fast, common). Microkernel pushes services to user space (fault-isolated, slower IPC). |
| System call vs library call? | Library calls are ordinary function calls in user space. System calls cross into kernel mode via a trap instruction — much more expensive. |

---

## How to Navigate

- **New to OS?** Read in the order above — each page builds on the prior.
- **Wondering about performance of any OS feature?** Understand [[System Calls]] first; the trap cost is the baseline overhead for all OS interactions.
- **Evaluating OS designs (Linux vs Windows vs Minix)?** [[OS Structure]] lays out the architectural options.

---

## Related Domains

- **[[Processes Overview]]** — once you know what an OS is (Foundations), the next natural question is how it manages running programs (Processes).
- **[[Design Principles Overview]]** — the Mechanism vs Policy distinction directly shapes OS structural decisions.
- **[[Case Studies Overview]]** — Linux (monolithic + modules), Windows NT (hybrid), Minix (microkernel) are Foundations concepts in practice.
