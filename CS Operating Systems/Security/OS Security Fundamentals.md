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
# OS Security Fundamentals

Security is not a single feature but a property of the entire system. Operating system security focuses on enforcing policies about who can do what to which resources — and ensuring those policies cannot be circumvented.

## 🎯 Intuition
**The Core Idea:** Security is the OS ensuring only the right people do the right things to the right resources. Because security is a property of the entire system, a single weakness can undermine otherwise strong components.

**Analogy:** Think of a building's security system — ID badges (authentication), locked doors (access control), cameras (auditing), and fire exits (availability). If one layer fails, the whole building becomes vulnerable.

**Why It Matters:** A single vulnerability can compromise the entire system. Operating system security exists to protect confidentiality, integrity, and availability across the whole system.

## ⚙️ Core Mechanics
### CIA Triad
Attacks target one or more of these: eavesdropping (C), tampering (I), denial of service (A).

| Goal | Meaning |
|------|---------|
| **Confidentiality** | Information is accessible only to authorised parties |
| **Integrity** | Information is modified only by authorised parties in authorised ways |
| **Availability** | The system is usable when legitimate users need it |

### Threat Model
A threat model specifies:
- **Assets**: what we are protecting (data, computation, cryptographic keys).
- **Threats**: who the adversary is (external attacker, malicious app, rogue insider) and what they can do.
- **Attack surface**: all the points at which an adversary can try to enter or extract data.

### Principle of Least Privilege
Each process, user, and component should have only the minimum rights needed to perform its function. A process handling user uploads should not have access to the authentication database. This limits the damage when any component is compromised.

### Protection Boundaries

| Boundary | Mechanism |
|----------|-----------|
| User/kernel | Hardware privilege levels (ring 0 vs ring 3) |
| Process isolation | Separate address spaces enforced by MMU |
| File permissions | User/group/other read/write/execute bits |
| Network perimeter | Firewall, VPN, TLS |

## 🔬 Deep Dive
### How Boundaries Are Enforced
The OS relies on concrete enforcement mechanisms. User/kernel separation is backed by hardware privilege levels such as ring 0 vs ring 3. Process isolation is enforced with separate address spaces enforced by the MMU. File permissions use user/group/other read/write/execute bits. Network boundaries are reinforced with firewall, VPN, and TLS.

### Attack Surface Minimisation
The attack surface is all the points at which an adversary can try to enter or extract data. Security improves when unnecessary exposed interfaces, privileged services, and reachable components are reduced.

### Security vs Usability Trade-off
Stricter security policies increase friction for legitimate users. Password complexity requirements lead to password reuse or sticky notes. Security decisions must account for user behaviour.

## 🏋️ Practice
### Warm-Up
- Which CIA property does a DoS attack target, and why?
- Give one example each of an attack on confidentiality, integrity, and availability.
- Why is security considered a property of the entire system rather than a single feature?

### Core Problems
- A web server runs as root. Which principle does this violate, and what extra risk does that create?
- Match each mechanism to its boundary: ring 0 vs ring 3, MMU-enforced address spaces, user/group/other permission bits, and firewall/VPN/TLS.
- Design a threat model for a university file server. Identify its assets, threats, and attack surface.

### Challenge
- Explain how attack-surface minimisation and least privilege work together to reduce damage after a compromise.
- A company makes its security policy stricter but users start writing passwords on sticky notes. Analyse this as a security-versus-usability trade-off and propose a better balance.

## Supporting Chunks

- [[Security - The OS enforces protection through a threat model built on least privilege]]
- [[Security - ASLR and DEP make memory-corruption exploits harder by randomising layout and blocking execution]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 9.
