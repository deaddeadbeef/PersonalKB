---
id: chunk-csos-186
type: chunk
source: "[[raw-os-034]]"
source_loc: "Log-Structured File Systems"
topic: "file-systems"
claim: "F2FS adapts LFS for flash storage by aligning writes to erase block boundaries, separating hot and cold data across six log areas, and using adaptive logging"
confidence: verified
supports:
  - "[[Log-Structured File Systems]]"
tags:
  - csos
  - csos/file-systems
  - chunk
up: "[[CS Operating Systems]]"
---
# File Systems — F2FS adapts LFS principles for flash storage

## Context

F2FS (Flash-Friendly File System), developed by Samsung, aligns writes to flash erase block boundaries and uses six active log areas (hot/warm/cold for both data and node blocks) to separate data by update frequency. This concentrates dead blocks in hot segments, improving cleaner efficiency. Adaptive logging switches between normal and threaded modes based on free space. F2FS is the default filesystem on many Android devices.

## Why It Matters

F2FS demonstrates how LFS principles evolved for modern hardware. Understanding hot/cold data separation and erase-block alignment explains flash storage performance characteristics and why Android chose F2FS over ext4 for internal storage.

## QnA Seeds

- Q: How does F2FS adapt LFS principles for flash storage characteristics?
- Q: What are F2FS's six log areas and why does separating hot and cold data help?
- Q: Why is erase block alignment important for flash file systems?
