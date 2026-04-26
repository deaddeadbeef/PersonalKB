---
id: chunk-csos-143
type: chunk
source: "[[raw-os-024]]"
source_loc: "Boot Process"
topic: "foundations"
claim: "UEFI replaces BIOS with firmware that reads FAT32 partitions, supports GPT for disks over 2 TB, and enforces Secure Boot cryptographic verification of the boot chain"
confidence: verified
supports:
  - "[[Boot Process and Initialization]]"
tags:
  - csos
  - csos/foundations
  - chunk
up: "[[CS Operating Systems]]"
---
# Foundations — UEFI replaces BIOS with filesystem-aware secure firmware

## Context

Legacy BIOS loads a 512-byte MBR (446 bytes boot code, 64 bytes partition table, 2-byte 0x55AA signature) from the boot device. UEFI provides a richer firmware environment: it can read FAT32 partitions, supports GPT partition tables enabling disks larger than 2 TB, and loads EFI boot applications directly. Secure Boot uses X.509 certificates in firmware NVRAM to verify bootloader and kernel signatures.

## Why It Matters

UEFI is the foundation of modern system integrity. Every security guarantee of a running OS depends on a trustworthy boot chain. Understanding UEFI explains Secure Boot debates, Linux shim bootloaders, and why firmware-level attacks are so dangerous.

## QnA Seeds

- Q: What limitations of BIOS does UEFI address?
- Q: How does UEFI Secure Boot verify the boot chain?
- Q: What is the MBR structure and why is 512 bytes a limitation?
