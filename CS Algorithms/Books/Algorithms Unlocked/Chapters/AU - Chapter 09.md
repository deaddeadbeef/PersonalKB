---
id: au-ch-09
type: book-chapter
chapter: 9
book: "Algorithms Unlocked"
author: "Thomas H. Cormen"
status: processed
chunk_count: 3
source: "[[Cormen 2013 - Algorithms Unlocked]]"
tags:
  - csa
  - book-chapter
up: "[[CS Algorithms/Books/Algorithms Unlocked/Chapter Index|Chapter Index]]"
confidence: established
freshness: stable
tier-coverage: [core]
---
# AU — Chapter 09: Data Compression

## Summary

Chapter 9 asks: if the previous chapter was about hiding information, how do we shrink it? The focus is entirely on **lossless** compression — perfect reconstruction guaranteed. Compression is possible because real data is redundant: ASCII wastes 1 bit per character (the high bit is always 0); English text has strongly non-uniform character frequencies, so variable-length codes (shorter codes for 'e', longer for 'z') can shrink text significantly. For variable-length codes to be unambiguously decodable, no codeword may be a prefix of another — this is the **prefix-free** property, represented by a binary tree where each leaf is a symbol and its root-to-leaf path spells the codeword. **Huffman coding** is a greedy algorithm that builds the *optimal* such tree: maintain a min-priority queue of nodes keyed by frequency; repeatedly merge the two lowest-weight nodes into a new parent node. After n−1 merges the single remaining root is the Huffman tree. Time $\Theta(n \lg n)$. No prefix-free code assigns shorter expected codeword length than Huffman for a given frequency distribution. **Run-length encoding (fax compression)** encodes long runs of same-colour pixels as (colour, length) pairs — practical for black-and-white document images. **LZW compression** builds a shared codebook dynamically: encoder and decoder start with the same initial dictionary and update it identically as they process data, so no dictionary needs to be transmitted. Strong on repetitive data (source code, genomic sequences); used in GIF images.

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| Lossless compression | Perfect reconstruction guaranteed; no information lost |
| Variable-length code | Frequent symbols get shorter codewords |
| Prefix-free code | No codeword is a prefix of another; uniquely decodable |
| Code tree | Binary tree where leaves = symbols; root-to-leaf path = codeword |
| Huffman algorithm | Greedy bottom-up build from min-priority queue; optimal prefix-free code |
| Run-length encoding | Encode (colour, run-length) pairs; effective on document images |
| LZW | Dynamic dictionary; encoder and decoder build codebook in sync; no header needed |

## Chunk Candidates

- [x] [[Compression - Huffman coding builds the optimal prefix-free code with a greedy merge]]
- [x] [[Compression - LZW builds a shared codebook dynamically requiring no transmitted dictionary]]
- [x] [[Compression - Run-length encoding encodes same-symbol runs as count-symbol pairs]]

## Wiki Pages Seeded

- [[Data Compression Overview]] — motivation, variable-length codes, prefix-free codes, run-length encoding, LZW
- [[Huffman Coding]] — greedy optimal prefix-free code; optimality proof sketch
- [[Run-Length Encoding]] — count-symbol pair encoding; document image compression
- [[LZW Compression]] — adaptive dictionary; encoder and decoder build codebook in sync; no header needed

## References

See [[CS Algorithms/Sources/Sources Index#Cormen 2013|Cormen 2013]].
