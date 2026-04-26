---
id: chunk-csa-049
type: chunk
source: "[[CP Algorithms - Online Reference]]"
source_loc: "Run-Length Encoding article"
topic: "compression"
claim: "Run-length encoding yields compression only when the expected run length exceeds 2; otherwise each run of length 1 becomes a 2-element pair and the output is larger than the input"
confidence: verified
supports:
  - "[[Run-Length Encoding]]"
tags:
  - csa
  - csa/compression
  - chunk
up: "[[CS Algorithms]]"
---
# Compression — Run-length encoding is effective only when expected run length exceeds two symbols

## Context

RLE replaces each run of k identical symbols with the pair (k, symbol). For this to compress:
- A run of length k encodes as 2 values (count + symbol) instead of k values.
- **Compression only occurs if k > 2**: runs of length 1 expand from 1 value to 2; runs of length 2 stay the same; runs of length 3+ shrink.
- **Break-even**: average run length = 2 exactly; input and output are the same size.
- **Worst case**: every symbol is distinct — an n-symbol input becomes a 2n-symbol output.

**Real-world implications**:
- **BMP bitmap images**: uncompressed Windows BMP supports a RLE variant (RLE4/RLE8) that is effective for simple graphics (flat-colour regions, icons) but counterproductive for photographs (no long runs).
- **Fax (ITU T.4 / G3)**: black-and-white text pages contain long white-pixel runs; RLE (combined with Huffman-coded run lengths) achieves 5–10× compression. The ITU standard embeds run-length frequencies directly into the Huffman code tables.
- **General text**: natural language has few long character runs; RLE is ineffective and is replaced by LZ-family or Huffman approaches.

## Why It Matters

Understanding the break-even condition explains why RLE is a domain-specific tool rather than a general-purpose compressor. Applying RLE naively to incompatible data (e.g., JPEG image output, already-compressed text) guarantees expansion, not compression. This motivates the use of pre-analysis (histogram of run lengths) before choosing a compression method.

## QnA Seeds

- Q: What is the minimum run length for RLE to achieve compression?
- Q: When does RLE expand rather than compress its input?
- Q: Why is RLE effective for fax documents but not for photographic images?
- Q: In what file formats is RLE encoding used, and what data properties make those formats good candidates?
