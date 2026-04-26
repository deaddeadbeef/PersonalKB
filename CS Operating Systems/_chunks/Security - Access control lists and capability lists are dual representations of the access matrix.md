---
id: chunk-csos-044
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 9"
topic: "security"
claim: "The access control matrix defines which subjects can perform which operations on which objects; ACLs store it per-object, capability lists store it per-subject — both are incomplete dual representations"
confidence: verified
supports:
  - "[[Access Control]]"
tags:
  - csos
  - csos/security
  - chunk
up: "[[CS Operating Systems]]"
---
# Security — Access control lists and capability lists are dual representations of the access matrix

## Context

The full access control matrix (subjects × objects × rights) is too large to store directly. ACLs store a column: each object carries a list of (subject, rights) pairs. Revoking an object's access is easy (modify its ACL); finding all objects accessible by a subject requires scanning all ACLs. Capability lists store a row: each subject holds a list of unforgeable tokens (capabilities) granting rights to specific objects. Delegating a capability is easy (pass the token); revoking it requires finding all holders. Real systems (POSIX: ACLs; Android: permissions; Kerberos: tickets) implement one or a hybrid.

## Why It Matters

The ACL vs capability debate has concrete security implications. ACL systems are vulnerable to the confused deputy problem (a privileged program used by an unprivileged user to access objects the user cannot directly access). Capability systems avoid this by making rights explicit and transferable. Understanding both models is necessary for reasoning about access control in OS design, web API authorization, and microservice security.

## QnA Seeds

- Q: What is the confused deputy problem and which access control model is vulnerable to it?
- Q: How would you revoke all access to a specific file in an ACL system vs a capability system?
- Q: What does RBAC add on top of basic ACLs?
