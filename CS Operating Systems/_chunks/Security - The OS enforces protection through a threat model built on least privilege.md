---
id: chunk-csos-043
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 9"
topic: "security"
claim: "The OS enforces protection through the principle of least privilege: each process receives only the minimum rights needed for its function, limiting damage when any component is compromised"
confidence: verified
supports:
  - "[[OS Security Fundamentals]]"
tags:
  - csos
  - csos/security
  - chunk
up: "[[CS Operating Systems]]"
---
# Security — The OS enforces protection through a threat model built on least privilege

## Context

Every security decision in an OS is shaped by a threat model: who the adversary is, what they can do, and what assets they threaten. The principle of least privilege (Saltzer and Schroeder, 1975) prescribes that every component — process, user, service — should have the minimum access rights needed to do its job. Consequences: a web server process should not have read access to the password database; a browser renderer should not have write access to system files. Violating least privilege means a single exploit can escalate to full compromise.

## Why It Matters

Most high-profile security breaches exploit over-privileged processes or accounts. Least privilege is implemented in OS design through mechanisms: process UIDs, capability sets (Linux capabilities), mandatory access control (SELinux), seccomp system call filtering, and containers. Understanding the threat model → least privilege chain is the first step in designing secure systems.

## QnA Seeds

- Q: What is the principle of least privilege and why does it matter for OS security?
- Q: What is a threat model and what elements does it contain?
- Q: Name three OS mechanisms that implement least privilege.
