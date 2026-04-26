---
id: chunk-csa-168
type: chunk
source: "[[Gusfield 1997 - Suffix Trees and Arrays]]"
source_loc: "BWT and Compressed Indexes"
topic: "strings"
claim: "The Burrows-Wheeler Transform derived from the suffix array clusters characters by context, enabling compressed text indexes like FM-index for pattern matching near entropy space"
confidence: verified
supports:
  - "[[BWT]]"
  - "[[FM-Index]]"
tags:
  - csa
  - csa/strings
  - chunk
up: "[[CS Algorithms]]"
---
# Strings — BWT enables compressed text indexing near entropy-bounded space

## Context

The Burrows-Wheeler Transform (BWT) permutes the text such that characters with similar contexts are clustered, enabling effective compression via run-length encoding and move-to-front coding. The BWT is derivable from the suffix array and forms the foundation of compressed full-text indexes like the FM-index, which supports pattern matching in space close to the text's entropy. This powers bioinformatics tools (Bowtie, BWA) for read mapping and is the basis of bzip2 compression.

## Why It Matters

The BWT bridges string indexing and compression, enabling simultaneous pattern matching and space-efficient storage—a critical capability for genomics and large-scale text processing.

## QnA Seeds

- Q: How does the BWT cluster characters by context?
- Q: What is the FM-index and how does it relate to the BWT?
- Q: Why is the BWT important in bioinformatics tools like Bowtie?
