---
id: chunk-csos-118
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 7 — Virtualization Fundamentals"
topic: "virtualization"
claim: "Extended Page Tables (EPT/NPT) add a second level of hardware address translation — the MMU walks both guest and host page tables — eliminating the overhead and complexity of shadow page tables maintained by the hypervisor"
confidence: verified
supports:
  - "[[Virtualization Fundamentals]]"
  - "[[Virtual Memory and Paging]]"
tags:
  - csos
  - csos/virtualization
  - chunk
up: "[[CS Operating Systems]]"
---
# Virtualization — Extended page tables eliminate shadow page table overhead

## Context

Before hardware nested paging, the hypervisor maintained shadow page tables that translated guest virtual addresses directly to host physical addresses. Every guest page table modification had to be intercepted and replicated in the shadow, causing significant overhead. Extended Page Tables (EPT on Intel, NPT/RVI on AMD) solve this by adding a second level of hardware translation: the MMU first walks the guest page tables (guest virtual → guest physical), then walks the host page tables (guest physical → host physical). This is entirely in hardware — the hypervisor no longer needs to intercept or shadow guest page table operations.

## Why It Matters

EPT/NPT dramatically reduced the overhead of memory-intensive virtualized workloads. Without nested paging, every guest page fault and page table update required a VM exit — with EPT, the guest manages its own page tables freely and the hardware handles the two-level translation. Live migration (moving a running VM with <100ms downtime) also relies on this infrastructure for efficient memory tracking.

## QnA Seeds

- Q: What problem did shadow page tables solve and what overhead did they introduce?
- Q: How does EPT's two-level translation work in hardware?
- Q: Why did EPT dramatically improve virtualized workload performance?
