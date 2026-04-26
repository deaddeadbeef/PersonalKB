---
id: chunk-csos-203
type: chunk
source: "[[raw-os-039]]"
source_loc: "SELinux and Mandatory Access Control"
topic: "security"
claim: "MAC enforces administrator-defined policies that no user or process can override, addressing DAC's weakness where compromised apps inherit all user permissions"
confidence: verified
supports:
  - "[[Access Control]]"
tags:
  - csos
  - csos/security
  - chunk
up: "[[CS Operating Systems]]"
---
# Security — MAC enforces admin policies overriding DAC

## Context

Under Discretionary Access Control (DAC), file owners control permissions and any process running as a user inherits all that user access rights. If an application is compromised, the attacker gains full user access. MAC enforces centrally-defined policies regardless of ownership or privileges. SELinux implements MAC in the Linux kernel, supplementing DAC with deny-by-default type enforcement.

## Why It Matters

The DAC-vs-MAC distinction is foundational to OS security. MAC explains why a compromised web server on an SELinux system cannot read user home directories even if running as root — the type enforcement policy explicitly denies it regardless of Unix permissions.

## QnA Seeds

- Q: What fundamental weakness of DAC does MAC address?
- Q: Why can a process not override MAC policies even with root privileges?
- Q: How does SELinux supplement rather than replace DAC?
