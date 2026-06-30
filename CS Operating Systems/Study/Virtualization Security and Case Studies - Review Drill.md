---
tags:
  - csos
  - csos/study
  - csos/virtualization
  - csos/security
  - csos/casestudies
up: "[[OS Study Index]]"
confidence: policy
---
# Virtualization, Security, and Case Studies — Review Drill

Active-recall drill for hypervisor models, virtualisation approaches, OS security mechanisms, access control models, malware defenses, and the three real OS case studies (Linux, Android, Windows NT).

**Canon pages:** [[Virtualization Fundamentals]] · [[Hypervisors]] · [[OS Security Fundamentals]] · [[Access Control]] · [[Authentication and Protection]] · [[Malware and Defenses]] · [[Case Studies Overview]] · [[Linux Architecture Overview]] · [[Android Architecture]] · [[Windows NT Architecture]] · [[Virtualization Overview]] · [[Security Overview]]

---

## How to Use

Answer each question before checking the canonical page. Virtualisation and security questions often hinge on precise distinctions — vague answers indicate gaps.

---

## Core Recall

**Virtualisation Fundamentals**

Q: What is a hypervisor (VMM) and why is it needed?
A: A **hypervisor** (Virtual Machine Monitor) sits between guest OSes and physical hardware, presenting each guest with an illusion of dedicated hardware while enforcing isolation between guests. It is needed because without it a guest OS would issue privileged instructions directly — crashing or corrupting other guests. The hypervisor intercepts and emulates (or delegates via hardware extensions) all privileged operations.

Q: What is the difference between a Type 1 and Type 2 hypervisor?
A: **Type 1 (bare-metal)**: the hypervisor runs directly on hardware — it *is* the privileged OS. Guests run on top of it. Lower overhead; used in data centres. Examples: VMware ESXi, Microsoft Hyper-V, Xen, KVM. **Type 2 (hosted)**: the hypervisor is an application running on top of a conventional host OS (Windows, Linux, macOS). Easier to install; slightly higher overhead from the extra OS layer. Examples: VMware Workstation, VirtualBox, QEMU (without KVM).

