---
id: chunk-csos-123
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 9 — OS Security Fundamentals"
topic: "security"
claim: "Discretionary Access Control (DAC) allows resource owners to set permissions at their discretion — this flexibility is its weakness because a compromised process inherits all the user's permissions and can modify access controls"
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
# Security — DAC lets owners set permissions but inherits all permissions on compromise

## Context

DAC is the default access control model in Unix/Linux and Windows. Unix uses a 12-bit permission model per file: three sets of read/write/execute bits for owner, group, and others, plus setuid, setgid, and sticky bits. Setuid is particularly security-sensitive because it allows a program to run with the file owner's privileges regardless of who executes it. Under DAC, a compromised process runs with all of the owning user's permissions and can freely modify access controls — if a web server process is exploited, the attacker gets all permissions of the www-data user, and can potentially escalate via setuid binaries.

## Why It Matters

DAC's vulnerability to compromised processes is the core motivation for MAC systems like SELinux and AppArmor. Understanding DAC's limitations also explains the principle of least privilege — running services as dedicated low-privilege users minimizes the blast radius of a compromise.

## QnA Seeds

- Q: What is the fundamental weakness of discretionary access control?
- Q: Why is the setuid bit a security concern?
- Q: How does running services as low-privilege users mitigate DAC's weakness?
