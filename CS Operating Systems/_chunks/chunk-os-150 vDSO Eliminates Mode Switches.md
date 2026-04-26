---
id: chunk-csos-150
type: chunk
source: "[[raw-os-025]]"
source_loc: "System Calls and API"
topic: "foundations"
claim: "The vDSO maps frequently-called read-only kernel data into user space, allowing calls like gettimeofday() to execute without a mode switch, reducing overhead from ~1 us to ~20 ns"
confidence: verified
supports:
  - "[[System Calls]]"
tags:
  - csos
  - csos/foundations
  - chunk
up: "[[CS Operating Systems]]"
---
# Foundations — vDSO eliminates mode switches for time queries

## Context

The vDSO (virtual dynamic shared object) is a small shared library mapped by the kernel into every process's address space. It exports frequently-called read-only operations like gettimeofday() and clock_gettime() that can read kernel-maintained data without trapping into kernel mode. This reduces latency from ~1 microsecond (full syscall) to ~20 nanoseconds.

## Why It Matters

Time queries are among the most frequent system calls in high-performance applications. The vDSO optimization shows how the OS can selectively relax the user/kernel boundary for read-only data to achieve dramatic performance gains without compromising security.

## QnA Seeds

- Q: What is the vDSO and how does it avoid mode switches?
- Q: What performance improvement does vDSO provide for gettimeofday()?
- Q: Why is the vDSO safe despite bypassing the normal syscall path?
