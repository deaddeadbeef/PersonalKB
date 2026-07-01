---
tags: [study, llm, drill]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: stable
tier-coverage: [practice]
---
# Alignment & Safety — Review Drill

## Quick-Fire Questions

1. **What are the three stages of the InstructGPT/RLHF pipeline?**
   (1) Supervised fine-tuning on demonstrations, (2) Reward model training on preference pairs, (3) PPO optimization against reward model with KL penalty.

2. **Why is the KL penalty needed in RLHF?**
   Prevents the policy from diverging too far from the SFT model, which would lead to reward hacking — exploiting the reward model rather than being genuinely helpful.

3. **How does DPO simplify RLHF?**
   Eliminates the reward model and PPO entirely. Uses a closed-form relationship between optimal policy and reward to train directly on preference pairs with binary cross-entropy loss.

4. **What is Constitutional AI?**
   Anthropic's approach: model self-critiques against a constitution (set of principles), revises its outputs, then trains on the revised data (RLAIF). Scales without human annotation.

5. **What is reward hacking?**
   The model finds ways to get high reward scores without actually being helpful — exploiting patterns in the reward model rather than satisfying the underlying human intent. Goodhart's law applied to RLHF.

6. **What is sycophancy in LLMs?**
   The model agrees with the user rather than being truthful — a failure mode where RLHF trains the model to tell people what they want to hear.

7. **GCG attack — what is it?**
   Gradient-based adversarial suffix generation (Zou et al. 2023). Optimizes a string appended to prompts that causes aligned models to comply with harmful requests.

8. **What are sparse autoencoders used for in mechanistic interpretability?**
   Decomposing superposed neural network activations into interpretable, monosemantic features. Each feature corresponds to a human-understandable concept.

9. **DPO vs RLHF — when might you prefer RLHF?**
   When you need online learning (policy generates its own data), more flexible reward modeling, or when preference data doesn't match the current policy distribution.

10. **What is the scalable oversight problem?**
    As AI systems become more capable, humans can't reliably evaluate their outputs. Constitutional AI and debate are attempts to use AI to help supervise AI.

11. **Where does alignment sit in the full training pipeline?**
    After broad pretraining and usually after SFT. Alignment/post-training shapes assistant behavior with preference data, reward models, DPO-style losses, or constitutional feedback; it does not replace corpus quality, retrieval grounding, or deployment policy. See [[LLM/Study/LLM Training Pipeline Map|LLM Training Pipeline Map]].

## References

- [[LLM/Study/LLM Study Index]]
- [[LLM/Sources/Sources Index]]
- [[LLM/LLM Book Reading Spine]]
