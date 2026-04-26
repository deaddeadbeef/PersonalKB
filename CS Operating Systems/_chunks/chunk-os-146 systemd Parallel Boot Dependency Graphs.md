---
id: chunk-csos-146
type: chunk
source: "[[raw-os-024]]"
source_loc: "Boot Process"
topic: "foundations"
claim: "systemd replaced SysVinit by parallelizing service startup with dependency graphs, tracking services via cgroups, and supporting socket activation for on-demand launch"
confidence: verified
supports:
  - "[[Boot Process and Initialization]]"
tags:
  - csos
  - csos/foundations
  - chunk
up: "[[CS Operating Systems]]"
---
# Foundations — systemd parallelizes boot with dependency graphs

## Context

SysVinit started services sequentially through numbered runlevels (0-6). systemd instead uses targets as runlevel analogs (multi-user.target = runlevel 3, graphical.target = runlevel 5) and builds a dependency graph to start independent services in parallel. It tracks services via cgroups, supports socket activation for on-demand service launch, and provides journald for structured logging.

## Why It Matters

systemd dramatically reduced Linux boot times and changed how services are managed. Understanding targets, dependency ordering, and cgroup-based tracking is essential for Linux system administration and troubleshooting startup failures on modern distributions.

## QnA Seeds

- Q: How does systemd achieve faster boot times than SysVinit?
- Q: What are systemd targets and how do they replace runlevels?
- Q: How does systemd use cgroups for service management?
