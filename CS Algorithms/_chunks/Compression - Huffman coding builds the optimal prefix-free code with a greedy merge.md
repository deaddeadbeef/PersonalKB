---
id: chunk-csa-019
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 9"
topic: "compression"
claim: "Huffman coding builds an optimal prefix-free code by greedily merging the two lowest-frequency nodes in Theta(n lg n)"
confidence: verified
supports:
  - "[[Huffman Coding]]"
  - "[[Data Compression Overview]]"
tags:
  - csa
  - csa/compression
  - chunk
up: "[[CS Algorithms]]"
---
# Compression — Huffman coding builds the optimal prefix-free code with a greedy merge

## Context

Huffman algorithm: create n leaf nodes each weighted by symbol frequency; insert all into a min-priority queue. Repeat n−1 times: extract the two minimum-weight nodes x and y, create a new internal node z with weight x.weight + y.weight and children x, y, insert z back. The final extracted node is the Huffman tree root. Assign 0/1 to left/right edges; each leaf's root-to-leaf path is its codeword. Time Θ(n lg n) — dominated by n−1 heap operations. Optimality proof: an exchange argument shows that any other prefix-free code can be transformed into the Huffman code without increasing total encoding length.

## Why It Matters

Huffman coding is used in DEFLATE (gzip, ZIP, PNG), JPEG entropy coding, and the ITU fax standard. It is also a clean example of a greedy algorithm with a provable optimality guarantee — not all greedy algorithms are optimal, but Huffman's is, and the proof structure is instructive.

## QnA Seeds

- Q: What data structure does Huffman coding use and why?
- Q: Why is Huffman coding provably optimal among prefix-free codes?
- Q: What are the limitations of Huffman coding compared to LZW?
