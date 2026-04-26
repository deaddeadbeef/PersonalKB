---
id: chunk-csos-166
type: chunk
source: "[[raw-os-029]]"
source_loc: "Windows NT Kernel Architecture"
topic: "case-studies"
claim: "The I/O Manager uses a layered IRP-based driver model where requests flow through stacks of filter, function, and bus drivers, enabling extensibility without modifying existing drivers"
confidence: verified
supports:
  - "[[Windows NT Architecture]]"
tags:
  - csos
  - csos/case-studies
  - chunk
up: "[[CS Operating Systems]]"
---
# Case Studies — IRP-based layered driver model for I/O

## Context

I/O Request Packets (IRPs) are the fundamental I/O data structure in Windows. Each IRP contains a stack of IO_STACK_LOCATION entries, one per driver in the device stack. Requests flow through filter drivers, function drivers, and bus drivers, with each adding or processing information. NTFS uses a Master File Table (MFT) with 1 KB entries; files under ~700 bytes fit entirely within the MFT entry.

## Why It Matters

The IRP model is why Windows supports such diverse I/O functionality (antivirus filter drivers, encryption layers, filesystem filters) without modifying the underlying drivers. Understanding the driver stack is essential for Windows driver development and I/O troubleshooting.

## QnA Seeds

- Q: What is an IRP and how does it flow through the Windows driver stack?
- Q: What types of drivers exist in a Windows device stack?
- Q: How does NTFS store small files efficiently in the MFT?
