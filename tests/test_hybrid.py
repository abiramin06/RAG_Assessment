from src.bm25_retriever import bm25_search
from src.vector_store import vector_search
from src.hybrid_retriever import hybrid_search


questions = [
    "casual leaves",
    "sick leaves",
    "salary payment",
    "office working hours",
    "planned leave notice",
    "medical certificate"
]


for question in questions:

    print("\nQUESTION:", question)

    bm25 = bm25_search(question, top_k=5)
    vector = vector_search(question, top_k=5)
    hybrid = hybrid_search(question, top_k=5)

    print("\nBM25 TOP 3:")
    for result in bm25[:3]:
        print(result["id"][:12], result["source"])

    print("\nVECTOR TOP 3:")
    for result in vector[:3]:
        print(result["id"][:12], result["source"])

    print("\nHYBRID TOP 3:")
    for result in hybrid[:3]:
        print(
            result["id"][:12],
            result["source"],
            "RRF:",
            round(result["rrf_score"], 5)
        )