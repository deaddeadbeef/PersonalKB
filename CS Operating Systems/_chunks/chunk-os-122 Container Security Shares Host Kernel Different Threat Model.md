---
id: chunk-csos-122
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 7 — Containers and OS-Level Virtualization"
topic: "virtualization"
claim: "Container security is fundamentally different from VM security because all containers share the host kernel — a kernel vulnerability exploitable from a container compromises the host and all other containers"
confidence: verified
supports:
  - "[[Virtualization Overview]]"
  - "[[OS Security Fundamentals]]"
tags:
  - csos
  - csos/virtualization
  - csos/security
  - chunk
up: "[[CS Operating Systems]]"
---
# Virtualization — Container security shares host kernel creating a different threat model

## Context

Unlike VMs, which run separate kernels with hardware-enforced isolation (VT-x, EPT), all containers share the host kernel. A kernel vulnerability exploitable via a system call available inside a container can compromise the host and every other container — the isolation boundary is the kernel's namespace/cgroup implementation rather than hardware. Defense-in-depth measures include seccomp (system call filtering), AppArmor/SELinux (MAC policies), rootless containers (user namespace remapping), and capability dropping. gVisor (Google) interposes a user-space kernel to intercept system calls, while Kata Containers runs each container inside a lightweight VM, combining container UX with VM isolation.

## Why It Matters

This shared-kernel model is the fundamental security tradeoff of containers vs. VMs. It explains why high-security multi-tenant environments (like public cloud) initially ran VMs rather than containers, and why hybrid approaches (Kata, gVisor, Firecracker) emerged to get container ergonomics with stronger isolation.

## QnA Seeds

- Q: Why is a container kernel exploit more damaging than a VM kernel exploit?
- Q: What defense-in-depth measures harden container security?
- Q: How do gVisor and Kata Containers address the shared-kernel problem?
