---
id: chunk-csa-020
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 9"
topic: "compression"
claim: "LZW builds a shared codebook dynamically as it encodes, so no dictionary needs to be transmitted — decoder reconstructs it from the output stream"
confidence: verified
supports:
  - "[[Data Compression Overview]]"
  - "[[LZW Compression]]"
tags:
  - csa
  - csa/compression
  - chunk
up: "[[CS Algorithms]]"
---
# Compression — LZW builds a shared codebook dynamically requiring no transmitted dictionary

## Context

Both encoder and decoder start with the same initial dictionary (e.g., all single characters). The encoder repeatedly finds the longest current-dictionary string matching the next portion of input, outputs its code, then adds the matched string extended by one character to the dictionary. The decoder receives codes and reconstructs the dictionary in sync — because it applies the same extension rule after each code, it arrives at the same dictionary as the encoder without any explicit transmission. LZW is effective on repetitive data (source code, genomic sequences) and was used in GIF images and Unix `compress`.

## Why It Matters

LZW demonstrates adaptive compression: the codebook is tuned to the specific input being compressed, not to a pre-measured frequency table. This makes it a single-pass algorithm, unlike Huffman which requires a frequency scan first. The synchronised dictionary construction is a beautiful algorithmic trick.

## QnA Seeds

- Q: How does the LZW decoder know the codebook without receiving it?
- Q: Why is LZW effective on repetitive data but not on random data?
- Q: How does LZW differ from Huffman coding in its approach to compression?
