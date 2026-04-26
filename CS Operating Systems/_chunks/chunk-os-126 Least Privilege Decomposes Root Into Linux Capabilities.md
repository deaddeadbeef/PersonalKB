---
id: chunk-csos-126
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 9 — OS Security Fundamentals"
topic: "security"
claim: "The principle of least privilege requires every process to operate with the minimum permissions needed; Linux capabilities decompose root's monolithic power into 40+ independent capabilities (e.g., CAP_NET_BIND_SERVICE) that can be granted individually"
confidence: verified
supports:
  - "[[OS Security Fundamentals]]"
  - "[[Authentication and Protection]]"
tags:
  - csos
  - csos/security
  - chunk
up: "[[CS Operating Systems]]"
---
# Security — Least privilege decomposes root into independent Linux capabilities

## Context

Traditionally, Unix had a binary privilege model: a process either ran as root (all permissions) or as a normal user (limited permissions). This violated the principle of least privilege — a web server needing to bind port 80 required full root access. Linux capabilities decompose root's monolithic power into 40+ individual permissions: CAP_NET_BIND_SERVICE (bind ports < 1024), CAP_SYS_ADMIN (broad administrative operations), CAP_DAC_OVERRIDE (bypass file permission checks), etc. A process can be granted only the specific capabilities it needs. The Trusted Computing Base (TCB) — the set of components whose correctness is essential for security — benefits from this decomposition because fewer components run with excessive privilege.

## Why It Matters

Capabilities are the mechanism behind container privilege dropping (Docker drops most capabilities by default), systemd service hardening, and rootless operation. They transform the security question from "does this need root?" (binary) to "which specific operations does this need?" (granular).

## QnA Seeds

- Q: What problem does the principle of least privilege solve in Unix's traditional root model?
- Q: Name three Linux capabilities and what each permits.
- Q: How do Linux capabilities relate to the Trusted Computing Base?
