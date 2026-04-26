---
tags: [chunk, llm]
id: "chunk-llm-011"
source: "[[LLM/_raw/raw-llm-003 BERT Pre-training of Deep Bidirectional Transformers]]"
source_loc: "Section 3.1, cf. RoBERTa"
topic: "next sentence prediction"
claim: "Next Sentence Prediction (NSP) was later shown unnecessary by RoBERTa, which achieved better results without it"
confidence: "verified"
supports: ["[[LLM/History and Landscape/BERT and Encoder Lineage]]"]
up: "[[LLM/LLM]]"
---

# Next Sentence Prediction Shown Unnecessary

## Context

BERT's original pre-training included two objectives: Masked Language Modeling (MLM) and Next Sentence Prediction (NSP). NSP is a binary classification task where the model receives two segments and predicts whether the second segment follows the first in the original document (50% positive, 50% random negative). The motivation was to help the model understand inter-sentence relationships, which is important for tasks like natural language inference and question answering.

However, RoBERTa (Liu et al., 2019) systematically ablated BERT's design choices and found that removing NSP either matched or improved downstream performance. The likely explanation is that NSP is too easy — the model can often distinguish random pairs using topic mismatch rather than learning genuine discourse coherence. RoBERTa replaced the two-segment input with single, longer sequences, which increased the effective context and improved MLM training.

## Why It Matters

The NSP story is a cautionary tale about auxiliary pre-training objectives. What seemed like a theoretically motivated addition (learning sentence relationships) turned out to be unnecessary or even harmful. This finding influenced subsequent model designs — GPT-style models use no such auxiliary objective, and later encoder models like ALBERT replaced NSP with Sentence Order Prediction, a harder task that did provide measurable benefit.

## QnA Seeds
- Q: Why did RoBERTa achieve better results without Next Sentence Prediction?
  A: NSP was too easy a classification task — the model could distinguish random sentence pairs by topic alone without learning real discourse understanding. Removing NSP allowed the use of longer contiguous sequences, which improved MLM training by providing more context. The benefits of better MLM outweighed any marginal gains from NSP.
- Q: What replaced NSP in subsequent encoder models?
  A: ALBERT introduced Sentence Order Prediction (SOP), where both segments come from the same document but may be in reversed order. This is harder than NSP because the topics always match — the model must genuinely understand discourse ordering. Other models simply dropped the objective entirely, relying on MLM alone (RoBERTa) or replaced it with different pre-training tasks like replaced token detection (ELECTRA).
