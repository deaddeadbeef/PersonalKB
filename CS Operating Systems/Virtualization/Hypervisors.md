---
tags:
  - csos
  - csos/virtualization
confidence: verified
freshness: stable
up: "[[Virtualization Overview]]"
tier-coverage: [intuition, core, deep-dive, practice]
---
# Hypervisors

## 🎯 Intuition
**The Core Idea:** A **hypervisor** (Virtual Machine Monitor) intercepts and virtualises the hardware interface, presenting each guest OS with an illusion of dedicated hardware. The key challenge is *fidelity* (guests behave as on real hardware), *isolation* (guests cannot interfere), and *performance* (overhead is minimal).

**Analogy:** Think of a stage manager running multiple plays on the same stage: each cast behaves as if the stage is theirs, while the manager controls access, swaps scenes, and prevents interference.

**Why It Matters:** The hypervisor makes each guest OS believe it has exclusive hardware access while actually multiplexing everything underneath. That is the foundation of cloud infrastructure.

## ⚙️ Core Mechanics
### Trap-and-Emulate
The classic hypervisor approach is **trap-and-emulate**: guest OS privileged instructions (those that touch hardware registers) cause a CPU trap into the hypervisor. The hypervisor emulates the expected effect in software and returns to the guest. This works perfectly when the CPU reliably traps all privileged instructions.

### The Historical x86 Problem
Historically, x86 had ~17 instructions that were sensitive but did *not* trap in user mode — they silently failed or returned wrong results. This broke trap-and-emulate and forced **binary translation** as an alternative. VMware's early approach was to scan and rewrite guest code before execution.

## 🔬 Deep Dive
### Hardware Virtualisation Extensions
Intel VT-x (2005) and AMD-V introduced a new CPU mode (VMX root/non-root) that provides proper trapping of all guest-mode privileged operations. The hypervisor runs in VMX root; guests run in VMX non-root. VM exits on privileged operations are handled by the hypervisor. This makes trap-and-emulate efficient without binary translation.

### Para-Virtualisation (Xen / Hyper-V enlightenments)
In **para-virtualisation**, the guest OS is modified to call the hypervisor via **hypercalls** instead of executing privileged instructions. The guest "knows" it is virtualised and cooperates. This is much faster than trap-and-emulate for I/O-heavy workloads.

### Production Hypervisors

| Hypervisor | Type | Para-virt support | Notes |
|------------|------|-------------------|-------|
| VMware ESXi | 1 | Partial (VMXNET3, PVSCSI) | Dominant enterprise hypervisor |
| KVM | 1 (kernel module) | virtio | Linux kernel + QEMU; open source |
| Xen | 1 | PV mode, PVH | Used by AWS historically |
| Hyper-V | 1 | Enlightenments | Microsoft; used in Azure |
| VirtualBox | 2 | Guest additions | Cross-platform; open source |

### Trade-Offs in Practice
Binary translation made problematic x86 guests workable before hardware support matured, but it added complexity. Para-virtualisation improves performance by cooperation, especially for I/O-heavy workloads, but requires guest modification. Hardware-assisted virtualisation avoids guest modification while restoring efficient, reliable trapping.

## 🏋️ Practice
### Warm-Up
1. What does a hypervisor virtualise?
2. What are the three main goals of a hypervisor besides simply “running VMs”?
3. What is trap-and-emulate?

### Core Problems
1. Why did the historical x86 design break pure trap-and-emulate?
2. How does binary translation differ from ordinary trap-and-emulate?
3. How do VT-x and AMD-V solve the main problem that early x86 virtualisation faced?

### Challenge
1. Compare the performance trade-offs of binary translation, para-virtualisation, and hardware-assisted virtualisation.
2. Explain why para-virtualisation can outperform trap-and-emulate for I/O-heavy workloads.
3. A cloud provider wants strong isolation, unmodified guests, and low overhead. Which deep-dive approach best fits those goals, and why?

## Supporting Chunks

- [[Virtualization - Type 1 and Type 2 hypervisors differ in where they sit in the software stack]]
- [[Virtualization - Para-virtualisation replaces trap-and-emulate with explicit hypercalls for efficiency]]

## See Also

- [[Virtual Memory and Paging]] — hypervisors use nested/shadow page tables to virtualise the MMU
- [[Interrupts and DMA]] — interrupt virtualisation and I/O device emulation are key hypervisor responsibilities
- [[Access Control]] — VM isolation is a coarse-grained access-control boundary between tenants
- [[Multiprocessor Systems]] — hypervisors schedule virtual CPUs onto physical cores, inheriting SMP scheduling concerns

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 7.
