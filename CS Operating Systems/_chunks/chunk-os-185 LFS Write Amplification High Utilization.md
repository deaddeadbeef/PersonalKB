---
id: chunk-csos-185
type: chunk
source: "[[raw-os-034]]"
source_loc: "Log-Structured File Systems"
topic: "file-systems"
claim: "Write amplification in LFS increases sharply at high disk utilization — approximately 2/(1-u) in the worst case — because the cleaner must process increasingly full segments"
confidence: verified
supports:
  - "[[Log-Structured File Systems]]"
tags:
  - csos
  - csos/file-systems
  - chunk
up: "[[CS Operating Systems]]"
---
# File Systems — LFS write amplification grows sharply at high utilization

## Context

Write amplification is the ratio of total physical writes to logical writes. At high utilization (above 80-90%), segments have fewer dead blocks, so the cleaner copies more live data per reclaimed segment. The worst-case formula 2/(1-u) means 90% utilization can produce 20x write amplification. LFS checkpoints (written to fixed disk locations) record log head and inode map positions for crash recovery.

## Why It Matters

The write amplification curve is why LFS saw limited adoption for general-purpose disk workloads and why flash SSDs (which use LFS-like FTLs internally) recommend keeping 10-20% free space. Understanding this relationship is essential for capacity planning on any log-structured storage system.

## QnA Seeds

- Q: What is write amplification and why does it matter for LFS?
- Q: What write amplification does 90% utilization produce in the worst case?
- Q: How do LFS checkpoints enable crash recovery?
