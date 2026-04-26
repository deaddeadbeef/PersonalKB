---
id: chunk-csa-050
type: chunk
source: "[[Erickson 2019 - Algorithms]]"
source_loc: "Chapter 11 — Data Compression"
topic: "compression"
claim: "LZW was covered by a Unisys/IBM patent until 2003–2004, which drove PNG and the DEFLATE format to avoid it; this illustrates how intellectual property constraints shape algorithm adoption"
confidence: verified
supports:
  - "[[LZW Compression]]"
tags:
  - csa
  - csa/compression
  - chunk
up: "[[CS Algorithms]]"
---
# Compression — LZW patent history and PNG DEFLATE choice illustrate how IP affects algorithm adoption

## Context

LZW (Lempel-Ziv-Welch, 1984) was patented by Unisys and IBM. The GIF image format (1987) used LZW and was initially patent-free in practice; however, in 1994–1995 Unisys began enforcing its patent on GIF encoders, creating licence fees for software developers. This triggered the creation of the **PNG** (Portable Network Graphics) format in 1995 as an open, patent-free alternative.

PNG uses **DEFLATE** for compression — a combination of LZ77 (an earlier Lempel-Ziv variant without patent coverage) and Huffman coding. DEFLATE is also the basis of gzip and zlib. The Unisys LZW patent expired in the US in 2003 and internationally by 2004, after which GIF encoding became freely implementable. By then, PNG was already dominant for lossless web graphics.

**Key distinction**: LZ77 (the basis of DEFLATE) and LZW are both Lempel-Ziv family algorithms, but LZ77 uses a sliding window over the *input stream* (referencing back to recent seen text) rather than an explicit growing dictionary. They share the adaptive-dictionary concept but differ in implementation, and LZ77 avoided the contested patents.

## Why It Matters

This history illustrates that algorithm selection in practice is not purely a performance question — intellectual property, licensing costs, and open standards play decisive roles. The same underlying compression insight (exploiting repeated substrings) led to two different implementations (LZW vs LZ77) with dramatically different adoption trajectories based entirely on patent coverage.

## QnA Seeds

- Q: Why did the PNG format choose DEFLATE over LZW?
- Q: What is the relationship between LZW and LZ77?
- Q: What happened to GIF encoder software in the mid-1990s and why?
- Q: When did the Unisys LZW patent expire, and what changed afterward?
