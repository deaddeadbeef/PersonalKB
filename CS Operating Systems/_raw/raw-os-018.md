---
tags: [cs-os, raw]
source_type: textbook_chapter
source_title: "Containers and OS-Level Virtualization"
authors: "Andrew S. Tanenbaum, Herbert Bos"
year: 2015
---

# Containers and OS-Level Virtualization

## Summary
Containers provide lightweight process isolation by leveraging Linux kernel features—namespaces for resource visibility isolation and cgroups for resource usage limits—without requiring a separate kernel per instance. Docker popularized container technology by packaging applications with their dependencies into portable, layered images. Compared to virtual machines, containers offer faster startup, lower overhead, and higher density, but share the host kernel, which introduces a different security model with a larger attack surface.

## Key Claims
- Linux namespaces provide the isolation foundation for containers: each namespace type creates an independent view of a specific system resource, so a containerized process sees its own PID tree, network stack, filesystem mounts, and user IDs without affecting or seeing the host's resources
- Control groups (cgroups) complement namespaces by enforcing resource limits (CPU, memory, I/O bandwidth, network) and accounting; without cgroups, a container could monopolize host resources, defeating the purpose of multi-tenant isolation
- Docker images use a union filesystem with copy-on-write layers: a base image layer (e.g., Ubuntu) is shared read-only across all containers using it, and each container adds a thin writable layer for its modifications—this makes images space-efficient and fast to distribute
- Containers start in milliseconds (vs. seconds-to-minutes for VMs) because there is no OS boot process—the container runtime simply creates namespaces, applies cgroups, and exec's the application process within the isolated environment
- Container security is fundamentally different from VM security because all containers share the host kernel; a kernel vulnerability exploitable from within a container compromises the host and all other containers—this is why defense-in-depth measures (seccomp, AppArmor, rootless containers) are essential

## Atomic Facts
1. Linux provides eight namespace types: PID (process IDs), Network (network interfaces, routing), Mount (filesystem mount points), UTS (hostname), IPC (System V IPC, POSIX message queues), User (UID/GID mapping), Cgroup (cgroup root), and Time (clock offsets, added in Linux 5.6)
2. Cgroups v2 (unified hierarchy, default since Linux 5.2/systemd 243) organizes resource controllers (cpu, memory, io, pids) in a single tree structure; cgroups v1 used separate hierarchies per controller, creating complex interactions and configuration inconsistencies
3. Docker uses a client-server architecture: the docker CLI communicates with the dockerd daemon, which manages images, containers, networks, and volumes; the actual container runtime is delegated to containerd and runc (the OCI-compliant low-level runtime)
4. A Docker image layer is identified by the SHA256 hash of its contents; layers are pulled and stored independently, so pulling a new image that shares base layers with an existing image only downloads the new layers—deduplication at the layer level
5. The Open Container Initiative (OCI) standardized the container image format (image-spec) and runtime specification (runtime-spec) in 2015, enabling interoperability between Docker, Podman, containerd, CRI-O, and other container tools
6. gVisor (Google) and Kata Containers (Intel/Hyper) address container security concerns by adding kernel-level isolation: gVisor interposes a user-space kernel (Sentry) that intercepts system calls, while Kata Containers runs each container inside a lightweight VM, combining container UX with VM-level isolation

## Significance
Containers transformed software deployment from "it works on my machine" to reproducible, portable artifacts that run identically across development, testing, and production environments. The container model—with Kubernetes as its orchestration layer—has become the default deployment unit for cloud-native applications, fundamentally changing how software is built, shipped, and operated at scale.

## Chunks Extracted
- [[chunk-os-119 Linux Namespaces Isolate Resource Visibility for Containers]]
- [[chunk-os-120 Cgroups Enforce Resource Limits Complementing Namespaces]]
- [[chunk-os-121 Docker Union Filesystem Uses Copy-on-Write Layers]]
- [[chunk-os-122 Container Security Shares Host Kernel Different Threat Model]]
