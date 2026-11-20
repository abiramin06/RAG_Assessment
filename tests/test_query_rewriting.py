import time

from src.hybrid_retriever import hybrid_search
from src.multi_query_retriever import multi_query_search


questions = [
    "How many casual leaves are provided?",
    "What happens when an employee becomes ill?",
    "How early should someone request planned leave?",
    "What proof is needed for extended illness?",
    "What are the office working hours?"
]


for question in questions:

    print("\nQUESTION:", question)

    # Original hybrid search
    start = time.perf_counter()

    baseline = hybrid_search(
        question,
        top_k=3
    )

    baseline_time = time.perf_counter() - start

    # Query rewriting + RRF
    start = time.perf_counter()

    rewritten = multi_query_search(
        question,
        top_k=3
    )

    rewrite_time = time.perf_counter() - start

    print("\nBASELINE TOP 3:")

    for result in baseline:
        print(result["source"])

    print("\nQUERY REWRITING TOP 3:")

    for result in rewritten:
        print(result["source"])

    print("\nLATENCY COMPARISON")

    print("Baseline:", round(baseline_time * 1000, 2), "ms")
    print("Rewriting:", round(rewrite_time * 1000, 2), "ms")