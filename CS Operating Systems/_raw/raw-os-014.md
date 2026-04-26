---
tags: [cs-os, raw]
source_type: textbook_chapter
source_title: "Inter-Process Communication"
authors: "Andrew S. Tanenbaum, Herbert Bos"
year: 2015
---

# Inter-Process Communication

## Summary
Inter-process communication (IPC) enables processes with separate address spaces to exchange data and coordinate execution. The two fundamental paradigms are shared memory (fast but requires explicit synchronization) and message passing (safer but involves kernel mediation). Concrete IPC mechanisms—pipes, signals, sockets, and RPCs—build on these paradigms to provide varying levels of abstraction, performance, and network transparency suited to different application patterns.

## Key Claims
- Shared memory IPC is the fastest form of inter-process communication because once the shared region is established, data transfer involves no system calls and no kernel intervention—processes simply read and write memory at hardware speed
- Message passing via send/receive operations provides a cleaner abstraction than shared memory because the kernel handles synchronization and copying, eliminating the class of bugs caused by concurrent unsynchronized access to shared regions
- Pipes are the original Unix IPC mechanism and enforce a simple unidirectional byte-stream protocol; named pipes (FIFOs) extend this to unrelated processes by creating a filesystem entry that any process can open
- Signals are the Unix mechanism for asynchronous notification of events; they function as software interrupts delivered to a process, but their handler restrictions (only async-signal-safe functions may be called) make them tricky to use correctly
- Remote Procedure Calls (RPCs) extend the IPC paradigm across network boundaries by making remote function calls appear syntactically identical to local calls, hiding the complexity of marshalling, network transport, and error handling behind client/server stubs

## Atomic Facts
1. The producer-consumer problem is the canonical IPC scenario: a producer process generates data items and places them in a bounded buffer, while a consumer process removes and processes them; correct implementation requires synchronizing on buffer-full and buffer-empty conditions
2. POSIX shared memory is established with shm_open() to create a named shared memory object and mmap() to map it into the process's address space; the shared region persists in the filesystem namespace (/dev/shm on Linux) until explicitly unlinked
3. Synchronous (blocking) message passing causes the sender to block until the receiver calls receive and vice versa—this provides a natural synchronization point called a rendezvous, used in Ada's concurrency model
4. Unix anonymous pipes created by pipe() return two file descriptors (read end and write end) and work only between related processes (typically parent-child); the shell implements command pipelines (cmd1 | cmd2) by connecting stdout of cmd1 to stdin of cmd2 via a pipe
5. Unix signals include SIGKILL (9, cannot be caught or ignored, forces process termination), SIGTERM (15, polite termination request), SIGSEGV (11, segmentation fault), and SIGCHLD (17, child process status change); a process registers signal handlers via sigaction()
6. gRPC (Google, 2015) is a modern RPC framework using Protocol Buffers for serialization and HTTP/2 for transport, supporting streaming and bidirectional communication; it generates client and server stubs from .proto interface definitions across 12+ programming languages

## Significance
IPC mechanisms are the connective tissue of all non-trivial software systems. The evolution from simple pipes to network-transparent RPCs to modern gRPC frameworks traces the expansion of computing from single-machine programs to distributed microservice architectures. Understanding the tradeoffs between shared memory (performance) and message passing (safety, network transparency) remains central to system architecture decisions today.

## Chunks Extracted
- [[chunk-os-103 Shared Memory IPC Avoids Kernel Mediation]]
- [[chunk-os-104 Message Passing Provides Safety Through Kernel Mediation]]
- [[chunk-os-105 Unix Pipes Enforce Unidirectional Byte-Stream IPC]]
- [[chunk-os-106 RPC Makes Remote Calls Syntactically Identical to Local]]
