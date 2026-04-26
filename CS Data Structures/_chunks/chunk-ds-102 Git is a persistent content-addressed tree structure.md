---
tags: [cs-ds, chunk]
id: chunk-ds-102
source: "[[raw-ds-024]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Git is a persistent content-addressed tree structure

## Context
Version control needs to track all historical states efficiently.

## Claim
Git stores snapshots as a DAG of content-addressed objects: blobs (files), trees (directories), and commits (snapshots). Unchanged files share blob objects across commits providing structural sharing identical to persistent data structures.

## Why It Matters
Proof that persistent data structure concepts power critical real-world infrastructure at massive scale.

## QnA Seeds
- Q: What is content-addressing? -> A: Object identity is its SHA-1 hash. Same content same address.
- Q: How does Git achieve structural sharing? -> A: Unchanged subtrees reuse the same tree object across commits.
