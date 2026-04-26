---
tags: [llm, architecture]
up: "[[2020–2021 — The Scaling Era Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Mixture-of-Experts Models

> **MoE models increase total parameter count by activating only a small set of experts per token, keeping compute far lower than a dense model of the same total size.**

## 🎯 Intuition
**The Core Idea:** Instead of sending every token through the same feed-forward network, an MoE model routes each token to only the most relevant expert sub-networks.
**Analogy:** An MoE model is like a hospital with many specialist doctors—the receptionist routes each patient to the right one or two specialists instead of making every doctor examine every case.
**Why It Matters:** MoE is the architecture behind several frontier models, including Mixtral, DeepSeek-V3, and reportedly GPT-4. It offers a path to scaling model capacity without the proportional increase in inference cost, which matters because inference economics increasingly dominate LLM deployment. The trade-off is that all experts still need to be loaded into memory, and routing plus cross-device communication make the system more complex.

---

## ⚙️ Core Mechanics
### How It Works
- In a standard transformer, every token passes through the same feed-forward network (FFN) in each layer.
- In an MoE model, the FFN is replaced with multiple parallel "expert" FFNs, and a learned router determines which experts process each token.
- The router typically selects the top-k experts (k=1 or k=2) based on a softmax over routing scores.
- **Router network**: linear layer mapping hidden state → expert scores; softmax + top-k selection
- **Top-k routing**: typically k=1 (Switch) or k=2 (Mixtral); determines how many experts process each token
- **Load balancing loss**: auxiliary loss encouraging equal utilization of experts; prevents "expert collapse"
- **Capacity factor**: maximum tokens per expert per batch; overflow tokens get dropped or routed to a buffer
- **Expert parallelism**: distribute experts across GPUs; each GPU holds a subset of experts
- **All-to-all communication**: tokens routed across GPUs to reach their assigned experts
- **Total params vs active params**: Mixtral 8×7B has 47B total but ~13B active per token
- Switch Transformer (Fedus et al. 2021) simplified MoE by using top-1 routing (one expert per token) and showed it could scale to trillion-parameter models.
- Mixtral (Jiang et al. 2024) applied MoE to the Mistral architecture with 8 experts, 2 active per token, achieving near-GPT-3.5 quality with much lower inference cost.
- DeepSeek-MoE used fine-grained expert segmentation (many small experts rather than few large ones) for better load balancing.
- The key insight: a model with 8× the total parameters but 2× the active parameters gets most of the benefits of the larger model while keeping inference cost close to the smaller one.

### Key Specifications

| Aspect | Dense Model | MoE Model |
|--------|------------|-----------|
| Active params per token | All params | Top-k experts only |
| Memory | proportional to active compute | Much larger (all experts) |
| Inference FLOPs | Proportional to params | Proportional to active params |
| Training complexity | Standard | Router training, load balancing |
| Example | LLaMA 70B | Mixtral 8×7B |

### Key Facts
- MoE replaces dense FFNs with multiple expert FFNs plus a learned router.
- The most common routing choices are top-1 and top-2 expert selection per token.
- Mixtral 8×7B has about 47B total parameters but only about 13B active parameters per token.
- Load-balancing losses are necessary to stop the router from collapsing onto a small subset of experts.
- MoE reduces active compute per token, but it does not remove the need to keep all experts resident in memory.

---

## 🔬 Deep Dive
### Technical Details
- Sparse activation is the defining systems property of MoE—only a fraction of the model is "active" for any given input.
- The router computes routing scores from the token hidden state, applies a softmax, and selects the top-k experts for execution.
- Capacity limits matter because each expert can only accept a bounded number of tokens per batch; overflow tokens may be dropped or sent to a fallback buffer.
- Expert parallelism lets different GPUs host different experts, but then all-to-all communication becomes central to runtime efficiency.
- Fine-grained expert segmentation, as in DeepSeek-MoE, uses many smaller experts instead of a few larger ones to improve utilization and load balancing.

### Limitations and Criticisms
- Memory requirements remain high because all experts must still be loaded even though only a few are active per token.
- Training is more complicated than dense transformers because the router, load-balancing objective, and capacity constraints all need to work correctly.
- Distributed all-to-all communication can become a major bottleneck when tokens are routed across devices.

### Impact and Legacy
Switch Transformer showed MoE could scale to trillion-parameter regimes with top-1 routing. Mixtral demonstrated that open-weight MoE systems could deliver near-GPT-3.5 quality at substantially lower inference cost than dense models of similar total size. More broadly, MoE established a practical way to decouple total capacity from active compute, which is why it remains central to many state-of-the-art model designs.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why does replacing a dense FFN with multiple experts reduce active compute per token?
2. What is the router doing in an MoE layer?
3. Why is load balancing necessary in sparse expert models?

### Core Problems
1. Compare a dense 70B model with an MoE system that has much larger total parameter count but only top-2 experts active per token. Explain the trade-offs in compute, memory, and deployment complexity.
2. Design the routing behavior you would want for a production MoE model running across multiple GPUs, including how you would think about top-k choice, capacity factor, and overflow handling.

### Challenge
1. Explain why a model with 8× the total parameters but only 2× the active parameters can capture much of the benefit of a larger dense model, and analyze where communication, routing quality, and memory overhead may still erase those gains in practice.

*See also:* [[Transformer Architecture]] — MoE extends the standard transformer with sparse routing; [[Compute Data and Parameter Trade-offs]] — MoE decouples parameter count from compute cost; [[Open-Weight Model Ecosystem]] — open MoE models like Mixtral; [[Speculative Decoding]] — draft models can leverage MoE efficiency; [[Efficient Attention and Long-Context Variants]] — combining MoE with efficient attention

## Supporting Chunks / References
### Supporting Chunks
*(To be populated as chunks are created)*

### References
- [[LLM/Sources/Sources Index]]