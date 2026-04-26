---
tags:
  - csos
  - csos/casestudies
confidence: verified
up: "[[Case Studies Overview]]"
tier-coverage: [intuition, core, deep-dive, practice]
---
# Android Architecture

## 🎯 Intuition
**The Core Idea:** Android is a mobile operating system built on the **Linux kernel** but replacing most of the GNU userspace with Google-designed components optimised for constrained mobile hardware and app-store delivery.

**Analogy:** Linux is the foundation of a house, and Android builds custom mobile-specific rooms on top of it — Binder IPC, the framework, ART, and the permission model.

**Why It Matters:** Android grafts a mobile-optimised software stack onto Linux and now runs on billions of devices, making it one of the most widely deployed OS designs in history.

## ⚙️ Core Mechanics
### Layer Stack
```
┌───────────────────────────────┐
│   Applications (Java/Kotlin)  │  Maps, Chrome, camera apps
├───────────────────────────────┤
│   Android Framework (Java)    │  Activity Manager, Window Manager, ContentProvider
├───────────────────────────────┤
│   Native Libraries + ART      │  libc (Bionic), OpenGL ES, SQLite, ART runtime
├───────────────────────────────┤
│   Hardware Abstraction Layer  │  HAL modules (camera, audio, GPS)
├───────────────────────────────┤
│   Linux Kernel                │  Drivers, memory, scheduling, Binder driver
└───────────────────────────────┘
```

### Binder IPC
Android replaces POSIX pipes and sockets for inter-app communication with **Binder** — a kernel driver (`/dev/binder`) that enables high-performance, type-safe remote procedure calls between processes.

## 🔬 Deep Dive
### Binder IPC in Detail
- Shared memory for large data (avoids extra copy).
- Object references across process boundaries (unlike file descriptors which are process-local).
- Built-in death notification (client learns if the remote process died).
- Used by all Android services (ActivityManagerService, WindowManagerService, etc.).

### Permission Model
Each Android app runs in its own Linux UID (isolated address space). Apps declare required permissions in their `AndroidManifest.xml`. On Android 6+, **dangerous permissions** (camera, microphone, location) require runtime user approval. An app cannot access another app's data without an explicit content provider or shared UID.

### ART Runtime
Android Runtime (ART, replacing Dalvik since Android 5.0) compiles `.dex` bytecode to native machine code **ahead-of-time (AOT)** at install time. This eliminates JIT pauses during execution and improves battery life. A profile-guided compilation pass refines hot paths after the first few runs.

## 🏋️ Practice
### Warm-Up
1. What major kernel does Android build on?
2. What is Binder, and where does it live?
3. Why does Android assign each app its own Linux UID?

### Core Problems
1. Explain the role of each layer in the Android stack from Applications down to the Linux Kernel.
2. Why does Android use Binder instead of relying only on traditional POSIX pipes for service communication?
3. How does Android's per-app UID model provide isolation?

### Challenge
1. Compare Binder IPC with ordinary process-local file descriptor usage. Why are object references across process boundaries important?
2. What advantage does AOT compilation in ART have over Dalvik's JIT for mobile devices?
3. A malicious app requests camera access but the user denies the runtime permission. Explain how Android's permission model and sandboxing work together to contain it.

## Supporting Chunks

- [[Case Studies - Android extends Linux with Binder IPC and a permission-based app sandbox]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 10.
