---
tags: [cs-os, raw]
source_type: textbook_chapter
source_title: "OS Security Fundamentals"
authors: "Andrew S. Tanenbaum, Herbert Bos"
year: 2015
---

# OS Security Fundamentals

## Summary
Operating system security protects system resources from unauthorized access through three pillars: authentication (verifying identity), authorization (granting permissions), and access control enforcement. Access control models—DAC, MAC, and RBAC—define different policies for who can access what resources under which conditions. Modern OSes implement defense-in-depth against exploitation techniques, with countermeasures like ASLR, stack canaries, and NX bits protecting against the buffer overflow attacks that have been the dominant attack vector for decades.

## Key Claims
- Authentication establishes identity (who are you?), authorization determines permissions (what can you do?), and access control enforcement ensures that every resource access is checked against the authorization policy—a failure in any layer compromises the entire security model
- Discretionary Access Control (DAC) allows resource owners to set permissions at their discretion (Unix file permissions, Windows ACLs); this flexibility is also its weakness—a compromised process inherits all the user's permissions and can modify access controls
- Mandatory Access Control (MAC) enforces system-wide policies that even resource owners cannot override; SELinux and AppArmor implement MAC on Linux, confining processes to only the resources explicitly permitted by their security policy regardless of the process's user context
- Buffer overflow attacks exploit the adjacency of local variables and return addresses on the stack: by writing past a buffer's boundary, an attacker can overwrite the return address to redirect execution to injected shellcode or existing code gadgets (ROP)
- Modern defense-in-depth employs multiple independent mitigations: stack canaries detect stack corruption before function return, ASLR randomizes memory layout to prevent hardcoded addresses, and NX/DEP marks data pages as non-executable—defeating an attack requires bypassing all layers simultaneously

## Atomic Facts
1. Unix DAC uses a 12-bit permission model per file: three sets of read/write/execute bits for owner, group, and others, plus setuid, setgid, and sticky bits; setuid is particularly security-sensitive because it allows a program to run with the file owner's privileges regardless of who executes it
2. RBAC (Role-Based Access Control) assigns permissions to roles rather than individual users; users are assigned to roles, and a user's effective permissions are the union of all their roles' permissions—this model simplifies administration in organizations with many users and is mandated by standards like NIST RBAC
3. The Trusted Computing Base (TCB) is the set of hardware, firmware, and software components whose correctness is essential for security; minimizing the TCB (the microkernel philosophy) reduces the attack surface, while monolithic kernels have a larger TCB with more potential vulnerability points
4. Stack canaries (invented in StackGuard, 1998) place a random value between local variables and the saved return address; before returning, the function checks whether the canary value has been modified—if so, the process is terminated, preventing exploitation of the overwritten return address
5. ASLR (Address Space Layout Randomization) randomizes the base addresses of the stack, heap, shared libraries, and executable code at load time; on 64-bit systems, the entropy (typically 28–40 bits) makes brute-force guessing of addresses computationally infeasible
6. The principle of least privilege states that every process should operate with the minimum set of permissions needed to complete its task; Linux capabilities (CAP_NET_BIND_SERVICE, CAP_SYS_ADMIN, etc.) decompose root's monolithic power into 40+ individual capabilities that can be granted independently

## Significance
OS security is the foundation upon which all application security rests—if the kernel is compromised, no amount of application-level security can help. The ongoing arms race between attack techniques (ROP chains, side-channel attacks, kernel exploits) and defenses (ASLR, CFI, sandboxing) reflects a fundamental asymmetry: defenders must protect every possible entry point while attackers need only find one vulnerability. This asymmetry drives the defense-in-depth philosophy that characterizes modern OS security architecture.

## Chunks Extracted
- [[chunk-os-123 DAC Lets Owners Set Permissions but Inherits on Compromise]]
- [[chunk-os-124 MAC Enforces System-Wide Policies Owners Cannot Override]]
- [[chunk-os-125 Buffer Overflows Exploit Stack Adjacency of Locals and Return]]
- [[chunk-os-126 Least Privilege Decomposes Root Into Linux Capabilities]]
