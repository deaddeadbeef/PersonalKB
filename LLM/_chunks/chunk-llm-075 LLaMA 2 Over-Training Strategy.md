---
tags: [chunk, llm]
id: "chunk-llm-075"
source: "[[LLM/_raw/raw-llm-019 LLaMA 2 Open Chat Models]]"
source_loc: "Key Takeaways 1"
topic: "LLaMA 2 training scale and over-training"
claim: "LLaMA 2 trained on 2T tokens (40% more than LLaMA 1), applying the over-training strategy for better inference economics."
confidence: "verified"
supports: ["[[LLM/Pretraining/Compute Data and Parameter Trade-offs]]"]
up: "[[LLM/LLM]]"
---

# LLaMA 2 Over-Training Strategy

## Context
LLaMA 2 was pretrained on 2 trillion tokens, a 40% increase over LLaMA 1's 1.4 trillion tokens. According to Chinchilla scaling laws, models of LLaMA 2's sizes (7B, 13B, 70B) would be compute-optimal with far fewer tokens. For instance, a 70B model is Chinchilla-optimal at approximately 1.4T tokens. By training on 2T tokens, LLaMA 2 deliberately "over-trained" relative to compute-optimality.

This over-training strategy reflects a key insight: Chinchilla-optimal is optimal for minimizing training cost, but not for minimizing total cost (training + inference). A smaller model trained on more data can match the quality of a larger model trained to Chinchilla-optimality, while being cheaper to serve. Since inference costs dominate for widely deployed models, investing extra training compute to get a smaller, better-trained model is economically rational even if it wastes some training FLOP budget.

## Why It Matters
LLaMA 2's over-training approach formalized the practical departure from Chinchilla-optimal ratios. It showed that real-world deployment economics — where inference costs dominate — justify spending more on training to get smaller, more efficient models. This principle has been embraced even more aggressively by LLaMA 3 (15T tokens) and other modern models.

## QnA Seeds
- Q: Why did LLaMA 2 train on more tokens than Chinchilla scaling laws would suggest?
  A: Chinchilla-optimal minimizes training cost but not total cost. Over-training produces a smaller, higher-quality model that's cheaper to serve at inference time. Since inference costs dominate for widely deployed models, investing extra training compute to improve the model beyond Chinchilla-optimal is economically rational.
- Q: How much more data did LLaMA 2 use compared to LLaMA 1?
  A: LLaMA 2 trained on 2T tokens, a 40% increase over LLaMA 1's 1.4T tokens. The context length was also extended from 2048 to 4096 tokens. Both changes contributed to improved model quality across benchmarks.
