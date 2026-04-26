---
id: chunk-csa-051
type: chunk
source: "[[MIT OCW 6006 - Introduction to Algorithms]]"
source_loc: "Lecture 12 — Data Compression"
topic: "compression"
claim: "Adaptive Huffman coding updates the code tree dynamically after each symbol, enabling single-pass encoding, but requires more complex bookkeeping than static Huffman and may perform worse on non-stationary sources"
confidence: verified
supports:
  - "[[Huffman Coding]]"
tags:
  - csa
  - csa/compression
  - chunk
up: "[[CS Algorithms]]"
---
# Compression — Adaptive Huffman coding enables single-pass encoding at the cost of implementation complexity

## Context

Standard (static) Huffman coding requires two passes: the first scans the input to build a frequency table; the second encodes the input using the code tree built from those frequencies. The frequency table (or the code tree) must be transmitted to the decoder before the encoded data.

**Adaptive Huffman** (Vitter, 1987) eliminates the pre-scan:
1. Encoder and decoder start with the same initial empty-or-default tree.
2. Both update the tree *in sync* after each symbol is processed.
3. The decoder reconstructs the identical sequence of trees because it sees the same encoded stream.

**Advantages**:
- Single-pass: data can be encoded as it arrives (streaming / on-the-fly compression).
- No separate dictionary transmission needed.

**Disadvantages and tradeoffs**:
- The tree update algorithm (maintaining the Huffman invariant — the sibling property — after each symbol) is significantly more complex to implement correctly than building a static tree once.
- The code tree is sub-optimal at the start of the stream, before enough symbols have been seen to converge to good frequencies. For short files, this overhead can result in worse compression than static Huffman.
- On non-stationary sources (where symbol frequencies change over time), adaptive Huffman tracks the distribution — but may lag abrupt changes.

## Why It Matters

Adaptive Huffman represents the tradeoff between implementation complexity and online operability. It is the forerunner of modern adaptive entropy coders (arithmetic coding variants, ANS). Understanding the two-pass vs one-pass distinction is important for choosing between static and adaptive schemes in practice.

## QnA Seeds

- Q: What does adaptive Huffman coding gain over static Huffman, and what does it give up?
- Q: Why do both encoder and decoder maintain identical code trees in adaptive Huffman?
- Q: When might static Huffman outperform adaptive Huffman?
- Q: What is the sibling property and why must adaptive Huffman maintain it?
