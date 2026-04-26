---
id: chunk-csos-052
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 11"
topic: "casestudies"
claim: "The Windows Registry is a hierarchical key-value persistent store that centralises all system and application configuration, replacing the fragmented .ini file approach of Win16"
confidence: verified
supports:
  - "[[Windows NT Architecture]]"
tags:
  - csos
  - csos/casestudies
  - chunk
up: "[[CS Operating Systems]]"
---
# Case Studies — The Windows Registry is a hierarchical persistent configuration store replacing ini files

## Context

The Windows 3.1/MS-DOS era used scattered `.ini` text files for configuration — each application managed its own, and there was no system-wide store. NT introduced the Registry: a binary tree of keys (folders) and values (typed data: strings, DWORDs, binary blobs), persisted in hive files (`%SystemRoot%\System32\config\SYSTEM`, `SOFTWARE`, etc.). The Registry is loaded by the kernel at boot; user hives are loaded on login. All hardware, driver, service, and application configuration lives there. The Registry Editor (`regedit.exe`) and PowerShell's Registry provider expose it to administrators.

## Why It Matters

The Registry is central to Windows administration, troubleshooting, and security. Auto-start malware registers in `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`. Driver configurations live in `HKLM\SYSTEM\CurrentControlSet`. Understanding the Registry hive structure, loading sequence, and transactional update model (for crash consistency) is essential for Windows system administrators, malware analysts, and forensic investigators.

## QnA Seeds

- Q: What problem did the Windows Registry solve compared to .ini files?
- Q: Where in the Registry does malware commonly establish persistence?
- Q: What are the five major Registry root keys (hives) and what does each contain?
