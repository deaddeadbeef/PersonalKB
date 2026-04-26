---
id: chunk-csos-162
type: chunk
source: "[[raw-os-028]]"
source_loc: "Linux Kernel Architecture"
topic: "case-studies"
claim: "/proc and /sys virtual filesystems expose kernel internals and device models as file hierarchies, enabling monitoring and tuning without specialized tools"
confidence: verified
supports:
  - "[[Linux Kernel]]"
tags:
  - csos
  - csos/case-studies
  - chunk
up: "[[CS Operating Systems]]"
---
# Case Studies — proc and sys expose kernel as file hierarchies

## Context

/proc exposes process and kernel information as readable files (e.g., /proc/cpuinfo, /proc/meminfo, /proc/[pid]/maps). /proc/sys/ contains writable files for kernel tuning (e.g., /proc/sys/vm/swappiness, default 60). /sys (sysfs) exports the kernel device model as a hierarchical directory representing devices, drivers, and buses. The OOM killer uses /proc/[pid]/oom_score_adj for tuning.

## Why It Matters

The "everything is a file" philosophy applied to kernel introspection is uniquely powerful. It means cat, grep, and echo can replace specialized monitoring tools, making Linux kernel tuning accessible via standard shell operations.

## QnA Seeds

- Q: What is the difference between /proc and /sys in Linux?
- Q: How can kernel parameters be tuned via /proc/sys/?
- Q: What information does /proc/[pid]/maps expose about a process?
