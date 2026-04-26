---
id: chunk-csos-106
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 2 — Inter-Process Communication"
topic: "processes"
claim: "Remote Procedure Calls extend IPC across network boundaries by making remote function calls appear syntactically identical to local calls, hiding marshalling, transport, and error handling behind generated client/server stubs"
confidence: verified
supports:
  - "[[Interprocess Communication]]"
tags:
  - csos
  - csos/processes
  - chunk
up: "[[CS Operating Systems]]"
---
# Processes — RPC makes remote calls syntactically identical to local calls

## Context

RPC extends the IPC paradigm across network boundaries. The programmer writes interface definitions, and a compiler generates client stubs (which marshal parameters and send them over the network) and server stubs (which unmarshal and invoke the actual function). The calling code sees a normal function signature. This location transparency was first formalized by Birrell and Nelson (1984). Modern incarnations include gRPC (Google, 2015), which uses Protocol Buffers for serialization and HTTP/2 for transport, supporting streaming, bidirectional communication, and stub generation across 12+ languages.

## Why It Matters

RPC is the dominant paradigm for microservice communication today. Understanding that every RPC hides network latency, partial failure, and serialization overhead behind a local-looking call is essential — ignoring these "fallacies of distributed computing" leads to systems that appear correct in testing but fail unpredictably under real network conditions.

## QnA Seeds

- Q: What do client and server stubs do in an RPC system?
- Q: How does gRPC differ from traditional RPC frameworks?
- Q: Why is location transparency in RPC both a feature and a risk?
