---
id: chunk-csa-031
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 9"
topic: "compression"
claim: "Run-length encoding replaces contiguous runs of the same symbol with (count, symbol) pairs — linear time, no stored table, and highly effective when runs are long"
confidence: verified
supports:
  - "[[Data Compression Overview]]"
  - "[[Run-Length Encoding]]"
tags:
  - csa
  - csa/compression
  - chunk
up: "[[CS Algorithms]]"
---
# Compression — Run-length encoding encodes same-symbol runs as count-symbol pairs

## Context

Scan the input left to right; count how many consecutive positions hold the same symbol. Output the pair (count, symbol). Repeat. Encoding and decoding are both linear in the input length — O(n). No codebook or frequency table is required; the format is self-describing.

**When it helps**: highly effective on inputs with long homogeneous runs. Classic example: binary (black-and-white) fax images. A typical document page consists mostly of white pixels with short black runs for text and graphics; runs of hundreds of same-coloured pixels are common. The ITU T.4 fax standard uses run-length encoding tuned to typical document statistics.

**When it hurts**: for inputs with frequent symbol changes (e.g., photographs with every-pixel variation), each run has length 1, so the output is larger than the input — the (count, symbol) pairs double the size.

**Worst case**: every element different → encoded length 2n vs. input length n → expansion by factor 2. In practice this is handled by mixing methods (e.g., DEFLATE uses LZ77 for pattern matching and Huffman for the output).

## Why It Matters

RLE illustrates that the best compression method depends entirely on the data distribution. It also shows that a single-pass, O(n) compression is achievable when structure is known in advance — no expensive frequency counting or codebook building.

## QnA Seeds

- Q: Describe the run-length encoding algorithm and its time complexity.
- Q: For what kinds of data does RLE achieve high compression ratios, and why?
- Q: When does RLE expand the data instead of compressing it?
