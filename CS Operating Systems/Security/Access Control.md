---
tags:
  - csos
  - csos/security
confidence: verified
freshness: stable
up: "[[Security Overview]]"
tier-coverage:
  - intuition
  - core
  - deep-dive
  - practice
---
# Access Control

**Access control** determines which subjects (users, processes) are permitted to perform which operations on which objects (files, devices, memory regions, system calls). The OS enforces access control decisions at every resource access point.

## 🎯 Intuition
**The Core Idea:** Access control is the OS deciding "you may" or "you may not" perform a given operation on a given resource.

**Analogy:** Think of a hotel key-card system. Your key card acts like a capability that opens your room but not others; the front desk acts like an ACL system that decides who gets which permissions on which rooms.

**Why It Matters:** Without access control, any process could read any file, modify any device state, or corrupt any part of the system.

## ⚙️ Core Mechanics
### Access Control Matrix
The theoretical foundation is an access control matrix with subjects as rows and objects as columns. Each cell lists the permitted operations (rights) for that subject-object pair. The matrix is too large to store directly, so practical systems use derived representations.

### Access Control Lists (ACLs)
ACLs store the matrix **column by column**: each object has a list of (subject, rights) pairs. When a subject requests access, the OS looks up the ACL on the object.

**Example (POSIX):** `rwxr-xr--` encodes three subject groups (owner, group, other) each with read/write/execute bits. Extended ACLs (`setfacl`) add named users/groups.

**Advantage:** Easy to revoke all access to an object (delete the ACL).  
**Disadvantage:** Hard to find all objects accessible by a given subject (audit trail).

### Capability Lists
Capability lists store the matrix **row by row**: each subject holds a set of unforgeable **capabilities** (tokens) granting specific rights to specific objects. Presenting a capability is proof of the right.

**Advantage:** Easy to transfer a specific right (pass the capability token).  
**Disadvantage:** Revoking access to an object requires finding all holders of its capabilities.

### Role-Based Access Control (RBAC)
Rather than assigning rights directly to users, rights are assigned to **roles** (Admin, Operator, ReadOnly), and users are assigned to roles. This rights → roles → users structure simplifies management in large organisations: adding a new admin is a role assignment, not thousands of individual ACL edits.

## 🔬 Deep Dive
### ACLs and Capabilities as Dual Views
ACLs and capability lists are dual representations of the same underlying access control matrix. ACLs answer "who can access this object?" more naturally, while capabilities answer "what can this subject access?" more naturally.

### Mandatory Access Control (MAC)
The OS can enforce system-wide policies that individual users cannot override:
- **Bell-LaPadula model** (confidentiality): no read up, no write down — prevents leaking secrets to lower clearances.
- **Biba model** (integrity): no read down, no write up — prevents low-integrity data corrupting high-integrity data.
- **SELinux / AppArmor**: practical MAC implementations in Linux using type enforcement.

### Trade-offs in Real Systems
ACLs are convenient for per-object administration and revocation. Capability systems make delegation and transfer more natural. RBAC reduces administrative complexity in large organisations. MAC adds stronger guarantees, but can be harder to configure and may restrict flexibility.

## 🏋️ Practice
### Warm-Up
- In the access control matrix, what do rows represent and what do columns represent?
- Why are ACLs described as a column-by-column representation of the matrix?
- Why are capability lists described as using unforgeable tokens?

### Core Problems
- How would you revoke user X's access to all files using ACLs? How would the same revocation problem differ in a capability-based system?
- A system stores permissions as `rwxr-xr--`. Explain which categories of users those bits apply to and what rights each category has.
- Design an RBAC scheme for a hospital records system. Define roles, assign rights to roles, and explain how users would be assigned.

### Challenge
- In Bell-LaPadula, can a Top Secret process write to an Unclassified file? Justify your answer using the model's rules.
- Compare ACLs and capabilities for a distributed system where rights must often be delegated temporarily. Which representation is more natural, and what revocation problem remains?
- A Linux server uses SELinux/AppArmor in addition to normal file permissions. Explain what extra protection MAC provides beyond discretionary access control.

## Supporting Chunks

- [[Security - Access control lists and capability lists are dual representations of the access matrix]]

## See Also

- [[File System Implementation]] — permission bits and ACLs are stored in inode metadata and checked on every file operation
- [[Address Spaces]] — hardware address-space isolation is the memory-protection complement to access control
- [[Hypervisors]] — VM isolation enforces access boundaries between guest operating systems
- [[Processes Overview]] — processes act as subjects in the access-control model; privilege separation limits damage

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 9.
