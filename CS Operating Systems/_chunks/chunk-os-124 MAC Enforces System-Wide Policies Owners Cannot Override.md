---
id: chunk-csos-124
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 9 — OS Security Fundamentals"
topic: "security"
claim: "Mandatory Access Control (MAC) enforces system-wide security policies that even resource owners cannot override — SELinux and AppArmor implement MAC on Linux, confining processes to explicitly permitted resources regardless of user context"
confidence: verified
supports:
  - "[[Access Control]]"
  - "[[OS Security Fundamentals]]"
tags:
  - csos
  - csos/security
  - chunk
up: "[[CS Operating Systems]]"
---
# Security — MAC enforces system-wide policies that owners cannot override

## Context

Unlike DAC where the resource owner decides permissions, MAC policies are set by a system administrator and enforced by the kernel regardless of user identity or ownership. SELinux (developed by the NSA) assigns security labels to every process and resource, and a policy engine checks every access against label-matching rules. AppArmor uses path-based profiles that specify which files and capabilities a program may use. Under MAC, even if an attacker compromises a root-owned process, the process is still confined to only the resources its MAC policy permits — it cannot access arbitrary files or make arbitrary system calls.

## Why It Matters

MAC is what makes security confinement possible beyond DAC's "all or nothing" user permission model. It's essential for container security (Docker uses AppArmor profiles by default), Android's app sandboxing (SELinux), and any system where defense must survive process compromise.

## QnA Seeds

- Q: How does MAC differ from DAC in who controls access policies?
- Q: What is the difference between SELinux's label-based and AppArmor's path-based approaches?
- Q: Why does MAC still confine a compromised root process?
