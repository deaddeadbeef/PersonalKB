---
id: chunk-csos-206
type: chunk
source: "[[raw-os-039]]"
source_loc: "SELinux and Mandatory Access Control"
topic: "security"
claim: "AppArmor uses pathname-based profiles rather than labels for simpler MAC configuration, while Android integrates SELinux with per-app types for kernel-level app sandboxing"
confidence: verified
supports:
  - "[[Access Control]]"
tags:
  - csos
  - csos/security
  - chunk
up: "[[CS Operating Systems]]"
---
# Security — AppArmor path-based MAC and Android SELinux sandboxing

## Context

AppArmor profiles (stored in /etc/apparmor.d/) define file access by pathname with r/w/x/m/k flags, capabilities, and network permissions. This is simpler than SELinux labels but less flexible (renaming files changes access). Android (since 5.0) assigns each app a unique SELinux type (untrusted_app, platform_app) with Binder IPC controlled by binder_call rules, enforcing isolation beyond Unix DAC.

## Why It Matters

AppArmor vs. SELinux represents the simplicity-vs-flexibility tradeoff in MAC. Android SELinux integration shows how MAC scales to mobile: every app is sandboxed at the kernel level, which is why Android malware cannot easily access other apps data.

## QnA Seeds

- Q: How does AppArmor path-based approach differ from SELinux labels?
- Q: How does Android use SELinux for per-app sandboxing?
- Q: What controls inter-app communication in Android SELinux policy?
