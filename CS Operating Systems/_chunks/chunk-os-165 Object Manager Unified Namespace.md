---
id: chunk-csos-165
type: chunk
source: "[[raw-os-029]]"
source_loc: "Windows NT Kernel Architecture"
topic: "case-studies"
claim: "The Object Manager provides a unified namespace for all kernel resources — processes, threads, files, registry keys — using handle-based access with reference counting"
confidence: verified
supports:
  - "[[Windows NT Architecture]]"
tags:
  - csos
  - csos/case-studies
  - chunk
up: "[[CS Operating Systems]]"
---
# Case Studies — Object Manager unified kernel resource namespace

## Context

Every kernel resource in Windows (processes, threads, files, mutexes, registry keys) is an object managed by the Object Manager. Applications access objects through handles, and the Object Manager applies consistent security (ACL checking via the Security Reference Monitor), reference counting, and lifetime management. The registry is managed by the Configuration Manager and stores settings in hives (SYSTEM, SOFTWARE, SAM, SECURITY, NTUSER.DAT) as binary files.

## Why It Matters

The Object Manager's unified model means that security, naming, and lifetime management are consistent across all resource types. This explains Windows' handle-based API design and why resource leaks manifest as handle leaks.

## QnA Seeds

- Q: What does the Windows Object Manager provide for kernel resources?
- Q: How do applications access kernel objects in Windows?
- Q: What are registry hives and how are they stored?
