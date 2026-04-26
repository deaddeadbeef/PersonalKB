---
id: mos-ch-09
type: book-chapter
chapter: 9
book: "Modern Operating Systems"
author: "Andrew S. Tanenbaum"
status: seeded
chunk_count: 5
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
tags:
  - csos
  - book-chapter
up: "[[Chapter Index]]"
---
# MOS — Chapter 09: Security

## Summary

Security is framed around the CIA triad (Confidentiality, Integrity, Availability). The chapter covers the OS's role as the enforcement layer between untrusted code and protected resources. The threat model includes external attackers, malicious software, and rogue insiders. Authentication mechanisms (passwords with hashing, biometrics, multi-factor) establish identity. The access control framework is developed from the theoretical access control matrix through practical implementations: ACLs attached to objects and capability lists held by subjects; RBAC as a scalability improvement. Mandatory access controls (Bell-LaPadula, Biba) enforce system-wide policies. Malware taxonomy covers viruses, worms, Trojans, rootkits, and ransomware, with corresponding defenses: sandboxing, address-space layout randomisation (ASLR), data-execution prevention (DEP), stack canaries, and code signing.

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| CIA triad | Confidentiality, Integrity, Availability — security goals |
| Least privilege | Give each process the minimum rights it needs |
| ACL | Access control list: per-object list of (subject, rights) pairs |
| Capability | Unforgeable token held by a subject granting specific rights |
| ASLR | Randomise load addresses to defeat address-dependent exploits |
| Rootkit | Malware that modifies the OS itself to hide its presence |

## Chunk Candidates

- [x] [[Security - The OS enforces protection through a threat model built on least privilege]]
- [x] [[Security - Access control lists and capability lists are dual representations of the access matrix]]
- [x] [[Security - Authentication verifies identity before granting access using passwords biometrics or tokens]]
- [x] [[Security - Malware exploits range from viruses to rootkits each requiring layered defenses]]
- [x] [[Security - ASLR and DEP make memory-corruption exploits harder by randomising layout and blocking execution]]

## Wiki Pages Seeded

- [[OS Security Fundamentals]] — CIA triad, threat model, least privilege, attack surface
- [[Access Control]] — access matrix, ACLs, capabilities, RBAC, MAC
- [[Authentication and Protection]] — passwords, hashing, biometrics, MFA, Kerberos
- [[Malware and Defenses]] — virus, worm, rootkit; ASLR, DEP, sandboxing

## References

See [[Sources Index#Tanenbaum 2015]].
