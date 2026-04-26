---
id: chunk-csos-121
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 7 — Containers and OS-Level Virtualization"
topic: "virtualization"
claim: "Docker images use a union filesystem with copy-on-write layers: a base image layer is shared read-only across all containers, and each container adds a thin writable layer — layers are identified by SHA256 hash and deduplicated"
confidence: verified
supports:
  - "[[Virtualization Overview]]"
  - "[[File System Implementation]]"
tags:
  - csos
  - csos/virtualization
  - chunk
up: "[[CS Operating Systems]]"
---
# Virtualization — Docker union filesystem uses copy-on-write layers

## Context

Docker images are built as stacks of read-only layers, each identified by the SHA256 hash of its contents. A base image layer (e.g., Ubuntu) is shared across all containers that use it. Each container adds a thin writable layer on top for its modifications using copy-on-write — a file is only copied to the writable layer when it is first modified. Layers are pulled and stored independently, so pulling a new image sharing base layers with existing images only downloads the new layers. The OCI (Open Container Initiative, 2015) standardized the image format (image-spec) and runtime specification (runtime-spec), enabling interoperability between Docker, Podman, containerd, and CRI-O.

## Why It Matters

The layered image model explains Docker's speed and efficiency: images are space-efficient (shared base layers), fast to build (only changed layers rebuilt), and fast to distribute (only missing layers downloaded). It's the same copy-on-write principle seen in Btrfs/ZFS snapshots applied to application packaging.

## QnA Seeds

- Q: How does Docker's copy-on-write layer model save disk space?
- Q: What is the OCI and what does it standardize?
- Q: Why does pulling a new Docker image often download very little data?
