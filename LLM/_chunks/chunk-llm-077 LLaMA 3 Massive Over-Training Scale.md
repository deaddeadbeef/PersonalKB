---
tags: [chunk, llm]
id: "chunk-llm-077"
source: "[[LLM/_raw/raw-llm-020 Llama 3 Herd of Models]]"
source_loc: "Key Takeaways 1"
topic: "LLaMA 3 training scale"
claim: "LLaMA 3 trained on 15T+ tokens — over 7× more than LLaMA 2, massively over-training relative to Chinchilla-optimal."
confidence: "verified"
supports: ["[[LLM/Pretraining/Compute Data and Parameter Trade-offs]]"]
up: "[[LLM/LLM]]"
---

# LLaMA 3 Massive Over-Training Scale

## Context
LLaMA 3 was pretrained on over 15 trillion tokens — a 7.5× increase over LLaMA 2's 2T tokens and more than 10× what Chinchilla scaling laws would prescribe as compute-optimal for its model sizes. Even the 8B model was trained on 15T tokens, representing an extreme degree of over-training where the training compute budget is far beyond what would be efficient for minimizing per-token loss at that model size.

This aggressive over-training strategy reflected Meta's conviction that inference economics dominate: it's better to invest heavily in training a smaller model to be as good as possible, because the per-inference cost savings compound massively across billions of API calls and user interactions. The 8B model trained on 15T tokens achieved quality that would have required a much larger (and more expensive to serve) Chinchilla-optimal model.

## Why It Matters
LLaMA 3's 15T token training dataset represents the most aggressive over-training in the open-weight ecosystem. It proved that massive over-training works — the 8B model matched LLaMA 2 70B on several benchmarks despite being 8× smaller. This has profound implications for deployment: inference of an 8B model is dramatically cheaper than a 70B model, so the extra training compute pays for itself quickly at scale.

## QnA Seeds
- Q: How much training data did LLaMA 3 use compared to LLaMA 2 and Chinchilla-optimal?
  A: LLaMA 3 used 15T+ tokens — 7.5× more than LLaMA 2's 2T tokens and over 10× the Chinchilla-optimal amount for its model sizes. Even the small 8B model was trained on the full 15T tokens, representing extreme over-training.
- Q: What practical benefit does LLaMA 3's extreme over-training provide?
  A: The 8B model matches LLaMA 2 70B quality on several benchmarks while being 8× smaller and dramatically cheaper to serve. The extra training investment pays for itself through inference savings — a principle that becomes more valuable as deployment scale increases.
