---
id: chunk-csos-169
type: chunk
source: "[[raw-os-030]]"
source_loc: "Network Stack in OS"
topic: "io"
claim: "sendfile() transfers data directly from a file's page cache to a socket buffer without user-space copies, reducing the web server file-serving path from four copies to two or one"
confidence: verified
supports:
  - "[[Network Stack]]"
tags:
  - csos
  - csos/io
  - chunk
up: "[[CS Operating Systems]]"
---
# IO — sendfile zero-copy file to socket transfer

## Context

Traditional file serving requires: read from disk to page cache, copy to user buffer, copy to socket buffer, DMA to NIC — four data movements. sendfile(out_fd, in_fd, offset, count) eliminates the user-space copies, transferring directly from page cache to socket. With DMA scatter-gather support, this can be reduced to a single copy. The epoll system call enables a single thread to monitor thousands of sockets efficiently.

## Why It Matters

sendfile() is why web servers like nginx can serve static files with minimal CPU overhead. Understanding zero-copy I/O explains a major class of performance optimizations in networked applications and why kernel-user boundary crossings are expensive.

## QnA Seeds

- Q: How many data copies does sendfile() eliminate compared to read+write?
- Q: Why is copying data through user space wasteful for file serving?
- Q: What role does DMA scatter-gather play in zero-copy I/O?
