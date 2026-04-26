---
id: chunk-csos-190
type: chunk
source: "[[raw-os-035]]"
source_loc: "Distributed File Systems"
topic: "file-systems"
claim: "Distributed filesystem consistency models differ by workload: NFS uses close-to-open, AFS uses session semantics, and GFS uses relaxed consistency — each optimizing for different access patterns"
confidence: verified
supports:
  - "[[Distributed File Systems]]"
tags:
  - csos
  - csos/file-systems
  - chunk
up: "[[CS Operating Systems]]"
---
# File Systems — DFS consistency models reflect workload tradeoffs

## Context

NFS close-to-open guarantees that changes written and closed by one client are visible to another client that subsequently opens the same file. AFS session semantics make writes visible at close. GFS provides relaxed consistency with defined semantics for concurrent appends. SMB/CIFS integrates with Windows infrastructure via Active Directory, mandatory locking, and distributed ACLs.

## Why It Matters

Consistency model selection is one of the most important distributed system design decisions. Each model trades consistency for performance or simplicity. Understanding these tradeoffs explains why different file systems suit different workloads and why strong consistency everywhere is impractical.

## QnA Seeds

- Q: What does NFS close-to-open consistency guarantee?
- Q: How do AFS session semantics differ from NFS close-to-open?
- Q: Why does GFS accept relaxed consistency?
