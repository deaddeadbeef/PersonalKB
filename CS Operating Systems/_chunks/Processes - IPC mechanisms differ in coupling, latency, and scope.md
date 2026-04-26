---
id: chunk-csos-009
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 2"
topic: "processes"
claim: "IPC mechanisms — shared memory, pipes, message passing, and signals — trade off bandwidth, coupling, and scope; no single mechanism is optimal for all situations"
confidence: verified
supports:
  - "[[Interprocess Communication]]"
tags:
  - csos
  - csos/processes
  - chunk
up: "[[CS Operating Systems]]"
---
# Processes — IPC mechanisms differ in coupling, latency, and scope

## Context

Shared memory achieves the highest bandwidth (no copying — producer and consumer read the same RAM) but requires explicit synchronisation and only works within a machine. Pipes are sequential and lightweight, natural for shell pipelines, but unidirectional and byte-stream only. Message passing is the most general — works across machines, provides natural structuring — but copies data through the kernel. Signals deliver only a number (no payload), are asynchronous, and are used for lifecycle events, not data transfer.

## Why It Matters

Choosing the right IPC mechanism has large performance and architectural implications. A web server handling 10,000 connections/sec cannot afford kernel-boundary crossings on every inter-thread communication; shared memory + atomic operations is the right choice. A microservice sending structured events across a network needs message passing (gRPC, Kafka). Android's Binder is specifically designed to be the lowest-latency cross-process RPC on a single device.

## QnA Seeds

- Q: What IPC mechanism has the highest bandwidth and why?
- Q: When is message passing preferred over shared memory?
- Q: What information does a UNIX signal carry?
