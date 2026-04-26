---
id: chunk-csos-036
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 7"
topic: "virtualization"
claim: "Type 1 hypervisors run directly on bare hardware for maximum performance; Type 2 hypervisors run inside a host OS for ease of installation — the split is about where OS responsibilities are delegated"
confidence: verified
supports:
  - "[[Virtualization Fundamentals]]"
  - "[[Hypervisors]]"
tags:
  - csos
  - csos/virtualization
  - chunk
up: "[[CS Operating Systems]]"
---
# Virtualization — Type 1 and Type 2 hypervisors differ in where they sit in the software stack

## Context

A Type 1 hypervisor (VMware ESXi, KVM, Xen, Hyper-V) runs directly on the physical hardware — it is the OS. Guest virtual machines run on top of it. A Type 2 hypervisor (VirtualBox, VMware Workstation) runs as an application inside a conventional host OS (Linux, Windows, macOS). The host OS manages hardware; the hypervisor requests hardware resources through the host's device drivers. Type 1 has less overhead; Type 2 is easier to install and manage.

## Why It Matters

The distinction explains the performance and deployment characteristics of different virtualisation products. Data centres use Type 1 (ESXi, KVM) because every efficiency percentage point matters when multiplied across thousands of servers. Developers use Type 2 (VirtualBox, WSL2) because installation doesn't require dedicating a machine. Understanding the stack also clarifies why KVM is both a kernel module and an OS — Linux acts as the Type 1 hypervisor when KVM is loaded.

## QnA Seeds

- Q: What is the key architectural difference between Type 1 and Type 2 hypervisors?
- Q: Why do data centres prefer Type 1 hypervisors?
- Q: Is KVM a Type 1 or Type 2 hypervisor? Explain.
