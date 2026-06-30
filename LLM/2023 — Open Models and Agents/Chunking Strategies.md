---
tags: [llm, rag]
up: "[[2023 — Open Models and Agents Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Chunking Strategies
> **One-line summary:** Chunking decides how documents are split for retrieval, and that choice strongly shapes RAG quality.

---

## 🎯 Intuition

### Core Idea
Chunking—breaking source documents into retrieval-friendly pieces—is one of the most consequential and underappreciated design decisions in a RAG system. The size, boundaries, and metadata of each chunk directly determine what the retriever can find and how much useful context the language model receives.

Raw documents are rarely the right unit for retrieval. A 50-page PDF retrieved whole would swamp the context window; a single sentence retrieved alone would lack surrounding context. Chunking carves documents into segments that balance two competing pressures: small enough to be precisely relevant to a query, large enough to carry self-contained meaning.

### Analogy
Chunking is like cutting a textbook into flashcards — too small loses context, too big can't find what you need.

### Why It Matters
Chunking is where information retrieval meets information loss. A poorly chunked corpus means the right answer exists in your data but the retriever can never surface it cleanly—either the relevant sentence is split across two chunks, or it's buried inside an oversized chunk alongside irrelevant text. Investing in chunking strategy often yields more improvement than upgrading the embedding model or adding a reranker.

---

## ⚙️ Core Mechanics

### How It Works
**Fixed-size chunking** is the simplest approach: split text every N tokens (or characters) with an overlap window of M tokens. Overlap ensures that information at chunk boundaries isn't lost. Typical settings range from 256–1024 tokens with 10–20% overlap. It's fast and deterministic but blind to document structure—a chunk boundary can land mid-sentence or mid-paragraph.

**Recursive chunking** respects document hierarchy. The splitter first tries to break on the largest structural element (section headings), then paragraphs, then sentences, then characters—stopping at whatever level produces chunks within the target size. This preserves logical units far better than fixed-size splitting.

**Semantic chunking** goes further: it embeds consecutive sentences, detects similarity breakpoints (where cosine similarity between adjacent sentence embeddings drops sharply), and splits there. The result is chunks that correspond to topic shifts rather than arbitrary boundaries.

**Parent-child chunking** indexes small chunks (e.g., 128 tokens) for precise retrieval but returns their larger parent chunk (e.g., 512 tokens) to the LLM, combining retrieval precision with generation context.

### Key Specifications
- **Fixed-size**: Split every N tokens with M-token overlap. Simple, fast, structure-agnostic.
- **Recursive**: Hierarchical splitting—headings → paragraphs → sentences → characters. Preserves document structure.
- **Semantic**: Embed sentences, compute rolling cosine similarity, split at drop-off points. Aligns chunks to topic boundaries.
- **Parent-child**: Index small chunks; at retrieval time, expand to the enclosing parent chunk before passing to the LLM.
- **Metadata enrichment**: Attach source title, section heading, page number, URL, and date to each chunk. Critical for citation and filtering.
- **Chunk size trade-off**: Smaller chunks → higher retrieval precision but less context per chunk. Larger chunks → more context but diluted relevance signal.
- **Overlap window**: Too little overlap → boundary information lost. Too much → redundant storage and retrieval noise.

### Key Facts
- Typical chunk sizes range from **256–1024 tokens** with **10–20% overlap**.
- The **"Lost in the Middle" effect** (Liu et al. 2023) means LLMs attend most to the beginning and end of the context window; information buried in the middle is disproportionately ignored.
- Chunk ordering in the assembled prompt matters because retrieval quality is not only about what is retrieved, but also where it appears in context.


| Strategy | Pros | Cons | Best For |
| --- | --- | --- | --- |
| Fixed-size | Simple, deterministic, fast | Ignores structure, mid-sentence splits | Homogeneous text (e.g., novels) |
| Recursive | Respects document hierarchy | Requires structural markers | Structured docs (Markdown, HTML) |
| Semantic | Topic-aligned boundaries | Slower (requires embedding pass) | Heterogeneous / long-form content |
| Parent-child | Precise retrieval + rich context | More complex indexing | Knowledge bases, documentation |

---

## 🔬 Deep Dive

### Technical Details
Chunking quality depends on more than length. Boundary choice, metadata, and prompt assembly all interact. Metadata enrichment makes later filtering and citation possible. Parent-child retrieval gives a system a way to search narrowly while answering broadly. Semantic chunking can detect topic shifts better than rule-based splitters, but it requires an extra embedding pass over the corpus.

The "Lost in the Middle" effect also means chunking and ranking should be considered together. Even a good chunk can become less useful if it is placed in the middle of a long assembled context where the model pays less attention.

### Limitations
Fixed-size chunking is cheap but structure-blind. Recursive chunking works best when source documents contain reliable headings or paragraphs. Semantic chunking improves topical coherence but adds compute and pipeline complexity. Parent-child schemes improve retrieval/generation balance but require more careful indexing and bookkeeping.

### Impact
Chunking is often a higher-leverage improvement than people expect. If the retrieval unit is wrong, even strong embeddings and rerankers are forced to work with damaged inputs. Good chunking raises both retrieval precision and downstream answer quality.

---

## 🏋️ Practice

### Warm-Up
1. Why is retrieving an entire 50-page PDF usually a bad idea for RAG?
2. What problem does overlap solve in fixed-size chunking?
3. When would recursive chunking usually beat fixed-size chunking?

### Core Problems
1. You are indexing a Markdown knowledge base with clear headings and paragraphs. Which chunking strategy is the best default, and why?
2. Your retriever keeps missing answers that sit right on chunk boundaries. What change would you try first?
3. You want precise retrieval but richer generation context. How does parent-child chunking help?

### Challenge
Design a chunking policy for a mixed corpus of PDFs, HTML docs, and wiki notes. Pick chunk sizes, overlap, metadata fields, and say when you would switch from recursive to semantic chunking.

---

## Supporting Chunks

### Supporting Chunks
- No supporting chunk notes are attached yet.

### See Also
- [[Tokenization]] — sub-word tokenization interacts with chunk boundaries
- [[Retrieval Pipelines and Context Assembly]] — chunking feeds retrieval pipelines
- [[KV Cache and Context Reuse]] — chunk size affects context window utilization
- [[Efficient Attention and Long-Context Variants]] — long-context models reduce chunking needs

## References
- [[LLM/Sources/Sources Index]]
