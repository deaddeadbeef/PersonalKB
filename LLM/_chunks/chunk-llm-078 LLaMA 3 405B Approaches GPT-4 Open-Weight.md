---
tags: [chunk, llm]
id: "chunk-llm-078"
source: "[[LLM/_raw/raw-llm-020 Llama 3 Herd of Models]]"
source_loc: "Key Takeaways 2"
topic: "LLaMA 3 frontier performance"
claim: "LLaMA 3 405B approached GPT-4 level performance while being open-weight, narrowing the open-closed capability gap."
confidence: "verified"
supports: ["[[LLM/History and Landscape/Open-Weight Model Ecosystem]]"]
up: "[[LLM/LLM]]"
---

# LLaMA 3 405B Approaches GPT-4 Open-Weight

## Context
LLaMA 3 405B achieved benchmark scores competitive with GPT-4 and Claude 3.5 Sonnet across major evaluation suites including MMLU, HumanEval, GSM8K, and MATH. On some benchmarks it matched or exceeded these closed models, while on others it trailed by small margins. This was the first time an open-weight model had reached parity with the frontier closed models on a broad set of evaluations.

The 405B model is a dense transformer (not MoE), making it expensive to serve but straightforward to understand and fine-tune. Meta released the full model weights, enabling the community to study, fine-tune, distill, and quantize a frontier-capable model for the first time. This transparency was in stark contrast to the closed approach taken by OpenAI and Google for their comparable models.

## Why It Matters
LLaMA 3 405B proved that the open-weight approach could produce frontier-quality models. This narrowing of the open-closed gap has strategic implications: organizations can now choose between API-based access to proprietary models and self-hosting comparable open models. It validated Meta's strategy of investing in open models and put competitive pressure on closed providers to demonstrate value beyond raw capability.

## QnA Seeds
- Q: How did LLaMA 3 405B compare to GPT-4 on benchmarks?
  A: It achieved competitive scores on major evaluations (MMLU, HumanEval, GSM8K, MATH), matching or exceeding GPT-4 and Claude 3.5 Sonnet on some benchmarks while trailing by small margins on others. It was the first open-weight model to reach approximate parity with frontier closed models across a broad evaluation suite.
- Q: Why is LLaMA 3 405B's performance significant for the open-weight ecosystem?
  A: It proved open-weight models can match frontier quality, giving organizations a real choice between proprietary APIs and self-hosted models. It validated Meta's open strategy, enabled community study of a frontier-capable model, and put competitive pressure on closed providers.
