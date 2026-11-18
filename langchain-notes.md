# Task 7 — LangChain Notes

> Stack: `langchain` 1.5.0 · `langchain-core` 1.8.2 · `langchain-groq` 1.2.0 · `langchain-huggingface` 1.2.3 · `langchain-text-splitters` 1.1.3
> Model: Groq `openai/gpt-oss-120b`, `temperature=0`, via `init_chat_model`

---

## 1. Theory Questions

> ⚠️ Written by me without AI assistance.

### Q1. A unit of work that can be invoked, batched, streamed, transformed and composed.

### Q2. chains components together by passing the output of the left component as the input to the right component


### Q3. invoke It takes a single input and produces the result all at once. batch Passing a list of inputs and executing them in parallel  stream To receive the outputs gradually

### Q4. does not always guarantee valid output by default depends on your LLM provider

### Q5. langchan for the linear task DAG as RAG a stack tasks for lops that need to check tools and re do task use langgraph

---

## 2. Pure Python (Task 4 / Task 5) vs. LangChain (Task 7)
| Metric | Pure Python (Task 4 / 5) | LangChain (Task 7) |
| --- | --- | --- |
| `customer_name` | 95.0% | 95.0% |
| `order_ids` | 100.0% | 100.0% |
| `product` | 65.0% | 90.0% |
| `issue_type` | 95.0% | 95.0% |
| `wants_refund` | 95.0% | 95.0% |
| `urgency` | 95.0% | 95.0% |
| `language` | 95.0% | 100.0% |
| Extraction Avg | 91.4% | 95.7% |
| RAG Correct (/12) | (not recorded in Task 5) | (grade `rag_results.md` by hand) |
| hit@3 | 60% (`500/50`) | 100% (`10/10`) at `1000/200` & `500/50` |
| Lines of Code | 130 (`34` extract + `96` RAG) | 337 (`205` extract + `132` RAG) |
---

### 3 things LangChain automated for me

1. [Structured JSON]
2. [Batch Concurrency]
3. [Chunking and vector search]

### 1 thing LangChain hid / made harder

using the combo of .invoke() and .batch()

### Final engineering verdict

[TODO: when would I use LangChain vs. plain Python in a real project, and why]
