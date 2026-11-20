import time

from src.hybrid_retriever import hybrid_search
from src.reranker import rerank_chunks


questions = [
    "How many casual leaves are provided?",
    "How many sick leaves are provided?",
    "What is the salary payment date?",
    "What are the office working hours?",
    "How many days advance notice is required?",
    "When is a medical certificate needed?",
    "What is the leave carry forward policy?",
    "What are employee attendance rules?",
    "What is the company's safety policy?",
    "What are employee responsibilities?"
]


for question in questions:

    print("\nQUESTION:", question)

    start = time.perf_counter()

    candidates = hybrid_search(
        question,
        top_k=50
    )

    retrieval_time = time.perf_counter() - start

    start = time.perf_counter()

    reranked = rerank_chunks(
        question,
        candidates,
        top_k=5
    )

    rerank_time = time.perf_counter() - start

    print("Candidates:", len(candidates))
    print("Final results:", len(reranked))
    print("Retrieval latency:", round(retrieval_time * 1000, 2), "ms")
    print("Reranking latency:", round(rerank_time * 1000, 2), "ms")