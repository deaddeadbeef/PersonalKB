---
id: chunk-csos-191
type: chunk
source: "[[raw-os-036]]"
source_loc: "Concurrency Bugs and Detection"
topic: "synchronization"
claim: "Atomicity violations account for ~70% of non-deadlock concurrency bugs, where a programmer assumes a code region executes atomically but interleaving breaks the invariant"
confidence: verified
supports:
  - "[[Concurrency Bugs]]"
tags:
  - csos
  - csos/synchronization
  - chunk
up: "[[CS Operating Systems]]"
---
# Synchronization — Atomicity violations are most common concurrency bug

## Context

The Lu et al. 2008 study of 105 bugs in MySQL, Apache, Mozilla, and OpenOffice found atomicity violations were ~70% of non-deadlock bugs. An atomicity violation occurs when a sequence intended to be atomic is interrupted: Thread A reads a pointer, Thread B sets it to NULL, Thread A dereferences NULL. The study also found 97% of non-deadlock bugs involved only one or two variables.

## Why It Matters

Knowing that atomicity violations dominate real-world concurrency bugs redirects defensive programming effort: the priority is ensuring compound operations are properly protected, not just individual memory accesses. The one-or-two-variables finding suggests targeted tool support can catch most bugs.

## QnA Seeds

- Q: What is an atomicity violation and why is it the most common concurrency bug?
- Q: What percentage of concurrency bugs did the Lu et al. study find were atomicity violations?
- Q: How many variables are typically involved in real-world concurrency bugs?
