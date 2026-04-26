---
tags: [cs-os, raw]
source_type: textbook_topic
source_title: "Distributed File Systems"
authors: Tanenbaum, Bos; Ghemawat, Gobioff, Leung
year: 2018
---

# Distributed File Systems

## Summary

Distributed file systems provide transparent access to files stored on remote servers, presenting a unified namespace that hides the physical location of data from applications. They extend the local filesystem abstraction across a network, enabling file sharing, centralized storage management, and data locality optimization for distributed computing.

NFS (Network File System), developed by Sun Microsystems in 1984, is the foundational Unix distributed filesystem. NFSv3 uses a stateless server design: each client request is self-contained, and the server maintains no per-client state, simplifying crash recovery (clients simply retry). NFS uses Remote Procedure Calls (RPC) over UDP or TCP, with file handles as opaque identifiers. NFSv4 introduced stateful operations (open/close, delegations, byte-range locking) for better performance and WAN support. NFS mounts appear as local directories, providing location transparency via the VFS layer.

CIFS/SMB (Common Internet File System / Server Message Block) is the Windows-native distributed filesystem protocol. SMBv3 supports encryption, multichannel (multiple network paths), and transparent failover. It provides mandatory file locking, distributed access control via ACLs, and integrates with Active Directory for authentication.

AFS (Andrew File System), developed at Carnegie Mellon, introduced whole-file caching on the client with server callbacks: the client caches the entire file locally, and the server promises to notify the client (callback) if another client modifies the file. This dramatically reduces server load for read-heavy workloads. AFS uses Kerberos for authentication and supports volume-level replication.

GFS (Google File System) and its open-source counterpart HDFS (Hadoop Distributed File System) were designed for large-scale, append-heavy workloads on commodity hardware. GFS uses a single master for metadata (namespace, chunk-to-server mapping) and large chunk sizes (64 MB) to reduce metadata overhead. Data is replicated across three chunk servers by default. HDFS follows the same architecture with a NameNode for metadata and DataNodes for storage. These systems optimize for high-throughput sequential access rather than low-latency random operations. Consistency models vary: NFS offers close-to-open consistency, AFS provides session semantics (writes visible at close), and GFS provides relaxed consistency with defined semantics for concurrent appends.

## Key Claims

- NFS achieves simple crash recovery through stateless server design in v3 (each request is self-contained), while NFSv4 introduced statefulness for performance features like delegations and byte-range locking
- AFS whole-file caching with server callbacks dramatically reduces server load for read-heavy workloads by serving most reads from the client's local cache
- GFS/HDFS optimize for large-scale sequential access on commodity hardware using large chunk sizes (64 MB), three-way replication, and a single metadata master, accepting relaxed consistency
- Consistency models across distributed file systems represent different tradeoffs: NFS close-to-open, AFS session semantics, and GFS relaxed consistency each optimize for different workload patterns
- SMB/CIFS integrates deeply with Windows infrastructure through Active Directory authentication, mandatory locking, and distributed ACLs, reflecting the Windows ecosystem's stateful design philosophy

## Atomic Facts

1. NFSv3 is stateless—the server does not track which clients have files open; all state (file offset, caching) is managed by the client, enabling simple crash recovery via client retry
2. AFS callback breaks notify clients of cached file invalidation; a callback promise is a guarantee from the server that it will inform the client before allowing any modification by another client
3. GFS uses a 64 MB chunk size (vs. typical 4–64 KB filesystem blocks) to reduce metadata size and amortize the cost of network round trips over large sequential transfers
4. HDFS default replication factor is 3: one replica on the local rack, one on a different node in the same rack, and one on a node in a different rack for rack-level fault tolerance
5. NFS close-to-open consistency guarantees that changes written and closed by one client are visible to another client that subsequently opens the same file
6. AFS uses Kerberos tickets for mutual authentication between client and server, providing strong identity verification without transmitting passwords

## Significance

Distributed file systems are fundamental infrastructure for networked computing, from enterprise file sharing (NFS, SMB) to cloud-scale data processing (HDFS). They illustrate core distributed systems challenges: consistency, caching, fault tolerance, and scalability. The design spectrum from NFS's simplicity to GFS's large-scale optimization demonstrates how workload characteristics drive architectural decisions. Understanding distributed file systems is essential for systems architecture, cloud computing, and big data infrastructure.

## Chunks Extracted

*Pending*
