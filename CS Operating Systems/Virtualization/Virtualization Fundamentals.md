---
tags:
  - csos
  - csos/virtualization
confidence: verified
freshness: stable
up: "[[Virtualization Overview]]"
tier-coverage: [intuition, core, deep-dive, practice]
---
# Virtualization Fundamentals

## 🎯 Intuition
**The Core Idea:** **Virtualisation** is the technique of running multiple independent operating systems (called **guest OSes**) on a single physical machine by inserting a software layer — the **hypervisor** (or Virtual Machine Monitor, VMM) — between the hardware and the guests.

**Analogy:** It is like a building with multiple apartments: each tenant thinks they have their own machine, but the landlord manages the shared physical structure and keeps tenants isolated from one another.

**Why It Matters:** Virtualisation creates the illusion of many computers from one physical machine. Cloud computing is built entirely on this idea.

## ⚙️ Core Mechanics
### Type 1 vs Type 2 Hypervisors
#### Type 1 (Bare-Metal)
Runs directly on physical hardware. The hypervisor *is* the OS; guests run on top of it. The hardware resources are fully managed by the hypervisor.

**Examples:** VMware ESXi, Microsoft Hyper-V, Xen, KVM (Linux kernel acts as hypervisor).

**Characteristics:** Lower overhead; better performance; typically used in data-centres.

#### Type 2 (Hosted)
Runs on top of a conventional host OS (Windows, Linux, macOS). The hypervisor is an application in the host.

**Examples:** VMware Workstation, Oracle VirtualBox, QEMU (without KVM).

**Characteristics:** Easier to install; slightly higher overhead; used for development and desktop virtualisation.

### Full Virtualisation vs Para-Virtualisation

| Approach | Guest OS modified? | Privileged instructions |
|----------|-------------------|------------------------|
| Full virtualisation | No | Trapped and emulated by hypervisor |
| Para-virtualisation | Yes (hypercalls) | Guest calls hypervisor explicitly |
| Hardware-assisted virt | No | CPU extensions handle trapping |

## 🔬 Deep Dive
### Why Virtualise?

| Goal | Benefit |
|------|---------|
| Server consolidation | Run 20 VMs on one server instead of 20 physical servers |
| Isolation | A crash or breach in one VM does not affect others |
| Snapshot and migration | Save, restore, or live-migrate a running VM |
| Development/testing | Run Windows and Linux on the same laptop |
| Cloud computing | Sell slices of physical hardware as elastic compute units |

### Hardware Virtualisation Extensions
Hardware virtualisation extensions (Intel VT-x, AMD-V) make full virtualisation efficient by providing dedicated trap modes for guest privileged instructions, eliminating the need for binary translation.

### Interpreting the Models
Type 1 hypervisors are usually chosen when performance and resource control matter most. Type 2 hypervisors are usually chosen when convenience matters most. Para-virtualisation improves efficiency by letting the guest cooperate explicitly, while hardware-assisted virtualisation keeps the guest unmodified by relying on CPU support.

## 🏋️ Practice
### Warm-Up
1. What is a hypervisor, and what role does it play in virtualisation?
2. What is the difference between a guest OS and a host OS?
3. Name two hardware virtualisation extensions used on x86 systems.

### Core Problems
1. Is KVM a Type 1 or Type 2 hypervisor? Justify your answer.
2. Why did early x86 CPUs make full virtualisation difficult?
3. Compare full virtualisation, para-virtualisation, and hardware-assisted virtualisation using the table above.

### Challenge
1. Compare para-virtualisation and hardware-assisted virtualisation for an I/O-heavy workload.
2. A company wants to consolidate many lightly loaded servers into one machine while preserving isolation and migration support. Use the “Why Virtualise?” table to explain the main benefits.
3. A developer wants to run Linux on a Windows laptop for testing. Explain why a Type 2 hypervisor may be preferable to a bare-metal deployment in that scenario.

## Supporting Chunks

- [[Virtualization - Type 1 and Type 2 hypervisors differ in where they sit in the software stack]]
- [[Virtualization - Para-virtualisation replaces trap-and-emulate with explicit hypercalls for efficiency]]
- [[Virtualization - Cloud infrastructure uses hypervisors to provide elastic multi-tenant compute]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 7.
