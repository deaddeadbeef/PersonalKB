---
tags:
  - csos
  - moc
up: "[[CS Operating Systems]]"
confidence: established
freshness: stable
tier-coverage: [intuition, core]
---
# Virtualization Overview

Virtualization allows multiple operating systems to run concurrently on a single physical machine by interposing a hypervisor between hardware and guest OSes. This domain covers the two hypervisor types, trap-and-emulate mechanics, para-virtualisation, and cloud infrastructure built on these foundations.

---

## Learn in This Order

1. [[Virtualization Fundamentals]] — type 1 vs type 2 hypervisors; full vs para-virtualisation; VMM goals (fidelity, performance, safety)
2. [[Hypervisors]] — VMware ESXi (type 1), KVM (type 1 in Linux), Xen (type 1); trap-and-emulate; binary translation; VMEXIT/VMENTER

---

## In This Domain

| Page | One-line summary |
|------|-----------------|
| [[Virtualization Fundamentals]] | Hypervisor types; full vs para-virtualisation; isolation model |
| [[Hypervisors]] | VMware/KVM/Xen; trap-and-emulate; hardware virtualization extensions |

---

## Common Distinctions

| Question | Answer |
|----------|--------|
| Type 1 vs Type 2 hypervisor? | Type 1 (bare-metal) runs directly on hardware (VMware ESXi, Xen, KVM). Type 2 runs inside a host OS (VirtualBox, VMware Workstation). Type 1 has lower overhead. |
| Full virtualisation vs para-virtualisation? | Full virtualisation: guest OS runs unmodified, hypervisor traps and emulates privileged instructions. Para-virtualisation: guest OS is modified to call hypercalls instead of privileged instructions — lower overhead. |
| Container vs VM? | A VM virtualises the full hardware stack (separate OS per VM). A container shares the host OS kernel, only isolating user-space (lighter, less isolation). |

---

## How to Navigate

- **New to virtualisation?** [[Virtualization Fundamentals]] gives the conceptual model and taxonomy.
- **Implementation details (trap-and-emulate, VMEXIT)?** [[Hypervisors]]
- **Cloud infrastructure context?** Both pages discuss how AWS/Azure/GCP use type-1 hypervisors.

---

## Related Domains

- **[[CS Operating Systems/Memory/Memory Management Overview|Memory Management Overview]]** — virtualisation adds a second layer of address translation (nested paging / EPT); understanding single-level paging first is essential.
- **[[OS Foundations Overview]]** — the kernel/user-mode distinction and privilege levels are what the hypervisor exploits to intercept guest OS behaviour.
- **[[Multiprocessor Overview]]** — cloud VMs run on NUMA multiprocessor hosts; scheduler affinity and NUMA-awareness apply to hypervisor scheduling.

## References

- [[CS Operating Systems/Sources/Sources Index]]
- [[CS Operating Systems/CS Operating Systems Book Reading Spine]]
