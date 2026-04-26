---
id: chunk-csos-189
type: chunk
source: "[[raw-os-035]]"
source_loc: "Distributed File Systems"
topic: "file-systems"
claim: "GFS and HDFS use a single metadata master, 64 MB chunk sizes, and three-way replication for large-scale sequential access on commodity hardware with relaxed consistency"
confidence: verified
supports:
  - "[[Distributed File Systems]]"
tags:
  - csos
  - csos/file-systems
  - chunk
up: "[[CS Operating Systems]]"
---
# File Systems — GFS HDFS optimize for large-scale sequential access

## Context

GFS (Google) and HDFS (Hadoop) target large-scale append-heavy workloads. A single master handles metadata (namespace, chunk-server mapping) while data is split into 64 MB chunks replicated three times (one local rack, one same rack, one different rack for fault tolerance). These systems optimize for high-throughput sequential access, accepting relaxed consistency for concurrent operations.

## Why It Matters

GFS/HDFS architecture is the foundation of big data infrastructure. Understanding the design choices (large chunks to reduce metadata, single master for simplicity, three-way replication for fault tolerance) explains how MapReduce and Spark process petabytes of data reliably.

## QnA Seeds

- Q: Why do GFS and HDFS use 64 MB chunk sizes?
- Q: How does HDFS replicate data across the cluster for fault tolerance?
- Q: What role does the single metadata master play and what is its limitation?
