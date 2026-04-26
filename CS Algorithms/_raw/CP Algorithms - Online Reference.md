---
id: raw-csa-004
type: raw
title: "CP-Algorithms.com — Competitive Programming Algorithms Reference"
author: "cp-algorithms.com contributors"
year: 2024
publisher: "Open community reference (cp-algorithms.com)"
url: "https://cp-algorithms.com/"
status: processed
chunk_count: 4
tags:
  - csa
  - raw
  - open-access
up: "[[CS Algorithms]]"
---
# CP-Algorithms — Online Reference

## Bibliographic Reference

cp-algorithms.com contributors. *Competitive Programming Algorithms Reference*. Available free at https://cp-algorithms.com/ (continuously maintained; articles date from c. 2014 onwards, based on the e-maxx.ru Russian CP reference).

## Description

CP-Algorithms is a community-maintained online reference of algorithms and data structures oriented toward competitive programming. Each article covers the algorithm, its correctness argument, complexity analysis, and implementation notes, often with code in C++. The reference is particularly strong on implementation-level correctness details — exactly why counting sort must scan right-to-left for stability, and exactly why KMP's failure function depends only on the pattern and not on the text being searched.

## Why It Matters

- **Open access**: completely free; no registration.
- **Implementation precision**: articles address corner cases and stability requirements that high-level textbooks sometimes gloss over.
- **Strong coverage of**: KMP string matching, radix/counting sort stability, RLE compression, and graph shortest-path algorithms.
- **Regularly updated**: community corrections keep content accurate.

## Chunk Candidates

| Chunk Topic | Target Wiki Notes |
|---|---|
| Counting sort right-to-left pass preserves input order of equal keys | [[Counting Sort]], [[Radix Sort]] |
| Radix sort LSD-first correctness relies on stability of each digit pass | [[Radix Sort]] |
| KMP failure function is computed on the pattern alone, independent of text | [[String Matching - KMP]] |
| RLE effective only when expected run length exceeds 2; used in fax and BMP | [[Run-Length Encoding]] |

## Related Wiki Notes

- [[Counting Sort]] — right-to-left stability mechanism
- [[Radix Sort]] — LSD-first correctness via stability
- [[String Matching - KMP]] — pattern-only failure function
- [[Run-Length Encoding]] — run-length threshold and real-world file formats
- [[LZW Compression]] — patent history context

## Chunks Created This Wave

- [[Sorting - Counting sort right-to-left pass preserves input order of equal keys ensuring stability]] (chunk-csa-045)
- [[Sorting - Radix sort LSD-first correctness relies on the stability of each digit-sort pass]] (chunk-csa-046)
- [[Strings - KMP failure function is computed on the pattern alone and is independent of the text]] (chunk-csa-047)
- [[Compression - Run-length encoding is effective only when expected run length exceeds two symbols]] (chunk-csa-049)
