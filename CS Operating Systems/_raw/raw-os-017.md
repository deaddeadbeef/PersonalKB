---
tags: [cs-os, raw]
source_type: textbook_chapter
source_title: "Virtualization Fundamentals"
authors: "Andrew S. Tanenbaum, Herbert Bos"
year: 2015
---

# Virtualization Fundamentals

## Summary
Virtualization interposes a software layer—the hypervisor (or virtual machine monitor)—between guest operating systems and the physical hardware, enabling multiple isolated OS instances to share the same machine. Type 1 hypervisors run directly on hardware for production workloads, while Type 2 hypervisors run atop a host OS for development and testing. The trap-and-emulate mechanism, combined with modern hardware extensions (Intel VT-x, AMD-V), enables near-native execution speed by running most guest instructions directly on the CPU while intercepting privileged operations.

## Key Claims
- The Popek-Goldberg virtualization requirements (1974) state that a processor architecture is efficiently virtualizable if all sensitive instructions (those that affect or depend on machine state) are a subset of privileged instructions (those that trap in user mode)—x86 violated this requirement until hardware virtualization extensions were added
- Type 1 (bare-metal) hypervisors like VMware ESXi, Xen, and Microsoft Hyper-V run directly on hardware with no host OS, providing lower overhead and better security isolation; they dominate data center and cloud deployments
- Type 2 (hosted) hypervisors like VirtualBox and VMware Workstation run as applications on a host OS, leveraging the host's device drivers at the cost of an additional software layer; they are primarily used for desktop virtualization and development
- Paravirtualization (pioneered by Xen) modifies the guest OS to replace non-virtualizable instructions with explicit hypervisor calls (hypercalls), achieving better performance than full virtualization at the cost of requiring guest OS modifications
- Hardware-assisted virtualization (Intel VT-x introduced 2005, AMD-V introduced 2006) adds a new processor mode and control structures (VMCS on Intel, VMCB on AMD) that handle trap-and-emulate automatically in hardware, making full virtualization efficient without guest OS modifications

## Atomic Facts
1. The trap-and-emulate technique works by running the guest OS in user mode: when the guest executes a privileged instruction, the CPU traps to the hypervisor, which emulates the instruction's intended effect on the virtual machine's state and returns control to the guest
2. x86 has 17 sensitive-but-unprivileged instructions (e.g., POPF, SGDT) that behave differently in user vs kernel mode without trapping; before VT-x, binary translation (VMware) or paravirtualization (Xen) was needed to handle these instructions
3. Intel VT-x introduces root mode (hypervisor) and non-root mode (guest), each with their own ring 0–3; VM exits transfer control from guest to hypervisor on configurable events, and VM entries return to the guest, with the VMCS storing both states
4. A shadow page table (used before hardware nested paging) is maintained by the hypervisor to translate guest virtual addresses directly to host physical addresses; the hypervisor intercepts guest page table modifications to keep the shadow synchronized
5. Extended Page Tables (EPT on Intel, NPT/RVI on AMD) add a second level of hardware address translation—the MMU walks both guest page tables (guest virtual → guest physical) and host page tables (guest physical → host physical), eliminating the overhead and complexity of shadow page tables
6. Live migration moves a running VM from one physical host to another with minimal downtime (typically under 100ms) by iteratively copying memory pages while the VM continues running, then pausing the VM for a final sync of remaining dirty pages and CPU state

## Significance
Virtualization is the foundational technology enabling cloud computing—without it, AWS, Azure, and GCP could not provide elastic, isolated compute instances to millions of tenants on shared hardware. The progression from software workarounds (binary translation) to hardware support (VT-x/EPT) to near-native performance illustrates how important abstractions eventually get hardware acceleration when demand justifies the silicon investment.

## Chunks Extracted
- [[chunk-os-115 Popek-Goldberg Requirements Define Efficient Virtualizability]]
- [[chunk-os-116 Trap-and-Emulate Runs Guest in User Mode]]
- [[chunk-os-117 VT-x Adds Root and Non-Root Modes for Full Virtualization]]
- [[chunk-os-118 Extended Page Tables Eliminate Shadow Page Table Overhead]]
