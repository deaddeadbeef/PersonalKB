---
id: mos-ch-01
type: book-chapter
chapter: 1
book: "Modern Operating Systems"
author: "Andrew S. Tanenbaum"
status: seeded
chunk_count: 5
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
tags:
  - csos
  - book-chapter
up: "[[Chapter Index]]"
confidence: verified
---
# MOS — Chapter 01: Introduction

## Summary

Tanenbaum opens by defining what an operating system is and why it exists: a layer of software that abstracts messy, heterogeneous hardware into clean, uniform interfaces for programs, while simultaneously arbitrating shared access to physical resources. The chapter traces OS history from batch systems through multiprogramming, timesharing, personal computing, and mobile/cloud systems. A hardware review covers CPUs, memory hierarchies, I/O, and buses. The critical distinction between kernel mode and user mode establishes the protection boundary. System calls are introduced as the precise interface through which user programs request OS services. The chapter closes with a survey of OS structure styles: monolithic, microkernel, hybrid, and exokernel.

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| Extended machine | OS presents idealised hardware to programs via clean abstractions |
| Resource manager | OS multiplexes CPU, memory, and I/O among competing processes |
| Kernel mode | CPU privilege level allowing unrestricted hardware access |
| System call | Controlled entry point into kernel via software interrupt |
| Monolithic kernel | All OS services run in a single kernel address space |
| Microkernel | Minimal kernel; most services run as user-space servers |

## Chunk Candidates

- [x] [[Foundations - OS serves as both extended machine and resource manager]]
- [x] [[Foundations - Kernel mode and user mode enforce the hardware privilege boundary]]
- [x] [[Foundations - System calls are the controlled interface from user space to the kernel]]
- [x] [[Foundations - Monolithic kernels colocate all OS services for performance]]
- [x] [[Foundations - Microkernels move services to user space for reliability at a performance cost]]

## Wiki Pages Seeded

- [[OS Fundamentals]] — OS purpose, dual role, history framing
- [[System Calls]] — system call mechanism, trap, POSIX examples
- [[OS Structure]] — monolithic, microkernel, hybrid, exokernel

## References

See [[Sources Index#Tanenbaum 2015]].
