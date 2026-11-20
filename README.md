Enterprise RAG – Company Knowledge Assistant

1. Project Overview

The Enterprise RAG (Retrieval-Augmented Generation) project is a document-based question-answering system that allows users to retrieve information from company documents and generate context-grounded answers.

The system uses document ingestion, text chunking, embeddings, vector search, hybrid retrieval, reranking, query rewriting, metadata filtering, and LLM-based answer generation.

It also includes citation validation and hallucination detection to improve answer reliability.

2. Project Objectives

- Load and process multiple document formats.
- Split documents into manageable text chunks.
- Generate embeddings for document chunks.
- Store embeddings in a Qdrant vector database.
- Retrieve relevant information using vector search and BM25.
- Combine retrieval results using Reciprocal Rank Fusion (RRF).
- Improve retrieval using cross-encoder reranking.
- Implement query rewriting and multi-query retrieval.
- Support metadata-based filtering.
- Manage context token budgets.
- Generate answers using an LLM.
- Validate citations and detect hallucinated answers.

3. Technologies Used

Technology| Purpose
Python| Core programming
FastAPI| API development
Qdrant| Vector database
Sentence Transformers| Embeddings
Cross-Encoder| Reranking
BM25| Keyword retrieval
Gemini API| LLM answer generation
OpenAI SDK| API integration
PyMuPDF| PDF extraction
python-docx| DOCX extraction
Pandas| Data processing
tiktoken| Token counting
pytest| Testing

4. Project Structure

RAG_Assessment/
│
├── data/
│   ├── pdf/
│   ├── docx/
│   └── csv/
│
├── src/
│   ├── loader.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── vector_store.py
│   ├── indexer.py
│   ├── retriever.py
│   ├── answer_generator.py
│   ├── query.py
│   ├── token_budget.py
│   ├── bm25_retriever.py
│   ├── hybrid_retriever.py
│   ├── reranker.py
│   ├── query_rewriter.py
│   └── multi_query_retriever.py
│
├── tests/
│
├── results/
│   ├── chunks.json
│   └── manifest.json
│
├── evaluation/
│
├── qdrant_db/
├── main.py
├── requirements.txt
├── .env
└── README.md

5. Document Ingestion Pipeline

The ingestion pipeline performs the following operations:

1. Load PDF, DOCX, and CSV documents.
2. Extract document text and metadata.
3. Split extracted text into chunks.
4. Generate embeddings using Sentence Transformers.
5. Store embeddings and metadata in Qdrant.
6. Save chunk information and document manifest.

Dataset

- Total files: 50
- Documents loaded: 160
- Total chunks: 460
- Skipped files: 0

6. Retrieval Techniques

Vector Search

Uses semantic embeddings and cosine similarity to retrieve relevant chunks.

BM25 Search

Uses keyword-based ranking to retrieve documents based on query terms.

Hybrid Search

Combines vector search and BM25 results using Reciprocal Rank Fusion (RRF).

Cross-Encoder Reranking

Reranks retrieved candidates based on query-document relevance.

Query Rewriting

Generates alternative versions of the original query to improve retrieval.

Multi-Query Retrieval

Combines results from multiple rewritten queries using RRF.

Metadata Filtering

Filters retrieved chunks using metadata such as department and topic.

7. Context Management

The context management module:

- Counts tokens using tiktoken.
- Applies a configurable context budget.
- Selects retrieved chunks within the token limit.
- Prevents excessive context from being sent to the LLM.

8. Answer Generation

The answer generation module uses the Gemini API through an OpenAI-compatible client.

The system:

- Generates answers using retrieved context.
- Restricts answers to the supplied context.
- Provides source citations.
- Returns a fallback response when sufficient information is unavailable.

9. Evaluation and Validation

The project includes tests for:

- BM25 retrieval
- Vector retrieval comparison
- Hybrid retrieval
- Reranking
- Reranking latency
- Query rewriting
- Metadata filtering
- Qdrant metadata
- Context token budgeting
- Citation validation
- Filtered answer generation
- Hallucination detection

Hallucination Detection Results

Metric| Result
Total questions| 10
Passed| 10
Failed| 0
Pass rate| 100%

This result is from the standalone hallucination detection test.

The complete pytest suite and final evaluation are still to be verified.

10. Installation

Clone or copy the project and install dependencies:

pip install -r requirements.txt

Configure your ".env" file:

GEMINI_API_KEY=your_api_key

Do not commit API keys or other secrets.

11. Run the Project

Run document ingestion

python -m src.indexer

Run the application

python main.py

Run individual tests

python -m tests.test_hallucination_detection
python -m tests.test_citation_validator
python -m tests.test_metadata_filter
python -m tests.test_hybrid
python -m tests.test_reranker

12. Conclusion

This project demonstrates the implementation of an enterprise document-based Retrieval-Augmented Generation system.

It combines semantic search, keyword search, hybrid retrieval, reranking, query rewriting, metadata filtering, context management, and LLM-based answer generation.

Citation validation and hallucination detection help improve the reliability and trustworthiness of generated answers.

Project: Enterprise RAG – Company Knowledge Assistant
Assessment: Week 7 – RAG Implementation and Evaluation