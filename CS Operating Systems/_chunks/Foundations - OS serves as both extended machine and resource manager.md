---
id: chunk-csos-001
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 1"
topic: "foundations"
claim: "The OS plays a dual role: an extended machine hiding hardware complexity, and a resource manager multiplexing CPU, memory, and I/O among processes"
confidence: verified
supports:
  - "[[OS Fundamentals]]"
tags:
  - csos
  - csos/foundations
  - chunk
up: "[[CS Operating Systems]]"
---
# Foundations — OS serves as both extended machine and resource manager

## Context

Tanenbaum opens Chapter 1 by establishing two complementary ways to think about what an OS is. The "extended machine" view (Dijkstra's "virtual machine") says the OS presents programs with clean, hardware-independent abstractions: files instead of disk sectors, sockets instead of Ethernet frames. The "resource manager" view says the OS arbitrates competing demands on finite hardware: it decides which of 50 processes runs on 4 CPUs this millisecond, and which disk I/O gets priority.

## Why It Matters

These two views predict what the OS must do in every design decision: provide useful abstractions (extended machine), and do so fairly and efficiently across multiple concurrent users (resource manager). A design choice that helps one view but ignores the other — e.g., an abstraction so general it cannot be implemented efficiently — is a red flag.

## QnA Seeds

- Q: What are the two roles of an operating system and how do they relate?
- Q: What does "extended machine" mean in the context of an OS?
- Q: Why must the OS manage resources rather than letting programs access hardware directly?
