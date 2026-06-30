---
tags:
  - csos
  - moc
up: "[[CS Operating Systems]]"
confidence: verified
---
# Security Overview

Operating system security defines who can do what, detects and recovers from attacks, and hardens the system against exploitation. This domain covers threat modeling, access control models, authentication mechanisms, and the defenses against malware and memory-corruption exploits.

---

## Learn in This Order

1. [[OS Security Fundamentals]] — threat model; principle of least privilege; attack surface; trusted computing base
2. [[Access Control]] — ACLs; capability lists; RBAC; mandatory access control (MAC); protection domains
3. [[Authentication and Protection]] — password hashing; biometrics; Kerberos; protection rings
4. [[Malware and Defenses]] — viruses, worms, rootkits; exploit mitigations (ASLR, DEP/NX); sandboxing

---

## In This Domain

| Page | One-line summary |
|------|-----------------|
| [[OS Security Fundamentals]] | Threat model; least privilege; attack surface; TCB |
| [[Access Control]] | ACLs vs capability lists; RBAC; MAC; protection domains |
| [[Authentication and Protection]] | Passwords; biometrics; Kerberos; protection rings |
| [[Malware and Defenses]] | Malware taxonomy; ASLR; DEP; sandboxing |

---

## Common Distinctions

| Question | Answer |
|----------|--------|
| ACL vs capability list? | ACL = per-object list of who has access (easy to revoke). Capability = per-subject token granting access (easy to delegate). They are duals; OS access control uses both depending on context. |
| Authentication vs authorization? | Authentication = verifying *who* you are (passwords, biometrics). Authorization = verifying *what* you can do (ACLs, RBAC). |
| ASLR vs DEP? | ASLR randomises memory layout to make exploit addresses unpredictable. DEP/NX marks memory regions non-executable to prevent shellcode execution. Used together for defense-in-depth. |
| Least privilege? | Each component should operate with the minimum permissions needed. Violation is the most common root cause of privilege escalation attacks. |

---

## How to Navigate

- **Starting with security?** [[OS Security Fundamentals]] establishes the threat model and vocabulary.
- **Access control design?** [[Access Control]] covers all major models.
- **Authentication system?** [[Authentication and Protection]]
- **Understanding modern exploit mitigations?** [[Malware and Defenses]]

---

## Related Domains

- **[[OS Foundations Overview]]** — kernel/user-mode separation and protection rings are the hardware enforcement mechanism for OS security.
- **[[Processes Overview]]** — process isolation and address space separation are the OS's primary security primitives.
- **[[Case Studies Overview]]** — Android's permission model and Windows' mandatory integrity control are Security concepts applied in real systems.

## References
- [[CS Operating Systems/Sources/Sources Index|CS Operating Systems Sources Index]]
