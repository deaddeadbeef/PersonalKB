---
id: chunk-csos-167
type: chunk
source: "[[raw-os-030]]"
source_loc: "Network Stack in OS"
topic: "io"
claim: "The kernel implements TCP/IP protocol processing internally and exposes the socket abstraction as the user-space API, with packets traversing NIC driver, IP, TCP/UDP, and socket buffer layers"
confidence: verified
supports:
  - "[[Network Stack]]"
tags:
  - csos
  - csos/io
  - chunk
up: "[[CS Operating Systems]]"
---
# IO — Kernel network stack implements TCP/IP with socket API

## Context

Incoming packets follow a layered path: NIC receives a frame and raises an interrupt, the driver copies it into an sk_buff (the fundamental Linux packet representation), IP validates headers and checks routing, TCP performs sequence validation and congestion management, and data lands in the socket receive buffer for the application. The reverse path applies for outgoing data.

## Why It Matters

Understanding packet flow through the kernel is essential for network performance tuning and debugging. The sk_buff structure and layered processing explain why network overhead exists and where optimization opportunities lie.

## QnA Seeds

- Q: What is the path of an incoming TCP packet through the Linux kernel?
- Q: What is sk_buff and why is it the fundamental packet structure?
- Q: How does the socket abstraction relate to the underlying protocol layers?
