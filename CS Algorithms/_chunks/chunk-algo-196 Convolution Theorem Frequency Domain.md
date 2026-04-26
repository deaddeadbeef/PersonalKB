---
id: chunk-csa-196
type: chunk
source: "[[Cormen 2022 - Fast Fourier Transform]]"
source_loc: "Convolution Theorem"
topic: "transforms"
claim: "The convolution theorem states that pointwise multiplication in frequency domain corresponds to convolution in time domain: DFT(a * b) = DFT(a) times DFT(b)"
confidence: verified
supports:
  - "[[FFT]]"
  - "[[Convolution]]"
tags:
  - csa
  - csa/transforms
  - chunk
up: "[[CS Algorithms]]"
---
# Transforms — Convolution theorem links pointwise multiplication to time-domain convolution

## Context

The convolution theorem is the mathematical foundation of FFT-based polynomial multiplication: the DFT of the convolution of two sequences equals the element-wise product of their DFTs. This means convolution (an O(n^2) operation in the time domain) can be computed in O(n log n) by transforming to frequency domain, multiplying pointwise, and transforming back. Applications extend beyond polynomials to signal filtering, image processing, and string matching via convolution-based pattern detection.

## Why It Matters

The convolution theorem is one of the most powerful tools in applied mathematics and algorithm design, enabling O(n log n) computation of operations that are naturally O(n^2).

## QnA Seeds

- Q: What does the convolution theorem state in terms of DFT?
- Q: How does the convolution theorem enable O(n log n) convolution?
- Q: What are applications of convolution beyond polynomial multiplication?
