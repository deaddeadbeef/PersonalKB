---
id: chunk-csos-033
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 6"
topic: "deadlocks"
claim: "A cycle in the resource-allocation graph is a necessary condition for deadlock with single-instance resources; with multiple instances, a cycle is necessary but not sufficient"
confidence: verified
supports:
  - "[[Deadlock Fundamentals]]"
  - "[[Deadlock Detection and Recovery]]"
tags:
  - csos
  - csos/deadlocks
  - chunk
up: "[[CS Operating Systems]]"
---
# Deadlocks — Resource-allocation graph cycles indicate potential deadlock

## Context

The resource-allocation graph has two node types: process circles and resource squares (with dots for instances). Request edges (process → resource) show what a process is waiting for; assignment edges (resource → process) show what is currently allocated. For single-instance resources, a cycle in this graph is necessary and sufficient for deadlock. For multi-instance resources, a cycle is necessary but not sufficient — additional analysis (the Banker-style detection algorithm) is required to determine if deadlock actually exists.

## Why It Matters

The graph provides an intuitive visual framework for reasoning about deadlock. System monitoring tools can construct resource-allocation graphs from lock acquisition traces and check for cycles to detect deadlock in production. The extension to multi-instance resources is non-trivial and motivates the more complex detection algorithms covered in Chapter 6.

## QnA Seeds

- Q: What do request edges and assignment edges represent in a resource-allocation graph?
- Q: For a single-instance resource system, what does a cycle in the resource graph prove?
- Q: Why is a cycle in a multi-instance resource graph insufficient to conclude deadlock?
