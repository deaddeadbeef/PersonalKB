---
id: chunk-csos-038
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 7"
topic: "virtualization"
claim: "Cloud infrastructure uses hypervisors to provide elastic multi-tenant compute: physical servers are sliced into VMs that can be rapidly provisioned, migrated, and deprovisioned on demand"
confidence: verified
supports:
  - "[[Virtualization Fundamentals]]"
tags:
  - csos
  - csos/virtualization
  - chunk
up: "[[CS Operating Systems]]"
---
# Virtualization — Cloud infrastructure uses hypervisors to provide elastic multi-tenant compute

## Context

IaaS cloud providers (AWS EC2, Azure VMs, GCP Compute Engine) hypervisor each physical server into many tenant VMs. Tenants get billed per VM-hour rather than per physical machine. The hypervisor provides isolation between tenants (memory, I/O, CPU) and enables live migration — a running VM can be moved from one physical host to another with sub-second downtime for maintenance or load balancing. Elastic scaling (Auto Scaling groups, Kubernetes HPA) adds/removes VMs automatically to match demand.

## Why It Matters

Virtualisation is the foundational technology of cloud computing. Without it, multi-tenancy (sharing physical hardware among paying customers) would be impossible to implement securely. Understanding hypervisor isolation helps engineers reason about cloud security boundaries, noisy-neighbour effects, and the performance characteristics of virtualised vs bare-metal compute.

## QnA Seeds

- Q: What is live migration of a VM and why is it useful?
- Q: How does a hypervisor prevent one tenant's VM from accessing another's memory?
- Q: What is the "noisy neighbour" problem in cloud computing?
