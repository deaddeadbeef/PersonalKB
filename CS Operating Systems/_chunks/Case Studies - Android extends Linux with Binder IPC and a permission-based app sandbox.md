---
id: chunk-csos-050
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 10"
topic: "casestudies"
claim: "Android builds on Linux but replaces POSIX IPC with Binder — a kernel driver enabling high-performance type-safe cross-process calls — and enforces app isolation via per-app Linux UIDs"
confidence: verified
supports:
  - "[[Android Architecture]]"
  - "[[Interprocess Communication]]"
tags:
  - csos
  - csos/casestudies
  - chunk
up: "[[CS Operating Systems]]"
---
# Case Studies — Android extends Linux with Binder IPC and a permission-based app sandbox

## Context

Android runs on Linux but its app ecosystem relies on Binder IPC rather than POSIX pipes or sockets. Binder is a character device (`/dev/binder`) that the kernel driver manages. Clients and servers register as Binder nodes; the kernel routes transactions between them, passing data via shared memory (avoiding extra copies). Each app gets a unique Linux UID at install time; apps cannot access each other's file system data without an explicit content provider. The Android permission model (AndroidManifest declarations + runtime grants) adds a second layer of access control on top of Linux's DAC.

## Why It Matters

Binder IPC is the backbone of the entire Android OS — all Android system services (ActivityManager, WindowManager, PackageManager) communicate via Binder. Understanding Binder is essential for Android security research, app performance optimisation, and reverse engineering. The UID-per-app isolation model is a key reason Android apps are better sandboxed than traditional desktop applications.

## QnA Seeds

- Q: Why did Google create Binder instead of using UNIX domain sockets?
- Q: How does Android use Linux UIDs to isolate apps?
- Q: What is the role of AIDL in Android Binder-based IPC?
