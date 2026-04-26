---
tags: [cs-ds, chunk]
id: chunk-ds-059
source: "[[raw-ds-040]]"
supports: ["[[Tries and Prefix Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# FM-index enables full-text search in compressed space

## Context
Full-text indices traditionally require several times the text size.

## Claim
The FM-index combines the Burrows-Wheeler Transform with wavelet trees and rank/select operations to support pattern counting in space often smaller than the original text.

## Why It Matters
Powers modern genome aligners like BWA and Bowtie indexing a 3GB genome in about 1GB.

## QnA Seeds
- Q: What is the BWT? -> A: Permutation of text that groups similar contexts and is highly compressible.
- Q: How is pattern search efficient? -> A: Backward search narrows the suffix array interval by one character per step.
