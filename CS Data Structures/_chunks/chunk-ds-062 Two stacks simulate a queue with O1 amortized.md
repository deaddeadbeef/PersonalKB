---
tags: [cs-ds, chunk]
id: chunk-ds-062
source: "[[raw-ds-003]]"
supports: ["[[Stacks and Queues]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Two stacks simulate a queue with O1 amortized per operation

## Context
Stacks support LIFO and queues support FIFO. Can one simulate the other?

## Claim
Using an inbox and outbox stack: enqueue pushes to inbox. Dequeue pops from outbox. When outbox empty reverse inbox into outbox. Each element is moved at most twice giving O(1) amortized.

## Why It Matters
Classic interview problem but also practical: some concurrent systems implement queues this way.

## QnA Seeds
- Q: Why amortized O(1)? -> A: Each element pushed and popped at most twice total.
- Q: When does the reversal happen? -> A: Only when outbox is empty and dequeue is called.
