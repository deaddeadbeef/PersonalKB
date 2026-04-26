---
id: chunk-csos-188
type: chunk
source: "[[raw-os-035]]"
source_loc: "Distributed File Systems"
topic: "file-systems"
claim: "AFS caches entire files on the client with server callback promises, dramatically reducing server load for read-heavy workloads by serving most reads locally"
confidence: verified
supports:
  - "[[Distributed File Systems]]"
tags:
  - csos
  - csos/file-systems
  - chunk
up: "[[CS Operating Systems]]"
---
# File Systems — AFS whole-file caching with server callbacks

## Context

AFS (Andrew File System), from Carnegie Mellon, caches the complete file on the client. The server issues a callback promise: it guarantees notification before allowing another client to modify the file. This means reads never contact the server after the initial fetch, dramatically reducing server load. AFS uses Kerberos for mutual authentication and supports volume-level replication.

## Why It Matters

AFS callback model is a landmark design for read-heavy distributed workloads. The callback-promise mechanism — where the server pushes invalidation rather than clients polling for changes — influenced subsequent distributed cache designs and CDN architectures.

## QnA Seeds

- Q: How does AFS reduce server load for read-heavy workloads?
- Q: What is a callback promise in AFS?
- Q: What authentication mechanism does AFS use?
