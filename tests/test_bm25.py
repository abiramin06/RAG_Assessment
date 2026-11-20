from src.bm25_retriever import bm25_search

questions = [
    "casual leaves",
    "sick leaves",
    "salary payment",
    "office working hours",
    "planned leave notice"
]

for question in questions:

    print("\nQUESTION:", question)

    results = bm25_search(
        question,
        top_k=3
    )

    for rank, result in enumerate(results, start=1):

        print(
            f"Rank {rank} | "
            f"Source: {result['source']} | "
            f"Score: {result['bm25_score']:.4f}"
        )

        print("Text:", result["text"][:150])