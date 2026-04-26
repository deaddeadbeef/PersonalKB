---
id: chunk-csa-194
type: chunk
source: "[[Cormen 2022 - Fast Fourier Transform]]"
source_loc: "Polynomial Multiplication"
topic: "transforms"
claim: "Polynomial multiplication in O(n log n) via FFT uses the evaluate-multiply-interpolate paradigm: forward FFT, pointwise multiplication, inverse FFT"
confidence: verified
supports:
  - "[[FFT]]"
  - "[[Polynomial Multiplication]]"
tags:
  - csa
  - csa/transforms
  - chunk
up: "[[CS Algorithms]]"
---
# Transforms — O(n log n) polynomial multiplication via evaluate-multiply-interpolate

## Context

To multiply two degree-n polynomials: (1) evaluate both at 2n points using forward FFT in O(n log n), (2) multiply the 2n point values element-wise in O(n), (3) interpolate back to coefficient form using inverse FFT in O(n log n). Total: O(n log n), down from naive O(n^2) coefficient multiplication. The convolution theorem formalizes this: pointwise multiplication in frequency domain equals convolution in time domain, DFT(a * b) = DFT(a) * DFT(b). This underpins big integer multiplication algorithms like Schonhage-Strassen.

## Why It Matters

FFT-based polynomial multiplication is a foundational technique enabling faster string matching, big integer arithmetic, and computational algebra—understanding it unlocks many algorithm speedups.

## QnA Seeds

- Q: What are the three steps of FFT-based polynomial multiplication?
- Q: What does the convolution theorem state?
- Q: Why is FFT multiplication O(n log n) instead of O(n^2)?