Q: What is trap-and-emulate, and what broke it on classic x86?
A: **Trap-and-emulate**: guest OS privileged instructions cause a CPU trap into the hypervisor; the hypervisor emulates the expected effect and returns to the guest. This is the "clean" virtualisation design. **Problem on classic x86**: ~17 instructions were *sensitive* (their behaviour differs in user vs kernel mode) but did NOT trap — they silently failed or returned wrong results in user mode. This made trap-and-emulate incorrect for unmodified x86 guests, requiring **binary translation** (VMware's early approach: rewrite guest code before execution). Intel VT-x (2005) fixed this by introducing VMX root/non-root modes that reliably trap all guest privileged operations.

Q: What is para-virtualisation, and what is its trade-off?
A: The guest OS is **modified** to replace privileged instructions with explicit **hypercalls** to the hypervisor. The guest "knows" it is virtualised and cooperates. Faster than trap-and-emulate for I/O-heavy workloads because hypercalls are cheaper than traps. Trade-off: requires guest OS source access; cannot run unmodified guest OSes. Used by Xen (PV mode) and Windows Hyper-V enlightenments.

---

**OS Security**

Q: What is a threat model, and why does every security decision depend on it?
A: A threat model explicitly identifies: (1) the assets to protect, (2) the adversaries and their capabilities, (3) the attack surface (entry points), and (4) acceptable risk. Without a threat model, security decisions have no grounding — you might over-engineer defenses against unlikely attacks while missing obvious ones. The OS threat model typically includes: malicious user programs, compromised applications, and hardware-level attackers for high-security deployments.

Q: Describe the access control matrix and its two practical representations.
A: The **access control matrix** is a theoretical construct: rows = subjects (users/processes), columns = objects (files, devices), cells = permitted operations. Too large to store directly. Practical representations: **ACLs (Access Control Lists)** — stored column-by-column on each object (POSIX `rwxr-xr--` is a compact ACL). Easy to revoke all access to an object; hard to find all objects a subject can access. **Capability lists** — stored row-by-row; each subject holds unforgeable tokens. Easy to delegate a right; hard to revoke from all holders.

Q: What is the difference between RBAC and MAC?
A: **RBAC (Role-Based Access Control)**: users are assigned to roles (Admin, Operator, ReadOnly); roles are assigned rights. Simplifies large organisations — adding an admin is a role assignment, not thousands of ACL edits. **MAC (Mandatory Access Control)**: the OS enforces system-wide policies that users *cannot override*. Bell-LaPadula (confidentiality): no read-up, no write-down. Biba (integrity): no read-down, no write-up. SELinux and AppArmor are practical MAC implementations in Linux using type enforcement.

Q: Name the major memory-corruption defenses and what each mitigates.
A: **ASLR** (Address Space Layout Randomisation): randomises load addresses of stack, heap, libraries — makes it hard to predict return addresses for buffer overflow exploits. **DEP / NX bit** (Data Execution Prevention): marks data regions non-executable — shellcode injected into the stack or heap cannot execute. **Stack canaries**: a random value placed before the saved return address; checked on function return — detects stack smashing before control is hijacked. **Code signing**: only loads kernel modules/extensions with valid cryptographic signatures.

---

**Malware**

Q: Distinguish virus, worm, trojan, and rootkit.
A: **Virus**: attaches to a host file; spreads by infecting other files when the host runs. Requires a host. **Worm**: standalone; spreads autonomously across networks without a host file. **Trojan horse**: appears useful but carries a hidden payload; spread by users running it voluntarily. **Rootkit**: modifies the OS kernel or bootloader to hide its presence — subverts OS visibility so it cannot be detected from within the compromised OS.

Q: What is return-oriented programming (ROP), and which defenses mitigate it?
A: ROP chains together short instruction sequences ("gadgets") already present in legitimate code, each ending in a `RET` instruction, to execute arbitrary logic without injecting new code. DEP/NX is ineffective against ROP (no new code is injected). Mitigations: **ASLR** (randomises gadget addresses — harder to build reliable chains), **Control-Flow Integrity (CFI)** (restricts the set of valid branch targets), and **stack canaries** (detect stack corruption before the ROP chain can execute).

---

**Case Studies**

Q: Why is Linux described as "monolithic with loadable modules", and what is the trade-off?
A: All OS services (scheduler, memory manager, VFS, networking, drivers) share a single kernel address space — a **monolithic** design. This allows direct function calls between subsystems with no IPC overhead — high performance. **Loadable modules** (`.ko` files, `insmod`/`modprobe`) allow drivers and file systems to be added at runtime without rebooting. Trade-off: a buggy kernel module runs with full kernel privilege and can corrupt any kernel data structure — poor fault isolation vs. a microkernel.

Q: How does Linux's CFS (Completely Fair Scheduler) work?
A: CFS tracks each process's **virtual runtime** (vruntime) — actual CPU time weighted inversely by priority. Processes are stored in a **red-black tree** keyed by vruntime. The scheduler always picks the process with the smallest vruntime — the most "underserved" process. This achieves proportional fairness without discrete time-slice buckets and runs in $O(\log n)$ per pick-next operation.

Q: How does VFS enable Linux to support multiple file systems transparently?
A: VFS defines abstract objects (superblock, inode, dentry, file) and operations (lookup, read, write, fsync). Every file system driver (ext4, XFS, tmpfs, procfs, NFS) implements this interface. A `read()` system call on an ext4 file, a tmpfs file, or an NFS file all follow the same VFS path — the kernel dispatch table routes to the appropriate driver. Applications see a uniform POSIX API regardless of the underlying storage.

Q: What is Android's key architectural departure from standard Linux?
A: Android runs the Linux kernel but replaces the standard user-space with an Android-specific stack. Key differences: (1) **Binder IPC**: a custom kernel driver for fast, secure inter-process communication — Android's system services communicate via Binder rather than Unix sockets or pipes. (2) **Permission model**: every app declares required permissions in its manifest; the OS enforces them at install and runtime — a capability-style model on top of Linux UIDs. (3) **ART runtime** (formerly Dalvik): apps run as compiled bytecode on a managed runtime, not native executables.

Q: Describe Windows NT's hybrid architecture.
A: Windows NT is a **hybrid** (not fully microkernel) design. A thin HAL (Hardware Abstraction Layer) sits at the bottom. The **NT Executive** (kernel-mode components: Object Manager, Process Manager, Memory Manager, I/O Manager, Security Reference Monitor) runs in kernel space but is structured as cooperating modules rather than a flat monolithic blob. A **microkernel** handles scheduling, IPC, and interrupt handling. User-mode services (Win32 subsystem) communicate via LPC (Local Procedure Call). The **Registry** is the hierarchical persistent configuration store (replaces Unix config files).

---

## Compare and Contrast

**Type 1 vs Type 2 Hypervisors**

| Property | Type 1 (bare-metal) | Type 2 (hosted) |
|----------|--------------------|--------------------|
| Runs on | Hardware directly | Host OS |
| Performance | Better | Slightly worse |
| Typical use | Data centre | Desktop / dev |
| Examples | ESXi, Hyper-V, Xen, KVM | VirtualBox, VMware Workstation |

**Full Virtualisation vs Para-Virtualisation vs Hardware-Assisted**

| Approach | Guest modified? | Mechanism | Performance |
|----------|----------------|-----------|-------------|
| Full virtualisation | No | Trap-and-emulate or binary translation | Moderate |
| Para-virtualisation | Yes (hypercalls) | Hypercall interface | Good |
| Hardware-assisted (VT-x) | No | CPU VMX root/non-root modes | Best |

**ACLs vs Capabilities**

| Property | ACLs | Capabilities |
|----------|------|-------------|
| Organised by | Object | Subject |
| Revoke access to object | Easy (delete ACL entry) | Hard (find all holders) |
| Delegate a right | Harder | Easy (pass the token) |
| Audit "what can subject X access?" | Hard | Easy (enumerate capabilities) |
| Used in | POSIX, Windows NTFS | SeL4, Android intents, AWS IAM |

**Linux vs Android vs Windows NT — Key Distinctions**

| Property | Linux | Android | Windows NT |
|----------|-------|---------|------------|
| Kernel type | Monolithic + modules | Monolithic (Linux kernel) | Hybrid (Executive + microkernel) |
| Scheduler | CFS (red-black tree, vruntime) | CFS + Android energy-aware | NT priority preemptive |
| IPC | Unix sockets, pipes, signals | Binder (custom kernel driver) | LPC |
| File system | VFS → ext4/XFS/… | VFS → ext4/F2FS | NTFS + Registry |
| Config store | Text files in /etc | SQLite databases + permissions | Registry |

---

## Common Mistakes

1. **KVM is Type 1, not Type 2** — KVM is a kernel module that turns the Linux kernel into a Type 1 hypervisor. Because KVM guests run directly on hardware (in VMX non-root mode), it is classified as Type 1. QEMU alone (without KVM) is Type 2.

2. **Para-virtualisation requires source access** — you cannot para-virtualise a proprietary OS like Windows unless the vendor provides "enlightenments" (as Hyper-V does). Unmodified guest OSes require full virtualisation or hardware-assisted virtualisation.

3. **ASLR is probabilistic, not deterministic** — ASLR makes exploitation harder by randomising addresses, but an attacker with a memory leak can defeat it. It is a mitigation, not a prevention.

4. **ACLs on POSIX are three groups, not arbitrary** — standard POSIX permission bits only have three subjects (owner, group, other). True named-user ACLs require extended ACLs (`setfacl`). Students conflate the basic `rwxr-xr--` bits with full ACL systems.

5. **Android's Binder is not just RPC** — Binder provides identity-verified IPC with kernel-enforced caller identity and security tokens. It enables Android's permission model; comparing it to a "simple socket" misses this security dimension.

---

## Links Back

- [[Virtualization Fundamentals]] — why virtualise; Type 1 vs Type 2; full vs para vs hardware-assisted
- [[Hypervisors]] — trap-and-emulate; VT-x; binary translation; para-virt hypercalls
- [[OS Security Fundamentals]] — threat model; access control matrix; protection rings
- [[Access Control]] — ACL vs capabilities; RBAC; MAC (Bell-LaPadula, Biba, SELinux)
- [[Authentication and Protection]] — passwords; biometrics; 2FA; identity verification
- [[Malware and Defenses]] — malware taxonomy; buffer overflow; ROP; ASLR; DEP; canaries
- [[Linux Architecture Overview]] — monolithic + modules; CFS; VFS; buddy/slab allocator
- [[Android Architecture]] — Binder IPC; permission model; ART runtime
- [[Windows NT Architecture]] — hybrid architecture; HAL; Executive; LPC; Registry
- [[Case Studies Overview]] — hub for case studies
- [[Virtualization Overview]] — hub for virtualisation
- [[Security Overview]] — hub for security

## References
- [[CS Operating Systems/Sources/Sources Index|CS Operating Systems Sources Index]]
