# AI Usage Log

## Task 7 — LangChain

**Tool:** Antigravity (AI coding assistant)

### What AI was used for
- Scaffolding `part_a_extract.py`: Pydantic `SupportTicket` schema (field names and `Literal` values taken from my Task 4 `labels.json`), the LCEL chain `ChatPromptTemplate | llm.with_structured_output(...)`, the single `.batch()` call, writing `predictions.jsonl`, and reusing my unchanged Task 4 `evaluate.py` for scoring.
- Writing `inspect_structured_output()` to capture the bound tool schema / `tool_choice` and the raw `AIMessage.tool_calls` (saved to `structured_output_evidence.txt`).
- Scaffolding `part_b_rag.py`: document loading with `source` metadata, `RecursiveCharacterTextSplitter`, `HuggingFaceEmbeddings`, `InMemoryVectorStore` retriever (k=3), the citation-enforcing prompt, the two chunk-size runs and the hit@3 calculation.
- Setting up the virtual environment / `requirements.txt` and generating empty templates for `langchain-notes.md` and this file.
