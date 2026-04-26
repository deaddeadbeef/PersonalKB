---
id: chunk-csos-187
type: chunk
source: "[[raw-os-035]]"
source_loc: "Distributed File Systems"
topic: "file-systems"
claim: "NFSv3 uses a stateless server design where each request is self-contained, enabling simple crash recovery through client retry without server-side session state"
confidence: verified
supports:
  - "[[Distributed File Systems]]"
tags:
  - csos
  - csos/file-systems
  - chunk
up: "[[CS Operating Systems]]"
---
# File Systems — NFS stateless design simplifies crash recovery

## Context

NFS (Network File System), developed by Sun in 1984, is the foundational Unix distributed filesystem. NFSv3 maintains no per-client state on the server: each request includes all information needed to service it, and caching is managed entirely by the client. When the server crashes and restarts, clients simply retry pending requests. NFSv4 introduced statefulness (open/close, delegations, byte-range locking) for better performance and WAN support.

## Why It Matters

NFS stateless design is a classic distributed systems simplification. Understanding why statelessness aids crash recovery — and why NFSv4 added state for performance — illustrates the fundamental statefulness tradeoff in distributed systems.

## QnA Seeds

- Q: Why does NFSv3 use a stateless server design?
- Q: How does NFSv3 crash recovery work compared to stateful protocols?
- Q: What statefulness did NFSv4 add and why?
