---
id: chunk-csa-193
type: chunk
source: "[[Cormen 2022 - Fast Fourier Transform]]"
source_loc: "FFT Algorithm"
topic: "transforms"
claim: "FFT computes the Discrete Fourier Transform in O(n log n) by exploiting root-of-unity symmetry in a divide-and-conquer decomposition of even and odd coefficients"
confidence: verified
supports:
  - "[[FFT]]"
  - "[[Divide and Conquer]]"
tags:
  - csa
  - csa/transforms
  - chunk
up: "[[CS Algorithms]]"
---
# Transforms — FFT computes DFT in O(n log n) via even-odd decomposition

## Context

The DFT evaluates a degree n-1 polynomial at the n-th roots of unity. The naive computation is O(n^2). The Cooley-Tukey FFT splits the polynomial into even-indexed and odd-indexed coefficients, recursively computes the DFT of each half-size problem, then combines using the butterfly operation: A(w^k) = A_even(w^(2k)) + w^k * A_odd(w^(2k)). The key identity w^(k+n/2) = -w^k halves the work at each level. The inverse FFT uses conjugated roots and 1/n scaling.

## Why It Matters

FFT is widely considered one of the most important algorithms of the 20th century, with applications spanning signal processing, image compression, telecommunications, and scientific computing.

## QnA Seeds

- Q: How does the Cooley-Tukey FFT decompose the DFT computation?
- Q: What identity of roots of unity enables the butterfly operation?
- Q: How does the inverse FFT relate to the forward FFT?
