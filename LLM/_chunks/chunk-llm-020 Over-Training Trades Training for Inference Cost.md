---
tags: [chunk, llm]
id: "chunk-llm-020"
source: "[[LLM/_raw/raw-llm-005 Training Compute-Optimal LLMs (Chinchilla)]]"
source_loc: "Section 4, Discussion"
topic: "over-training strategy"
claim: "Over-training (training smaller models longer than compute-optimal) trades training efficiency for lower inference cost — the LLaMA strategy"
confidence: "verified"
supports: ["[[LLM/Pretraining/Compute Data and Parameter Trade-offs]]"]
up: "[[LLM/LLM]]"
---

# Over-Training Trades Training Efficiency for Inference Cost

## Context

While compute-optimal training (Chinchilla scaling) minimizes loss for a given training budget, it doesn't account for inference costs. A compute-optimal 70B model achieves great loss per training FLOP, but serving it is expensive — each inference request requires a forward pass through all 70B parameters. In production, inference cost often dominates total cost of ownership because the model serves millions of requests over its lifetime.

Over-training deliberately trains a smaller model on more data than the Chinchilla-optimal ratio, accepting slightly worse training FLOP efficiency in exchange for a cheaper-to-serve model. LLaMA exemplified this strategy: LLaMA-7B was trained on 1T tokens (about 7× the compute-optimal ~140B), and LLaMA-65B on 1.4T tokens. The loss is marginally higher than a compute-optimal allocation would achieve, but the resulting models are much smaller and therefore cheaper and faster at inference time.

## Why It Matters

Over-training resolved the tension between optimal training and practical deployment. It acknowledged that training is a one-time cost but inference runs continuously. This insight was crucial for the open-source LLM ecosystem, where smaller models running on consumer hardware are far more valuable than massive models trapped in expensive data centers. The LLaMA, Mistral, and Phi model families all embrace over-training to various degrees.

## QnA Seeds
- Q: Why would you deliberately deviate from compute-optimal training?
  A: Compute-optimal training minimizes loss per training FLOP but ignores inference costs. If you plan to serve the model to millions of users, a smaller over-trained model (e.g., 7B trained on 1T tokens) costs far less per query than a compute-optimal larger model (e.g., 30B trained on 600B tokens), even though the training was less FLOP-efficient. Total cost of ownership = training cost + (inference cost × number of queries).
- Q: What are the diminishing returns of over-training?
  A: As you train a small model on increasingly more data, each additional token provides less loss improvement — the model approaches its capacity limit. A 7B model trained on 2T tokens is better than one trained on 1T, but the improvement from 2T to 4T is smaller. Eventually, no amount of additional data can compensate for the model's limited parameter count. At that point, only increasing model size can reduce loss further.
