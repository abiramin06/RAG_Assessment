from src.hybrid_retriever import hybrid_search
from src.reranker import rerank_chunks


questions = [
    "How many casual leaves are provided?",
    "How many sick leaves are provided?",
    "What is the salary payment date?",
    "What are the office working hours?",
    "How many days advance notice is required for planned leave?"
]


for question in questions:

    print("\nQUESTION:", question)

    candidates = hybrid_search(
        question,
        top_k=50
    )

    print("Candidates:", len(candidates))

    reranked = rerank_chunks(
        question,
        candidates,
        top_k=5
    )

    print("\nRERANKED TOP 5:")

    for rank, result in enumerate(reranked, start=1):

        print(
            rank,
            result["source"],
            "Score:",
            round(result["rerank_score"], 4)
        )