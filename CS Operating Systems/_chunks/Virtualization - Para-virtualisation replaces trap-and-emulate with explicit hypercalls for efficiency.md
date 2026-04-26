---
id: chunk-csos-037
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 7"
topic: "virtualization"
claim: "Para-virtualisation replaces expensive trap-and-emulate with explicit hypercalls — the guest OS is modified to call the hypervisor directly for privileged operations, improving I/O performance significantly"
confidence: verified
supports:
  - "[[Hypervisors]]"
  - "[[Virtualization Fundamentals]]"
tags:
  - csos
  - csos/virtualization
  - chunk
up: "[[CS Operating Systems]]"
---
# Virtualization — Para-virtualisation replaces trap-and-emulate with explicit hypercalls for efficiency

## Context

In full virtualisation, every privileged guest instruction causes a hardware trap to the hypervisor, which emulates the effect and resumes the guest. For I/O-intensive workloads, this can mean thousands of traps per second. Para-virtualisation (Xen, virtio) modifies the guest OS to replace privileged instructions with hypercalls — direct calls to a known hypervisor ABI. Xen's paravirt guests run Xen-aware Linux/BSDs. virtio defines a standard I/O protocol; Linux, Windows, and BSD guests use virtio drivers for near-native I/O performance.

## Why It Matters

Para-virtualisation closed the performance gap between native and virtualised I/O on disk and network in the mid-2000s, making virtualisation practical for latency-sensitive workloads. virtio is now a standard across hypervisors (KVM, Xen, VirtualBox, VMware). Modern hardware virtualisation extensions (VT-x, AMD-V) have since made full virtualisation nearly as fast as para-virt for CPU-heavy workloads, but virtio remains the dominant I/O paravirt approach.

## QnA Seeds

- Q: What is the performance cost of trap-and-emulate that para-virtualisation avoids?
- Q: What is a hypercall and how does it differ from a system call?
- Q: What does virtio standardise and why is it important?
