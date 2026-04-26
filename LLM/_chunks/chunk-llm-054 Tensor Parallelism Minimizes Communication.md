---
tags: [chunk, llm]
id: "chunk-llm-054"
source: "[[LLM/_raw/raw-llm-014 Megatron-LM Model Parallelism]]"
source_loc: "Key Takeaways 2"
topic: "Tensor parallelism communication efficiency"
claim: "Tensor parallelism splits the column-parallel and row-parallel linear layers to minimize communication: only two all-reduces per layer."
confidence: "verified"
supports: ["[[LLM/Pretraining/Training Infrastructure and Parallelism]]"]
up: "[[LLM/LLM]]"
---

# Tensor Parallelism Minimizes Communication

## Context
The critical challenge in model parallelism is minimizing inter-GPU communication, which can easily become the bottleneck. Megatron-LM's tensor parallelism achieves this through a clever pairing of column-parallel and row-parallel linear layers. In the forward pass, the column-parallel first layer requires no communication (each GPU independently computes its output columns), and only the row-parallel second layer requires an all-reduce to sum partial results. This gives exactly one all-reduce per MLP block and one per attention block — two per transformer layer total.

In the backward pass, the complementary all-reduce operations occur (one in each sub-layer but in the opposite direction — all-reduce of gradients). The total communication volume per layer is 2 × (number of activations) × (bytes per element), which scales with hidden size but not with the number of GPUs. On high-bandwidth interconnects like NVLink within a node, this overhead is small relative to the computation, enabling near-linear scaling.

## Why It Matters
The two-all-reduce-per-layer design is what makes tensor parallelism practical. With NVLink providing 600+ GB/s between GPUs within a node, the communication overhead for a layer with a few thousand hidden dimensions is microseconds — negligible compared to the matrix multiplications. This efficiency is why tensor parallelism is always used within a node (where bandwidth is high) while pipeline parallelism handles the inter-node dimension.

## QnA Seeds
- Q: Why does Megatron-LM's tensor parallelism need only two all-reduces per transformer layer?
  A: The column-parallel/row-parallel pairing means the first linear layer's outputs don't need synchronization (each GPU computes independent columns), and only the second layer's row-parallel reduction requires an all-reduce. One all-reduce for the MLP block and one for the attention block gives exactly two per layer.
- Q: Why is tensor parallelism typically used within a single node rather than across nodes?
  A: Because it requires high-bandwidth communication (all-reduce after each layer). Within a node, NVLink provides 600+ GB/s, making the two all-reduces per layer negligible. Across nodes, interconnect bandwidth is much lower, so pipeline parallelism (which communicates less frequently) is preferred.
