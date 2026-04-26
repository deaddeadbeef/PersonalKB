---
tags: [cs-ds, raw]
source_type: textbook_chapter
source_title: "Arrays and Contiguous Memory"
authors: [Pat Morin]
year: 2013
up: "[[Sources Index]]"
---

# Arrays and Contiguous Memory

## Summary

Arrays store elements in contiguous memory locations, providing O(1) random access via index arithmetic (base + offset * element_size). Dynamic arrays use geometric resizing (typically 2x) to achieve amortized O(1) append. Arrays offer excellent cache performance due to spatial locality but suffer from O(n) insertion and deletion in the middle.

## Key Claims

1. Contiguous memory enables O(1) random access via base address arithmetic
2. Geometric resizing achieves amortized O(1) append despite occasional O(n) copies
3. Arrays provide superior cache performance over linked structures due to spatial locality
4. Dynamic arrays waste at most half their allocated memory at any time
5. Middle insertions require shifting O(n) elements

## Atomic Facts

1. Array access: base_address + index * sizeof(element)
2. Typical growth factor: 2x (Java ArrayList, C++ vector)
3. Amortized analysis: n appends cost O(n) total, so O(1) each
4. Cache line: typically 64 bytes on modern CPUs
5. Python list, Java ArrayList, C++ std::vector are all dynamic arrays
6. Some implementations shrink when load drops below 25%

## Significance

Arrays are the most fundamental data structure, underpinning nearly all other structures and providing the baseline for performance comparison.

## Chunks Extracted

*Pending*
