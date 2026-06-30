---
id: mos-ch-07
type: book-chapter
chapter: 7
book: "Modern Operating Systems"
author: "Andrew S. Tanenbaum"
status: seeded
chunk_count: 3
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
tags:
  - csos
  - book-chapter
up: "[[Chapter Index]]"
confidence: verified
---
# MOS — Chapter 07: Virtualization and the Cloud

## Summary

Virtualisation allows multiple operating systems to share a single physical machine by inserting a hypervisor between hardware and guest OS. Type 1 (bare-metal) hypervisors run directly on hardware with maximum performance; Type 2 (hosted) hypervisors run inside a conventional OS, sacrificing some efficiency for ease of installation. Full virtualisation traps all privileged instructions and emulates them; para-virtualisation requires modifying the guest OS to call the hypervisor explicitly (hypercalls), avoiding the overhead of trap-and-emulate. Hardware virtualisation extensions (Intel VT-x, AMD-V) make full virtualisation efficient without binary translation. The chapter connects this to cloud computing: cloud providers use virtualisation to slice physical servers into tenant VMs, enabling elastic scale-out, rapid provisioning, and workload isolation as cloud service models (IaaS, PaaS, SaaS).

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| Type 1 hypervisor | Bare-metal; runs directly on hardware; highest performance |
| Type 2 hypervisor | Hosted; runs inside host OS; easier setup, higher overhead |
| Full virtualisation | Guest OS unmodified; hypervisor traps and emulates privileged instructions |
| Para-virtualisation | Guest OS modified to use hypercalls; faster than full virt |
| Cloud elasticity | Ability to provision/release VMs on demand to match workload |

## Chunk Candidates

- [x] [[Virtualization - Type 1 and Type 2 hypervisors differ in where they sit in the software stack]]
- [x] [[Virtualization - Para-virtualisation replaces trap-and-emulate with explicit hypercalls for efficiency]]
- [x] [[Virtualization - Cloud infrastructure uses hypervisors to provide elastic multi-tenant compute]]

## Wiki Pages Seeded

- [[Virtualization Fundamentals]] — what virtualisation is, type 1 vs type 2, use cases
- [[Hypervisors]] — VMware ESXi, KVM, Xen; trap-and-emulate; hardware extensions

## References

See [[Sources Index#Tanenbaum 2015]].
