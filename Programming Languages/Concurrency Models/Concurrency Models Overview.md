---
tags: [programming-languages, concurrency]
up: "[[Programming Languages]]"
confidence: established
freshness: stable
tier-coverage: [intuition, core, deep-dive]
---
# Concurrency Models Overview

Concurrency — executing multiple computations in overlapping time periods — is the defining challenge of modern software. How a language handles concurrency reveals its deepest assumptions about safety, performance, and programmer ergonomics. The choices are not just technical — they're philosophical.

## The Fundamental Problem

Shared mutable state plus concurrency equals bugs. When multiple threads can read and write the same data simultaneously, race conditions, deadlocks, and data corruption become possible. Every concurrency model is, at its core, a strategy for managing this tension.

## Major Concurrency Models

| Model | Key Idea | Languages |
|-------|----------|-----------|
| Threads + Locks | OS threads with mutual exclusion | C, C++, Java, Python |
| CSP (Channels) | Communicating Sequential Processes | Go, Rust (channels), Clojure (core.async) |
| Actor Model | Isolated processes with message passing | Erlang, Elixir, Akka (Scala/Java) |
| Async/Await | Cooperative task scheduling | JavaScript, Rust, Python, C#, Swift, Kotlin |
| STM | Software Transactional Memory | Haskell, Clojure |
| Data Parallelism | Same operation on collections | CUDA, SIMD intrinsics, array languages |

## Design Philosophy Spectrum

**Don't share anything:** Erlang's actor model — each process has its own memory, communication only via message passing. Data races are impossible by construction.

**Share carefully:** Rust — shared state is allowed but the type system prevents data races at compile time. Send and Sync traits encode thread safety in the type system.

**Share with discipline:** Go — goroutines share memory but the idiom is "don't communicate by sharing memory; share memory by communicating" (via channels).

**Share freely, lock manually:** Java, C++ — full shared-memory concurrency with programmer-managed synchronization. Maximum flexibility, maximum danger.

## In This Hub

- [[Threads and Locks]]
- [[CSP and Channel-Based Concurrency]]
- [[The Actor Model]]
- [[Async-Await and Event Loops]]
- [[Software Transactional Memory]]

## References

- [[Programming Languages/Sources/Sources Index|Sources Index]]
