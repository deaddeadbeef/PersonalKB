---
id: chunk-csos-156
type: chunk
source: "[[raw-os-027]]"
source_loc: "Process Creation: fork/exec Model"
topic: "processes"
claim: "Copy-on-write makes fork() nearly free by sharing physical pages read-only and only copying when written, reducing fork from O(n) memory copy to approximately O(1) in fork+exec"
confidence: verified
supports:
  - "[[Process Creation]]"
tags:
  - csos
  - csos/processes
  - chunk
up: "[[CS Operating Systems]]"
---
# Processes — COW makes fork nearly free for fork-exec

## Context

Rather than duplicating all memory pages, fork() marks both parent and child page table entries as read-only pointing to the same physical frames. Only when either process writes is a copy made. In the common fork+exec pattern, the child's exec replaces the entire address space before any writes, so zero data pages are physically copied. On Linux, fork() is implemented via clone() with flags specifying resource sharing.

## Why It Matters

Without COW, forking a multi-gigabyte process would be impractically expensive. COW is why fork+exec remains viable for process creation even for large server processes, and why vfork() is largely obsolete.

## QnA Seeds

- Q: How does copy-on-write optimize fork() performance?
- Q: Why are zero pages copied in the common fork+exec pattern?
- Q: How is fork() implemented in the Linux kernel?
