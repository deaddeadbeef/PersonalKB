---
id: chunk-csos-035
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 6"
topic: "deadlocks"
claim: "Deadlock prevention eliminates one Coffman condition structurally; resource ordering (eliminating circular wait) is the most practical prevention technique in real systems"
confidence: verified
supports:
  - "[[Deadlock Prevention]]"
tags:
  - csos
  - csos/deadlocks
  - chunk
up: "[[CS Operating Systems]]"
---
# Deadlocks — Prevention eliminates deadlock by attacking one Coffman condition structurally

## Context

The four prevention strategies correspond to the four Coffman conditions: make resources shareable (eliminating mutual exclusion — only works for read-only resources); require all-or-nothing resource requests (eliminating hold-and-wait — wastes resources, requires upfront knowledge); allow preemption (eliminating no-preemption — disrupts work-in-progress); or impose a global ordering on resources and require processes to request in ascending order (eliminating circular wait). The last strategy — lock ordering — is the only one widely used in production; Linux kernel developers follow lock class ordering enforced by the lockdep tool.

## Why It Matters

Prevention is the most conservative strategy: deadlock simply cannot occur. The cost is reduced utilisation or additional constraints on program structure. Lock ordering is the standard practice in OS kernel and database engine development. Understanding the four prevention attacks also clarifies why each of the other three strategies (avoidance, detection, ostrich) exists — each is a response to the practical unworkability of prevention in general.

## QnA Seeds

- Q: Which Coffman condition does resource ordering eliminate, and how?
- Q: Why is "require all resources upfront" impractical for most programs?
- Q: What is the lockdep tool in Linux and what prevention strategy does it enforce?
