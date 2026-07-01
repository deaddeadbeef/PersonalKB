---
tags: [cs-algorithms, techniques, streaming]
up: "[[Techniques Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, practice]
---

# Streaming Algorithms

> **One-line summary** Streaming algorithms process data in one pass or a small number of passes while using much less memory than the input size.

## Intuition

A streaming algorithm assumes the input is too large, too fast, or too remote to store in full. The algorithm reads each item as it arrives and maintains a compact summary. The central tradeoff is accuracy versus memory: exact answers may be impossible in tiny space, but approximate answers can be extremely useful.

Examples include counting distinct items with HyperLogLog, estimating item frequencies with Count-Min Sketch, and filtering set membership with Bloom filters. These structures sacrifice perfect detail in exchange for bounded memory and predictable update time.

## Core Patterns

- **Sketches:** compact summaries that approximate counts, frequencies, or cardinalities.
- **Reservoir sampling:** keep a uniform sample from a stream of unknown length.
- **Sliding windows:** summarize only recent items rather than the whole stream.
- **One-sided error filters:** allow false positives while preventing false negatives, as in Bloom filters.

## Why It Matters

Streaming algorithms are common in telemetry systems, network monitoring, databases, search engines, fraud detection, and observability pipelines. They answer questions such as "how many unique users?", "which keys are heavy hitters?", and "have we probably seen this item before?" without storing the full event log.

## Practice

1. Explain why exact distinct counting needs memory proportional to the number of distinct items.
2. Compare Count-Min Sketch and HyperLogLog by the question each one answers.
3. Describe one operational risk of using an approximate streaming summary.

## References

- [[CS Data Structures/Hash-Based Structures/Count-Min Sketch]]
- [[CS Data Structures/Hash-Based Structures/HyperLogLog]]
- [[CS Data Structures/Hash-Based Structures/Bloom Filters and Probabilistic Structures]]
