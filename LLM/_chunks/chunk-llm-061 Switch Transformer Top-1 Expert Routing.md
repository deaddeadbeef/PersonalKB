---
tags: [chunk, llm]
id: "chunk-llm-061"
source: "[[LLM/_raw/raw-llm-016 Switch Transformers Trillion Parameter MoE]]"
source_loc: "Key Takeaways 1"
topic: "Switch Transformer top-1 routing"
claim: "Switch Transformer simplified MoE routing to top-1 (one expert per token), reducing communication and improving training stability."
confidence: "verified"
supports: ["[[LLM/Architecture Variants/Mixture-of-Experts Models]]"]
up: "[[LLM/LLM]]"
---

# Switch Transformer Top-1 Expert Routing

## Context
Prior Mixture-of-Experts models (like GShard) used top-2 routing, where each token is dispatched to its two highest-scoring experts and the results are combined. This required more inter-GPU communication (tokens sent to two experts instead of one) and introduced training instability from load balancing between two selections. Switch Transformer made the radical simplification of routing each token to exactly one expert (top-1 routing).

Despite the apparent loss of capacity from using one expert instead of two, top-1 routing proved superior in practice. It halved the communication cost (each token travels to one expert), simplified the gating computation, and improved training stability by reducing the optimization complexity. The Switch Transformer's gating function computes a softmax over expert scores and routes each token to its highest-scoring expert, with the gate value used to scale the expert's output.

## Why It Matters
The top-1 simplification was counterintuitive — less should be worse — but it demonstrated that in MoE, reducing routing complexity can improve both efficiency and quality. This insight shaped all subsequent MoE architectures: Mixtral, Grok, and DBRX all use top-K routing with small K values, and the focus shifted to making simple routing work well rather than engineering complex multi-expert combinations.

## QnA Seeds
- Q: How does Switch Transformer's routing differ from earlier MoE approaches?
  A: Switch Transformer routes each token to exactly one expert (top-1), while earlier models like GShard used top-2 routing (each token sent to two experts). Top-1 routing halves communication cost, simplifies gating, and improves training stability despite using fewer experts per token.
- Q: Why did top-1 routing outperform top-2 despite using fewer experts per token?
  A: Reduced communication overhead allowed more actual computation per unit of time, simpler gating meant fewer optimization difficulties, and the single expert still had access to the full expert capacity. The efficiency gains from simplification outweighed the theoretical capacity loss.
