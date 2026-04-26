---
id: chunk-csos-205
type: chunk
source: "[[raw-os-039]]"
source_loc: "SELinux and Mandatory Access Control"
topic: "security"
claim: "RBAC in SELinux restricts which types a user can transition to based on role assignment, limiting lateral movement even when type enforcement rules would permit the transition"
confidence: verified
supports:
  - "[[Access Control]]"
tags:
  - csos
  - csos/security
  - chunk
up: "[[CS Operating Systems]]"
---
# Security — RBAC restricts type transitions by user role

## Context

Role-Based Access Control layers over Type Enforcement: even if a TE rule allows a type transition, RBAC can block it if the user assigned role does not permit assuming that type. Multi-Level Security (MLS) adds sensitivity labels implementing the Bell-LaPadula model (no read up, no write down) for classified environments. The three layers (TE, RBAC, MLS) provide defense-in-depth.

## Why It Matters

RBAC adds a critical second layer of defense. Even if a type enforcement policy is overly permissive, RBAC limits what types users can assume. This defense-in-depth approach is why SELinux meets government security standards (CC EAL4+).

## QnA Seeds

- Q: How does RBAC layer over Type Enforcement in SELinux?
- Q: What does Multi-Level Security add beyond TE and RBAC?
- Q: What is the Bell-LaPadula model core rule?
