---
id: chunk-csos-145
type: chunk
source: "[[raw-os-024]]"
source_loc: "Boot Process"
topic: "foundations"
claim: "The initramfs provides a temporary root filesystem with drivers needed to mount the real root, enabling boot from RAID, LVM, or encrypted storage that requires drivers not built into the kernel"
confidence: verified
supports:
  - "[[Boot Process and Initialization]]"
tags:
  - csos
  - csos/foundations
  - chunk
up: "[[CS Operating Systems]]"
---
# Foundations — initramfs enables boot from complex storage

## Context

After the kernel decompresses and initializes the CPU and memory management, it mounts the initramfs — a cpio archive compressed with gzip, xz, or zstd, unpacked into a tmpfs. This temporary root contains essential drivers and tools to locate and mount the real root filesystem. Once the real root is mounted, the kernel executes init (PID 1) from it.

## Why It Matters

initramfs solves the chicken-and-egg problem: the kernel needs drivers to read the root filesystem, but those drivers may live on the root filesystem. This is critical for any non-trivial storage setup (RAID, LVM, LUKS encryption) and explains why initramfs corruption can prevent boot.

## QnA Seeds

- Q: What problem does initramfs solve during the boot process?
- Q: What format is the initramfs archive and how is it loaded?
- Q: Why is initramfs necessary for booting from encrypted or RAID volumes?
