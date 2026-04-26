---
tags: [cs-os, raw]
source_type: textbook_topic
source_title: "Network Stack in OS"
authors: Tanenbaum, Bos; Stevens
year: 2018
---

# Network Stack in OS

## Summary

The operating system's network stack implements the protocol layers that enable networked communication, typically organized according to the TCP/IP model (link, internet, transport, application). The kernel provides the socket abstraction as the primary API for network I/O, mapping loosely to the OSI model: sockets abstract transport-layer endpoints, while the kernel handles IP routing, TCP/UDP processing, and interfacing with network device drivers internally.

Packet flow for an incoming TCP segment follows a well-defined path: the NIC receives the frame and raises a hardware interrupt. The NIC driver copies the frame into a kernel socket buffer (`sk_buff` in Linux) and passes it up. The IP layer validates the header, checks routing tables, and processes options. If the packet is destined locally, it is passed to the transport layer. TCP performs sequence number validation, congestion window management, reassembly of out-of-order segments, and ACK generation. Finally, the data is placed in the socket's receive buffer, where it becomes available to the application via `recv()`/`read()`. For outgoing data, the path reverses: the application writes to the socket, TCP segments the data and adds headers, IP adds its header and selects the output interface, and the driver queues the frame for transmission by the NIC.

NAPI (New API) in Linux combines interrupt-driven and polling-based packet processing. After the first packet interrupt, the driver switches to polling mode to batch-process packets, reducing interrupt overhead at high packet rates. The kernel can process thousands of packets per interrupt cycle with NAPI.

Zero-copy I/O optimizations reduce unnecessary data copies. The `sendfile()` system call transfers data directly from a file's page cache to a socket buffer without copying through user space, commonly used by web servers. For maximum performance, kernel bypass frameworks like DPDK (Data Plane Development Kit) map NIC queues directly into user-space memory, allowing applications to process packets without any kernel involvement. DPDK achieves line-rate processing (10–100 Gbps) but requires dedicated CPU cores and bypasses the kernel's protocol stack entirely, sacrificing its security model and multi-tenant isolation.

## Key Claims

- The kernel's network stack implements TCP/IP protocol processing in kernel space, exposing the socket abstraction as the user-space API for all network I/O operations
- Packet processing follows a layered path through the kernel (NIC driver → IP → TCP/UDP → socket buffer), with each layer adding or removing headers and performing protocol-specific validation
- NAPI's hybrid interrupt/polling model reduces per-packet interrupt overhead at high packet rates by batching packet processing during poll cycles
- Zero-copy techniques like sendfile() eliminate user-space data copies, reducing CPU overhead and memory bandwidth consumption for bulk data transfers
- Kernel bypass (DPDK) achieves maximum packet processing performance by mapping NIC hardware directly to user space, trading kernel isolation and security for raw throughput

## Atomic Facts

1. The Linux `sk_buff` structure is the fundamental packet representation in the kernel, containing pointers to packet headers at each layer, reference counts, and metadata for routing decisions
2. `sendfile(out_fd, in_fd, offset, count)` transfers data from a file descriptor to a socket without copying to user space, reducing a web server's file-serving path from four copies to two (or one with DMA scatter-gather)
3. Linux Generic Receive Offload (GRO) coalesces multiple small received packets into fewer large packets before passing them up the stack, reducing per-packet processing overhead
4. TCP window scaling (RFC 7323) allows receive windows up to 1 GB, necessary for high-bandwidth-delay-product paths
5. DPDK uses hugepages (2 MB or 1 GB) for packet buffer memory to reduce TLB misses, and binds NIC queues to specific CPU cores via the UIO or VFIO driver frameworks
6. The `epoll` system call enables a single thread to efficiently monitor thousands of sockets for I/O readiness, forming the basis of event-driven servers (nginx, Node.js)

## Significance

The OS network stack is one of the most performance-critical kernel subsystems, as network throughput directly impacts application responsiveness and data center efficiency. Understanding the packet processing path illuminates key systems concepts: interrupt handling, DMA, zero-copy optimization, and the tradeoff between kernel isolation and raw performance. The evolution from simple interrupt-per-packet processing to NAPI, zero-copy, and kernel bypass reflects the broader tension between abstraction safety and hardware-speed data processing.

## Chunks Extracted

*Pending*
